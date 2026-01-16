#!/usr/bin/env python3
"""
Model 3: First-Time Medalists (Classification + Count Model)
Based on: output/model_design.md
Translated by: @code_translator

This model predicts first-time medalists using a two-stage approach:
1. Logistic regression for probability of first medal
2. Count model for medals conditional on first medal

TODO: Data limitation - source file only includes medal-winning countries
Need to include zero-medal countries to properly predict first-time medalists
Consultation with @modeler required for alternative approach
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import statsmodels.api as sm
from scipy.stats import nbinom
import pickle
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)


# Continent mapping for regional spillover effect
CONTINENT_MAP = {
    'Europe': ['GBR', 'FRA', 'GER', 'ITA', 'ESP', 'NED', 'BEL', 'SWE', 'SUI', 'DEN', 'NOR',
               'FIN', 'HUN', 'POL', 'GRE', 'AUT', 'CZE', 'CRO', 'SRB', 'BUL', 'ROU', 'POR',
               'IRL', 'LTU', 'LAT', 'EST', 'SVK', 'SVN', 'BIH', 'MNE', 'MKD', 'ALB', 'MLT',
               'LUX', 'MON', 'SMR', 'AND', 'ISL', 'CYP', 'GEO', 'ARM', 'AZE', 'MDA', 'UKR',
               'BLR', 'RUS', 'NOR', 'SWE', 'FIN', 'DEN'],
    'Asia': ['CHN', 'JPN', 'KOR', 'TPE', 'PRK', 'IRI', 'KAZ', 'UZB', 'KGZ', 'TJK', 'MGL',
             'THA', 'INA', 'MAS', 'SIN', 'VIE', 'PHL', 'HKG', 'ISR', 'JOR', 'QAT', 'UAE',
             'KSA', 'KUW', 'IRQ', 'SYR', 'LBN', 'JOR', 'YEM', 'OMA', 'BHR', 'IND', 'PAK',
             'SRI', 'BAN', 'NEP', 'AFG', 'MYA', 'CAM', 'LAO'],
    'Americas': ['USA', 'CAN', 'BRA', 'MEX', 'ARG', 'COL', 'JAM', 'CUB', 'DOM', 'TTO', 'PUR',
                 'CHI', 'PER', 'VEN', 'ECU', 'BOL', 'URU', 'PAR', 'PAN', 'CRC', 'HAI', 'GUA',
                 'BAR', 'GRN', 'BAH', 'BER', 'ANT', 'GUY', 'SUR', 'BLZ', 'HON', 'SLV', 'NIC'],
    'Africa': ['RSA', 'KEN', 'ETH', 'MAR', 'TUN', 'ALG', 'EGY', 'NGR', 'COD', 'CMR', 'CIV',
               'GHA', 'UGA', 'ZAM', 'ZIM', 'ANG', 'MOZ', 'NAM', 'BOT', 'MRI', 'SEY', 'SEN',
               'GAB', 'CIV', 'BEN', 'TOG', 'MLI', 'SOM', 'LBR', 'SLE', 'GUI', 'ERI'],
    'Oceania': ['AUS', 'NZL', 'FIJ', 'PNG', 'SAM', 'TON', 'VAN', 'SOL', 'NOC', 'NRU', 'PLW',
                'COK', 'TGA']
}

# Create reverse lookup
COUNTRY_TO_CONTINENT = {}
for continent, countries in CONTINENT_MAP.items():
    for country in countries:
        COUNTRY_TO_CONTINENT[country] = continent


def load_features(path: str = 'implementation/data/features_core.csv') -> pd.DataFrame:
    """Load feature data from CSV file."""
    df = pd.read_csv(path)

    # Handle missing values
    df['prev_total_medals'] = df['prev_total_medals'].fillna(0)
    df['prev_gold_count'] = df['prev_gold_count'].fillna(0)
    df['medal_trend_3'] = df['medal_trend_3'].fillna(0)
    df['participation_growth'] = df['participation_growth'].fillna(0)

    print(f"Loaded features: {df.shape}")
    return df


def identify_never_won_countries(df: pd.DataFrame) -> list:
    """
    Identify countries that have never won a medal.

    Args:
        df: Feature DataFrame

    Returns:
        List of NOC codes for never-won countries

    NOTE: The source data (medal_counts_clean.csv) only contains medal-winning
    countries. Therefore, this function will return an empty list because all
    countries in the dataset have won at least one medal. To properly identify
    "never-won" countries, we would need a complete list of all NOCs that have
    participated but never won a medal.
    """
    medal_counts = df.groupby('noc')['total_medals'].sum()
    never_won = medal_counts[medal_counts == 0].index.tolist()
    print(f"   Found {len(never_won)} countries that have never won a medal")
    return never_won


def create_regional_spillover(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create regional spillover feature (neighbors' medal success).

    Args:
        df: Feature DataFrame

    Returns:
        DataFrame with regional spillover column
    """
    df = df.copy()

    # Add continent column
    df['continent'] = df['noc'].map(COUNTRY_TO_CONTINENT)
    df['continent'] = df['continent'].fillna('Other')

    # Calculate regional spillover: average medals of same-continent countries
    # (excluding self)
    yearly_avg = df.groupby(['year', 'continent'])['total_medals'].transform('mean')
    df['regional_spillover'] = yearly_avg

    return df


def prepare_first_time_data(df: pd.DataFrame, never_won: list) -> tuple:
    """
    Prepare data for first-time medalist prediction.

    Args:
        df: Feature DataFrame
        never_won: List of never-won country NOCs

    Returns:
        (X_train, y_train, X_2028, feature_names)

    NOTE: Due to data limitation (no zero-medal countries), this function
    will work with an empty or very small subset. For proper implementation,
    we need data augmentation to include countries that participated but
    never won medals.
    """
    # Filter to never-won countries
    df_never = df[df['noc'].isin(never_won)].copy()

    # Create target: did they win their first medal in this Olympics?
    # For countries that never won, first medal occurs when total_medals > 0
    df_never['first_medal'] = (df_never['total_medals'] > 0).astype(int)

    # Features for first-medal probability
    # logit(p) = eta0 + eta1*log(athletes) + eta2*participation_growth +
    #            eta3*sports_diversity + eta4*regional_spillover

    features = ['athlete_count', 'sports_count', 'participation_growth', 'regional_spillover']

    X = df_never[features].copy()
    X['log_athletes'] = np.log(df_never['athlete_count'] + 1)
    X = X[['log_athletes', 'sports_count', 'participation_growth', 'regional_spillover']]
    X = sm.add_constant(X)

    y = df_never['first_medal'].values

    # Split: use historical data for training, 2024 as "test" for 2028 prediction
    train_idx = df_never['year'] < 2024

    # Create 2028 features (use 2024 as baseline)
    df_2024 = df_never[df_never['year'] == 2024].copy()
    if len(df_2024) > 0:
        df_2028 = df_2024.copy()
        df_2028['year'] = 2028
        df_2028['athlete_count'] = df_2024['athlete_count'].values
        df_2028['sports_count'] = df_2024['sports_count'].values
        df_2028['participation_growth'] = df_2024['participation_growth'].values
        df_2028['regional_spillover'] = df_2024['regional_spillover'].values

        X_2028 = df_2028[['log_athletes', 'sports_count', 'participation_growth', 'regional_spillover']].copy()
        X_2028['log_athletes'] = np.log(df_2028['athlete_count'] + 1)
        X_2028 = X_2028[['log_athletes', 'sports_count', 'participation_growth', 'regional_spillover']]
        X_2028 = sm.add_constant(X_2028)
        noc_list_2028 = df_2028['noc'].values
        country_list_2028 = df_2028['country'].values
    else:
        X_2028 = None
        noc_list_2028 = []
        country_list_2028 = []

    # FIXED: Use direct indexing with boolean mask instead of .iloc
    return X[train_idx], y[train_idx], X_2028, noc_list_2028, country_list_2028, X.columns.tolist()


def train_first_medal_model(X_train: pd.DataFrame, y_train: np.ndarray) -> dict:
    """
    Train logistic regression model for first-medal probability.

    Args:
        X_train: Training features
        y_train: Binary target (1 = first medal)

    Returns:
        Dictionary with fitted model
    """
    # Use statsmodels for detailed output
    model = sm.Logit(y_train, X_train)
    result = model.fit(disp=0, maxiter=100)

    return {
        'model': result,
        'params': result.params,
        'pvalues': result.pvalues,
        'llf': result.llf,
        'aic': result.aic,
        'bic': result.bic
    }


def fit_zero_truncated_nb(historical_first_medals: np.ndarray) -> dict:
    """
    Fit Zero-Truncated Negative Binomial to historical first-time medal counts.

    Args:
        historical_first_medals: Array of medal counts for first-time winners

    Returns:
        Dictionary with parameters (n, p) for NB distribution
    """
    # Filter to positive counts (by definition, first-time winners have > 0)
    positive_medals = historical_first_medals[historical_first_medals > 0]

    if len(positive_medals) < 5:
        # Fall back to simple empirical distribution
        return {
            'method': 'empirical',
            'mean': positive_medals.mean() if len(positive_medals) > 0 else 1,
            'std': positive_medals.std() if len(positive_medals) > 1 else 1
        }

    # Method of moments for NB parameters
    mean = positive_medals.mean()
    var = positive_medals.var()

    if var > mean:  # Overdispersion present
        # NB parameterization: n (size), p
        # E[X] = n(1-p)/p, Var[X] = n(1-p)/p^2
        p = mean / var
        n = mean * p / (1 - p)

        # Ensure valid parameters
        n = max(n, 0.1)
        p = np.clip(p, 0.01, 0.99)

        return {
            'method': 'NB',
            'n': n,
            'p': p,
            'mean': mean,
            'std': np.sqrt(var)
        }
    else:
        # Use Poisson approximation
        return {
            'method': 'Poisson',
            'lambda': mean,
            'mean': mean,
            'std': np.sqrt(mean)
        }


def predict_first_time_medalists(X_2028: pd.DataFrame,
                                  first_medal_model: dict,
                                  count_model: dict,
                                  noc_list: list,
                                  country_list: list) -> pd.DataFrame:
    """
    Predict first-time medalists for 2028.

    Args:
        X_2028: Feature matrix for 2028
        first_medal_model: Fitted logistic model
        count_model: Fitted count distribution parameters
        noc_list: List of NOC codes
        country_list: List of country names

    Returns:
        DataFrame with predictions
    """
    if X_2028 is None or len(noc_list) == 0:
        return pd.DataFrame()

    # Predict probability of first medal
    probs = first_medal_model['model'].predict(X_2028)

    # Expected medal count conditional on first medal
    if count_model['method'] == 'NB':
        # NB mean
        expected_conditional = count_model['n'] * (1 - count_model['p']) / count_model['p']
    elif count_model['method'] == 'Poisson':
        expected_conditional = count_model['lambda']
    else:
        expected_conditional = count_model['mean']

    # Expected total medals = P(first medal) * E[medals | first medal]
    expected_medals = probs * expected_conditional

    # Round for point estimate
    expected_medals_rounded = np.round(expected_medals).astype(int)

    # Create results DataFrame
    results = pd.DataFrame({
        'NOC': noc_list,
        'Country': country_list,
        'Prob_First_Medal': probs,
        'Odds': probs / (1 - probs + 1e-10),
        'Expected_Medals': expected_medals,
        'Pred_Medals_Rounded': expected_medals_rounded
    })

    # Sort by probability
    results = results.sort_values('Prob_First_Medal', ascending=False)

    return results


def bootstrap_expected_count(results: pd.DataFrame, n_bootstraps: int = 1000) -> dict:
    """
    Bootstrap to estimate expected number of first-time medalists.

    Args:
        results: Prediction results with probabilities
        n_bootstraps: Number of bootstrap samples

    Returns:
        Dictionary with bootstrap statistics
    """
    probs = results['Prob_First_Medal'].values

    # Bootstrap: simulate first-medal events
    n_countries = len(probs)
    bootstrap_counts = []

    for _ in range(n_bootstraps):
        # Simulate Bernoulli events
        first_medals = np.random.binomial(1, probs)
        bootstrap_counts.append(first_medals.sum())

    bootstrap_counts = np.array(bootstrap_counts)

    return {
        'mean': bootstrap_counts.mean(),
        'std': bootstrap_counts.std(),
        'median': np.median(bootstrap_counts),
        'ci_lower': np.percentile(bootstrap_counts, 2.5),
        'ci_upper': np.percentile(bootstrap_counts, 97.5)
    }


def main():
    """Main execution function."""
    print("=" * 60)
    print("Model 3: First-Time Medalists")
    print("=" * 60)

    # 1. Load features
    print("\n1. Loading features...")
    df = load_features('implementation/data/features_core.csv')

    # 2. Add regional spillover
    print("\n2. Creating regional spillover feature...")
    df = create_regional_spillover(df)

    # 3. Identify never-won countries
    print("\n3. Identifying never-won countries...")
    print("   NOTE: Dataset only includes medal-winning countries.")
    print("   For proper first-time medalist prediction, we need data on")
    print("   countries that participated but never won medals.")
    never_won = identify_never_won_countries(df)

    # 4. Prepare data
    print("\n4. Preparing data...")
    X_train, y_train, X_2028, noc_list, country_list, feature_names = prepare_first_time_data(df, never_won)
    print(f"   Training samples: {len(y_train)}")
    print(f"   First-medal events in training: {y_train.sum()}")
    print(f"   Never-won countries for 2028 prediction: {len(noc_list)}")

    # 5. Train first-medal probability model
    if len(y_train) > 0:
        print("\n5. Training first-medal probability model...")
        first_medal_model = train_first_medal_model(X_train, y_train)
        print(f"   Log-likelihood: {first_medal_model['llf']:.2f}")
        print(f"   AIC: {first_medal_model['aic']:.2f}")
        print(f"   Parameters:")
        for name, val in first_medal_model['params'].items():
            print(f"     {name}: {val:.4f}")

        # 6. Fit count distribution for first-time medalists
        print("\n6. Fitting count distribution for first-time medalists...")
        # Get historical first-time medal counts
        historical_first = df[df['total_medals'] > 0].groupby('noc')['total_medals'].min().values
        count_model = fit_zero_truncated_nb(historical_first)
        print(f"   Count model: {count_model['method']}")
        print(f"   Expected medals given first medal: {count_model['mean']:.2f}")

        # 7. Predict first-time medalists for 2028
        print("\n7. Predicting first-time medalists for 2028...")
        results = predict_first_time_medalists(X_2028, first_medal_model, count_model, noc_list, country_list)
    else:
        print("\n5. Skipping model training - insufficient data")
        print("   (No zero-medal countries in dataset)")
        first_medal_model = None
        count_model = {'method': 'none', 'mean': 0}
        results = pd.DataFrame()
        bootstrap_stats = {'mean': 0, 'std': 0, 'median': 0, 'ci_lower': 0, 'ci_upper': 0}

    if len(results) > 0:
        # 8. Bootstrap expected count
        print("\n8. Bootstrapping expected number of first-time medalists...")
        bootstrap_stats = bootstrap_expected_count(results)

        print(f"\n   Expected first-time medalists in 2028:")
        print(f"     Mean: {bootstrap_stats['mean']:.1f}")
        print(f"     Median: {bootstrap_stats['median']:.1f}")
        print(f"     95% CI: [{bootstrap_stats['ci_lower']:.0f}, {bootstrap_stats['ci_upper']:.0f}]")

        print(f"\n   Top 20 most likely first-time medalists:")
        top_20 = results.head(20).copy()
        top_20['Odds'] = top_20['Odds'].apply(lambda x: f"{x:.2f}")
        print(top_20[['NOC', 'Country', 'Prob_First_Medal', 'Odds']].to_string(index=False))

        # Filter to those with probability > 0.1 for output
        likely = results[results['Prob_First_Medal'] > 0.05].copy()
    else:
        print("   No never-won countries to predict")
        likely = pd.DataFrame()

    # 9. Save results
    print("\n9. Saving results...")
    if len(results) > 0:
        results.to_csv('output/results/results_3.csv', index=False)
        print(f"   Saved {len(results)} predictions to output/results/results_3.csv")

        # Save summary
        summary = pd.DataFrame([{
            'Expected_First_Time_Medalists': bootstrap_stats['mean'],
            'CI_Lower': bootstrap_stats['ci_lower'],
            'CI_Upper': bootstrap_stats['ci_upper'],
            'Probability_Threshold': 0.1,
            'Countries_Above_Threshold': (results['Prob_First_Medal'] > 0.1).sum()
        }])
        summary.to_csv('output/results/results_3_summary.csv', index=False)

    # 10. Save models
    print("\n10. Saving models...")
    model_bundle = {
        'first_medal_model': first_medal_model,
        'count_model': count_model,
        'feature_names': feature_names,
        'bootstrap_stats': bootstrap_stats,
        'data_limitation_note': 'Dataset only contains medal-winning countries. ' +
                                'Need zero-medal country data for proper prediction.'
    }
    with open('implementation/models/model_3.pkl', 'wb') as f:
        pickle.dump(model_bundle, f)
    print("   Saved to implementation/models/model_3.pkl")

    print("\n" + "=" * 60)
    print("Model 3 Implementation Complete")
    print("=" * 60)

    return results, model_bundle


if __name__ == "__main__":
    results, models = main()
