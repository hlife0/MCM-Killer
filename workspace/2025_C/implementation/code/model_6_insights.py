#!/usr/bin/env python3
"""
Model 6: Original Insights (Multi-Method Exploratory Analysis)
Based on: output/model_design.md
Translated by: @code_translator

This model provides novel analytical insights:
1. Olympic Efficiency Analysis (Stochastic Frontier)
2. Regime Dynamics
3. Sport Life Cycle Analysis
4. Geographic Diffusion
5. Counterfactual Scenarios
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.optimize import minimize
import networkx as nx
import statsmodels.api as sm  # FIXED: Added missing import
import pickle
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)


# Continent mapping for spatial analysis
CONTINENT_MAP = {
    'USA': 'Americas', 'CAN': 'Americas', 'BRA': 'Americas', 'MEX': 'Americas',
    'ARG': 'Americas', 'COL': 'Americas', 'JAM': 'Americas', 'CUB': 'Americas',
    'DOM': 'Americas', 'TTO': 'Americas', 'PUR': 'Americas', 'CHI': 'Americas',
    'PER': 'Americas', 'VEN': 'Americas', 'ECU': 'Americas', 'URU': 'Americas',
    'GBR': 'Europe', 'FRA': 'Europe', 'GER': 'Europe', 'ITA': 'Europe',
    'ESP': 'Europe', 'NED': 'Europe', 'BEL': 'Europe', 'SWE': 'Europe',
    'SUI': 'Europe', 'DEN': 'Europe', 'NOR': 'Europe', 'FIN': 'Europe',
    'HUN': 'Europe', 'POL': 'Europe', 'GRE': 'Europe', 'AUT': 'Europe',
    'CZE': 'Europe', 'CRO': 'Europe', 'SRB': 'Europe', 'BUL': 'Europe',
    'ROU': 'Europe', 'POR': 'Europe', 'IRL': 'Europe', 'UKR': 'Europe',
    'RUS': 'Europe', 'BLR': 'Europe', 'LTU': 'Europe', 'LAT': 'Europe',
    'EST': 'Europe', 'SVK': 'Europe', 'SVN': 'Europe',
    'CHN': 'Asia', 'JPN': 'Asia', 'KOR': 'Asia', 'TPE': 'Asia',
    'PRK': 'Asia', 'IRI': 'Asia', 'KAZ': 'Asia', 'UZB': 'Asia',
    'THA': 'Asia', 'INA': 'Asia', 'MAS': 'Asia', 'SIN': 'Asia',
    'VIE': 'Asia', 'PHI': 'Asia', 'HKG': 'Asia', 'ISR': 'Asia',
    'IND': 'Asia', 'PAK': 'Asia', 'SRI': 'Asia',
    'AUS': 'Oceania', 'NZL': 'Oceania',
    'RSA': 'Africa', 'KEN': 'Africa', 'ETH': 'Africa', 'MAR': 'Africa',
    'TUN': 'Africa', 'ALG': 'Africa', 'EGY': 'Africa', 'NGR': 'Africa'
}


def load_features(path: str = 'implementation/data/features_core.csv') -> pd.DataFrame:
    """Load feature data from CSV file."""
    df = pd.read_csv(path)

    # Handle missing values and inf values
    df['prev_total_medals'] = df['prev_total_medals'].fillna(0)
    df['participation_growth'] = df['participation_growth'].fillna(0)
    # FIXED: Handle inf values in participation_growth
    df['participation_growth'] = df['participation_growth'].replace([np.inf, -np.inf], 0)

    print(f"Loaded features: {df.shape}")
    return df


# ============================================================================
# INSIGHT 1: OLYMPIC EFFICIENCY ANALYSIS (Stochastic Frontier)
# ============================================================================

class StochasticFrontierModel:
    """
    Stochastic Frontier Analysis for Olympic efficiency.

    Models: log(Y) = beta*X + v - u
    where v ~ N(0, sigma_v^2) is noise and u >= 0 is inefficiency
    """

    def __init__(self):
        self.params = None
        self.lambda_ = None  # sigma_u / sigma_v
        self.sigma_sq = None
        self.efficiency = {}

    def fit(self, X: np.ndarray, y: np.ndarray) -> dict:
        """
        Fit stochastic frontier model using MLE.

        Args:
            X: Feature matrix (inputs: athletes, sports)
            y: Output (log medals)

        Returns:
            Fitted parameters
        """
        n, k = X.shape

        def log_likelihood(params):
            # Unpack parameters
            beta = params[:k]
            sigma_v = np.exp(params[k])  # Ensure positive
            sigma_u = np.exp(params[k + 1])

            sigma_sq = sigma_v**2 + sigma_u**2
            lambda_ = sigma_u / sigma_v

            # Residuals
            epsilon = y - X @ beta

            # Log likelihood for stochastic frontier
            # Using Battese and Coelli (1988) formulation
            sigma = np.sqrt(sigma_sq)
            sigma_star = sigma_v * sigma_u / sigma

            # CDF and PDF terms
            z = (lambda_ * epsilon) / sigma
            cdf = stats.norm.cdf(z)
            pdf = stats.norm.pdf(z)

            # Log likelihood
            ll = -n * np.log(sigma) + np.sum(np.log(cdf)) - \
                 0.5 * np.sum((epsilon / sigma_v)**2)

            return -ll  # Minimize negative log likelihood

        # Initial values
        init_beta = np.linalg.lstsq(X, y, rcond=None)[0]
        init_params = np.concatenate([init_beta, [np.log(1.0), np.log(0.5)]])

        # Optimize
        result = minimize(log_likelihood, init_params, method='L-BFGS-B',
                         options={'maxiter': 1000})

        if result.success:
            params = result.x
            beta = params[:k]
            sigma_v = np.exp(params[k])
            sigma_u = np.exp(params[k + 1])

            self.params = beta
            self.lambda_ = sigma_u / sigma_v
            self.sigma_sq = sigma_v**2 + sigma_u**2

        return self.params

    def predict_efficiency(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        Predict efficiency scores.

        Args:
            X: Feature matrix
            y: Actual outputs

        Returns:
            Efficiency scores (0-1, where 1 = fully efficient)
        """
        if self.params is None:
            raise ValueError("Model not fitted")

        # Predicted frontier
        y_pred = X @ self.params

        # Residuals
        epsilon = y - y_pred

        # JLMS estimator (Jondrow et al., 1982)
        sigma_v = np.sqrt(self.sigma_sq / (1 + self.lambda_**2))
        sigma_u = self.lambda_ * sigma_v

        # E[u|epsilon]
        sigma_star = sigma_v * sigma_u / np.sqrt(self.sigma_sq)
        z = (self.lambda_ * epsilon) / np.sqrt(self.sigma_sq)

        pdf_z = stats.norm.pdf(z)
        cdf_z = stats.norm.cdf(z)

        e_u = epsilon * (sigma_u**2 / self.sigma_sq) + \
              sigma_star * (pdf_z / cdf_z)

        # Efficiency = exp(-u)
        efficiency = np.exp(-e_u)
        efficiency = np.clip(efficiency, 0, 1)

        return efficiency


def analyze_efficiency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze Olympic efficiency for all countries.

    Args:
        df: Feature DataFrame

    Returns:
        DataFrame with efficiency scores
    """
    # Use recent data (post-2000)
    df_recent = df[df['year'] >= 2000].copy()

    # Create inputs (log athletes, log sports)
    X = df_recent[['athlete_count', 'sports_count']].copy()
    X['log_athletes'] = np.log(df_recent['athlete_count'] + 1)
    X['log_sports'] = np.log(df_recent['sports_count'] + 1)
    X = X[['log_athletes', 'log_sports']].values
    X = sm.add_constant(X)

    # Output (log medals)
    y = np.log(df_recent['total_medals'] + 1).values

    # Fit stochastic frontier
    sf_model = StochasticFrontierModel()
    sf_model.fit(X, y)

    # Get efficiency scores
    efficiency = sf_model.predict_efficiency(X, y)

    # Aggregate by country
    results = df_recent.copy()
    results['efficiency'] = efficiency
    results['log_athletes'] = X[:, 1]
    results['log_sports'] = X[:, 2]

    # FIXED: Use 'noc' instead of 'NOC' - ensure column naming consistency
    country_efficiency = results.groupby('noc').agg({
        'efficiency': 'mean',
        'total_medals': 'mean',
        'country': 'first'
    }).reset_index()

    # FIXED: Rename both 'noc' to 'NOC' AND 'country' to 'Country' for consistency with output format
    country_efficiency = country_efficiency.rename(columns={'noc': 'NOC', 'country': 'Country'})
    country_efficiency = country_efficiency.sort_values('efficiency', ascending=False)
    country_efficiency['Rank'] = range(1, len(country_efficiency) + 1)

    return country_efficiency


# ============================================================================
# INSIGHT 2: REGIME DYNAMICS
# ============================================================================

def classify_regime(medal_history: np.ndarray) -> str:
    """
    Classify a country's performance regime.

    Args:
        medal_history: Array of medal counts

    Returns:
        Regime label
    """
    if len(medal_history) < 3:
        return 'Unknown'

    mean_medals = medal_history.mean()
    recent_mean = medal_history[-3:].mean() if len(medal_history) >= 3 else mean_medals
    trend = np.polyfit(range(len(medal_history)), medal_history, 1)[0]

    # Classification rules
    if mean_medals == 0:
        return 'Non_Medalist'
    elif mean_medals <= 5:
        if trend > 0.5:
            return 'Emerging'
        elif trend < -0.5:
            return 'Declining'
        else:
            return 'Emerging'
    elif mean_medals <= 20:
        if trend > 1:
            return 'Developing'
        elif trend < -1:
            return 'Declining'
        else:
            return 'Stable_Developing'
    else:
        if trend < -2:
            return 'Declining'
        else:
            return 'Dominant'


def analyze_regime_dynamics(df: pd.DataFrame) -> tuple:
    """
    Analyze regime dynamics for all countries.

    Args:
        df: Feature DataFrame

    Returns:
        (DataFrame with regime classifications, DataFrame with transitions)
    """
    regime_history = []

    for noc in df['noc'].unique():
        country_data = df[df['noc'] == noc].sort_values('year')
        medals = country_data['total_medals'].values

        if len(medals) < 3:
            continue

        # Classify current regime
        current_regime = classify_regime(medals)

        # Track regime over time
        for i in range(len(medals)):
            if i >= 2:
                regime_history.append({
                    'noc': noc,  # FIXED: Use lowercase 'noc' for consistency
                    'Country': country_data['country'].iloc[0],
                    'Year': country_data['year'].iloc[i],
                    'Medals': medals[i],
                    'Regime': classify_regime(medals[:i+1])
                })

    regime_df = pd.DataFrame(regime_history)

    # Calculate transition probabilities
    if len(regime_df) > 0:
        regime_df['Next_Regime'] = regime_df.groupby('noc')['Regime'].shift(-1)

        transitions = regime_df.groupby(['Regime', 'Next_Regime']).size().reset_index(name='Count')

        # Calculate probabilities
        regime_counts = regime_df['Regime'].value_counts().to_dict()
        transitions['Probability'] = transitions.apply(
            lambda row: row['Count'] / regime_counts.get(row['Regime'], 1),
            axis=1
        )
    else:
        transitions = pd.DataFrame()

    return regime_df, transitions


# ============================================================================
# INSIGHT 3: SPORT LIFE CYCLE ANALYSIS
# ============================================================================

def analyze_sport_dispersion(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze sport concentration over time (life cycle analysis).

    Args:
        df: Sport feature DataFrame

    Returns:
        DataFrame with dispersion metrics
    """
    # Load sport features
    sport_df = pd.read_csv('implementation/data/features_sport.csv')

    # Aggregate by sport-year
    sport_year = sport_df.groupby(['sport', 'year'])['sport_medals'].sum().reset_index()

    # Calculate Herfindahl-Hirschman Index (concentration)
    dispersion_results = []

    for year in sport_year['year'].unique():
        year_data = sport_year[sport_year['year'] == year]

        total_medals = year_data['sport_medals'].sum()
        if total_medals == 0:
            continue

        # HHI: sum of squared shares
        shares = year_data['sport_medals'] / total_medals
        hhi = (shares**2).sum()

        # Dispersion: 1 - HHI (higher = more dispersed)
        dispersion = 1 - hhi

        # Number of medal-winning countries
        n_countries = sport_df[(sport_df['year'] == year) &
                               (sport_df['sport_medals'] > 0)]['noc'].nunique()

        dispersion_results.append({
            'Year': year,
            'Dispersion': dispersion,
            'HHI': hhi,
            'N_Sports': len(year_data),
            'N_Countries': n_countries
        })

    dispersion_df = pd.DataFrame(dispersion_results)
    dispersion_df = dispersion_df.sort_values('Year')

    return dispersion_df


# ============================================================================
# INSIGHT 4: GEOGRAPHIC DIFFUSION
# ============================================================================

def analyze_spatial_clustering(df: pd.DataFrame) -> dict:
    """
    Analyze geographic clustering of Olympic success.

    Args:
        df: Feature DataFrame

    Returns:
        Dictionary with spatial analysis results
    """
    # Add continent
    df_copy = df.copy()
    df_copy['continent'] = df_copy['noc'].map(CONTINENT_MAP).fillna('Other')

    # Calculate continent totals by year
    continent_year = df_copy.groupby(['year', 'continent'])['total_medals'].sum().reset_index()

    # Calculate share of world total
    world_total = df_copy.groupby('year')['total_medals'].sum().reset_index()
    world_total.columns = ['year', 'world_total']

    continent_year = continent_year.merge(world_total, on='year')
    continent_year['share'] = continent_year['total_medals'] / continent_year['world_total']

    # Calculate concentration (Herfindahl for continents)
    continent_hhi = []

    for year in df_copy['year'].unique():
        year_data = continent_year[continent_year['year'] == year]
        if len(year_data) == 0:
            continue

        hhi = (year_data['share']**2).sum()
        continent_hhi.append({'Year': year, 'Continent_HHI': hhi})

    # Calculate Moran's I-like measure (simplified)
    # For actual Moran's I, we'd need a proper spatial weights matrix
    spatial_results = {
        'continent_hhi': pd.DataFrame(continent_hhi),
        'continent_shares': continent_year
    }

    return spatial_results


# ============================================================================
# INSIGHT 5: COUNTERFACTUAL ANALYSIS
# ============================================================================

def counterfactual_no_host(df: pd.DataFrame, models: dict) -> pd.DataFrame:
    """
    Simulate medal tables without host advantage.

    Args:
        df: Feature DataFrame
        models: Trained models (from Model 1)

    Returns:
        DataFrame with counterfactual predictions
    """
    # Get most recent data
    recent = df[df['year'] == 2024].copy()

    # Simulate removing host effect
    # Host effect typically adds ~10-20% to medal count
    HOST_EFFECT = 0.15

    # Identify historical hosts and their advantage
    historical_hosts = {
        2004: 'GRE', 2008: 'CHN', 2012: 'GBR',
        2016: 'BRA', 2020: 'JPN', 2024: 'FRA'
    }

    counterfactual_results = []

    for year, host_noc in historical_hosts.items():
        year_data = df[df['year'] == year].copy()
        host_data = year_data[year_data['noc'] == host_noc]

        if len(host_data) == 0:
            continue

        actual_medals = host_data['total_medals'].values[0]
        counterfactual_medals = actual_medals / (1 + HOST_EFFECT)

        counterfactual_results.append({
            'Year': year,
            'Host_NOC': host_noc,
            'Actual_Medals': actual_medals,
            'Counterfactual_No_Host': round(counterfactual_medals),
            'Host_Advantage': round(actual_medals - counterfactual_medals)
        })

    return pd.DataFrame(counterfactual_results)


def counterfactual_no_boycott(df: pd.DataFrame) -> pd.DataFrame:
    """
    Simulate 1980/1984 without boycotts.

    Args:
        df: Feature DataFrame

    Returns:
        DataFrame with boycott analysis
    """
    # 1980 Moscow: USA-led boycott
    # 1984 Los Angeles: Soviet-led boycott

    # Affected countries
    boycotters_1980 = ['USA', 'GBR', 'FRA', 'GER', 'JPN', 'AUS', 'CAN', 'TUR', 'KEN']
    boycotters_1984 = ['RUS', 'GDR', 'POL', 'CUB', 'CZE', 'HUN', 'BUL', 'ROU']

    boycott_results = []

    # 1980 analysis
    df_1980 = df[df['year'] == 1980].copy()
    ussr_1980 = df_1980[df_1980['noc'] == 'RUS']

    if len(ussr_1980) > 0:
        ussr_medals = ussr_1980['total_medals'].values[0]

        # Estimate USA and allies medals based on 1976/1984
        usa_1976 = df[(df['noc'] == 'USA') & (df['year'] == 1976)]['total_medals'].values
        usa_1984 = df[(df['noc'] == 'USA') & (df['year'] == 1984)]['total_medals'].values

        if len(usa_1976) > 0 and len(usa_1984) > 0:
            # Interpolate expected 1980 medals
            expected_usa_1980 = (usa_1976[0] + usa_1984[0]) / 2

            boycott_results.append({
                'Year': 1980,
                'Scenario': 'No_Boycott',
                'Affected_Nation': 'USA',
                'Expected_Medals': round(expected_usa_1980),
                'Actual_Medals': 0  # USA didn't participate
            })

    # 1984 analysis
    df_1984 = df[df['year'] == 1984].copy()
    usa_1984 = df_1984[df_1984['noc'] == 'USA']

    if len(usa_1984) > 0:
        usa_medals = usa_1984['total_medals'].values[0]

        # Estimate USSR and allies medals
        ussr_1980 = df[(df['noc'] == 'RUS') & (df['year'] == 1980)]['total_medals'].values
        ussr_1988 = df[(df['noc'] == 'RUS') & (df['year'] == 1988)]['total_medals'].values

        if len(ussr_1980) > 0 and len(ussr_1988) > 0:
            expected_ussr_1984 = (ussr_1980[0] + ussr_1988[0]) / 2

            boycott_results.append({
                'Year': 1984,
                'Scenario': 'No_Boycott',
                'Affected_Nation': 'USSR',
                'Expected_Medals': round(expected_ussr_1984),
                'Actual_Medals': 0
            })

    return pd.DataFrame(boycott_results)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("=" * 60)
    print("Model 6: Original Insights (Multi-Method Analysis)")
    print("=" * 60)

    # 1. Load features
    print("\n1. Loading features...")
    df = load_features('implementation/data/features_core.csv')

    results = {}

    # 2. Efficiency Analysis
    print("\n2. Analyzing Olympic efficiency...")
    efficiency_df = analyze_efficiency(df)

    print(f"   Top 15 most efficient countries:")
    print(efficiency_df.head(15)[['Rank', 'NOC', 'Country', 'efficiency']].to_string(index=False))

    results['efficiency'] = efficiency_df

    # 3. Regime Dynamics
    print("\n3. Analyzing regime dynamics...")
    regime_df, transitions = analyze_regime_dynamics(df)

    # FIXED: Handle empty regime_df case
    if len(regime_df) > 0:
        # Get current regime for each country
        current_regimes = regime_df.groupby('noc').last().reset_index()
        current_regimes = current_regimes.sort_values(['Regime', 'Medals'], ascending=[True, False])

        print(f"\n   Current regime distribution:")
        regime_counts = current_regimes['Regime'].value_counts()
        for regime, count in regime_counts.items():
            print(f"     {regime}: {count} countries")

        print(f"\n   Countries in 'Emerging' regime:")
        emerging = current_regimes[current_regimes['Regime'] == 'Emerging']
        print(emerging[['noc', 'Country', 'Medals']].head(15).to_string(index=False))
    else:
        current_regimes = pd.DataFrame()
        print("   No regime data available")

    results['regime'] = regime_df
    results['transitions'] = transitions

    # 4. Sport Life Cycle
    print("\n4. Analyzing sport life cycles (dispersion)...")
    dispersion_df = analyze_sport_dispersion(df)

    print(f"\n   Dispersion trend (higher = more competitive):")
    print(dispersion_df.tail(10).to_string(index=False))

    # Classify life cycle stages
    recent_dispersion = dispersion_df.tail(5)['Dispersion'].mean()
    if recent_dispersion > 0.8:
        life_cycle_stage = "Introduction (High Dispersion)"
    elif recent_dispersion > 0.6:
        life_cycle_stage = "Consolidation"
    else:
        life_cycle_stage = "Maturity (Concentrated)"

    print(f"\n   Current Life Cycle Stage: {life_cycle_stage}")

    results['dispersion'] = dispersion_df

    # 5. Geographic Diffusion
    print("\n5. Analyzing geographic clustering...")
    spatial_results = analyze_spatial_clustering(df)

    print(f"\n   Continent HHI trend (concentration of medals by continent):")
    print(spatial_results['continent_hhi'].tail(10).to_string(index=False))

    results['spatial'] = spatial_results

    # 6. Counterfactual Analysis
    print("\n6. Running counterfactual scenarios...")

    # No host advantage
    host_cf = counterfactual_no_host(df, {})
    print(f"\n   Counterfactual: No Host Advantage")
    print(host_cf.to_string(index=False))

    # No boycott
    boycott_cf = counterfactual_no_boycott(df)
    print(f"\n   Counterfactual: No Boycotts")
    print(boycott_cf.to_string(index=False))

    results['host_counterfactual'] = host_cf
    results['boycott_counterfactual'] = boycott_cf

    # 7. Compile summary insights
    print("\n7. Compiling summary insights...")

    # FIXED: Handle empty current_regimes case
    n_emerging = len(current_regimes[current_regimes['Regime'] == 'Emerging']) if len(current_regimes) > 0 else 0
    n_dominant = len(current_regimes[current_regimes['Regime'] == 'Dominant']) if len(current_regimes) > 0 else 0

    summary_insights = {
        'most_efficient_country': efficiency_df.iloc[0]['Country'] if len(efficiency_df) > 0 else 'N/A',
        'avg_efficiency': efficiency_df['efficiency'].mean() if len(efficiency_df) > 0 else 0,
        'n_emerging_countries': n_emerging,
        'n_dominant_countries': n_dominant,
        'current_dispersion': recent_dispersion,
        'life_cycle_stage': life_cycle_stage,
        'total_host_advantage_1980_2024': host_cf['Host_Advantage'].sum() if len(host_cf) > 0 else 0
    }

    print(f"\n   Key Insights:")
    print(f"     - Most Efficient: {summary_insights['most_efficient_country']}")
    print(f"     - Emerging Countries: {summary_insights['n_emerging_countries']}")
    print(f"     - Total Host Advantage (1980-2024): {summary_insights['total_host_advantage_1980_2024']} medals")
    print(f"     - Life Cycle Stage: {summary_insights['life_cycle_stage']}")

    # 8. Save results
    print("\n8. Saving results...")

    efficiency_df.to_csv('output/results/results_6_efficiency.csv', index=False)
    print("   Saved efficiency rankings to output/results/results_6_efficiency.csv")

    if len(regime_df) > 0:
        current_regimes.to_csv('output/results/results_6_regimes.csv', index=False)
        print("   Saved regime classifications to output/results/results_6_regimes.csv")

    dispersion_df.to_csv('output/results/results_6_dispersion.csv', index=False)
    print("   Saved dispersion analysis to output/results/results_6_dispersion.csv")

    host_cf.to_csv('output/results/results_6_host_cf.csv', index=False)
    boycott_cf.to_csv('output/results/results_6_boycott_cf.csv', index=False)

    # Save summary
    summary_df = pd.DataFrame([summary_insights])
    summary_df.to_csv('output/results/results_6_summary.csv', index=False)

    # 9. Save models
    print("\n9. Saving models...")
    model_bundle = {
        'summary': summary_insights,
        'efficiency_model': efficiency_df.to_dict('records') if len(efficiency_df) > 0 else [],
        'transitions': transitions.to_dict('records') if len(transitions) > 0 else []
    }
    with open('implementation/models/model_6.pkl', 'wb') as f:
        pickle.dump(model_bundle, f)
    print("   Saved to implementation/models/model_6.pkl")

    print("\n" + "=" * 60)
    print("Model 6 Implementation Complete")
    print("=" * 60)

    return results, model_bundle


if __name__ == "__main__":
    results, models = main()
