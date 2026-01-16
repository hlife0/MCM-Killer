#!/usr/bin/env python3
"""
Model 1: Medal Count Model
Based on: output/model_design.md
Translated by: @code_translator

Simplified implementation using Ridge regression for medal count prediction.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import pickle
import warnings
import os
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
    df['participation_growth'] = df['participation_growth'].fillna(0)

    print(f"Loaded features: {df.shape}")
    return df


def prepare_data(df: pd.DataFrame, test_year: int = 2020) -> tuple:
    """Prepare data for model training with temporal split."""
    # Features for prediction
    features = ['is_host', 'log_athletes', 'log_sports', 'prev_total_medals', 'medal_trend_3']

    # Create log features
    df_copy = df.copy()
    df_copy['log_athletes'] = np.log(df['athlete_count'] + 1)
    df_copy['log_sports'] = np.log(df['sports_count'] + 1)

    X = df_copy[features].copy()
    y = df['total_medals'].values

    # Temporal split
    train_mask = df['year'].values < test_year
    test_mask = df['year'].values >= test_year

    train_indices = np.where(train_mask)[0]
    test_indices = np.where(test_mask)[0]

    X_train = X.iloc[train_indices].reset_index(drop=True)
    X_test = X.iloc[test_indices].reset_index(drop=True)
    y_train = y[train_indices]
    y_test = y[test_indices]

    return X_train, X_test, y_train, y_test, features


def train_model(X_train: pd.DataFrame, y_train: np.ndarray) -> dict:
    """Train Ridge regression model for medal prediction."""
    model = Ridge(alpha=1.0, random_state=RANDOM_STATE)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_train)

    # Calculate metrics
    rmse = np.sqrt(mean_squared_error(y_train, y_pred))
    r2 = r2_score(y_train, y_pred)

    return {
        'model': model,
        'coef': model.coef_,
        'intercept': model.intercept_,
        'feature_names': X_train.columns.tolist(),
        'rmse': rmse,
        'r2': r2
    }


def gold_model_predict(df: pd.DataFrame, total_predictions: np.ndarray) -> np.ndarray:
    """Predict gold medals as a fraction of total medals."""
    avg_gold_ratio = 0.33

    if 'prev_gold_count' in df.columns and 'prev_total_medals' in df.columns:
        gold_ratio = df['prev_gold_count'] / (df['prev_total_medals'] + 1)
        gold_ratio = gold_ratio.fillna(avg_gold_ratio)
    else:
        gold_ratio = pd.Series([avg_gold_ratio] * len(df))

    host_idx = df['is_host'].values if 'is_host' in df.columns else np.zeros(len(df))
    host_gold_boost = 0.05

    gold_predictions = total_predictions * (gold_ratio.values + host_idx * host_gold_boost)
    gold_predictions = np.minimum(gold_predictions, total_predictions)
    gold_predictions = np.maximum(gold_predictions, 0)

    return np.round(gold_predictions).astype(int)


def predict_2028(df: pd.DataFrame, model: dict) -> pd.DataFrame:
    """Generate predictions for 2028 Los Angeles Olympics."""
    # Get countries from most recent data
    recent = df[df['year'] == 2024].copy()

    if len(recent) == 0:
        latest_year = df['year'].max()
        recent = df[df['year'] == latest_year].copy()

    # Create 2028 features
    pred_2028 = recent.copy()
    pred_2028['year'] = 2028
    pred_2028['prev_total_medals'] = recent['total_medals'].values
    pred_2028['medal_trend_3'] = recent['medal_trend_3'].values * 0.8
    pred_2028['is_host'] = 0
    pred_2028['log_athletes'] = np.log(recent['athlete_count'] + 1)
    pred_2028['log_sports'] = np.log(recent['sports_count'] + 1)

    # USA is host in 2028
    usa_idx = pred_2028['noc'] == 'USA'
    if usa_idx.any():
        pred_2028.loc[usa_idx, 'is_host'] = 1

    # Prepare features
    features = model['feature_names']
    X_2028 = pred_2028[features]

    # Predict
    pred_total = model['model'].predict(X_2028)
    pred_total = np.round(pred_total).astype(int)
    pred_total = np.maximum(pred_total, 0)

    # Predict gold
    pred_gold = gold_model_predict(pred_2028, pred_total)

    # Create results
    results = pd.DataFrame({
        'NOC': pred_2028['noc'].values,
        'Country': pred_2028['country'].values,
        'Pred_Total_2028': pred_total,
        'Pred_Gold_2028': pred_gold,
    })

    # Add prediction intervals
    std_error = np.sqrt(pred_total + 1)
    results['PI_2.5'] = np.maximum(0, pred_total - 1.96 * std_error).astype(int)
    results['PI_97.5'] = (pred_total + 1.96 * std_error).astype(int)
    results['PI_2.5'] = np.minimum(results['PI_2.5'], results['Pred_Total_2028'])
    results['PI_97.5'] = np.maximum(results['PI_97.5'], results['Pred_Total_2028'])

    return results


def main():
    """Main execution function."""
    print("=" * 60)
    print("Model 1: Medal Count Model")
    print("=" * 60)

    # 1. Load features
    print("\n1. Loading features...")
    df = load_features('implementation/data/features_core.csv')

    # 2. Prepare data
    print("\n2. Preparing data...")
    X_train, X_test, y_train, y_test, features = prepare_data(df, test_year=2020)
    print(f"   Training samples: {len(y_train)}")
    print(f"   Test samples: {len(y_test)}")
    print(f"   Features: {features}")

    # 3. Train model
    print("\n3. Training model...")
    model = train_model(X_train, y_train)
    print(f"   Training RMSE: {model['rmse']:.3f}")
    print(f"   Training R2: {model['r2']:.3f}")

    # 4. Evaluate on test set
    print("\n4. Evaluating on test set...")
    y_pred_test = model['model'].predict(X_test)
    y_pred_test = np.round(y_pred_test).astype(int)
    y_pred_test = np.maximum(y_pred_test, 0)

    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    test_r2 = r2_score(y_test, y_pred_test)
    print(f"   Test RMSE: {test_rmse:.3f}")
    print(f"   Test R2: {test_r2:.3f}")

    # 5. Generate 2028 predictions
    print("\n5. Generating 2028 predictions...")
    results_2028 = predict_2028(df, model)

    # Sort and rank
    results_2028 = results_2028.sort_values('Pred_Total_2028', ascending=False)
    results_2028['Rank'] = range(1, len(results_2028) + 1)

    print(f"\n   Top 15 countries predicted for 2028:")
    print(results_2028[['Rank', 'NOC', 'Country', 'Pred_Gold_2028', 'Pred_Total_2028']].head(15).to_string(index=False))

    # 6. Save results
    print("\n6. Saving results...")
    os.makedirs('output/results', exist_ok=True)
    os.makedirs('implementation/models', exist_ok=True)

    output_path = 'output/results/results_1.csv'
    results_2028.to_csv(output_path, index=False)
    print(f"   Saved to {output_path}")

    # 7. Save model
    print("\n7. Saving model...")
    model_bundle = {
        'model': model,
        'test_metrics': {'rmse': test_rmse, 'r2': test_r2}
    }
    with open('implementation/models/model_1.pkl', 'wb') as f:
        pickle.dump(model_bundle, f)
    print("   Saved to implementation/models/model_1.pkl")

    print("\n" + "=" * 60)
    print("Model 1 Implementation Complete")
    print("=" * 60)

    return results_2028, model_bundle


if __name__ == "__main__":
    results, models = main()
