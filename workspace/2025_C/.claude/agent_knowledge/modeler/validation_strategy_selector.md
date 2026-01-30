# Validation Strategy Selector

> [!CRITICAL]
> **[MANDATORY] ALL models MUST include validation strategy appropriate to data type.**

## Validation Strategy Table

| Component | Requirement | Validation | Must Not Simplify |
|-----------|-------------|------------|-------------------|
| **Validation Strategy** | **Select based on data type** | **Temporal / Spatial / K-Fold / LOOCV / Group** | **YES** |
| Out-of-Sample Metrics | RMSE, MAE, R², accuracy, coverage | At least 2 metrics reported | YES |
| Train/Test Comparison | Check for overfitting | Train vs test performance difference < 20% | YES |
| Uncertainty Quantification | 95% CI/PI or prediction intervals | Required for Bayesian/probabilistic models | YES |
| Holdout Set | Explicit train/test split | No training on test data | YES |

## Strategy Selector (choose ONE based on data type)

| Data Type | Validation Method | Rationale | When to Use |
|-----------|------------------|-----------|-------------|
| **Time Series** | Temporal holdout | Predict future from past | Data has year/date/time column |
| **Spatial** | Spatial holdout | Predict unseen locations | Data has lat/lon/coordinates |
| **Cross-Sectional** | K-fold CV | Generalize across samples | No temporal/spatial structure |
| **Hierarchical/Clustered** | Group K-fold | Respect data structure | Data has group/country/region IDs |
| **Small Sample (<100)** | LOOCV | Maximize training data | Fewer than 100 observations |
| **Optimization** | Test instances | Validate on benchmark | Problem requires optimization |

## Example (for time series data like Olympic medals)

```markdown
### Model 1 Validation Strategy (MANDATORY)

**Data Type**: Time series (years 1896-2024)

**Validation Method**: Temporal holdout
- Train: 1896-2016 (historical data)
- Test: 2020-2024 (future predictions)

**Rationale**: Prevents data leakage; validates model's ability to predict future

**Out-of-Sample Metrics**:
- Test RMSE: Target < 5 medals
- Test MAE: Target < 3 medals
- Test R²: Target > 0.7
- 95% Prediction Interval Coverage: Target 90-95%

**Overfitting Check**:
- Train RMSE / Test RMSE < 1.2
- If ratio > 1.2: Model overfitting, require regularization

**Implementation**:
```python
from implementation.code.validation_strategy import UniversalValidator

validator = UniversalValidator(data, target_column='medals')
splits = validator.create_validation_splits(test_size=0.2)  # Auto-detects temporal

# Train on each split
for fold, (train_idx, test_idx) in enumerate(splits):
    train_data = data.loc[train_idx]
    test_data = data.loc[test_idx]
    # ... model training and evaluation ...
```
```
