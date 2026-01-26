# Protocol 15: Observation-Implication Patterns

> **Purpose**: Transform descriptive statements into insightful ones
> **Applies To**: All result statements, figure captions, table descriptions
> **Enforcement**: @narrative_weaver, @writer, @editor, @judge_zero

## Core Principle

Every result statement must contain TWO parts:
1. **Observation**: What the data shows (fact)
2. **Implication**: What this means (insight)

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
```

## Sentence Templates

### Template 1: Basic Observation-Implication

```
[Metric] = [Value] ([Uncertainty]) (Observation), [indicating/suggesting/
demonstrating/revealing] that [Physical/Economic/Policy Meaning] (Implication).
```

**Examples**:
- "RMSE = 4.2 (95% CI: 3.8-4.6), indicating that model predictions are accurate within ±4.2 cases per region."
- "β = 0.7 for developing regions, suggesting higher contact rates compared to developed regions (β = 0.3)."

### Template 2: Comparison-Based

```
[Metric A] vs. [Metric B] shows [Difference] (Observation), demonstrating
that [Reason for Difference] (Implication).
```

**Examples**:
- "Model C (RMSE = 4.2) outperforms Model A (RMSE = 7.2) by 42%, demonstrating that hierarchical structure captures regional heterogeneity."
- "Hub cities show 3.2x faster spread than peripheral cities, demonstrating the amplification effect of network centrality."

### Template 3: Trend-Based

```
[Metric] [increases/decreases] [from X to Y] as [Factor] [changes]
(Observation), which [indicates/suggests] that [Mechanism] (Implication).
```

**Examples**:
- "RMSE decreases from 7.2 to 4.2 as network structure is incorporated, indicating that spatial topology is a first-order effect."

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

### Weak Verbs (AVOID)

| Verb | Problem |
|------|---------|
| shows | Purely descriptive |
| displays | Purely descriptive |
| presents | Purely descriptive |
| is | No implication |

## Quality Checklist

For every result statement, verify:
- [ ] Contains quantitative observation (number, range, comparison)?
- [ ] Contains physical/economic/policy implication?
- [ ] Uses strong implication verb?
- [ ] Avoids purely descriptive language?
- [ ] Includes uncertainty where appropriate?

**If any check fails**: Revise before inclusion.

## Examples: Before and After

### Example 1

**Before** (REJECT):
> "Figure 3 shows the model accuracy."

**After** (ACCEPT):
> "Figure 3 demonstrates that model accuracy reaches 89% (95% CI: 86-92%), indicating robust generalization across validation regions and suggesting the model is suitable for policy scenario analysis."

### Example 2

**Before** (REJECT):
> "The sensitivity analysis is shown in Table 4."

**After** (ACCEPT):
> "Table 4 reveals that predictions remain stable (RMSE ±8%) under ±20% parameter perturbation, demonstrating model robustness and supporting confidence in the policy recommendations."

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture, based on narrative arc template 4
