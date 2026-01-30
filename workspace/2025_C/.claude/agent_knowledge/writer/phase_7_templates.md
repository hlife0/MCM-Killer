# Phase 7 Sub-Phase Templates and Instructions

This file contains detailed instructions and templates for each Phase 7 sub-phase (7A-7F).

## Phase 7 Sub-Phase Overview

| Sub-Phase | Sections to Write | Est. Time | Output |
|-----------|-------------------|-----------|--------|
| **7A** | Abstract + Introduction + Notation | 10-15 min | paper.tex (framework) |
| **7B** | Model sections (5 models, full math) | 30-40 min | paper.tex (appended) |
| **7C** | Results section (data + figures) | 15-20 min | paper.tex (appended) |
| **7D** | Sensitivity + Strengths/Weaknesses | 10-15 min | paper.tex (appended) |
| **7E** | Discussion + Conclusions + Bibliography | 10-15 min | paper.tex (complete) |
| **7F** | LaTeX compilation to PDF | 5-10 min | paper.pdf |

## Checkpoint Reporting Format

After completing each sub-phase, report to @director:

```
Director, Phase 7[X] complete.

File: output/paper/paper.tex
Sections written: [list sections]
Word count: [count]
Checkpoint: output/paper/checkpoint_7[X].md

Ready for Phase 7[Y].
```

## Phase 7A: Framework Writing

**Input Files:**
- `output/requirements_checklist.md`
- `output/research_notes.md`
- `output/narrative_arc_*.md` (if available)

**Tasks:**
1. Write Summary Sheet (Abstract)
   - 250-350 words
   - Background → Methods → Results → Implications
   - Include ≥3 quantitative metrics
2. Write Introduction
   - Problem background
   - Restatement of problem
   - Our approach
3. Write Notation section
   - Complete notation table from model_design.md

**Output:** `paper.tex` with framework sections

**Quality Check:**
- [ ] Abstract contains ≥3 quantitative metrics
- [ ] Introduction starts with compelling hook
- [ ] All notation from model_design.md included

## Phase 7B: Model Sections

**Input Files:**
- `output/model_design.md` (CRITICAL - copy WORD-FOR-WORD)

**Tasks:**
1. For each model (typically 5 models):
   - Model Overview (2-3 sentences)
   - Mathematical Formulation (COPY equations exactly)
   - Solution Approach (4-6 steps)
   - Model Justification (1 paragraph)
2. Each model section should be 1.5-2.5 pages

**Output:** `paper.tex` with model sections appended

**Quality Check:**
- [ ] ALL equations copied word-for-word (not rewritten)
- [ ] ALL parameters defined immediately after equations
- [ ] Each model section is 1.5-2.5 pages
- [ ] Model names match model_design.md exactly

## Phase 7C: Results Integration

**Input Files:**
- `output/results_summary.md`
- `output/figures/*.png`
- `output/implementation/data/*.csv`

**Tasks:**
1. Write Implementation Details subsection
2. For each model:
   - Present numerical results
   - Include tables (using `csv_to_latex_table.py`)
   - Include figures with 4-element captions
3. Place figures IMMEDIATELY after first reference using `[H]`
4. Use `../figures/` path (not `figures/`)

**Output:** `paper.tex` with Results section appended

**Quality Check:**
- [ ] All figures from output/figures/ embedded
- [ ] All figures have 4-element captions (Observation → Implication → Story → Takeaway)
- [ ] Tables generated from CSV using Protocol 18 script
- [ ] Figure paths use `../figures/` (relative to output/paper/)

## Phase 7D: Analysis Sections

**Input Files:**
- `output/model_design.md` (sensitivity plans)
- `output/results_summary.md`

**Tasks:**
1. Write Sensitivity Analysis section
   - For each model: parameter tested, range, results
   - Include sensitivity figures
2. Write Strengths and Weaknesses section
   - 3-5 strengths with explanations
   - 3-5 weaknesses with potential improvements

**Output:** `paper.tex` with analysis sections appended

**Quality Check:**
- [ ] Sensitivity analysis covers all models
- [ ] Strengths/weaknesses are balanced
- [ ] Each item has substantive explanation

## Phase 7E: Conclusions

**Input Files:**
- `output/requirements_checklist.md`
- `output/narrative_arc_*.md`
- `output/docs/methodology_evolution_{i}.md` (if available)

**Tasks:**
1. Write Discussion section
   - Synthesis and Conclusions
   - Response to each requirement
   - Evaluation and Bias Analysis
   - Implications
   - Final Recommendations
2. Write Conclusions section
3. Write Bibliography
4. Include "What We Discovered" subsection (3-6 insights)

**Output:** `paper.tex` with conclusions and bibliography

**Quality Check:**
- [ ] Each requirement explicitly answered
- [ ] "What We Discovered" subsection present
- [ ] Bibliography properly formatted
- [ ] Methodology evolution insights integrated (≤2 sentences each)

## Phase 7F: LaTeX Compilation

**Tasks:**
1. Compile LaTeX to PDF:
   ```bash
   cd output/paper/
   pdflatex paper.tex
   pdflatex paper.tex  # Run twice for references
   ```
2. Check exit code (0 = success, non-zero = failure)
3. If failed:
   - Examine errors: `grep -i "error" paper.log`
   - Fix errors (max 3 attempts)
   - Retry compilation
4. Report compilation status to Director

**Output:** `paper.pdf`

**Error Types:**

| Error Type | You Fix | Example |
|-----------|---------|---------|
| **Syntax errors** | ✅ Yes | Missing `}`, unclosed environments |
| **Table errors** | ✅ Yes | Misaligned `&` or `\\` |
| **Math errors** | ✅ Yes | Unescaped `_` or `^` |
| **File not found** | ✅ Yes | Missing image files |
| **Package errors** | ❌ No (escalate) | Missing packages, fonts |

**Submission Format:**

**SUCCESS:**
```
Director, LaTeX compilation SUCCESSFUL.

File: output/paper/paper_{i}.tex
PDF: output/paper/paper_{i}.pdf (pages: 27)
Log: output/paper/paper_{i}.log (no errors)

Compilation time: 45 seconds
Paper is ready for Phase 7.5 LaTeX Compilation Gate.
```

**FAILURE** (with fixable errors):
```
Director, LaTeX compilation FAILED (attempt 1/3).

File: output/paper/paper_{i}.tex
Errors:
  - Line 234: Missing }
  - Line 456: Misaligned table

Fixing now...
```

**FAILURE** (after 3 attempts):
```
Director, LaTeX compilation FAILED after 3 attempts.

Errors persist:
  - Complex table alignment (lines 400-450)
  - Nested environment issues (Section 5)

Recommendation: Request rewind to Phase 7
Reason: Cannot resolve with simple fixes
Action: Simplify LaTeX structure
```

## Resume Capability

If a sub-phase times out:
1. **Check VERSION_MANIFEST.json** for last completed sub-phase
2. **Resume from that sub-phase** (don't redo completed work)
3. **Read paper.tex** to verify current state
4. **Continue from where work stopped**

Example VERSION_MANIFEST.json:
```json
{
  "phase_7a": { "status": "completed", "timestamp": "2026-01-28T14:30:00Z" },
  "phase_7b": { "status": "completed", "timestamp": "2026-01-28T15:15:00Z" },
  "phase_7c": { "status": "in_progress", "timestamp": "2026-01-28T15:30:00Z" }
}
```

If timeout at Phase 7C:
- Resume from Phase 7C (7A and 7B already complete)
- Read paper.tex to see what's already written
- Continue appending from current state
