# Workspace Setup

> **Source**: Extracted from CLAUDE.md v3.3.0
> **Purpose**: Directory and file initialization commands

## Workspace Initialization (MANDATORY)

> [!CRITICAL] **At START of EVERY competition, you MUST:**
> 1. Create all directories
> 2. Create orchestration_log.md with template
> 3. Verify all files exist
> **NEVER proceed to Phase 0 until all setup is complete.**

### Step 1: Create Directory Structure

```bash
mkdir -p output/docs/consultations output/docs/rewind output/docs/validation output/docs/insights
mkdir -p output/implementation/code output/implementation/data output/implementation/logs output/implementation/models
mkdir -p output/model output/model_proposals output/figures output/paper output/results
```

### Step 2: Create Orchestration Log (MANDATORY)

> [!CRITICAL] **You MUST create `output/docs/orchestration_log.md` with the template below BEFORE Phase 0 starts.**

Create the file with this template:

```markdown
# Orchestration Log: MCM Competition

## Metadata
- **Problem**: [To be filled by Director]
- **Start Time**: [ISO timestamp when Phase 0 starts]
- **Director**: @director
- **Target Completion**: 72 hours

## Phase Execution Table

| Phase | Name | Agent | Start | End | Duration | MINIMUM | Status | Gate | Notes |
|-------|------|-------|-------|-----|----------|---------|--------|------|-------|
| 0 | Problem Understanding | | | | | 35m | PENDING | | |
| 0.1 | External Resources | | | | | 15m | PENDING | | |
| 0.2 | Knowledge Retrieval | | | | | 20m | PENDING | | |
| 0.5 | Methodology Gate | | | | | 25m | PENDING | | |
| 1 | Model Design | | | | | 120m | PENDING | | |
| 1.5 | Time Validation | | | | | 10m | PENDING | | |
| 2 | Feasibility Check | | | | | 35m | PENDING | | |
| 3 | Data Processing | | | | | 75m | PENDING | | |
| 4 | Code Translation | | | | | 75m | PENDING | | |
| 4.5 | Fidelity Check | | | | | 10m | PENDING | | |
| 5 | Model Training | | | | | 180m | PENDING | | |
| 5.5 | Data Authenticity | | | | | 10m | PENDING | | |
| 5.8 | Insight Extraction | | | | | 25m | PENDING | | |
| 6 | Visualization | | | | | 35m | PENDING | | |
| 6.5 | Visual Gate | | | | | 10m | PENDING | | |
| 7A | Paper Framework | | | | | 25m | PENDING | | |
| 7B | Model Sections | | | | | 60m | PENDING | | |
| 7C | Results Integration | | | | | 45m | PENDING | | |
| 7D | Analysis Sections | | | | | 25m | PENDING | | |
| 7E | Conclusions | | | | | 32m | PENDING | | |
| 7F | LaTeX Compilation | | | | | 15m | PENDING | | |
| 7.5 | LaTeX Gate | | | | | 10m | PENDING | | |
| 8 | Summary | | | | | 35m | PENDING | | |
| 9 | Polish | | | | | 35m | PENDING | | |
| 9.1 | Mock Judging | | | | | 20m | PENDING | | |
| 9.5 | Editor Feedback | | | | | 20m | PENDING | | |
| 10 | Final Review | | | | | 35m | PENDING | | |
| 11 | Self-Evolution | | | | | 10m | PENDING | | |

**TOTAL MINIMUM: 1035 minutes (~17 hours)**

## Time Enforcement Reminder

> [!CRITICAL] Before marking any phase COMPLETE:
> 1. Read phase_{X}_timing.json to get actual duration
> 2. Verify Duration >= MINIMUM (from table above)
> 3. Call @time_validator and wait for APPROVE
> 4. IF Duration < MINIMUM → REJECT + FORCE RERUN (no exceptions)
> 5. "Work quality" does NOT override time requirements

## Cumulative Time Tracking
- **Total Elapsed**: 0 min
- **Phases Complete**: 0/28

## Decisions & Handoffs
[Log key decisions here]

---
*Template from workspace_setup.md v3.3.0*
```

### Step 3: Verification

**Verify directories**:
```bash
ls -la output/docs/ output/implementation/ output/model/ output/paper/
```

**Verify orchestration_log.md exists**:
```bash
cat output/docs/orchestration_log.md | head -20
```

**Checklist before Phase 0:**
- [ ] All directories exist
- [ ] `output/docs/orchestration_log.md` exists with template
- [ ] Template has MINIMUM column populated
- [ ] Time enforcement reminder is present

**NEVER proceed to Phase 0 until all checkboxes are complete.**

---

*Reference: CLAUDE.md v3.3.0 - Main operational documentation*
