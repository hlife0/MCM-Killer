# Consultation Export Protocol (v3.2.0)

> **Source**: CLAUDE.md v3.2.0 Mandatory Consultation Export
> **Purpose**: Detailed reference for mandatory consultation document export

---

## Overview

EVERY agent MUST export a consultation document after completing work. This ensures:
1. Work is documented for future reference
2. Knowledge is transferred between phases
3. Decisions are traceable and auditable
4. Next agents have context for their work

---

## Export Requirements

### Path Convention

```
output/docs/consultations/phase_{X}_{agent}_{timestamp}.md
```

**Timestamp Format**: `YYYY-MM-DDTHH-MM-SS` (hyphens instead of colons for filesystem safety)

**Examples**:
- `phase_0_reader_2026-01-30T14-30-00.md`
- `phase_1_modeler_2026-01-30T16-00-00.md`
- `phase_3_data_engineer_2026-01-30T18-45-00.md`
- `phase_5_model_trainer1_2026-01-30T20-00-00.md`

### Generating Timestamp in Bash

```bash
# Generate filesystem-safe timestamp
TIMESTAMP=$(date +%Y-%m-%dT%H-%M-%S)
echo "phase_1_modeler_${TIMESTAMP}.md"
```

---

## Document Template

```markdown
# Phase {X} Consultation: @{agent_name}

**Timestamp**: {ISO timestamp, e.g., 2026-01-30T14:30:00}
**Phase**: {X} - {phase_name}
**Duration**: {XX} minutes

---

## Work Summary

{Brief description of what was done - 2-4 sentences}

Example:
"Processed raw Olympic medal data from 1896-2023. Created feature engineering
pipeline with 15 derived features including medal momentum, host country advantage,
and GDP-normalized performance metrics. Validated data integrity with zero missing
values in critical columns."

---

## Deliverables

List all files created or modified:

- `{file1.ext}`: {brief description}
- `{file2.ext}`: {brief description}
- `{file3.ext}`: {brief description}

Example:
- `output/implementation/data/features_1.pkl`: Serialized feature matrix (5000 rows × 15 cols)
- `output/implementation/data/features_1.csv`: Human-readable feature export
- `output/docs/data_dictionary.md`: Feature definitions and sources

---

## Key Decisions Made

Document significant decisions with rationale:

1. **{Decision 1}**
   - Choice: {what was decided}
   - Rationale: {why this choice was made}
   - Alternatives considered: {what else was considered}

2. **{Decision 2}**
   - Choice: {what was decided}
   - Rationale: {why this choice was made}

Example:
1. **Feature normalization approach**
   - Choice: Z-score normalization per country
   - Rationale: Accounts for varying baseline performance across nations
   - Alternatives considered: Min-max scaling (rejected due to outlier sensitivity)

2. **Missing data handling**
   - Choice: Forward-fill with 3-year moving average
   - Rationale: Maintains temporal consistency in panel data

---

## Issues Encountered

Document any problems and their resolutions:

- **{Issue 1}**: {brief description}
  - Resolution: {how it was resolved}
  - Impact: {any remaining effects}

- **{Issue 2}**: {brief description}
  - Resolution: {how it was resolved}

Example:
- **GDP data gaps for 1896-1950**
  - Resolution: Used Maddison Project historical GDP estimates
  - Impact: Lower confidence for pre-1950 economic features

- **Duplicate country codes**
  - Resolution: Standardized to ISO 3166-1 alpha-3
  - Impact: None after correction

---

## Recommendations for Next Phase

Provide guidance for the next agent(s):

{What the next agent should know - 2-5 bullet points}

Example:
- Feature matrix is ready for Model 1 (random forest) and Model 2 (Bayesian)
- Country "host_advantage" feature has high variance - consider interaction terms
- GDP features are less reliable pre-1960 - may need sensitivity analysis
- Time series are not stationary - differencing may be required for ARIMA

---

## Quality Self-Assessment

- **Confidence**: {1-10} - How confident are you in the work quality?
- **Completeness**: {percentage} - What percentage of requirements were met?
- **Rigor**: HIGH / MEDIUM / LOW - How thorough was the analysis?

Example:
- Confidence: 8
- Completeness: 95%
- Rigor: HIGH
```

---

## Director Verification

Before approving any phase, Director MUST verify consultation export:

### Verification Command

```bash
# Check consultation document exists
ls output/docs/consultations/phase_{X}_*.md | wc -l

# Expected: At least 1 file per agent that worked on phase
```

### Verification Checklist

- [ ] Consultation document exists at correct path
- [ ] Document follows template structure
- [ ] All sections are populated (not placeholders)
- [ ] Deliverables match actual files created
- [ ] Self-assessment is reasonable (not all 10s)

### If Missing

Request agent to export consultation before proceeding:

```
@{agent}: Please export your consultation document.

Required path: output/docs/consultations/phase_{X}_{agent}_{timestamp}.md
Template: See knowledge_base/consultation_export_protocol.md

Do not proceed until this is complete.
```

---

## Documentation Path Convention

Full output/docs structure:

```
output/docs/
├── consultations/           # All consultation records
│   ├── phase_0_reader_2026-01-30T14-30-00.md
│   ├── phase_0_researcher_2026-01-30T15-00-00.md
│   ├── phase_1_modeler_2026-01-30T16-00-00.md
│   ├── phase_3_data_engineer_2026-01-30T18-45-00.md
│   ├── phase_4_code_translator_2026-01-30T20-00-00.md
│   ├── phase_5_model_trainer1_2026-01-30T22-00-00.md
│   ├── phase_5_model_trainer2_2026-01-30T22-30-00.md
│   ├── feedback_model_1_advisor.md        # Model consultation feedback
│   ├── feedback_model_1_feasibility_checker.md
│   ├── feedback_model_1_data_engineer.md
│   ├── feedback_model_1_code_translator.md
│   └── feedback_model_1_researcher.md
│
├── phase_reports/           # Phase completion reports
│   ├── phase_0_completion.md
│   ├── phase_1_completion.md
│   ├── phase_2_completion.md
│   └── ...
│
├── time_rejections.md       # Time rejection log
│
├── validation/              # Validation reports
│   ├── methodology_evaluation_1_advisor.md
│   ├── methodology_evaluation_1_validator.md
│   ├── code_review_model_1.md
│   └── ...
│
├── research_notes.md        # @reader/@researcher output
├── requirements_checklist.md
├── orchestration_log.md     # Director's log
└── known_issues.md          # Issue tracking
```

---

## Model Consultation Feedback

During Phase 1 (Model Design), each model requires 5-agent consultation.

### Feedback File Naming

```
output/docs/consultations/feedback_model_{N}_{agent}.md
```

**Required consultants**:
1. `feedback_model_1_researcher.md` - O-Prize alignment
2. `feedback_model_1_feasibility_checker.md` - Technical feasibility
3. `feedback_model_1_data_engineer.md` - Data availability
4. `feedback_model_1_code_translator.md` - Implementability
5. `feedback_model_1_advisor.md` - Weaknesses/improvements

### Director Verification

```bash
# Verify all 5 feedback files exist
ls -1 output/docs/consultations/feedback_model_1_*.md | wc -l
# Expected: 5
```

---

## Integration with Phase Completion

1. Agent completes phase work
2. Agent creates consultation document
3. Agent reports completion to Director
4. Director verifies consultation exists
5. Director calls @time_validator for time check
6. If all passed, proceed to next phase

---

*Reference: CLAUDE.md - Mandatory Consultation Export (v3.2.0)*
