# Protocol 28: Protocol 15 - Interpretation over Description

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Protocol Number**: 15
> **Applies To**: All text-generating agents and visualizations
> **Complementary**: Protocol 14 (Academic Style Alignment)

---

## Purpose

Enforce **Observation-Implication structure** across all paper content to ensure physical interpretation, not just description.

**Core Principle**: "Every observation MUST be paired with physical implication."

**Rule**: **"Figure X shows Y" is BANNED.**

---

## Applicability

**Affected Agents**:
- @writer (primary)
- @narrative_weaver (outline generation)
- @visualizer (figure captions)
- @editor (enforcement)
- @summarizer (summary writing)

**Unaffected Agents**:
- @director (coordination only)
- @modeler (math)
- @code_translator (code)
- @validator (numerical validation)

---

## The Forbidden Pattern

### ❌ BANNED: Pure Description

```
Figure 1 shows X vs Y.
Figure 2 displays the relationship between A and B.
Our model achieves RMSE=4.2.
The graph illustrates infection over time.
```

**Problem**: These statements describe WHAT, but not WHY or SO WHAT.

**Result**: @judge_zero Persona C (Exhausted Editor) → REJECT

---

## The Required Pattern

### ✅ REQUIRED: Observation-Implication

**Template**:
```
[Observation] → [Implication]

Figure [N] demonstrates [Quantitative Result], which [Implication Verb] [Physical Mechanism].
```

**Implication Verbs**:
- indicates
- suggests
- demonstrates
- reveals
- implies
- elucidates
- underscores
- highlights

**Examples**:
```
✅ Figure 1 shows X increases with Y (p<0.001), indicating strong positive correlation.

✅ Figure 2 displays A exceeds B by 20% (t=3.4, p<0.01), suggesting主办国效应 significantly enhances performance.

✅ Our model achieves RMSE=4.2 (95% CI: [3.8, 4.6]), demonstrating high predictive accuracy.

✅ The graph illustrates infection peaks at day 47 (I_max=12,400), revealing hub-driven acceleration mechanism.
```

---

## Protocol Requirements

### Requirement 1: Figure Captions (MANDATORY)

**All figure captions MUST be conclusionary.**

**Format**:
```
Figure [N]: [Short Title]. [Observation + Implication].
```

**Examples**:

❌ **BAD**:
```latex
\begin{figure}
    \includegraphics{infection_curve.png}
    \caption{Infection over time}
\end{figure}
```

✅ **GOOD**:
```latex
\begin{figure}
    \includegraphics{infection_curve.png}
    \caption{Infection peaks at day 47 (I_max=12,400), indicating
    hub-driven acceleration mechanism (p<0.001).}
\end{figure}
```

**Validation**:
- @visualizer MUST generate conclusionary captions
- @narrative_weaver MUST check all captions in outline
- @validator MUST check captions in Phase 7.5
- @judge_zero Persona C MUST check captions in Phase 9.1

---

### Requirement 2: Results Statements (MANDATORY)

**All quantitative results MUST include interpretation.**

**Template**:
```
Our model achieves [Metric] = [Value] ([Uncertainty]), [Implication Verb] [Physical Meaning].
```

**Examples**:

❌ **BAD**:
```latex
Our model achieves RMSE=4.2 and R²=0.89.
```

✅ **GOOD**:
```latex
Our model achieves RMSE=4.2 (95\% CI: [3.8, 4.6]) and R²=0.89 (p<0.001),
demonstrating high predictive accuracy and strong fit to epidemic dynamics.
```

---

### Requirement 3: Abstract Rules (MANDATORY)

**Abstract MUST contain ≥3 quantitative metrics, each with interpretation.**

**Template**:
```
We propose [Model Name], which [Mechanism]. Our model achieves
[Metric 1] ([Interpretation]), [Metric 2] ([Interpretation]),
and [Metric 3] ([Interpretation]), demonstrating [Overall Contribution].
```

**Example**:

❌ **BAD**:
```
We propose SIR-Network model for epidemic prediction. Our model performs
well on test data and provides insights into transmission dynamics.
```

✅ **GOOD**:
```
We propose SIR-Network model, which captures hub-driven transmission dynamics.
Our model achieves RMSE=4.2 (↓27% vs baseline, p<0.001), R²=0.89 (95\% CI: [0.85, 0.93]),
and correctly predicts peak infection day (error: ±1.2 days), demonstrating
the critical importance of network topology in epidemic forecasting.
```

---

## Implementation in Agent Prompts

### @writer Prompt Template

```markdown
# Agent: @writer

## Protocol 15: Interpretation over Description (CRITICAL)

**RULE**: Every observation MUST be paired with physical implication.

### ❌ FORBIDDEN Patterns
- "Figure X shows Y"
- "Our model achieves Z"
- "The graph displays A vs B"

### ✅ REQUIRED Patterns
- "Figure X demonstrates Y, which indicates Z"
- "Our model achieves Z (p<0.001), demonstrating W"
- "The graph illustrates A exceeds B by 20% (p<0.01), suggesting C"

### Quality Checklist
Before outputting each paragraph, verify:
- [ ] Does this statement describe WHAT happened?
- [ ] Does this statement explain WHY it matters?
- [ ] Does this statement include physical implication?
- [ ] Does this statement use "indicating", "suggests", or "demonstrates"?

If any check fails, REVISE before output.
```

---

### @visualizer Prompt Template

```markdown
# Agent: @visualizer

## Protocol 15: Figure Caption Enforcement (MANDATORY)

**RULE**: All figure captions MUST be conclusionary.

### Caption Template
```
Figure [N]: [Descriptive Title]. [Quantitative Observation],
which [indicates/suggests/demonstrates] [Physical Mechanism].
```

### Examples

❌ **BAD**: "Figure 1: Infection over time"
✅ **GOOD**: "Figure 1: Infection curve. Infection peaks at day 47
(I_max=12,400), indicating hub-driven acceleration (p<0.001)."

❌ **BAD**: "Figure 2: Model comparison"
✅ **GOOD**: "Figure 2: Model performance. SIR-Network reduces RMSE
by 27% compared to baseline (p<0.001), demonstrating superiority of
topology-aware modeling."

### Validation
For every figure generated, verify:
- [ ] Caption contains quantitative observation?
- [ ] Caption contains implication verb?
- [ ] Caption explains physical meaning?
- [ ] Caption includes uncertainty (if applicable)?
```

---

### @narrative_weaver Prompt Template

```markdown
# Agent: @narrative_weaver

## Protocol 15: Narrative Structure Enforcement

**RULE**: Enforce Observation-Implication structure in paper outline.

### For Every Planned Figure

Check:
- [ ] Planned caption contains quantitative observation?
- [ ] Planned caption contains physical implication?
- [ ] Caption uses "indicating", "suggests", or "demonstrates"?

**If any check fails**, REJECT outline and ask @visualizer to revise.

### For Every Results Section

Check:
- [ ] Results paragraphs interpret findings?
- [ ] Not just listing numbers, but explaining meaning?
- [ ] Connects to physical mechanisms?

**If any check fails**, add interpretation requirements to outline.
```

---

## Enforcement Mechanisms

### 1. Phase 7.5: LaTeX Compilation Gate

**@validator** checks:
- All figure captions are conclusionary
- Results statements include interpretation
- Abstract contains ≥3 metrics with interpretation

**Failure**: @validator REJECT → @writer must revise

---

### 2. Phase 9.1: Mock Judging

**@judge_zero (Persona C)** checks:
- Figure captions non-descriptive → WARN (-10 points each)
- Abstract空洞 (no interpretation) → REJECT (-20 to -30 points)
- Generic results statements → WARN (-10 points)

**Result**: Low score → DEFCON 1 → Fix

---

### 3. Phase 11: Automated Scoring

**`mmbench_score.py`** checks:
```
Figure caption analysis:
- Contains numbers? (+2 points)
- Contains conclusionary verb? (+3 points)
- Contains physical implication? (+1 point)
```

**Non-descriptive captions**: Automatic score deduction

---

## Quality Assurance

### Verification Checklist

**After any text generation**, verify:

- [ ] No "Figure X shows Y" patterns
- [ ] No "Our model achieves Z" without interpretation
- [ ] All figure captions conclusionary
- [ ] All results statements interpreted
- [ ] Abstract contains ≥3 metrics with interpretation
- [ ] Observation-Implication structure used throughout

### Test Case

**Input**: @writer generates results section

**Verification**:
```
1. Scan for "shows", "displays", "illustrates" without "indicating"
2. Check figure captions for conclusionary content
3. Check results statements for interpretation
4. If any fail → REJECT and require revision
```

---

## Examples

### Example 1: Figure Caption Evolution

**Draft 1 (BAD)**:
```
Figure 1: Infection curve
```

**Draft 2 (Better, but still BAD)**:
```
Figure 1: Infection curve. The infection peaks at day 47.
```

**Draft 3 (GOOD)**:
```
Figure 1: Infection curve. Infection peaks at day 47 (I_max=12,400),
indicating hub-driven acceleration mechanism.
```

**Draft 4 (BEST - with uncertainty)**:
```
Figure 1: Infection curve. Infection peaks at day 47 (I_max=12,400,
95% CI: [11,800, 13,000]), indicating hub-driven acceleration mechanism
(p<0.001).
```

---

### Example 2: Results Statement Evolution

**Draft 1 (BAD)**:
```
Our SIR-Network model achieves RMSE=4.2 and R²=0.89.
```

**Draft 2 (Better, but still BAD)**:
```
Our SIR-Network model achieves RMSE=4.2 and R²=0.89, which is good.
```

**Draft 3 (GOOD)**:
```
Our SIR-Network model achieves RMSE=4.2 (95% CI: [3.8, 4.6]) and R²=0.89
(p<0.001), demonstrating high predictive accuracy.
```

**Draft 4 (BEST - with physical meaning)**:
```
Our SIR-Network model achieves RMSE=4.2 (95% CI: [3.8, 4.6]), representing
a 27% reduction vs baseline (p<0.001), and R²=0.89, demonstrating that
capturing network topology significantly improves epidemic forecasting.
```

---

### Example 3: Abstract Evolution

**Draft 1 (BAD)**:
```
We propose a SIR-Network model for epidemic prediction on airline networks.
Our model performs well on test data and provides insights into transmission
dynamics.
```

**Draft 2 (Better, but still BAD)**:
```
We propose a SIR-Network model for epidemic prediction on airline networks.
Our model achieves RMSE=4.2 and correctly predicts peak infection day.
```

**Draft 3 (GOOD)**:
```
We propose SIR-Network model for epidemic prediction on airline networks,
which captures hub-driven transmission dynamics. Our model achieves RMSE=4.2
(95% CI: [3.8, 4.6]) and correctly predicts peak infection day with ±1.2 days
error, demonstrating the importance of network topology in epidemic forecasting.
```

**Draft 4 (BEST - full interpretation)**:
```
We propose SIR-Network model for epidemic prediction on airline networks,
which captures multi-scale hub-driven transmission dynamics. Our model achieves
RMSE=4.2 (95% CI: [3.8, 4.6], ↓27% vs baseline, p<0.001), R²=0.89, and
correctly predicts peak infection day (error: ±1.2 days), demonstrating that
topology-aware modeling significantly outperforms homogeneous-mixing approaches
and reveals critical insights into hub-mediated epidemic acceleration.
```

---

## Impact

**Without Protocol 15**:
- Generic, descriptive papers
- "Figure X shows Y" pattern throughout
- @judge_zero Persona C rejections
- No O-Prize competitiveness

**With Protocol 15**:
- Insightful, interpretive papers
- Every observation paired with implication
- Physical understanding demonstrated
- O-Prize-level competitiveness

**Value**: **Transforms "descriptive" papers into "interpretive" papers.**

---

## Complementary Protocols

### Protocol 14: Academic Style Alignment

- **Protocol 14**: Vocabulary constraints (show → demonstrate)
- **Protocol 15**: Structure constraints (description → interpretation)

**Together**: Ensure both word choice AND sentence structure are academic

### Protocol 13: Mock Court Rewind

- **Protocol 13**: Triggers DEFCON 1 if paper rejected
- **Protocol 15**: Prevents Persona C (Editor) rejections via good structure

---

## Dependencies

**Required**:
- Protocol 14 (Academic Style Alignment)
- @validator (Phase 7.5)
- @judge_zero (Phase 9.1)
- mmbench_score.py (Phase 11)

**Agents Enforced**:
- @writer, @narrative_weaver, @visualizer, @editor, @summarizer

**Validation**:
- @validator (Phase 7.5)
- @judge_zero Persona C (Phase 9.1)
- mmbench_score.py (Phase 11)

---

## Related Protocols

- **Protocol 14**: Academic Style Alignment (complementary)
- **Protocol 13**: Mock Court Rewind (enforces via rejection)
- **Protocol 23**: Phase 5.8 Insight Extraction (generates implications)

---

**Document Version**: v3.1.0
**Protocol Type**: Quality Enforcement
**Severity**: HIGH (LINT ERROR on violation)
**Status**: Ready for Implementation
