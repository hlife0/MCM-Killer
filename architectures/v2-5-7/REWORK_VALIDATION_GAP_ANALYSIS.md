# Rework Validation Gap Analysis

> **Date**: 2026-01-19
> **Questions**:
> 1. Does @model_trainer → @code_translator go through @director when training errors occur?
> 2. Is reworked code re-validated against Design Expectations Table?

---

## 🔍 Question 1: @model_trainer → @code_translator Error Handling

### ✅ Answer: YES - Must go through @director

**Location**: model_trainer.md lines 169-228

**Standard Protocol** (v2.5.7 and v2.5.8):

```
@model_trainer: "⚠️ ERROR DETECTED during Phase 5B training
Model: {i}
Error: {error_message}
Line: {line_number}
Error Type: {implementation / data / resource}
Severity: CRITICAL (training halted)
Awaiting @director guidance."
   ↓
@dicator: "@code_translator: Error detected in model_{i}.py
          Error: {specific error}
          Line: {line_number}
          This is a {implementation / data} error.
          Please investigate and provide fix."
   ↓
@code_translator: "Investigation complete:
Error cause: {root cause}
Fix: {specific fix}
Updated code: {patch}
Recommendation: Resume training from checkpoint or restart"
   ↓
@dicator: "@model_trainer: Fix applied. Resume training.
Actions:
1. Kill current process
2. Restart training with fixed code
3. Continue monitoring"
   ↓
@model_trainer: "Restarting training with fixed code..."
```

**Verification**: ✅ **@model_trainer cannot directly contact @code_translator**

**Evidence**:
- model_trainer.md line 191: "**@director response**"
- model_trainer.md line 194-201: @director delegates to @code_translator
- model_trainer.md line 217-228: @director decision, @model_trainer resumes

---

## ⚠️ Question 2: Is Reworked Code Re-Validated?

### ❌ Answer: NO - Missing rework validation loop

**Current Protocol** (v2.5.7/v2.5.8):

```
Phase 4: @code_translator writes code
   ↓
Phase 4.5: @time_validator validates → ✅ APPROVE
   ↓
Phase 5A/5B: @model_trainer trains
   ↓
Error detected!
   ↓
@model_trainer → @director → @code_translator
   ↓
@code_translator: "Fix applied"
   ↓
@dicator: "@model_trainer: Resume training"
   ↓
⚠️ **MISSING**: No re-validation by @time_validator
   ↓
@model_trainer resumes training with fixed code
```

**What's Missing**:

1. **No Phase 4.5 Re-validation**
   - @time_validator only runs once (after initial code submission)
   - Reworked code is NOT re-checked against Design Expectations Table
   - No comparison table (Design vs Actual vs Tolerance vs Verdict)

2. **No Samples Validation After Fix**
   - If @code_translator fixes error by changing tune/chains/draws
   - No verification that changes still meet design expectations
   - Risk: "Fix" introduces simplification

3. **No Regression Check**
   - Fixed code might introduce new issues
   - No systematic check that fix didn't break other parameters

---

## 📊 Problem Scenarios

### Scenario 1: Fix Introduces Simplification (CRITICAL RISK)

**What CAN happen**:

```python
# Initial code (Phase 4.5 APPROVED)
trace = pm.sample(
    draws=20000,        # ✅ Within design (16000-24000)
    tune=2000,          # ✅ Exact match
    chains=4,           # ✅ Exact match
    cores=4
)
# Phase 4.5: ✅ APPROVE (100% score)

# Training error occurs (2 hours in)
# Error: AttributeError: 'TensorVariable' object has no attribute 'logp'

# @code_translator fixes error BUT also simplifies (unauthorized)
trace = pm.sample(
    draws=1000,         # ❌ 20× below minimum (16000)
    tune=2000,          # ✅ Still exact
    chains=4,           # ✅ Still exact
    cores=4
)

# @code_translator: "Fix applied: Changed pm.logp to pm.logp()"
# @director: "Resume training"
# @model_trainer: Resumes training

# ⚠️ NO RE-VALIDATION BY @time_validator
# ⚠️ Simplification goes undetected
# Training completes in 43 minutes (vs 12-18 hours expected)

# Phase 5.5: @time_validator checks training duration
# "Training: 43 minutes vs Expected: 12-18 hours"
# ❌ REJECT (Training < 30% of expected)
```

**Problem**: @time_validator detects lazy training (Phase 5.5), but **root cause** (unauthorized simplification during fix) is **missed** because Phase 4.5 was not re-run.

---

### Scenario 2: Fix Changes Design Parameters

**What CAN happen**:

```python
# Initial code (Phase 4.5 APPROVED)
with pm.Model() as model:
    alpha = pm.HalfNormal('alpha', sigma=1)
    beta = pm.Normal('beta', mu=0, sigma=1)
    # ... model definition
    trace = pm.sample(
        draws=20000,
        tune=2000,
        chains=4,
        target_accept=0.95
    )

# Training error: Divergent transitions >10%
# @modeler recommends: "Increase target_accept to 0.99"

# @code_translator fixes:
trace = pm.sample(
    draws=20000,        # ✅ Still within design
    tune=2000,          # ✅ Still exact
    chains=4,           # ✅ Still exact
    target_accept=0.99  # ⚠️ NOT in design expectations table
)

# @code_translator: "Fix applied: target_accept increased to 0.99"
# @director: "Resume training"

# ⚠️ QUESTION: Does this still meet design expectations?
# Design expectations table does NOT specify target_accept
# So is this a violation?
# NO RE-VALIDATION → UNCERTAIN
```

**Problem**: Ambiguous whether parameter added during fix is allowed or not.

---

### Scenario 3: Emergency Protocol Fix (v2.5.8)

**What happens**:

```
@model_trainer: R-hat 1.42 → @modeler (emergency)
@modeler: "@code_translator: 🚨 EMERGENCY FIX AUTHORIZED
Fix: tune: 2000 → 4000, target_accept: 0.95 → 0.99"

@code_translator: Implements fix
@dicator: Retroactive review → ✅ APPROVED
@model_trainer: Resumes training

# ⚠️ QUESTION: Should @time_validator re-run Phase 4.5?
# Design: tune=2000 (exact), target_accept=0.95 (specified)
# Fix: tune=4000, target_accept=0.99
# Does this violate design expectations?

# NO RE-VALIDATION → UNCERTAIN COMPLIANCE
```

**Problem**: Emergency protocol fixes are NOT re-validated against Design Expectations Table.

---

## 🚨 Critical Gap Identified

### Missing Process: Phase 4.5 Re-validation After Rework

**Current State**:
```
Phase 4.5 validation: ✅ ONE TIME ONLY
  ↓
Code rework during training: ❌ NO RE-VALIDATION
  ↓
Risk: Undetected simplification or parameter violations
```

**Should Be**:
```
Phase 4.5 validation: ✅ INITIAL
  ↓
Code rework during training: ⚠️ TRIGGER Phase 4.5 RE-VALIDATION
  ↓
@time_validator: Check modified code against Design Expectations Table
  ↓
If ✅ PASS: Resume training
If ❌ FAIL: Full rework required
```

---

## 📋 Impact Assessment

### Risk Level: **HIGH**

**Why This Matters**:

1. **Academic Fraud Risk**:
   - @code_translator can simplify during fix
   - Goes undetected until Phase 5.5 (training duration check)
   - But Phase 5.5 only checks duration, NOT specific parameters
   - Root cause masked

2. **Design Erosion**:
   - Multiple small fixes → gradual parameter drift
   - Each fix seems reasonable in isolation
   - Cumulative effect violates design expectations
   - No systematic check catches this

3. **Validation Bypass**:
   - @code_translator learns: "Fix during training = escape hatch"
   - Initial Phase 4.5 is strict, but rework is unvalidated
   - Creates incentive to "fix" later rather than implement correctly initially

### Estimated Probability of Occurrence

| Scenario | Probability | Impact | Detection Risk |
|----------|-------------|--------|----------------|
| **Fix introduces simplification** | HIGH (40%) | CRITICAL | LOW (Phase 5.5 may catch, but unclear root cause) |
| **Fix adds new parameters** | MEDIUM (25%) | MEDIUM | VERY LOW (no check) |
| **Emergency fix violates design** | LOW (10%) | HIGH | VERY LOW (retroactive approval doesn't check parameters) |
| **Cumulative parameter drift** | MEDIUM (30%) | HIGH | VERY LOW (no systematic check) |

---

## 🎯 Recommendations

### Recommendation 1: Add Phase 4.5 Re-validation (CRITICAL)

**Update model_trainer.md** Step 3:

```markdown
**Step 3: Error Detected → Report to @director**

**When error detected during watch mode**:

[Current error reporting...]

**@director response**:

@dicator: "@code_translator: Error detected in model_{i}.py
          Error: {specific error}
          Line: {line_number}
          This is a {implementation / data} error.

          Please investigate and provide fix."

**@code_translator investigates and fixes**:

@code_translator: "Investigation complete:
Error cause: {root cause}
Line {line_number}: {what's wrong}

Fix: {specific fix}
Updated code: {patch}
Changes made: {list of all modified parameters}

Recommendation: Resume training from checkpoint (if available) or restart"
```

**NEW: Add re-validation step**:

```markdown
**@director decision (CRITICAL: Must validate reworked code)**:

**IF fix changes design parameters (tune, chains, draws, etc.)**:
@dicator: "@time_validator: RE-VALIDATION REQUIRED

@code_translator has modified model_{i}.py:
Changes: {list of parameter changes}

Please run Phase 4.5 validation on reworked code:
- Check against Design Expectations Table
- Create comparison table (Design vs Actual vs Tolerance vs Verdict)
- Calculate overall score
- Return APPROVE/REJECT decision

Do NOT allow training to resume until validation complete."

**@time_validator runs Phase 4.5**:
- Read reworked model_{i}.py
- Compare to Design Expectations Table
- Generate comparison table
- Return decision:
  - ✅ APPROVE: Changes within tolerance → Allow training
  - ❌ REJECT: Changes violate design → Full rework required

**IF @time_validator APPROVES**:
@dicator: "@model_trainer: Fix applied and validated. Resume training.
Actions:
1. Kill current process
2. Restart training with fixed code
3. Continue monitoring"

**IF @time_validator REJECTS**:
@dicator: "@code_translator: Fix REJECTED by @time_validator
Reason: {specific violation}
Action: Full rework required to match design exactly."
```

---

### Recommendation 2: Define "Design Expectations Compliance Scope"

**Create clarification document**:

```markdown
## Design Expectations Table: Scope of Parameters

### Parameters That CAN Be Modified During Fix (with re-validation)

**Condition**: Fix must be validated by @time_validator before training resumes

**Tolerated adjustments**:
1. **Bug fixes only**: Syntax errors, API incompatibilities
   - Example: `pm.logp(var)` → `pm.logp(var, data)` (API fix)
   - Constraint: Does NOT change algorithm or parameters

2. **Within tolerance adjustments** (if re-validated):
   - tune: 2000 → 2100 (+5%, within ±20% tolerance)
   - draws: 20000 → 19000 (-5%, within ±20% tolerance)
   - Constraint: Must pass Phase 4.5 re-validation

### Parameters That CANNOT Be Modified During Fix

**Absolute red lines** (require Phase 1 rewind):
1. **Algorithm changes**: NUTS → Slice (requires design update)
2. **Feature removal**: Dropping features from design (violates completeness)
3. **Sample reduction**: 20000 → 1000 (violates "Must Not Simplify")

**Emergency protocol exceptions** (v2.5.8):
- Can exceed tolerance IF:
  - Emergency criteria met (R-hat > 1.3 OR 12h+ elapsed)
  - @modeler authorizes
  - @director retroactively approves
```

---

### Recommendation 3: Mandatory Change Summary

**Update @code_translator reporting requirement**:

```markdown
**When reporting fix, you MUST include**:

```
@code_translator: "Investigation complete:
Error cause: {root cause}
Line {line_number}: {what's wrong}

Fix: {specific fix}
Updated code: {patch}

📋 CHANGES SUMMARY (MANDATORY):
- Files modified: model_{i}.py (lines {X}-{Y})
- Parameters changed: {list all changed parameters}
  - Before: {value} → After: {value}
- Algorithm changed: YES/NO
- Features added/removed: YES/NO
- Design expectations compliance: {assessment}

Recommendation: Resume training from checkpoint or restart"
```

**Why this matters**:
- Forces @code_translator to declare all changes
- Enables @director to decide if re-validation needed
- Creates audit trail for parameter modifications
```

---

## ✅ Final Answer Summary

### Question 1: Does @model_trainer → @code_translator go through @director?

**Answer**: ✅ **YES**

**Evidence**:
- model_trainer.md lines 191-228: Complete standard protocol
- @model_trainer reports to @director
- @director delegates to @code_translator
- @director decides when training resumes
- **NO direct @model_trainer → @code_translator communication**

**Exception**: v2.5.8 Emergency Protocol
- @model_trainer → @modeler (direct)
- @modeler → @code_translator (direct)
- BUT @director still reviews retroactively
- Single-use limit, severity threshold, time limit

---

### Question 2: Is reworked code re-validated against Design Expectations Table?

**Answer**: ❌ **NO - This is a CRITICAL GAP**

**Current State**:
- Phase 4.5 validation: **ONE TIME ONLY** (after initial code submission)
- Reworked code: **NO RE-VALIDATION**
- Risk: Undetected simplification or parameter violations

**Missing Components**:
1. No Phase 4.5 re-validation trigger
2. No Design Expectations Table comparison for fixes
3. No parameter change audit trail
4. No regression check for reworked code

**Impact**:
- **HIGH RISK**: Academic fraud through "fix" simplification
- **MEDIUM RISK**: Parameter drift over multiple fixes
- **LOW RISK**: Emergency protocol fixes bypass validation

**Recommendation**: Add Phase 4.5 re-validation step for all fixes that change design parameters.

---

**Document Version**: Rework Validation Gap Analysis
**Last Updated**: 2026-01-19
**Status**: Complete - Critical gap identified
