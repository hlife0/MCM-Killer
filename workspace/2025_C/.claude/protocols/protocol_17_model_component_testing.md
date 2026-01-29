# Protocol 17: Model Component Testing

**Version**: 3.2.0
**Status**: Active
**Owner**: @code_translator (create tests), @model_trainer (run tests)
**Scope**: Phase 4 (Code Translation) → Phase 5 (Training)
**Priority**: HIGH

---

## Purpose

Catch model implementation bugs before launching long-running training jobs (Phase 5B). This protocol addresses the Model 3B failure from MCM 2025 Problem C, where a dimension mismatch error (234,10) vs (234,8) was discovered only after 14 hours of training, wasting significant competition time.

---

## Rationale

**Problem**: Insufficient pre-training validation led to:
- Model 3B failed with dimension mismatch after 14 hours of training
- Error: "ValueError: shapes (234,10) and (234,8) not aligned"
- Root cause: Synthetic control matrix had 10 columns, but model expected 8
- Time lost: 14 hours (failed training) + 2 hours (debugging) + 14 hours (re-training) = 30 hours total
- Impact: Delayed paper writing, increased time pressure

**Solution**: Mandatory pre-training unit tests catch dimension errors before full training, preventing 14-hour failures.

---

## Pre-Training Checklist

**Before Phase 5B Launch**: All 4 validation steps must pass

```
□ Unit tests created for all model components
□ Dimensions verified (e.g., synthetic control: (234, 8))
□ Synthetic data test passed (100 rows)
□ NUTS initialization converged (100 iterations, R-hat < 1.1)
□ Only then: Launch Phase 5B (14-hour training)
```

**If ANY check fails**: Do not launch Phase 5B. Fix issue, re-run tests.

---

## Unit Test Requirements

### 1. Test Coverage

**Required Tests** (per model file `model_*.py`):

| Component | Test Purpose | Input Size | Expected Output |
|-----------|--------------|------------|-----------------|
| Data loading | Verify CSV reading | 100 rows | DataFrame (100, cols) |
| Feature preprocessing | Check dimension compatibility | (100, 10) | (100, 8) after selection |
| Model initialization | Test parameter setup | config dict | Model object |
| Forward pass | Verify computation | (100, 8) | (100,) predictions |
| Gradient computation | Check derivative calculation | (100, 8) | Gradients (100, 8) |
| Loss function | Validate loss computation | (100,), (100,) | Scalar loss value |

### 2. Test Data

**Synthetic Data Generation**:
```python
def generate_synthetic_test_data(n_rows=100, n_features=10):
    """Generate synthetic data for unit testing.

    Args:
        n_rows: Number of rows (default: 100 for quick testing)
        n_features: Number of features (default: 10)

    Returns:
        X, y: Feature matrix and target vector
    """
    np.random.seed(42)
    X = np.random.randn(n_rows, n_features)
    y = np.random.randn(n_rows)
    return X, y
```

**Requirements**:
- Fixed random seed (42) for reproducibility
- Small dataset (100 rows) for fast execution (<30 seconds)
- Covers all edge cases (missing values, outliers, etc.)

### 3. Test Execution

**Location**: Each model file must include `if __name__ == "__main__":` test block

**Example** (`model_3b.py`):
```python
if __name__ == "__main__":
    print("Running Model 3B unit tests...")

    # Test 1: Dimension verification
    X, y = generate_synthetic_test_data(n_rows=100, n_features=10)
    assert X.shape == (100, 10), f"Expected (100, 10), got {X.shape}"
    print("✓ Test 1 passed: Dimension verification")

    # Test 2: Feature selection
    X_selected = select_features(X, feature_indices=[0,1,2,3,4,5,6,7])
    assert X_selected.shape == (100, 8), f"Expected (100, 8), got {X_selected.shape}"
    print("✓ Test 2 passed: Feature selection")

    # Test 3: Model initialization
    model = SyntheticControlModel(n_controls=8)
    assert model is not None, "Model initialization failed"
    print("✓ Test 3 passed: Model initialization")

    # Test 4: Forward pass
    predictions = model.predict(X_selected)
    assert predictions.shape == (100,), f"Expected (100,), got {predictions.shape}"
    print("✓ Test 4 passed: Forward pass")

    print("\n✅ All Model 3B unit tests passed!")
```

---

## Dimension Verification Protocol

### 1. Expected Dimensions Table

**Before Phase 5B**: Create dimension specification table for each model

| Model | Input Matrix Shape | Control Matrix Shape | Output Shape | Feature Count |
|-------|-------------------|----------------------|--------------|---------------|
| Model 1 | (234, 15) | N/A | (234,) | 15 |
| Model 2 | (234, 12) | N/A | (234,) | 12 |
| Model 3A | (234, 10) | N/A | (234,) | 10 |
| Model 3B | (234, 8) | (234, 8) | (234,) | 8 |
| Model 4 | (234, 20) | N/A | (234,) | 20 |

**Verification Step**:
```python
# Verify actual vs expected dimensions
actual_shape = X_train.shape
expected_shape = (234, 8)

if actual_shape != expected_shape:
    raise ValueError(
        f"Dimension mismatch: Expected {expected_shape}, got {actual_shape}\n"
        f"Model 3B requires 8 features, but data has {actual_shape[1]} features"
    )
```

### 2. Shape Validation Function

**Required Function** (include in each `model_*.py`):
```python
def validate_dimensions(X, y, model_name, expected_features):
    """Validate input dimensions match expected shape.

    Args:
        X: Feature matrix
        y: Target vector
        model_name: Name of model (for error message)
        expected_features: Expected number of features

    Raises:
        ValueError: If dimensions don't match expected shape
    """
    n_samples, n_features = X.shape

    # Validate feature count
    if n_features != expected_features:
        raise ValueError(
            f"{model_name} dimension error:\n"
            f"  Expected features: {expected_features}\n"
            f"  Actual features: {n_features}\n"
            f"  Shape: {X.shape}\n"
            f"  Check feature selection or data preprocessing!"
        )

    # Validate sample count
    if n_samples != y.shape[0]:
        raise ValueError(
            f"{model_name} sample count mismatch:\n"
            f"  X samples: {n_samples}\n"
            f"  y samples: {y.shape[0]}\n"
            f"  Check data alignment!"
        )

    print(f"✓ {model_name} dimensions validated: {X.shape} → {y.shape}")
```

**Usage**:
```python
# Before training
validate_dimensions(
    X_train,
    y_train,
    model_name="Model 3B (Synthetic Control)",
    expected_features=8
)
```

---

## Reduced Dataset Validation

### 1. Purpose

Validate model runs correctly on small dataset before committing to 14-hour full training.

**Test Configuration**:
- Dataset size: 100 rows (vs. full 234 rows)
- Training iterations: 100 (vs. full 10,000+)
- Expected runtime: <2 minutes (vs. 14 hours)

### 2. Validation Script

**Location**: `output/implementation/code/validate_reduced_dataset.py`

```python
import pandas as pd
import numpy as np
from model_1 import Model1
from model_2 import Model2
from model_3a import Model3A
from model_3b import Model3B
from model_4 import Model4

def validate_reduced_dataset():
    """Validate all models on reduced dataset (100 rows)."""
    print("Validating models on reduced dataset...")

    # Load features
    features = pd.read_pickle("output/implementation/data/features_1.pkl")

    # Create reduced dataset (first 100 rows)
    features_reduced = features.iloc[:100]

    # Test each model
    models = {
        "Model 1": Model1(),
        "Model 2": Model2(),
        "Model 3A": Model3A(),
        "Model 3B": Model3B(),
        "Model 4": Model4()
    }

    for model_name, model in models.items():
        try:
            print(f"\nTesting {model_name}...")

            # Run on reduced data
            model.fit(features_reduced)
            predictions = model.predict(features_reduced)

            # Validate output shape
            assert predictions.shape == (100,), \
                f"{model_name} output shape incorrect: {predictions.shape}"

            print(f"✓ {model_name} passed reduced dataset validation")

        except Exception as e:
            print(f"❌ {model_name} FAILED: {str(e)}")
            return False

    print("\n✅ All models passed reduced dataset validation!")
    return True

if __name__ == "__main__":
    success = validate_reduced_dataset()
    exit(0 if success else 1)
```

**Usage**:
```bash
python output/implementation/code/validate_reduced_dataset.py
```

**Expected Output**:
```
Testing Model 1...
✓ Model 1 passed reduced dataset validation

Testing Model 2...
✓ Model 2 passed reduced dataset validation

Testing Model 3B...
✓ Model 3B passed reduced dataset validation

✅ All models passed reduced dataset validation!
```

---

## Convergence Pre-Check

### 1. NUTS Initialization Test

**Purpose**: Verify MCMC sampling converges before committing to 14-hour run.

**Test Configuration**:
- Sampling iterations: 100 (vs. full 10,000+)
- Chains: 2 (vs. full 4)
- Expected runtime: <5 minutes (vs. 14 hours)
- Convergence criterion: R-hat < 1.1

### 2. Pre-Check Script

**Location**: `output/implementation/code/check_nuts_convergence.py`

```python
import pymc as pm
import numpy as np

def check_nuts_convergence(model, X, y, n_iter=100, tune=50):
    """Quick NUTS convergence test.

    Args:
        model: Model object with .fit() method
        X: Feature matrix (reduced dataset: 100 rows)
        y: Target vector
        n_iter: Number of sampling iterations (default: 100)
        tune: Number of tuning iterations (default: 50)

    Returns:
        bool: True if converged (R-hat < 1.1), False otherwise
    """
    print(f"Running NUTS convergence test ({n_iter} iterations)...")

    try:
        # Run quick NUTS test
        with model:
            trace = pm.sample(
                draws=n_iter,
                tune=tune,
                chains=2,
                progressbar=False
            )

        # Check R-hat values
        rhat_values = pm.summary(trace)['r_hat']
        max_rhat = rhat_values.max()

        print(f"Max R-hat: {max_rhat:.3f}")

        if max_rhat < 1.1:
            print(f"✓ NUTS convergence test passed (R-hat < 1.1)")
            return True
        else:
            print(f"❌ NUTS convergence test failed (R-hat ≥ 1.1)")
            print(f"  Max R-hat: {max_rhat:.3f}")
            print(f"  Possible causes: Model identifiability, insufficient data, poor initialization")
            return False

    except Exception as e:
        print(f"❌ NUTS convergence test FAILED: {str(e)}")
        return False
```

**Usage**:
```python
# Before Phase 5B launch
X_test, y_test = generate_synthetic_test_data(n_rows=100, n_features=8)
model = SyntheticControlModel(n_controls=8)

# Check convergence
if not check_nuts_convergence(model, X_test, y_test):
    raise ValueError("NUTS convergence failed. Do not proceed to Phase 5B.")
```

---

## Implementation Workflow

### Phase 4: Code Translation (@code_translator)

**Deliverables**:
1. `model_*.py` files with unit tests in `if __name__ == "__main__":` block
2. `validate_dimensions()` function in each model file
3. Synthetic data generation function

**Verification**:
```python
# Run unit tests for each model
python model_1.py  # Should output: "✅ All Model 1 unit tests passed!"
python model_2.py  # Should output: "✅ All Model 2 unit tests passed!"
python model_3b.py  # Should output: "✅ All Model 3B unit tests passed!"
```

---

### Phase 5A: Quick Training (@model_trainer)

**Before Training**:
1. Run unit tests: `python model_*.py` for all models
2. Verify all tests pass
3. If any test fails: Fix bug, re-run test, do not proceed to training

**After Training**:
1. Verify output dimensions match expected shapes
2. Check for convergence warnings
3. Document any issues in `output/docs/known_issues.md`

---

### Phase 5B: Full Training (@model_trainer)

**Before Launch** (CRITICAL):
1. ✅ Unit tests passed (all models)
2. ✅ Dimensions verified (all models)
3. ✅ Reduced dataset validation passed
4. ✅ NUTS convergence check passed (for Bayesian models)
5. **Only then**: Launch Phase 5B (14-hour training)

**After Launch**:
1. Monitor first 100 iterations for errors
2. If error occurs within first 100 iterations: Kill training, fix bug, restart
3. If no errors after 100 iterations: Likely successful, continue monitoring

---

## Enforcement Mechanisms

### @code_translator Responsibilities
1. **Include Unit Tests**: Every model file must have test block
2. **Add Dimension Validation**: Every model file must have `validate_dimensions()`
3. **Test Before Handoff**: Run all tests before delivering to @model_trainer
4. **Document Bugs**: If tests fail, document issue and fix before proceeding

**Validation**: @director verifies all model files have test blocks before Phase 5

---

### @model_trainer Responsibilities
1. **Run Unit Tests**: Before Phase 5A, run `python model_*.py` for all models
2. **Verify Dimensions**: Check dimension specification table matches actual data
3. **Run Reduced Dataset Test**: Execute `validate_reduced_dataset.py` before Phase 5B
4. **Check NUTS Convergence**: Run convergence pre-check for Bayesian models
5. **Block Phase 5B**: If ANY validation fails, do not launch full training

**Validation**: @director confirms all tests passed before approving Phase 5B launch

---

### @director Responsibilities
1. **Verify Test Existence**: Check all model files have `if __name__ == "__main__":` blocks
2. **Verify Test Execution**: Confirm @model_trainer ran all tests successfully
3. **Verify Dimension Table**: Review dimension specification for accuracy
4. **Approve Phase 5B**: Only after all 4 validation steps passed
5. **Block if Failures**: If any test fails, do not approve Phase 5B

**Approval Checklist**:
```
□ All model files have unit tests (verified by inspection)
□ All unit tests passed (verified by @model_trainer report)
□ Dimension table created and verified (matches data)
□ Reduced dataset validation passed (exit code 0)
□ NUTS convergence check passed (for Bayesian models)
□ Phase 5B launch approved
```

---

## Failure Scenarios & Recovery

### Scenario 1: Unit Test Failure
**Error**: `AssertionError: Expected (100, 8), got (100, 10)`

**Recovery**:
1. @code_translator identifies bug (e.g., wrong feature indices)
2. Fixes bug in model file
3. Re-runs unit test
4. Only after test passes: Delivers to @model_trainer

**Time Lost**: <1 hour (vs. 14 hours if discovered during Phase 5B)

---

### Scenario 2: Dimension Mismatch
**Error**: `ValueError: shapes (234,10) and (234,8) not aligned`

**Recovery**:
1. @model_trainer detects mismatch during reduced dataset validation
2. @code_translator fixes feature selection (e.g., `features[:, :8]`)
3. @model_trainer re-runs reduced dataset validation
4. Only after pass: Launches Phase 5B

**Time Lost**: 2 hours (vs. 30 hours if discovered during full training)

---

### Scenario 3: NUTS Non-Convergence
**Error**: `R-hat = 1.35 (threshold: 1.1)`

**Recovery**:
1. @model_trainer detects non-convergence in pre-check
2. @modeler investigates model identifiability
3. Adjusts priors or model structure
4. Re-runs convergence pre-check
5. Only after convergence: Launches Phase 5B

**Time Lost**: 4 hours (vs. 14 hours + failed training)

---

## Success Metrics

**Quantitative**:
- 100% of models pass unit tests before Phase 5A
- 0% of Phase 5B runs fail due to dimension errors
- Average time to detect bugs: <5 minutes (vs. 14 hours without protocol)

**Qualitative**:
- No training failures due to implementation bugs
- All dimension errors caught before full training
- Systematic validation (not ad-hoc testing)

---

## Lessons from MCM 2025 Problem C

**What Went Wrong**:
- Model 3B failed after 14 hours with dimension mismatch
- No pre-training unit tests to catch bug
- No dimension verification before training
- No reduced dataset validation
- Time lost: 30 hours (14h failed + 2h debug + 14h re-train)

**How Protocol 17 Prevents Recurrence**:
- Unit tests catch dimension bugs before training (5 minutes vs. 14 hours)
- Dimension verification table makes requirements explicit
- Reduced dataset validation (100 rows) catches errors in 2 minutes vs. 14 hours
- NUTS convergence pre-check (100 iterations) detects sampling issues in 5 minutes vs. 14 hours
- @director enforcement ensures tests run before Phase 5B approval

---

## Related Protocols

- **Protocol 4**: Phase 4.5 Re-Validation (implementation fidelity check)
- **Protocol 5**: Idealistic Mode (perfect implementation, not simplified)
- **Protocol 12**: Error Monitoring (Phase 5B watch mode)

---

## Changelog

**v3.2.0** (2026-01-29): Initial creation
- Addresses Model 3B dimension mismatch from MCM 2025 Problem C
- Implements 4-step pre-training validation checklist
- Establishes unit test requirements for all models
- Creates dimension verification protocol
- Adds reduced dataset validation (catches errors in 2 minutes vs. 14 hours)
