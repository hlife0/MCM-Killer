# Judgment Report Template for @judge_zero

## Purpose
This template provides structure for adversarial mock judging of MCM papers before final submission.

## Judgment Report Structure

### Section 1: Executive Summary
- Verdict: PASS / REJECT
- Overall score: X/10
- Critical issues summary: 2-3 sentences

---

## Template

### 1. EXECUTIVE SUMMARY

**Verdict**: PASS / REJECT

**Overall Score**: X/10

**Summary**: [2-3 sentences summarizing the paper's overall quality and critical issues]

---

### 2. STRENGTHS (What Works)

**Content Strengths**:
- [ ] Problem fully addressed (all requirements)
- [ ] Models appropriate and well-justified
- [ ] Results quantitative and specific
- [ ] Analysis thorough and insightful
- [ ] Conclusions well-supported by data

**Presentation Strengths**:
- [ ] Abstract effective (3+ metrics, 250-350 words)
- [ ] Paper well-organized and readable
- [ ] Figures/tables clear and well-integrated
- [ ] Writing style academic and precise
- [ ] Citations appropriate

**Technical Strengths**:
- [ ] Models correctly implemented
- [ ] Methods clearly explained
- [ ] Assumptions reasonable and stated
- [ ] Sensitivity analysis performed
- [ ] Limitations acknowledged

---

### 3. WEAKNESSES (Critical Issues)

**Content Weaknesses**:
- [ ] Missing or incomplete requirements
- [ ] Models oversimplified or inappropriate
- [ ] Results vague or lack specificity
- [ ] Analysis superficial or missing
- [ ] Conclusions not supported by data

**Presentation Weaknesses**:
- [ ] Abstract ineffective (<3 metrics, wrong length)
- [ ] Poor organization or flow
- [ ] Figures/tables unclear or misplaced
- [ ] Writing style informal or imprecise
- [ ] Formatting issues

**Technical Weaknesses**:
- [ ] Models incorrectly implemented
- [ ] Methods unclear or missing
- [ ] Assumptions unreasonable or unstated
- [ ] No sensitivity analysis
- [ ] Limitations ignored

---

### 4. THE KILL LIST (Max 3 Critical Issues)

**Issue #1**: [Title]
- **Location**: [Section/Line]
- **Severity**: CRITICAL / HIGH / MEDIUM
- **Description**: [2-3 sentences explaining the problem]
- **Impact**: [How this affects paper quality]
- **Fix Required**: [Specific action needed]

**Issue #2**: [Title]
- **Location**: [Section/Line]
- **Severity**: CRITICAL / HIGH / MEDIUM
- **Description**: [2-3 sentences explaining the problem]
- **Impact**: [How this affects paper quality]
- **Fix Required**: [Specific action needed]

**Issue #3**: [Title]
- **Location**: [Section/Line]
- **Severity**: CRITICAL / HIGH / MEDIUM
- **Description**: [2-3 sentences explaining the problem]
- **Impact**: [How this affects paper quality]
- **Fix Required**: [Specific action needed]

---

### 5. DETAILED ANALYSIS

#### 5.1 Abstract Assessment
- [ ] Length appropriate (250-350 words)
- [ ] Contains 3+ quantitative metrics
- [ ] All models mentioned by name
- [ ] Clear structure (Background → Methods → Results → Implications)
- [ ] Specific numerical results included

**Verdict**: PASS / NEEDS IMPROVEMENT / FAIL

**Comments**: [Specific feedback]

---

#### 5.2 Model Assessment

**Model 1**: [Name]
- [ ] Mathematical formulation complete
- [ ] Parameters clearly defined
- [ ] Assumptions stated and justified
- [ ] Solution approach clear
- [ ] Appropriate for requirement

**Verdict**: PASS / NEEDS IMPROVEMENT / FAIL

**Comments**: [Specific feedback]

[Repeat for each model]

---

#### 5.3 Results Assessment

- [ ] All requirements addressed
- [ ] Results quantitative (numbers, %, intervals)
- [ ] Figures/tables well-integrated
- [ ] Captions descriptive (Observation → Implication)
- [ ] Uncertainty quantified where appropriate

**Verdict**: PASS / NEEDS IMPROVEMENT / FAIL

**Comments**: [Specific feedback]

---

#### 5.4 Analysis Assessment

- [ ] Sensitivity analysis performed
- [ ] Strengths identified (specific, not generic)
- [ ] Weaknesses acknowledged with mitigations
- [ ] Insights original and valuable
- [ ] Recommendations actionable

**Verdict**: PASS / NEEDS IMPROVEMENT / FAIL

**Comments**: [Specific feedback]

---

#### 5.5 Writing Style Assessment

- [ ] Academic tone maintained
- [ ] Active voice used ("We develop", not "It was developed")
- [ ] Strong verbs employed (quantify, demonstrate, reveal)
- [ ] Precise language (specific numbers, not vague statements)
- [ ] No grammatical or spelling errors

**Verdict**: PASS / NEEDS IMPROVEMENT / FAIL

**Comments**: [Specific feedback]

---

### 6. FINAL RECOMMENDATION

**If PASS**: Paper meets O-Prize standards and is ready for submission.

**If REJECT**: Paper has critical flaws that must be addressed before submission.

**Next Steps**:
- [ ] Address Kill List issues (assign to specific agents)
- [ ] Re-evaluate after fixes
- [ ] Consider second mock judgment

---

## Scoring Rubric

| Score Range | Quality Level | Description |
|-------------|---------------|-------------|
| 9-10 | O-Prize Winner | Outstanding, publication-ready |
| 7-8 | Finalist | Strong, minor improvements needed |
| 5-6 | Meritorious | Adequate, moderate improvements needed |
| 3-4 | Successful Participant | Weak, significant improvements needed |
| 1-2 | Problematic | Critical flaws, major rework required |

---

## Common Issues to Flag

### Critical Issues (Automatic REJECT)
1. Missing or incomplete requirements
2. No mathematical formulation in model sections
3. Results completely qualitative (no numbers)
4. Plagiarism or academic dishonesty
5. Paper exceeds 25 pages (excluding summary)

### High-Priority Issues
1. Abstract lacks quantitative metrics
2. Models not justified or explained
3. Figures/tables missing or poorly placed
4. No sensitivity analysis
5. Conclusions not supported by results

### Medium-Priority Issues
1. Writing style inconsistent or informal
2. Minor formatting issues
3. Some results vague or imprecise
4. Limited analysis of implications

---

## Mercy Rule

After 3 REJECT verdicts:
- If paper has improved significantly but still has issues
- Issue conditional PASS with required revisions
- Specify which issues must be fixed before actual submission
- Allow paper to proceed with warnings

---

**Template Version**: 1.0
**Last Updated**: 2026-01-28
**Agent**: @judge_zero
**Protocol**: DEFCON 1 Mock Judgment
