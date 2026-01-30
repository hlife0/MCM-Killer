# Phase 7 Quick Reference: Page Budget Allocator

**Based on O-Prize Paper Analysis (2020-2022, n=8)**

---

## 🎯 Target: 28-Page Paper Structure

```
┌─────────────────────────────────────────────────────────────┐
│ SUMMARY SHEET (1 page) - NOT counted in 25-page limit      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ MAIN CONTENT (25 pages) - COUNTED in limit                 │
│                                                             │
│  Phase 7A: Introduction          [3 pages]  10.7%          │
│  Phase 7B: Models                [11 pages] 39.3%  ████████│
│  Phase 7C: Results               [7 pages]  25.0%  █████   │
│  Phase 7D: Sensitivity + S/W     [4 pages]  14.3%  ███     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ REFERENCES (1 page) - NOT counted in limit                 │
│ APPENDIX (2 pages) - NOT counted in limit                  │
└─────────────────────────────────────────────────────────────┘

Total visible pages: 29 (1 summary + 25 main + 1 refs + 2 appendix)
Complies with MCM 25-page limit: ✓ YES
```

---

## 📊 Page Budget Breakdown by Phase

| Phase | Section | Pages | Time | % | Priority | Quality Check |
|---|---|---|---|---|---|---|
| **7A** | Abstract | 1.0 | 1h | 3.6% | CRITICAL | Standalone readability |
| | Intro + Background | 1.0 | 1h | 3.6% | HIGH | Problem clarity |
| | Assumptions | 0.5 | 0.5h | 1.8% | HIGH | Justification |
| | Notation | 0.5 | 0.5h | 1.8% | MEDIUM | Completeness |
| | **7A Subtotal** | **3** | **3h** | **10.7%** | | |
| **7B** | Model Overview | 1.0 | 1h | 3.6% | HIGH | Architecture clarity |
| | Model 1 | 4.0 | 4h | 14.3% | CRITICAL | Full derivation |
| | Model 2 | 4.0 | 4h | 14.3% | CRITICAL | Full derivation |
| | Model 3 (if any) | 1.5 | 1.5h | 5.4% | MEDIUM | Integration |
| | Integration | 0.5 | 0.5h | 1.8% | MEDIUM | Workflow |
| | **7B Subtotal** | **11** | **11h** | **39.3%** | | |
| **7C** | Setup/Parameters | 1.0 | 1h | 3.6% | HIGH | Reproducibility |
| | Results (figures) | 4.0 | 4h | 14.3% | CRITICAL | Visual quality |
| | Validation | 1.5 | 1.5h | 5.4% | CRITICAL | Metrics |
| | Edge cases | 0.5 | 0.5h | 1.8% | MEDIUM | Coverage |
| | **7C Subtotal** | **7** | **7h** | **25.0%** | | |
| **7D** | Sensitivity Tests | 2.0 | 2h | 7.1% | CRITICAL | Parameter sweep |
| | Strengths | 1.0 | 1h | 3.6% | HIGH | Honesty |
| | Weaknesses | 0.5 | 0.5h | 1.8% | HIGH | Self-awareness |
| | Conclusion | 0.5 | 0.5h | 1.8% | MEDIUM | Synthesis |
| | **7D Subtotal** | **4** | **4h** | **14.3%** | | |
| **Refs** | Bibliography | 1.0 | 0.5h | 3.6% | MEDIUM | Formatting |
| **App** | Code/Tables | 2.0 | 1.5h | 7.1% | LOW | Readability |
| | | | | | | |
| **TOTAL** | | **28** | **27h** | **100%** | | |

---

## ⚡ Phase-by-Phase Checklist

### Phase 7A: Introduction (3 pages, 3 hours)

**Page allocation:**
- [ ] Abstract: 1 page (full page summary)
- [ ] Introduction body: 1 page (context + motivation)
- [ ] Assumptions: 0.5 pages (bullet list)
- [ ] Notation table: 0.5 pages (symbols defined)

**Exit criteria:**
- [ ] Can a judge understand problem + approach in 3 minutes?
- [ ] All assumptions justified?
- [ ] Notation table covers all symbols used in Phase 7B?

---

### Phase 7B: Models (11 pages, 11 hours)

**Page allocation:**
- [ ] Overview diagram/framework: 1 page
- [ ] Model 1 (primary): 4 pages
  - [ ] Problem formulation (0.5 pg)
  - [ ] Equations + derivations (2.5 pg)
  - [ ] Algorithm/solution method (1 pg)
- [ ] Model 2 (secondary): 4 pages
  - [ ] Problem formulation (0.5 pg)
  - [ ] Equations + derivations (2.5 pg)
  - [ ] Algorithm/solution method (1 pg)
- [ ] Model 3 (if needed): 1-2 pages
- [ ] Integration/data flow: 0.5 pages

**Exit criteria:**
- [ ] All equations numbered and referenced?
- [ ] Mathematical notation consistent with 7A table?
- [ ] Can a peer reproduce the model from description?
- [ ] Are subsystems clearly connected?

---

### Phase 7C: Results (7 pages, 7 hours)

**Page allocation:**
- [ ] Experimental setup: 1 page (parameters, data sources)
- [ ] Results presentation: 4 pages (figures, tables, interpretation)
  - [ ] Minimum 4-6 high-quality figures
  - [ ] Each figure has descriptive caption
  - [ ] Results interpreted, not just shown
- [ ] Validation/verification: 1.5 pages
  - [ ] Comparison to real data/benchmarks
  - [ ] Accuracy metrics (RMSE, R², etc.)
- [ ] Edge cases/scenarios: 0.5 pages

**Exit criteria:**
- [ ] Figures are publication-quality (300 DPI, clear labels)?
- [ ] Results validated against external data?
- [ ] At least 3 different scenarios/test cases shown?
- [ ] Captions explain what to see in each figure?

---

### Phase 7D: Sensitivity + S/W (4 pages, 4 hours)

**Page allocation:**
- [ ] Sensitivity analysis: 2 pages
  - [ ] Test 3-5 key parameters
  - [ ] Show parameter variation graphs
  - [ ] Discuss robustness
- [ ] Strengths: 1 page
  - [ ] What model does well
  - [ ] Novel contributions
  - [ ] Practical applicability
- [ ] Weaknesses: 0.5 pages
  - [ ] Honest limitations
  - [ ] Simplifying assumptions impact
- [ ] Conclusion: 0.5 pages
  - [ ] Summary of findings
  - [ ] Future work suggestions

**Exit criteria:**
- [ ] At least 3 parameters tested for sensitivity?
- [ ] Weaknesses are honest but constructive?
- [ ] Conclusion ties back to original problem?
- [ ] Demonstrates critical thinking and self-awareness?

---

### References + Appendix (3 pages, 2 hours)

**Page allocation:**
- [ ] References: 1 page (15-25 citations, IEEE or APA format)
- [ ] Code listings: 1-1.5 pages (key algorithms only, commented)
- [ ] Supplementary tables: 0.5-1 pages (extended data)

**Exit criteria:**
- [ ] All in-text citations matched to references?
- [ ] Code is readable and commented?
- [ ] Appendix adds value without clutter?

---

## 🚨 Emergency Adjustments

### If Over 25 Pages (Main Content)

**Cut in this order:**
1. ✂️ Introduction: 3 → 2 pages (trim background)
2. ✂️ Results: 7 → 6 pages (consolidate figures into multi-panels)
3. ✂️ Model details: Move lengthy derivations to appendix
4. ✂️ Edge cases: 0.5 → 0 pages (cut if necessary)

**DO NOT CUT:**
- ❌ Sensitivity analysis
- ❌ Core model equations
- ❌ Validation results
- ❌ Strengths/weaknesses

### If Under 22 Pages (Too Short)

**Add in this order:**
1. ➕ Results: 7 → 9 pages (more test cases, scenarios)
2. ➕ Sensitivity: 2 → 3 pages (more parameter sweeps)
3. ➕ Model: 11 → 12 pages (more derivation detail)
4. ➕ Validation: 1.5 → 2.5 pages (alternative method comparison)

**DO NOT PAD WITH:**
- ❌ Redundant text
- ❌ Overly large figures (use white space efficiently)
- ❌ Excessive background literature

---

## 📈 O-Prize Statistics Reference

**From analysis of 8 O-Prize papers (2020-2022):**

| Metric | Value |
|---|---|
| Average total pages | 27.0 (excluding summary) |
| Page range | 23-38 pages |
| Most common length | 24 pages (4 papers) |
| Model section average | 10.5 pages (38.9%) |
| Results section average | 6.5 pages (24.1%) |
| Introduction average | 2.6 pages (9.7%) |
| Sensitivity average | 2.4 pages (8.8%) |
| Conclusion/S&W average | 1.5 pages (5.6%) |
| Appendix range | 0-5 pages |

**Key insight:** O-Prize papers prioritize **model depth** (39%) over introduction length (10%).

---

## 🎨 Figure Budget Guidelines

Based on O-Prize samples, aim for:

| Section | Figures | Type |
|---|---|---|
| Phase 7A | 0-1 | Problem diagram/framework |
| Phase 7B | 2-3 | Model architecture, flowcharts |
| Phase 7C | 6-8 | Results graphs, validation plots |
| Phase 7D | 2-3 | Sensitivity plots |
| **Total** | **10-15** | **High-quality, captioned** |

**Figure quality checklist:**
- [ ] 300 DPI or vector format (PDF)
- [ ] Clear axis labels with units
- [ ] Legends positioned clearly
- [ ] Captions explain what to observe
- [ ] Consistent color scheme throughout paper

---

## 🕐 Time Management per Phase

```
Hour  Phase  Activity                        Pages  Cumulative
──────────────────────────────────────────────────────────────
0-1   7A     Write abstract                  1      1
1-2   7A     Write introduction + notation   2      3
2-3   7A     Finalize assumptions           ─      3
──────────────────────────────────────────────────────────────
3-7   7B     Model 1 formulation            4      7
7-11  7B     Model 2 formulation            4      11
11-14 7B     Model 3 + integration          3      14
──────────────────────────────────────────────────────────────
14-18 7C     Generate results + figures     4      18
18-20 7C     Validation analysis            2      20
20-21 7C     Setup/edge cases               1      21
──────────────────────────────────────────────────────────────
21-23 7D     Sensitivity tests              2      23
23-24 7D     Strengths analysis             1      24
24-25 7D     Weaknesses + conclusion        1      25
──────────────────────────────────────────────────────────────
25-26 Refs   Format references              1      26
26-27 App    Code + tables                  2      28
──────────────────────────────────────────────────────────────
27-30 Polish Proofreading, formatting       ─      28
```

**Total:** 30 hours (with 3h buffer for Phase 7)

---

## 🏆 O-Prize Alignment Scoring

Use this to self-evaluate before submission:

| Criterion | Target | Your Paper | Score |
|---|---|---|---|
| Total pages (main) | 23-28 | ____ | __/10 |
| Model section | 10-12 pages | ____ | __/10 |
| Results section | 6-8 pages | ____ | __/10 |
| Introduction | 2-4 pages | ____ | __/10 |
| Sensitivity | 2-4 pages | ____ | __/10 |
| Figures | 10-15 | ____ | __/10 |
| Validation included? | Yes | Yes/No | __/10 |
| S/W reflection? | Yes | Yes/No | __/10 |
| Equations numbered? | Yes | Yes/No | __/10 |
| Code in appendix? | Yes | Yes/No | __/10 |
| **TOTAL** | | | __/100 |

**Scoring:**
- 90-100: Excellent O-Prize alignment
- 80-89: Strong submission
- 70-79: Acceptable but room for improvement
- <70: Revisions needed

---

**Document Version:** 1.0
**Source:** O-Prize_Page_Allocation_Analysis.md
**Usage:** Print and post during Phase 7 for quick reference
