# Methodology Evolution Template: Academic Style

**Version**: 1.0
**Date**: 2026-01-28
**Purpose**: Document technical challenges, methodological refinements, and research insights using formal academic discourse

---

## Template Structure

```markdown
# Methodology Evolution: Model {i}

**Date**: {YYYY-MM-DD}
**Model**: {Model Name}
**Requirement(s) Addressed**: {List}

---

## 1. Initial Approach and Assumptions

### Method Overview
[Brief technical description: 2-3 sentences]
- Starting method and rationale
- Key assumptions
- Expected performance characteristics

### Design Expectations
- Target metrics: [specific quantitative goals]
- Computational constraints: [time/memory limits]
- Data requirements: [features/samples needed]

---

## 2. Technical Challenges Identified

### Primary Challenge
**Symptom**: [Specific technical issue with quantitative data]
- Observed behavior: [what went wrong, with numbers]
- Detection method: [logs/validation checks]
- Impact severity: [High/Medium/Low]

**Root Cause Analysis**
- Hypothesis 1: [possible cause 1]
- Hypothesis 2: [possible cause 2]
- Validated cause: [which hypothesis was confirmed]
- Evidence: [log data/analysis supporting conclusion]

**Physical/Domain Interpretation**
- Technical symptom → Domain mechanism mapping
- What this reveals about: [problem domain/model assumptions]
- Connection to: [theoretical principle]

### Secondary Challenges (if applicable)
[Repeat above structure for each major challenge]

---

## 3. Methodological Refinement

### Refinement Strategy
**Change Implemented**: [technical description of refinement]
- What was changed: [specific modification]
- Rationale: [connection between challenge and solution]
- Expected outcome: [hypothesized improvement]

### Implementation Details
- Algorithm adjustment: [specific changes]
- Parameter modifications: [before → after comparison]
- Feature additions/removals: [if applicable]
- Computational approach: [new methods/tools used]

---

## 4. Validation and Results

### Quantitative Improvement
| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| [Metric 1] | [value] | [value] | [+X%] |
| [Metric 2] | [value] | [value] | [+Y%] |
| [Metric 3] | [value] | [value] | [+Z%] |

**Key Results**:
- Primary metric: [specific improvement with CI/p-value if applicable]
- Secondary metrics: [additional improvements]
- Efficiency gains: [time/computation reduction if any]

### Validation Method
- Test performed: [cross-validation/held-out test/etc]
- Sample size: [N]
- Confidence level: [95% CI or equivalent]
- Statistical significance: [if applicable]

---

## 5. Research Implications

### 5.1 Methodological Contribution

**Insight**: [What this reveals about modeling approaches]
- Technical principle: [generalizable lesson]
- Applicability: [when this insight is relevant]
- Transferability: [other problems/domains where applicable]

### 5.2 Domain Insights

**Finding**: [What this reveals about the problem domain]
- Domain mechanism: [underlying principle discovered]
- Policy/theoretical implication: [practical consequence]
- Broader relevance: [connection to larger field]

### 5.3 Limitations and Remaining Challenges

**Acknowledged Limitations**:
1. **[Limitation 1]**: [Description]
   - Scope: [when this limitation applies]
   - Impact: [how it affects results]
   - Mitigation: [what was done to address]

2. **[Limitation 2]**: [Description]
   - Scope: [when this limitation applies]
   - Impact: [how it affects results]
   - Mitigation: [what was done to address]

**Future Work Directions**:
- Immediate: [short-term improvements]
- Extended: [longer-term research directions]
- Exploratory: [speculative avenues for investigation]

---

## 6. Integration to Paper

### Discussion Section Points (≤2 sentences each)

**Point 1**: [Technical observation] → [Quantitative improvement]
Example: "R-hat > 1.3 for β parameters indicated parameter correlation. Reparameterization reduced correlation by 67%, improving convergence efficiency."

**Point 2**: [Methodological insight] → [Domain implication]
Example: "Convergence patterns revealed regional heterogeneity in medal distributions, suggesting geographically-tailored modeling approaches."

**Point 3**: [Limitation acknowledgment] → [Future work direction]
Example: "The model exhibits increased prediction error when external covariates change rapidly, indicating potential for adaptive feature selection in future iterations."

### Abstract/Conclusion Integration
- One-sentence summary: [Key takeaway for paper's opening or closing]
```

---

## Language Guidelines

### ✅ REQUIRED (Academic Style)
- "Technical challenge," "convergence issue," "systematic bias"
- "Methodological refinement," "model adjustment," "iterative improvement"
- "Analysis revealed," "investigation demonstrated," "evaluation indicated"
- "The model exhibits," "results suggest," "data indicates"
- "Limitation," "constraint," "boundary condition"

### ❌ FORBIDDEN (Narrative Style)
- "The ordeal," "the struggle," "the battle"
- "Revelation," "epiphany," "breakthrough," "disaster," "crisis"
- "We discovered," "we realized," "we found" (use passive/impersonal)
- "Amazing," "incredible," "surprising" (use emotional-neutral terms)
- "Journey," "path," "quest" (metaphorical language)

---

## Quantitative Requirements

### Mandatory Elements
- **Every claim requires a number**: No qualitative statements without support
- **Before/After comparisons**: Show change with specific metrics
- **Statistical validation**: Include CI, p-value, or equivalent when applicable
- **Evidence-based reasoning**: Cite log data, validation results, or theoretical basis

### Examples

**Good** (Quantitative):
```
Symptom: R-hat values exceeded 1.3 for 15% of β parameters
Evidence: Log file epoch 50 shows R-hat mean = 1.35, max = 1.42
Improvement: After reparameterization, R-hat < 1.1 for all parameters (98% reduction)
```

**Bad** (Qualitative):
```
Symptom: High R-hat values
Evidence: The model wasn't converging well
Improvement: Much better after fixing
```

---

## Integration Examples

### Example 1: Convergence Issue → Methodological Insight

**Challenge**:
- Symptom: R-hat > 1.3 for β parameters (mean: 1.35, max: 1.42)
- Cause: Parameter correlation masking convergence assessment
- Refinement: Centered parameterization + non-centered reparameterization

**Result**:
- R-hat reduced to < 1.05 for all parameters (97% improvement)
- Convergence time: 3.2 hours → 1.8 hours (44% faster)
- Effective sample size: increased by 2.3×

**Paper Integration** (≤2 sentences):
"Parameter correlation caused R-hat > 1.3 for β parameters (mean: 1.35). Non-centered reparameterization reduced R-hat < 1.05 and decreased convergence time by 44%."

### Example 2: Data Quality Issue → Domain Insight

**Challenge**:
- Symptom: Prediction errors 3.2× higher for first-time medalists
- Cause: Sparse historical data for emerging nations
- Refinement: Hierarchical shrinkage prior

**Result**:
- Prediction error reduced by 58% for sparse-data countries
- Overall RMSE: 4.2 → 3.1 (26% improvement)
- Trade-off: 12% increase in error for well-established countries

**Paper Integration** (≤2 sentences):
"Hierarchical shrinkage reduced prediction error by 58% for countries with sparse historical data (RMSE: 6.8 → 2.9). This approach reveals strong regional clustering in medal-winning patterns."

### Example 3: Computational Limitation → Future Work

**Challenge**:
- Symptom: Model training exceeded 12-hour target for 3+ region models
- Cause: O(n³) scaling with country count
- Refinement: Variational inference approximation

**Result**:
- Training time: 14.2 hours → 4.8 hours (66% reduction)
- Accuracy trade-off: 3.5% increase in RMSE
- Computational efficiency: 8.3× faster

**Paper Integration** (≤2 sentences):
"Variational approximation reduced training time by 66% (14.2h → 4.8h) with a 3.5% RMSE trade-off. Future work should explore expectation-propagation to balance accuracy and computational efficiency."

---

## Quality Checklist

Before finalizing `methodology_evolution_{i}.md`, verify:

### Structure
- [ ] All sections present (1-6)
- [ ] No storytelling headers ("The Ordeal", "The Revelation", etc.)
- [ ] Technical language throughout
- [ ] Quantitative data in every section

### Content
- [ ] At least 1 technical challenge → refinement mapping
- [ ] All claims supported by numbers
- [ ] Physical/domain interpretation provided
- [ ] Limitations acknowledged transparently

### Language
- [ ] No forbidden words (ordeal, revelation, treasure, etc.)
- [ ] Required terminology used (challenge, refinement, indicates)
- [ ] Emotional-neutral tone maintained
- [ ] Active voice minimized

### Integration Ready
- [ ] ≤2 sentence summary points for Discussion section
- [ ] Abstract/Conclusion one-liner provided
- [ ] Quantitative metrics ready for citation

---

## References and Further Reading

### Academic Writing Standards
- [Limitations in Research – A Simplified Guide with Examples](https://www.ref-n-write.com/blog/limitations-in-research-a-simplified-guide-with-examples/) (2024)
- [How To Write The Methodology Chapter](https://gradcoach.com/how-to-write-the-methodology-chapter/)
- [Organizing Your Social Sciences Research Paper: Limitations](https://libguides.usc.edu/writingguide/limitations)

### Reference Paper Patterns
- 2009116.pdf: Transparent limitations section (6+ items, bullet-point format)
- 2024 O-Prize papers: Quantitative focus, observation → implication structure
- Analysis docs/reference_paper_analysis.md: Section structure and depth guidelines

### Internal Documentation
- CLAUDE.md Phase 5.8: Methodology evolution workflow
- .claude/agents/metacognition_agent.md: Agent instructions and constraints
- .claude/protocols/protocol_14_academic_style.md: Style alignment rules
- .claude/agents/writer.md: Integration guidance for Discussion section

---

**Template Version**: 1.0
**Last Updated**: 2026-01-28
**Maintained By**: @metacognition_agent
