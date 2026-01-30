# Protocol 17: Page Count Feedback (Phase 7)

## Overview

**Purpose**: Provide real-time page count feedback to @writer during Phase 7 sub-phases to prevent exceeding 28-page limit.

**When Called**: After each Phase 7 sub-phase (7A, 7B, 7C, 7D, 7E)

**Target**: 28 pages maximum (allows manual reduction to 25 pages later)

---

## Thresholds (28-Page System)

| Status | Page Range | Meaning | Action |
|--------|------------|---------|--------|
| ✅ **GREEN** | <24 pages | Safe zone | Proceed without changes |
| ⚠️ **YELLOW** | 24-26 pages | Warning zone | Recommend review, can proceed |
| 🔴 **RED** | 26-28 pages | Critical zone | Recommend consolidation before proceeding |
| 🛑 **CRITICAL** | >28 pages | Over limit | MUST consolidate, cannot proceed |

---

## Budget Targets by Sub-Phase (ALIGNED WITH O-PRIZE PAPERS)

**Based on analysis of 8 O-Prize papers (2020-2022):**

| Sub-Phase | Sections | Target Pages | Cumulative Target | O-Prize % |
|-----------|----------|--------------|-------------------|-----------|
| **7A** | Abstract + Intro + Notation | 3 pages | 3 pages | 10.7% |
| **7B** | Model sections (all models) | 11 pages | 14 pages | 39.3% |
| **7C** | Results + Figures | 7 pages | 21 pages | 25.0% |
| **7D** | Sensitivity + Strengths/Weaknesses + Conclusions | 4 pages | 25 pages | 14.3% |
| **7E** | References + Appendix | 3 pages | 28 pages | 10.7% |
| **7F** | Compilation (no new content) | 0 pages | 28 pages | - |

**Total budget = 28 pages** (allows 3-page buffer before manual reduction to 25)

**Key Insight**: O-Prize papers allocate 39% to model development (largest section), NOT introduction. Model section should be 11 pages with detailed mathematics.

---

## Feedback Format Template

```
Phase 7[X] Page Count Feedback:

Measured: [X.X] pages
Target: [Y] pages
Status: [GREEN/YELLOW/RED/CRITICAL]

Budget Analysis:
- Cumulative: [current] / [target]
- Remaining budget: [pages left]
- Sections remaining: [list]
- Projected final: [estimate]

[If YELLOW/RED/CRITICAL]:
Recommendations:
1. [Specific consolidation suggestion]
2. [Section to shorten]
3. [Figure consolidation options]

Verdict: ✅ PROCEED / ⚠️ REVISE RECOMMENDED / 🛑 MUST CONSOLIDATE
```

---

## Example Scenarios

### Scenario 1: GREEN Status (Phase 7A)

```
Phase 7A Page Count Feedback:

Measured: 2.8 pages
Target: 3 pages
Status: ✅ GREEN (0.2 pages under budget)

Budget Analysis:
- Cumulative: 2.8 / 3
- Remaining budget: 25.2 pages for 7B-7E
- Sections remaining: Models (11p), Results (7p), Sensitivity/S&W/Conclusions (4p), Refs/Appendix (3p)
- Projected final: 27.8 pages

Verdict: ✅ PROCEED to Phase 7B
```

**Director action**: Proceed to Phase 7B immediately.

---

### Scenario 2: YELLOW Status (Phase 7C)

```
Phase 7C Page Count Feedback:

Measured: 19.5 pages
Target: 21 pages (cumulative: 3 + 11 + 7)
Status: ⚠️ YELLOW (1.5 pages under budget - good!)

Budget Analysis:
- Cumulative: 19.5 / 21 (within target)
- Remaining budget: 5.5 pages for 7D, 7E
- Sections remaining: Sensitivity/S&W/Conclusions (4p), Refs/Appendix (3p)
- Projected final: 26.5 pages

Recommendations:
1. Consider consolidating Figures 8-9 into single multi-panel figure (saves 0.5 pages if needed later)
2. Keep Discussion section concise (aim for 1.5 pages instead of 2 pages)

Verdict: ✅ PROCEED (within acceptable range)
```

**Director action**:
- Option 1: Ask @writer to implement recommendations before proceeding
- Option 2: Allow proceed but monitor closely in 7D/7E

---

### Scenario 3: RED Status (Phase 7D)

```
Phase 7D Page Count Feedback:

Measured: 26.2 pages
Target: 22 pages
Status: 🔴 RED (4.2 pages over budget)

Budget Analysis:
- Cumulative: 26.2 / 22
- Remaining budget: -0.2 pages for 7E (DEFICIT)
- Sections remaining: Discussion (2p), Conclusions (1p)
- Projected final: 29.2 pages (EXCEEDS 28-PAGE LIMIT)

Recommendations:
1. **URGENT**: Consolidate model sections (reduce from 7 pages to 5 pages):
   - Merge Model 1 and Model 2 into single integrated framework (-1 page)
   - Remove redundant equations, keep only novel formulations (-0.5 pages)
   - Consolidate assumption tables (-0.5 pages)

2. Reduce Results section (from 8 pages to 6.5 pages):
   - Merge Tables 2-3 into single comparison table (-0.5 pages)
   - Move Figure 5 to Appendix (-0.5 pages)
   - Shorten results narrative by 0.5 pages

3. Reduce Sensitivity section (from 2.5 pages to 1.5 pages):
   - Consolidate sensitivity figures into multi-panel (-0.5 pages)
   - Summarize parameter variations in table format (-0.5 pages)

Verdict: 🛑 MUST CONSOLIDATE before Phase 7E
```

**Director action**:
- BLOCK progression to Phase 7E
- Send @writer back to revise phases 7B, 7C, 7D
- Request specific consolidations
- Re-run page count check after revisions

---

### Scenario 4: CRITICAL Status (Phase 7E)

```
Phase 7E Page Count Feedback:

Measured: 29.3 pages
Target: 26 pages
Status: 🛑 CRITICAL (3.3 pages over 28-page HARD LIMIT)

Budget Analysis:
- Cumulative: 29.3 pages
- Hard limit: 28 pages
- Overage: 1.3 pages

**CRITICAL**: Paper exceeds 28-page hard limit. CANNOT PROCEED to Phase 7.5.

Emergency Consolidation Required:
1. **Immediate (-1.5 pages)**:
   - Remove Figure 7 (move to Appendix) (-0.5 pages)
   - Merge Tables 4-5 into single table (-0.5 pages)
   - Remove redundant paragraphs in Discussion (-0.5 pages)

2. **If still over (-1.0 pages)**:
   - Consolidate Model 3 and Model 4 sections (-0.5 pages)
   - Reduce Introduction from 2.5 to 2 pages (-0.5 pages)

3. **If still over (-0.8 pages)**:
   - Merge Figures 2-3 into multi-panel (-0.5 pages)
   - Reduce Strengths/Weaknesses from 1.5 to 1 page (-0.5 pages)

Verdict: 🛑 REJECT - MUST CONSOLIDATE to ≤28 pages before Phase 7.5
```

**Director action**:
- REJECT current paper
- Send @writer back with emergency consolidation instructions
- Re-run entire page count check after revisions
- Do NOT proceed until page count ≤28

---

## Budget Calculation Formulas

### Remaining Budget
```
Remaining Budget = Total Budget - Current Pages
Total Budget = 26 pages (target) or 28 pages (hard limit)
```

### Projected Final Page Count
```
Projected Final = Current Pages + Estimated Pages for Remaining Sections
```

**Estimation Table** (O-Prize aligned, based on actual papers):
- Abstract + Intro + Notation: 3 pages (10.7%)
- Model sections (per model): ~2.2 pages × 5 = 11 pages (39.3%)
- Results + Figures: 7 pages (25.0%)
- Sensitivity Analysis: 2 pages (7.1%)
- Strengths/Weaknesses + Conclusions: 2 pages (7.1%)
- References: 1 page (3.6%)
- Appendix: 2 pages (7.1%)

**Total typical**: 28 pages

---

## Consolidation Strategies

### Strategy 1: Figure Consolidation
**When**: YELLOW or RED status
**Technique**: Multi-panel figures
**Savings**: 0.5-1 page per consolidation
**Example**:
- Before: Figure 2 (full page) + Figure 3 (full page) = 2 pages
- After: Figure 2 (a-b multi-panel) = 1 page
- Savings: 1 page

### Strategy 2: Table Merging
**When**: YELLOW or RED status
**Technique**: Combine related tables
**Savings**: 0.3-0.5 pages per merge
**Example**:
- Before: Table 2 (Model parameters) + Table 3 (Model results) = 1 page
- After: Combined table with parameters and results = 0.5 pages
- Savings: 0.5 pages

### Strategy 3: Model Section Reduction
**When**: RED or CRITICAL status
**Technique**: Remove redundant derivations, merge related models
**Savings**: 0.5-1 page per model reduction
**Example**:
- Before: Model 1 (2 pages) + Model 2 (2 pages) = 4 pages
- After: Integrated Model 1-2 (3 pages) = 3 pages
- Savings: 1 page

### Strategy 4: Narrative Tightening
**When**: Any status (always good practice)
**Technique**: Remove redundant paragraphs, wordiness
**Savings**: 0.2-0.5 pages per section
**Example**:
- Remove transition paragraphs that repeat information
- Consolidate multi-sentence statements into single sentences
- Remove redundant introductory/concluding paragraphs

### Strategy 5: Appendix Migration
**When**: CRITICAL status (emergency)
**Technique**: Move non-essential content to appendix
**Savings**: 0.5-2 pages
**Example**:
- Move detailed derivations to appendix
- Move supplementary figures to appendix
- Move sensitivity analysis tables to appendix

---

## Communication Examples

### Example 1: Positive Feedback (GREEN)
```
@director: Phase 7B complete, requesting @editor page check.

@editor: Phase 7B Page Count Feedback:

Measured: 9.8 pages
Target: 10 pages
Status: ✅ GREEN (0.2 under budget)

Budget Analysis:
- Cumulative: 9.8 / 10
- Remaining budget: 16.2 pages for 7C, 7D, 7E
- Sections remaining: Results (8p), Analysis (4p), Conclusions (4p)
- Projected final: 25.8 pages

Excellent work staying within budget. Model sections are appropriately detailed.

Verdict: ✅ PROCEED to Phase 7C

@director: @writer, proceed to Phase 7C (Results Integration).
```

### Example 2: Warning Feedback (YELLOW with recommendations)
```
@director: Phase 7C complete, requesting @editor page check.

@editor: Phase 7C Page Count Feedback:

Measured: 20.2 pages
Target: 18 pages
Status: ⚠️ YELLOW (2.2 pages over budget)

Budget Analysis:
- Cumulative: 20.2 / 18
- Remaining budget: 3.8 pages for 7D, 7E
- Sections remaining: Sensitivity (2p), Strengths (1p), Discussion (2p), Conclusions (1p)
- Projected final: 26.2 pages (within 28-page limit but tight)

Recommendations:
1. Consolidate Figures 6-7 into single multi-panel figure (-0.5 pages)
2. Reduce Results section narrative by tightening transition paragraphs (-0.5 pages)
3. Merge Tables 3-4 into single comparison table (-0.5 pages)

Implementing these would bring cumulative to 18.7 pages (closer to target).

Verdict: ⚠️ REVISE RECOMMENDED (or proceed with caution)

@director: @writer, please implement @editor's recommendations before proceeding to Phase 7D.
```

### Example 3: Critical Feedback (RED - MUST consolidate)
```
@director: Phase 7D complete, requesting @editor page check.

@editor: Phase 7D Page Count Feedback:

Measured: 27.5 pages
Target: 22 pages
Status: 🔴 RED (5.5 pages over budget)

Budget Analysis:
- Cumulative: 27.5 / 22
- Remaining budget: -1.5 pages for 7E (DEFICIT)
- Sections remaining: Discussion (2p), Conclusions (1p)
- Projected final: 30.5 pages (EXCEEDS 28-PAGE HARD LIMIT by 2.5 pages)

**CRITICAL**: Current trajectory will exceed 28-page limit.

Emergency Consolidation Plan:
1. Model sections (reduce 7 pages → 5.5 pages = -1.5 pages):
   - Consolidate Models 2-3 into integrated framework (-0.5 pages)
   - Remove equation derivations, cite instead (-0.5 pages)
   - Merge assumption tables (-0.5 pages)

2. Results section (reduce 8 pages → 6.5 pages = -1.5 pages):
   - Consolidate Figures 4-5 into multi-panel (-0.5 pages)
   - Merge Tables 2-3 (-0.5 pages)
   - Tighten narrative (-0.5 pages)

3. Sensitivity section (reduce 2.5 pages → 1.5 pages = -1 page):
   - Multi-panel sensitivity figures (-0.5 pages)
   - Tabulate parameter variations (-0.5 pages)

Total savings: 4 pages → Projected final: 26.5 pages (within limit)

Verdict: 🛑 MUST CONSOLIDATE before Phase 7E

@director: @writer, CRITICAL page count issue. Implement emergency consolidation plan immediately. Do NOT proceed to Phase 7E until cumulative ≤24 pages.
```

---

## How to Measure Page Count

### Method 1: PDF Page Count (Recommended)
```bash
cd output/paper
pdflatex -interaction=nonstopmode paper.tex
pdfinfo paper.pdf | grep Pages
```

Output: `Pages: 19`

### Method 2: LaTeX Word Count (Alternative)
```bash
texcount -total -brief paper.tex
```

Output: `Words in text: 8500` → Estimate: 8500/350 ≈ 24.3 pages (assuming 350 words/page)

**Note**: PDF page count is more accurate because it accounts for figures, tables, equations.

---

## Quick Reference: Verdict Decision Tree

```
Is cumulative page count < 24?
├─ YES → ✅ GREEN → PROCEED
└─ NO → Is cumulative page count 24-26?
    ├─ YES → ⚠️ YELLOW → RECOMMEND REVIEW (can proceed)
    └─ NO → Is cumulative page count 26-28?
        ├─ YES → 🔴 RED → RECOMMEND CONSOLIDATION
        └─ NO → 🛑 CRITICAL → MUST CONSOLIDATE (BLOCK)
```

---

## Integration with Phase 7 Workflow

**Standard Flow**:
1. @writer completes Phase 7X
2. @writer reports page count to @director
3. @director calls @editor for page check (Protocol 17)
4. @editor compiles, measures, analyzes, provides feedback
5. **If GREEN**: @director → @writer proceed to 7(X+1)
6. **If YELLOW**: @director → @writer optional revisions, then proceed
7. **If RED/CRITICAL**: @director → @writer MUST revise, then re-check

**Revision Loop**:
1. @editor provides specific recommendations
2. @writer implements revisions
3. @writer recompiles and measures new page count
4. @writer reports to @director
5. @director → @editor for re-check
6. Repeat until status = GREEN or acceptable YELLOW
7. Maximum 2 revision rounds per sub-phase

---

## Summary

**Key Principle**: Proactive page management prevents last-minute emergency consolidation.

**Editor Role**: Act as early warning system, providing actionable feedback before problems become critical.

**Success Metric**: Paper stays ≤28 pages throughout Phase 7, allowing smooth progression to Phase 7.5 and Phase 8.
