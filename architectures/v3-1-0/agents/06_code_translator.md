# Agent Enhancement: @code_translator

> **Enhancement Type**: Additive (does not replace existing functionality)
> **New Capability**: Development Diary Documentation
> **Added Phase**: Throughout Phase 4 and 5 (Implementation)
> **Purpose**: Capture struggles for @metacognition_agent insight extraction

---

## Overview

This document specifies **enhancements** to the existing @code_translator agent. The core functionality remains unchanged—@code_translator still translates mathematical models into executable code.

**New Addition**: Development Diary (`dev_diary_{i}.md`)

---

## Why This Enhancement?

The v3.0.0 @code_translator produced working code but lost **the story of the struggle**. When code "just works," we lose:

1. **What went wrong initially** (gradient explosions, convergence issues)
2. **Why certain choices were made** (why this optimizer, why this learning rate)
3. **What the errors revealed** (data heterogeneity, model misspecification)

This information is **gold** for the paper narrative but was previously discarded.

---

## The Development Diary

### Purpose

Capture the **subjective experience** of implementation to complement the **objective logs**.

### When to Write

Write a diary entry whenever:
- An error occurs and is fixed
- A design decision is made
- Something unexpected happens
- A parameter is tuned
- The model is modified

### Diary Location

```
output/docs/insights/dev_diary_{model_number}.md
```

---

## Diary Entry Format

Structure based on `templates/writing/3_dev_diary_entry.md`.

```markdown
# Development Diary: Model {i}

> **Model**: {Model Name}
> **Implementation Start**: {Timestamp}
> **Implementation End**: {Timestamp}
> **Status**: [In Progress / Complete / Blocked]

---

## Entry 1: {Timestamp}

### Context
[What was I trying to do?]

### The Struggle
**Symptom**: [What error/issue occurred?]
**Error Message** (if applicable):
```
[Exact error text]
```

### The Investigation
[What did I try to diagnose the problem?]
- Tried: [Action 1] → Result: [What happened]
- Tried: [Action 2] → Result: [What happened]
- Tried: [Action 3] → Result: [What happened]

### The Fix
**Solution**: [What fixed the problem?]
**Code Change**:
```python
# Before
[old code]

# After
[new code]
```

### The Why (My Hypothesis)
[Why do I think this happened? What does this reveal about the data/model/problem?]

**Physical Interpretation**: [If applicable, what does this mean in domain terms?]

### Time Spent
- Diagnosis: {X} minutes
- Fix: {Y} minutes
- Verification: {Z} minutes

---

## Entry 2: {Timestamp}
...

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Entries | {N} |
| Total Struggles | {M} |
| Time on Debugging | {X} hours |
| Most Common Issue | {Category} |

---

## Key Insights for @metacognition_agent

1. **Insight 1**: [What did the struggles reveal?]
2. **Insight 2**: [What pattern emerged?]
3. **Insight 3**: [What should the paper highlight?]
```

---

## Struggle Categories

When documenting a struggle, classify it:

| Category | Examples | Typical Physical Meaning |
|----------|----------|-------------------------|
| **Convergence** | Loss diverges, R-hat > 1.1 | Data heterogeneity, model misspecification |
| **Numerical** | NaN, Inf, overflow | Scale mismatch, wrong functional form |
| **Performance** | Too slow, memory issues | Complexity vs data tradeoff |
| **Logic** | Wrong output, unexpected behavior | Assumption violation |
| **Data** | Missing values, format issues | Real-world messiness |
| **Integration** | API mismatch, dependency issues | Technical debt |

---

## Example Diary Entries

### Example 1: Gradient Explosion

```markdown
## Entry 3: 2026-01-25 14:32

### Context
Training SIR-Network model with Adam optimizer, lr=0.01.

### The Struggle
**Symptom**: Loss exploded to Inf at epoch 5
**Error Message**:
```
RuntimeWarning: overflow encountered in exp
Loss: inf
```

### The Investigation
- Tried: Reducing lr to 0.001 → Still exploded at epoch 12
- Tried: Gradient clipping (max_norm=1.0) → Stabilized but loss oscillates
- Tried: Log-transform on β parameter → Stable training

### The Fix
**Solution**: Applied log-transform to transmission rate β
**Code Change**:
```python
# Before
beta = nn.Parameter(torch.tensor(0.5))

# After
log_beta = nn.Parameter(torch.tensor(-0.69))  # log(0.5)
beta = torch.exp(log_beta)  # Ensures positivity
```

### The Why (My Hypothesis)
The gradient explosion reveals that **β interacts multiplicatively** with other parameters (population, contact rate). The original additive parameterization forced the optimizer to make increasingly large updates. Log-transform respects the multiplicative nature.

**Physical Interpretation**: Transmission rate effects compound—a 10% increase in β has different absolute effects at β=0.1 vs β=0.9. Log-space makes the optimization landscape more uniform.

### Time Spent
- Diagnosis: 25 minutes
- Fix: 10 minutes
- Verification: 15 minutes
```

---

### Example 2: R-hat Divergence

```markdown
## Entry 5: 2026-01-25 16:45

### Context
Running Bayesian hierarchical model with 8 regions.

### The Struggle
**Symptom**: R-hat > 1.3 for regions 5-8 (Asia-Pacific) even with 10,000 samples
**Diagnostic Output**:
```
Region 1 (NA): R-hat = 1.02 ✓
Region 2 (EU): R-hat = 1.01 ✓
...
Region 5 (Asia): R-hat = 1.37 ✗
Region 6 (Pacific): R-hat = 1.42 ✗
```

### The Investigation
- Tried: Increasing samples to 20,000 → Still divergent
- Tried: Stronger priors (σ=0.1 instead of 1.0) → Improved to R-hat=1.15, still >1.05
- Tried: Non-centered parameterization → No improvement
- Tried: Removing regions 5-8 → All remaining regions converge perfectly

### The Fix
**Solution**: Created separate parameter groups for distinct regional clusters
**Code Change**:
```python
# Before
beta = pm.Normal('beta', mu=beta_global, sigma=sigma_pool, shape=8)

# After
# Two-cluster hierarchical model
beta_developed = pm.Normal('beta_dev', mu=mu_dev, sigma=sigma_dev, shape=4)
beta_developing = pm.Normal('beta_developing', mu=mu_developing, sigma=sigma_developing, shape=4)
beta = tt.concatenate([beta_developed, beta_developing])
```

### The Why (My Hypothesis)
The R-hat divergence is NOT a numerical issue—it reveals **fundamental regional heterogeneity**. Asia-Pacific regions have distinct cultural factors (mask-wearing norms, collectivist compliance) and economic factors (healthcare access, population density) that cannot be captured by a single global prior.

**Physical Interpretation**: One-size-fits-all epidemic models fail because transmission mechanisms differ qualitatively between developed and developing regions. This is a FEATURE of the data, not a bug in the code.

### Time Spent
- Diagnosis: 45 minutes
- Fix: 30 minutes
- Verification: 20 minutes

### Note for @metacognition_agent
This is a major insight! The "failure" to converge actually revealed the key finding of our paper: regional heterogeneity in transmission dynamics. This should be the centerpiece of Section 3.3.
```

---

## Integration with Existing @code_translator

### Original Responsibilities (Preserved)
1. Translate mathematical specifications to code
2. Ensure code correctness and efficiency
3. Handle data preprocessing
4. Implement training loops

### New Responsibilities (Added)
5. **Document struggles in dev_diary_{i}.md**
6. **Classify issues by category**
7. **Provide physical interpretation hypotheses**
8. **Flag major insights for @metacognition_agent**

---

## Workflow Integration

### During Implementation (Phase 4/5)

```
@code_translator receives model specification
    ↓
Attempts implementation
    ↓
[If error occurs]
    ├── Fix the error (as before)
    └── NEW: Write diary entry
        ├── Document symptom
        ├── Document investigation
        ├── Document fix
        └── Hypothesize physical meaning
    ↓
Continue implementation
    ↓
[On completion]
    ├── Produce working code (as before)
    └── NEW: Finalize dev_diary_{i}.md
```

### After Implementation (Phase 5.8)

```
@metacognition_agent reads:
    ├── logs/summary.json (objective)
    └── dev_diary_{i}.md (subjective) ← NEW INPUT
    ↓
Generates narrative_arc_{i}.md
```

---

## Quality Standards for Diary Entries

### DO:
- Write entries in real-time, not retrospectively
- Be specific about error messages and symptoms
- Include actual code snippets (before/after)
- Hypothesize about physical meaning
- Flag insights that should appear in the paper

### DON'T:
- Skip entries because "it was a simple bug"
- Write vague descriptions ("something was wrong")
- Forget to include the investigation steps
- Omit time spent (useful for project management)

---

## Minimum Entry Requirements

Each struggle entry MUST contain:

1. **Timestamp** - When did this happen?
2. **Symptom** - What went wrong? (exact error or behavior)
3. **Fix** - What solved it? (code or configuration change)
4. **Hypothesis** - Why did this happen? (physical/domain interpretation)

Optional but valuable:
- Investigation steps (what was tried)
- Time spent (for project tracking)
- Flag for @metacognition_agent (if major insight)

---

## Output Files

### Primary Output (Existing)
- `src/models/model_{i}.py` - Executable model code
- `src/training/train_{i}.py` - Training script

### New Outputs
- `output/docs/insights/dev_diary_{i}.md` - Struggle documentation
- Comments in code linking to diary entries:
  ```python
  # Note: Log-transform required due to gradient explosion
  # See dev_diary_1.md Entry 3 for details
  log_beta = nn.Parameter(torch.tensor(-0.69))
  ```

---

## Version History

- **v1.0** (2026-01-25): Initial enhancement specification from m-orientation Sprint 2
