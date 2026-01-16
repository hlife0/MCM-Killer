#!/usr/bin/env python3
"""
Model 2: 2028 LA Projections (Hierarchical AR Model)
Based on: output/model_design.md
Translated by: @code_translator

This model implements an Autoregressive model for 2028 medal projections
with momentum and host advantage effects.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.utils import resample
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from scipy import stats
import pickle
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)


def load_features(path: str = 'implementation/data/features_core.csv') -> pd.DataFrame:
    """Load feature data from CSV file."""
    df = pd.read_csv(path)

    # Handle missing values
    df['prev_total_medals'] = df['prev_total_medals'].fillna(0)
    df['prev_gold_count'] = df['prev_gold_count'].fillna(0)
    df['medal_trend_3'] = df['medal_trend_3'].fillna(0)

    # FIXED: Handle inf values in participation_growth (e.g., Egypt 1984: first participation)
    # Replace inf and -inf with 0
    df['participation_growth'] = df['participation_growth'].fillna(0)
    df['participation_growth'] = df['participation_growth'].replace([np.inf, -np.inf], 0)

    print(f"Loaded features: {df.shape}")
    return df


def create_lag_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create lag features for autoregressive modeling.

    Args:
        df: Feature DataFrame

    Returns:
        DataFrame with lag features
    """
    df = df.sort_values(['noc', 'year'])

    # Create lags for each country
    df['lag1_total'] = df.groupby('noc')['total_medals'].shift(1)  # t-1 (4 years)
    df['lag2_total'] = df.groupby('noc')['total_medals'].shift(2)  # t-2 (8 years)
    df['lag1_gold'] = df.groupby('noc')['gold_count'].shift(1)
    df['lag2_gold'] = df.groupby('noc')['gold_count'].shift(2)

    # Momentum: recent trend
    df['momentum'] = df.groupby('noc')['total_medals'].apply(
        lambda x: x.rolling(window=3, min_periods=1).apply(lambda y: np.polyfit(range(len(y)), y, 1)[0] if len(y) > 1 else 0, raw=True)
    ).reset_index(level=0, drop=True)

    # Fill missing lags
    df['lag1_total'] = df['lag1_total'].fillna(0)
    df['lag2_total'] = df['lag2_total'].fillna(0)
    df['lag1_gold'] = df['lag1_gold'].fillna(0)
    df['lag2_gold'] = df['lag2_gold'].fillna(0)
    df['momentum'] = df['momentum'].fillna(0)

    return df


def prepare_ar_data(df: pd.DataFrame, test_year: int = 2020) -> tuple:
    """
    Prepare data for AR model training.

    Args:
        df: Feature DataFrame
        test_year: Year to use for test split

    Returns:
        (X_train, X_test, y_train, y_test, feature_names)
    """
    # Features for AR model
    ar_features = [
        'is_host',
        'lag1_total',
        'lag2_total',
        'momentum',
        'athlete_count',
        'participation_growth'
    ]

    X = df[ar_features].copy()
    X['log_athletes'] = np.log(df['athlete_count'] + 1)
    X = X[['is_host', 'lag1_total', 'lag2_total', 'momentum', 'log_athletes', 'participation_growth']]

    # Add constant
    X = sm.add_constant(X)

    # Target
    y = df['total_medals'].values

    # Temporal split
    train_idx = df['year'] < test_year
    test_idx = df['year'] >= test_year

    # FIXED: Use direct indexing with boolean mask instead of .iloc
    return (X[train_idx], X[test_idx],
            y[train_idx], y[test_idx],
            X.columns.tolist())


def train_ar_model(X_train: pd.DataFrame, y_train: np.ndarray) -> dict:
    """
    Train autoregressive model for medal projections.

    Args:
        X_train: Training features
        y_train: Training targets

    Returns:
        Dictionary with fitted model and parameters
    """
    # Use OLS for interpretability
    model = sm.OLS(y_train, X_train)
    result = model.fit_regularized(alpha=0.1, L1_wt=0.5)  # Elastic Net

    # Also fit unregularized for comparison
    model_ols = sm.OLS(y_train, X_train)
    result_ols = model_ols.fit(disp=0)

    return {
        'model': result_ols,
        'model_regularized': result,
        'params': result_ols.params,
        'pvalues': result_ols.pvalues,
        'rsquared': result_ols.rsquared,
        'aic': result_ols.aic,
        'bic': result_ols.bic
    }


def detect_regime_change(medals_series: np.ndarray) -> tuple:
    """
    Detect structural regime changes using Chow test approximation.

    Args:
        medals_series: Time series of medal counts

    Returns:
        (has_breakpoint, breakpoint_idx, f_statistic)
    """
    if len(medals_series) < 8:
        return False, None, 0

    f_stats = []
    for bp in range(3, len(medals_series) - 3):
        # Split at potential breakpoint
        y1 = medals_series[:bp]
        y2 = medals_series[bp:]

        if len(y1) < 3 or len(y2) < 3:
            continue

        # Fit separate models
        x1 = np.arange(len(y1))
        x2 = np.arange(len(y2))

        try:
            # Separate regressions
            coef1 = np.polyfit(x1, y1, 1)
            coef2 = np.polyfit(x2, y2, 1)

            # Pooled regression
            x_all = np.arange(len(medals_series))
            coef_pooled = np.polyfit(x_all, medals_series, 1)

            # Residual sums of squares
            rss1 = np.sum((y1 - np.polyval(coef1, x1))**2)
            rss2 = np.sum((y2 - np.polyval(coef2, x2))**2)
            rss_pooled = np.sum((medals_series - np.polyval(coef_pooled, x_all))**2)

            # Chow test F-statistic
            k = 2  # parameters
            n = len(medals_series)
            f_stat = ((rss_pooled - (rss1 + rss2)) / k) / ((rss1 + rss2) / (n - 2*k))

            f_stats.append((bp, f_stat))
        except Exception:
            continue

    if not f_stats:
        return False, None, 0

    # Find maximum F-statistic
    bp, f_max = max(f_stats, key=lambda x: x[1])

    # Critical value at alpha=0.05
    has_break = f_max > 4.0  # Approximate critical value

    return has_break, bp, f_max


def predict_2028(df: pd.DataFrame, ar_model: dict, use_regime: bool = True) -> pd.DataFrame:
    """
    Generate 2028 predictions using AR model.

    Args:
        df: Feature DataFrame
        ar_model: Fitted AR model
        use_regime: Whether to use regime-aware predictions

    Returns:
        DataFrame with 2028 predictions
    """
    # Get countries with recent data
    recent = df[df['year'] == 2024].copy()

    # Create 2028 features
    pred_2028 = recent.copy()
    pred_2028['year'] = 2028

    # Lag features
    pred_2028['lag1_total'] = recent['total_medals'].values
    pred_2028['lag2_total'] = recent.groupby('noc')['total_medals'].shift(1).fillna(0).values
    pred_2028['momentum'] = recent['medal_trend_3'].values * 0.5  # Decay momentum

    # Host advantage
    pred_2028['is_host'] = 0
    usa_idx = pred_2028['noc'] == 'USA'
    pred_2028.loc[usa_idx, 'is_host'] = 1

    # Participation
    pred_2028['athlete_count'] = recent['athlete_count'].values
    pred_2028['participation_growth'] = 0  # No data yet

    # Prepare feature matrix
    X_2028 = pred_2028[['is_host', 'lag1_total', 'lag2_total', 'momentum', 'athlete_count', 'participation_growth']].copy()
    X_2028['log_athletes'] = np.log(pred_2028['athlete_count'] + 1)
    X_2028 = X_2028[['is_host', 'lag1_total', 'lag2_total', 'momentum', 'log_athletes', 'participation_growth']]
    X_2028 = sm.add_constant(X_2028, has_constant='add')

    # Ensure columns match training
    expected_cols = ar_model['params'].index.tolist()
    for col in expected_cols:
        if col not in X_2028.columns:
            X_2028[col] = 0
    X_2028 = X_2028[expected_cols]

    # Predict total medals
    pred_total = ar_model['model'].predict(X_2028)
    pred_total = np.maximum(pred_total, 0)  # No negative predictions
    pred_total = np.round(pred_total).astype(int)

    # Predict gold medals (proportional model)
    gold_ratio = recent['gold_count'] / (recent['total_medals'] + 1)
    avg_gold_ratio = gold_ratio.mean()

    pred_gold = pred_total * gold_ratio.fillna(avg_gold_ratio).values
    pred_gold = np.round(pred_gold).astype(int)
    pred_gold = np.minimum(pred_gold, pred_total)

    # Calculate improvement/decline
    medals_2024 = recent['total_medals'].values
    delta = pred_total - medals_2024

    # Bootstrap for prediction intervals (simplified)
    # Use standard errors from model
    predictions = ar_model['model'].get_prediction(X_2028)
    pred_int = predictions.conf_int(alpha=0.05)

    pi_lower = np.maximum(0, pred_int[:, 0]).astype(int)
    pi_upper = (pred_int[:, 1] + 1).astype(int)

    # Classification of improvers/decliners
    # Using delta > 1 as threshold for meaningful change
    is_improver = delta > 1
    is_decliner = delta < -1
    is_stable = ~is_improver & ~is_decliner

    # Create results
    results = pd.DataFrame({
        'NOC': pred_2028['noc'].values,
        'Country': pred_2028['country'].values,
        'Medals_2024': medals_2024,
        'Pred_Total_2028': pred_total,
        'Pred_Gold_2028': pred_gold,
        'Delta': delta,
        'PI_2.5': pi_lower,
        'PI_97.5': pi_upper,
        'Improver': is_improver,
        'Decliner': is_decliner,
        'Stable': is_stable
    })

    return results


def generate_medal_table(results: pd.DataFrame) -> pd.DataFrame:
    """
    Generate official-style medal table for 2028.

    Args:
        results: Prediction results

    Returns:
        Sorted medal table
    """
    medal_table = results[['NOC', 'Country', 'Pred_Gold_2028', 'Pred_Total_2028']].copy()

    # Sort by gold, then total (official Olympic ranking)
    medal_table = medal_table.sort_values(['Pred_Gold_2028', 'Pred_Total_2028'], ascending=False)
    medal_table['Rank'] = range(1, len(medal_table) + 1)

    return medal_table


def analyze_improvers_decliners(results: pd.DataFrame) -> dict:
    """
    Analyze predicted improvers and decliners.

    Args:
        results: Prediction results

    Returns:
        Dictionary with analysis
    """
    improvers = results[results['Improver']].sort_values('Delta', ascending=False)
    decliners = results[results['Decliner']].sort_values('Delta')

    # Countries with largest expected changes
    top_improvers = improvers.head(10)[['NOC', 'Country', 'Medals_2024', 'Pred_Total_2028', 'Delta']]
    top_decliners = decliners.head(10)[['NOC', 'Country', 'Medals_2024', 'Pred_Total_2028', 'Delta']]

    return {
        'n_improvers': len(improvers),
        'n_decliners': len(decliners),
        'n_stable': results['Stable'].sum(),
        'top_improvers': top_improvers,
        'top_decliners': top_decliners
    }


def main():
    """Main execution function."""
    print("=" * 60)
    print("Model 2: 2028 LA Projections (AR Model)")
    print("=" * 60)

    # 1. Load features
    print("\n1. Loading features...")
    df = load_features('implementation/data/features_core.csv')

    # 2. Create lag features
    print("\n2. Creating lag features...")
    df = create_lag_features(df)

    # 3. Prepare data
    print("\n3. Preparing data...")
    X_train, X_test, y_train, y_test, feature_names = prepare_ar_data(df, test_year=2020)
    print(f"   Training samples: {len(y_train)}")
    print(f"   Test samples: {len(y_test)}")

    # 4. Train AR model
    print("\n4. Training AR model...")
    ar_model = train_ar_model(X_train, y_train)
    print(f"   R-squared: {ar_model['rsquared']:.3f}")
    print(f"   AIC: {ar_model['aic']:.1f}")
    print(f"   Parameters:")
    for name, val in ar_model['params'].items():
        print(f"     {name}: {val:.4f}")

    # 5. Evaluate on test set
    print("\n5. Evaluating on test set...")
    y_pred_test = ar_model['model'].predict(X_test)
    y_pred_test = np.round(y_pred_test).astype(int)
    y_pred_test = np.maximum(y_pred_test, 0)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    r2 = r2_score(y_test, y_pred_test)
    print(f"   Test RMSE: {rmse:.3f}")
    print(f"   Test R2: {r2:.3f}")

    # 6. Detect regime changes for major countries
    print("\n6. Detecting regime changes...")
    major_countries = df[df['year'] == 2024].sort_values('total_medals', ascending=False).head(10)['noc'].values

    regime_changes = []
    for noc in major_countries:
        country_data = df[df['noc'] == noc]['total_medals'].values
        has_break, bp, f_stat = detect_regime_change(country_data)
        if has_break:
            regime_changes.append((noc, bp, f_stat))

    if regime_changes:
        print(f"   Detected {len(regime_changes)} regime changes:")
        for noc, bp, f_stat in regime_changes:
            print(f"     {noc}: F={f_stat:.2f}")
    else:
        print("   No significant regime changes detected")

    # 7. Generate 2028 predictions
    print("\n7. Generating 2028 predictions...")
    results = predict_2028(df, ar_model)

    # 8. Generate medal table
    print("\n8. Generating 2028 medal table...")
    medal_table = generate_medal_table(results)
    print(f"\n   Top 15 countries for 2028:")
    print(medal_table.head(15).to_string(index=False))

    # 9. Analyze improvers/decliners
    print("\n9. Analyzing changes from 2024...")
    analysis = analyze_improvers_decliners(results)
    print(f"   Predicted improvers: {analysis['n_improvers']}")
    print(f"   Predicted decliners: {analysis['n_decliners']}")
    print(f"   Predicted stable: {analysis['n_stable']}")

    print(f"\n   Top 10 predicted improvers:")
    print(analysis['top_improvers'].to_string(index=False))

    # 10. Save results
    print("\n10. Saving results...")
    results.to_csv('output/results/results_2_predictions.csv', index=False)
    medal_table.to_csv('output/results/results_2.csv', index=False)
    print("   Saved to output/results/results_2.csv")

    # 11. Save model
    print("\n11. Saving model...")
    model_bundle = {
        'ar_model': ar_model,
        'feature_names': feature_names,
        'regime_changes': regime_changes,
        'metrics': {'RMSE': rmse, 'R2': r2}
    }
    with open('implementation/models/model_2.pkl', 'wb') as f:
        pickle.dump(model_bundle, f)
    print("   Saved to implementation/models/model_2.pkl")

    print("\n" + "=" * 60)
    print("Model 2 Implementation Complete")
    print("=" * 60)

    return results, medal_table, model_bundle


if __name__ == "__main__":
    results, medal_table, models = main()
