# Writing Enhancement Protocol (V2.0)

> **"Writing Enhancement" Protocol**
> This system enforces professional academic writing standards to prevent template errors, loose formatting, and lack of pseudo-code.

---

## Overview

The Writing Enhancement Protocol addresses three key pain points:
1. **Template errors** - wrong document class, missing packages
2. **Loose formatting** - excessive bullets, low prose density
3. **Timeout prevention** - pre-generated summaries, increased time budgets

---

## 1. Template Correction (@writer)

### Hardcoded Document Class

```latex
\documentclass{mcmthesis}
```

| DO | DON'T |
|----|-------|
| `\documentclass{mcmthesis}` | `\documentclass{article}` |
| Use MCM template class | `\documentclass[10pt]{article}` |

### Required Package Preload

Add these to your preamble at Phase 7A start:

```latex
% Algorithm support (MANDATORY - V2.0)
\usepackage{algorithm}
\usepackage{algorithmic}

% Alternative: algorithmicx with algpseudocode
% \usepackage{algorithm}
% \usepackage{algpseudocode}
```

### Verification Checklist

- [ ] Document class is `mcmthesis` (not `article`)
- [ ] `algorithm` package is loaded
- [ ] `algorithmic` or `algpseudocode` package is loaded
- [ ] `mcmthesis.cls` copied to `output/paper/`

---

## 2. Dense Academic Style (@writer)

### Anti-List-Abuse Rules

| Section | Max Bullets Allowed | Prose Requirement |
|---------|---------------------|-------------------|
| Results | 5 per subsection | Each bullet must be preceded/followed by explanatory paragraph |
| Discussion | 3 per subsection | Prefer prose paragraphs over lists |
| Conclusions | 6 total | Final takeaways only, not findings |
| Model Sections | 0 | NO bullets in model descriptions |

### Information Density Guidelines

1. **Reduce Paragraph Breaks**: Consolidate related sentences
   - BAD: New paragraph for each point
   - GOOD: Group related findings in flowing paragraphs

2. **Remove Unnecessary Spacing**:
   ```latex
   % REMOVE these from your LaTeX (unless strictly required):
   \setlength{\parindent}{0pt}
   \vspace{1cm}
   ```

3. **Minimum Paragraph Density**:
   - Each paragraph: 4-6 sentences minimum
   - Each page: 70% text, 30% figures/tables/equations

### Example: Bad vs Good Writing

**BAD (bullet-heavy)**:
```latex
\subsection{Results}
Key findings:
\begin{itemize}
\item GDP correlates with medals (r=0.72)
\item Population matters less (r=0.45)
\item Host countries gain 12 extra medals
\item Historical performance predicts future
\item Climate affects winter sports
\end{itemize}
```

**GOOD (prose-heavy)**:
```latex
\subsection{Results}
Our analysis reveals several significant predictors of Olympic success.
Economic factors play the dominant role, with GDP showing a strong
correlation with medal counts (r=0.72, p<0.001). This relationship
persists across all Olympic cycles, suggesting that sustained
investment in athletic infrastructure is crucial. In contrast,
population size exhibits a weaker association (r=0.45), indicating
that demographic advantage alone is insufficient without corresponding
resource allocation. Host nations demonstrate a substantial home
advantage, gaining an average of 12.3 additional medals compared to
their non-hosting baseline.
```

---

## 3. Pseudo-code Requirement

### When Required

Pseudo-code is MANDATORY for:
- Mechanism design models (game theory, auction design)
- Iterative optimization algorithms
- Multi-step decision processes
- Any algorithm with conditional branching

### Template

```latex
\begin{algorithm}
\caption{Algorithm Name}
\begin{algorithmic}[1]
\REQUIRE Input parameters
\ENSURE Output description
\STATE Initialize variables
\FOR{each iteration}
    \IF{condition}
        \STATE Action A
    \ELSE
        \STATE Action B
    \ENDIF
\ENDFOR
\RETURN Result
\end{algorithmic}
\end{algorithm}
```

### Example: Medal Allocation Mechanism

```latex
\begin{algorithm}
\caption{Bayesian Medal Prediction with Uncertainty Quantification}
\begin{algorithmic}[1]
\REQUIRE Historical data $\mathcal{D}$, prior distributions $\pi(\theta)$
\ENSURE Predicted medal counts with 95\% credible intervals
\STATE Initialize MCMC chains with random starting points
\FOR{$t = 1$ to $T$ iterations}
    \FOR{each parameter $\theta_i$}
        \STATE Propose $\theta_i^* \sim q(\theta_i^* | \theta_i^{(t-1)})$
        \STATE Compute acceptance ratio $\alpha = \min(1, \frac{p(\theta_i^* | \mathcal{D})}{p(\theta_i^{(t-1)} | \mathcal{D})})$
        \IF{$u < \alpha$ where $u \sim \text{Uniform}(0,1)$}
            \STATE Accept: $\theta_i^{(t)} \gets \theta_i^*$
        \ELSE
            \STATE Reject: $\theta_i^{(t)} \gets \theta_i^{(t-1)}$
        \ENDIF
    \ENDFOR
\ENDFOR
\STATE Discard burn-in samples
\RETURN Posterior samples for prediction and uncertainty quantification
\end{algorithmic}
\end{algorithm}
```

---

## 4. Pre-Generated Summary (@metacognition_agent)

### Purpose

Prevent @writer timeouts from parsing raw CSVs by pre-generating structured summaries.

### Output File

`output/docs/results_summary_snippet.md`

### Timing

Generate at end of Phase 5.8, before Phase 6.

### Template

```markdown
# Results Summary Snippet (for @writer)

## Quick Stats (copy-paste ready)
- Total countries analyzed: {N}
- Time period: {start_year} - {end_year}
- Key metric range: {min} - {max} ({unit})

## Model-by-Model Summary

### Model 1: {Name}
**Key Finding**: {One sentence with number}
**Performance**: R² = {value}, RMSE = {value}
**Notable**: {Surprising or important observation}

### Model 2: {Name}
**Key Finding**: {One sentence with number}
**Performance**: {Metric} = {value}
**Notable**: {Observation}

[... repeat for all models ...]

## Top 5 Insights (for Results section)
1. {Insight with specific number}
2. {Insight with specific number}
3. {Insight with specific number}
4. {Insight with specific number}
5. {Insight with specific number}

## Counterintuitive Findings (for Discussion)
- {Finding that challenges expectations}
- {Finding that challenges expectations}

## Ready-to-Use Sentences
- "Our analysis reveals that {X} accounts for {Y%} of variance..."
- "Surprisingly, {factor} showed {direction} relationship with {outcome}..."
- "The model predicts {X} with {confidence interval}..."
```

### Example Output

```markdown
# Results Summary Snippet (for @writer)

## Quick Stats (copy-paste ready)
- Total countries analyzed: 234
- Time period: 1896 - 2024
- Key metric range: 0 - 473 (total medals per country per Olympics)

## Model-by-Model Summary

### Model 1: Bayesian Hierarchical Model
**Key Finding**: GDP explains 68.3% of variance in medal counts
**Performance**: R² = 0.683, RMSE = 4.2 medals
**Notable**: Effect sizes vary by 3x between developed and developing nations

### Model 2: Host Effect Model
**Key Finding**: Host nations gain 12.3 additional medals on average
**Performance**: Effect size = 12.3 (95% CI: 8.7, 15.9)
**Notable**: Effect persists for 2 Olympics after hosting

## Top 5 Insights (for Results section)
1. GDP per capita shows stronger predictive power (r=0.72) than total GDP (r=0.61)
2. Host advantage is 40% larger for smaller nations
3. Winter sports show higher regional concentration (Gini=0.89) than summer (Gini=0.67)
4. Historical momentum explains 23% of incremental medal gains
5. Climate-sport matching improves predictions by 8.3%

## Counterintuitive Findings (for Discussion)
- Population size has negative partial correlation with medals per capita
- Wealthier nations show diminishing returns above $50K GDP/capita

## Ready-to-Use Sentences
- "Our analysis reveals that GDP per capita accounts for 68.3% of variance in medal counts..."
- "Surprisingly, population showed a negative relationship with medals per capita after controlling for wealth..."
- "The model predicts 2028 LA Olympics medal distributions with 95% CI width averaging 4.2 medals..."
```

---

## 5. Time Allocation

### Updated Phase 7 Minimums

| Phase | Old MIN | New MIN | Change |
|-------|---------|---------|--------|
| 7C | 35m | **45m** | +30% |
| 7E | 25m | **32m** | +30% |

### Updated Phase 7 Sub-Phases

```
7A (Framework 10-15m) → 7B (Models 30-40m) → 7C (Results 20-25m) → 7D (Analysis 10-15m) → 7E (Conclusions 12-18m) → 7F (Compile 5-10m)
```

### Rationale

- **7C (Results)**: More time needed for thorough results writing with proper prose density
- **7E (Conclusions)**: More time needed for complete conclusions addressing all requirements

---

## Chain of Accountability

```
@metacognition_agent (Phase 5.8)
    ↓ generates
results_summary_snippet.md
    ↓ consumed by
@writer (Phase 7A)
    ↓ uses
Correct template (mcmthesis + algorithm packages)
    ↓ produces
Dense prose with pseudo-code
    ↓ validated by
@editor (Page count + formatting check)
```

---

## Verification Checklist

### Template Correction
- [ ] Document class is `mcmthesis`
- [ ] `algorithm` package loaded
- [ ] `algorithmic` or `algpseudocode` loaded
- [ ] `mcmthesis.cls` in `output/paper/`

### Dense Academic Writing
- [ ] Results section has ≤5 bullets per subsection
- [ ] Discussion section uses prose paragraphs
- [ ] No `\setlength{\parindent}{0pt}` unless justified
- [ ] Each paragraph has 4+ sentences

### Pseudo-code
- [ ] Mechanism Design model includes pseudo-code block
- [ ] Algorithm environment used correctly
- [ ] Line numbers enabled (`[1]`)

### Pre-Generated Summary
- [ ] `results_summary_snippet.md` exists before Phase 7
- [ ] Contains model-by-model summary with metrics
- [ ] Contains Top 5 Insights with specific numbers
- [ ] Contains ready-to-use sentences

### Time Allocation
- [ ] Phase 7C minimum is 45m
- [ ] Phase 7E minimum is 32m

---

## Common Issues and Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| "Undefined control sequence \REQUIRE" | Missing algorithm package | Add `\usepackage{algorithmic}` |
| "Too many bullets in Results" | List-heavy writing | Convert bullets to prose paragraphs |
| "@writer timeout parsing CSVs" | No pre-generated summary | Ensure @metacognition generates snippet |
| "Sparse pages" | Low prose density | Add context sentences, increase paragraph length |
| "Wrong document class" | Started with article | Replace with `\documentclass{mcmthesis}` |

---

## Notes

- The Writing Enhancement Protocol is **mandatory** for all Phase 7 work
- Dense prose is preferred over structured lists for academic credibility
- Pseudo-code demonstrates algorithmic depth to judges
- Pre-generated summaries prevent redundant work and timeouts
- Time increases ensure quality without rushing
