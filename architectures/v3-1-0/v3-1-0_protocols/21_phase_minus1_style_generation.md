# Protocol 21: Phase -1 - Style Guide Generation

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Phase**: Phase -1 (Pre-competition)
> **Agent**: @knowledge_librarian
> **Tool**: tools/style_analyzer.py

---

## Purpose

Automatically generate `style_guide.md` by analyzing O-Prize winning papers in `reference_papers/` directory. This gives the system "academic审美" (academic aesthetic sense) before competition begins.

---

## When to Execute

**Trigger**: Manual trigger before competition OR auto-detect new PDFs in `reference_papers/`

**Frequency**: Once per competition (when reference papers are updated)

**Timing**: Before Phase 0 (Problem Understanding)

---

## Process

### Step 1: Collect Reference Papers

**Input**: `reference_papers/*.pdf`

**Requirement**: At least 2-3 O-Prize winning papers
- 2024 Problem C O-Prize papers
- 2023 Problem D O-Prize papers
- Other high-scoring MCM/ICM papers

### Step 2: Run Style Analyzer

**Command**:
```bash
python tools/style_analyzer.py reference_papers/ knowledge_library/academic_writing/style_guide.md
```

**Tool Implementation**: See `m-orientation/B_IMPLEMENTATION_GUIDES/01_sprint_1_foundation.md`

### Step 3: Verify Output

**Check**:
- [ ] `style_guide.md` generated
- [ ] Contains ≥10 recommended academic verbs (elucidate, demonstrate, quantify, etc.)
- [ ] Contains abstract rules (≥3 numbers requirement)
- [ ] Contains sentence templates (Observation-Implication patterns)

---

## Output Format

### Generated: `knowledge_library/academic_writing/style_guide.md`

**Structure**:
```markdown
# O-Prize Style Guide (Auto-Generated)

## 1. Vocabulary Constraints

### Recommended Verbs (High Academic Value)
- elucidate (Top 1, frequency: 4.2 per 10k words)
- demonstrate (Top 2, frequency: 3.8)
- quantify (Top 3, frequency: 3.5)

### Banned Weak Words
- show → Use "demonstrate" or "illustrate"
- get → Use "obtain" or "achieve"
- say → Use "state" or "posit"

## 2. Abstract Rules
- **Rule 1**: 100% of reference papers contain numbers in Abstract
- **Action**: Abstract MUST include ≥3 specific metrics (RMSE, R², p-values, percentages)

## 3. Narrative Sentence Templates
- Template α: "Figure [N] demonstrates [Result], which implies [Mechanism]."
- Template β: "While initial model [Action], refined model [Action], resulting in [Outcome]."

## 4. Figure Caption Standards
- Reference papers: 87% conclusionary captions
- **Standard**: Captions must contain quantitative findings
- ❌ "Figure 1: X vs Y"
- ✅ "Figure 1: Increasing X leads to saturation in Y (p < 0.001)"
```

---

## Integration with Other Components

### Protocol 14: Academic Style Alignment

**All text-generating agents** (@writer, @narrative_weaver, @editor) **MUST** load `style_guide.md` as System Context.

**Enforcement**:
- @validator checks compliance in Phase 7.5
- @judge_zero (Persona C) checks in Phase 9.1
- Persistent violations trigger prompt review in Phase 11

---

## Failure Modes

### Failure Mode 1: No Reference Papers

**Symptom**: `reference_papers/` directory empty

**Fallback**: Use built-in default style guide

**Action**: Log warning and use default rules:
- Recommended verbs: elucidate, demonstrate, quantify, corroborate
- Banned words: show, get, say
- Abstract must have ≥3 numbers

### Failure Mode 2: Style Analysis Tool Error

**Symptom**: `tools/style_analyzer.py` crashes

**Fallback**: Manual style guide creation

**Action**: @knowledge_librarian creates basic style_guide.md manually

---

## Quality Assurance

### Verification Checklist

After Phase -1 completion, verify:

- [ ] `knowledge_library/academic_writing/style_guide.md` exists
- [ ] File contains ≥10 recommended verbs
- [ ] File contains ≥3 abstract rules
- [ ] File contains ≥2 sentence templates
- [ ] File size > 5KB (indicates substantial content)

### Test Case

**Input**: 2-3 O-Prize papers in `reference_papers/`

**Expected Output**:
```
✅ Style guide generated: knowledge_library/academic_writing/style_guide.md
✅ Extracted 25 recommended verbs
✅ Abstract rule: 100% contain numbers → Require ≥3
✅ Extracted 5 sentence templates
✅ Extracted figure caption rules
```

---

## Dependencies

**Input**:
- `reference_papers/*.pdf` (O-Prize papers)

**Tool**:
- `tools/style_analyzer.py` (Python script)
- Dependencies: `pdfplumber`, `spacy`

**Output**:
- `knowledge_library/academic_writing/style_guide.md`

---

## Example Output

### Sample style_guide.md (excerpt)

```markdown
# O-Prize Style Guide (Auto-Generated from 3 papers)

## 1. Vocabulary Constraints

### Top 10 Academic Verbs
1. elucidate (4.2 per 10k words) - "explain in detail"
2. demonstrate (3.8) - "show clearly"
3. quantify (3.5) - "express as number"
4. corroborate (2.9) - "support with evidence"
5. exacerbate (2.1) - "make worse"
6. mitigate (2.0) - "alleviate"
7. underscore (1.8) - "emphasize"
8. pinpoint (1.7) - "identify precisely"
9. illuminate (1.6) - "clarify"
10. reveal (1.5) - "make visible"

### Banned Words
- show → Use "demonstrate" (1200% more academic)
- get → Use "obtain" or "achieve"
- say → Use "state" or "posit"
- look at → Use "examine" or "investigate"
```

---

## Success Criteria

Phase -1 is successful when:

1. ✅ `style_guide.md` generated from O-Prize papers
2. ✅ File contains data-driven rules (not guesses)
3. ✅ All text agents can load style_guide.md successfully
4. ✅ @judge_zero (Persona C) can validate against style_guide.md

---

## Next Steps

After Phase -1 completes:
- Proceed to Phase 0 (Problem Understanding)
- Phase 0.2 will use HMML 2.0 + style_guide.md for method recommendations
- Phase 7 will enforce style_guide.md constraints via Protocol 14

---

**Document Version**: v3.1.0
**Related Protocols**: Protocol 14 (Academic Style Alignment), Protocol 15 (Interpretation over Description)
**Related Agents**: @knowledge_librarian, @writer, @narrative_weaver, @editor, @judge_zero
