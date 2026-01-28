# Phase 7 Sub-Phase Quick Reference for @director

**Purpose**: Guide for calling Phase 7 sub-phases correctly
**Status**: ✅ Active (implemented 2026-01-28)

---

## Overview

Phase 7 is now split into 6 sub-phases (7A-7F) to prevent timeouts. Each sub-phase is called separately by @director.

---

## Calling Sequence

### Phase 7A: Paper Framework

```
@writer: Phase 7A - Write paper framework

Write the following sections for output/paper/paper.tex:
1. Abstract (with ≥3 quantitative metrics)
2. Introduction (Problem Background + Restatement + Our Approach)
3. Notation table (if not in template)

Requirements:
- Use \documentclass{mcmthesis}
- Include \mcmsetup{} with team number and problem
- Write \begin{abstract}...\end{abstract}
- Include \tableofcontents

DO NOT write model sections yet (that's Phase 7B).

After completion, report:
- Sections written
- Word count
- Confirm paper.tex created
```

**Expected Output**: `output/paper/paper.tex` (~200-300 lines)
**Time**: 10-15 minutes

---

### Phase 7B: Model Sections

```
@writer: Phase 7B - Write model sections

Read output/paper/paper.tex to verify Phase 7A is complete.

Then APPEND model sections:
- Section 4: Model Development
- For each of 5 models:
  * Model Overview
  * Assumptions (copy from model_design.md WORD-FOR-WORD)
  * Mathematical Formulation (copy equations WORD-FOR-WORD)
  * Solution Approach (copy complete algorithm)
- Each model should be 2-3 pages with FULL math detail

CRITICAL: Copy-Adapt-Paste protocol
- DO NOT summarize
- DO NOT paraphrase
- Copy equations EXACTLY from model_design.md
- Include ALL assumptions, constraints, parameters

After writing, read back paper.tex to verify no corruption.
```

**Expected Output**: `output/paper/paper.tex` (~600-800 lines total)
**Time**: 30-40 minutes

---

### Phase 7C: Results Integration

```
@writer: Phase 7C - Integrate results data and figures

Read output/paper/paper.tex to verify Phases 7A-7B are complete.

Then APPEND Results section:
- Section 5: Results
- Implementation Details
- For each model:
  * Numerical results (from results_quick_*.csv)
  * Tables with key metrics
  * Figures (from output/figures/*.png)
  * Use \includegraphics for each figure
  * Follow Protocol 15: Observation → Implication with numbers

Input files:
- output/implementation/data/results_quick_*.csv
- output/figures/*.png (22 figures)

After writing, read back paper.tex to verify no corruption.
```

**Expected Output**: `output/paper/paper.tex` (~800-1000 lines total)
**Time**: 15-20 minutes

---

### Phase 7D: Analysis Sections

```
@writer: Phase 7D - Write analysis sections

Read output/paper/paper.tex to verify Phases 7A-7C are complete.

Then APPEND analysis sections:
- Section 6: Sensitivity Analysis
  * For each model: parameter tested, range, results
  * Include sensitivity figures if available
- Section 7: Strengths and Weaknesses
  * 3-5 strengths (with explanations)
  * 3-5 weaknesses (with potential improvements)

Reference: sensitivity analysis plans from model_design.md

After writing, read back paper.tex to verify no corruption.
```

**Expected Output**: `output/paper/paper.tex` (~1000-1200 lines total)
**Time**: 10-15 minutes

---

### Phase 7E: Conclusions

```
@writer: Phase 7E - Write conclusions and bibliography

Read output/paper/paper.tex to verify Phases 7A-7D are complete.

Then APPEND final sections:
- Section 8: Discussion and Conclusions
  * Synthesis and Conclusions
  * Response to each requirement (with numerical answers)
  * Evaluation and Bias Analysis
  * Implications
  * Final Recommendations
- Bibliography
  * Include references for methods, data sources, etc.
  * Use proper academic format
- Appendices (if needed)

After writing, read back paper.tex to verify completeness.
```

**Expected Output**: `output/paper/paper.tex` (complete, ~1200-1400 lines)
**Time**: 10-15 minutes

---

### Phase 7F: LaTeX Compilation

```
@writer: Phase 7F - Compile LaTeX to PDF

Read output/paper/paper.tex to verify it's complete.

Then compile LaTeX:
cd output/paper
pdflatex paper.tex
pdflatex paper.tex  # Run twice for references

Check exit code:
- 0 = Success
- Non-zero = Compilation failed

If failed:
1. Check paper.log for errors: grep -i "error" paper.log
2. Fix errors (max 3 attempts)
3. Retry compilation

Report compilation status:
- SUCCESS: paper.pdf generated, page count
- FAILURE: errors encountered, need help

After success, paper.pdf is ready for Phase 7.5 (LaTeX Gate).
```

**Expected Output**: `output/paper/paper.pdf` (25 pages or less)
**Time**: 5-10 minutes

---

## Checkpoint Tracking

After each Phase 7 sub-phase completes, update VERSION_MANIFEST.json:

```json
{
  "phase_7_subphases": {
    "7A": { "status": "completed", "timestamp": "2026-01-28T14:30:00Z" },
    "7B": { "status": "completed", "timestamp": "2026-01-28T15:15:00Z" },
    "7C": { "status": "in_progress", "timestamp": "2026-01-28T15:30:00Z" }
  },
  "phase_7_resume_point": "7C"
}
```

## Resume Protocol

If a sub-phase times out:

1. Check VERSION_MANIFEST.json for last completed sub-phase
2. Resume from that sub-phase (skip completed ones)
3. Read paper.tex to verify current state
4. Continue execution

Example:
- 7A completed, 7B completed, 7C timed out
- Resume from 7C (don't redo 7A-7B)
- Continue to 7D, 7E, 7F

---

## Verification Commands

After each sub-phase:

```bash
# Check file size
wc -l output/paper/paper.tex

# Check specific sections exist
grep "begin{abstract}" output/paper/paper.tex
grep "section.*Model" output/paper/paper.tex
grep "section.*Results" output/paper/paper.tex

# After 7F: Verify PDF exists
ls -lh output/paper/paper.pdf
```

---

## Troubleshooting

| Issue | Symptom | Solution |
|-------|---------|----------|
| Timeout | Sub-phase takes >2× estimated time | Break into smaller chunks |
| Corruption | paper.tex has garbled text | Delete and rewrite section |
| Missing figures | \includegraphics errors | Verify files in output/figures/ |
| Compilation errors | pdflatex fails | Check paper.log for errors |
| Resume failure | Can't determine where to resume | Check VERSION_MANIFEST.json |

---

## Success Criteria

Phase 7 is complete when:

- [ ] All 6 sub-phases (7A-7F) have status="completed"
- [ ] paper.tex exists and is >1200 lines
- [ ] paper.pdf exists and compiles without errors
- [ ] PDF has ≤25 pages (excluding summary sheet)
- [ ] All 5 models documented with full math
- [ ] All 22 figures embedded
- [ ] All results integrated
- [ ] Bibliography included

---

**Quick Reference Version**: 1.0
**Last Updated**: 2026-01-28
**Implementation Status**: ✅ Active
