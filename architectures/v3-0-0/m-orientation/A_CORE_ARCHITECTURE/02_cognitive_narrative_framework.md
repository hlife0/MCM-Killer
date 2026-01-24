# Cognitive Narrative Framework

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Purpose**: Define the "o1-style" thinking narrative framework for MCM-Killer

---

## Core Concept: Narrative as Computation

### The Problem with v3.0.0

Current papers are "flat" - they describe what was done, but not how thinking evolved.

**Example v3.0.0**:
```
We used a Bayesian hierarchical model to predict Olympic medals.
The model achieved RMSE = 4.2.
```

This is correct but lacks depth. It doesn't show the research process.

### The v3.1.0 Solution

Transform "struggles and errors" into "research insights" through cognitive narrative.

**Example v3.1.0**:
```
We initially constructed a global hierarchical model (Model 1-A), but
encountered severe R-hat divergence (R-hat > 1.3, Figure 2a). This
divergence revealed fundamental data heterogeneity across regions, violating
the global pooling assumption. We refined the model with region-specific
partial pooling (Model 1-B), which both resolved convergence (R-hat < 1.05,
Figure 2b) and improved RMSE from 5.8 to 4.2.

This evolution demonstrates that 主办国效应 operates differently across
cultural/economic regions, suggesting that region-tailored policies are
more appropriate than global prescriptions (see Sensitivity Analysis, Section 4.2).
```

This shows:
1. **Initial approach** (Model 1-A)
2. **Specific struggle** (R-hat divergence)
3. **Physical insight** (Regional heterogeneity)
4. **Solution** (Model 1-B)
5. **Research value** (Policy implication)

---

## The Hero's Journey for Science

### Template Structure

Every model in the paper should follow this narrative arc:

#### 1. The Call (Initial Approach)
```
"We begin with [simple/basic method X], motivated by [theoretical reason Y]."
```

#### 2. The Ordeal (Encountered Struggle)
```
"However, training revealed [specific technical issue Z]."
"[Show data/figure demonstrating the issue]."
```

#### 3. The Revelation (Insight)
```
"Analysis of this struggle revealed [physical meaning W]."
"[Explain why this matters physically/economically]."
```

#### 4. The Resolution (Refined Approach)
```
"Informed by this insight, we refined the model to [improved approach]."
```

#### 5. The Treasure (Result + Meaning)
```
"The refined model achieves [metric improvement], AND demonstrates
[deeper understanding of underlying phenomenon]."
```

---

## Observation-Implication Protocol

### Definition

Every result description must follow this pattern:

**Observation**: What does the data/show?

**Implication**: What does this mean physically/economically/sociologically?

### Examples

**BAD (Isolated Description)**:
```
Figure 1 shows model predictions match actual values well.
```

**GOOD (Observation-Implication)**:
```
Figure 1 shows model predictions closely match actual values (Observation),
with RMSE = 4.2 (↓15% from baseline), indicating the model successfully
captures the non-linear主办国效应without overfitting to short-term fluctuations
(Implication).
```

**Application Points**:
- Figure captions
- Table analysis
- Result descriptions
- Discussion section

---

## Transforming Struggles into Insights

### Mapping Technical → Physical

| Technical Issue | Physical Meaning | Research Value |
|-----------------|------------------|----------------|
| **R-hat divergence** | Data heterogeneity | Reveals sub-populations |
| **Gradient explosion** | Scale mismatch | Reveals multiplicative relationships |
| **Slow convergence** | Weak identifiability | Suggests over-parameterization |
| **Loss oscillation** | Data non-stationarity | Requires time-varying models |
| **Numerical instability** | Model boundary violation | Model assumptions violated |

### Implementation: Phase 5.8

**Input Sources**:
1. `training_full.log` - Complete training record
2. `dev_diary_{i}.md` - Implementation struggles
3. Phase 1 consultation feedback - Original design intent

**Analysis Framework**:
```
1. Detect Pattern (What went wrong?)
2. Interpret Physically (Why did it matter?)
3. Evolve Model (How did we fix it?)
4. Extract Insight (What did we learn?)
```

---

## The "Struggle" Taxonomy

### Category 1: Data-Model Mismatch

**Symptoms**:
- R-hat divergence
- Slow convergence
- Numerical instability

**Physical Meaning**:
- Model assumptions violated
- Data structure differs from assumption
- Hidden heterogeneity exists

**Narrative Treatment**:
```
"The convergence struggles were not computational artifacts but revealed
fundamental data structure. This insight led us to [refined model]."
```

### Category 2: Scale Sensitivity

**Symptoms**:
- Gradient explosion/vanishing
- Poor conditioning
- Numerical overflow

**Physical Meaning**:
- Wrong scale relationship (log vs linear)
- Missing interactions
- Wrong functional form

**Narrative Treatment**:
```
"Gradient sensitivity revealed that variables interact multiplicatively
(log-transformed), not additively. This fundamentally changed our
understanding of [economic mechanism]."
```

### Category 3: Boundary Violation

**Symptoms**:
- Predictions outside valid range
- Probability violations
- Impossible values

**Physical Meaning**:
- Model extrapolation beyond data support
- Constraint violation
- Physical boundary crossed

**Narrative Treatment**:
```
"The model generated negative predictions for early years, revealing
extrapolation risk beyond data support. We constrained predictions to
physically plausible range (≥0), acknowledging model limitations."
```

---

## Writing Style: o1-Inspired Narrative

### Characteristics

1. **Explicit Reasoning**: "We chose X because Y, not just "We used X."
2. **Process Transparency**: Show abandoned approaches, not just final
3. **Struggle Integration**: Errors become insights
4. **Quantitative Rigor**: Every claim supported by data

### Template: Model Section

```latex
\section{Model Building}

\subsection{Initial Approach and Limitations}
We began with Model 1-A, a [description], assuming [assumption].
This approach seemed promising because [reason], but training revealed
[struggle].

\subsection{Insight and Evolution}
The convergence struggles (Figure~\ref{fig:convergence}) revealed
[physical meaning]. This led us to recognize that [deeper understanding].

\subsection{Final Model}
Informed by this insight, we refined Model 1-A to Model 1-B by
[specific change]. The refined model achieved [improvement],
AND demonstrated [deeper understanding].
```

---

## Integration with Existing Phases

### Phase 4: Code Translation

**@code_translator** enhancement:
```
Create dev_diary_{i}.md alongside code.

For every non-trivial implementation choice or error:
- Document the struggle
- Explain the solution
- Note the research value
```

### Phase 5B: Full Training

**@model_trainer** watch mode enhancement:
```
Monitor not just for errors, but for "interesting struggles":
- Loss oscillations → Document pattern
- Long convergence → Document why
- Parameter sensitivity → Document ranges
```

### Phase 7: Paper Writing

**@writer** + @narrative_weaver collaboration:
```
1. @narrative_weaver reads narrative_arc_{i}.md
2. @narrative_weaver generates paragraph outline
3. @writer fleshes out outline with LaTeX
4. Both ensure Observation-Implication structure
```

---

## Quality Assurance

### Checkpoint: Narrative Depth

**Question**: Does the paper show "thought process"?

**Indicators**:
- [ ] Abandoned approaches mentioned
- [ ] Specific struggles documented
- [ ] Physical insights extracted
- [ ] Evolution narrative present

**Anti-Pattern**: "We tried X, it worked, so we used it."

### Checkpoint: Insight Density

**Question**: Are there insights per model?

**Indicators**:
- [ ] "Model Limitations" section present
- [ ] Sensitivity analysis discusses physical meaning
- [ ] Struggles connected to deeper understanding

**Anti-Pattern**: All models work perfectly on first try.

---

## Summary

The v3.1.0 Cognitive Narrative Framework transforms papers from "reports of results" into "stories of discovery." By documenting struggles, extracting insights, and weaving narratives, the system produces papers that demonstrate:

1. **Deep thinking** (o1-style)
2. **Research process** (not just final answer)
3. **Physical understanding** (not just math)
4. **O-Prize competitiveness** (thoughtful analysis)

This is the key differentiator from v3.0.0 and the path to O-Prize success.
