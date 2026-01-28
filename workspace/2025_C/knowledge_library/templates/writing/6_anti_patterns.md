# Anti-Patterns to Avoid in MCM Papers

**Purpose**: Identify and prevent common mistakes in MCM competition papers.

**Reference**: `knowledge_library/academic_writing/ANTI_PATTERNS.md` (comprehensive version)

---

## Top 12 Anti-Patterns

### 1. Rubber-Stamp Quality Gates
**Pattern**: Letting phases proceed without meeting criteria.

**Why Bad**: Downstream phases fail due to inadequate inputs.

**Example**:
```
@director: "Phase 4 looks mostly complete, proceed to Phase 5."
[Reality: Model 3 implementation incomplete, missing 2 features]
```

**Fix**: Enforce gates strictly. BLOCK progression until all criteria met.

**Detection Checklist**:
- [ ] All required files exist
- [ ] Validation gate passed
- [ ] All verdicts collected
- [ ] Director approved

---

### 2. Vague Quantification
**Pattern**: Using weak quantifiers instead of specific numbers.

**Why Bad**: Loses precision, reduces credibility, fails MCM standards.

**Examples**:
- ❌ "The model performs well"
- ❌ "Significant improvement observed"
- ❌ "A large number of countries"
- ✅ "The model achieves RMSE of 3.2 medals"
- ✅ "12.3% improvement over baseline"
- ✅ "79 countries (51% of NOCs)"

**Fix**: Replace vague terms with specific metrics:
- "well" → "achieves X accuracy"
- "significant" → "X% increase (p<0.05)"
- "large" → "X units (Y% of total)"

---

### 3. Model Summarization
**Pattern**: Summarizing models instead of full mathematical formulation.

**Why Bad**: Loses technical depth, fails to demonstrate rigor.

**Example**:
```
❌ "We developed a regression model to predict outcomes."
✅ "We developed a Bayesian hierarchical model:
   \begin{equation}
   y_{i,t} \sim \text{Poisson}(\lambda_{i,t})
   \end{equation}
   where $\lambda_{i,t} = \exp(\beta_0 + \beta_1 x_{i,t})$"
```

**Fix**: Copy-Adapt-Paste protocol:
- Include ALL equations
- Define ALL parameters
- Show complete solution approach

---

### 4. Figure/Figure Orphans
**Pattern**: Placing figures far from first reference or missing captions.

**Why Bad**: Disrupts reading flow, reduces comprehension.

**Examples**:
```
❌ "As shown in Figure 3 (3 pages later)..."
❌ "\includegraphics{figure.png}" [no caption]
✅ "Figure 3 shows X (Observation), indicating Y (Implication)."
   [Figure placed immediately after this sentence]
```

**Fix**:
- Place figures at first mention using [H]
- Use descriptive captions: Observation → Implication format
- Include specific numbers in captions

---

### 5. Generic Strengths/Weaknesses
**Pattern**: Listing generic, uninformative strengths and weaknesses.

**Why Bad**: Wastes space, demonstrates shallow analysis.

**Examples**:
```
❌ Strength: "Our model is comprehensive."
❌ Weakness: "Our model has some limitations."
✅ Strength: "Hurdle model correctly captures zero-inflation,
   improving prediction accuracy for small countries by 23%."
✅ Weakness: "BSTS convergence slow for >50 countries (45 min vs 5 min),
   mitigated by using variational inference approximation."
```

**Fix**:
- Be specific: Include numbers or examples
- Be meaningful: Link to actual performance or limitations
- Be actionable: Mention mitigations for weaknesses

---

### 6. Results Repetition
**Pattern**: Repeating results in Discussion/Conclusions.

**Why Bad**: Wastes space, shows lack of synthesis.

**Example**:
```
Results: "The US will win 127.9 medals (95% PI: 77.8-178.1)."
Discussion: "As shown in Results, the US will win 127.9 medals..."
```

**Fix**: In Discussion, focus on:
- What results mean (implications)
- Why they matter (significance)
- What to do about them (recommendations)
- NOT restating the numbers

---

### 7. Weak Verbs
**Pattern**: Using weak, passive verbs instead of strong, active ones.

**Why Bad**: Reduces impact, sounds unprofessional.

**Examples**:
```
❌ "We use a regression model."
❌ "The model shows good results."
❌ "We make predictions for 2028."
✅ "We employ a Bayesian hierarchical model."
✅ "The model demonstrates 23% improvement over baseline."
✅ "We generate 2028 projections with 95% prediction intervals."
```

**Fix**: Replace weak verbs:
- "use" → "employ", "utilize", "apply"
- "show" → "demonstrate", "reveal", "indicate"
- "make" → "construct", "generate", "produce"
- "help" → "facilitate", "enable", "support"

---

### 8. Overcrowded Tables
**Pattern**: Tables with too many columns or rows.

**Why Bad**: Unreadable, violates MCM formatting standards.

**Examples**:
```
❌ Table with 12 columns, 25 rows
✅ Split into 2 tables: 6 columns, 12 rows each
```

**Fix**:
- Maximum 7-8 columns
- Maximum 15 rows
- Split into multiple tables if needed
- Use booktabs format (\toprule, \midrule, \bottomrule)

---

### 9. Missing Uncertainty
**Pattern**: Reporting point estimates without uncertainty quantification.

**Why Bad**: Overstates precision, unrealistic for stochastic systems.

**Examples**:
```
❌ "The US will win 128 medals in 2028."
✅ "The US will win 127.9 medals (95% PI: 77.8-178.1)."
✅ "China projected 83.7 medals ± 16.4 (SD)."
```

**Fix**: Always include uncertainty:
- Prediction intervals: "X (95% PI: Y-Z)"
- Standard errors: "X ± Y (SE)"
- Confidence intervals: "X (95% CI: Y-Z)"
- Standard deviation: "X ± Y (SD)"

---

### 10. Assumption Dumping
**Pattern**: Listing 10+ assumptions without prioritization or justification.

**Why Bad**: Overwhelms reader, misses critical assumptions.

**Example**:
```
❌ Assumptions:
1. Data is accurate
2. Model is correct
3. Parameters are constant
4. No external shocks
5. Linear relationship
... (15 more)

✅ Critical Assumptions:
1. Olympic performance follows hurdle structure (justified by 60+
   zero-medal countries vs 50+ medal-winning countries)
2. Host advantage diminished post-2000 (justified by regression
   analysis showing 15% → 3% effect)
```

**Fix**:
- List only critical assumptions (3-5)
- Provide justification for each
- Link to empirical evidence
- Distinguish critical from incidental

---

### 11. Figure Path Errors
**Pattern**: Incorrect relative paths for figure files.

**Why Bad**: Figures don't render in PDF.

**Example**:
```
❌ \includegraphics{figures/model_1.png}
   [When paper.tex is in output/paper/ and figures are in output/figures/]

✅ \includegraphics{../figures/model_1.png}
   [Correct relative path]
```

**Fix**:
- Use relative paths from compilation directory
- If compiling from output/paper/: use ../figures/
- Verify all figures exist before compilation

---

### 12. Narrative Over Technical
**Pattern**: Storytelling instead of technical analysis.

**Why Bad**: Unprofessional, wastes space, demonstrates wrong priorities.

**Example**:
```
❌ "Our journey began with a struggle. After many long nights and
   countless cups of coffee, we finally had an epiphany that led
   us to the treasure of a breakthrough..."

✅ "Sensitivity analysis revealed R-hat > 1.3 for β parameters,
   indicating parameter correlation. We addressed this through
   reparameterization, improving convergence efficiency by 40%."
```

**Fix**:
- Use neutral technical language
- Focus on methodological progression
- Report quantitative improvements
- Omit emotional content

---

## Anti-Pattern Detection Checklist

### Content Anti-Patterns
- [ ] No vague quantification (replace with specific numbers)
- [ ] No model summarization (include full math)
- [ ] No generic strengths/weaknesses (be specific)
- [ ] No results repetition (synthesize, don't restate)
- [ ] No missing uncertainty (always include intervals/errors)

### Presentation Anti-Patterns
- [ ] No figure orphans (place at first mention)
- [ ] No overcrowded tables (split if needed)
- [ ] No incorrect figure paths (use ../figures/)

### Writing Anti-Patterns
- [ ] No weak verbs (use strong, active verbs)
- [ ] No assumption dumping (prioritize critical ones)
- [ ] No narrative over technical (use neutral language)

---

## Reference

For comprehensive anti-patterns analysis, see:
`knowledge_library/academic_writing/ANTI_PATTERNS.md`

---

**Template Version**: 1.0
**Last Updated**: 2026-01-28
**Purpose**: Phase 7 quality control and agent prompt enhancement
