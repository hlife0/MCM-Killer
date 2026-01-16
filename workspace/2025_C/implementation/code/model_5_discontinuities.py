#!/usr/bin/env python3
"""
Model 5: Structural Performance Discontinuities (Breakpoint + SCM/DiD)
Based on: output/model_design.md
Translated by: @code_translator

This model detects structural performance breaks in country-sport trajectories
and estimates discontinuity magnitudes using synthetic control or DiD.
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.optimize import minimize
from statsmodels.stats.multitest import multipletests
import ruptures as rpt
import pickle
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)


# Sport cluster mapping
SPORT_CLUSTERS = {
    'Swimming': 'Aquatics', 'Diving': 'Aquatics', 'Water Polo': 'Aquatics',
    'Judo': 'Combat', 'Wrestling': 'Combat', 'Boxing': 'Combat',
    'Taekwondo': 'Combat', 'Fencing': 'Combat',
    'Artistic Gymnastics': 'Gymnastics', 'Rhythmic Gymnastics': 'Gymnastics',
    'Athletics': 'Athletics',
    'Tennis': 'Racket', 'Table Tennis': 'Racket', 'Badminton': 'Racket',
    'Rowing': 'Water_other', 'Canoe': 'Water_other', 'Sailing': 'Water_other',
    'Weightlifting': 'Weight', 'Archery': 'Target', 'Shooting': 'Target'
}


def load_sport_features(path: str = 'implementation/data/features_sport.csv') -> pd.DataFrame:
    """Load sport-level feature data."""
    df = pd.read_csv(path)

    # Map sports to clusters
    df['sport_cluster'] = df['sport'].map(SPORT_CLUSTERS).fillna('Other')

    # Handle missing values
    df['sport_medals'] = df['sport_medals'].fillna(0)

    print(f"Loaded sport features: {df.shape}")
    return df


def prepare_time_series(df: pd.DataFrame, min_observations: int = 5) -> dict:
    """
    Prepare time series for breakpoint detection.

    Args:
        df: Sport feature DataFrame
        min_observations: Minimum observations for time series

    Returns:
        Dictionary of time series by (noc, sport_cluster)
    """
    # Aggregate to noc-sport_cluster-year level
    df_agg = df.groupby(['noc', 'sport_cluster', 'year'])['sport_medals'].sum().reset_index()

    # Create time series for each noc-cluster
    time_series = {}

    for noc in df_agg['noc'].unique():
        for cluster in df_agg['sport_cluster'].unique():
            ts = df_agg[(df_agg['noc'] == noc) & (df_agg['sport_cluster'] == cluster)].copy()
            ts = ts.sort_values('year')

            if len(ts) >= min_observations:
                key = (noc, cluster)
                time_series[key] = {
                    'years': ts['year'].values,
                    'medals': ts['sport_medals'].values,
                    'n_obs': len(ts)
                }

    print(f"   Created {len(time_series)} time series (>= {min_observations} obs)")
    return time_series


def detect_breakpoint_pelt(time_series: np.ndarray, penalty: float = 5.0) -> int:
    """
    Detect single breakpoint using PELT algorithm.

    Args:
        time_series: Array of medal counts
        penalty: Penalty for breakpoint (BIC-like)

    Returns:
        Index of breakpoint (or None if no break detected)
    """
    if len(time_series) < 6:
        return None

    try:
        # Use ruptures library for change point detection
        algo = rpt.Pelt(model="rbf").fit(time_series)
        breakpoints = algo.predict(pen=penalty)

        # Return the first breakpoint (excluding end)
        if len(breakpoints) > 1:
            bp = breakpoints[0] - 1  # Convert to index
            if 0 < bp < len(time_series) - 1:
                return bp
    except Exception:
        pass

    return None


def detect_breakpiece_chow(years: np.ndarray, medals: np.ndarray, min_obs: int = 3) -> tuple:
    """
    Detect structural break using Chow test approximation.

    Args:
        years: Array of years
        medals: Array of medal counts
        min_obs: Minimum observations per segment

    Returns:
        (breakpoint_idx, f_statistic)
    """
    if len(medals) < 6:
        return None, 0

    best_f = 0
    best_bp = None

    # Try each potential breakpoint
    for bp in range(min_obs, len(medals) - min_obs):
        # Split data
        y1, y2 = medals[:bp], medals[bp:]
        x1, x2 = np.arange(len(y1)), np.arange(len(y2))

        if len(y1) < 2 or len(y2) < 2:
            continue

        try:
            # Fit separate linear models
            coef1 = np.polyfit(x1, y1, 1)
            coef2 = np.polyfit(x2, y2, 1)

            # Fit pooled model
            x_all = np.arange(len(medals))
            coef_pooled = np.polyfit(x_all, medals, 1)

            # Calculate RSS
            rss1 = np.sum((y1 - np.polyval(coef1, x1))**2)
            rss2 = np.sum((y2 - np.polyval(coef2, x2))**2)
            rss_pooled = np.sum((medals - np.polyval(coef_pooled, x_all))**2)

            # Chow test F-statistic
            k = 2  # parameters (slope + intercept)
            n = len(medals)

            if (n - 2*k) > 0:
                f_stat = ((rss_pooled - (rss1 + rss2)) / k) / ((rss1 + rss2) / (n - 2*k))

                if f_stat > best_f:
                    best_f = f_stat
                    best_bp = bp

        except Exception:
            continue

    # Critical value at alpha=0.05
    if best_f > 4.0:
        return best_bp, best_f

    return None, best_f


def estimate_break_effect(medals: np.ndarray, bp: int) -> float:
    """
    Estimate the magnitude of a break.

    Args:
        medals: Medal count time series
        bp: Breakpoint index

    Returns:
        Estimated effect size (difference in means post vs pre)
    """
    if bp is None or bp <= 0 or bp >= len(medals):
        return 0

    pre_mean = medals[:bp].mean()
    post_mean = medals[bp:].mean()

    return post_mean - pre_mean


def build_synthetic_control(treated_unit: np.ndarray,
                           donor_pool: pd.DataFrame,
                           pre_period: slice) -> dict:
    """
    Build synthetic control for treated unit.

    Args:
        treated_unit: Time series for treated country-sport
        donor_pool: DataFrame with donor time series
        pre_period: Slice for pre-treatment period

    Returns:
        Dictionary with synthetic control weights and results
    """
    # Get pre-treatment data
    treated_pre = treated_unit[pre_period]

    # Get donor pre-treatment data
    donor_pre = donor_pool.iloc[pre_period].values.T  # Transpose for optimization

    # Number of donors
    n_donors = donor_pre.shape[1]

    if n_donors == 0:
        return {'success': False, 'error': 'No donors available'}

    # Optimization: minimize ||X_treated - X_donors * w||^2
    # subject to sum(w) = 1, w >= 0

    def objective(weights):
        synthetic = np.dot(donor_pre, weights)
        return np.sum((treated_pre - synthetic)**2)

    # Initial weights (equal)
    w0 = np.ones(n_donors) / n_donors

    # Constraints: sum(w) = 1
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

    # Bounds: w >= 0
    bounds = [(0, 1) for _ in range(n_donors)]

    try:
        result = minimize(objective, w0, bounds=bounds,
                         constraints=constraints, method='SLSQP')

        if result.success:
            weights = result.x

            # Create synthetic control for all periods
            donor_all = donor_pool.values.T
            synthetic_all = np.dot(donor_all, weights)

            return {
                'success': True,
                'weights': weights,
                'synthetic': synthetic_all,
                'donor_ids': donor_pool.columns.tolist()
            }
        else:
            return {'success': False, 'error': 'Optimization failed'}

    except Exception as e:
        return {'success': False, 'error': str(e)}


def did_estimator(treated_pre: np.ndarray, treated_post: np.ndarray,
                  control_pre: np.ndarray, control_post: np.ndarray) -> dict:
    """
    Difference-in-Differences estimator.

    Args:
        treated_pre: Treated unit pre-treatment
        treated_post: Treated unit post-treatment
        control_pre: Control units pre-treatment
        control_post: Control units post-treatment

    Returns:
        Dictionary with DiD estimate
    """
    # Average treatment effect
    treated_diff = treated_post.mean() - treated_pre.mean()
    control_diff = control_post.mean() - control_pre.mean()

    did_estimate = treated_diff - control_diff

    # Simple standard error (assuming independence)
    var_treated = np.var(treated_post) / len(treated_post) + np.var(treated_pre) / len(treated_pre)
    var_control = np.var(control_post) / len(control_post) + np.var(control_pre) / len(control_pre)

    se = np.sqrt(var_treated + var_control)

    # T-statistic
    t_stat = did_estimate / se if se > 0 else 0

    # P-value (two-sided)
    p_value = 2 * (1 - stats.norm.cdf(abs(t_stat)))

    return {
        'estimate': did_estimate,
        'se': se,
        't_stat': t_stat,
        'p_value': p_value,
        'treated_diff': treated_diff,
        'control_diff': control_diff
    }


def analyze_discontinuities(df: pd.DataFrame, time_series: dict) -> pd.DataFrame:
    """
    Analyze structural discontinuities across all country-sport pairs.

    Args:
        df: Sport feature DataFrame
        time_series: Dictionary of time series

    Returns:
        DataFrame with detected discontinuities
    """
    results = []
    p_values = []

    for (noc, cluster), ts_data in time_series.items():
        years = ts_data['years']
        medals = ts_data['medals']

        # Detect breakpoint
        bp_idx, f_stat = detect_breakpiece_chow(years, medals)

        if bp_idx is not None:
            # Effect size
            effect = estimate_break_effect(medals, bp_idx)

            # Year of breakpoint
            bp_year = years[bp_idx]

            # Get country name
            # FIXED: Changed .first() to .iloc[0] to avoid deprecation warning
            if 'country' in df.columns:
                country_df = df[df['noc'] == noc]
                country_name = country_df['country'].iloc[0] if len(country_df) > 0 else noc
            else:
                country_name = noc

            # Calculate p-value from F-statistic
            # F(k, n-2k) distribution
            k = 2
            n = len(medals)
            p_val = 1 - stats.f.cdf(f_stat, k, n - 2*k)

            results.append({
                'NOC': noc,
                'Country': country_name,
                'Sport_Cluster': cluster,
                'Breakpoint_Year': bp_year,
                'Breakpoint_Index': bp_idx,
                'F_Statistic': f_stat,
                'P_Value': p_val,
                'Effect_Size': effect,
                'Pre_Mean': medals[:bp_idx].mean(),
                'Post_Mean': medals[bp_idx:].mean(),
                'Pre_Std': medals[:bp_idx].std(),
                'Post_Std': medals[bp_idx:].std(),
                'N_Observations': n
            })

            p_values.append(p_val)

    if not results:
        print("   No discontinuities detected")
        return pd.DataFrame()

    results_df = pd.DataFrame(results)

    # FDR correction
    reject, p_corrected, _, _ = multipletests(p_values, alpha=0.05, method='fdr_bh')
    results_df['P_Value_Corrected'] = p_corrected
    results_df['Significant'] = reject

    # Filter to significant discontinuities with meaningful effect
    significant = results_df[(results_df['Significant']) &
                             (np.abs(results_df['Effect_Size']) > 1)].copy()

    print(f"   Detected {len(significant)} significant discontinuities (after FDR correction)")

    return significant


def estimate_synthetic_effects(significant_df: pd.DataFrame,
                               time_series: dict,
                               df: pd.DataFrame) -> pd.DataFrame:
    """
    Estimate synthetic control effects for significant discontinuities.

    Args:
        significant_df: DataFrame with significant discontinuities
        time_series: Dictionary of time series
        df: Original feature DataFrame

    Returns:
        DataFrame with synthetic control estimates
    """
    results = []

    for _, row in significant_df.iterrows():
        noc = row['NOC']
        cluster = row['Sport_Cluster']
        bp_idx = row['Breakpoint_Index']

        key = (noc, cluster)
        if key not in time_series:
            continue

        medals = time_series[key]['medals']
        target_len = len(medals)

        # Create donor pool from same sport cluster, different countries
        donor_data = []
        for (donor_noc, donor_cluster), ts in time_series.items():
            if donor_cluster == cluster and donor_noc != noc:
                donor_medals = ts['medals']
                donor_len = len(donor_medals)

                # FIXED: Handle negative pad_width for short time series
                # Skip donors longer than target (can't pad negatively)
                if donor_len > target_len:
                    continue

                # Calculate pad_width, ensuring it's non-negative
                pad_width = target_len - donor_len

                # Only pad if donor is shorter than target
                if pad_width >= 0:
                    donor_ts = np.pad(donor_medals,
                                     (0, pad_width),
                                     constant_values=0)
                    if len(donor_ts) == target_len:
                        donor_data.append(donor_ts)

        if not donor_data:
            continue

        donor_df = pd.DataFrame(donor_data).T

        # Build synthetic control
        pre_period = slice(0, bp_idx)
        post_period = slice(bp_idx, len(medals))

        sc_result = build_synthetic_control(medals, donor_df, pre_period)

        if not sc_result['success']:
            # Fall back to DiD
            treated_pre = medals[pre_period]
            treated_post = medals[post_period]
            control_pre = donor_df.iloc[pre_period].values.flatten()
            control_post = donor_df.iloc[post_period].values.flatten()

            did_result = did_estimator(treated_pre, treated_post, control_pre, control_post)

            results.append({
                'NOC': noc,
                'Sport_Cluster': cluster,
                'Breakpoint_Year': row['Breakpoint_Year'],
                'Method': 'DiD',
                'Effect_Estimate': did_result['estimate'],
                'SE': did_result['se'],
                'T_Statistic': did_result['t_stat'],
                'P_Value': did_result['p_value']
            })
        else:
            # Synthetic control successful
            synthetic = sc_result['synthetic']
            pre_actual = medals[pre_period].mean()
            post_actual = medals[post_period].mean()
            pre_synthetic = synthetic[pre_period].mean()
            post_synthetic = synthetic[post_period].mean()

            # Treatment effect
            actual_diff = post_actual - pre_actual
            synthetic_diff = post_synthetic - pre_synthetic
            effect = actual_diff - synthetic_diff

            results.append({
                'NOC': noc,
                'Sport_Cluster': cluster,
                'Breakpoint_Year': row['Breakpoint_Year'],
                'Method': 'Synthetic Control',
                'Effect_Estimate': effect,
                'Pre_Actual': pre_actual,
                'Post_Actual': post_actual,
                'Pre_Synthetic': pre_synthetic,
                'Post_Synthetic': post_synthetic,
                'SE': np.nan,
                'T_Statistic': np.nan,
                'P_Value': np.nan
            })

    return pd.DataFrame(results)


def identify_investment_opportunities(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify top sport clusters for investment based on historical discontinuities.

    Args:
        df: Results DataFrame with discontinuity effects

    Returns:
        DataFrame with investment recommendations
    """
    if df.empty:
        return pd.DataFrame()

    # Aggregate by sport cluster
    cluster_stats = df.groupby('Sport_Cluster').agg({
        'Effect_Estimate': ['mean', 'std', 'count'],
        'NOC': 'nunique'
    }).reset_index()

    cluster_stats.columns = ['Sport_Cluster', 'Mean_Effect', 'Std_Effect',
                            'N_Discontinuities', 'N_Countries']

    # Calculate ROI-like metric (effect per discontinuity)
    cluster_stats['ROI_Score'] = cluster_stats['Mean_Effect'] / (cluster_stats['Std_Effect'] + 1)

    # Filter to clusters with multiple discontinuities (more evidence)
    cluster_stats = cluster_stats[cluster_stats['N_Discontinuities'] >= 2]

    # Sort by ROI score
    cluster_stats = cluster_stats.sort_values('ROI_Score', ascending=False)

    return cluster_stats


def main():
    """Main execution function."""
    print("=" * 60)
    print("Model 5: Structural Performance Discontinuities")
    print("=" * 60)

    # 1. Load sport features
    print("\n1. Loading sport features...")
    df_sport = load_sport_features('implementation/data/features_sport.csv')

    # Add country names
    noc_map = pd.read_csv('implementation/data/noc_mapping.csv')
    df_sport = df_sport.merge(noc_map, on='noc', how='left')

    # 2. Prepare time series
    print("\n2. Preparing time series for breakpoint detection...")
    time_series = prepare_time_series(df_sport, min_observations=5)

    # 3. Analyze discontinuities
    print("\n3. Analyzing discontinuities...")
    discontinuities = analyze_discontinuities(df_sport, time_series)

    if discontinuities.empty:
        print("   No significant discontinuities found")
        results_df = pd.DataFrame()
        synthetic_results = pd.DataFrame()
        investment_opportunities = pd.DataFrame()
    else:
        print(f"\n   Top discontinuities by effect size:")
        top_effects = discontinuities.nlargest(10, 'Effect_Size')
        print(top_effects[['NOC', 'Sport_Cluster', 'Breakpoint_Year', 'Effect_Size', 'P_Value_Corrected']].to_string(index=False))

        # 4. Estimate synthetic control effects
        print("\n4. Estimating synthetic control effects...")
        synthetic_results = estimate_synthetic_effects(discontinuities, time_series, df_sport)

        if not synthetic_results.empty:
            print(f"   Estimated {len(synthetic_results)} treatment effects")
            print(f"\n   Top effects by magnitude:")
            print(synthetic_results.nlargest(10, 'Effect_Estimate')[['NOC', 'Sport_Cluster', 'Method', 'Effect_Estimate']].to_string(index=False))

        # 5. Identify investment opportunities
        print("\n5. Identifying investment opportunities...")
        investment_opportunities = identify_investment_opportunities(synthetic_results)

        if not investment_opportunities.empty:
            print(f"\n   Top investment opportunities by sport cluster:")
            print(investment_opportunities.head(10).to_string(index=False))

        # 6. Compile results
        print("\n6. Compiling results...")

        # Merge discontinuities with synthetic results
        results_df = discontinuities.merge(
            synthetic_results[['NOC', 'Sport_Cluster', 'Method', 'Effect_Estimate', 'SE']],
            on=['NOC', 'Sport_Cluster'],
            how='left'
        )

        # Rename for clarity
        results_df = results_df.rename(columns={
            'Effect_Size': 'Break_Magnitude',
            'Effect_Estimate': 'SC_DiD_Effect'
        })

    # 7. Save results
    print("\n7. Saving results...")
    if not results_df.empty:
        results_df.to_csv('output/results/results_5.csv', index=False)
        print(f"   Saved {len(results_df)} discontinuities to output/results/results_5.csv")

    if not investment_opportunities.empty:
        investment_opportunities.to_csv('output/results/results_5_investment.csv', index=False)
        print("   Saved investment opportunities to output/results/results_5_investment.csv")

    # 8. Save models
    print("\n8. Saving models...")
    model_bundle = {
        'time_series': {k: v for k, v in list(time_series.items())[:100]},  # Limit size
        'n_discontinuities': len(results_df) if not results_df.empty else 0,
        'discontinuities': results_df.to_dict('records') if not results_df.empty else []
    }
    with open('implementation/models/model_5.pkl', 'wb') as f:
        pickle.dump(model_bundle, f)
    print("   Saved to implementation/models/model_5.pkl")

    print("\n" + "=" * 60)
    print("Model 5 Implementation Complete")
    print("=" * 60)

    return results_df, synthetic_results, model_bundle


if __name__ == "__main__":
    discontinuities, synthetic_effects, models = main()
