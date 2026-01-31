# V2.0 Protocols Reference

> **Version**: 2.0.0
> **Purpose**: Complete reference for all V2.0 system upgrade protocols

---

## Protocol 1: "No Data Left Behind"

### Purpose
Comprehensive variable utilization to prevent data omission in the modeling pipeline.

### Chain of Accountability

```
@reader → @researcher → @data_engineer
(documents)   (maps)      (verifies)
```

### Agent Responsibilities

#### @reader (Phase 0)
- Outputs **Complete Variable List** for EVERY dataset
- Format per variable:
  - Name
  - Type (numeric, categorical, datetime, etc.)
  - Missing rate (%)
  - Potential use case

#### @researcher (Phase 0)
- Creates **Variable-Model Mapping** for ALL variables
- Must justify ANY variable exclusion with:
  - Statistical analysis showing non-relevance
  - Replacement variable that captures same information
  - Domain-specific reasoning with citations

#### @data_engineer (Phase 3)
- Runs **Data Loss Check** comparing before/after cleaning
- Must justify ANY dropped columns with same criteria as @researcher
- Outputs: `data_loss_report.md`

### Invalid vs Valid Justifications

| Invalid Excuses | Valid Justifications |
|-----------------|---------------------|
| "Too many categories" | Statistical analysis (chi-square, correlation < 0.05) |
| "Not relevant" | Replacement variable exists (with mapping) |
| "Too complex" | Domain-specific reasoning (with citation) |
| "Not enough time" | Collinearity analysis (VIF > 10) |
| "Doesn't fit" | Missing rate > 90% with no imputation strategy |

### Verification Checklist

- [ ] All datasets have complete variable lists
- [ ] All variables are mapped to at least one model
- [ ] Exclusions have valid justifications
- [ ] Data loss report shows < 5% unexplained loss

---

## Protocol 2: "Data-Shape Driven Innovation"

### Purpose
Enforce innovation based on data features, not just problem keywords.

### Chain of Accountability

```
@reader → @knowledge_librarian → @researcher
(documents)   (triggers)          (validates)
```

### Feature-Method Mapping Table

| Data Shape | Methods Triggered |
|------------|-------------------|
| Spatial (lat/lon/region) | Gravity Model, GWR, GNN, Kriging |
| Time + Multivariate | Tensor Decomposition, VAR, State-Space |
| Network structure | GNN, Community Detection, PageRank |
| High cardinality | Entity Embeddings, Target Encoding |
| Hierarchical | Mixed Effects, HLM |
| Count data | Poisson, Negative Binomial, Zero-Inflated |
| Survival/Duration | Cox PH, AFT, Kaplan-Meier |
| Panel data | Fixed Effects, Random Effects, Difference-in-Differences |

### @knowledge_librarian Responsibilities
- Trigger method retrieval based on detected data shapes
- Output: `feature_triggered_methods.md`
- Must identify ALL applicable methods, not just common ones

### @researcher Responsibilities
1. Validate ALL @knowledge_librarian feature-triggered methods
2. For each underutilized variable, identify 2+ innovative uses:
   - Non-traditional interpretation
   - Cross-domain application
   - Interaction effects
3. Explain judge appeal for each innovation

### Invalid vs Valid Justifications

| Invalid Excuses | Valid Justifications |
|-----------------|---------------------|
| "Too complex" | Specific data mismatch (with evidence) |
| "Not enough time" | Statistical evidence (sample size insufficient) |
| "Doesn't fit" | Domain-specific reasoning (with citation) |

---

## Protocol 3: "Visualization Enhancement"

### Purpose
Ensure visual quality, diversity, and asset integrity.

### Chain of Accountability

```
@writer → @visualizer → Phase 6.5 Pre-Check → Phase 7
(requests)  (diversifies)    (validates)         (proceeds)
```

### @writer: Conceptual Visualization Requests

When @writer needs diagrams (flowcharts, DAGs, architecture):
- DO NOT create visualizations yourself
- Use REQUEST_CONCEPTUAL_DIAGRAM format:

```markdown
REQUEST_CONCEPTUAL_DIAGRAM:
Type: [flowchart|DAG|architecture|concept_map]
Purpose: [description]
Elements: [list of components]
Relationships: [connections to show]
Output: figures/conceptual/[filename].png
```

### @visualizer: Chart Diversity Enforcement

**Rules**:
1. Maximum 2 consecutive charts of the same type
2. Minimum 4 different chart types across all figures
3. Generate **Chart Diversity Report** before Phase 6.5

**Chart Types to Mix**:
- Line charts (trends)
- Bar/Column charts (comparisons)
- Scatter plots (relationships)
- Heatmaps (matrices)
- Box plots (distributions)
- Geographic maps (spatial)
- Network graphs (connections)
- Sankey diagrams (flows)

### Phase 6.5: Asset Pre-Check

**Purpose**: Verify all image paths before Phase 7 to prevent LaTeX errors.

**Workflow**:
```bash
python tools/asset_pre_check.py
# Exit 0 = proceed to Phase 7
# Exit != 0 = callback @visualizer with missing list
```

**On Failure**:
1. Call @visualizer: "Regenerate missing/corrupt figures: [list]"
2. Wait for completion
3. Re-run pre-check
4. Loop until passed

**Full Details**: knowledge_base/asset_precheck_protocol.md

---

## Protocol 4: "Writing Enhancement"

### Purpose
Enforce professional academic writing standards for MCM papers.

### Chain of Accountability

```
@metacognition_agent → @writer → Output
(generates snippet)     (uses template)  (dense prose)
```

### Key Components

#### 1. Template Correction
- Use **mcmthesis** document class
- Correct algorithm packages: `algorithm2e` or `algorithmicx`
- Proper bibliography: `\bibliographystyle{plain}`

#### 2. Dense Academic Style
- Prose-heavy paragraphs (minimize bullet lists)
- Maximum 2 bullet lists per section
- Pseudo-code for algorithms (not bulleted steps)
- Observation-Implication structure for results

#### 3. Pre-Generated Summaries
- @metacognition_agent generates `results_summary_snippet.md` at Phase 5.8
- Contains key findings, comparisons, implications
- @writer incorporates (not copy-pastes) into narrative

#### 4. Time Allocations (Increased +30%)
| Phase | Original | V2.0 Allocation |
|-------|----------|-----------------|
| 7C (Results) | 35m | **45m** |
| 7E (Conclusions) | 25m | **32m** |

### Full Details

See: knowledge_base/writing_enhancement_protocol.md

---

## Protocol Enforcement Summary

| Protocol | Enforced At | Validator | Failure Action |
|----------|-------------|-----------|----------------|
| No Data Left Behind | Phases 0, 3 | @time_validator | REJECT, rerun |
| Data-Shape Innovation | Phases 0.2, 1 | @advisor | REJECT, rerun |
| Visualization Enhancement | Phase 6.5 | Director | Callback @visualizer |
| Writing Enhancement | Phases 7A-7F | @editor | REJECT, rerun |

---

## Quick Reference

| Protocol | One-Line Summary |
|----------|------------------|
| No Data Left Behind | Reader→Researcher→Data Engineer chain ensures all variables considered |
| Data-Shape Innovation | Feature-triggered method retrieval based on data shape |
| Visualization Enhancement | Chart diversity + asset pre-check before writing |
| Writing Enhancement | mcmthesis + dense prose + pre-generated snippets |
