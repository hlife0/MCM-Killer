# @director/@time_validator Handoff Protocol

> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Purpose**: Define clear handoff logic between @director and @time_validator

---

## Problem Statement

**ISSUE**: @director and @time_validator have unclear decision-making boundaries.

**Examples**:
```
@time_validator: "Training time: 78 hours. This seems long."

@director: "Should I approve? Should I reject? What's my criteria?"
```

**Root Cause**: Unclear decision matrix and escalation thresholds.

---

## Decision Ownership (v2.5.7)

### @time_validator's Responsibilities

1. **Analyze** model design, dataset, and code
2. **Estimate** training time accurately
3. **Detect** lazy implementation
4. **Recommend** action (approve/reject/escalate)
5. **DOES NOT decide** on simplification (that's @director's job)

### @director's Responsibilities

1. **Evaluate** @time_validator's recommendations
2. **Decide** on escalations (>48 hours)
3. **Coordinate** solutions (not approve simplifications)
4. **Maintain** strict standards (quality > time)
5. **Consult** @modeler before any design changes

---

## Handoff Protocol (v2.5.7)

### Phase 1.5: Time Estimate Validation

```
@director calls @time_validator:
"@time_validator: Validate time estimates for Phase 5B.

Read:
- output/model/model_design_*.md (all models)
- output/implementation/data/features_*.pkl (all datasets)
- output/implementation/code/model_*.py (all implementations)

Provide:
1. Per-model time estimate
2. Total time estimate
3. Algorithm fidelity check
4. Feature completeness check
5. Recommendation (APPROVE/REJECT/ESCALATE)"
```

**@time_validator response template**:
```markdown
## Time Validation Report

### Files Analyzed
✓ model_design_1.md (Model 1: Hierarchical Bayesian)
✓ model_design_2.md (Model 2: Gradient Boosting)
✓ model_design_3.md (Model 3: Neural Network)
✓ model_design_4.md (Model 4: Ensemble)
✓ features_1.pkl (5000 rows × 50 columns)
✓ features_2.pkl (5000 rows × 50 columns)
✓ features_3.pkl (5000 rows × 50 columns)
✓ features_4.pkl (5000 rows × 50 columns)
✓ model_1.py (PyMC with HMC, 10000 samples × 4 chains)
✓ model_2.py (XGBoost, 1000 trees)
✓ model_3.py (PyTorch NN, 3 layers, 100 epochs)
✓ model_4.py (Ensemble of 4 models)

### Per-Model Estimates

| Model | Algorithm | Dataset | Samples/Params | Expected Time |
|-------|-----------|---------|----------------|---------------|
| 1 | PyMC hierarchical | 5000×50 | 10000×4 | **12-15 hours** |
| 2 | XGBoost | 5000×50 | 1000 trees | **2-3 hours** |
| 3 | Neural Network | 5000×50 | 100 epochs | **4-6 hours** |
| 4 | Ensemble | 5000×50 | 4 models | **18-25 hours** |

### Total Estimate
**Minimum**: 36 hours (12+2+4+18)
**Maximum**: 49 hours (15+3+6+25)
**Expected**: 42 hours

### Algorithm Fidelity Check
- ✓ Model 1: Uses PyMC (matches design)
- ✓ Model 2: Uses XGBoost (matches design)
- ✓ Model 3: Uses PyTorch (matches design)
- ✓ Model 4: Ensemble of 4 (matches design)

### Feature Completeness Check
- ✓ Model 1: All 15 features present
- ✓ Model 2: All 12 features present
- ✓ Model 3: All 20 features present
- ✓ Model 4: All features present

### Recommendation

**Total estimate: 42 hours (<48 hours threshold)**

✅ **RECOMMEND: APPROVE**

All implementations match designs.
All features present.
Total time acceptable.

Action: Proceed with Phase 5B (parallel with paper writing)
```

---

### Phase 4.5: Implementation Fidelity Check

```
@director calls @time_validator:
"@time_validator: STRICT MODE check for model_{i}.py

Verify:
1. Algorithm match (design vs code)
2. Feature completeness (all designed features present)
3. Iterations/parameters (within tolerance)
4. NO unauthorized simplifications

Report: output/docs/validation/time_validator_code_{i}.md"
```

**@time_validator decision matrix**:

| Check | Result | Action |
|-------|--------|--------|
| Algorithm match | ✓ Pass | Continue |
| Algorithm match | ✗ Fail | **AUTO-REJECT**: @code_translator must rework |
| Features | ✓ All present | Continue |
| Features | ✗ Missing | **AUTO-REJECT**: @code_translator must include |
| Iterations | ✓ Within tolerance | Continue |
| Iterations | ✗ Reduced | **AUTO-REJECT**: @code_translator must fix |

**@time_validator response** (if pass):
```markdown
## Implementation Fidelity Report: Model 1

✅ **PASS**: Implementation matches design

### Algorithm
Design: PyMC with HMC
Code: `import pymc as pm; pm.sample(...)` → **MATCH**

### Features
Design: 15 features
Code: All 15 features used → **COMPLETE**

### Iterations
Design: 10000 samples, 4 chains, 2000 tune
Code: `pm.sample(draws=10000, tune=2000, chains=4)` → **MATCH**

### Simplifications
No unauthorized simplifications detected

### Recommendation
✅ **APPROVE**: Proceed to Phase 5
```

**@time_validator response** (if fail):
```markdown
## Implementation Fidelity Report: Model 1

❌ **REJECT**: Lazy implementation detected

### Algorithm
Design: PyMC with HMC
Code: `from sklearn.linear_model import LinearRegression` → **MISMATCH**

### Issue
Code uses sklearn.LinearRegression instead of PyMC.
This is unauthorized simplification.

### Impact
- Expected time: 12-15 hours (PyMC)
- Actual time: <1 min (sklearn)
- Discrepancy: 1000×

### Recommendation
❌ **REJECT**: @code_translator must rework using PyMC

Action Required:
- Reword model_1.py using PyMC (not sklearn)
- Re-run Phase 4.5 validation
- Do not proceed to Phase 5 until fix
```

---

### Phase 5.5: Data Authenticity Check

```
@director calls @time_validator:
"@time_validator: STRICT MODE check for training_{i}.log

Verify:
1. Training duration ≥ 30% of expected (RED LINE)
2. Algorithm used matches design
3. Training iterations completed
4. NO evidence of skip/simplify

Report: output/docs/validation/time_validator_data_{i}.md"
```

**@time_validator decision matrix**:

| Check | Pass Threshold | Fail Action |
|-------|---------------|-------------|
| Training duration | ≥ 30% of expected | Auto-reject |
| Algorithm | Exact match | Reject |
| Features | All present | Reject |
| Iterations | ≥ 80% of specified | Reject |

**@time_validator response** (if fail):
```markdown
## Data Authenticity Report: Model 1

❌ **REJECT**: Training duration red line violation

### Training Duration
Expected: 12-15 hours
Actual: 0.72 hours (43 minutes)
Ratio: 0.72 / 3.6 minimum = **5× below threshold**

### Issue
Training completed in 43 minutes, but design specified 12-15 hours.
This indicates:
- Simplified algorithm (sklearn vs PyMC)
- Reduced iterations (1000 vs 10000)
- Or both

### Algorithm Verification
Design: PyMC with HMC
Code: sklearn.LinearRegression → **MISMATCH**

### Conclusion
❌ **REJECT**: Lazy implementation confirmed

Action Required:
1. Re-run training with correct algorithm (PyMC)
2. Use specified iterations (10000 samples × 4 chains)
3. Expect 12-15 hours training time
4. Do not proceed to Phase 6 until fix complete
```

---

## 48-Hour Escalation Protocol (v2.5.7)

### Trigger: Total Estimate > 48 Hours

**@time_validator response**:
```markdown
## Time Validation Report

⚠️ **48-HOUR THRESHOLD EXCEEDED**

### Total Estimate
Model 1: 15 hours
Model 2: 18 hours
Model 3: 20 hours
Model 4: 25 hours
**Total: 78 hours (>48 hours)**

### Analysis
All implementations match designs ✓
All features present ✓
No simplifications detected ✓

Issue is NOT lazy implementation.
Issue is model complexity vs competition time.

### Competition Time Check
@director: Please provide competition hours remaining

### Options
1. **PROCEED**: If ≥90 hours remaining (sufficient buffer)
2. **PROCEED_WITH_CAUTION**: If ≥78 hours remaining (tight)
3. **CONSULT_MODELER**: If <78 hours (need simplification)

### Recommendation
**ESCALATE_TO_DIRECTOR**

Awaiting decision on:
- Competition time remaining
- Whether to proceed or simplify
```

**@director decision framework**:
```python
def evaluate_48h_escalation(total_hours, competition_remaining):
    """
    @director's decision logic
    """
    if total_hours <= 48:
        # Not an escalation, @time_validator decides
        return "TIME_VALIDATOR_DECIDES"

    # Escalation case (>48 hours)
    if competition_remaining >= total_hours * 1.2:
        # Sufficient buffer (20% margin)
        return {
            'decision': 'PROCEED',
            'rationale': f'Sufficient time: {competition_remaining}h remaining, {total_hours}h needed (20% buffer)',
            'action': 'Start Phase 5B, proceed with parallel workflow'
        }
    elif competition_remaining >= total_hours:
        # Tight but feasible
        return {
            'decision': 'PROCEED_WITH_CAUTION',
            'rationale': f'Tight timeline: {competition_remaining}h remaining, {total_hours}h needed',
            'action': 'Start Phase 5B immediately, use parallel workflow, monitor progress'
        }
    else:
        # Insufficient time
        return {
            'decision': 'CONSULT_MODELER',
            'rationale': f'Insufficient time: {competition_remaining}h remaining, {total_hours}h needed',
            'action': 'Escalate to @modeler for model simplification (requires approval)'
        }
```

---

## @director Decision Scenarios (v2.5.7)

### Scenario 1: <48 Hours, All Pass

```
@time_validator: "Total: 42 hours. All implementations match designs.
                  ✅ RECOMMEND: APPROVE"

@director decision:
✅ **PROCEED**

Rationale:
- 42 hours < 48 hours threshold
- All implementations faithful
- 96 hours competition time remaining
- Sufficient buffer

Action:
"@model_trainer: Start Phase 5B full training.
 @visualizer: Start Phase 6 with quick results (parallel)
 @writer: Start Phase 7 with quick results (parallel)"
```

---

### Scenario 2: >48 Hours, Sufficient Time

```
@time_validator: "Total: 78 hours (>48 hours).
                  All implementations match designs.
                  ⚠️ ESCALATE_TO_DIRECTOR"

@director checks:
- Competition remaining: 90 hours

@director decision:
✅ **PROCEED**

Rationale:
- 78 hours needed, 90 hours remaining
- 12-hour buffer (15% margin)
- Sufficient time

Action:
"@model_trainer: Start Phase 5B immediately.
 Expected: 78 hours.
 @visualizer + @writer: Start parallel work with quick results."
```

---

### Scenario 3: >48 Hours, Tight Timeline

```
@time_validator: "Total: 78 hours (>48 hours).
                  All implementations match designs.
                  ⚠️ ESCALATE_TO_DIRECTOR"

@director checks:
- Competition remaining: 80 hours

@director decision:
⚠️ **PROCEED_WITH_CAUTION**

Rationale:
- 78 hours needed, 80 hours remaining
- Only 2-hour buffer (2.5% margin)
- Tight but feasible

Action:
"@model_trainer: Start Phase 5B IMMEDIATELY.
 Priority: Highest.
 @visualizer + @writer: Start parallel work NOW.
 We will update paper when Phase 5B completes.

 Monitor progress closely.
 If training exceeds estimate, be prepared to adjust."
```

---

### Scenario 4: >48 Hours, Insufficient Time

```
@time_validator: "Total: 78 hours (>48 hours).
                  All implementations match designs.
                  ⚠️ ESCALATE_TO_DIRECTOR"

@director checks:
- Competition remaining: 60 hours

@director decision:
⏸️ **CONSULT_MODELER**

Rationale:
- 78 hours needed, 60 hours remaining
- 18-hour deficit (23% shortfall)
- Insufficient time for full training

Action:
"@modeler: Time constraint issue.

 Competition: 60 hours remaining
 Training estimate: 78 hours
 Deficit: 18 hours

 Options:
 1. Simplify models (requires your approval)
 2. Prioritize 2-3 most critical models
 3. Proceed with Phase 5A only (quick results)

 I will NOT simplify without your consultation.
 Please advise which models are highest priority."

@modeler response:
"Models 1 and 2 are most critical.
 Model 3 and 4 are supplementary.

Recommendation:
- Train Model 1 (15 hours) + Model 2 (18 hours) = 33 hours
- Skip Model 3 and 4
- Total: 33 hours (well within 60 hours remaining)"

@director decision:
✅ **PROCEED_WITH_PRIORITIES**

Action:
"@model_trainer: Train Model 1 and 2 ONLY.
 Skip Model 3 and 4.
 @writer: Document Model 3 and 4 as 'future work'"
```

---

## Simplification Protocol (v2.5.7)

### CRITICAL: @director NEVER Approves Simplification Unilaterally

**❌ FORBIDDEN**:
```
@director: "@time_validator says training will take 78 hours.
          @code_translator: Simplify the models."

@code_translator: "OK, I'll reduce iterations and use sklearn."

Result: Academic fraud
```

**✅ CORRECT**:
```
@director: "@time_validator says training will take 78 hours.
          We have 60 hours remaining.

          @modeler: We need your guidance.
          Options:
          1. Simplify models (requires your design decision)
          2. Prioritize subset of models
          3. Submit with Phase 5A results only

          What do you recommend?"

@modeler: "Models 1 and 2 are critical. 3 and 4 can be future work."

@director: "✅ APPROVED: Train Model 1 and 2 only.
          No simplification, just prioritization."

Result: Maintains quality, manages time
```

---

## Decision Flow: Complete (v2.5.7)

```
┌─────────────────────────────────────┐
│ @director calls @time_validator    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ @time_validator analyzes:           │
│ - model_design_*.md                 │
│ - features_*.pkl                    │
│ - model_*.py                        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ @time_validator provides:           │
│ 1. Time estimate (total)            │
│ 2. Algorithm fidelity               │
│ 3. Feature completeness             │
│ 4. Recommendation                   │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ Total > 48h? │
        └──────┬───────┘
               │
      ┌────────┴────────┐
      │                 │
     NO                YES
      │                 │
      ▼                 ▼
┌──────────┐    ┌─────────────────┐
│ Any      │    │ Time remaining? │
│ failures?│    └────────┬────────┘
└────┬─────┘             │
     │          ┌────────┼────────┐
    NO          │        │        │
     │     ≥120%    80-120%  <80%
     YES        │        │        │
     │          ▼        ▼        ▼
     ▼      ┌─────┐ ┌─────────┐ ┌───────────┐
┌─────────┐│PROCEED│⚠️CAUTION ││CONSULT     │
│@time_val││      │ │         │ │@MODELER   │
│decides  │└─────┘ └─────────┘ └───────────┘
└────┬────┘   │         │           │
     │       │         │           ▼
     ▼       │         │    [@modeler decides]
  AUTO-      │         │    - Simplify?
  REJECT     │         │    - Prioritize?
             │         │    - Phase 5A only?
             │         │
             └─────────┴───────────┐
                                │
                                ▼
                         ┌─────────────┐
                         │ @director   │
                         │ executes    │
                         │ decision    │
                         └─────────────┘
```

---

## Communication Templates (v2.5.7)

### Template 1: @director → @time_validator

```
"@time_validator: Validate time estimates for Phase 5B.

Files to read:
- output/model/model_design_*.md
- output/implementation/data/features_*.pkl
- output/implementation/code/model_*.py

Provide:
1. Per-model time estimate (with rationale)
2. Total time estimate
3. Algorithm fidelity check (design vs code)
4. Feature completeness check
5. Recommendation: APPROVE / REJECT / ESCALATE

Report to: output/docs/validation/time_validator_phase_1.5.md"
```

### Template 2: @time_validator → @director (APPROVE)

```
"## Time Validation Report

Total Estimate: 42 hours (<48 hours threshold)

Per-Model Breakdown:
- Model 1: 12 hours (PyMC, 5000×50, 10000×4)
- Model 2: 8 hours (XGBoost, 5000×50, 1000 trees)
- Model 3: 10 hours (NN, 5000×50, 100 epochs)
- Model 4: 12 hours (Ensemble, 4 models)

Fidelity Check:
✓ All algorithms match designs
✓ All features present
✓ No simplifications detected

Recommendation: ✅ APPROVE

Action: Proceed with Phase 5B"
```

### Template 3: @time_validator → @director (ESCALATE)

```
"## Time Validation Report

⚠️ 48-HOUR THRESHOLD EXCEEDED

Total Estimate: 78 hours

Per-Model Breakdown:
- Model 1: 15 hours
- Model 2: 18 hours
- Model 3: 20 hours
- Model 4: 25 hours

Fidelity Check:
✓ All algorithms match designs
✓ All features present
✓ No simplifications detected

Issue: Model complexity, not lazy implementation

Recommendation: ⚠️ ESCALATE_TO_DIRECTOR

Awaiting decision on:
- Competition time remaining
- Proceed vs simplify vs prioritize"
```

### Template 4: @director → @modeler (CONSULT)

```
"@modeler: Time constraint escalation.

@time_validator estimates: 78 hours training
Competition remaining: 60 hours
Deficit: 18 hours

All models are faithfully implemented (no lazy shortcuts).

Options:
1. Simplify models (requires your design approval)
2. Prioritize subset of models
3. Submit with Phase 5A results only

I will NOT approve simplification without your consultation.

Please advise which approach you recommend."
```

### Template 5: @director → @model_trainer (PROCEED)

```
"@model_trainer: Start Phase 5B full training.

Models to train: [list]

Expected duration: [X hours]
Priority: [Highest / Normal / Parallel with paper]

Output files:
- output/results/results_*.csv
- output/implementation/logs/training_*_full.log
- output/implementation/models/model_*_full.pkl

Start immediately."
```

---

## Consequences of Violating Protocol (v2.5.7)

| Violation | Who | Consequence |
|-----------|-----|-------------|
| @director approves simplification without @modeler | @director | Protocol breach, document issue |
| @time_validator doesn't read all files | @time_validator | Inaccurate estimates, re-do analysis |
| @time_validator doesn't check fidelity | @time_validator | Lazy implementation missed |
| @director unilaterally simplifies | @director | Academic fraud risk |

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
