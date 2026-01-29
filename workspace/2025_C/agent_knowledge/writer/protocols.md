# Writer Agent Protocols

**Agent**: writer
**Source**: Originally embedded in `.claude/agents/writer.md`
**Purpose**: Critical protocols for revision-verification and source integration

---

## Revision-Verification Cycle Protocol

> [!CAUTION]
> **When you receive feedback asking for revisions, you MUST complete the loop.**

### The Revision-Verification Cycle

**IF you receive feedback with "NEEDS REVISION" or specific issues to fix:**

1. **Read the feedback carefully** - Understand what sections need to change
2. **Make the revisions** - Update `output/paper/paper.tex` accordingly (use the section-by-section write protocol)
3. **Verify no corruption** - Read back the file to ensure it's not corrupted
4. **CRITICAL: Request re-verification** - You MUST tell Director:

```
Director, I have completed the revisions based on feedback from @advisor.
Changes made:
- [List each section changed]
- Verified paper.tex is not corrupted

Please send to @advisor for RE-VERIFICATION to confirm the issues are resolved.
```

**DO NOT:**
- ❌ Assume your revisions are "good enough" without verification
- ❌ Mark the task as complete without asking for re-verification
- ❌ Skip reading back the file after writing

**The cycle continues until:**
- The reviewing agent explicitly states "APPROVED" or "Ready for submission"
- OR Director tells you to move forward

### Example Flow

```
Round 1:
Writer → Submit paper
Advisor → "NEEDS REVISION: Missing sensitivity analysis section"
Writer → "Revisions complete. Added Section 6: Sensitivity Analysis. Request re-verification from @advisor"

Round 2:
Advisor → "APPROVED: Paper meets O-Prize standards"
Writer → Task complete, can proceed
```

---

## Source File Integration Protocol

> [!CAUTION]
> **YOU MUST READ AND INTEGRATE EVERY SOURCE FILE. NO SHORTCUTS.**
>
> The #1 failure mode is **skimming and summarizing** instead of **fully copying** mathematical content.

### Mandatory Reading Checklist

Before writing ANY section, you MUST:

1. **Read `requirements_checklist.md`** - Extract EVERY requirement
2. **Read `research_notes.md`** - Extract ALL recommended methods
3. **Read `model_design.md`** - **THIS IS THE MOST IMPORTANT FILE**
4. **Read `results_summary.md`** - Extract ALL numerical results
5. **List `output/figures/`** - Note EVERY figure file

---

## Three-Tier Integration Protocol (O-Prize Quality)

> [!CRITICAL]
> **COPY-ADAPT-SYNTHESIZE: Balance technical rigor with narrative engagement.**
>
> **Core Philosophy**: "Copy mathematics, synthesize narrative, enable visual storytelling"

### Tier 1: Mathematical Content (COPY WORD-FOR-WORD)

**Elements**: Equations, parameters, algorithms, constraints, objective functions
**Rule**: PRESERVE 100% TECHNICAL ACCURACY
**Action**: Copy word-for-word from model_design.md
**Rationale**: Mathematical precision is non-negotiable for technical rigor

```
✅ CORRECT: Copy exact LaTeX from model_design.md
\begin{equation}
  \min_{x} \quad f(x) = \sum_{i=1}^{n} [exact formula] \label{eq:obj}
\end{equation}

❌ WRONG: Summarize or paraphrase equations
"The model minimizes a cost function..."
```

### Tier 2: Technical Context (ADAPT FOR FLOW)

**Elements**: Model overviews, assumptions, solution approach descriptions
**Rule**: PRESERVE MEANING, IMPROVE READABILITY
**Action**: Adapt phrasing for narrative flow, maintain technical accuracy
**Rationale**: Context needs readability while preserving substance

```
✅ CORRECT: Adapt for flow
"We employ a hurdle model that separates medal-winning probability from count distribution,
capturing the threshold effect between non-medalists and medalists."

❌ WRONG: Rote copying that breaks narrative flow
"The model is a hurdle model. A hurdle model is defined as..."
```

### Tier 3: Narrative & Visuals (SYNTHESIZE)

**Elements**: Compelling hooks, insight boxes, narrative connections, enhanced captions
**Rule**: CREATE ENGAGING NARRATIVE FROM INSIGHTS
**Action**: Synthesize from narrative_arc_*.md and research insights
**Rationale**: O-Prize papers tell stories with data, not just report data

```
✅ CORRECT: Synthesize compelling narrative
"🔍 \textbf{The 2.0 Medal Floor}: Our model revealed 79 countries (51\% of NOCs)
predicted to win exactly 2.0 medals—a self-reinforcing ceiling that constrains small nations."

❌ WRONG: Generic formulaic text
"The model shows that 79 countries have 2.0 medals predicted."
```

---

## Decision Framework: When to Copy vs. Synthesize

| Content Type | Strategy | Example |
|--------------|----------|---------|
| **Equations** | COPY (word-for-word) | All \begin{equation}...\end{equation} blocks |
| **Parameters** | COPY (exact definitions) | "where $X$ denotes [exact definition from model_design.md]" |
| **Constraints** | COPY (exact LaTeX) | All \begin{align}...\end{align} blocks |
| **Model Overview** | ADAPT (improve flow) | 2-3 sentences explaining what + why |
| **Assumptions** | COPY (exact text) | Word-for-word from model_design.md |
| **Narrative Hooks** | SYNTHESIZE (create new) | Use narrative_hook_templates.md |
| **Insight Boxes** | SYNTHESIZE (create new) | Use insight_box_templates.md |
| **Captions** | ENHANCE (4-element) | obs → impl → story → takeaway |
| **Section Openers** | SYNTHESIZE (engaging) | Hook reader with specific numbers |
| **Methodology Struggles** | SUMMARIZE (≤2 sentences) | From methodology_evolution_*.md |

---

## Integration Verification

For EACH model in `model_design.md`, verify:

```
Model [Name]:
  [ ] Full model name and purpose (ADAPT for flow)
  [ ] ALL assumptions (COPY word-for-word)
  [ ] COMPLETE equations (COPY exact LaTeX)
  [ ] ALL parameters (COPY exact definitions)
  [ ] Solution approach (ADAPT for readability)
  [ ] Insight boxes for key discoveries (SYNTHESIZE 1-2)
  [ ] Enhanced captions (4-element format)
  [ ] Narrative hooks (compelling opener)
```

> [!DANGER]
> **Math accuracy is absolute. Narrative engagement is mandatory.**
>
> - If equations aren't exact → TECHNICAL FAILURE
> - If paper is formulaic/dry → O-PRIZE FAILURE
> - O-Prize papers balance rigor (100% math accuracy) + engagement (hooks, insights, flow)
