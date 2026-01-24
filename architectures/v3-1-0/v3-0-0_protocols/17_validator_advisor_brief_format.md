# @validator/@advisor Concise Evaluation Format Protocol

> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Purpose**: Simplify @validator and @advisor evaluations to brief score + pass/fail format

---

## Problem Statement

**CRITICAL ISSUE**: @director's thinking process is too long because @validator and @advisor provide verbose evaluations that @director must read and analyze.

**Current Problem**:
```
@validator: "I've reviewed the methodology document in detail.
           The document contains sophisticated Bayesian hierarchical models
           with NUTS sampling, 4 chains, 20000 samples. The approach is
           mathematically sound with proper priors. The convergence
           diagnostics are appropriate. I find this to be excellent work.
           Grade: 9/10"

@advisor: "After careful analysis of the methodological framework,
          I have concerns about the lack of sensitivity analysis.
          The document would benefit from additional robustness checks.
          However, the core approach is solid. Grade: 7/10"

@director: [Spends 5 minutes analyzing both verbose reports]
           "Let me think about this. @validator gave 9/10, @advisor gave 7/10.
           @validator says sophisticated Bayesian approach, @advisor says
           lacks sensitivity analysis. Should I approve or request revision?
           Let me weigh the evidence..."
```

**Root Cause**:
1. **@validator and @advisor write verbose reports** - Takes too long to read
2. **@director must analyze verbose reports** - Adds cognitive load
3. **No standardized brief format** - Inconsistent structure
4. **@director makes decision based on reading reports** - Should just check pass/fail

---

## Solution: Brief Format Protocol

### Core Principles

**Principle 1: @validator/@advisor BRIEF FORMAT**
- **First response**: Score + Pass/Fail + 1-sentence justification
- **Detailed reports**: Written to file, not sent to @director
- **@director reads**: Only the brief response, not the detailed report

**Principle 2: Standardized Brief Format**
```markdown
Grade: X.Y/10 | Verdict: ✅ PASS / ❌ FAIL
Justification: [1 sentence max]
File verified: [path] ([N] lines)
```

**Principle 3: Unified Report Format**
- Reports written to files follow standard template
- Reports can be referenced by @researcher if revision needed
- Reports NOT read by @director (only brief response)

---

## Brief Format Specification

### @validator Brief Format

**When @director calls @validator:**

```
@director: "@validator: Validate output/model/model_design_1.md"
```

**@validator responds (BRIEF FORMAT):**

```markdown
Grade: 9.2/10 | Verdict: ✅ PASS

Justification: All equations mathematically sound with proper notation and complete specification.

File verified: output/model/model_design_1.md (324 lines)

Detailed report written to: output/docs/validation/validator_model_1.md
```

**@validator does NOT**:
- ❌ Write verbose evaluation in chat
- ❌ List all equations found
- ❌ Provide detailed analysis
- ❌ Make @director read long text

**@validator DOES**:
- ✅ Write detailed report to file (for @researcher reference)
- ✅ Provide brief score + verdict + justification
- ✅ Confirm file read with line count

**Example detailed report (written to file, NOT shown in chat):**
```markdown
# Validation Report: Model 1 Design

## File Information
- Path: output/model/model_design_1.md
- Lines: 324
- Last modified: 2026-01-19 14:23:45

## Equations Reviewed
| Equation | Page | Status | Notes |
|----------|------|--------|-------|
| (1) Medal count distribution | 2 | ✅ PASS | Proper Poisson specification |
| (2) Hierarchical prior | 3 | ✅ PASS | Appropriate hyperpriors |
| (3) Likelihood function | 4 | ✅ PASS | Correct formulation |
... [detailed analysis continues]

## Strengths
1. Mathematically rigorous formulation
2. Complete specification of all parameters
3. Appropriate choice of Bayesian inference
4. Proper convergence diagnostics planned

## Weaknesses
1. Could benefit from sensitivity analysis
2. Prior sensitivity not fully explored

## Overall Assessment
Grade: 9.2/10

The model design is mathematically sound and complete. Minor improvements
possible (sensitivity analysis) but not required for approval.

Verdict: ✅ PASS
```

---

### @advisor Brief Format

**When @director calls @advisor:**

```
@director: "@advisor: Evaluate output/model/model_design_1.md"
```

**@advisor responds (BRIEF FORMAT):**

```markdown
Grade: 8.5/10 | Verdict: ✅ PASS

Justification: Methodologically sound with appropriate Bayesian approach; minor improvements possible (sensitivity analysis).

File verified: output/model/model_design_1.md (324 lines)

Detailed report written to: output/docs/consultations/advisor_model_1.md
```

**@advisor does NOT**:
- ❌ Write verbose evaluation in chat
- ❌ Discuss methodology in detail
- ❌ Provide lengthy critique
- ❌ Make @director read long text

**@advisor DOES**:
- ✅ Write detailed consultation to file (for @researcher reference)
- ✅ Provide brief score + verdict + justification
- ✅ Confirm file read with line count

---

## @director Decision Logic (Simplified)

### Old Way (WRONG)

```
@director reads @validator's verbose report (10 sentences)
@director reads @advisor's verbose report (8 sentences)
@director analyzes: "@validator says X, Y, Z. @advisor says A, B, C."
@director spends 2 minutes thinking
@director makes decision
```

### New Way (CORRECT)

```
@validator: "Grade: 9.2/10 | ✅ PASS | Justification: [1 sentence]"
@advisor: "Grade: 8.5/10 | ✅ PASS | Justification: [1 sentence]"

@director checks:
- @validator verdict: ✅ PASS
- @advisor verdict: ✅ PASS
- Both verified same file: output/model/model_design_1.md (324 lines)

@director decision: ✅ APPROVE (both passed)
```

### Decision Matrix

| @validator | @advisor | @director decision | Rationale |
|------------|----------|-------------------|-----------|
| ✅ PASS | ✅ PASS | ✅ APPROVE | Consensus: both approve |
| ✅ PASS | ❌ FAIL | ❌ REJECT | Someone fails = reject |
| ❌ FAIL | ✅ PASS | ❌ REJECT | Someone fails = reject |
| ❌ FAIL | ❌ FAIL | ❌ REJECT | Consensus: both reject |

**Rule**: **IF anyone says FAIL → @director REJECTS** (no deliberation needed)

---

## Report Format Standardization

### Detailed Report Template (Written to File)

**Both @validator and @advisor MUST use this format for detailed reports:**

```markdown
# {Report Type}: Model {i} {Content Type}

## File Information
- Path: {file_path}
- Lines: {line_count}
- Last modified: {timestamp}
- Read by: {agent_name}
- Read date: {current_date}

## Grade
**Score**: X.Y/10
**Verdict**: ✅ PASS / ❌ FAIL

## Brief Evaluation (For @director)
{One-sentence justification - this is what @director sees in chat}

## Detailed Analysis (For @researcher reference)

### {Category 1}
{Detailed analysis}

### {Category 2}
{Detailed analysis}

## Strengths (What's Good)
1. {Strength 1}
2. {Strength 2}

## Weaknesses (What Needs Improvement)
1. {Weakness 1}
2. {Weakness 2}

## Recommendations
{Specific recommendations for improvement}

## Conclusion
{Overall assessment}

---

**Report Generated**: {timestamp}
**Agent**: {agent_name}
**Version**: v2.5.7 Brief Format Protocol
```

---

## Communication Protocol

### Phase 0.5 Example: Model Methodology Quality Gate

**OLD WAY (Verbose - WRONG)**:
```
@director: "@validator and @advisor: Evaluate methodology quality"

@validator: "I've read the research_notes.md file (843 lines).
           The document contains comprehensive methodology including:
           - Problem formulation with mathematical notation
           - Data sources and preprocessing
           - Model selection rationale
           The approach is sophisticated and well-justified.
           I give this a grade of 9/10."

@advisor: "After reviewing the methodology, I find it to be
          generally sound. However, I have some concerns about
          the lack of sensitivity analysis and the choice of
          priors could be better justified. I give this 7/10."

@director: [Spends time analyzing both reports]
           "Let me think about this. 9/10 vs 7/10. One says
           sophisticated, one says concerns about sensitivity.
           Should I approve or ask for revision?"
```

**NEW WAY (Brief - CORRECT)**:
```
@director: "@validator: Read output/docs/research_notes.md and evaluate methodology quality"
@director: "@advisor: Read output/docs/research_notes.md and evaluate methodology quality"

@validator: "Grade: 9.0/10 | ✅ PASS
            Justification: Sophisticated Bayesian approach with proper mathematical formulation.
            File verified: output/docs/research_notes.md (843 lines)
            Detailed report: output/docs/validation/validator_methodology.md"

@advisor: "Grade: 9.8/10 | ✅ PASS
           Justification: Excellent methodology with comprehensive approach and appropriate techniques.
           File verified: output/docs/research_notes.md (843 lines)
           Detailed report: output/docs/consultations/advisor_methodology.md"

@director checks:
- Both read: output/docs/research_notes.md (843 lines) ✅ (same file)
- @validator: 9.0/10 ✅ PASS
- @advisor: 9.8/10 ✅ PASS

@director decision: ✅ APPROVE (both passed, average 9.4/10 = EXCELLENT)
```

---

## When Revision is Needed

**If @validator or @advisor returns ❌ FAIL:**

```
@validator: "Grade: 4.0/10 | ❌ FAIL
            Justification: Missing critical equations (2) and (3), mathematical notation incomplete.
            File verified: output/model/model_design_1.md (150 lines)
            Detailed report: output/docs/validation/validator_model_1.md"

@director decision: ❌ REJECT (@validator failed)

@director to @modeler: "@validator rated 4.0/10 (FAIL). Issues:
                        - Missing critical equations (2) and (3)
                        - Mathematical notation incomplete
                        Please revise. See detailed report: output/docs/validation/validator_model_1.md"
```

**Note**: @director does NOT read the detailed report. Just refers to it.

**@modeler reads detailed report**, makes revisions, then:
```
@modeler: "Revisions complete. Addressed:
          - Added equation (2): Hierarchical prior specification
          - Added equation (3): Likelihood function
          - Completed mathematical notation
          Ready for re-verification."
```

---

## Report Reference by @researcher

**When revision is needed and @modeler needs guidance:**

```
@modeler: "@director: I need guidance on revising model design.
          What specifically needs improvement?"

@director: "@researcher: Review output/docs/validation/validator_model_1.md
           and provide specific guidance on addressing the failures."

@researcher: [Reads detailed report]
            "Based on @validator's report:
             1. Equation (2) needed: Specify hierarchical prior structure
             2. Equation (3) needed: Define likelihood function
             3. Notation: Use standard Bayesian notation (θ, φ, etc.)

             Suggested additions:
             - Equation (2): θ_c ~ N(μ_θ, σ_θ²) for c = 1,...,C
             - Equation (3): y_ct ~ Poisson(λ_ct) with log(λ_ct) = θ_c + X_ctβ

             Reference: Gelman et al. (2013) Bayesian Data Analysis"
```

---

## Enforcement Protocol

### @validator/@advisor Brief Format Rules

**MUST**:
- ✅ First line: "Grade: X.Y/10 | Verdict: ✅ PASS / ❌ FAIL"
- ✅ Second line: "Justification: [1 sentence max]"
- ✅ Third line: "File verified: [path] ([N] lines)"
- ✅ Fourth line: "Detailed report written to: [path]"
- ✅ Write detailed report to file using standard template

**MUST NOT**:
- ❌ Write verbose evaluation in chat (>3 sentences)
- ❌ List all items found in file
- ❌ Provide detailed analysis in chat
- ❌ Make @director read long text

### @director Decision Rules

**MUST**:
- ✅ Read only brief format (first 4 lines)
- ✅ Check both agents verified same file (path + line count)
- ✅ Check verdicts (PASS/FAIL)
- ✅ Apply: "Someone fails = reject" rule
- ✅ Provide clear decision with rationale

**MUST NOT**:
- ❌ Read detailed reports (validator_*.md, advisor_*.md)
- ❌ Analyze verbose evaluations
- ❌ Spend time deliberating (decision is automatic from verdicts)

---

## Examples: Complete Scenarios

### Scenario 1: Both Pass → Approve

```
@director: "@validator: Validate output/model/model_design_1.md"
@director: "@advisor: Evaluate output/model/model_design_1.md"

@validator: "Grade: 9.0/10 | ✅ PASS
            Justification: Mathematically sound with proper specification.
            File verified: output/model/model_design_1.md (324 lines)
            Detailed report: output/docs/validation/validator_model_1.md"

@advisor: "Grade: 8.5/10 | ✅ PASS
           Justification: Appropriate methodology with minor improvements possible.
           File verified: output/model/model_design_1.md (324 lines)
           Detailed report: output/docs/consultations/advisor_model_1.md"

@director:
Both verified: output/model/model_design_1.md (324 lines) ✅
@validator: 9.0/10 ✅ PASS
@advisor: 8.5/10 ✅ PASS
Average: 8.75/10 = EXCELLENT

Decision: ✅ APPROVE

Proceeding to Phase 1.5 (Time Estimate Validation)
```

### Scenario 2: One Fails → Reject

```
@director: "@validator: Validate output/model/model_design_2.md"
@director: "@advisor: Evaluate output/model/model_design_2.md"

@validator: "Grade: 3.0/10 | ❌ FAIL
            Justification: Missing 3 critical equations and incomplete mathematical specification.
            File verified: output/model/model_design_2.md (85 lines)
            Detailed report: output/docs/validation/validator_model_2.md"

@advisor: "Grade: 7.0/10 | ✅ PASS
           Justification: Approach sound but needs completion.
           File verified: output/model/model_design_2.md (85 lines)
           Detailed report: output/docs/consultations/advisor_model_2.md"

@director:
Both verified: output/model/model_design_2.md (85 lines) ✅
@validator: 3.0/10 ❌ FAIL
@advisor: 7.0/10 ✅ PASS

Decision: ❌ REJECT (@validator failed)

@modeler: @validator rated 3.0/10 (FAIL).
         Issues: Missing 3 critical equations, incomplete specification.
         Please revise. See: output/docs/validation/validator_model_2.md
```

### Scenario 3: Both Fail → Reject

```
@director: "@validator: Validate output/paper/paper.tex"
@director: "@advisor: Evaluate output/paper/paper.tex"

@validator: "Grade: 4.0/10 | ❌ FAIL
            Justification: Multiple LaTeX compilation errors and missing sections.
            File verified: output/paper/paper.tex (423 lines)
            Detailed report: output/docs/validation/validator_paper.md"

@advisor: "Grade: 5.0/10 | ❌ FAIL
           Justification: Structure incomplete and quality below competition standards.
           File verified: output/paper/paper.tex (423 lines)
           Detailed report: output/docs/consultations/advisor_paper.md"

@director:
Both verified: output/paper/paper.tex (423 lines) ✅
@validator: 4.0/10 ❌ FAIL
@advisor: 5.0/10 ❌ FAIL

Decision: ❌ REJECT (both failed)

@writer: Both @validator (4.0/10) and @advisor (5.0/10) failed.
         Issues: LaTeX errors, missing sections, incomplete structure.
         Please revise. See:
         - output/docs/validation/validator_paper.md
         - output/docs/consultations/advisor_paper.md
```

---

## Implementation Checklist

**For @validator**:
- [ ] Uses brief format (first 4 lines)
- [ ] Provides grade + verdict + justification
- [ ] Confirms file read with path + line count
- [ ] Writes detailed report to standardized path
- [ ] Does NOT write verbose evaluation in chat

**For @advisor**:
- [ ] Uses brief format (first 4 lines)
- [ ] Provides grade + verdict + justification
- [ ] Confirms file read with path + line count
- [ ] Writes detailed consultation to standardized path
- [ ] Does NOT write verbose evaluation in chat

**For @director**:
- [ ] Reads only brief format (first 4 lines)
- [ ] Verifies both agents read same file (path + line count)
- [ ] Checks verdicts (PASS/FAIL)
- [ ] Applies "someone fails = reject" rule
- [ ] Does NOT read detailed reports

**For @researcher**:
- [ ] Available to read detailed reports when revision needed
- [ ] Provides specific guidance based on detailed report content
- [ ] References standard methodologies (textbooks, papers)

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
