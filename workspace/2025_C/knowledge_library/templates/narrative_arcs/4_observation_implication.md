# Protocol 15: Observation-Implication Templates

> **Purpose**: Transform descriptive statements into insightful ones
> **Applies To**: All result statements, figure captions, table descriptions
> **Enforcement**: @narrative_weaver, @writer, @editor, @judge_zero

---

## Core Principle

Every result statement must contain TWO parts:

1. **Observation**: What the data shows (fact)
2. **Implication**: What this means (insight)

---

## The Problem

### FORBIDDEN (Descriptive Only)

These statements are **banned** in O-Prize papers:

```
❌ "Figure 1 shows RMSE vs. training epochs."
❌ "The accuracy was 85%."
❌ "Table 2 displays the results of sensitivity analysis."
❌ "The model predicts 10,000 cases."
❌ "R² = 0.89 for the regression model."
```

**Why banned?** These tell the reader WHAT but not WHY IT MATTERS.

---

### REQUIRED (Observation + Implication)

These statements are **required**:

```
✅ "Figure 1 shows RMSE decreasing from 7.2 to 4.2 (Observation),
    indicating that network structure is essential for accurate
    epidemic prediction (Implication)."

✅ "The accuracy was 85% (95% CI: 82-88%) (Observation), confirming
    robustness across bootstrap samples (Implication)."

✅ "Table 2 reveals that RMSE varies by ±12% when β changes by ±20%
    (Observation), demonstrating moderate sensitivity that warrants
    careful calibration (Implication)."

✅ "The model predicts 10,000 cases (Observation), suggesting that
    current intervention levels are insufficient to achieve
    containment (Implication)."

✅ "R² = 0.89 (Observation), indicating that the model explains 89%
    of variance while leaving 11% to unmodeled factors—consistent
    with acknowledged regional heterogeneity (Implication)."
```

---

## Sentence Templates

### Template 1: Basic Observation-Implication

```
[Metric] = [Value] ([Uncertainty]) (Observation), [indicating/suggesting/
demonstrating/revealing] that [Physical/Economic/Policy Meaning] (Implication).
```

**Examples**:
- "RMSE = 4.2 (95% CI: 3.8-4.6), indicating that model predictions are
  accurate within ±4.2 cases per region."
- "β = 0.7 for developing regions, suggesting higher contact rates
  compared to developed regions (β = 0.3)."

---

### Template 2: Comparison-Based

```
[Metric A] vs. [Metric B] shows [Difference] (Observation), demonstrating
that [Reason for Difference] (Implication).
```

**Examples**:
- "Model C (RMSE = 4.2) outperforms Model A (RMSE = 7.2) by 42%,
  demonstrating that hierarchical structure captures regional
  heterogeneity that aggregate models miss."
- "Hub cities show 3.2x faster spread than peripheral cities,
  demonstrating the amplification effect of network centrality."

---

### Template 3: Trend-Based

```
[Metric] [increases/decreases] [from X to Y] as [Factor] [changes]
(Observation), which [indicates/suggests] that [Mechanism] (Implication).
```

**Examples**:
- "RMSE decreases from 7.2 to 4.2 as network structure is incorporated,
  which indicates that spatial topology is a first-order effect."
- "Prediction uncertainty increases from ±5% to ±15% beyond day 14,
  which suggests that long-range forecasts require wider confidence bands."

---

### Template 4: Threshold/Condition-Based

```
When [Condition], [Outcome] (Observation), revealing that
[Mechanism is active/constraint is binding] (Implication).
```

**Examples**:
- "When hub infection exceeds 10%, cascade effects dominate (R₀ > 3),
  revealing a critical threshold for intervention timing."
- "When regional β exceeds 0.6, R-hat diverges (>1.3), revealing
  fundamental heterogeneity that global models cannot capture."

---

### Template 5: Surprising Result

```
Contrary to [Expectation/Previous Work], [Finding] (Observation),
which [challenges/extends/refines] our understanding of [Domain Concept]
(Implication).
```

**Examples**:
- "Contrary to homogeneous mixing assumptions, peripheral high-density
  cities showed slower spread than central low-density cities, which
  challenges traditional density-based risk assessment."
- "Unlike previous MCM solutions that used aggregate SEIR, our network
  approach reveals hub-dependent dynamics invisible to compartmental
  models, extending epidemic modeling beyond mean-field assumptions."

---

## Figure Caption Templates

### Template A: Performance Figure

```
Figure [N]: [Title]. [Performance metric] achieves [Value] ([Uncertainty])
(Observation), [demonstrating/indicating] that [Model/Method] effectively
captures [Phenomenon] (Implication). [Additional detail if needed].
```

**Example**:
```
Figure 3: Model Performance Across Regions. RMSE = 4.2 (95% CI: 3.8-4.6)
across 8 regions, demonstrating that the hierarchical network model
effectively captures regional heterogeneity. Hub regions (1-4) show
tighter predictions (RMSE = 3.1) than peripheral regions (5-8, RMSE = 5.3),
consistent with data density differences.
```

---

### Template B: Comparison Figure

```
Figure [N]: [Title]. [Model/Method A] vs. [Model/Method B] shows
[Quantitative Difference] (Observation), demonstrating that [Enhancement]
provides [Specific Benefit] (Implication).
```

**Example**:
```
Figure 4: Model Evolution Comparison. Hierarchical SIR-Network (Model C)
achieves 42% lower RMSE than baseline SIR (Model A), demonstrating that
network topology and regional heterogeneity are essential—not optional—
for accurate epidemic prediction.
```

---

### Template C: Sensitivity Figure

```
Figure [N]: [Title]. [Metric] varies by [Range] when [Parameter] changes
by [Amount] (Observation), indicating [Sensitivity Level] and suggesting
that [Policy/Methodological Implication] (Implication).
```

**Example**:
```
Figure 5: Sensitivity to Transmission Rate. RMSE varies by ±18% when
β is perturbed by ±20%, indicating moderate sensitivity. This suggests
that careful calibration of transmission rates is warranted, particularly
for high-stakes predictions beyond 14 days.
```

---

### Template D: Conceptual Figure

```
Figure [N]: [Title]. [Diagram Description] illustrates [Structure/Process]
(Observation), enabling [Insight/Understanding] (Implication).
```

**Example**:
```
Figure 2: Hierarchical Model Architecture. The three-level structure
(global → cluster → region) illustrates the partial pooling strategy,
enabling information sharing across similar regions while preserving
local variation—a key innovation for handling regional heterogeneity.
```

---

## Table Description Templates

### Template A: Results Table

```
Table [N] summarizes [Metric] across [Conditions/Models] (Observation),
revealing that [Key Finding] (Implication). [Highlight specific values
with interpretation].
```

**Example**:
```
Table 1 summarizes RMSE across three model specifications, revealing
that each enhancement contributes meaningfully: network structure
reduces RMSE by 29% (Model A→B), while hierarchical priors provide
an additional 18% reduction (Model B→C). The compounded improvement
of 42% justifies the additional model complexity.
```

---

### Template B: Parameter Table

```
Table [N] reports [Parameter] estimates with [Uncertainty Measure]
(Observation), indicating that [Interpretation of Values/Ranges]
(Implication).
```

**Example**:
```
Table 2 reports regional transmission rates (β) with 95% credible
intervals, indicating substantial heterogeneity: developed regions
(β = 0.28-0.35) show systematically lower transmission than
developing regions (β = 0.55-0.72). This 2x difference has critical
implications for resource allocation.
```

---

## Verb Reference

### Strong Implication Verbs (PREFERRED)

| Verb | Use When |
|------|----------|
| **indicates** | Direct evidence for a conclusion |
| **demonstrates** | Strong proof of a claim |
| **reveals** | Uncovering something non-obvious |
| **suggests** | Reasonable inference with uncertainty |
| **confirms** | Validating prior expectation |
| **challenges** | Contradicting prior belief |
| **extends** | Building on prior work |
| **enables** | Making something possible |

### Weak Verbs (AVOID)

| Verb | Problem |
|------|---------|
| shows | Purely descriptive |
| displays | Purely descriptive |
| presents | Purely descriptive |
| is | No implication |
| was | No implication |

---

## Quality Checklist

For every result statement, verify:

- [ ] Contains quantitative observation (number, range, comparison)?
- [ ] Contains physical/economic/policy implication?
- [ ] Uses strong implication verb?
- [ ] Avoids purely descriptive language?
- [ ] Includes uncertainty where appropriate?

**If any check fails**: Revise before inclusion.

---

## Examples: Before and After

### Example 1

**Before** (REJECT):
> "Figure 3 shows the model accuracy."

**After** (ACCEPT):
> "Figure 3 shows that model accuracy reaches 89% (95% CI: 86-92%),
> indicating robust generalization across validation regions and
> suggesting the model is suitable for policy scenario analysis."

---

### Example 2

**Before** (REJECT):
> "The sensitivity analysis is shown in Table 4."

**After** (ACCEPT):
> "Table 4 reveals that predictions remain stable (RMSE ±8%) under
> ±20% parameter perturbation, demonstrating model robustness and
> supporting confidence in the policy recommendations derived from
> our baseline calibration."

---

### Example 3

**Before** (REJECT):
> "R-hat values are reported in Table 3."

**After** (ACCEPT):
> "Table 3 reports R-hat < 1.02 for all parameters, confirming
> convergence of the Bayesian inference and validating that our
> posterior estimates are reliable for uncertainty quantification."

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation Protocol 15
