# 13-Agent System Expansion Analysis

> **Date**: 2026-01-15
> **Task**: Sync v2.4.1's anti-academic fraud and data pollution mechanism
> **Objective**: Expand workspace from 10-agent to 13-agent system

---

## Executive Summary

Current workspace uses a **10-agent system** that violates v2.4.1's **separation of concerns** principle. The `coder` agent is performing duties that should be split across 4 specialized agents, creating risks of:

1. **Data pollution** (Python objects in CSV files)
2. **Incomplete feasibility checks** (skipping technical validation)
3. **Rushed implementation** (no model translation review)
4. **Insufficient training validation** (missing Phase 5A/B separation)

---

## Current vs Target Architecture

### Current Workspace (10 Agents - INCORRECT)

```
1. reader          → Problem analysis
2. researcher      → Method brainstorming
3. modeler         → Mathematical design
4. coder           → ❌ DOES TOO MUCH:
                     - Feasibility checking
                     - Data engineering
                     - Code translation
                     - Model training
5. validator       → Quality verification
6. visualizer      → Graphics creation
7. writer          → Paper writing
8. summarizer      → Summary sheet
9. editor          → Language polish
10. advisor        → Final review
```

### Target Architecture (13 Agents - CORRECT per v2.4.1)

```
1. reader               → Problem analysis
2. researcher           → Method brainstorming
3. modeler              → Mathematical design
4. feasibility_checker  → ✅ Technical feasibility assessment
5. data_engineer        → ✅ Data processing & feature engineering
6. code_translator      → ✅ Math → Python translation
7. model_trainer        → ✅ Two-phase training (5A/5B)
8. validator            → Quality verification
9. visualizer           → Graphics creation
10. writer              → Paper writing
11. summarizer          → Summary sheet
12. editor              → Language polish
13. advisor             → Final review
```

---

## Responsibility Mapping: coder → 4 Agents

### What `coder` Currently Does (WRONG)

| Phase | Task | Current Agent | Should Be |
|-------|------|---------------|-----------|
| Phase 2 | Feasibility checking | ❌ Skipped or merged | feasibility_checker |
| Phase 3 | Data processing | coder | data_engineer |
| Phase 4 | Code implementation | coder | code_translator |
| Phase 5A | Quick validation | coder (often skipped) | model_trainer |
| Phase 5B | Full training | coder | model_trainer |

### Detailed Breakdown

#### 1. feasibility_checker (Phase 2)

**Current Problem**:
- Feasibility checks are often skipped or merged into Phase 1
- No dedicated validation gate for technical feasibility
- Modeler may propose models that are computationally infeasible

**Should Do**:
- Evaluate library availability
- Assess computational resources required
- Estimate time constraints
- Generate `model/feasibility_{i}.md`
- Participate in MODEL and CODE validation gates

**Validation Gate**: MODEL (alongside validator)

---

#### 2. data_engineer (Phase 3)

**Current Problem**:
- coder may skip data quality checks
- Python objects (lists, dicts) can pollute CSV files
- No `check_data_quality()` function enforcement
- Data cleaning and feature engineering mixed with coding

**Should Do**:
- Read and clean raw data
- Create features per model_design specification
- **[v2.4.1 CRITICAL] Enforce data integrity**:
  - CSV cells must be scalar only (int, float, str, bool)
  - No serialized Python objects (`['a', 'b']` or `{'x': 1}`)
  - Must include `check_data_quality(df)` function
- Generate `implementation/data/features_{i}.pkl` and `.csv`

**No Validation Participation** (but must self-correct)

---

#### 3. code_translator (Phase 4)

**Current Problem**:
- Mathematical models translated to code without dedicated review
- No standardized code structure
- Test code often missing
- Implementation consistency issues

**Should Do**:
- Translate model_design mathematics to Python
- Generate `implementation/code/model_{i}.py` with standard structure:
  - `load_features()`
  - `train_model()`
  - `predict()`
  - `main()`
- Generate `implementation/code/test_{i}.py`
- Ensure code matches mathematical specification exactly

**Validation Gate**: CODE, TRAINING

---

#### 4. model_trainer (Phase 5A/5B)

**Current Problem**:
- Phase 5 often skipped or rushed
- No separation between quick validation (5A) and full training (5B)
- Training failures discovered too late
- No mandatory sanity checks

**Should Do**:
- **Phase 5A (MANDATORY)**:
  - Use 10-20% data, reduced iterations
  - Ensure code runs, model viable
  - Output: `results_quick_{i}.csv`
  - Time: ≤30 minutes
  - **Never skip for "time constraints"**

- **Phase 5B (OPTIONAL)**:
  - Full dataset, full convergence
  - Complete diagnostics
  - Output: `results_{i}.csv`
  - Time: 4-6 hours
  - Can mark as "future optimization" if needed

**No Validation Participation** (but must sanity check)

---

## Phase Workflow Changes

### Current (10-Agent System)

```
Phase 0: reader + researcher
Phase 1: modeler
Phase 2: ❌ SKIPPED or merged into Phase 1
Phase 3: coder (data processing)
Phase 4: coder (code implementation)
Phase 5: coder (training - often incomplete)
Phase 6: visualizer
Phase 7: writer
Phase 8: summarizer
Phase 9: editor
Phase 10: advisor
```

### Target (13-Agent System)

```
Phase 0: reader + researcher
Phase 1: modeler
Phase 2: ✅ feasibility_checker (NEW - validates technical feasibility)
Phase 3: ✅ data_engineer (NEW - data integrity enforced)
Phase 4: ✅ code_translator (NEW - standardized translation)
Phase 5A: ✅ model_trainer (NEW - mandatory quick validation)
Phase 5B: ✅ model_trainer (optional full training)
Phase 6: visualizer
Phase 7: writer
Phase 8: summarizer
Phase 9: editor
Phase 10: advisor
```

---

## v2.4.1 Anti-Fraud Mechanisms to Integrate

### 1. Data Integrity Standards (from data_engineer)

**Scalar Principle**:
```
✅ ALLOWED in CSV: int, float, str (pure), bool
❌ FORBIDDEN in CSV: lists, dicts, numpy objects, serialized strings
```

**Mandatory Self-Check**:
```python
def check_data_quality(df):
    # Check for object types that might be serialized lists/dicts
    for col in df.select_dtypes(include=['object']):
        if df[col].astype(str).str.contains(r'^\[|^\{').any():
            raise ValueError(f"Column {col} contains serialized Python objects!")

    # Check for duplicates
    if df.duplicated().any():
        raise ValueError(f"Data contains {df.duplicated().sum()} duplicate rows!")

    print("✅ Data Quality Check Passed")
```

### 2. Completeness Mandate (from model_trainer)

**Phase 5A is MANDATORY**:
- Never skip for "time constraints"
- At minimum: Quick validation with reduced data
- If time permits: Full training (5B)
- Explicitly mark 5B status in report

**Forbidden Behaviors**:
```
❌ Skip Phase 5 entirely
❌ Use "time constraints" as excuse to skip 5A
❌ Output "TODO" or "待训练" placeholders
```

### 3. Defensive Agent Engineering (from all agents)

**Verify-Before-Submit**:
- Automated pre-validation
- Self-correction before submission
- No simplification allowed
- Quality > Efficiency

**When Token Limits Hit**:
- PAUSE and request user intervention
- DO NOT skip phases or simplify outputs

---

## Implementation Plan

### Step 1: Update CLAUDE.md

**Changes Required**:
1. Update "10-member team" → "13-member team"
2. Update phase workflow table to include Phase 2
3. Update agent roster table to include 4 new agents
4. Update consultation protocol to include new agents
5. Update shared files section

### Step 2: Create 4 New Agent Files

**With YAML frontmatter**:
```yaml
---
name: {agent_name}
description: {brief description}
tools: {list of tools}
model: opus
---
```

**Agents to create**:
1. `feasibility_checker.md`
2. `data_engineer.md`
3. `code_translator.md`
4. `model_trainer.md`

**Language**: English (v2.5.0 reference is in Chinese, but workspace uses English)

### Step 3: Update Existing 10 Agents

**Agents to update**:
1. `reader.md` - Add Phase 2 consultation trigger
2. `researcher.md` - Add feasibility consultation
3. `modeler.md` - Add Phase 2 gate requirement
4. `coder.md` - **RENAME or DEPRECATE** (split into 4 agents)
5. `validator.md` - Update for new validation gates
6. `visualizer.md` - Update data source paths
7. `writer.md` - Update Phase 5A/5B result handling
8. `summarizer.md` - No major changes
9. `editor.md` - No major changes
10. `advisor.md` - Update review criteria for 13-agent workflow

### Step 4: Update Phase Validation Gates

**New Gates**:
- **MODEL**: feasibility_checker + validator (Phase 2)
- **DATA**: (no gate, but data_engineer self-checks)
- **CODE**: code_translator + validator (Phase 4)
- **TRAINING**: model_trainer self-check + advisor review (Phase 5)

---

## Risk Analysis

### High-Risk Areas

1. **Backward Compatibility**:
   - Existing workflow expects 10 agents
   - Need to update all references to `coder`

2. **Coordination Complexity**:
   - More agents = more communication overhead
   - Need clear handoff protocols

3. **Token Usage**:
   - 4 additional agents may increase context switching
   - Need efficient consultation mechanisms

### Mitigation Strategies

1. **Clear Agent Boundaries**:
   - Each agent has specific, non-overlapping duties
   - Handoff protocols documented

2. **Phased Rollout**:
   - Create new agents first
   - Update existing agents second
   - Test with sample problem third

3. **Documentation Updates**:
   - CLAUDE.md as single source of truth
   - Agent files reference each other appropriately

---

## Success Criteria

✅ All 13 agents created with YAML frontmatter
✅ CLAUDE.md updated for 13-agent coordination
✅ Existing 10 agents updated for consistency
✅ Phase workflow includes Phase 2 (feasibility_checker)
✅ Data integrity standards enforced (data_engineer)
✅ Phase 5A mandatory requirement enforced (model_trainer)
✅ Validation gates updated for new agent roles
✅ No duplicate responsibilities across agents
✅ All agent files use English language

---

## References

- v2.4.1 architecture.md (lines 44-57: agent list)
- v2.4.1 methodology.md (data integrity standards)
- v2.4.1 retrospective.md (anti-fraud mechanisms)
- v2.5.0 agents/feasibility_checker.md
- v2.5.0 agents/data_engineer.md
- v2.5.0 agents/code_translator.md
- v2.5.0 agents/model_trainer.md

---

**Next Step**: Update CLAUDE.md for 13-agent system
