# O-Prize MCM Paper Page Allocation Analysis

**Analysis Date:** 2026-01-30
**Sample Size:** 8 O-Prize winning papers (2020-2022, Problems A-D)
**Purpose:** Determine realistic page budgets for Phase 7 sub-phases based on actual O-Prize papers

---

## Executive Summary

Analysis of 8 randomly sampled O-Prize papers reveals that successful MCM papers allocate approximately:
- **39% to Model Development** (11 pages)
- **25% to Results/Validation** (7 pages)
- **14% to Sensitivity/Strengths/Weaknesses** (4 pages)
- **11% to Introduction** (3 pages)
- **11% to References/Appendix** (3 pages)

**Key Finding:** O-Prize papers prioritize mathematical model development and validation over lengthy introductions or discussions.

---

## Sample Papers Analyzed

| Paper ID | Year-Problem | Total Pages* | Intro | Model | Results | Sensitivity | Conclusion | Refs | Appendix |
|---|---|---|---|---|---|---|---|---|---|
| 2021A-2100454 | 2021-A | 24 | 4 | 7 | 6 | 2 | 1 | 1 | 2 |
| 2020B-2007698 | 2020-B | 29 | 2 | 13 | 10 | 1 | 2 | 1 | 0 |
| 2021B-2102199 | 2021-B | 24 | 3 | 9 | 3 | 2 | 1 | 1 | 5 |
| 2021C-2101166 | 2021-C | 24 | 3 | 11 | 3 | 2 | 1 | 1 | 3 |
| 2022A-2200289 | 2022-A | 24 | 3 | 10 | 0** | 4 | 2 | 1 | 4 |
| 2020C-2002116 | 2020-C | 38 | 1 | 12 | 15 | 4 | 2 | 1 | 3 |
| 2020D-2002526 | 2020-D | 23 | 3 | 10 | 5 | 2 | 1 | 1 | 1 |
| 2020A-2001334 | 2020-A | 30 | 2 | 12 | 10 | 2 | 2 | 1 | 1 |

\* Excluding summary sheet
\*\* Results integrated within model sections

---

## Statistical Summary

### Average Page Allocation

| Section Type | Average Pages | Percentage of Total | Range |
|---|---|---|---|
| Introduction + Background | 2.6 | 9.7% | 1-4 pages |
| Model Formulation | 10.5 | 38.9% | 7-13 pages |
| Results + Analysis | 6.5 | 24.1% | 0-15 pages |
| Sensitivity Analysis | 2.4 | 8.8% | 1-4 pages |
| Conclusion + Strengths/Weaknesses | 1.5 | 5.6% | 1-2 pages |
| References | 1.0 | 3.7% | 1 page |
| Appendix (Code/Tables) | 2.4 | 8.8% | 0-5 pages |
| **TOTAL** | **27.0** | **100%** | **23-38 pages** |

---

## Recommended Page Budgets for 28-Page System

Based on the analysis, here are the recommended allocations for a standard 28-page MCM paper (excluding summary sheet):

### Section-Level Budget

| Section Type | Recommended Pages | Percentage | Notes |
|---|---|---|---|
| **Introduction + Background** | 3 | 10.7% | Problem context, literature review, assumptions |
| **Model Formulation** | 11 | 39.3% | Mathematical development, algorithms, equations |
| **Results + Validation** | 7 | 25.0% | Simulations, figures, validation, analysis |
| **Sensitivity Analysis** | 2 | 7.1% | Parameter testing, robustness checks |
| **Conclusion + S/W** | 2 | 7.1% | Strengths, weaknesses, future work |
| **References** | 1 | 3.6% | Bibliography |
| **Appendix** | 2 | 7.1% | Code, supplementary tables |
| **TOTAL** | **28** | **100%** | **Excluding summary sheet** |

---

## Phase 7 Sub-Phase Recommendations

Mapping the analysis to MCM-Killer's Phase 7 structure:

| Phase | Description | Target Pages | Percentage | Key Components |
|---|---|---|---|---|
| **Phase 7A** | Abstract + Introduction + Notation | **3 pages** | 10.7% | • 1-page abstract<br>• Problem restatement<br>• Background (0.5-1 pg)<br>• Assumptions (0.5 pg)<br>• Notation table (0.5 pg) |
| **Phase 7B** | Model Development | **11 pages** | 39.3% | • Model overview (1 pg)<br>• Model 1 formulation (3-4 pg)<br>• Model 2 formulation (3-4 pg)<br>• Model 3 (if applicable, 2-3 pg)<br>• Integration/framework (1 pg) |
| **Phase 7C** | Results + Validation | **7 pages** | 25.0% | • Simulation setup (1 pg)<br>• Results presentation (4-5 pg)<br>• Validation/verification (1-2 pg)<br>• Figures and tables (integrated) |
| **Phase 7D** | Sensitivity + Strengths/Weaknesses | **4 pages** | 14.3% | • Sensitivity analysis (2 pg)<br>• Strengths (1 pg)<br>• Weaknesses (0.5 pg)<br>• Conclusion (0.5 pg) |
| **Phase 7E** | Discussion/Conclusion | **Integrated into 7D** | — | Merged with strengths/weaknesses |
| **References + Appendix** | Supporting Materials | **3 pages** | 10.7% | • References (1 pg)<br>• Code listings (1-2 pg)<br>• Supplementary tables (0-1 pg) |
| | **TOTAL** | **28 pages** | **100%** | **Plus 1-page summary sheet** |

---

## Key Insights from O-Prize Papers

### 1. Model Section Dominance (39% of paper)

O-Prize papers dedicate nearly **40% of content to model development**. This includes:
- Detailed mathematical formulations
- Algorithm descriptions
- Equation derivations
- Subsystem integration

**Implication:** Teams should not skimp on model detail. Judges want to see rigorous mathematical development.

### 2. Results Integration Pattern

Results sections vary widely (0-15 pages, avg 6.5):
- Some papers (like 2022A-2200289) integrate results directly into model sections
- Others (like 2020C-2002116) have extensive standalone results sections
- **Focus on validation and visualization** over narrative discussion
- Figures and tables are critical—not just numbers

**Implication:** Results should emphasize visual evidence and validation metrics, not lengthy textual analysis.

### 3. Compact Introduction (10% of paper)

Successful papers average only **2.6 pages for introduction**:
- Papers "get to the models quickly"
- Background is problem-focused and concise
- No extensive literature reviews
- Assumptions are listed efficiently

**Implication:** Don't over-invest in introduction. Judges want to see the math.

### 4. Sensitivity Analysis is Critical (9% of paper)

All O-Prize papers include sensitivity analysis:
- Average 2.4 pages dedicated specifically to sensitivity
- Tests robustness of key parameters
- Often includes graphical analysis
- Demonstrates model reliability

**Implication:** Phase 7D (Sensitivity) is non-negotiable for O-Prize consideration.

### 5. Strengths/Weaknesses as Scholarship Signal (6% of paper)

Successful papers dedicate 1.5 pages to reflection:
- Honest assessment of limitations
- Clear articulation of strengths
- Future work suggestions
- Demonstrates critical thinking and maturity

**Implication:** Teams should critically evaluate their own work—judges value self-awareness.

### 6. Page Count Sweet Spot

- **Range:** 23-38 pages (excluding summary)
- **Mode:** 24 pages (4 papers)
- **Target:** 27-28 pages is optimal
- Papers under 25 pages may lack depth
- Papers over 30 pages may include redundancy

### 7. Appendix Usage Varies Widely (0-5 pages)

- Some papers have no appendix (2020B)
- Others include extensive code/tables (2021B: 5 pages)
- Average: 2.4 pages
- Typically contains:
  - Python/MATLAB code
  - Supplementary data tables
  - Extended derivations

**Implication:** Use appendix for supplementary material that supports but doesn't interrupt main narrative.

---

## Operational Recommendations for MCM-Killer System

### Phase 7A: Abstract + Introduction (3 pages)

**Time allocation:** 4 hours
**Page budget:** 3 pages

| Component | Pages | Notes |
|---|---|---|
| Abstract | 1.0 | Full 1-page summary |
| Problem Restatement | 0.3 | Brief, focused |
| Background/Motivation | 0.8 | Problem context only |
| Assumptions | 0.4 | Bullet list format |
| Notation Table | 0.5 | Symbols and definitions |

**Quality check:**
- Can a judge understand the problem and approach in 3 minutes?
- Are assumptions clearly justified?
- Is notation table complete but concise?

### Phase 7B: Model Development (11 pages)

**Time allocation:** 10-12 hours
**Page budget:** 11 pages

| Component | Pages | Notes |
|---|---|---|
| Model Overview/Framework | 1.0 | High-level architecture |
| Model 1 (Primary) | 4.0 | Full derivation + equations |
| Model 2 (Secondary) | 4.0 | Full derivation + equations |
| Model 3 (If needed) | 1.5 | Simplified presentation |
| Integration/Workflow | 0.5 | How models connect |

**Quality check:**
- Are equations numbered and referenced?
- Is mathematical notation consistent with Phase 7A table?
- Are assumptions for each sub-model stated?
- Can a mathematical peer reproduce the model?

### Phase 7C: Results + Validation (7 pages)

**Time allocation:** 6-8 hours
**Page budget:** 7 pages

| Component | Pages | Notes |
|---|---|---|
| Experimental Setup | 1.0 | Parameters, data sources |
| Results Presentation | 4.0 | Figures, tables, interpretation |
| Validation/Verification | 1.5 | Accuracy metrics, comparisons |
| Edge Cases/Scenarios | 0.5 | Unusual conditions tested |

**Quality check:**
- Are figures publication-quality with clear captions?
- Is validation against real data or benchmarks?
- Are results explained, not just shown?

### Phase 7D: Sensitivity + Strengths/Weaknesses (4 pages)

**Time allocation:** 4-5 hours
**Page budget:** 4 pages

| Component | Pages | Notes |
|---|---|---|
| Sensitivity Analysis | 2.0 | Parameter variation tests |
| Model Strengths | 1.0 | What the model does well |
| Model Weaknesses | 0.5 | Honest limitations |
| Conclusion | 0.5 | Summary and future work |

**Quality check:**
- Are at least 3-5 key parameters tested for sensitivity?
- Are weaknesses honest but constructive?
- Does conclusion tie back to original problem?

### References + Appendix (3 pages)

**Time allocation:** 2 hours
**Page budget:** 3 pages

| Component | Pages | Notes |
|---|---|---|
| References | 1.0 | 15-25 citations, formatted |
| Code Listings | 1.5 | Key algorithms only |
| Supplementary Tables | 0.5 | Extended data |

**Quality check:**
- Are all citations properly formatted?
- Is code commented and readable?
- Does appendix add value without being cluttered?

---

## Validation Against MCM Rules

### Official MCM Requirements

- **Maximum:** 25 pages for solution paper (excluding summary sheet, references, appendices)
- **Summary Sheet:** 1 page (not counted in 25-page limit)
- **References:** Unlimited (not counted in 25-page limit)
- **Appendices:** Unlimited (not counted in 25-page limit)

### Our 28-Page Budget Breakdown

| Section | Pages | Counts Toward Limit? |
|---|---|---|
| Introduction | 3 | ✓ Yes |
| Model Development | 11 | ✓ Yes |
| Results/Validation | 7 | ✓ Yes |
| Sensitivity + S/W | 4 | ✓ Yes |
| **MAIN CONTENT SUBTOTAL** | **25** | **Within limit** |
| Summary Sheet | 1 | ✗ No (separate requirement) |
| References | 1 | ✗ No (unlimited) |
| Appendix | 2 | ✗ No (unlimited) |
| **TOTAL PAPER** | **29** | **Compliant** |

**Note:** Our 28-page budget (excluding summary) includes references and appendix. The **core content is 25 pages**, perfectly aligned with MCM rules.

---

## Comparison: Theoretical vs. Actual O-Prize Allocation

| Section | Theoretical "Ideal" | O-Prize Reality | Difference |
|---|---|---|---|
| Introduction | 15% (4-5 pages) | 10% (3 pages) | **-5%** |
| Model | 30% (8 pages) | 39% (11 pages) | **+9%** |
| Results | 25% (7 pages) | 25% (7 pages) | Same |
| Sensitivity | 5% (1-2 pages) | 9% (2-3 pages) | **+4%** |
| Conclusion | 10% (2-3 pages) | 6% (2 pages) | **-4%** |

**Key Insight:** O-Prize papers invest **more in models and sensitivity**, and **less in introduction and conclusion** than theoretical guidelines suggest. This aligns with MCM's emphasis on mathematical rigor.

---

## Risk Factors and Adjustments

### If Running Out of Space (>25 pages)

**Priority cuts:**
1. **Introduction:** Reduce from 3 → 2 pages (cut background detail)
2. **Appendix:** Move extensive code to online repository, cite link
3. **Results:** Consolidate figures, use multi-panel layouts
4. **Model:** Tighten notation, move derivations to appendix

**DO NOT cut:**
- Sensitivity analysis
- Model formulation core equations
- Validation results
- Strengths/weaknesses

### If Under Page Budget (<22 pages)

**Priority additions:**
1. **Results:** Add more test cases, edge scenarios
2. **Sensitivity:** Expand parameter sweep analysis
3. **Model:** Add more derivation detail or subsystem explanation
4. **Validation:** Include comparison with alternative approaches

**DO NOT pad with:**
- Redundant text
- Overly large figures
- Excessive background literature
- Repetitive conclusions

---

## Phase 7 Timeline with Page Budgets

| Phase | Duration | Page Target | Key Deliverable |
|---|---|---|---|
| **Phase 7A** | Hours 48-52 (4h) | 3 pages | Abstract + Introduction complete |
| **Phase 7B** | Hours 52-64 (12h) | 11 pages | All models formulated |
| **Phase 7C** | Hours 64-72 (8h) | 7 pages | Results visualized and validated |
| **Phase 7D** | Hours 72-76 (4h) | 4 pages | Sensitivity + S/W complete |
| **Phase 7E** | Hours 76-78 (2h) | Integrated | Final polish and conclusion |
| **Phase 7F** | Hours 78-80 (2h) | 3 pages | References + appendix finalized |
| **Buffer** | Hours 80-84 (4h) | — | Final proofreading and formatting |

**Total:** 36 hours for Phase 7 (within 48-hour contest window after 12h break post-Phase 6)

---

## Conclusion

This analysis of 8 O-Prize papers (2020-2022) reveals that successful MCM teams:

1. **Prioritize mathematical rigor** (39% to models)
2. **Validate thoroughly** (25% to results)
3. **Keep introductions concise** (11% only)
4. **Include robust sensitivity analysis** (9%)
5. **Reflect critically on limitations** (6%)

The recommended **28-page budget** (25 pages main content + 1 summary + 2 refs/appendix) aligns with:
- MCM official rules (25-page limit for main content)
- Observed O-Prize paper lengths (avg 27 pages)
- MCM-Killer's phase structure

**For Phase 7 planning:** Teams should allocate time proportionally:
- **42% of time** → Model development (Phase 7B)
- **28% of time** → Results/validation (Phase 7C)
- **14% of time** → Sensitivity/S&W (Phase 7D)
- **16% of time** → Introduction, refs, polish (Phases 7A, 7E, 7F)

This evidence-based allocation maximizes alignment with actual O-Prize winning strategies.

---

**Document Version:** 1.0
**Data Source:** D:\MCM-Killer\MCM-Killer\student paper (2020-2022)
**Analysis Script:** D:\MCM-Killer\MCM-Killer\analyze_papers.py
