# Model Design Consultation Response Templates

> **Purpose**: This file contains templates and guidance for providing feedback when @modeler requests consultation on a draft model proposal. Your data engineering expertise ensures the model design is feasible with available data.

---

## 🆔 [CRITICAL NEW] Model Design Consultation (MANDATORY)

> [!CRITICAL]
> **[MANDATORY] When @modeler requests consultation on a draft proposal, you MUST provide feedback.**
>
> This is NOT optional. Your data expertise ensures the model design is feasible with available data.

### When Consultation is Requested

**Director will send you**: `output/model_proposals/model_X_draft.md`

**Your task**: Review the draft and provide feedback from your data engineering perspective.

### Consultation Response

**Read the draft**:
```
Read: output/model_proposals/model_X_draft.md
```

**Evaluate from data perspective**:
- **Data Availability**: Do we have the required data or can it be derived?
- **Feature Engineering Feasibility**: Can the proposed features be created?
- **Data Quality**: Is the available data sufficient quality?
- **Computational Feasibility**: Can the data be processed in reasonable time?

**Write feedback**:
```
Write to: output/docs/consultations/feedback_model_X_data_engineer.md
```

**Feedback Format**:
```markdown
# Feedback on Model X Draft - @data_engineer

## Data Feasibility Assessment
- **Data Availability**: [All data available / Some needs derivation / Missing critical data]
- **Feature Engineering**: [Fully feasible / Partially feasible / Not feasible]
- **Verdict**: [PROCEED WITH CAUTION / NEEDS REVISION / NOT FEASIBLE]

## ✅ Data Strengths
1. [Strength 1]
2. [Strength 2]

## ❌ Data Concerns
1. [Concern 1] - [Impact on model]
2. [Concern 2] - [Impact on model]

## 💡 Recommendations

### Data Availability
- [What data is available]
- [What data needs derivation]
- [How to derive missing data]

### Feature Engineering
- [Feasibility of proposed features]
- [Alternative features if needed]
- [Feature complexity concerns]

### Data Quality Considerations
- [Quality issues in available data]
- [How to address quality issues]
- [Potential impact on model performance]

## Summary
**If data is FEASIBLE**:
All required data is available or can be derived. Model design is compatible with data constraints.

**If NEEDS REVISION**:
Model design requires data/features that are not available. Suggested revisions:
1. [Revision 1]
2. [Revision 2]
```

**Report to Director**:
```
Director, I have completed my data engineering review of Model X draft.

Feedback: output/docs/consultations/feedback_model_X_data_engineer.md
Verdict: [PROCEED / NEEDS REVISION / NOT FEASIBLE]

Summary: [2-3 sentence assessment]
```
