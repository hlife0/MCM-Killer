# Protocol 27: Academic Style Alignment (Protocol 14)

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Protocol Number**: 14
> **Applies To**: All text-generating agents

---

## Purpose

Enforce **Academic Style Guide** (`style_guide.md`) across all paper generation to ensure O-Prize-level writing quality.

**Core Principle**: Violating style_guide.md is equivalent to syntax error.

---

## Applicability

**Affected Agents**:
- @writer (primary)
- @narrative_weaver (outline generation)
- @editor (final polish)
- @summarizer (summary writing)

**Unaffected Agents**:
- @director (coordination only)
- @modeler (math)
- @code_translator (code)
- @visualizer (figures)
- @model_trainer (training)

---

## Protocol Requirements

### Requirement 1: Mandatory Style Guide Loading

**All text-generating agents MUST**:

1. **Load** `knowledge_library/academic_writing/style_guide.md` as System Context
2. **Read** the style guide before generating any text
3. **Follow** all rules in style guide

**Failure**: LINT ERROR (treat as syntax error)

---

### Requirement 2: Vocabulary Constraints

**Banned Words** → **Recommended Replacements**:

| Banned | Recommended | Rationale |
|---------|-------------|-----------|
| show | demonstrate, illustrate | 1200% more academic |
| get | obtain, achieve | More precise |
| say | state, posit | More formal |
| look at | examine, investigate | More academic |
| put | place, situate | Context-dependent |

---

### Requirement 3: Abstract Rules

**Critical Rule**: Abstract MUST contain ≥3 quantitative metrics.

**Examples**:
- ❌ "Our model performs well."
- ✅ "Our model achieves RMSE=4.2 (↓27%), R²=0.89 (p<0.001)."

**Validation**:
- @validator checks in Phase 7.5
- @judge_zero (Persona C) checks in Phase 9.1
- Missing numbers → REJECT

---

### Requirement 4: Sentence Templates

**Use Observation-Implication structure**:

❌ **BAD** (Isolated description):
> "Figure 1 shows X vs Y."

✅ **GOOD** (Observation-Implication):
> "Figure 1 shows X increases with Y (Observation),
> indicating strong positive correlation (Implication)."

**Templates from style_guide.md**:
- "Figure [N] demonstrates [Result], which implies [Mechanism]."
- "While initial model [Action], refined model [Action], resulting in [Outcome]."

---

## Implementation in Agent Prompts

### @writer Prompt Template

```markdown
# Agent: @writer

## System Context (CRITICAL - DO NOT MODIFY)
You MUST read and follow: knowledge_library/academic_writing/style_guide.md

This document contains:
- Required vocabulary (e.g., "elucidate", "demonstrate", "quantify")
- Banned words (e.g., "show", "get", "say")
- Sentence templates (e.g., "Figure X demonstrates Y, implying Z")
- Structural rules (e.g., Abstract must contain ≥3 numbers)

**Violating style_guide.md is equivalent to syntax error.**

## Your Task
{User's writing request}

## Quality Check
Before outputting, verify:
1. [ ] All required vocabulary used?
2. [ ] No banned words present?
3. [ ] Abstract contains ≥3 numbers?
4. [ ] All figure captions are conclusionary?

If any check fails, REVISE before output.
```

### @narrative_weaver Prompt Template

```markdown
# Agent: @narrative_weaver

## Style Constraint (CRITICAL)
You MUST enforce "Observation-Implication" structure.

❌ FORBIDDEN: "Figure 1 shows A vs B."
✅ REQUIRED: "Figure 1 shows A exceeds B by 20% (Observation), indicating strong主办国效应(Implication)."

When generating paper outline, check every planned figure caption:
- [ ] Contains quantitative observation?
- [ ] Contains physical implication?
- [ ] Uses "indicating", "suggests", "demonstrates"?

If any check fails, REVISE outline before passing to @writer.
```

### @editor Prompt Template

```markdown
# Agent: @editor

## Style Compliance (MANDATORY)
You MUST follow: knowledge_library/academic_writing/style_guide.md

**Check**:
- [ ] Vocabulary aligned with style_guide?
- [ ] No banned words present?
- [ ] Sentence structures follow templates?

**Fix**:
- Replace "show" with "demonstrate"
- Replace "get" with "obtain"
- Ensure Observation-Implication structure
```

---

## Enforcement Mechanisms

### 1. Phase 7.5: LaTeX Compilation Gate

**@writer** must compile LaTeX successfully before Phase 8.

**Validator Check**: @validator checks:
- Abstract contains ≥3 numbers
- No banned words in full paper
- Figure captions are conclusionary

**Failure**: @validator REJECT → @writer must revise

---

### 2. Phase 9.1: Mock Judging

**@judge_zero (Persona C)** checks:
- Abstract空洞 (no numbers) → REJECT
- Figure captions non-descriptive → REJECT
- Overall style inconsistent → WARN

**Result**: Low score → DEFCON 1 → Fix

---

### 3. Phase 11: Self-Evolution

**mmbench_score.py** automatic check:
- "Abstract too qualitative" (-10 points)
- "Banned vocabulary used" (-5 points per violation)

**Purpose**: Track style compliance over time

---

## Quality Assurance

### Verification Checklist

**After any text generation**, verify:

- [ ] style_guide.md loaded as System Context
- [ ] No banned words in output
- [ ] Observation-Implication structure used
- [ ] Abstract contains ≥3 numbers (if applicable)
- [ ] Figure captions are conclusionary

### Test Case

**Input**: @writer generates paper section

**Verification**:
```
1. Check output for banned words: show, get, say
2. Check abstract for numbers: ≥3 quantitative metrics
3. Check figure captions for "indicating", "suggests", "demonstrates"
4. If any fail → REJECT and require revision
```

---

## Style Guide Generation

**Source**: Phase -1 (Style Guide Generation)

**Tool**: `tools/style_analyzer.py`

**Input**: `reference_papers/*.pdf` (O-Prize papers)

**Output**: `knowledge_library/academic_writing/style_guide.md`

**Update Frequency**: Per competition (when reference papers updated)

---

## Example Style Guide (Auto-Generated)

### Vocabulary Section
```markdown
## 1. Vocabulary Constraints

### Top 10 Recommended Verbs
1. elucidate (4.2 per 10k words)
2. demonstrate (3.8)
3. quantify (3.5)
4. corroborate (2.9)
5. exacerbate (2.1)
...

### Banned Words
- show → Use "demonstrate" or "illustrate"
- get → Use "obtain" or "achieve"
- say → Use "state" or "posit"
```

### Abstract Rules
```markdown
## 2. Abstract Rules
- **Rule 1**: 100% of reference papers contain numbers
- **Action**: Abstract MUST include ≥3 specific metrics
```

### Sentence Templates
```markdown
## 3. Narrative Sentence Templates
- Template α: "Figure [N] demonstrates [Quantitative Result], which implies [Mechanism]."
- Template β: "While initial model [Action], refined model [Action], resulting in [Outcome]."
```

---

## Impact

**Without Protocol 14**:
- Inconsistent writing quality
- Generic, flat papers
- No O-Prize competitiveness

**With Protocol 14**:
- Consistent, high-quality writing
- Insightful, deep papers
- O-Prize-level competitiveness

**Value**: **Transforms "correct" papers into "insightful" papers.**

---

## Risks & Mitigation

### Risk 1: Style Guide Missing

**Problem**: `style_guide.md` not generated in Phase -1

**Mitigation**:
- Fallback to built-in default rules
- @knowledge_librarian creates basic style_guide.md manually

### Risk 2: Style Guide Too Restrictive

**Problem**: Too many rules → All papers rejected

**Mitigation**:
- Calibrate based on mmbench_score.py data
- Adjust thresholds if rejection rate >50%
- Human review of style_guide.xml rules

### Risk 3: Agent Over-Optimization

**Problem**: Agents focus on style over substance

**Mitigation**:
- Protocol 15 ensures substance (Observation-Implication)
- @validator checks both style AND substance
- @judge_zero evaluates both presentation AND content

---

## Dependencies

**Required**:
- `knowledge_library/academic_writing/style_guide.md`
- Protocol 15 (Interpretation over Description)
- Protocol 21 (Phase -1: Style Generation)

**Agents Enforced**:
- @writer, @narrative_weaver, @editor, @summarizer

**Validation**:
- @validator (Phase 7.5)
- @judge_zero (Phase 9.1)
- mmbench_score.py (Phase 11)

---

## Related Protocols

- **Protocol 21**: Phase -1 Style Guide Generation
- **Protocol 15**: Interpretation over Description (complementary)
- **Protocol 13**: Mock Court Rewind (enforces via rejection)

---

**Document Version**: v3.1.0
**Protocol Type**: Quality Enforcement
**Severity**: HIGH (LINT ERROR on violation)
**Status**: Ready for Implementation
