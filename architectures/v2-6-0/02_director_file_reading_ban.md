# @director File Reading Ban Protocol

> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Purpose**: Prevent @director from contaminating agent evaluations by reading files before delegating

---

## Problem Statement

**CRITICAL ISSUE**: When @director reads files before delegating to agents, agents receive contaminated context and may evaluate wrong files.

**Example Failure** (v2.5.6):
```
Step 1: @director: Read(output/docs/research_notes.md) → "I see sophisticated Bayesian methods"
Step 2: @director: "@advisor, evaluate the methodology quality"
Step 3: @advisor: Works from @director's implicit context, NOT the actual file
Step 4: @advisor: "This lacks methodological content, 1/10, CRITICAL FAILURE"

Reality: research_notes.md contains 843 lines of sophisticated methods
@validator: "Sophisticated methods, 9/10, APPROVED"

Root Cause: @director read the file → contaminated the delegation → @advisor evaluated wrong content
```

**Why This Happens**:
1. @director wants to "verify" or "understand" before delegating
2. @director reads file, forms own mental model
3. @director calls agent with: "Evaluate X" (no file path specified)
4. Agent receives @director's understanding as implicit context
5. Agent evaluates based on @director's context, not actual file
6. OR agent reads a different/stale file

**Impact**:
- **Agent independence violated**
- **Evaluations based on wrong content**
- **@director becomes single point of failure**
- **Quality gates fail to catch issues**

---

## Solution: @director File Reading Ban

### Core Principle

**@director CANNOT read files that agents will evaluate**

@director's job is **coordination**, not **verification**. Verification is the agents' job.

### Forbidden Pattern

```
❌ FORBIDDEN:
@director: Read(output/docs/research_notes.md)
         → Forms understanding
         → "@advisor: Evaluate methodology quality"
         → @advisor works from @director's context

❌ FORBIDDEN:
@director: Read(output/model/model_design.md)
         → Checks completeness
         → "@validator: Verify this design"
         → @validator works from @director's understanding
```

### Required Pattern

```
✅ CORRECT:
@director: "@advisor: Read output/docs/research_notes.md and evaluate methodology quality (1-10 grade)"
         → @advisor: Read(output/docs/research_notes.md)
         → @advisor: "I read: output/docs/research_notes.md (843 lines)"
         → @advisor: Evaluates based on actual file content
         → @director: Verifies @advisor read correct file

✅ CORRECT:
@director: "@validator: Read output/model/model_design.md and verify mathematical correctness"
         → @validator: Read(output/model/model_design.md)
         → @validator: "I read: output/model/model_design.md (lines 1-450)"
         → @validator: Verifies based on actual file
         → @director: Verifies @validator read correct file
```

---

## Implementation Rules

### Rule 1: Specify Exact File Paths

**@director MUST include exact file path in delegation**

```
❌ VAGUE:
"@advisor: Evaluate the methodology quality"

✅ EXPLICIT:
"@advisor: Read output/docs/research_notes.md and evaluate methodology sophistication (1-10 grade)"

❌ VAGUE:
"@validator: Check if this model is mathematically sound"

✅ EXPLICIT:
"@validator: Read output/model/model_design_1.md and verify mathematical correctness of equations (1)-(15)"
```

**Required Elements**:
- **File path**: `output/docs/research_notes.md`
- **Task**: "evaluate methodology sophistication"
- **Output format**: "(1-10 grade)" or similar specification

### Rule 2: Agents Must Report File Read

**All agents MUST explicitly state which file they read**

**Required Report Format**:
```markdown
## File Read Verification
- **File**: output/docs/research_notes.md
- **Size**: 843 lines
- **Last modified**: 2026-01-19 12:34:56
- **Read timestamp**: 2026-01-19 12:35:10

## Evaluation
[... evaluation content based on actual file ...]
```

**Agent Prompt Template**:
```markdown
## CRITICAL: File Read Verification (MANDATORY)

When @director asks you to evaluate a file:

1. Read the EXACT file path specified by @director
2. At the START of your report, include:
   ```markdown
   ## File Read Verification
   - **File**: [exact file path]
   - **Size**: [number] lines
   - **Last modified**: [timestamp if available]
   ```
3. Base your evaluation ENTIRELY on the file content
4. Reference specific line numbers or sections
5. If file doesn't exist or is wrong, report immediately
```

### Rule 3: @director Must Verify Correct File Read

**@director's checklist after calling any agent**:

```markdown
## Agent File Read Verification

After calling [agent], verify:

- [ ] Agent specified which file was read
- [ ] File path matches expected location
- [ ] File size matches expected (e.g., 843 lines)
- [ ] Evaluation content references specific file content
- [ ] No evidence agent worked from cached context

If ANY check fails:
→ Re-call agent with EXPLICIT file path
→ "Please read [exact file path] and report which file you read"
```

**Example Verification**:
```
@director calls @advisor:
"@advisor: Read output/docs/research_notes.md and evaluate methodology"

@advisor responds:
"## File Read Verification
- File: output/docs/research_notes.md
- Size: 843 lines

## Evaluation
[...]"

@director verifies:
✓ Agent specified file: output/docs/research_notes.md
✓ File size: 843 lines (matches expected)
✓ Evaluation references specific methods from file

→ Verification passed, proceed with evaluation
```

**Example Failure**:
```
@director calls @advisor:
"@advisor: Evaluate the methodology"

@advisor responds:
"This methodology lacks sophistication. 1/10. CRITICAL FAILURE."

@director verifies:
✗ Agent did NOT specify file read
✗ Evaluation doesn't reference specific file
✗ Evidence suggests agent worked from @director's context

→ @director re-calls:
"@advisor: Please read output/docs/research_notes.md (843 lines) and evaluate.
   Report which file you read at the start of your response."
```

---

## Affected Phases

### Phase 0.5: Model Methodology Quality Gate

**OLD (v2.5.6)**:
```
@director: Read(research_notes.md) → Understands content
@director: "@advisor + @validator: Evaluate methodology quality"
Risk: Agents work from @director's context
```

**NEW (v2.5.7)**:
```
@director: "@advisor: Read output/docs/research_notes.md and evaluate methodology sophistication (1-10)"
@director: "@validator: Read output/docs/research_notes.md and evaluate technical rigor (1-10)"
@advisor: "## File Read Verification - File: output/docs/research_notes.md - Size: 843 lines [...]"
@validator: "## File Read Verification - File: output/docs/research_notes.md - Size: 843 lines [...]"
@director: Verifies both agents read the same file
```

### Phase 1: Model Design Validation (5 agents)

**OLD (v2.5.6)**:
```
@director: Read(model_design.md) → Checks completeness
@director: "Send to 5 agents for consultation"
Risk: Agents receive @director's understanding
```

**NEW (v2.5.7)**:
```
@director: "@researcher: Read output/model_proposals/model_1_draft.md and provide feedback"
@director: "@feasibility_checker: Read output/model_proposals/model_1_draft.md and evaluate feasibility"
[... same for @data_engineer, @code_translator, @advisor]
@director: Verifies all 5 agents read the same file (lines 1-934)
@director: Checks all 5 feedback files exist
@director: "@modeler: All 5 feedback files received. Read them and revise."
```

### Phase 10: Final Review

**OLD (v2.5.6)**:
```
@director: Read(paper.tex) → Skims content
@director: "@advisor: Review and approve"
Risk: @advisor works from @director's summary
```

**NEW (v2.5.7)**:
```
@director: "@advisor: Read output/paper/paper.tex and review against O-Prize standards"
@director: "@advisor: Compare against output/requirements_checklist.md"
@advisor: "## File Read Verification - File: output/paper/paper.tex - Size: 450 lines [...]"
@advisor: "## File Read Verification - File: output/requirements_checklist.md - Size: 50 lines [...]"
@director: Verifies @advisor read both files
```

---

## Agent Prompt Updates

### @director (CLAUDE.md) Updates

**Add to CRITICAL RULES section**:
```markdown
> [!CAUTION] **@director FILE READING BAN (v2.5.7)**
> - You CANNOT read files that agents will evaluate
> - You MUST specify exact file paths when delegating
> - You MUST verify agents read the correct file
> - Violation → Agent evaluations contaminated → Quality gates fail
```

**Add to Phase 0.5 section**:
```markdown
## Phase 0.5: Model Methodology Quality Gate (v2.5.7 ENHANCED)

### Entry Criteria
- @researcher completed `output/docs/research_notes.md`

### @director's Tasks (MANDATORY)

1. **DO NOT READ research_notes.md** ← NEW CONSTRAINT
2. **Call @advisor + @validator in PARALLEL with EXPLICIT file paths**:
   - "@advisor: Read output/docs/research_notes.md and evaluate methodology sophistication (1-10 grade)"
   - "@validator: Read output/docs/research_notes.md and evaluate technical rigor (1-10 grade)"
3. **Wait for both evaluations**
4. **Verify both agents read the same file**:
   - [ ] @advisor specified: "File: output/docs/research_notes.md, Size: 843 lines"
   - [ ] @validator specified: "File: output/docs/research_notes.md, Size: 843 lines"
   - [ ] File sizes match
5. **Calculate average grade**: (advisor_avg + validator_avg) / 2
6. **Decision**: [same as before]
```

### @advisor.md Updates

**Add to agent role**:
```markdown
## CRITICAL: File Read Verification (v2.5.7 MANDATORY)

> [!CAUTION]
> **[ MANDATORY] When @director asks you to evaluate a file, you MUST:**
> 1. Read the EXACT file path specified
> 2. Report file verification at the START of your response
> 3. Base evaluation ENTIRELY on file content

### File Read Verification Template

At the START of every evaluation, include:

```markdown
## File Read Verification
- **File**: [exact file path from @director's request]
- **Size**: [number] lines
- **Last modified**: [timestamp if available]
- **Read timestamp**: [current time]

## Evaluation
[... your evaluation based on file content ...]
```

### Example

**@director's request**:
"@advisor: Read output/docs/research_notes.md and evaluate methodology sophistication (1-10 grade)"

**@advisor's response**:
```markdown
## File Read Verification
- **File**: output/docs/research_notes.md
- **Size**: 843 lines
- **Last modified**: 2026-01-19 12:34:56
- **Read timestamp**: 2026-01-19 12:35:10

## Methodology Sophistication Evaluation

[... evaluation based on 843 lines of content ...]

**Grade**: 9/10
```

### If File Not Found

```markdown
## File Read Error
- **Requested file**: output/docs/research_notes.md
- **Error**: File does not exist or cannot be accessed
- **Action**: Please verify file path and re-send request
```
```

### @validator.md Updates

**Add similar file read verification section as @advisor**

---

## Testing & Verification

### Test Case 1: Correct Flow

```
Scenario: Phase 0.5 evaluation

Step 1: @director calls agents:
"@advisor: Read output/docs/research_notes.md and evaluate methodology"
"@validator: Read output/docs/research_notes.md and evaluate technical rigor"

Step 2: @advisor responds:
"## File Read Verification
- File: output/docs/research_notes.md
- Size: 843 lines
[... evaluation ...] Grade: 9/10"

Step 3: @validator responds:
"## File Read Verification
- File: output/docs/research_notes.md
- Size: 843 lines
[... evaluation ...] Grade: 9/10"

Step 4: @director verifies:
✓ @advisor read: output/docs/research_notes.md (843 lines)
✓ @validator read: output/docs/research_notes.md (843 lines)
✓ File paths match
✓ File sizes match
✓ Evaluations reference specific file content

→ Verification passed, proceed with grade calculation
```

### Test Case 2: Failure Detection

```
Scenario: Phase 0.5 evaluation, @director forgets ban

Step 1: @director (WRONG):
Read(output/docs/research_notes.md) → "I see Bayesian methods"
"@advisor: Evaluate methodology quality"

Step 2: @advisor (CONFUSED):
"This lacks methodological content. 1/10."

Step 3: @director (VERIFIES):
@advisor's response doesn't include file verification
@director realizes mistake

Step 4: @director (CORRECTS):
"@advisor: Please read output/docs/research_notes.md (843 lines) and evaluate.
   Report which file you read at the start."

Step 5: @advisor (CORRECTED):
"## File Read Verification
- File: output/docs/research_notes.md
- Size: 843 lines
[... evaluation ...] Grade: 9/10"

→ Corrected, evaluation now based on actual file
```

---

## Consequences of Violation

| Violation | Consequence |
|-----------|------------|
| @director reads evaluation target | Quality gate may fail, agent evaluations contaminated |
| @director doesn't specify file path | Agent may read wrong file, re-call required |
| Agent doesn't report file read | Re-call with explicit instruction |
| Agent reads wrong file | Re-call with exact path, verification required |

**If violation detected**:
1. **Stop current workflow**
2. **Re-call agent with EXPLICIT file path**
3. **Require file read verification**
4. **Document violation in output/docs/validation/** for future reference

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Active
