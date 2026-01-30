# Mandatory Sanity Check Protocols

**Purpose**: This document defines the mandatory sanity checks that must be performed before saving any training results. These checks prevent the #1 failure mode: generating results that are obviously wrong.

**Source**: Extracted from model_trainer.md

**Context**: The most common training failure is not code crashes or convergence issues, but generating results that pass technical validation but fail basic domain logic checks (e.g., predicting a country will win "first medal ever" when they have historical medals).

---

## 🚨 MANDATORY Sanity Checks

> [!CAUTION]
> **Before saving results, you MUST verify outputs make sense.**
> **The #1 failure mode is generating results that are obviously wrong.**

### Required Sanity Checks

**1. First-Time Winner Verification**

If your model predicts a country will win their "first medal ever", VERIFY:

```python
# Check if country has historical medals
historical_medals = df[df['Country'] == country]['Total_Medals'].sum()
if historical_medals > 0:
    raise ValueError(f"ERROR: {country} has {historical_medals} historical medals - NOT a first-time winner!")
```

**Countries that are NEVER first-time winners** (major Olympic powers):
- USA, China, Great Britain, Russia, Germany, France, Italy, Australia, Japan, South Korea, Netherlands, Hungary, Spain, Canada, Brazil, Kenya, Jamaica, Cuba, Poland, Sweden, Norway, Switzerland

**2. Medal Count Bounds**

```python
# No country should predict > 200 total medals (US record is ~126)
assert predicted_total <= 200, f"Unrealistic: {country} predicted {predicted_total} medals"

# No country should predict > 50 golds (US/China record is ~40-48)
assert predicted_gold <= 60, f"Unrealistic: {country} predicted {predicted_gold} golds"
```

**3. Consistency Check**

```python
# Total = Gold + Silver + Bronze
assert predicted_total == predicted_gold + predicted_silver + predicted_bronze
```

**4. Prediction Interval Validation**

```python
# Confidence intervals must be valid
assert all(ci_upper >= ci_lower), "Invalid confidence intervals!"
assert all(ci_mean >= ci_lower), "Mean below lower bound!"
assert all(ci_mean <= ci_upper), "Mean above upper bound!"
```

---

## Integration into Training Workflow

**Phase 5A (Quick Training)**:
```python
# After generating predictions
predictions = predict(quick_model, X_test)

# MANDATORY: Run sanity checks
assert predictions is not None, "Predictions is None"
assert len(predictions) > 0, "Predictions is empty"
assert all(predictions >= 0), "Negative predictions detected!"

# Domain-specific checks
for idx, pred in enumerate(predictions):
    country = X_test.iloc[idx]['Country']
    # Check first-time winner claim
    # Check medal bounds
    # Check consistency

print("✅ Phase 5A sanity checks passed")
```

**Phase 5B (Full Training)**:
```python
# After generating final predictions
predictions = predict(full_model, X_test)

# MANDATORY: Run ALL sanity checks
# 1. First-time winner verification
# 2. Medal count bounds
# 3. Consistency check
# 4. Prediction interval validation

# If ANY check fails → STOP and investigate
# DO NOT save results with failed sanity checks

print("✅ Phase 5B sanity checks passed")
```

---

## Common Failure Modes

**Failure Mode 1: Historical Medal Ignore**
```
❌ WRONG: Model predicts "Germany wins first medal" (Germany has 1000+ historical medals)
✅ CORRECT: Verify historical data before making first-time winner claims
```

**Failure Mode 2: Unrealistic Totals**
```
❌ WRONG: Model predicts "Fiji wins 150 total medals" (implausible for small nation)
✅ CORRECT: Apply upper bounds based on historical records and country size
```

**Failure Mode 3: Math Inconsistency**
```
❌ WRONG: Total = 45, but Gold + Silver + Bronze = 43
✅ CORRECT: Enforce Total = Gold + Silver + Bronze constraint
```

**Failure Mode 4: Invalid Intervals**
```
❌ WRONG: 95% CI lower bound = 50, upper bound = 40
✅ CORRECT: Ensure lower ≤ mean ≤ upper for all predictions
```

---

## Reporting Sanity Check Failures

**When sanity check fails**:

```
@model_trainer: "⚠️ SANITY CHECK FAILED

Model: {i}
Phase: 5A/5B
Check: {which check failed}

Details:
- Prediction: {what was predicted}
- Issue: {why it's wrong}
- Example: {specific example}

Actions Required:
1. Investigate root cause (model design? data? implementation?)
2. Fix underlying issue
3. Re-run training
4. Verify sanity checks pass

Training halted until issue resolved.

Awaiting @director guidance."
```

---

## Director Decision Protocol

**When @model_trainer reports sanity check failure**:

```
@director: [ANALYZES failure type]

IF model design issue (wrong constraints, missing logic):
  "REWIND to Phase 1 (@modeler)
  Reason: Model lacks domain constraint for {issue}
  Action: Add constraint/logic to model design"

IF data issue (historical data missing/wrong):
  "REWIND to Phase 3 (@data_engineer)
  Reason: Historical medal data incomplete
  Action: Verify and complete historical medal dataset"

IF implementation issue (constraint not coded):
  "@code_translator: Add sanity check constraint to model_{i}.py
  Constraint: {specific constraint}
  Re-run Phase 4.5 validation after fix"

IF convergence issue (model overfitting):
  "@modeler: Review model regularization
  Issue: Predictions outside realistic bounds
  Action: Recommend regularization strategy"
```
