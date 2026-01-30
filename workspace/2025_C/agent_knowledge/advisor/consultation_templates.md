# Consultation Templates for Advisor Agent

This file contains standardized templates for providing feedback during model design consultations and re-verification processes.

---

## Model Design Consultation Feedback Format

When @advisor is requested to provide feedback on a model design draft, use this template:

```markdown
# Feedback on Model X Draft - @advisor

## Overall Assessment
- **O-Prize Potential**: [Weak / Moderate / Strong]
- **Sophistication**: [Too Basic / Adequate / Excellent]
- **Verdict**: [NEEDS REVISION / ACCEPTABLE / STRONG]

## ✅ Strengths
1. [What's working well]
2. [Good methodological choices]
3. [Sound mathematical approach]

## ❌ Critical Issues (Must Fix)
1. [Issue 1] - [Why it's critical]
2. [Issue 2] - [Why it's critical]

## 💡 Recommendations

### Increase Sophistication
- [How to make the model more competitive for O-Prize]
- [Advanced methods to consider]
- [Hybrid approaches]

### Computational Intensity
- [Current: X hours] - [Meets / Does not meet] 2-6h requirement
- [If too fast: Suggest more intensive methods]

### Methodological Improvements
- [Better assumptions]
- [Stronger validation approach]
- [More comprehensive sensitivity analysis]

### Comparison to O-Prize Winners
Based on O-Prize papers I've reviewed:
- [How this compares]
- [What would make it more competitive]

## Summary
**If NEEDS REVISION**:
The model requires revision to meet O-Prize standards. Priority fixes:
1. [Fix 1]
2. [Fix 2]

**If ACCEPTABLE or STRONG**:
Solid approach. Optional enhancements:
1. [Enhancement 1]
2. [Enhancement 2]
```

**Report to Director**:
```
Director, I have completed my faculty advisor review of Model X draft.

Feedback: output/docs/consultations/feedback_model_X_advisor.md
Verdict: [NEEDS REVISION / ACCEPTABLE / STRONG]

Summary: [2-3 sentence assessment]
```

---

## Verification Checklist

Before approving:
- [ ] I read the requirements checklist
- [ ] I read the submitted paper
- [ ] I compared with at least one O-Prize paper
- [ ] I provided specific, actionable feedback
- [ ] I saved my review to output/advisor_review.md
- [ ] **I checked that paper uses mcmthesis class (not article)**
- [ ] **I verified model_design.md content is fully copied (not summarized)**
- [ ] **I checked that each model section is 2-3 pages long**
