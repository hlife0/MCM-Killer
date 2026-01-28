# Protocol 3: Enhanced @time_validator Analysis

> **Purpose**: Fix inaccurate time predictions through comprehensive file reading and line-by-line code analysis
> **Owner**: @time_validator
> **Scope**: Phases 1.5 (Time Estimate), 4.5 (Fidelity Check), 5.5 (Anti-Fraud)

## Problem Statement

Inaccurate time predictions cause planning failures:

```
@time_validator prediction: 16 hours
Actual training time: 43 minutes
Error: 22× underestimate
```

## Enhancements

### Enhancement 1: @time_validator MUST Read 3 File Types

**Required files for analysis**:
1. **Model design**: `output/model/model_design_{i}.md`
2. **Dataset**: `output/implementation/data/features_{i}.pkl` (check shape/size)
3. **Implementation**: `output/implementation/code/model_{i}.py` (line-by-line)

### Enhancement 2: @time_validator MUST Analyze Line-by-Line

**Line-by-line analysis checklist**:
- Import statements (which library?)
- Model definition (what algorithm?)
- Sampling parameters (how many iterations?)
- Loops (nested = O(n²) or O(n³)?)

**Example analysis**:
```
Line 15: import pymc as pm          → Bayesian MCMC (slow)
Line 42: pm.sample(10000, chains=4)  → 40,000 samples
Line 58: for region in regions:      → Nested loop O(n×m)
Line 78: for city in cities:         → Triple nested O(n×m×k)
Verdict: High computational complexity
```

### Enhancement 3: @time_validator MUST Use Empirical Table

**Empirical time estimation table**:

| Algorithm | Dataset | Samples | Expected Time |
|-----------|---------|---------|---------------|
| PyMC hierarchical | 5000×50 | 10000×4 | 12-15 hours |
| sklearn.LinearRegression | ANY | ANY | <0.1 hours |
| Random Forest | 5000×50 | 100 trees | 0.5-1 hours |
| Neural Network | 5000×50 | 1000 epochs | 2-4 hours |

**Accuracy Target**: ±50% of actual time

## Enhanced Analysis Process

### Step 1: Read Model Design

**Extract from `model_design_{i}.md`**:
- Algorithm specification
- Iteration/sampling parameters
- Computational requirements
- Design Expectations Table

### Step 2: Inspect Dataset

**From `features_{i}.pkl`**:
- Shape: (rows, columns)
- Data types
- Memory size
- Feature complexity

### Step 3: Line-by-Line Code Analysis

**From `model_{i}.py`**:
```python
# Example code analysis
import pymc as pm                    # Bayesian MCMC
with pm.Model() as model:
    pm.Normal("mu", mu=0, sigma=10)  # Prior
    likelihood = pm.Normal("y",      # Likelihood
                          mu=mu,
                          sigma=sigma,
                          observed=y)
    trace = pm.sample(10000,          # 10,000 samples
                     chains=4,        # 4 chains
                     tune=2000)       # 2,000 tuning steps

# Analysis:
# Algorithm: PyMC (slow)
# Samples: 10,000 × 4 = 40,000 posterior samples
# Tuning: 2,000 iterations
# Dataset: 5,000 rows × 50 columns
# Expected: 12-15 hours (from empirical table)
```

### Step 4: Cross-Reference with Empirical Table

**Match algorithm + dataset + samples** → Get expected time

### Step 5: Provide Estimate with Uncertainty

**Output format**:
```
Model {i}: PyMC hierarchical, 5000×50, 10000×4 chains
Estimated: 12-15 hours (range: 10-20 hours)
Algorithm: Exact match (PyMC)
Features: All 15 present
Verdict: VALID
```

## Accuracy Target

**Goal**: ±50% of actual time

**Example**:
- Predicted: 12-15 hours
- Actual: 14 hours → Accuracy: 93% (within target)
- Predicted: 12-15 hours
- Actual: 43 minutes → Error: 22× (VIOLATION)

## Common Mistakes to Avoid

**MISTAKE 1**: Not reading code
- Result: Miss sklearn disguised as "Bayesian"

**MISTAKE 2**: Not checking dataset size
- Result: 500×50 treated same as 5000×50

**MISTAKE 3**: Not counting iterations
- Result: 1000 samples treated same as 10000

**MISTAKE 4**: Not using empirical table
- Result: Guessing instead of data-driven estimates

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
