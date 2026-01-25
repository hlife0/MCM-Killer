# Template: Abstract

> **Purpose**: Structured abstract with required quantitative evidence
> **Word Limit**: 150-200 words
> **Required Elements**: 3+ quantitative metrics

---

## Structure

An O-Prize abstract has **four components**:

1. **Context** (1-2 sentences): Why this problem matters
2. **Method** (2-3 sentences): What we did (innovation)
3. **Results** (2-3 sentences): What we found (with numbers)
4. **Implications** (1-2 sentences): Why it matters (policy/theory)

---

## Template

```
[CONTEXT]
{Problem description} affects {scale/magnitude}. Current approaches
{limitation of existing methods}.

[METHOD]
We develop a {method name} that {key innovation}. Our approach {unique
feature 1} and {unique feature 2}, enabling {capability}.

[RESULTS]
Our model achieves {Metric 1} = {Value 1} ({comparison to baseline}),
{Metric 2} = {Value 2} ({uncertainty}), and {Metric 3} = {Value 3}
({interpretation}). {Additional key finding with number}.

[IMPLICATIONS]
These findings {indicate/demonstrate/reveal} that {insight}. {Policy
recommendation or theoretical contribution with quantified impact}.
```

---

## Required Quantitative Elements

The abstract MUST contain at least **3 quantitative metrics**:

| Metric Type | Examples | Purpose |
|-------------|----------|---------|
| **Performance** | RMSE, R², MAE, Accuracy | Show model quality |
| **Improvement** | ↓27%, 42% reduction | Show value added |
| **Domain** | 3 hub nodes, 10,000 cases | Show real-world relevance |
| **Uncertainty** | 95% CI, p-value | Show rigor |
| **Comparison** | 2x faster, 3.5x more | Show relative benefit |

---

## Example: Epidemic Modeling

```
Global epidemic spread remains a critical public health challenge,
with transmission patterns poorly understood across heterogeneous
populations. Current compartmental models assume homogeneous mixing,
ignoring network topology effects that dominate real-world dynamics.

We develop a Hierarchical SIR-Network model that integrates airline
traffic data with regional demographics. Our approach employs Bayesian
inference with partial pooling, enabling region-specific transmission
estimates while borrowing strength across similar populations.

Our model achieves RMSE = 4.2 (↓42% from baseline), R² = 0.89
(p < 0.001), and identifies 3 critical hub nodes responsible for 67%
of cascade effects. The hierarchical structure reveals systematic
differences: developed regions show β = 0.3 ± 0.05 versus β = 0.7 ± 0.08
for developing regions—a 2.3x difference in transmission rates.

These findings demonstrate that network topology and regional
heterogeneity are essential—not optional—for accurate prediction.
Region-tailored interventions could reduce global mortality by 34%
compared to uniform policies.
```

**Word Count**: 178 words
**Metrics Present**: RMSE, R², 3 hub nodes, 67%, β values, 2.3x, 34%

---

## Common Mistakes

### ❌ AVOID

1. **Vague claims**:
   > "Our model performs well."

2. **No numbers**:
   > "We find significant improvement."

3. **No implications**:
   > "The model was validated." [So what?]

4. **Too technical**:
   > "We use NUTS with 4000 warmup and 2000 samples..."

5. **Too long** (>250 words)

### ✅ DO

1. **Specific claims**:
   > "Our model achieves RMSE = 4.2."

2. **Multiple numbers**:
   > "RMSE = 4.2 (↓42%), R² = 0.89, identifies 3 hub nodes."

3. **Clear implications**:
   > "This suggests region-tailored policies could reduce mortality by 34%."

4. **Accessible language**:
   > "Our approach combines network data with Bayesian estimation..."

5. **Concise** (150-200 words)

---

## Checklist

Before finalizing abstract:

- [ ] Contains problem context (1-2 sentences)?
- [ ] Describes method innovation (2-3 sentences)?
- [ ] Reports ≥3 quantitative metrics?
- [ ] Includes uncertainty or confidence level?
- [ ] States policy/theoretical implication?
- [ ] Word count: 150-200 words?
- [ ] No jargon without explanation?
- [ ] Flows logically from context → method → results → implications?

---

## Sentence Starters

### Context
- "The challenge of [X] affects [scale]..."
- "[Problem] remains a critical concern for [domain]..."
- "Understanding [phenomenon] is essential for [reason]..."

### Method
- "We develop a [model type] that [innovation]..."
- "Our approach integrates [X] with [Y], enabling..."
- "We employ [method] with [enhancement], allowing..."

### Results
- "Our model achieves [metric] = [value]..."
- "The results demonstrate [X]% improvement in..."
- "Analysis reveals [quantitative finding]..."

### Implications
- "These findings indicate that [insight]..."
- "This suggests that [policy/theory recommendation]..."
- "The [X]% improvement has critical implications for..."

---

## Version History

- **v1.0** (2026-01-25): Initial template from m-orientation
