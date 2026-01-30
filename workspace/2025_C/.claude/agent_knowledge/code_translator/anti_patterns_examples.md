# Real-World Anti-Patterns (v2.5.7 MANDATORY STUDY)

> [!CAUTION] **[MANDATORY] Study these real examples of lazy implementation.**
>
> These are **FORBIDDEN PATTERNS** detected by @time_validator. DO NOT repeat these mistakes.

## Anti-Pattern 1: Algorithm Substitution (sklearn vs PyMC)

**❌ FORBIDDEN: sklearn When Design Specifies Bayesian**

```python
# REAL EXAMPLE FROM Model 5 (model_5_changepoint.py:139-142)
# Design: "Bayesian change point detection with PyMC"
# Implementation: Used sklearn.linear_model.PoissonRegressor

from sklearn.linear_model import PoissonRegressor  # ← WRONG!
model = PoissonRegressor(alpha=0, max_iter=1000)
model.fit(X, medals)
mu_pred = model.predict(X)
```

**Why Wrong**: Design specified Bayesian inference, sklearn is frequentist (no posterior distributions), algorithm fundamentally changed, no approval

**v2.5.7 Verdict**: ❌ **AUTO-REJECT** (Algorithm mismatch)

**✅ CORRECT Approach**:
```python
import pymc as pm
with pm.Model() as model:
    tau = pm.DiscreteUniform('tau', lower=0, upper=T)
    pm.Poisson('y', mu=mu, observed=medals)
    trace = pm.sample(5000, tune=2000, chains=4)
```

**What To Do When PyMC Fails**:
```
Director, PyMC API incompatibility detected in Model 5.
Error: [specific error message]
Options:
1. Fix PyMC version/installation
2. Update model design to use compatible PyMC API
3. DO NOT switch to sklearn (simplification = fraud)
Awaiting guidance.
```

---

## Anti-Pattern 2: Training Duration Red Line Violation

**❌ FORBIDDEN: Training Time < 30% of Expected**

```python
# REAL EXAMPLE FROM Model 1
# Design: "Expected training time: 3-5 hours"
# Actual: "Training completed in 0.31 hours (18.7 minutes)"

trace = pm.sample(tune=5000, draws=5000, chains=4)
# But training finished in 18.7 minutes instead of 3-5 hours!
```

**Why Suspicious**: Expected 3-5 hours (180-300 min), Actual 18.7 min, **10× below minimum**, **3× below red line** (30% threshold = 54 min)

**v2.5.7 Verdict**: ❌ **AUTO-REJECT** (Training < 30% of expected)

**What To Do**:
1. **Verify**: Check actual algorithm used (not just parameters)
2. **Report**: If training is suspiciously fast, tell @director BEFORE reporting completion
3. **Do NOT**: Claim "all good" when training is 10× faster than expected

---

## Anti-Pattern 3: Massive Iteration Reduction

**❌ FORBIDDEN: Reduce Iterations Beyond ±20% Tolerance**

```python
# REAL EXAMPLE FROM Quick Training 5A
# Design: "5000 tune + 5000 draws, 4 chains"
# Quick training: "100 tune + 100 draws, 2 chains"

trace = pm.sample(tune=100, draws=100, chains=2)  # ← 50× reduction!
```

**v2.5.7 Tolerance**: ±20% maximum, **Actual**: 2000-10000% beyond tolerance

| Model | Expected | Quick Training | Reduction | Verdict |
|-------|----------|----------------|-----------|---------|
| Model 1 | 5000+5000 | 100+100 | **50×** | ❌ EXCEEDS |
| Model 2 | 10,000 MC | 100 | **100×** | ❌ EXCEEDS |
| Model 3 | 3000+1000 | 100+50 | **30×/20×** | ❌ EXCEEDS |
| Model 4 | 50,000 VI | 1000 | **50×** | ❌ EXCEEDS |
| Model 6 | 1000 bootstrap | 10 | **100×** | ❌ EXCEEDS |

**Rule**: ±10% OK, ±20% max, **>±20% ❌ FORBIDDEN** (requires @director approval)

---

## Anti-Pattern 4: Feature Workarounds ("Use Available Columns")

**❌ FORBIDDEN: Hardcoded Columns Instead of All Features**

```python
# REAL EXAMPLE FROM Model 6
# Design: "15 features including Gold, Silver, Bronze, ..."
# Implementation: Hardcoded 3 columns

inputs_cols = ['AthleteCount', 'EventCount', 'YearsParticipated']
outputs_cols = ['Gold', 'Silver', 'Bronze']  # ← Only 3 features!
```

**Why Wrong**: Design specified 15 features, code only uses 6 hardcoded columns, missing 9 features

**v2.5.7 Verdict**: ❌ **INCOMPLETE** (Only 6/15 features)

**✅ CORRECT**:
```python
available_features = [col for col in designed_features if col in dea_df.columns]
if len(available_features) < len(designed_features):
    missing = set(designed_features) - set(available_features)
    raise ValueError(f"Missing {len(missing)} required features: {missing}\nDO NOT use 'available columns' workaround.\nReport to @director.")
inputs_cols = designed_features  # All 15 features
```

---

## Anti-Pattern 5: Silent Fallback Mechanisms

**❌ FORBIDDEN: Catch All Errors and Hide with Simple Fallback**

```python
# REAL EXAMPLE FROM Model 5
try:
    model = PoissonRegressor(alpha=0, max_iter=1000)
    model.fit(X, medals)
except:
    mu_pred = np.full_like(medals, medals.mean())  # ← BARE except!
```

**Why Wrong**: Bare `except:` catches ALL errors, falls back to trivial implementation, no error reported, silent degradation

**v2.5.7 Verdict**: ❌ **HIDDEN SIMPLIFICATION**

**✅ CORRECT**:
```python
try:
    model = PoissonRegressor(alpha=0, max_iter=1000)
    model.fit(X, medals)
except (ValueError, ConvergenceWarning) as e:
    logger.error(f"Model fitting failed: {e}")
    raise RuntimeError(f"DO NOT use simple mean fallback.\nRequires @director coordination.")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise  # Re-raise, DO NOT hide
```

**Rules**: ✅ Catch specific exceptions, ✅ Log errors, ✅ Report to @director, ❌ NEVER bare except, ❌ NEVER silent fallback

---

## Summary Table: Anti-Patterns Detected

| Anti-Pattern | Real Example | v2.5.7 Verdict | Correct Action |
|--------------|--------------|----------------|----------------|
| **Algorithm substitution** | sklearn vs PyMC (Model 5, 6) | ❌ AUTO-REJECT | Report to @director, do not simplify |
| **Training < 30%** | 18.7 min vs 3-5h (Model 1) | ❌ AUTO-REJECT | Verify actual algorithm, report discrepancy |
| **Iterations >20%** | 50-100× reduction (Quick Train) | ❌ EXCEEDS | Use ±20% tolerance, get approval |
| **Feature workaround** | 6/15 features (Model 6) | ❌ INCOMPLETE | Report missing features, do not skip |
| **Silent fallback** | Bare except + mean (Model 5) | ❌ HIDDEN | Catch specific errors, report |

---

## How To Avoid These Anti-Patterns

**Before Writing Code**:
1. Read model_design.md carefully (all equations, parameters, features)
2. Verify computational requirements (2-6 hours)
3. Check required libraries installed

**When Writing Code**:
1. Implement EXACTLY what design specifies (no shortcuts)
2. Use exact parameters (iterations, chains, samples)
3. Include ALL designed features (no "available columns")

**When Errors Occur**:
- Simple bug → Fix yourself
- Algorithm/complexity affected → **STOP, report to @director**
- Missing features → **STOP, report to @director**
- Library incompatibility → **STOP, report to @director**

**Before Reporting Completion**:
1. Verify training time reasonable (not 10× faster)
2. Verify all features from design present
3. Verify algorithm matches design (PyMC not sklearn)
4. Verify parameters within ±20%

**Remember**: These anti-patterns caused **AUTO-REJECT** by @time_validator. Learn from mistakes.
