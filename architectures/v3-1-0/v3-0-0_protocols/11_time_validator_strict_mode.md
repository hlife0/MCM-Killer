# @time_validator Strict Mode Protocol

> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Purpose**: Ensure @time_validator rejects ALL lazy implementations, especially training duration shortcuts

---

## Problem Statement

**CRITICAL ISSUE**: @code_translator simplifies implementation → training time drops from 12-18 hours to 43 minutes → @time_validator does not reject.

**Example Failure** (v2.5.6):
```
Phase 5B Training Results:
  Expected: 12-18 hours (from model_design.md)
  Actual: 43 minutes (0.72 hours)

  @code_translator's bugs:
  - Model 3: "PyMC API incompatible" → Used simple logistic regression
  - Model 4: "Function not defined" → Used PCA instead
  - Model 5: "KeyError: 'years'" → Simplified change point detection
  - Model 6: "KeyError: 'Gold'" → Used available columns

  Result: Training completed in 43 minutes (23× faster than expected)

  @time_validator (v2.5.6):
  "Training completed successfully.
   Results file exists.
   File size looks reasonable.
   ✅ APPROVED"

  WHAT SHOULD HAVE HAPPENED:
  "Training time (43 min) is 23× below minimum acceptable (3.6 hours).
   ❌ REJECT: Lazy implementation detected."
```

**Why This Happens**:
1. **@code_translator encounters implementation error**
2. **@code_translator chooses "simpler alternative"** (thinking this is pragmatic)
3. **@code_translator does NOT consult @director** (doesn't realize simplification = fraud)
4. **@time_validator checks "did training complete?"** not "is this the designed method?"**
5. **@time_validator sees "43 minutes" but doesn't enforce red line**

**Impact**:
- **Academic fraud**: Simplified methods presented as sophisticated
- **O-Prize standards violated**: 43-minute training is non-competitive
- **Quality gate failure**: @time_validator should have auto-rejected
- **@modeler's design wasted**: 12-18 hour methods replaced with shortcuts

---

## Core Principles

### Principle 1: Simplification = Academic Fraud

**@code_translator MUST understand**:
- Simplifying implementation without approval = **Academic fraud**
- "It doesn't work" is NOT an excuse to simplify
- **Correct approach**: Consult @director, fix the issue, or request design change

### Principle 2: Training Duration Red Line

**@time_validator MUST enforce**:
- If training time < 30% of expected → **AUTO-REJECT**
- No exceptions, no "it's good enough"
- 43 minutes vs 12-18 hours = **23× below threshold** → **REJECT**

### Principle 3: Algorithm Match Verification

**@time_validator MUST verify**:
- Does code use the EXACT algorithm specified in design?
- PyMC vs sklearn = **MISMATCH** → **REJECT**
- "Simpler version" = **LAZY IMPLEMENTATION** → **REJECT**

---

## Implementation: @time_validator Strict Mode

### Enhanced Check 1: Training Duration Red Line

**v2.5.6 (OLD)**:
```python
# @time_validator checks
if training_completed and results_file_exists:
    return "✅ APPROVED"
```

**v2.5.7 (NEW) - Strict Mode**:
```python
# @time_validator strict mode
def verify_training_duration(log_file, expected_hours):
    """
    Verify training duration meets minimum threshold.

    Red Line: actual_hours >= 30% of minimum expected_hours
    """
    actual_hours = extract_duration_from_log(log_file)
    minimum_expected = expected_hours * 0.30  # 30% threshold

    if actual_hours < minimum_expected:
        ratio = minimum_expected / actual_hours
        return {
            "verdict": "❌ REJECT",
            "reason": (
                f"Training duration ({actual_hours:.2f}h) is {ratio:.1f}× "
                f"below minimum acceptable ({minimum_expected:.2f}h). "
                f"Expected: {expected_hours:.2f}h. "
                f"This indicates LAZY IMPLEMENTATION or simplified algorithm."
            ),
            "action": "Re-run with correct implementation. Do not simplify.",
            "red_line_violation": True
        }

    return {"verdict": "✅ PASS", "actual_hours": actual_hours}

# Example from problematic case:
# expected_hours = 12 (from model_design.md)
# actual_hours = 0.72 (43 minutes)
# minimum_expected = 12 * 0.30 = 3.6 hours
# ratio = 3.6 / 0.72 = 5.0
# verdict: "❌ REJECT: 5× below minimum acceptable (3.6h)"
```

**Decision Matrix**:

| Expected | Actual | Ratio | Verdict |
|----------|--------|-------|---------|
| 12-18h | 43 min (0.72h) | 5× below | ❌ **REJECT** |
| 12-18h | 2h | 1.8× below | ❌ **REJECT** |
| 12-18h | 3.5h | Just below 30% | ❌ **REJECT** |
| 12-18h | 4h | Meets 30% | ⚠️ **SUSPICIOUS** (investigate) |
| 12-18h | 8h | Meets threshold | ✅ **PASS** |

**Red Line Threshold: 30% of minimum expected**
- **Rationale**: 30% allows for some optimization but catches lazy shortcuts
- **Examples**:
  - Expected: 12-18h → Minimum: 3.6h
  - Expected: 4-6h → Minimum: 1.2h
  - Expected: 2-4h → Minimum: 0.6h

### Enhanced Check 2: Algorithm Match Verification

**v2.5.6 (OLD)**:
```python
# @time_validator checks
if code_runs and results_look_valid:
    return "✅ APPROVED"
```

**v2.5.7 (NEW) - Strict Mode**:
```python
# @time_validator strict mode
def verify_algorithm_match(design_file, code_file):
    """
    Verify code implementation matches design specification.
    """
    design_algorithm = extract_algorithm_spec(design_file)
    code_algorithm = extract_implementation(code_file)

    # Check 1: Algorithm match
    if not algorithms_match(design_algorithm, code_algorithm):
        return {
            "verdict": "❌ LAZY IMPLEMENTATION",
            "reason": (
                f"Design specifies '{design_algorithm}', "
                f"but code uses '{code_algorithm}'. "
                f"This is unauthorized simplification."
            ),
            "action": "@code_translator must rework using correct algorithm",
            "mismatch": True
        }

    # Check 2: Library match
    if not libraries_match(design_algorithm, code_algorithm):
        return {
            "verdict": "❌ ALGORITHM CHANGE",
            "reason": (
                f"Design requires {design_library}, "
                f"code uses {code_library}. "
                f"Example: PyMC vs sklearn"
            ),
            "action": "Reimplement using specified library",
            "mismatch": True
        }

    return {"verdict": "✅ MATCH", "algorithm": design_algorithm}

# Example from problematic case:
# design: "PyMC with HMC sampling, 2000 samples, 4 chains"
# code: "sklearn.LinearRegression"
# verdict: "❌ LAZY IMPLEMENTATION: Algorithm mismatch"
```

**Examples of Lazy Implementation**:

| Design | Code | Verdict |
|--------|------|---------|
| PyMC with HMC | sklearn.LinearRegression | ❌ **LAZY** |
| Bayesian hierarchical | sklearn.RandomForest | ❌ **LAZY** |
| MCMC sampling (10000) | MCMC sampling (1000) | ❌ **REDUCED** |
| Deep learning (5000 epochs) | Deep learning (500 epochs) | ❌ **REDUCED** |
| Ensemble of 5 models | Ensemble of 2 models | ❌ **INCOMPLETE** |

### Enhanced Check 3: Feature Completeness Verification

**v2.5.6 (OLD)**:
```python
# @time_validator checks (if at all)
# Often skipped in v2.5.6
```

**v2.5.7 (NEW) - Strict Mode**:
```python
# @time_validator strict mode
def verify_feature_completeness(design_file, code_file, data_file):
    """
    Verify all designed features are implemented.
    """
    design_features = extract_feature_list(design_file)
    code_features = extract_features_used(code_file)
    data_columns = extract_column_names(data_file)

    missing_features = set(design_features) - set(code_features)
    unavailable_features = set(design_features) - set(data_columns)

    # Check 1: Missing features in code
    if missing_features:
        return {
            "verdict": "❌ INCOMPLETE",
            "reason": (
                f"Code is missing {len(missing_features)} features: {missing_features}. "
                f"Design specifies {len(design_features)} features, "
                f"code implements {len(code_features)}."
            ),
            "action": "@code_translator must include all designed features",
            "missing": list(missing_features)
        }

    # Check 2: Unavailable features in data
    if unavailable_features:
        return {
            "verdict": "⚠️ DATA STRUCTURE MISMATCH",
            "reason": (
                f"Design specifies {len(unavailable_features)} features not in data: {unavailable_features}. "
                f"This indicates a Phase 3 (@data_engineer) or Phase 1 (@modeler) issue."
            ),
            "action": "Consult @director for data structure fix (DO NOT simplify)",
            "missing": list(unavailable_features),
            "requires_coordination": True
        }

    return {
        "verdict": "✅ COMPLETE",
        "features": len(design_features),
        "all_present": True
    }

# Example from problematic case:
# design: ["Gold", "Silver", "Bronze", "years", "host_country", ...]
# code: Uses "available columns" (only 10 columns)
# missing: ["years", "Gold"]
# verdict: "❌ INCOMPLETE: Missing features ['years', 'Gold']"
```

**Decision Flow**:
```
Feature missing in code?
├─ Yes → Is feature in data?
│   ├─ Yes → ❌ INCOMPLETE (code_translator must include it)
│   └─ No → ⚠️ DATA STRUCTURE MISMATCH (consult @director, DO NOT simplify)
└─ No → ✅ COMPLETE
```

**CRITICAL**: If feature missing from data:
- **DO NOT**: "Use available columns instead"
- **DO**: "Consult @director for data structure fix"

### Enhanced Check 4: Iteration/Parameter Verification

**v2.5.7 (NEW) - Strict Mode**:
```python
# @time_validator strict mode
def verify_iterations_parameters(design_file, code_file):
    """
    Verify iterations and parameters match specification.
    """
    design_spec = extract_hyperparameters(design_file)
    code_spec = extract_hyperparameters_from_code(code_file)

    violations = []

    for param, design_value in design_spec.items():
        if param not in code_spec:
            violations.append(f"Missing parameter: {param}")
            continue

        code_value = code_spec[param]

        # Check for iteration reduction
        if "iterations" in param.lower() or "samples" in param.lower() or "epochs" in param.lower():
            if code_value < design_value * 0.80:  # Allow ±20% tolerance
                ratio = design_value / code_value
                violations.append(
                    f"{param}: {code_value} (reduced by {ratio:.1f}× from {design_value})"
                )

    if violations:
        return {
            "verdict": "❌ REDUCED COMPLEXITY",
            "reason": (
                f"Parameters reduced: {', '.join(violations)}. "
                f"This indicates lazy implementation to reduce training time."
            ),
            "action": "@code_translator must use specified parameters",
            "violations": violations
        }

    return {"verdict": "✅ MATCH", "parameters": design_spec}

# Example:
# design: "pm.sample(draws=10000, tune=2000, chains=4)"
# code: "pm.sample(draws=1000, tune=200, chains=2)"
# verdict: "❌ REDUCED: draws reduced by 10×, tune reduced by 10×, chains reduced by 2×"
```

**Tolerance Policy**:
- **Iterations/samples/epochs**: ±20% tolerance
  - Design: 10000 → Minimum: 8000
  - Design: 5000 → Minimum: 4000
- **Chains**: No reduction allowed
  - Design: 4 chains → Code must use 4 chains
- **Other parameters**: Case-by-case basis

---

## Implementation: @code_translator Behavioral Change

### Old Behavior (v2.5.6) - FORBIDDEN

```
@code_translator encounters error:
  "KeyError: 'Gold'"

@code_translator thinks:
  "This column doesn't exist. I'll use available columns instead."

@code_translator implements:
  features = df.columns  # Use available columns

@code_translator reports:
  "Implementation complete, used available columns"

Result: Training time 43 minutes (LAZY)
```

### New Behavior (v2.5.7) - REQUIRED

```
@code_translator encounters error:
  "KeyError: 'Gold'"

@code_translator thinks:
  "STOP! This is a data structure issue.
   Simplification = Academic Fraud.
   I MUST consult @director."

@code_translator reports:
  "Director, implementation issue detected:

  File: output/implementation/code/model_6.py
  Error: KeyError: 'Gold'

  Model design specifies:
  - Features: Gold, Silver, Bronze, years, host_country, [...]

  Data structure has:
  - Columns: [list of available columns]

  Missing features: ['Gold', 'years']

  This is a data structure mismatch, NOT an implementation detail.

  Options:
  1. Rewind to Phase 3 (@data_engineer) to fix feature engineering
  2. Consult @modeler to update design to match actual data
  3. DO NOT proceed with 'available columns' workaround

  Awaiting guidance before proceeding."

@director coordinates:
  "@data_engineer: model_6 requires 'Gold' and 'years' features.
   Please verify these are in features_6.pkl"

  [Issue resolved in Phase 3 or Phase 1]

@code_translator implements correctly:
  features = df[designed_feature_list]

Result: Training time 12-18 hours (CORRECT)
```

### @code_translator Prompt Updates

**Add to agent prompt**:
```markdown
## 🚨 CRITICAL: Simplification = Academic Fraud (v2.5.7)

> [!CAUTION]
> **[ ABSOLUTE FORBIDDEN] Simplifying implementation without @director approval**
>
> Simplification = Academic Fraud = Immediate Rejection
>
> When you encounter implementation errors:
> - ❌ FORBIDDEN: "Use available columns instead"
> - ❌ FORBIDDEN: "Use simpler algorithm"
> - ❌ FORBIDDEN: "Reduce iterations to make it work"
> - ✅ REQUIRED: Report error to @director immediately
> - ✅ REQUIRED: Request coordination to fix root cause
> - ✅ REQUIRED: Wait for guidance before proceeding

### Decision Tree: Implementation Error

```
Implementation error encountered
├─ Is it a simple typo/bug?
│   ├─ Yes → Fix it yourself (e.g., variable name, syntax)
│   └─ No → Does it affect algorithm/complexity?
│       ├─ Yes → STOP, report to @director
│       └─ No → Can you fix without changing design?
│           ├─ Yes → Fix and document change
│           └─ No → Report to @director
```

### Examples

**❌ FORBIDDEN: Simplify to avoid error**
```python
# WRONG: Data structure mismatch
try:
    features = df[['Gold', 'Silver', 'Bronze', 'years']]
except KeyError:
    features = df.columns  # Use available columns (FRAUD!)
```

**✅ CORRECT: Report and wait for guidance**
```python
# CORRECT: Report error to @director
@code_translator: "Director, encountered KeyError: 'Gold' in model_6.py.
                  Model design specifies features that don't exist in data.
                  This requires coordination between @modeler and @data_engineer.
                  DO NOT proceed with workaround.
                  Awaiting guidance."
```

**❌ FORBIDDEN: Simplify algorithm**
```python
# WRONG: PyMC doesn't work, use sklearn instead
try:
    import pymc as pm
    model = pm.Model()
except:
    from sklearn.linear_model import LinearRegression  # FRAUD!
    model = LinearRegression()
```

**✅ CORRECT: Report incompatibility**
```python
# CORRECT: Report API issue to @director
@code_translator: "Director, PyMC API incompatibility detected.
                  TensorVariable has no logp attribute in this version.
                  Options:
                  1. Fix PyMC version
                  2. Update model design to use compatible PyMC API
                  3. DO NOT switch to sklearn (simplification = fraud)
                  Awaiting guidance."
```

### Consequences of Violation

| Violation | Consequence |
|-----------|------------|
| Simplify algorithm without approval | ❌ @time_validator REJECTS, full rework required |
| Use available columns instead of designed features | ❌ @time_validator REJECTS, data structure fix required |
| Reduce iterations without approval | ❌ @time_validator REJECTS, use specified parameters |
| Repeated violations | Formal warning, potential agent reinitialization |
```

---

## Integration with Phases

### Phase 4.5: Implementation Fidelity Check

**v2.5.7 Enhanced Protocol**:
```
@director calls @time_validator:
"@time_validator: Strict mode check for model_{i}.py

 Verify:
 1. Algorithm match (design vs code)
 2. Feature completeness (all designed features present)
 3. Iterations/parameters (within tolerance)
 4. NO unauthorized simplifications

 Report: output/docs/validation/time_validator_code_{i}.md"

@time_validator executes strict mode checks:
✓ Algorithm: PyMC with HMC (MATCH)
✓ Features: 15/15 present (COMPLETE)
✓ Iterations: 10000 samples (MATCH)
✓ NO simplifications detected

→ Verdict: ✅ APPROVE
```

### Phase 5.5: Data Authenticity Check

**v2.5.7 Enhanced Protocol**:
```
@director calls @time_validator:
"@time_validator: Strict mode check for training_{i}.log

 Verify:
 1. Training duration ≥ 30% of expected (RED LINE)
 2. Algorithm used matches design
 3. Training iterations completed as specified
 4. NO evidence of skip/simplify

 Report: output/docs/validation/time_validator_data_{i}.md"

@time_validator executes strict mode checks:
❌ Duration: 0.72h (expected 12-18h)
❌ 5× below minimum acceptable (3.6h)
❌ Algorithm: sklearn (design: PyMC)
❌ Features: 10/15 (5 missing)

→ Verdict: ❌ REJECT (Lazy implementation detected)
```

---

## Decision Matrix

### @time_validator Decision Flow

```
Check 1: Training duration
├─ < 30% of expected?
│   ├─ Yes → ❌ AUTO-REJECT (Red line violation)
│   └─ No → Continue to Check 2
│
Check 2: Algorithm match
├─ Mismatch?
│   ├─ Yes → ❌ REJECT (Lazy implementation)
│   └─ No → Continue to Check 3
│
Check 3: Feature completeness
├─ Missing features?
│   ├─ Yes → ❌ REJECT (Incomplete)
│   └─ No → Continue to Check 4
│
Check 4: Iterations/parameters
├─ Reduced > 20%?
│   ├─ Yes → ❌ REJECT (Reduced complexity)
│   └─ No → ✅ APPROVE
```

### Severity Levels

| Check | Severity | Action | Example |
|-------|----------|--------|---------|
| Duration < 30% | **CRITICAL** | Auto-reject, full rework | 43 min vs 12-18h |
| Algorithm mismatch | **CRITICAL** | Auto-reject, full rework | sklearn vs PyMC |
| Missing features | **HIGH** | Reject, include all | 10/15 features |
| Iterations reduced | **HIGH** | Reject, use specified | 1000 vs 10000 |
| Minor tweaks (±10%) | **LOW** | Note, approve | 9000 vs 10000 |

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
