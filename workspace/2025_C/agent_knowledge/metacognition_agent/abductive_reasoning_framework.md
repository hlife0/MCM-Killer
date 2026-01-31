# Abductive Reasoning Framework

> **Purpose**: Guide for transforming technical symptoms into research insights
> **Reference**: metacognition_agent.md Core Philosophy section

---

## Overview

You use **abductive reasoning** - the logic of best explanation:

```
Observation: Technical symptom observed
  ↓
Hypothesis Generation: Multiple possible explanations
  ↓
Validation: Check against evidence (dev_diary, logs)
  ↓
Best Explanation: Select most supported hypothesis
  ↓
Physical Meaning: Translate to domain understanding
  ↓
Research Value: Extract implications for policy/theory
```

---

## The Three Types of Reasoning

| Type | Direction | Example |
|------|-----------|---------|
| **Deductive** | General → Specific | "All metals conduct electricity. Copper is a metal. Therefore, copper conducts electricity." |
| **Inductive** | Specific → General | "These 100 swans are white. Therefore, all swans are white." |
| **Abductive** | Observation → Best Explanation | "The grass is wet. Best explanation: It rained last night." |

**You use abductive reasoning** because you start with observations (technical symptoms) and work backward to the best explanation (physical mechanism).

---

## Complete Example: Loss Oscillation

### Step 1: Observation

```
Training log shows:
- Epochs 1-49: Loss decreasing steadily (3.2 → 1.1)
- Epochs 50-100: Loss oscillating (1.1 ↔ 1.8)
- Final: Loss settles at 1.4
```

### Step 2: Hypothesis Generation

| Hypothesis | Mechanism | Testable Prediction |
|------------|-----------|---------------------|
| H1: Data heterogeneity | Different regions have different dynamics | Loss oscillation correlates with region batches |
| H2: Learning rate too high | Overshooting minima | Reducing LR should smooth loss |
| H3: Regime shift in data | Pre/post event behavior differs | Loss oscillation starts at specific time point |
| H4: Label noise | Contradictory labels confuse model | High loss on specific samples |

### Step 3: Validation Against Evidence

**Check dev_diary.md**:
```markdown
## Day 2: Loss Oscillation
Noticed loss started oscillating around epoch 50.
Tried reducing learning rate - didn't help.
Checked batch composition - found that African countries
had very different patterns from European countries.
Split training by region - each region converged smoothly.
```

**Evidence supports**: H1 (Data heterogeneity)
**Evidence rejects**: H2 (LR reduction didn't help)

### Step 4: Best Explanation

```
The loss oscillation was caused by data heterogeneity.
African and European countries have fundamentally different
medal-winning dynamics that cannot be captured by a single
global model with pooled parameters.
```

### Step 5: Physical Meaning

```
The oscillation revealed that global pooling assumptions
are violated in Olympic medal prediction. Countries operate
under different "regimes" based on:
- Economic development stage
- Sports infrastructure investment patterns
- Historical participation duration
```

### Step 6: Research Value

```
Policy Implication:
"One-size-fits-all" predictions are inappropriate.
Medal forecasts should be region-specific.

Methodological Contribution:
Hierarchical models with regional random effects
outperform pooled global models.

Future Work:
Investigate optimal clustering of countries by
sports development characteristics rather than geography.
```

---

## Technical → Physical Mapping Table

Use this table to generate hypotheses from technical symptoms:

| Technical Symptom | Physical Hypotheses | Investigation Steps |
|-------------------|---------------------|---------------------|
| **Loss oscillation** | 1. Data heterogeneity<br>2. Regime shift<br>3. Non-stationarity<br>4. Batch composition effects | Check by-group losses, temporal splits, batch statistics |
| **Gradient explosion** | 1. Scale mismatch between features<br>2. Multiplicative relationships<br>3. Numerical precision issues | Check feature ranges, correlation matrix, precision settings |
| **R-hat divergence (>1.1)** | 1. Hidden subgroups in data<br>2. Violated pooling assumption<br>3. Multimodal posterior<br>4. Insufficient warmup | Run by-group, check trace plots, increase warmup |
| **Slow convergence** | 1. Weak identifiability<br>2. Over-parameterization<br>3. Uninformative priors<br>4. High posterior correlation | Check n_eff, reduce parameters, use informative priors |
| **NaN / Inf values** | 1. Boundary violation (log of negative)<br>2. Division by zero<br>3. Overflow from large values<br>4. Underflow from small probabilities | Add guards, check inputs, use log-space |
| **Negative predictions** | 1. Extrapolation beyond training data<br>2. Linear assumption violated<br>3. Missing constraints in model | Add output constraints, use appropriate link function |
| **Overfitting** | 1. Model complexity >> data information<br>2. Insufficient regularization<br>3. Data leakage | Reduce complexity, add regularization, check splits |
| **Underfitting** | 1. Model too simple for data structure<br>2. Important features missing<br>3. Incorrect functional form | Add complexity, feature engineering, try nonlinear |

---

## Validation Techniques

### Cross-Reference with dev_diary.md

```python
# Look for these patterns in dev_diary:
patterns_to_find = [
    "tried",          # What was attempted
    "noticed",        # Observations made
    "found that",     # Discoveries
    "fixed by",       # Solutions that worked
    "didn't help",    # Solutions that failed
    "surprising",     # Unexpected findings
]
```

### Cross-Reference with Log Data

```python
# Check summary.json for:
checks = {
    "loss_trend": "Is oscillation present?",
    "convergence_metrics": "R-hat, n_eff values?",
    "timing": "When did issues start?",
    "by_group": "Any group-specific patterns?",
}
```

---

## Output Templates

### Insight Statement Template

```markdown
**Symptom**: [Specific technical observation with numbers]

**Best Explanation**: The [symptom] was not a bug—it revealed
[physical mechanism]. This indicates [domain phenomenon] is at play.

**Evidence**:
- Log data shows: [specific metrics]
- dev_diary confirms: [coder observation]
- Theory predicts: [why this makes sense]

**Research Value**: This finding suggests [implication for policy/theory/methodology].
```

### Anti-Pattern vs Good Example

**❌ Bad (Technical-only)**:
```
The loss oscillated between epochs 50-100.
We fixed it by reducing batch size.
```

**✅ Good (Physical interpretation)**:
```
The loss oscillation (epochs 50-100) revealed data heterogeneity
between continental regions. African nations' medal dynamics
differ fundamentally from European patterns due to different
sports investment trajectories. This violation of the global
pooling assumption necessitated hierarchical modeling with
regional random effects, improving RMSE by 23%.
```

---

## Quality Checklist

Before finalizing your analysis:

- [ ] Started with specific, quantified observation
- [ ] Generated multiple competing hypotheses
- [ ] Validated against dev_diary.md evidence
- [ ] Validated against log data
- [ ] Selected best explanation with justification
- [ ] Translated to physical/domain meaning
- [ ] Extracted research value (so what?)
- [ ] Used academic language (no emotional framing)
- [ ] Quantified improvements where applicable
