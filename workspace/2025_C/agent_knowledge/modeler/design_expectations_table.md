# Design Expectations Table Template

**Purpose**: This template defines the mandatory Design Expectations Table that MUST be included for every model. This table is CRITICAL for @time_validator to validate @code_translator's implementation and prevent unauthorized simplifications.

**Source**: Extracted from modeler.md lines 946-1161

---

## Design Expectations Table (v2.5.7 MANDATORY)

> [!CRITICAL] **[v2.5.7 MANDATORY] You MUST include a Design Expectations Table for EVERY model.**
>
> This table is CRITICAL for @time_validator to validate @code_translator's implementation.
> Without this table, validation is impossible.

### Design Expectations Table Template

**For EACH model, include the following table:**

```markdown
## Model {i} Design Expectations (MANDATORY)

### Category 1: Sampling Algorithm (if applicable)
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Sampler | NUTS / Slice / Metropolis | [specify] | [specify] | - | YES / NO |
| Gradient Calculation | Auto-diff / Finite diff | [specify] | [specify] | - | YES / NO |
| Tree Depth | [value] | [min] | [max] | layers | YES / NO |
| Iterations per draw | ~[value] | [min] | [max] | gradient evals | YES / NO |

### Category 2: MCMC Parameters (if applicable)
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Chains | [value] | [value] | [value] | chains | YES |
| Tune samples | [value] | [value] | [value] | samples | YES |
| Draw samples | [value] | [value] | [value] | samples | YES |
| Total iterations | [value] | [value] | [value] | samples | YES |

### Category 3: Neural Network Parameters (if applicable)
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Hidden layers | [value] | [value] | [value] | layers | YES |
| Hidden units | [value] | [value] | [value] | units | YES |
| Training epochs | [value] | [value] | [value] | epochs | YES |
| Batch size | [value] | [value] | [value] | samples | NO |
| Learning rate | [value] | [min] | [max] | - | NO |

### Category 4: Ensemble Parameters (if applicable)
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Base models | [value] | [value] | [value] | models | YES |
| Bootstrap samples | [value] | [value] | [value] | samples | YES |
| Hyperparameter combinations | [value] | [value] | [value] | combinations | YES |

### Category 5: Features
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Total features | [count] | [count] | [count] | features | YES |
| Specific features | [list all features] | ALL | ALL | - | YES |

### Category 6: Computational Requirements
| Parameter | Design Specification | Minimum Acceptable | Maximum Acceptable | Unit | Must Not Simplify |
|-----------|---------------------|-------------------|-------------------|------|-------------------|
| Training time | [range] | [min] | [max] | hours | NO* |
| Memory usage | [estimate] | [max] | [max] | GB | NO |

*Training time has tolerance: if algorithm correct but faster/slower, investigate but don't auto-reject

### Category 7: Out-of-Sample Validation

> [!CRITICAL]
> **[MANDATORY] ALL models MUST include validation strategy appropriate to data type.**

| Component | Requirement | Validation | Must Not Simplify |
|-----------|-------------|------------|-------------------|
| **Validation Strategy** | **Select based on data type** | **Temporal / Spatial / K-Fold / LOOCV / Group** | **YES** |
| Out-of-Sample Metrics | RMSE, MAE, R², accuracy, coverage | At least 2 metrics reported | YES |
| Train/Test Comparison | Check for overfitting | Train vs test performance difference < 20% | YES |
| Uncertainty Quantification | 95% CI/PI or prediction intervals | Required for Bayesian/probabilistic models | YES |
| Holdout Set | Explicit train/test split | No training on test data | YES |

**Validation Strategy Selector (choose ONE based on data type)**:

| Data Type | Validation Method | Rationale | When to Use |
|-----------|------------------|-----------|-------------|
| **Time Series** | Temporal holdout | Predict future from past | Data has year/date/time column |
| **Spatial** | Spatial holdout | Predict unseen locations | Data has lat/lon/coordinates |
| **Cross-Sectional** | K-fold CV | Generalize across samples | No temporal/spatial structure |
| **Hierarchical/Clustered** | Group K-fold | Respect data structure | Data has group/country/region IDs |
| **Small Sample (<100)** | LOOCV | Maximize training data | Fewer than 100 observations |
| **Optimization** | Test instances | Validate on benchmark | Problem requires optimization |

**Example (for time series data like Olympic medals)**:

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

### Design Rationale (MANDATORY)

For each CRITICAL parameter (Must Not Simplify = YES), provide rationale:

```markdown
#### Rationale for Critical Parameters

**Sampler: NUTS**
- **Why**: Hamiltonian Monte Carlo with automatic tuning for efficient posterior exploration
- **Alternatives considered**: Slice (simpler, less efficient), Metropolis (random walk, slow)
- **Cannot simplify to**: Slice, Metropolis, or any non-HMC method without approval

**Chains: 4**
- **Why**: Convergence diagnostics (R-hat) require ≥4 chains for reliable assessment
- **Alternatives considered**: 2 chains (insufficient for R-hat)
- **Cannot simplify to**: < 4 chains

**Draws: 20000**
- **Why**: Posterior convergence and effective sample size require 20000+ samples
- **Tolerance**: ±20% (16000-24000 acceptable)
- **Cannot simplify to**: < 16000 (below tolerance)

**Total Features: 15**
- **Why**: Model specification requires all 15 features for accurate prediction
- **List**: GDP, host_advantage, years, Gold, Silver, Bronze, ...
- **Cannot simplify to**: < 15 features
```
```

### Example: Complete Design Expectations Table

```markdown
## Model 1 Design Expectations

### Category 1: Sampling Algorithm
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS (No-U-Turn Sampler) | NUTS | NUTS | - | YES |
| Tree Depth | 5-10 | 5 | 10 | layers | YES |
| Target Accept | 0.95 | 0.85 | 1.0 | - | NO |

### Category 2: MCMC Parameters
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Chains | 4 | 4 | 4 | chains | YES |
| Tune | 2000 | 2000 | 2000 | samples | YES |
| Draws | 20000 | 16000 | 24000 | samples | YES |
| Total | 88000 | 70400 | 105600 | samples | YES |

### Category 3: Features
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Total features | 15 | 15 | 15 | features | YES |
| Required features | GDP, host_advantage, years_participated, Gold, Silver, Bronze, population, GDP_per_capita, previous_medals, host_history, continent, sport_count, athlete_count, event_count, coach_count | ALL | ALL | - | YES |

### Category 4: Computational Requirements
| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Training time | 12-18 | 12 | 18 | hours | NO |

### Design Rationale

**Sampler: NUTS**
- **Why**: HMC with automatic tuning for Bayesian hierarchical models
- **Alternatives**: Slice (simpler), Metropolis (less efficient)
- **Cannot simplify**: Must use NUTS for acceptable performance

**Chains: 4**
- **Why**: R-hat convergence diagnostic requires ≥4 chains
- **Cannot simplify**: <4 chains invalidates convergence assessment

**Draws: 20000, Tune: 2000**
- **Why**: Posterior convergence and effective sample size >1000 per parameter
- **Tolerance**: ±20% (16000-24000 acceptable)
- **Cannot simplify**: <16000 below tolerance, requires approval

**Features: 15 total**
- **Why**: Model specification requires all features for unbiased estimation
- **List**: [see above]
- **Cannot simplify**: Missing features = biased estimates = invalid model
```

### Why This Is Critical

**Without Design Expectations Table**:
- @code_translator may simplify (20000 → 1000 samples)
- @time_validator has no basis to detect simplification
- Result: Academic fraud through lazy implementation

**With Design Expectations Table**:
- @time_validator creates comparison table (Design vs Actual vs Tolerance vs Verdict)
- @director enforces "one fail = all fail" rule
- Result: Implementation matches design exactly
