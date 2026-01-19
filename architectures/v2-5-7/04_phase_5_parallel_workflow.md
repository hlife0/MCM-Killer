# Phase 5 Parallel Workflow Protocol

> **Version**: v2.5.7
> **Date**: 2026-01-19
> **Purpose**: Allow paper writing to proceed after Phase 5A without waiting for Phase 5B

---

## Problem Statement

**INEFFICIENCY**: Phase 5B (Full Training) takes 6+ hours, but paper writing must wait until completion.

**Current Workflow (v2.5.6)**:
```
Phase 5A (30 min) → Phase 5B (6+ hours) → Phase 6 (Visualization) → Phase 7 (Paper Writing)

Problem: @writer idle for 6+ hours waiting for Phase 5B to complete
```

**Desired Workflow (v2.5.7)**:
```
Phase 5A (30 min) → Branch:
  ├─ Path A: Phase 6 (Quick) → Phase 7 (Paper with quick results)
  └─ Path B: Phase 5B (6+ hours, parallel)

When Phase 5B completes → Update paper with final results
```

---

## Core Principle

**PAPER WRITING PROCEEDS AFTER PHASE 5A**

Phase 5A provides sufficient results for paper structure and preliminary analysis.

Phase 5B runs in parallel, results integrated when complete.

---

## Implementation: Phase 5 Split Workflow

### Phase 5A: Quick Training (MANDATORY, ≤30 min)

**Purpose**: Validate model viability, provide preliminary results

**Specification**:
- **Data**: 10-20% of full dataset
- **Iterations**: Reduced (e.g., 20% of full iterations)
- **Goal**: Ensure model trains without errors
- **Output**: `results_quick_{i}.csv`

**Exit Criteria**:
- [ ] All models train successfully
- [ ] No crashes or errors
- [ ] Preliminary results reasonable
- [ ] `results_quick_{i}.csv` files exist

**Example**:
```python
# Phase 5A specification
quick_data_ratio = 0.15  # 15% of full data
quick_iterations = 1000   # vs 10000 for full training
quick_chains = 2          # vs 4 for full training

# Expected time: 20-30 minutes total
```

---

### Phase 5B: Full Training (OPTIONAL BUT RECOMMENDED, >6 hours)

**Purpose**: Generate high-quality results for final submission

**Specification**:
- **Data**: 100% of dataset
- **Iterations**: Full convergence (as specified in model_design.md)
- **Goal**: Publication-quality results with tight confidence intervals
- **Output**: `results_{i}.csv`

**Time Expectation (v2.5.7 UPDATED)**:
- **Minimum**: 6 hours (per model)
- **Typical**: 8-12 hours (per model)
- **Maximum**: Up to 48 hours (with @director approval)

**Example**:
```python
# Phase 5B specification (v2.5.7)
full_data_ratio = 1.0    # 100% of data
full_iterations = 10000   # Full MCMC sampling
full_chains = 4           # Full parallel chains
tune_samples = 2000       # Full tuning

# Expected time: 8-12 hours per model
# 4 models × 10 hours = 40 hours total
```

**❌ FORBIDDEN**: "Time constraints, skip Phase 5B"
**✅ REQUIRED**: At minimum complete Phase 5A
**✅ RECOMMENDED**: Execute Phase 5B if competition time permits

---

### Parallel Workflow (v2.5.7 NEW)

```
AFTER Phase 5A completes:

Path A (PAPER PATH):
  Phase 5A (quick results) → Phase 6 (Quick figures) → Phase 7 (Paper draft)
  Time: 30 min + 30 min + 2-3 hours = 3-4 hours

Path B (TRAINING PATH):
  Phase 5A (quick results) → Phase 5B (Full training, parallel with Path A)
  Time: 6-12 hours (runs in background)

MERGE:
  When Phase 5B completes → Update Phase 6 figures → Update Phase 7 paper sections
  Time: 30 min (update figures) + 1 hour (update paper)
```

**@director coordination**:
```python
# After Phase 5A completes
@director: "@model_trainer: Start Phase 5B full training in background.
             Expected time: 8-12 hours.
             Generate: results_1.csv, results_2.csv, results_3.csv, results_4.csv"

@director: "@visualizer: Create figures using results_quick_*.csv.
             These are preliminary, we'll update with final results later."

@director: "@writer: Start writing paper using results_quick_*.csv.
             Mark Results section as DRAFT.
             We'll update with final results when Phase 5B completes."
```

**When Phase 5B completes**:
```python
@model_trainer: "Phase 5B complete. Final results: results_*.csv"

@director: "@visualizer: Regenerate figures with final results.
             Replace quick_*.png with final_*.png"

@director: "@writer: Update Results section with final results.
             Update tables, figures, and analysis.
             Remove DRAFT marker from Results section."
```

---

## File Naming Convention (v2.5.7)

| Phase | File | Purpose | Timing |
|-------|------|---------|--------|
| 5A | `results_quick_{i}.csv` | Quick validation results | After 5A (30 min) |
| 5B | `results_{i}.csv` | Final high-quality results | After 5B (6-12 hours) |
| 6 (quick) | `figure_{name}_quick.png` | Quick figures for paper draft | Parallel with 5B |
| 6 (final) | `figure_{name}.png` | Final figures | After 5B completes |
| 7 (draft) | `paper_draft.tex` | Paper with quick results | Parallel with 5B |
| 7 (final) | `paper.tex` | Updated with final results | After 5B completes |

---

## Phase 5B Time Expectations (v2.5.7 CRITICAL UPDATE)

### Old Specification (v2.5.6) - DEPRECATED

```
Phase 5B: Full Training (4-6 hours)
```

**Problem**: "4-6 hours" creates false expectation. Actual training often takes longer.

### New Specification (v2.5.7) - ACTIVE

```
Phase 5B: Full Training (>6 hours)

Minimum: 6 hours per model
Typical: 8-12 hours per model
Maximum: 48 hours (with @director approval)
```

**Per-Model Breakdown**:

| Model Type | Complexity | Iterations | Expected Time |
|------------|-----------|------------|---------------|
| Simple Bayesian | Low | 2000 samples | 4-6 hours |
| Hierarchical Bayesian | Medium | 5000 samples | 6-10 hours |
| Complex Bayesian | High | 10000 samples | 10-15 hours |
| Deep Learning | Very High | 5000 epochs | 12-20 hours |

**Total Competition Time**:
- 4 models × 8 hours = 32 hours
- Competition: 4 days × 24 hours = 96 hours
- **Training time: 33% of competition (acceptable)**

**@modeler Time Estimate Requirements**:
```markdown
## Time Estimate (MANDATORY)

For each model, provide:
- Algorithm: [e.g., PyMC with HMC]
- Data size: [e.g., 5000 rows × 50 columns]
- Iterations: [e.g., 10000 samples, 4 chains]
- Expected time: [e.g., 10-12 hours]

Rationale: [Explain calculation]
```

---

## 48-Hour Escalation Protocol (v2.5.7 NEW)

### Trigger

**When @time_validator predicts >48 hours training**:

```
@time_validator: "Director, Phase 5B time estimate:

Model 1: 15 hours
Model 2: 18 hours
Model 3: 20 hours
Model 4: 25 hours
Total: 78 hours (>48 hours threshold)

Recommendation: Request @director decision on:
1. Proceed with full training (78 hours)
2. Simplify models (requires consultation)
3. Prioritize subset of models"

Action: ESCALATE_TO_DIRECTOR
```

### @director Decision Framework

```python
def evaluate_48h_escalation(total_hours, competition_hours_remaining):
    """
    @director decision logic for >48h training estimates
    """
    if total_hours > 48:
        # Check competition time remaining
        if competition_hours_remaining >= total_hours * 1.2:
            # Sufficient buffer, proceed
            decision = "PROCEED"
            rationale = "Sufficient competition time (96 hours total)"
        elif competition_hours_remaining >= total_hours:
            # Tight but feasible
            decision = "PROCEED_WITH_CAUTION"
            rationale = "Tight timeline, parallel work required"
        else:
            # Insufficient time
            decision = "CONSULT_MODELER"
            rationale = "Need to simplify or prioritize models"

    return decision, rationale
```

**@director response examples**:

```
Scenario 1: 78 hours, 90 hours remaining
@director: "PROCEED with full training.
            Competition has 90 hours remaining.
            78 hours training + 12 hours buffer = sufficient."

Scenario 2: 78 hours, 60 hours remaining
@director: "PROCEED_WITH_CAUTION.
            Start Phase 5B immediately.
            Paper writing proceeds in parallel with quick results.
            Update paper when Phase 5B completes."

Scenario 3: 78 hours, 48 hours remaining
@director: "CONSULT_MODELER.
            @modeler: We have 48 hours remaining, training estimated 78 hours.
            Options:
            1. Simplify models (consult before changing)
            2. Prioritize 2-3 most critical models
            3. Phase 5A only (submit with quick results)
            Awaiting recommendation."
```

**CRITICAL**: **NEVER simplify without @modeler consultation**

---

## Workspace Directory (v2.5.7 ENHANCED)

### Enhanced Directory Structure

```
output/
├── implementation/
│   ├── code/
│   │   ├── model_1.py
│   │   ├── model_2.py
│   │   ├── model_3.py
│   │   └── model_4.py
│   ├── data/
│   │   ├── features_1.pkl        # Feature matrix (shape, size metadata)
│   │   ├── features_2.pkl
│   │   ├── features_3.pkl
│   │   └── features_4.pkl
│   ├── logs/
│   │   ├── training_1_quick.log  # Phase 5A log
│   │   ├── training_1_full.log   # Phase 5B log
│   │   └── training_*.log
│   └── models/
│       ├── model_1_quick.pkl     # Quick model (Phase 5A)
│       └── model_1_full.pkl      # Full model (Phase 5B)
├── results/
│   ├── results_quick_1.csv       # Phase 5A results
│   ├── results_1.csv             # Phase 5B results
│   └── results_*.csv
└── docs/
    └── validation/
        └── time_validator_*.md   # @time_validator reports
```

### Metadata Requirements (v2.5.7 NEW)

**@time_validator MUST read**:

1. **Dataset shape/size**: `output/implementation/data/features_{i}.pkl`
   ```python
   import pandas as pd
   df = pd.read_pickle('output/implementation/data/features_1.pkl')

   # Log shape and size
   print(f"Shape: {df.shape}")  # (5000, 50)
   print(f"Memory: {df.memory_usage().sum() / 1024**2:.2f} MB")
   ```

2. **Model script implementation**: `output/implementation/code/model_{i}.py`
   - Read every line
   - Analyze time complexity
   - Check for simplifications

3. **Training log**: `output/implementation/logs/training_{i}_full.log`
   - Extract actual training time
   - Verify iterations completed
   - Check convergence

---

## Decision Flow: Phase 5

```
Phase 5A Complete?
├─ Yes → @director decision:
│   ├─ Option 1: Start Phase 5B in background + Start paper writing (PARALLEL)
│   ├─ Option 2: Start Phase 5B, wait for completion (SEQUENTIAL)
│   └─ Option 3: Skip Phase 5B, submit with Phase 5A results (LAST RESORT)
│
└─ No → @model_trainer debug → Retry Phase 5A

[After Phase 5A complete]

@director checks @time_validator estimate:
├─ Estimate < 48 hours?
│   ├─ Yes → PROCEED with Phase 5B + Start paper (PARALLEL)
│   └─ No (>48 hours) → ESCALATE
│       ├─ Time remaining sufficient?
│       │   ├─ Yes → PROCEED with caution
│       │   └─ No → CONSULT @modeler for simplification
```

---

## Example: Full Workflow (v2.5.7)

```
T=0h: Phase 5A starts
T=0.5h: Phase 5A complete → results_quick_*.csv

@director decision:
"@time_validator: Estimate Phase 5B time"

@time_validator:
"Model 1: 10 hours (PyMC, 10000 samples, 5000 rows)
 Model 2: 12 hours (PyMC, 10000 samples, 5000 rows)
 Model 3: 8 hours (PyMC, 5000 samples, 5000 rows)
 Model 4: 15 hours (Ensemble, 20000 samples)
 Total: 45 hours (<48 hours, PROCEED)"

@director: "PROCEED with PARALLEL workflow.

            Path A: @visualizer + @writer start work
            Path B: @model_trainer starts Phase 5B"

T=0.5h: Phase 6 starts (quick figures)
T=1h: Phase 7 starts (paper with quick results)
T=4h: Paper draft complete

T=45h: Phase 5B complete → results_*.csv

@director: "@visualizer: Regenerate figures with final results
            @writer: Update Results section with final results"

T=46h: Final paper complete
T=46h: Phase 8-10 proceed (final polish)
```

---

## Consequences of Skipping Phase 5B

| Scenario | Impact | O-Prize Competitiveness |
|----------|--------|------------------------|
| Phase 5A only (quick results) | Weak confidence intervals, unstable estimates | **Non-competitive** |
| Phase 5B full training | Tight confidence intervals, robust estimates | **Competitive** |

**@advisor responsibility**: "If Phase 5B skipped → MUST downgrade quality assessment"

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
