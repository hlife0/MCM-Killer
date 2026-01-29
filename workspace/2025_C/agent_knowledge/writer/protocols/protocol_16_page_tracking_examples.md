# Protocol 16: Page Count Tracking Examples

**Agent**: @writer
**Protocol**: 16 (Page Count Tracking)
**Purpose**: Show examples of page count reporting and consolidation

---

## Example 1: Normal Progression (All Checkpoints Pass)

### Phase 7A Complete
```
Director, Phase 7A complete.

File: output/paper/paper.tex
Sections written: Abstract, Introduction, Notation
Page count: 2.8 / 3.0 pages
Status: ✅ PASS (within budget)

Checkpoint: output/paper/checkpoint_7A.md
Ready for Phase 7B.
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

## Page Budget Reference Table

### Quick Reference for @writer

| Section | Budget | Cumulative | Checkpoint |
|---------|--------|------------|------------|
| Abstract | 0.3 | 0.3 | - |
| Introduction | 1.2 | 1.5 | After 7A |
| Notation | 0.5 | 2.0 | After 7A |
| Models | 6.0 | 8.0 | After 7B |
| Data | 2.0 | 10.0 | After 7C |
| Results | 8.0 | 18.0 | After 7C |
| Sensitivity | 2.0 | 20.0 | After 7D |
| Strengths/Weaknesses | 2.0 | 22.0 | After 7D |
| Discussion | 1.5 | 23.5 | After 7E |
| Conclusions | 1.0 | 24.5 | After 7E |
| Bibliography | 0.5 | 25.0 | After 7E |

### Alert Thresholds

| Status | Condition | Action |
|--------|-----------|--------|
| ✅ PASS | Page count ≤ budget | Proceed to next phase |
| ⚠️ YELLOW | Page count ≥ 20.0 | Tighten remaining sections |
| ❌ RED | Page count ≥ 23.0 | Stop writing, consolidate |
| ❌ CRITICAL | Page count ≥ 25.0 | Block submission, mandatory consolidation |

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
- Adjust if approaching yellow/red thresholds

---

**END OF PROTOCOL 16 EXAMPLES**
