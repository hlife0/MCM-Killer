# Results Summary Snippet Guide

> **Purpose**: Template and examples for generating pre-Phase 7 results summaries
> **Reference**: metacognition_agent.md Results Summary Snippet section (V2.0)

---

## Overview

> **"Writing Enhancement" Protocol - Pre-Generated Summary**

Before Phase 7, you MUST generate a structured Results Summary Snippet.
This prevents @writer timeouts from parsing raw CSVs.

**Output File**: `output/docs/results_summary_snippet.md`

**Timing**: Generate at end of Phase 5.8, before Phase 6.

---

## Full Template

```markdown
# Results Summary Snippet (for @writer)

## Quick Stats (copy-paste ready)
- Total countries analyzed: {N}
- Time period: {start_year} - {end_year}
- Key metric range: {min} - {max} ({unit})
- Total Olympics covered: {N_olympics}
- Total athlete-events: {N_records}

## Model-by-Model Summary

### Model 1: {Name}
**Key Finding**: {One sentence with specific number}
**Performance**: R² = {value}, RMSE = {value}, MAE = {value}
**Notable**: {Surprising or important observation}
**Confidence**: {95% CI for key parameter or prediction}

### Model 2: {Name}
**Key Finding**: {One sentence with specific number}
**Performance**: {Primary metric} = {value}, {Secondary metric} = {value}
**Notable**: {Observation}
**Confidence**: {Uncertainty quantification}

### Model 3: {Name}
**Key Finding**: {One sentence with specific number}
**Performance**: {Metrics}
**Notable**: {Observation}
**Confidence**: {Uncertainty}

[... repeat for all models ...]

## Top 5 Insights (for Results section)
1. {Insight with specific number and context}
2. {Insight with specific number and context}
3. {Insight with specific number and context}
4. {Insight with specific number and context}
5. {Insight with specific number and context}

## Counterintuitive Findings (for Discussion)
- {Finding that challenges expectations, with evidence}
- {Finding that challenges conventional wisdom}
- {Unexpected relationship or non-relationship}

## Key Comparisons
- Model X vs Model Y: {Which performed better and by how much}
- Before vs After intervention: {Quantified difference}
- Region A vs Region B: {Key difference}

## Ready-to-Use Sentences
- "Our analysis reveals that {X} accounts for {Y%} of variance in {outcome}..."
- "Surprisingly, {factor} showed a {direction} relationship with {outcome} (β = {value}, p < {threshold})..."
- "The model predicts {outcome} with {metric} = {value} ({confidence interval})..."
- "Sensitivity analysis confirms that results are robust to {assumption} (Δ < {threshold})..."
- "The {effect} explains approximately {X%} of the observed {phenomenon}..."

## Tables Ready for LaTeX

### Table 1: Model Comparison
| Model | R² | RMSE | MAE | Key Strength |
|-------|-----|------|-----|--------------|
| Model 1 | {val} | {val} | {val} | {strength} |
| Model 2 | {val} | {val} | {val} | {strength} |
| ... | ... | ... | ... | ... |

### Table 2: Key Coefficients
| Variable | Coefficient | 95% CI | Interpretation |
|----------|-------------|--------|----------------|
| {var1} | {β} | [{lo}, {hi}] | {meaning} |
| {var2} | {β} | [{lo}, {hi}] | {meaning} |
| ... | ... | ... | ... |
```

---

## Complete Example

```markdown
# Results Summary Snippet (for @writer)

## Quick Stats (copy-paste ready)
- Total countries analyzed: 206
- Time period: 1896 - 2024
- Key metric range: 0 - 473 (total medals per country per Olympics)
- Total Olympics covered: 29 Summer Games
- Total athlete-events: 271,116 records

## Model-by-Model Summary

### Model 1: Bayesian Hierarchical Medal Predictor
**Key Finding**: GDP per capita explains 68.3% of variance in medal counts
**Performance**: R² = 0.683, RMSE = 4.2 medals, MAE = 2.8 medals
**Notable**: Effect sizes vary by 3.2x between developed and developing nations
**Confidence**: GDP coefficient β = 0.71 (95% CI: [0.62, 0.80])

### Model 2: Host Nation Advantage Model
**Key Finding**: Host nations gain 12.3 additional medals on average
**Performance**: Effect size = 12.3 medals (Cohen's d = 0.89)
**Notable**: Effect persists for 2 Olympics after hosting (decay rate = 0.6/cycle)
**Confidence**: Host effect 95% CI: [8.7, 15.9] medals

### Model 3: Sport-Specific Efficiency Model
**Key Finding**: Investment efficiency varies 5.8x across sports categories
**Performance**: Within-sport R² = 0.81, Cross-sport R² = 0.54
**Notable**: Small nations excel in technical sports (gymnastics, diving)
**Confidence**: Efficiency rankings stable across bootstrap samples (τ = 0.92)

### Model 4: Historical Momentum Model
**Key Finding**: Past 3 Olympics explain 23% of incremental medal gains
**Performance**: AR(3) model RMSE = 3.1 medals
**Notable**: Momentum effect stronger for rising nations (β = 1.4) vs established (β = 0.3)
**Confidence**: Momentum coefficient 95% CI: [0.18, 0.28]

### Model 5: Medal Redistribution Simulator
**Key Finding**: Adding 5 new sports increases medal inequality (Gini +0.04)
**Performance**: Simulation validated against 2020 Tokyo (error < 5%)
**Notable**: Proposed sports favor existing medal leaders (78% capture rate)
**Confidence**: Redistribution predictions 90% CI width: ±8 medals for top 20

### Model 6: Unified Prediction Framework
**Key Finding**: Ensemble reduces prediction error by 18% vs best single model
**Performance**: R² = 0.76, RMSE = 3.4 medals
**Notable**: Model disagreement highest for "breakthrough" nations
**Confidence**: 2028 LA predictions with 95% PI width: ±6.2 medals average

## Top 5 Insights (for Results section)
1. GDP per capita shows stronger predictive power (r = 0.72) than total GDP (r = 0.61), suggesting investment intensity matters more than absolute wealth
2. Host advantage is 40% larger for nations with < 50 historical medals, indicating disproportionate benefit for smaller Olympic programs
3. Winter sports show higher regional concentration (Gini = 0.89) than summer sports (Gini = 0.67), reflecting climate-dependent infrastructure requirements
4. Historical momentum explains 23% of incremental medal gains, but effect diminishes for nations with > 100 cumulative medals
5. Climate-sport matching improves predictions by 8.3% for winter sports but only 2.1% for summer sports

## Counterintuitive Findings (for Discussion)
- Population size has negative partial correlation with medals per capita (r = -0.34) after controlling for GDP, suggesting diseconomies of scale in talent development
- Wealthier nations show diminishing returns above $50K GDP/capita, with optimal efficiency around $35-45K
- Historical medal momentum is weaker for traditionally dominant nations, suggesting "ceiling effects" in sports development

## Key Comparisons
- Bayesian vs Frequentist: Bayesian model outperforms by 12% RMSE with better uncertainty quantification
- 2020 vs 2024 predictions: Model accuracy improved from 82% to 89% within top-20 ranking
- Continental: Europe (mean = 24 medals) vs Africa (mean = 3 medals), gap narrowing at 0.5 medals/decade

## Ready-to-Use Sentences
- "Our analysis reveals that GDP per capita accounts for 68.3% of variance in national medal counts, significantly outperforming population-based predictors (ΔR² = 0.21)."
- "Surprisingly, population showed a negative relationship with medals per capita after controlling for economic factors (β = -0.34, p < 0.001), suggesting that larger nations face coordination challenges in elite sports development."
- "The model predicts 2028 Los Angeles medal distributions with RMSE = 3.4 medals and 95% prediction intervals averaging ±6.2 medals for top-20 nations."
- "Sensitivity analysis confirms that results are robust to prior specification (Bayes factor < 3 across reasonable priors) and temporal subsetting (cross-validation RMSE stable within ±0.4 medals)."
- "The host nation effect explains approximately 8% of the observed variance in medal counts, with benefits persisting for an average of 1.7 subsequent Olympic cycles."

## Tables Ready for LaTeX

### Table 1: Model Comparison
| Model | R² | RMSE | MAE | Key Strength |
|-------|-----|------|-----|--------------|
| Bayesian Hierarchical | 0.683 | 4.2 | 2.8 | Uncertainty quantification |
| Host Effect | 0.71 | 3.9 | 2.6 | Causal interpretation |
| Sport-Specific | 0.81 | 3.1 | 2.1 | Granular predictions |
| Historical Momentum | 0.62 | 4.8 | 3.2 | Trend capture |
| Redistribution Sim | N/A | 4.1 | 2.9 | Policy scenarios |
| Unified Ensemble | 0.76 | 3.4 | 2.3 | Overall accuracy |

### Table 2: Key Coefficients
| Variable | Coefficient | 95% CI | Interpretation |
|----------|-------------|--------|----------------|
| GDP per capita (log) | 0.71 | [0.62, 0.80] | 10% GDP increase → 7% more medals |
| Host nation | 12.3 | [8.7, 15.9] | Medals above baseline when hosting |
| Historical momentum | 0.23 | [0.18, 0.28] | Fraction of past gains retained |
| Population (log) | 0.08 | [-0.02, 0.18] | Weak, non-significant effect |
| Regional variance | 2.4 | [1.8, 3.2] | SD of regional random effects |
```

---

## Verification Checklist

Before submitting the snippet:

- [ ] `results_summary_snippet.md` saved to `output/docs/`
- [ ] All models have summary entries
- [ ] Metrics include actual numbers (not placeholders)
- [ ] Top 5 insights have specific quantification
- [ ] Counterintuitive findings included
- [ ] Ready-to-use sentences are grammatically complete
- [ ] Tables have correct structure for LaTeX conversion
- [ ] File generated BEFORE Phase 6 begins

---

## How @writer Uses This

1. @writer reads `results_summary_snippet.md` at Phase 7C start
2. @writer expands bullet points into prose paragraphs
3. @writer uses ready-to-use sentences as paragraph starters
4. @writer copies tables directly (or uses csv_to_latex_table.py)
5. @writer does NOT need to parse raw CSVs

**Result**: Faster Phase 7C completion, no CSV parsing timeouts, consistent numbers throughout paper.
