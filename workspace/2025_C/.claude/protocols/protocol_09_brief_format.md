# Protocol 9: @validator/@advisor Brief Format

> **Purpose**: Enable fast decision-making by requiring concise evaluations in chat, detailed reports to files
> **Owner**: @validator, @advisor
> **Scope**: Phases 0.5, 1, 4, 5.5, 10 (all validation phases)

## Problem Statement

Long evaluations in chat cause cognitive overload and slow decisions:

```
@validator: [50 lines of detailed analysis in chat]
@director: "Let me read all this..."
[5 minutes later]
@director: "OK, but what's the verdict?"
```

## Brief Format

### Brief Format (First 4 Lines Only in Chat)

**Template**:
```
Grade: 9.0/10 | Verdict: PASS
Justification: Mathematically sound with proper specification.
File verified: output/model/model_design_1.md (324 lines)
Detailed report written to: output/docs/validation/validator_model_1.md
```

**Example 1** (PASS):
```
Grade: 9.5/10 | Verdict: PASS
Justification: Hierarchical structure well-specified, proper priors,
sensitivity analysis included.
File verified: output/model/model_design_2.md (412 lines)
Detailed report: output/docs/validation/validator_model_2.md
```

**Example 2** (NEEDS_REVISION):
```
Grade: 6.0/10 | Verdict: NEEDS_REVISION
Justification: Missing sensitivity analysis, priors not justified.
File verified: output/model/model_design_3.md (298 lines)
Detailed report: output/docs/validation/validator_model_3.md
```

**Example 3** (REJECT):
```
Grade: 4.0/10 | Verdict: REJECT
Justification: Algorithm mismatch (sklearn instead of PyMC), only 5/15
features present.
File verified: output/implementation/code/model_1.py (187 lines)
Detailed report: output/docs/validation/validator_code_1.md
```

## Detailed Report (To File)

**Full report written to file**:
- `output/docs/validation/validator_model_{i}.md`
- `output/docs/validation/advisor_model_{i}.md`

**Detailed report structure**:
```markdown
# Validation Report: Model 1 Design

**Validator**: @validator
**Date**: 2026-01-28
**File Verified**: output/model/model_design_1.md (324 lines)

## Overall Grade: 9.5/10

## Verdict: PASS

## Strengths
1. Hierarchical structure well-specified
2. Proper prior distributions (Normal, Half-Cauchy)
3. Sensitivity analysis plan included
4. Clear parameter identification

## Weaknesses
1. Prior justification could be stronger (Minor)
2. Computational requirements not fully specified (Minor)

## Recommendations
1. Add prior justification references (Optional)
2. Include expected runtime estimates (Optional)

## Detailed Analysis
[50-100 lines of detailed analysis...]

## Conclusion
Model design is sound and ready for implementation.
```

## @director Decision Logic

**Simple decision logic**:
```
IF @validator PASS AND @advisor PASS:
    RETURN "APPROVE - Proceed to next phase"
ELIF @validator NEEDS_REVISION OR @advisor NEEDS_REVISION:
    RETURN "REWORK - Address issues before proceeding"
ELSE:
    RETURN "REJECT - Major issues, consider rewind"
```

**Example decision**:
```
@validator: "Grade: 9.5/10 | Verdict: PASS"
@advisor: "Grade: 8.5/10 | Verdict: PASS"

@director: "Both PASS → APPROVE - Proceed to Phase 2"
```

## Communication Quality Standards

### Brief Format Requirements

**REQUIRED in brief**:
- [ ] Grade (X/10)
- [ ] Verdict (PASS/NEEDS_REVISION/REJECT)
- [ ] Justification (1-2 sentences)
- [ ] File verified (path + line count)
- [ ] Detailed report location

**FORBIDDEN in brief**:
- [ ] Long explanations (>50 words)
- [ ] Multiple paragraphs
- [ ] Detailed analysis
- [ ] Code snippets

### Detailed Report Requirements

**REQUIRED in detailed report**:
- [ ] File verified (path, size, timestamp)
- [ ] Overall grade
- [ ] Verdict
- [ ] Strengths (3-5 bullet points)
- [ ] Weaknesses (3-5 bullet points)
- [ ] Recommendations (specific actions)
- [ ] Detailed analysis (50-100 lines)
- [ ] Conclusion

## Benefits

**For @director**:
- Faster decisions (read 4 lines instead of 50)
- Reduced cognitive load
- Clear verdict immediately visible

**For @validator/@advisor**:
- Still provides detailed analysis (in file)
- Brief format forces clarity
- Verdict unambiguous

**For workflow**:
- Reduced chat clutter
- Faster phase transitions
- Better documentation (detailed reports archived)

## Example Workflow

**Without Protocol 9**:
```
@validator: [50 lines in chat]
@director: "Let me process..."
[waits 2 minutes]
@director: "OK, I think it's good but let me check..."
[waits another minute]
@director: "Wait, I need to re-read..."
Total: 5 minutes
```

**With Protocol 9**:
```
@validator: "Grade: 9.5/10 | Verdict: PASS | Details: output/docs/validation/..."
@director: "PASS → APPROVE"
Total: 10 seconds
```

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
