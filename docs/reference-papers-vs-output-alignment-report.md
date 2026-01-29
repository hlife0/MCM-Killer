# Reference Papers vs Output Alignment Report

**Date**: 2026-01-29
**Project**: MCM 2025 Problem C - Olympic Medal Tables
**Purpose**: Identify misalignment between reference_papers and output directories, provide remediation plan

---

## Executive Summary

**Critical Issues Found**: 6
**Alignment Gap**: HIGH - Multiple versions, data inconsistencies, missing results
**Estimated Fix Time**: 2-3 hours
**Submission Risk**: HIGH - Must resolve before competition submission

---

## Directory Structure Overview

### Reference Papers (`workspace/2025_C/reference_papers/`)
- **Count**: 44 PDF files (O-Award winning papers from previous competitions)
- **Purpose**: Gold standard for methodology, style, presentation
- **Naming**: Numeric IDs (e.g., 2009116.pdf, 2401445.pdf, 2406176.pdf, 2318036.pdf)
- **Usage**: Studied by @judge_zero for calibration during mock judging

### Output (`workspace/2025_C/output/`)
- **Status**: Complete MCM workflow execution (22 phases)
- **Paper**: Multiple versions (6 PDFs)
- **Results**: Inconsistent between paper and CSV files
- **Score**: 87/100 (MINOR_REVISION verdict)

---

## Problem 1: Multiple Paper Versions (CRITICAL)

### Issue
**Location**: `output/paper/`
**Files**:
```
paper.pdf                  (3,318,969 bytes) - Original 50-page version
paper_final.pdf            (2,936,008 bytes) - Attempted final version
paper_no_survival.pdf      (2,935,993 bytes) - Survival removed
paper_polished.pdf         (2,208,240 bytes) - Condensed version
paper_revised.pdf          (2,935,993 bytes) - Post-judgment revision
paper_revised_fixed.pdf    (2,936,008 bytes) - Latest version
```

### Root Cause
1. **Phase 7F**: Original compilation → paper.pdf (50 pages)
2. **Phase 9 (Polish)**: Condensed to 18 pages → paper_polished.pdf
3. **Post-Polish**: Survival analysis added back → expanded to 50 pages
4. **Phase 9.1 (Mock Judgment)**: Issues found → created paper_revised.pdf
5. **Post-Judgment**: Fixed survival removal → paper_revised_fixed.pdf

### Alignment Gap
- **Reference papers**: Each competition has ONE final submission PDF
- **Output**: 6 PDF versions with unclear which is "final"
- **Risk**: Submitting wrong version, confusion about authoritative source

### Solution
1. **Identify canonical version**: `paper_revised_fixed.pdf` (latest, post-judgment fixes)
2. **Create `paper_SUBMISSION.pdf`**: Rename canonical version with clear naming
3. **Archive drafts**: Move other versions to `output/paper/drafts/` subdirectory
4. **Update VERSION_MANIFEST.json**: Add "submission_version" field

**Action Items**:
```bash
cd output/paper
mkdir drafts
mv paper.pdf paper_final.pdf paper_no_survival.pdf paper_polished.pdf paper_revised.pdf drafts/
mv paper_revised_fixed.pdf paper_SUBMISSION.pdf
```

---

## Problem 2: Data Consistency (CRITICAL)

### Issue
**Location**: `output/paper/paper_revised_fixed.tex` vs `output/results/results_1.csv`

### Specific Inconsistencies
| Country | Paper Value | CSV Value | Discrepancy |
|---------|-------------|-----------|-------------|
| China Gold | "25.4 [14.5, 42.3]" | "25.27 [14.04, 42.23]" | Rounding + interval width |
| China Total | "72.7 [40.8, 119.9]" | "70.65 [39.63, 115.69]" | ~2 medal difference |
| USA Gold | "57.8 [52.3, 63.4]" | "57.81 [52.31, 63.41]" | Minor rounding |

### Root Cause
1. **Paper written**: Values copied from quick training (results_quick_1.csv)
2. **Full training completed**: results_1.csv generated with slight differences
3. **Paper not updated**: Original values remained in LaTeX

### Alignment Gap
- **Reference papers**: All table values match source data exactly
- **Output**: Judges verifying calculations would find discrepancies
- **Risk**: Credibility damage, automatic verification failures

### Solution
**Option A**: Update paper.tex to match CSV values (RECOMMENDED)
- Search/replace all forecast values in paper.tex
- Re-compile to new PDF
- Verify all figures use updated values

**Option B**: Regenerate CSV from paper values (NOT RECOMMENDED)
- Would require re-running training
- Time-intensive
- Risk of new inconsistencies

**Action Items**:
1. Extract all forecast values from results_1.csv
2. Find/replace in paper_revised_fixed.tex:
   ```latex
   % OLD
   China & 25.4 & [14.5, 42.3] & 72.7 & [40.8, 119.9] \\
   % NEW
   China & 25.3 & [14.0, 42.2] & 70.7 & [39.6, 115.7] \\
   ```
3. Recompile LaTeX
4. Verify figures regenerate with correct values

---

## Problem 3: Missing Model 3C Results (HIGH)

### Issue
**Location**: `output/paper/paper_revised_fixed.tex` Section 5.3.3 (lines 414-439)
**Claim**: "Europe: 4.2 cycles to first medal, Africa: 9.4 cycles"
**Evidence**: results_quick_3c.csv exists (9,260 bytes)
**Missing**: results_3c.csv (full training output)

### File Status
```
output/results/results_1.csv         ✅ Exists (15,562 bytes)
output/results/results_2.csv         ✅ Exists (9,097 bytes)
output/results/results_3c.csv        ❌ MISSING
output/results_quick/results_quick_3c.csv  ✅ Exists (9,260 bytes)
```

### Root Cause
1. **Phase 5A**: Quick training generated results_quick_3c.csv
2. **Phase 5B**: Full training incomplete for Model 3C (survival analysis)
3. **Paper written**: Used quick results for survival section
4. **Post-judgment**: Survival removed from some versions but not others

### Alignment Gap
- **Reference papers**: All claims backed by data files or appendices
- **Output**: Survival analysis claims with no full results file
- **Risk**: Judges request supporting data → cannot provide

### Solution
**Option A**: Remove survival analysis entirely (CURRENT STATUS)
- ✅ Already done in paper_revised_fixed.tex (via remove_survival_final.py)
- ✅ Reduces page count from 50 to 45
- ⚠️ Still exceeds 25-page limit

**Option B**: Generate full results_3c.csv (NOT RECOMMENDED)
- Requires re-running Model 3C training
- Time-intensive (1-2 hours)
- Adds back pages already removed

**Verification Required**:
```bash
# Check if survival sections exist in paper_revised_fixed.tex
grep -n "survival\|3\.3\|cycles" output/paper/paper_revised_fixed.tex
```

---

## Problem 4: Page Count Exceeded (HIGH)

### Issue
**Current Status**: 45 pages (paper_revised_fixed.pdf)
**Competition Limit**: 25 pages (MCM/ICM standard)
**Overage**: 20 pages (80% over limit)

### Page Count by Version
| Version | Pages | Status |
|---------|-------|--------|
| paper.pdf | ~50 | Original |
| paper_polished.pdf | ~18 | Under limit ⚠️ too short |
| paper_revised_fixed.pdf | ~45 | Over limit ❌ |

### Root Cause
1. **Phase 9 polish**: Aggressive condensation to 18 pages
2. **Post-polish decision**: Survival analysis added back (re-expanding to 45)
3. **Trade-off misjudgment**: Prioritized content over page limit

### Alignment Gap
- **Reference papers**: All within 17-25 page range (O-Award winners)
- **Output**: 45 pages = automatic DQ risk
- **Risk**: Judges may reject for page limit violation

### Solution
**Target**: Reduce to ≤25 pages (40% reduction)

**Condensation Strategy** (from editing_notes.md):
1. ✅ Assumptions: Condensed from 8 → 1 page
2. ✅ Data section: Reduced from 3 → 0.5 pages
3. ✅ Sensitivity Analysis: Reduced from 6 → 1.5 pages
4. ❌ Survival analysis: Should remain removed
5. **Additional needed**:
   - Bibliography: 18 → 12 refs (done)
   - Discussion: 4 → 1.5 pages
   - Remove redundant figures: 12 → 6 figures

**Action Items**:
1. **Revert to paper_polished.tex** (18 pages) as base
2. **Add back ONLY essential content**:
   - Critical equations (all 3 models)
   - Key results tables (2028 forecasts)
   - 6 best figures (top 10, zero-inflation, sport specialization, etc.)
3. **Use appendices**: Non-essential content (full assumptions, sensitivity tables) → appendix (doesn't count toward page limit)
4. **Target**: 22-24 pages with appendix

**Alternative**: Use `paper_polished.tex` but add survival summary (1-2 paragraphs, no full section)

---

## Problem 5: Figure Caption Inconsistency (MEDIUM)

### Issue
**Location**: Table 2 vs Figure 1
**Problem**: Table shows China "70.7 total", Figure shows different values

### Root Cause
1. **Figure generated**: From results_quick_1.csv (earlier training run)
2. **Table updated**: With results_1.csv values (later training run)
3. **Regeneration missed**: Figure PNG not recreated with new data

### Alignment Gap
- **Reference papers**: All figures match corresponding tables exactly
- **Output**: Visual inconsistencies create confusion
- **Risk**: Judges cross-referencing → find discrepancies

### Solution
1. **Regenerate all figures** from results_1.csv:
   ```bash
   cd output/figures
   python create_visualizations.py  # Rerun with latest results
   ```
2. **Verify**: Figure 1 values match Table 2 exactly
3. **Recompile**: LaTeX with updated figures

---

## Problem 6: File Naming Convention (MEDIUM)

### Issue
**Location**: All output directories
**Current naming**:
```
results_1.csv, results_2.csv, results_3c.csv (missing)
results_quick_1.csv, results_quick_2.csv, results_quick_3a.csv, results_quick_3c.csv
```

### Alignment Gap
- **Reference papers**: Clear, systematic naming
- **Output**: Inconsistent prefixes (results_ vs results_quick_)
- **Risk**: Confusion about which files are "final" vs "intermediate"

### Solution
**Reorganize with clear structure**:
```
output/
├── results/
│   ├── final/
│   │   ├── model_1_forecasts_2028.csv        (Canonical)
│   │   ├── model_2_first_time_odds.csv       (Canonical)
│   │   └── model_3_integrated_analysis.csv   (Canonical)
│   ├── quick/                                (Intermediate, Phase 5A)
│   └── traces/                               (MCMC trace files)
```

**Renaming Script**:
```bash
cd output/results
mkdir final quick traces
mv results_1.csv final/model_1_forecasts_2028.csv
mv results_2.csv final/model_2_first_time_odds.csv
mv results_quick_*.csv quick/
mv trace_1.nc traces/
```

---

## Summary of Required Actions

### Priority 1: Critical (Must Fix)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | Consolidate to single submission PDF | 5 min | Eliminates version confusion |
| 2 | Update paper.tex values to match CSV | 30 min | Data consistency |
| 3 | Reduce page count to ≤25 | 60 min | Avoid DQ |
| 4 | Regenerate figures from final CSV | 15 min | Visual consistency |

**Total Priority 1**: ~110 minutes (1.8 hours)

### Priority 2: High (Should Fix)

| # | Action | Effort | Impact |
|---||--------|--------|--------|
| 5 | Reorganize results directory structure | 15 min | Clarity |
| 6 | Update VERSION_MANIFEST.json | 10 min | Documentation |

**Total Priority 2**: ~25 minutes

### Priority 3: Medium (Nice to Fix)

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 7 | Add missing references to bibliography | 15 min | Academic polish |
| 8 | Enhance figure captions (Protocol 15) | 20 min | Presentation |

**Total Priority 3**: ~35 minutes

---

## Alignment Checklist

### vs. Reference Papers Standards

| Criterion | Reference Papers | Current Output | Gap | Action |
|-----------|-----------------|----------------|-----|--------|
| **Single PDF** | 1 submission file | 6 PDF versions | ❌ | Consolidate to 1 |
| **Page Count** | 17-25 pages | 45 pages | ❌ | Reduce to ≤25 |
| **Data Consistency** | Tables match source | Table/CSV mismatch | ❌ | Update LaTeX values |
| **Figure Alignment** | Figures match tables | Figure/table mismatch | ❌ | Regenerate figures |
| **Results Files** | All claims backed | Missing results_3c.csv | ⚠️ | Remove survival claims |
| **File Organization** | Clear structure | Mixed naming | ⚠️ | Reorganize |
| **Bibliography** | 12-20 references | 10 references | ⚠️ | Add 2-3 refs |
| **Visual Quality** | Professional figures | 12 figures, good quality | ✅ | No change needed |

---

## Recommended Workflow

### Step 1: Prepare Clean Workspace (5 min)
```bash
cd workspace/2025_C/output/paper
mkdir drafts
mv paper.pdf paper_final.pdf paper_no_survival.pdf paper_polished.pdf paper_revised.pdf drafts/
```

### Step 2: Fix Data Consistency (30 min)
1. Extract values from `results/results_1.csv`
2. Find/replace in `paper_revised_fixed.tex`
3. Recompile: `pdflatex paper_revised_fixed.tex`

### Step 3: Regenerate Figures (15 min)
```bash
cd output/figures
python create_visualizations.py  # Uses latest results_1.csv
```

### Step 4: Reduce Page Count (60 min)
1. Use `paper_polished.tex` (18 pages) as starting point
2. Add back ONLY essential content from paper_revised_fixed.tex:
   - Critical equations
   - 2028 forecast tables
   - 6 best figures
3. Move non-essentials to appendix
4. Target: 22-24 pages

### Step 5: Final Compilation and Verification (10 min)
```bash
pdflatex paper_final_SUBMISSION.tex
bibtex paper_final_SUBMISSION
pdflatex paper_final_SUBMISSION.tex
pdflatex paper_final_SUBMISSION.tex
```

### Step 6: Organize Results Directory (15 min)
```bash
cd output/results
mkdir final quick traces
mv results_1.csv final/model_1_forecasts_2028.csv
mv results_2.csv final/model_2_first_time_odds.csv
mv results_quick_*.csv quick/
mv trace_1.nc traces/
```

---

## Post-Alignment Verification Checklist

- [ ] **Single submission PDF**: `paper_SUBMISSION.pdf` exists
- [ ] **Page count**: ≤25 pages (verify with PDF page count)
- [ ] **Data consistency**: All table values match CSV files
- [ ] **Figure alignment**: Figure values match table values
- [ ] **No survival section**: Removed from paper.tex
- [ ] **Figures regenerate**: All use latest results_1.csv
- [ ] **Bibliography**: 12+ references
- [ ] **VERSION_MANIFEST updated**: Submission version documented
- [ ] **Drafts archived**: Old versions moved to `drafts/`
- [ ] **Results organized**: Clear final/quick/traces structure

---

## Conclusion

**Current Alignment Status**: ⚠️ **SIGNIFICANT MISALIGNMENT**

**Primary Issues**:
1. Multiple PDF versions with unclear submission candidate
2. Data inconsistencies between paper and source files
3. Page count severely exceeds limit (45 vs 25 pages)
4. Missing results files for some claims

**Alignment Path**:
- **Time Required**: ~2-3 hours
- **Difficulty**: MEDIUM (straightforward but time-consuming)
- **Risk Reduction**: HIGH → Submission competitive after fixes

**Final Recommendation**:
Execute Priority 1 actions (1.8 hours) before submission. The paper methodology is strong (87/100), but presentation issues must be resolved to match reference paper standards.

---

**Next Steps**:
1. Execute consolidation script (see Step 1 above)
2. Run data consistency fix (Step 2)
3. Regenerate figures (Step 3)
4. Reduce page count (Step 4) - MOST CRITICAL
5. Final verification (Step 5-6)

**Estimated Completion**: 2-3 hours
**Submission Readiness**: After Priority 1 fixes complete
