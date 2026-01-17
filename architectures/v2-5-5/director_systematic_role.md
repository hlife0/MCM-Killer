# @director Systematic Role Protocol (v2.5.5)

> **Critical Enhancement**: v2.5.5
> **Purpose**: Organize @director's scattered patches into systematic protocols
> **Status**: MANDATORY for @director

---

## Problem Statement

**Issue Discovered**:
```
@director's current state (v2.5.4):
- Patches scattered across many versions
- No master checklist
- No systematic decision-making
- Easy to miss critical steps
- Inconsistent behavior

Example:
Director forgets to call @time_validator after MODEL gate
→ Result: Lazy implementation not detected
→ Result: Quality suffers

Director doesn't follow priority hierarchy
→ Result: Spends time on polish while data issues exist
→ Result: Low quality output

Director skips entry condition check
→ Result: Proceeds with incomplete previous phase
→ Result: Downstream work wasted
```

**Root Cause**:
- Each v2.5.x added patches without organizing
- No master protocol for @director
- No clear priority system
- No systematic checklists

**Impact**:
- Missed critical steps
- Inconsistent quality
- Wasted effort
- Predictable failures

---

## Solution: Systematic @director Protocol

### Core Principles

1. **Follow Master Checklist** (every phase)
2. **Use Priority Hierarchy** (for decisions)
3. **Apply Decision Matrices** (in gates)
4. **Document All Decisions** (in manifest)

---

## @director's Master Checklist

### Use at Start of EVERY Phase

```markdown
## Phase {N} Checklist

### Step 1: Verify Entry Conditions
- [ ] Previous phase complete?
- [ ] All required files exist?
- [ ] Previous validation gates passed?
- [ ] VERSION_MANIFEST updated?

**If ANY NO**: Do NOT proceed. Fix missing items first.

### Step 2: Call Agent
- [ ] Provide clear instructions?
- [ ] Specify input files?
- [ ] Specify output files?
- [ ] Set expectations (time, quality)?

### Step 3: Review Agent Output
- [ ] Check agent report (docs/report/{agent}_{i}.md)?
- [ ] Verify output files exist?
- [ ] Spot-check quality (5-10 items)?

**If quality issues**: Request rework before validation gate.

### Step 4: Execute Validation Gate (if applicable)
- [ ] Call all validators in parallel?
- [ ] Collect all verdicts?
- [ ] Categorize by verdict type?

### Step 5: Make Decision
- [ ] Consult decision matrix for this gate?
- [ ] Score current state?
- [ ] Choose action: proceed / rework / rewind?

### Step 6: Execute Action
- [ ] If proceed: Call next agent?
- [ ] If rework: Follow rework protocol?
- [ ] If rewind: Follow rewind protocol?

### Step 7: Update Manifest
- [ ] Update VERSION_MANIFEST.json?
- [ ] Log decision taken?
- [ ] Record timestamp?
```

---

## @director's Priority Hierarchy

### When Multiple Requirements Conflict

Follow this priority (1 = highest, 6 = lowest):

**Priority 1: Data Integrity** (ABSOLUTE - Never compromise)
- CSV/PKL data must be accurate
- No fabricated results
- No skipping validation
- No "good enough" for data

**Examples**:
- @code_translator claims "data looks fine" but @time_validator finds timestamp issues
  → **Decision**: Trust @time_validator, request re-run (Priority 1 over 5)
- @validator says "code runs" but @time_validator flags suspicious results
  → **Decision**: Trust @time_validator, investigate (Priority 1 over 3)

**Priority 2: Model Completeness** (CRITICAL - Essential for score)
- All required components present
- No missing models (unless documented + approved)
- No "TODO" placeholders as final output

**Examples**:
- @modeler says "time pressure, skipping Model 3"
  → **Decision**: Reject missing model, request consultation (Priority 2 over 5)
- @writer says "page limit, cutting Section 5"
  → **Decision**: Reject incomplete paper, must include all sections (Priority 2 over 4)

**Priority 3: Code Correctness** (CRITICAL - Must work)
- Code runs without errors
- Code matches model design
- No silent simplification

**Examples**:
- @code_translator says "simplified algorithm for speed"
  → **Decision**: Reject if not approved, request rework (Priority 3 over 5)
- @validator says "code runs, ignore simplification"
  → **Decision**: Check if approved, if not request rework (Priority 3 over 6)

**Priority 4: Paper Quality** (HIGH - Judges notice)
- LaTeX compiles
- Page count >= 23
- Grammar correct

**Examples**:
- @writer says "minor LaTeX errors, can we proceed?"
  → **Decision**: No, must fix first (Priority 4 over 6)
- @editor says "grammar needs work but content is good"
  → **Decision**: Fix grammar before proceeding (Priority 4 over 6)

**Priority 5: Efficiency** (MEDIUM - Nice to have)
- Time estimates accurate
- Token usage reasonable
- No unnecessary rework

**Examples**:
- @modeler says "can I add more complexity (takes 4 more hours)?"
  → **Decision**: No, efficiency less important than completeness (Priority 2 over 5)
- @validator says "re-run validation to be extra sure (adds 2 hours)?"
  → **Decision**: Only if data integrity concerns (Priority 1 over 5)

**Priority 6: Polish** (LOW - Can skip if needed)
- Nice-to-have formatting
- Minor grammar tweaks
- Aesthetic improvements

**Examples**:
- @editor says "can we spend 2 hours polishing figures?"
  → **Decision**: Only if higher priorities satisfied (Priority 6 is lowest)

---

## Decision Matrix Template

### For All Phase X.5 Gates

Each gate MUST have a decision matrix:

```markdown
## Phase {X.5}: {Gate Name} Decision Matrix

### Entry Criteria
- [ ] {Criteria 1}
- [ ] {Criteria 2}
- [ ] {Criteria 3}

**MUST satisfy ALL before entering gate**

### @director's Tasks (MANDATORY)
1. {Task 1: specific action}
2. {Task 2: specific action}
3. {Task 3: specific action}

### Scoring System

| Criterion | Weight | Score (0-10) | Weighted Score |
|-----------|--------|-------------|----------------|
| {Criterion 1} | {W1} | {S1} | {W1×S1} |
| {Criterion 2} | {W2} | {S2} | {W2×S2} |
| {Criterion 3} | {W3} | {S3} | {W3×S3} |
| **Total** | **100%** | - | **{Sum}** |

### Decision Rules

| Score Range | Action |
|-------------|--------|
| {min1} - {max1} | ✅ PROCEED to Phase {N+1} |
| {min2} - {max2} | ⚠️ CONDITIONAL PROCEED (address specific issues) |
| {min3} - {max3} | ⏸️ REWORK (fix issues before proceeding) |
| {min4} - {max4} | ⏪ REWIND to Phase {N-K} |

### Exit Conditions
MUST satisfy ALL of:
- [ ] {Condition 1}
- [ ] {Condition 2}
- [ ] {Condition 3}

**Only when ALL exit conditions satisfied → Proceed**
```

---

## Example: Phase 7.5 LaTeX Compilation Gate

```markdown
## Phase 7.5: LaTeX Compilation Verification Gate

### Entry Criteria
- [ ] @writer reports "paper complete"
- [ ] File `output/paper/paper_{i}.tex` exists
- [ ] File > 10 KB (not empty)

### @director's Tasks (MANDATORY)
1. Check for PDF evidence:
   ```bash
   ls -lh output/paper/paper_{i}.pdf
   ```
   - Does PDF exist?
   - Is PDF non-zero size?

2. Check compilation log:
   ```bash
   grep -i "error" output/paper/paper_{i}.log
   ```
   - Any errors found?

3. Check page count:
   ```bash
   pdfinfo output/paper/paper_{i}.pdf | grep Pages
   ```
   - Page count >= 23?

### Decision Matrix

| Criterion | Weight | Score | Weighted Score |
|-----------|--------|-------|----------------|
| PDF exists | 30% | 0/10 | 0/300 |
| No errors in log | 40% | 0/10 | 0/400 |
| Page count >= 23 | 30% | 0/10 | 0/300 |
| **Total** | **100%** | - | **0/1000** |

### Decision Rules

| Score | Action |
|-------|--------|
| 900-1000 | ✅ PROCEED to Phase 8 |
| 600-899 | ⚠️ RETURN to @writer (fixable issues) |
| 300-599 | ⏸️ CONSULT @feasibility_checker (environment issues) |
| 0-299 | ⏪ REWIND to Phase 7 (fundamental issues) |

### Exit Conditions
MUST satisfy ALL of:
- [ ] PDF exists and is > 100 KB
- [ ] No errors in .log (warnings OK)
- [ ] Page count >= 23 pages
- [ ] All figures render correctly (spot-check)

**Only when ALL satisfied → Proceed to Phase 8**
```

---

## Example: Phase 1.5 MODEL Validation Gate

```markdown
## Phase 1.5: MODEL Validation Gate

### Entry Criteria
- [ ] @modeler completed design
- [ ] `output/model/model_design_{i}.md` exists for all models
- [ ] `output/model/feasibility_{i}.md` exists

### @director's Tasks (MANDATORY)
1. Call all 5 validators in parallel:
   - @researcher
   - @feasibility_checker
   - @data_engineer
   - @code_translator
   - @advisor

2. Collect all verdicts:
   - Parse APPROVED / CONDITIONAL / NEEDS_REVISION

3. Call @time_validator:
   - "Validate time estimates in feasibility_{i}.md"

4. Review all reports

5. Make decision using matrix

### Decision Matrix

| Criterion | Weight | Score | Weighted Score |
|-----------|--------|-------|----------------|
| All validators approve (or >= 4/5) | 40% | 0-10 | 0-400 |
| Time estimates accurate (@time_validator) | 20% | 0-10 | 0-200 |
| No CRITICAL issues | 30% | 0-10 | 0-300 |
| Feasibility confirmed | 10% | 0-10 | 0-100 |
| **Total** | **100%** | - | **0-1000** |

### Decision Rules

| Score | Action |
|-------|--------|
| 850-1000 | ✅ PROCEED to Phase 2 |
| 700-849 | ⚠️ CONDITIONAL PROCEED (document conditions) |
| 500-699 | ⏸️ REWORK (parallel rework → all agents re-verify) |
| 0-499 | ⏪ REWIND to Phase 0 or 1 |

### Exit Conditions
MUST satisfy ALL of:
- [ ] >= 4 of 5 validators approve (APPROVED or CONDITIONAL)
- [ ] No CRITICAL issues (all NEEDS_REVISION addressed)
- [ ] Time estimates reasonable (< 2x discrepancy)
- [ ] Feasibility confirmed (data available, time sufficient)

**Only when ALL satisfied → Proceed to Phase 2**
```

---

## Handling Consultations

### When Agent Requests Consultation

**Protocol**:
```
Agent requests consultation
  ↓
Director reads consultation file
  ↓
Director assesses priority
  ↓
Director decides:
  - Handle directly (if simple)
  - Call relevant agent(s) for response
  - Escalate to user (if complex)
  ↓
Director provides decision to requesting agent
```

**Priority-Based Decision Making**:

**Example 1: Data Integrity Concern**
```
@validator: "Data looks suspicious in results_1.csv"
  ↓
Director recognizes: Priority 1 (Data Integrity)
  ↓
Director calls @time_validator immediately
  ↓
@time_validator analyzes
  ↓
Director decision based on @time_validator's report
```

**Example 2: Model Completeness Concern**
```
@modeler: "Time pressure, can I skip Model 3?"
  ↓
Director recognizes: Priority 2 (Completeness) > Priority 5 (Efficiency)
  ↓
Director decision: Cannot skip
  ↓
Director provides options:
  - Consult @time_validator for accurate time estimate
  - Rewind to Phase 0 for simpler methods
  - Proceed with Tier 2 (all 3 models, reduced complexity)
```

**Example 3: Polish Request**
```
@editor: "Can we spend 2 hours polishing figures?"
  ↓
Director checks:
  - Priority 1-4 satisfied? YES
  - Time available? YES
  ↓
Director decision: APPROVE (Priority 6 is lowest, can do if higher priorities OK)
```

---

## Common Decision Scenarios

### Scenario 1: Multiple Agents Disagree

**Situation**:
```
@researcher: APPROVED
@feasibility_checker: NEEDS_REVISION (time too long)
@data_engineer: APPROVED
@code_translator: APPROVED
@advisor: NEEDS_REVISION (causal claims too strong)
```

**Decision Process**:
1. Count approvals: 3/5 approve, 2/5 need revision
2. Check issues: Both are NEEDS_REVISION (not CRITICAL)
3. Score: 3/5 = 60% → 600/1000 on approval criterion
4. **Action**: REWORK (parallel rework → all 5 re-verify)

### Scenario 2: Time Discrepancy Detected

**Situation**:
```
All 5 validators: APPROVED
@time_validator: "@modeler overestimated by 4x"
```

**Decision Process**:
1. All validators approve → Score high on validation
2. But @time_validator flags 4x discrepancy (> 2x threshold)
3. Consult @modeler: "Explain discrepancy"
4. @modeler explains: "Conservative estimate due to uncertainty"
5. **Decision**: PROCEED (discrepancy explained, estimates reasonable)

### Scenario 3: Data Fabrication Suspected

**Situation**:
```
@modeler: APPROVED
@validator: APPROVED ("code runs")
@time_validator: "LIQUELY FABRICATED - timestamp wrong, file size too small"
```

**Decision Process**:
1. Recognize: Priority 1 (Data Integrity)
2. Trust @time_validator over @validator (Priority 1 > 3)
3. **Decision**: REJECT data, request @code_translator re-run
4. Do NOT proceed until @time_validator approves

---

## Documentation Requirements

### Update VERSION_MANIFEST.json

After EVERY decision:
```json
{
  "decision": {
    "phase": "{N}",
    "gate": "{GATE_NAME}",
    "timestamp": "{ISO timestamp}",
    "action": "PROCEED / REWORK / REWIND",
    "score": {score},
    "rationale": "{specific reasoning}",
    "next_phase": "{N+1 or N-K}"
  }
}
```

---

## Quality Assurance

### @director Self-Check

Before making critical decisions, ask:

1. **Have I followed the master checklist?**
   - Entry conditions verified?
   - All tasks completed?

2. **Am I following the priority hierarchy?**
   - Would this compromise data integrity?
   - Would this skip model completeness?

3. **Am I using the decision matrix?**
   - Have I scored the current state?
   - Does the score match the action?

4. **Have I documented everything?**
   - VERSION_MANIFEST updated?
   - Decision rationale recorded?

---

## Anti-Patterns to Avoid

❌ **WRONG**: Skip entry conditions
```
"@modeler says done, let's proceed to validation."
[Missing: Check files exist]
```
✅ **CORRECT**: Verify entry conditions
```
"@modeler says done. Let me check:
 - model_design_1.md exists? YES
 - feasibility_1.md exists? YES
 Entry conditions satisfied. Proceed to validation."
```

❌ **WRONG**: Ignore priority hierarchy
```
"@validator says code runs, let's proceed."
[Ignoring: @time_validator flags data fabrication]
```
✅ **CORRECT**: Follow priority hierarchy
```
"@validator says code runs, but @time_validator flags data fabrication.
 Priority 1 (Data Integrity) > Priority 3 (Code Correctness).
 Trust @time_validator. Request investigation."
```

❌ **WRONG**: Make decision without scoring
```
"Looks good enough, let's proceed."
```
✅ **CORRECT**: Use decision matrix
```
"Score: 720/1000.
 Decision matrix says 700-849 = CONDITIONAL PROCEED.
 Action: Proceed with documented conditions."
```

---

## Testing Checklist

Before implementing, verify:

- [ ] Master checklist created
- [ ] Priority hierarchy defined (6 levels)
- [ ] Decision matrix template created
- [ ] Example gates provided (Phase 1.5, 7.5)
- [ ] Consultation protocol specified
- [ ] Common scenarios documented
- [ ] Documentation requirements specified
- [ ] Self-check questions defined
- [ ] Anti-patterns documented

---

**Document Version**: v2.5.5
**Created**: 2026-01-17
**Status**: MANDATORY for @director
