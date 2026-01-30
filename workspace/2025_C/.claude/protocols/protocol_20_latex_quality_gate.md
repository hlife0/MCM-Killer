# Protocol 20: LaTeX Quality Gate (Phase 7.5)

**Version**: 3.3.0
**Status**: Active
**Owner**: @editor (primary checker), @writer (fixes issues)
**Scope**: Phase 7.5 (LaTeX Compilation Gate)
**Priority**: HIGH

---

## Overview

**Purpose**: Verify LaTeX formatting quality beyond just compilation success.

**When Called**: After Phase 7F (after paper.tex compiled to PDF)

**Scope**: Compilation + Blank Space + Text Overflow + Page Breaks

**Decision**: PASS → Phase 8 | ISSUES → Revise → Re-check | 3 failures → Rewind to Phase 7

---

## Check 1: Compilation Success (Existing)

### What to Check
- [ ] `paper.pdf` exists in `output/paper/` directory
- [ ] No LaTeX compilation errors in `paper.log`
- [ ] All figures render correctly
- [ ] All tables render correctly
- [ ] All equations display properly
- [ ] Table of contents generated
- [ ] Page numbers present

### How to Check
```bash
cd output/paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex  # Second pass for references

# Check exit code
echo $?  # Should be 0 for success

# Check for errors in log
grep -i "error" paper.log

# Verify PDF created
ls -lh paper.pdf
```

### Common Compilation Errors

| Error Type | Example | Fix |
|------------|---------|-----|
| Missing `}` | `\textbf{text` | Add closing brace |
| Unclosed environment | `\begin{table}` without `\end{table}` | Close environment |
| Undefined command | `\customcommand` | Define command or remove |
| Missing figure | `! File 'fig1.png' not found` | Check file path |
| Math mode error | `Missing $ inserted` | Add `$...$` around math |

### Feedback Format (Compilation)
```
Compilation Check: ✅ PASS / ❌ FAIL

[If FAIL]:
Errors Found:
- Line 245: Missing } after \textbf{Model Description
- Line 389: Undefined command \customfigure
- Missing file: output/figures/figure_5.png

Fix: @writer please correct these errors and recompile.
```

---

## Check 2: Blank Space Detection (NEW)

### What to Look For

**Definition**: Large vertical blank spaces (>1 inch) that waste page real estate.

**Common Locations**:
- After figures with `[H]` placement forcing text to next page
- Before/after section breaks with manual `\clearpage` or `\newpage`
- Around large tables that break poorly
- At end of sections with inadequate text flow

### Visual Inspection Checklist
- [ ] Scan each page for large vertical gaps
- [ ] Check page transitions (bottom of one page, top of next)
- [ ] Identify half-empty pages
- [ ] Check section breaks for awkward spacing

### How to Detect

**Method 1: Visual PDF Review**
```bash
# Open PDF and visually scan each page
evince output/paper/paper.pdf  # Linux
open output/paper/paper.pdf    # Mac
start output/paper/paper.pdf   # Windows

# Look for:
# - Pages with >50% blank space
# - Large gaps between paragraphs (>2 inches)
# - Awkward page breaks mid-section
```

**Method 2: Page Density Analysis**
```bash
# Check page count vs word count ratio
pdfinfo output/paper/paper.pdf | grep Pages
texcount -total -brief paper.tex

# Calculate: words/page
# Typical: 300-400 words/page
# Suspicious: <250 words/page (indicates excessive blank space)
```

### Common Causes and Fixes

#### Cause 1: Figure Placement Forcing Text to Next Page
**Symptom**: Large blank space after figure, text starts on next page

**LaTeX Pattern**:
```latex
\begin{figure}[H]  % [H] forces figure HERE
\includegraphics{figure.png}
\caption{...}
\end{figure}

% If figure is large, LaTeX may push it to next page,
% leaving large blank on current page
```

**Fix**:
```latex
% Option 1: Use flexible placement
\begin{figure}[htbp]  % Allow LaTeX to optimize placement
\includegraphics{figure.png}
\caption{...}
\end{figure}

% Option 2: Reduce figure size
\includegraphics[width=0.7\textwidth]{figure.png}  % Instead of 0.9\textwidth

% Option 3: Use \FloatBarrier from placeins package
\usepackage{placeins}
\section{Results}
\FloatBarrier  % Ensures all floats placed before this point
```

#### Cause 2: Manual Page Breaks
**Symptom**: Half-page blank before section

**LaTeX Pattern**:
```latex
% Bad: Manual page breaks
\newpage
\section{Model Description}

\clearpage
\section{Results}
```

**Fix**:
```latex
% Remove manual page breaks, let LaTeX handle it
\section{Model Description}
\section{Results}

% If section MUST start on new page, use:
\newpage\section{Results}  % No blank line between
```

#### Cause 3: Large Tables Breaking Poorly
**Symptom**: Table doesn't fit on page, leaving large blank

**LaTeX Pattern**:
```latex
\begin{table}[H]
\begin{tabular}{...}
... very long table (30+ rows) ...
\end{tabular}
\end{table}
```

**Fix**:
```latex
% Option 1: Use longtable for multi-page tables
\usepackage{longtable}
\begin{longtable}{...}
... table content ...
\end{longtable}

% Option 2: Reduce font size
\begin{table}[H]
\small  % or \footnotesize
\begin{tabular}{...}
... table content ...
\end{tabular}
\end{table}

% Option 3: Split into multiple tables
```

### Feedback Format (Blank Space)
```
Blank Space Check: ✅ PASS / ⚠️ ISSUES FOUND

[If ISSUES]:
Issues Found:
1. Page 5: Large blank space (8 inches) after Figure 2
   - Cause: Figure placement with [H] forcing text to next page
   - Fix: Change \begin{figure}[H] to \begin{figure}[htbp]

2. Page 12: Half-page blank before Section 4 (Results)
   - Cause: Manual \newpage command
   - Fix: Remove \newpage on line 342

3. Page 18: Large gap (4 inches) around Table 3
   - Cause: Table too wide, breaking poorly
   - Fix: Reduce table font size with \small or split into two tables

Total blank space detected: 3 issues
Priority: HIGH (wasting ~1.5 pages)
```

---

## Check 3: Text Overflow Detection (NEW)

### What to Look For

**Definition**: Text extending beyond page margins or causing LaTeX warnings.

**Types**:
- Overfull hbox: Text too wide for line
- Overfull vbox: Content too tall for page
- Tables wider than text width
- Math equations extending into margin

### How to Detect

**Method 1: Check LaTeX Log**
```bash
# Check for overfull/underfull warnings
grep "Overfull" output/paper/paper.log
grep "Underfull" output/paper/paper.log

# Example output:
# Overfull \hbox (15.23pt too wide) in paragraph at lines 342--345
# Underfull \hbox (badness 10000) in paragraph at lines 456--458
```

**Method 2: Visual PDF Inspection**
```bash
# Look for:
# - Text extending beyond right margin
# - Tables cut off at right edge
# - Math equations overlapping margin
# - Long URLs breaking page layout
```

### Common Causes and Fixes

#### Cause 1: Long URLs in Bibliography
**Symptom**: Overfull hbox in bibliography section

**LaTeX Pattern**:
```latex
\bibitem{ref1}
Author. Title. Available at: https://very-long-url-that-does-not-break-properly.com/path/to/resource
```

**Fix**:
```latex
% Use url package with breakurl
\usepackage{url}
\usepackage{breakurl}

\bibitem{ref1}
Author. Title. Available at: \url{https://very-long-url-that-does-not-break-properly.com/path/to/resource}
```

#### Cause 2: Wide Tables
**Symptom**: Table extends beyond right margin

**LaTeX Pattern**:
```latex
\begin{table}[H]
\begin{tabular}{lccccccccc}  % 10 columns, too wide
... table content ...
\end{tabular}
\end{table}
```

**Fix**:
```latex
% Option 1: Scale table to fit
\usepackage{graphicx}
\begin{table}[H]
\resizebox{\textwidth}{!}{  % Scale to text width
\begin{tabular}{lccccccccc}
... table content ...
\end{tabular}
}
\end{table}

% Option 2: Reduce font size
\begin{table}[H]
\small  % or \footnotesize
\begin{tabular}{lccccccccc}
... table content ...
\end{tabular}
\end{table}

% Option 3: Rotate table
\usepackage{rotating}
\begin{sidewaystable}
\begin{tabular}{lccccccccc}
... table content ...
\end{tabular}
\end{sidewaystable}
```

#### Cause 3: Long Math Equations
**Symptom**: Equation extends beyond right margin

**LaTeX Pattern**:
```latex
\begin{equation}
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 + \beta_4 x_4 + \beta_5 x_5 + \beta_6 x_6 + \epsilon
\end{equation}
```

**Fix**:
```latex
% Option 1: Use multline for line breaks
\usepackage{amsmath}
\begin{multline}
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 \\
    + \beta_4 x_4 + \beta_5 x_5 + \beta_6 x_6 + \epsilon
\end{multline}

% Option 2: Use align for multi-line equations
\begin{align}
y &= \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3 \nonumber \\
  &\quad + \beta_4 x_4 + \beta_5 x_5 + \beta_6 x_6 + \epsilon
\end{align}
```

#### Cause 4: Long Words Without Hyphenation
**Symptom**: Long technical terms don't break, causing overfull hbox

**LaTeX Pattern**:
```latex
The methodological framework incorporates socioeconomic factors...
```

**Fix**:
```latex
% Option 1: Manual hyphenation hints
The method\-ological framework incorporates socio\-economic factors...

% Option 2: Use \allowbreak
The methodological\allowbreak framework incorporates socioeconomic\allowbreak factors...

% Option 3: Rewrite sentence
The framework incorporates socioeconomic factors...
```

### Feedback Format (Text Overflow)
```
Text Overflow Check: ✅ PASS / ⚠️ ISSUES FOUND

[If ISSUES]:
Issues Found:
1. Line 342: Overfull hbox (15.2pt too wide)
   - Cause: Long URL in bibliography (reference 12)
   - Fix: Use \url{} command with breakurl package

2. Table 3 (page 15): Width exceeds text margins by 23pt
   - Cause: 10-column table without scaling
   - Fix: Add \resizebox{\textwidth}{!}{...} wrapper

3. Equation (8) on page 18: Extends into right margin
   - Cause: Long equation without line break
   - Fix: Use multline environment to split across lines

Total overflow issues: 3
Priority: MEDIUM (affects readability but doesn't break PDF)
```

---

## Check 4: Page Break Quality (NEW)

### What to Look For

**Definition**: Poor page breaks that hurt readability.

**Types**:
- Orphan: Section header at bottom of page with no following text
- Widow: Single line of paragraph at top of page
- Split caption: Figure/table caption separated from content
- Awkward table splits: Table header on one page, data on next

### How to Detect

**Visual Inspection**:
- Scan page transitions (bottom of page N, top of page N+1)
- Check section headers (should have ≥2 lines of text following)
- Check figures/tables (caption should be on same page as content)
- Check multi-page tables (headers should repeat)

### Common Causes and Fixes

#### Issue 1: Section Header Orphan
**Symptom**: Section header at bottom of page, text starts on next page

**LaTeX Pattern**:
```latex
% End of page 10
...previous section text...

\section{Model Validation}  % Orphan header at bottom
% Page break occurs here

% Top of page 11
The validation process involves...
```

**Fix**:
```latex
% Option 1: Use needspace package
\usepackage{needspace}
\needspace{3\baselineskip}  % Ensure 3 lines available
\section{Model Validation}
The validation process involves...

% Option 2: Manual \pagebreak before section
\pagebreak
\section{Model Validation}
The validation process involves...
```

#### Issue 2: Widow Line
**Symptom**: Single line of paragraph at top of page

**LaTeX Pattern**:
```latex
% Bottom of page 12
The model incorporates multiple parameters including GDP,
population, and historical medal counts to predict future
% Page break occurs here
% Top of page 13
performance with 95% confidence intervals.  % Widow line
```

**Fix**:
```latex
% Add to preamble to prevent widows/orphans
\widowpenalty=10000
\clubpenalty=10000

% Or manually adjust paragraph breaks
```

#### Issue 3: Split Figure Caption
**Symptom**: Figure on one page, caption on next page

**LaTeX Pattern**:
```latex
\begin{figure}[t]  % Top placement
\includegraphics[width=\textwidth]{large_figure.png}
% Page break occurs here
\caption{Description of figure...}  % Caption on next page
\end{figure}
```

**Fix**:
```latex
% Option 1: Use [!h] for here placement
\begin{figure}[!h]
\includegraphics[width=\textwidth]{large_figure.png}
\caption{Description of figure...}
\end{figure}

% Option 2: Reduce figure size to fit on one page
\begin{figure}[t]
\includegraphics[width=0.85\textwidth]{large_figure.png}  % Reduced from \textwidth
\caption{Description of figure...}
\end{figure}

% Option 3: Force figure to next page
\clearpage
\begin{figure}[t]
\includegraphics[width=\textwidth]{large_figure.png}
\caption{Description of figure...}
\end{figure}
```

#### Issue 4: Awkward Table Split
**Symptom**: Table header on one page, data rows on next

**LaTeX Pattern**:
```latex
\begin{table}[H]
\begin{tabular}{lcc}
\toprule
Country & Predicted & Actual \\
\midrule
% Page break occurs here
USA & 38 & 40 \\
China & 35 & 38 \\
...
\end{tabular}
\end{table}
```

**Fix**:
```latex
% Use longtable with repeating headers
\usepackage{longtable}
\begin{longtable}{lcc}
\toprule
Country & Predicted & Actual \\
\midrule
\endfirsthead  % Header for first page

\toprule
Country & Predicted & Actual \\
\midrule
\endhead  % Repeating header for subsequent pages

USA & 38 & 40 \\
China & 35 & 38 \\
...
\end{longtable}
```

### Feedback Format (Page Breaks)
```
Page Break Check: ✅ PASS / ⚠️ ISSUES FOUND

[If ISSUES]:
Issues Found:
1. Page 7: Section 3.2 header ("Model Validation") at bottom with no text
   - Issue: Orphan section header
   - Fix: Add \needspace{3\baselineskip} before \section{Model Validation}

2. Page 10-11: Figure 5 on page 10, caption on page 11
   - Issue: Split figure caption
   - Fix: Reduce figure size to 0.85\textwidth or use \clearpage before figure

3. Page 15: Widow line at top of page
   - Issue: Single line of paragraph isolated
   - Fix: Already set \widowpenalty in preamble, may require manual adjustment

Total page break issues: 3
Priority: LOW (affects aesthetics but not functionality)
```

---

## Complete Feedback Template

```
Phase 7.5: LaTeX Quality Gate

Compilation: ✅ PASS / ❌ FAIL
Pages: [count] (target: <28)

Blank Space Check: ✅ PASS / ⚠️ ISSUES FOUND
[If issues: List with page numbers and fixes]

Text Overflow Check: ✅ PASS / ⚠️ ISSUES FOUND
[If issues: List with line numbers and fixes]

Page Break Check: ✅ PASS / ⚠️ ISSUES FOUND
[If issues: List with page numbers and fixes]

Overall Verdict:
✅ PASS - Proceed to Phase 8
⚠️ MINOR ISSUES - @writer please address [X] items, then re-check
🛑 MAJOR ISSUES - @writer must revise, then re-submit for Phase 7.5

[If issues found]:
Priority Fixes:
1. [Most critical issue - affects functionality]
2. [Second priority - affects readability]
3. [Third priority - affects aesthetics]

@writer: Please revise and resubmit for Phase 7.5 re-check.
```

---

## Example: Complete Phase 7.5 Check

### Scenario 1: PASS (No Issues)

```
Phase 7.5: LaTeX Quality Gate

Compilation: ✅ PASS
- paper.pdf generated successfully
- No errors in paper.log
- All 15 figures rendered
- All 8 tables rendered
Pages: 26 (target: <28) ✅

Blank Space Check: ✅ PASS
- No large vertical gaps detected
- Page density: 340 words/page (healthy)
- All page transitions smooth

Text Overflow Check: ✅ PASS
- No overfull hbox warnings
- No underfull hbox warnings (badness >10000)
- All tables within margins
- All equations within margins

Page Break Check: ✅ PASS
- No orphan section headers
- No widow lines
- All figure captions on same page as figures
- Table breaks handled with longtable

Overall Verdict: ✅ PASS - Proceed to Phase 8

Excellent formatting quality. Paper is ready for Phase 8 (Summary).
```

### Scenario 2: MINOR ISSUES

```
Phase 7.5: LaTeX Quality Gate

Compilation: ✅ PASS
Pages: 27 (target: <28) ✅

Blank Space Check: ⚠️ ISSUES FOUND
1. Page 12: Half-page blank before Section 4
   - Fix: Remove \newpage on line 342

Text Overflow Check: ⚠️ ISSUES FOUND
1. Line 567: Overfull hbox (12pt too wide) - long URL
   - Fix: Use \url{} command
2. Table 5: Width exceeds margins by 18pt
   - Fix: Add \resizebox{\textwidth}{!}{...}

Page Break Check: ✅ PASS

Overall Verdict: ⚠️ MINOR ISSUES - Fix 3 items, then re-check

Priority Fixes:
1. Remove manual \newpage (line 342) - saves 0.5 pages
2. Fix URL overflow (line 567) - affects readability
3. Scale Table 5 - affects readability

Estimated time to fix: 5-10 minutes

@writer: Please address these 3 items and recompile. The issues are straightforward and won't require restructuring.
```

### Scenario 3: MAJOR ISSUES

```
Phase 7.5: LaTeX Quality Gate

Compilation: ✅ PASS
Pages: 28.5 (target: <28) ❌ OVER LIMIT

Blank Space Check: ⚠️ ISSUES FOUND
1. Page 5: Large blank (8 inches) after Figure 2
2. Page 12: Half-page blank before Section 4
3. Page 18: Large gap (4 inches) around Table 3
   Total wasted space: ~1.5 pages

Text Overflow Check: ⚠️ ISSUES FOUND
1. Lines 342, 567, 789: Overfull hbox (URLs)
2. Table 3, Table 5: Exceed margins
3. Equation (12): Extends into margin

Page Break Check: ⚠️ ISSUES FOUND
1. Page 7: Orphan section header
2. Page 15: Split figure caption

Overall Verdict: 🛑 MAJOR ISSUES - Must revise before Phase 8

Priority Fixes:
1. **CRITICAL**: Reduce page count to ≤28 pages
   - Fix blank space issues (saves ~1.5 pages)
   - This will bring total to 27 pages ✅

2. **HIGH**: Fix text overflow issues
   - Affects professional appearance
   - 6 issues to address

3. **MEDIUM**: Fix page break issues
   - Affects readability
   - 2 issues to address

Estimated time to fix: 30-45 minutes

@writer: Please address ALL issues listed above. Focus on blank space consolidation first to get under 28-page limit, then fix overflow and page break issues. Resubmit for Phase 7.5 re-check when complete.
```

---

## Revision Loop Protocol

### Standard Flow
1. @editor provides detailed feedback
2. @writer implements fixes
3. @writer recompiles (`pdflatex paper.tex` twice)
4. @writer reports to @director: "Phase 7.5 revisions complete"
5. @director → @editor for re-check
6. @editor re-runs all 4 checks
7. **If PASS**: Proceed to Phase 8
8. **If ISSUES**: Repeat steps 1-7 (max 3 iterations)

### Maximum Iterations
- **Iteration 1**: Full detailed feedback
- **Iteration 2**: Re-check with focus on remaining issues
- **Iteration 3**: Final attempt
- **After 3 failures**: Rewind to Phase 7 (major restructuring needed)

### Tracking Iterations
```
Phase 7.5 Re-Check (Iteration 2):

Previous Issues:
1. ✅ FIXED: Blank space on page 12
2. ✅ FIXED: URL overflow on line 567
3. ❌ NOT FIXED: Table 5 still exceeds margins

New Issues:
4. ⚠️ NEW: Page 15 now has widow line (side effect of fixing blank space)

Remaining: 2 issues
Progress: 66% (2/3 original issues fixed)

Verdict: ⚠️ MINOR ISSUES - Fix 2 remaining items
```

---

## Quick Reference Checklist

### Pre-Check Setup
- [ ] Navigate to `output/paper/`
- [ ] Compile: `pdflatex paper.tex` (twice)
- [ ] Verify PDF created
- [ ] Open PDF for visual inspection
- [ ] Open `paper.log` for warning check

### During Check
- [ ] **Check 1**: Compilation success (errors in log?)
- [ ] **Check 2**: Blank space (visual scan of all pages)
- [ ] **Check 3**: Text overflow (grep log for "Overfull")
- [ ] **Check 4**: Page breaks (scan page transitions)

### Post-Check
- [ ] Categorize issues by priority (CRITICAL/HIGH/MEDIUM/LOW)
- [ ] Provide specific fixes for each issue
- [ ] Estimate fix time
- [ ] Provide clear verdict (PASS/MINOR/MAJOR)

---

## Summary

**Purpose**: Ensure paper has professional LaTeX formatting quality.

**Key Checks**: Compilation + Blank Space + Text Overflow + Page Breaks

**Success Criteria**: Paper compiles cleanly, uses page space efficiently, respects margins, and has good page break quality.

**Editor Role**: Quality gatekeeper preventing poorly formatted papers from proceeding to Phase 8.
