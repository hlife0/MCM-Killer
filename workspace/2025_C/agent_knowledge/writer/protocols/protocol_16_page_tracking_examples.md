# Protocol 16: Page Count Tracking Examples (UPDATED - 28-Page System)

**Agent**: @writer
**Protocol**: 16 (Page Count Tracking with Editor Feedback)
**Purpose**: Show examples of page count reporting, editor feedback, and consolidation
**NEW**: Editor provides feedback after each sub-phase (7A-7F)

---

## NEW: 28-Page System Overview

**Change**: Target increased from 25 → 28 pages to allow manual reduction later

**Updated Thresholds**:
- ✅ **GREEN**: <24 pages (safe zone)
- ⚠️ **YELLOW**: 24-26 pages (warning, review needed)
- 🔴 **RED**: 26-28 pages (critical, consolidation required)
- 🛑 **CRITICAL**: >28 pages (REJECT, must consolidate)

**NEW Workflow**: After each sub-phase:
1. @writer completes sub-phase → Reports page count to @director
2. @director → @editor for page check (Protocol 17)
3. @editor → Feedback (GREEN/YELLOW/RED/CRITICAL)
4. If changes needed: @writer revises → repeat
5. If GREEN/YELLOW OK: Proceed to next sub-phase

---

## Example 1: Normal Progression with Editor Feedback (All GREEN)

### Phase 7A Complete
```
@writer: Director, Phase 7A complete.

File: output/paper/paper.tex
Sections written: Abstract, Introduction, Notation
Page count: 2.8 / 3.0 pages
Status: ✅ GREEN (within budget)

Checkpoint: output/paper/checkpoint_7A.md
Awaiting @editor page check before Phase 7B.
```

**NEW: @director calls @editor for page check**
```
@director: @editor, review Phase 7A page count and formatting.
- File: output/paper/paper.tex
- Sections: Abstract, Introduction, Notation
- Writer's page count: 2.8 pages
- Budget: 3.0 pages
```

**NEW: @editor provides feedback (Protocol 17)**
```
@editor: Phase 7A Page Count Feedback:

Measured: 2.8 pages
Target: 3 pages
Status: ✅ GREEN (0.2 under budget)

Budget Analysis:
- Cumulative: 2.8 / 3
- Remaining budget: 23.2 pages for 7B-7E
- Sections remaining: Models (7p), Results (8p), Analysis (4p), Conclusions (4p)
- Projected final: 25.8 pages

Verdict: ✅ PROCEED to Phase 7B
```

**@director to @writer**
```
@director: @writer, @editor approves. Proceed to Phase 7B.
```

### Phase 7B Complete
```
Director, Phase 7B complete.

File: output/paper/paper.tex
Sections written: Model 1-5 sections (with full mathematical formulations)
Page count: 9.5 / 10.0 pages cumulative
Status: ✅ PASS (within budget)

Checkpoint: output/paper/checkpoint_7B.md
Ready for Phase 7C.
```

### Phase 7C Complete
```
Director, Phase 7C complete.

File: output/paper/paper.tex
Sections written: Data Description, Results (with figures and tables)
Page count: 17.8 / 18.0 pages cumulative
Status: ✅ PASS (within budget)

Checkpoint: output/paper/checkpoint_7C.md
Ready for Phase 7D.
```

### Phase 7D Complete
```
Director, Phase 7D complete.

File: output/paper/paper.tex
Sections written: Sensitivity Analysis, Strengths/Weaknesses
Page count: 21.5 / 22.0 pages cumulative
Status: ✅ PASS (within budget)

Checkpoint: output/paper/checkpoint_7D.md
Ready for Phase 7E.
```

### Phase 7E Complete
```
Director, Phase 7E complete.

File: output/paper/paper.tex
Sections written: Discussion, Conclusions, Bibliography
Page count: 24.8 / 25.0 pages cumulative
Status: ✅ PASS (within budget, 0.2 pages under limit)

Checkpoint: output/paper/checkpoint_7E.md
Ready for Phase 7F (LaTeX compilation).
```

---

## Example 2: Yellow Warning (Approaching Limit)

### Phase 7C Complete
```
Director, Phase 7C complete.

File: output/paper/paper.tex
Sections written: Data Description, Results
Page count: 20.3 / 18.0 pages cumulative
Status: ⚠️ YELLOW WARNING (exceeds budget by 2.3 pages)

Issue: Results section longer than expected (included extra diagnostic figures)

Action Plan for Remaining Sections:
- Discussion: Reduce from 1.5 to 1.0 pages (-0.5)
- Conclusions: Reduce from 1.0 to 0.75 pages (-0.25)
- Consolidate 2 figures onto 1 page (-1.0)
- Expected final: 20.3 - 1.75 = 18.55 pages

Checkpoint: output/paper/checkpoint_7C.md
Awaiting @director guidance before Phase 7D.
```

### @director Response
```
@writer: Yellow warning acknowledged.

Action: Tighten remaining sections as proposed.
Constraint: No new figures, consolidate existing only.

Proceed to Phase 7D with tightened budget.
```

---

## Example 3: Red Critical (Exceeds Limit)

### Phase 7E Complete
```
Director, Phase 7E complete.

File: output/paper/paper.tex
Sections written: Discussion, Conclusions, Bibliography
Page count: 26.7 / 25.0 pages cumulative
Status: ❌ RED CRITICAL (exceeds limit by 1.7 pages)

Action: STOPPED writing. Awaiting consolidation instructions.

Current page breakdown:
- Abstract: 0.3
- Introduction: 1.5
- Notation: 0.5
- Models: 7.5 (over budget)
- Data: 2.5
- Results: 9.2 (over budget)
- Sensitivity: 2.5
- Strengths/Weaknesses: 2.5
- Discussion: 1.5
- Conclusions: 1.0
- Bibliography: 0.5
- Appendices: 2.0

Checkpoint: output/paper/checkpoint_7E.md
BLOCKED: Cannot proceed to Phase 7F.
```

### @director Response
```
@writer: Red critical alert received. Emergency consolidation required.

Consolidation Plan (Priority Order):
1. Move appendices to supplement: -2.0 pages
   - Create supplementary_materials.pdf
   - Add note in main text: "See Supplementary Appendix A"

2. Consolidate Results figures: -2.0 pages
   - Merge Model 1-3 diagnostics (3 → 1 page)
   - Merge Model 4-5 diagnostics (2 → 1 page)

3. Reduce Model descriptions: -1.0 pages
   - Each model: 1.5 → 1.3 pages (5 models total)

4. Shorten Discussion: -0.3 pages
   - Remove redundant summary points

Expected after consolidation: 26.7 - 5.3 = 21.4 pages ✓

Execute consolidation and report back.
```

---

## Example 4: Emergency Consolidation Execution

### Consolidation Report
```
Director, consolidation complete.

File: output/paper/paper.tex
Actions Taken:

1. ✅ Appendices moved to supplement
   - Created: output/paper/supplementary_materials.pdf
   - Added reference in main text (Section 6)
   - Pages saved: -2.0

2. ✅ Results figures consolidated
   - Figure 3: Model 1-3 diagnostics (merged from 3 pages to 1)
   - Figure 4: Model 4-5 diagnostics (merged from 2 pages to 1)
   - Pages saved: -2.0

3. ✅ Model descriptions reduced
   - Each model section: 1.5 → 1.3 pages
   - Removed non-essential derivations
   - Pages saved: -1.0

4. ✅ Discussion shortened
   - Removed redundant summary (paragraph 3)
   - Pages saved: -0.3

Total pages saved: -5.3
Page count: 26.7 → 21.4 pages
Status: ✅ PASS (within 25-page limit)

Revised page breakdown:
- Abstract: 0.3
- Introduction: 1.5
- Notation: 0.5
- Models: 6.5 (reduced)
- Data: 2.5
- Results: 7.2 (consolidated)
- Sensitivity: 2.5
- Strengths/Weaknesses: 2.5
- Discussion: 1.2 (shortened)
- Conclusions: 1.0
- Bibliography: 0.5

Checkpoint: output/paper/checkpoint_7E_consolidated.md
Ready for Phase 7F (LaTeX compilation).
```

### @director Response
```
@writer: Consolidation verified.

Page count: 21.4 / 25.0 pages ✓
Status: ✅ APPROVED for Phase 7F

Proceed to LaTeX compilation.
```

---

## Example 5: LaTeX Table Usage (Protocol 18 Integration)

### Wrong Way (Manual Transcription)
```latex
% ❌ FORBIDDEN: Manually transcribing values
\begin{table}[htbp]
\centering
\caption{2028 Olympic Medal Forecasts}
\begin{tabular}{lcccc}
\toprule
Country & Gold & Silver & Bronze & Total \\
\midrule
China & 25.27 & 22.45 & 18.30 & 66.02 \\  % Manually typed
USA & 38.15 & 35.20 & 28.90 & 102.25 \\     % Manually typed
Great Britain & 14.50 & 12.30 & 10.20 & 37.00 \\
\bottomrule
\end{tabular}
\end{table}
```

**Problem**: Manual transcription creates inconsistencies (Protocol 18 violation)

---

### Right Way (Automated Injection)
```bash
# Step 1: Generate LaTeX table from CSV
python output/implementation/code/csv_to_latex_table.py \
    output/results/results_1.csv \
    1 \
    output/paper/tables/

# Output:
# ✅ Generated LaTeX table: output/paper/tables/table_1.tex
#    Source CSV: output/results/results_1.csv
#    Rows: 234, Columns: 8
```

```latex
% Step 2: Include generated table in paper.tex
\begin{table}[htbp]
\centering
\caption{2028 Olympic Medal Forecasts (90\% Credible Intervals)}
\label{tab:forecasts_2028}
\input{../output/paper/tables/table_1.tex}
\end{table}
```

**Advantages**:
- ✅ 100% consistency (CSV = LaTeX)
- ✅ No manual transcription errors
- ✅ Easy to regenerate (re-run script)
- ✅ Passes Protocol 18 validation

---

## Page Budget Reference Table (O-PRIZE ALIGNED)

### Quick Reference for @writer

**Based on analysis of 8 O-Prize papers (2020-2022):**

| Section | Budget | Cumulative | O-Prize % | Checkpoint |
|---------|--------|------------|-----------|------------|
| Abstract | 1.0 | 1.0 | 3.6% | - |
| Introduction | 2.0 | 3.0 | 7.1% | After 7A |
| Notation | - | 3.0 | - | After 7A |
| **Models (all)** | 11.0 | 14.0 | 39.3% | After 7B |
| Results | 7.0 | 21.0 | 25.0% | After 7C |
| Sensitivity | 2.0 | 23.0 | 7.1% | After 7D |
| Strengths/Weaknesses | 1.0 | 24.0 | 3.6% | After 7D |
| Conclusions | 1.0 | 25.0 | 3.6% | After 7D |
| References | 1.0 | 26.0 | 3.6% | After 7E |
| Appendix | 2.0 | 28.0 | 7.1% | After 7E |

**Key Insight**: O-Prize papers allocate 39% to model development (NOT introduction). Model section should be detailed with full mathematics.

### Alert Thresholds (UPDATED - 28-Page System)

| Status | Condition | Action |
|--------|-----------|--------|
| ✅ GREEN | Page count <24 | Proceed to next phase |
| ⚠️ YELLOW | Page count 24-26 | Warning, review recommended (can proceed) |
| 🔴 RED | Page count 26-28 | Critical, consolidation recommended before proceeding |
| 🛑 CRITICAL | Page count >28 | Block progression, MUST consolidate |

**Key Change**: Thresholds shifted from 20/23/25 to 24/26/28 to align with 28-page target.

---

## Tips for Staying Within Budget

### 1. Write Concisely
- Use active voice: "We develop" (not "It was developed")
- Remove filler words: "in order to" → "to"
- Avoid repetition: State once, reference later

### 2. Consolidate Visuals
- Use 2×2 figure grids where appropriate
- Merge similar figures (e.g., Model 1-3 diagnostics)
- Reduce figure size (full-page → half-page)

### 3. Prioritize Content
- Keep only essential equations in main text
- Move non-essential derivations to appendices
- Move supplementary results to online appendix

### 4. Track Continuously
- Check page count after EVERY section
- Report to @director at each checkpoint
- **NEW**: Wait for @editor feedback before proceeding
- Adjust if approaching yellow/red thresholds

---

## Example 6: Editor Feedback Workflow (YELLOW Warning at Phase 7C)

### Phase 7C Complete
```
@writer: Director, Phase 7C complete.

File: output/paper/paper.tex
Sections written: Data Description, Results (with figures and tables)
Page count: 19.5 / 18.0 pages cumulative
Status: ⚠️ YELLOW (1.5 pages over budget)

Checkpoint: output/paper/checkpoint_7C.md
Awaiting @editor page check before Phase 7D.
```

**@director calls @editor for page check**
```
@director: @editor, review Phase 7C page count and formatting.
- File: output/paper/paper.tex
- Sections: Data Description, Results
- Writer's page count: 19.5 pages
- Budget: 18.0 pages
```

**@editor provides YELLOW feedback (Protocol 17)**
```
@editor: Phase 7C Page Count Feedback:

Measured: 19.5 pages
Target: 18 pages
Status: ⚠️ YELLOW (1.5 pages over budget)

Budget Analysis:
- Cumulative: 19.5 / 18
- Remaining budget: 4.5 pages for 7D, 7E
- Sections remaining: Sensitivity (2p), Strengths (1p), Discussion (2p), Conclusions (1p)
- Projected final: 25.5 pages

Recommendations:
1. Consider consolidating Figures 8-9 into single multi-panel figure (-0.5 pages)
2. Reduce Results section introduction from 1 page to 0.5 pages (-0.5 pages)
3. Keep Discussion section concise (aim for 1.5 pages instead of 2 pages)

Verdict: ⚠️ REVISE RECOMMENDED (but can proceed if writer confident)
```

**@director decision: Option 1 - Request revisions**
```
@director: @writer, please implement @editor's recommendations 1 and 2 before proceeding to Phase 7D.
- Consolidate Figures 8-9 (-0.5 pages)
- Reduce Results intro (-0.5 pages)
- Target: 18.5 pages after revisions
```

**@writer revises and re-reports**
```
@writer: Director, Phase 7C revisions complete.

Actions taken:
1. ✅ Consolidated Figures 8-9 into single multi-panel figure
2. ✅ Reduced Results introduction from 1.0 to 0.5 pages

Page count: 19.5 → 18.5 pages
Status: ✅ GREEN (0.5 pages over budget, acceptable)

Awaiting @editor re-check before Phase 7D.
```

**@editor re-checks**
```
@editor: Phase 7C Re-Check:

Measured: 18.5 pages
Target: 18 pages
Status: ✅ GREEN (0.5 over budget, within acceptable range)

Budget Analysis:
- Cumulative: 18.5 / 18
- Remaining budget: 5.5 pages for 7D, 7E
- Projected final: 24.5 pages

Verdict: ✅ PROCEED to Phase 7D

Good work consolidating figures and tightening narrative.
```

**@director to @writer**
```
@director: @writer, @editor approves. Proceed to Phase 7D.
```

---

## Example 7: Editor Feedback Workflow (RED Critical at Phase 7D)

### Phase 7D Complete
```
@writer: Director, Phase 7D complete.

File: output/paper/paper.tex
Sections written: Sensitivity Analysis, Strengths/Weaknesses
Page count: 26.2 / 22.0 pages cumulative
Status: 🔴 RED (4.2 pages over budget)

Issue: Sensitivity section longer than expected due to comprehensive parameter variations

Checkpoint: output/paper/checkpoint_7D.md
Awaiting @editor page check before Phase 7E.
```

**@director calls @editor for page check**
```
@director: @editor, review Phase 7D page count and formatting.
- File: output/paper/paper.tex
- Sections: Sensitivity Analysis, Strengths/Weaknesses
- Writer's page count: 26.2 pages
- Budget: 22.0 pages
```

**@editor provides RED feedback (Protocol 17)**
```
@editor: Phase 7D Page Count Feedback:

Measured: 26.2 pages
Target: 22 pages
Status: 🔴 RED (4.2 pages over budget)

Budget Analysis:
- Cumulative: 26.2 / 22
- Remaining budget: -0.2 pages for 7E (DEFICIT)
- Sections remaining: Discussion (2p), Conclusions (1p)
- Projected final: 29.2 pages (EXCEEDS 28-PAGE LIMIT)

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

Total savings: 4 pages → Projected final: 26.2 - 4 = 22.2 pages ✅

Verdict: 🛑 MUST CONSOLIDATE before Phase 7E
```

**@director decision: BLOCK progression**
```
@director: @writer, CRITICAL page count issue. Implement emergency consolidation plan immediately.
- Target: Reduce from 26.2 to ≤24 pages
- Do NOT proceed to Phase 7E until cumulative ≤24 pages
- Follow @editor's consolidation plan exactly
```

**@writer consolidates and re-reports**
```
@writer: Director, consolidation complete.

Actions taken:
1. ✅ Consolidated Models 2-3 sections (-0.5 pages)
2. ✅ Removed equation derivations, added citations (-0.5 pages)
3. ✅ Merged assumption tables (-0.5 pages)
4. ✅ Consolidated Results Figures 4-5 into multi-panel (-0.5 pages)
5. ✅ Merged Tables 2-3 (-0.5 pages)
6. ✅ Tightened Results narrative (-0.5 pages)
7. ✅ Created multi-panel sensitivity figures (-0.5 pages)
8. ✅ Tabulated parameter variations (-0.5 pages)

Total pages saved: -4.0
Page count: 26.2 → 22.2 pages
Status: ✅ GREEN (0.2 pages over target, acceptable)

Awaiting @editor re-check before Phase 7E.
```

**@editor re-checks**
```
@editor: Phase 7D Re-Check:

Measured: 22.2 pages
Target: 22 pages
Status: ✅ GREEN (0.2 over budget, well within acceptable range)

Budget Analysis:
- Cumulative: 22.2 / 22
- Remaining budget: 3.8 pages for 7E
- Sections remaining: Discussion (2p), Conclusions (1p)
- Projected final: 25.2 pages (within 28-page limit ✅)

Consolidation Quality:
- Model sections: Well integrated, no loss of clarity
- Results: Effective figure consolidation
- Sensitivity: Good use of multi-panel and tables

Verdict: ✅ PROCEED to Phase 7E

Excellent consolidation work. Paper is now on track to finish ≤26 pages.
```

**@director to @writer**
```
@director: @writer, @editor approves. Proceed to Phase 7E.
- Remaining budget: 3.8 pages for Discussion + Conclusions
- Stay within budget to avoid further consolidation
```

---

**END OF PROTOCOL 16 EXAMPLES (UPDATED)**
