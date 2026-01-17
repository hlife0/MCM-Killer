# CLAUDE.md v2.5.5 Update Guide

> **Version**: v2.5.5
> **Date**: 2026-01-17
> **Purpose**: Guide for updating CLAUDE.md from v2.5.4 to v2.5.5

---

## Critical v2.5.5 Updates to Add to CLAUDE.md

### 1. Update Header (Lines 1-5)

**v2.5.4**:
```markdown
# MCM-Killer: Multi-Agent Competition System v2.5.4
```

**v2.5.5**:
```markdown
# MCM-Killer: Multi-Agent Competition System v2.5.5

## 🎯 Your Role: Team Captain (Director)

You are the **Director** orchestrating a **14-member MCM competition team** (13 from v2.5.4 + 1 new @time_validator).
```

### 2. Add @time_validator to Team Table

**Add to agent table** (around line 113):

```markdown
| @time_validator | **[NEW v2.5.5]** Time & Quality Validator | Validates time estimates, detects lazy implementation, prevents data fabrication | - |
```

**Update agent count**: 13 → 14 members

### 3. Add v2.5.5 Critical Updates to Phase Table

**Add to workflow table** (around line 48):

**After Phase 1**, add:
```markdown
| **1.5** | **Time Estimate Validation** | **@time_validator** | **✅ TIME_CHECK** | **5-10 min** |
```

**After Phase 4**, add:
```markdown
| **4.5** | **Implementation Fidelity Check** | **@time_validator** | **✅ FIDELITY** | **5-10 min** |
```

**After Phase 5**, add:
```markdown
| **5.5** | **Data Authenticity Verification** | **@time_validator** | **✅ ANTI_FRAUD** | **5-10 min** |
```

**Update v2.5.4 Critical Updates section** to include v2.5.5:

```markdown
**[v2.5.5 CRITICAL ENHANCEMENTS]**:
- **Phase 1.5 (NEW)**: @time_validator validates modeler's time estimates
- **Phase 4.5 (NEW)**: @time_validator checks for lazy code implementation
- **Phase 5.5 (NEW)**: @time_validator verifies data authenticity (prevents fabrication)
- **Re-verification (ENHANCED)**: Strict approval standards (3+ sentences, evidence required)
- **Re-verification (ENHANCED)**: ALL agents re-verify (not just rejecters)
- **@reader (ENHANCED)**: Selective requirements are MANDATORY for quality
- **@modeler (ENHANCED)**: Must consult @director before simplifying models
- **@director (ENHANCED)**: Systematic protocols with master checklist and priority hierarchy

**[v2.5.4 CRITICAL UPDATES]** (inherited):
- Phase 6.5, 7.5, 9.5 gates (still active)
- Multi-agent rework (enhanced in v2.5.5)
- Modeler quality standards (still active)
```

### 4. Update Critical Rules Section

**Add after existing rules** (around line 108):

```markdown
> [!CAUTION] **[v2.5.5] NEVER APPROVE LAZY RE-VERIFICATIONS**
> - Re-verification must be thorough (3+ sentences, specific evidence)
> - "Looks good, approved" is FORBIDDEN
> - Query agent if verdict < 300 characters

> [!CAUTION] **[v2.5.5] ALL AGENTS MUST RE-VERIFY**
> - When work is revised, ALL relevant agents re-verify (not just rejecters)
> - Agents who approved must verify revisions don't break their approval

> [!CAUTION] **[v2.5.5] @reader MUST TREAT ALL REQUIREMENTS AS MANDATORY**
> - "选择性/加分项/附加项" are MANDATORY for quality papers
> - Unclear data → MUST search reliable sources
> - Never mark as "optional" and skip

> [!CAUTION] **[v2.5.5] @MODELER MUST CONSULT BEFORE SIMPLIFYING**
> - Cannot unilaterally degrade to Tier 2/3
> - Must create proposal and consult @director
> - @director calls @time_validator for analysis
> - Tier 2/3 requires explicit approval

> [!CAUTION] **[v2.5.5] FOLLOW DIRECTOR PRIORITY HIERARCHY**
> - Priority 1: Data Integrity (ABSOLUTE)
> - Priority 2: Model Completeness (CRITICAL)
> - Priority 3: Code Correctness (CRITICAL)
> - Priority 4: Paper Quality (HIGH)
> - Priority 5: Efficiency (MEDIUM)
> - Priority 6: Polish (LOW)
> - Never sacrifice higher priority for lower
```

### 5. Add Director Master Checklist

**Add new section after "Critical Rules"**:

```markdown
## 📋 Director Master Checklist (v2.5.5)

**Use at start of EVERY phase**:

### Step 1: Verify Entry Conditions
- [ ] Previous phase complete?
- [ ] All required files exist?
- [ ] Previous validation gates passed?
- [ ] VERSION_MANIFEST updated?

### Step 2: Call Agent
- [ ] Provide clear instructions?
- [ ] Specify input files?
- [ ] Specify output files?
- [ ] Set expectations (time, quality)?

### Step 3: Review Agent Output
- [ ] Check agent report?
- [ ] Verify output files exist?
- [ ] Spot-check quality (5-10 items)?

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

### 6. Update Validation Gate Sections

**For MODEL validation gate** (around Phase 1):

```markdown
## Phase 1.5: MODEL Validation Gate + Time Check

**Participants** (5 agents): @researcher, @feasibility_checker, @data_engineer, @code_translator, @advisor

**v2.5.5 Enhancement**: After 5 agents complete validation:

1. Call @time_validator:
   ```
   "@time_validator: Please validate time estimates in output/model/feasibility_{i}.md
    and output/model/model_design_{i}.md"
   ```

2. Review @time_validator's report:
   - Check for discrepancies > 2x
   - If found: Query @modeler for explanation

3. Make decision:
   - If 4-5 agents approve AND time estimates reasonable → Proceed to Phase 2
   - If 2-3 agents reject → Parallel rework → ALL 5 re-verify
   - If 1 agent rejects → Single rework → Single re-verify

**Re-verification Protocol (v2.5.5)**:
- **ALL 5 agents** must re-verify (not just those who rejected)
- Each must provide detailed approval (3+ sentences, specific evidence)
- Lazy approvals (< 300 chars) → Query for details
```

**For CODE validation gate** (around Phase 4):

```markdown
## Phase 4.5: CODE Validation Gate + Fidelity Check

**Participants** (2 agents): @modeler, @validator

**v2.5.5 Enhancement**: After 2 agents complete validation:

1. Call @time_validator:
   ```
   "@time_validator: Please check implementation fidelity.
    Design: output/model/model_design_{i}.md
    Code: implementation/code/model_{i}.py"
   ```

2. Review @time_validator's report:
   - Check for unauthorized simplifications
   - Algorithm changed? (e.g., PyMC → sklearn)
   - Iterations reduced? (e.g., 10000 → 1000)
   - Features missing?

3. If major deviations found:
   - Request @code_translator rework
   - Or get @director approval if justified

4. Make decision:
   - Both approve AND no lazy implementation → Proceed to Phase 5
```

**For TRAINING validation gate** (around Phase 5):

```markdown
## Phase 5.5: TRAINING Validation Gate + Data Verification

**Participants** (2 agents): @modeler, @validator

**v2.5.5 Enhancement**: After 2 agents complete validation:

1. Call @time_validator:
   ```
   "@time_validator: Please verify data authenticity.
    Code: implementation/code/model_{i}.py
    Output: implementation/data/results_{i}.csv"
   ```

2. Review @time_validator's report:
   - Check timestamps (CSV created after training?)
   - Check file size (not too small?)
   - Check statistical properties (reasonable ranges?)
   - Check for patterns (repeating values? too perfect?)

3. If suspicious or fabricated:
   - Request @code_translator re-run with verification
   - Do NOT proceed until @time_validator approves
```

### 7. Update Rework Protocol

**Find rework section** (around line 300-400), add:

```markdown
## Enhanced Re-verification Protocol (v2.5.5)

**When sending for re-verification**:

**OLD (v2.5.4)**: Only agents who rejected re-verify

**NEW (v2.5.5)**: ALL relevant agents re-verify

**Example**:
```
Original validation:
  @researcher:          APPROVED
  @feasibility_checker: NEEDS_REVISION
  @data_engineer:       APPROVED
  @code_translator:     APPROVED
  @advisor:             NEEDS_REVISION

Re-verification set (v2.5.5): ALL 5 agents
  - @feasibility_checker, @advisor (re-verify own revisions)
  - @researcher, @data_engineer, @code_translator (verify no regression)
```

**Strict Approval Standards (v2.5.5)**:

**FORBIDDEN**:
- "Looks good, approved."
- "Fixed the issues, good to go."
- "All set, no problems found."

**REQUIRED** (minimum):
- 3+ sentences
- Specific file locations
- Evidence of checking
- No regression detected

**Example good approval**:
```
"I re-verified the revisions:
- Checked lines 45-67 in model_design_2.md
- Found that equation (1) now includes theta definition ✅
- Verified assumption 4 has justification ✅
- Confirmed no regressions in other sections ✅
All issues resolved. APPROVED."
```

**Director Enforcement**:
- If verdict < 300 characters → Query for details
- If no "checked:" or "evidence:" → Query for details
- If no specific locations → Query for details
```

### 8. Add @time_validator Agent Section

**Add new agent section** (around line 500):

```markdown
## @time_validator (NEW in v2.5.5)

**Role**: Time & Quality Validator

**Responsibilities**:
1. **Time Estimate Validation** (Phase 1.5)
   - Validates @modeler's time estimates
   - Algorithmic complexity analysis
   - Flags discrepancies > 2x

2. **Implementation Fidelity Check** (Phase 4.5)
   - Compares design vs code
   - Detects lazy simplifications
   - Flags unauthorized changes

3. **Data Authenticity Verification** (Phase 5.5)
   - Timestamp verification
   - File size verification
   - Statistical sanity checks
   - Prevents data fabrication

**When to Call**:
- After MODEL validation gate (Phase 1.5)
- After CODE validation gate (Phase 4.5)
- After TRAINING completion (Phase 5.5)

**Report Format**:
- Detailed analysis with specific evidence
- Line numbers and file locations
- Quantified discrepancies (e.g., "10x reduction")
- Clear verdict: APPROVE / FLAG / REJECT

**Integration**:
- Works alongside @validator
- Provides specialized analysis
- Does NOT replace standard validation
```

---

## Summary of Changes

**Sections to Update**:
1. Header: v2.5.4 → v2.5.5, 13 → 14 agents
2. Agent table: Add @time_validator
3. Workflow table: Add Phases 1.5, 4.5, 5.5
4. Critical rules: Add 6 new v2.5.5 cautions
5. Add: Director master checklist
6. Update: All validation gate sections with @time_validator calls
7. Update: Rework protocol with "ALL agents re-verify"
8. Add: @time_validator agent section
9. Update: v2.5.4 → v2.5.5 critical updates

**Files to Create**:
- `.claude/agents/time_validator.md` (use architecture v2.5.5 spec)

**Documents to Reference**:
- All v2.5.5 agents should reference:
  - `architectures/v2-5-5/architecture.md`
  - `architectures/v2-5-5/SUMMARY.md`
  - Agent-specific spec documents

---

**Update Date**: 2026-01-17
**Version**: v2.5.5
**Status**: Ready for implementation
