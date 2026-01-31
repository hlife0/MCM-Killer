# Integration with 22-Phase Workflow

> **Version**: 3.2.0
> **Purpose**: Define how external resources pipeline integrates with existing phases

---

## Phase Table Update

### New Phase: 0.1 (External Resource Gathering)

Insert between Phase 0 and Phase 0.2:

| Phase | Name | Agent | Gate | Time | Notes |
|-------|------|-------|------|------|-------|
| 0 | Problem Understanding | reader, researcher | - | 30m | Unchanged |
| **0.1** | **External Resource Processing** | **resource_ingestor, quality_checker** | **-** | **10-30m** | **NEW (parallel)** |
| 0.2 | Knowledge Retrieval | knowledge_librarian | - | 10-15m | Now includes external resources |
| 0.5 | Methodology Gate | advisor, validator | ✅ METHODOLOGY | 15-20m | Can reference external resources |

**Critical**: Phase 0.1 runs IN PARALLEL with Phase 0.2 - it does NOT block the workflow.

---

## Integration Points by Phase

### Phase 0: Problem Understanding

**Integration**:
- @reader extracts problem keywords → trigger search terms for Phase 0.1
- No external resources used yet (internal focus)

**Output for Phase 0.1**:
```json
{
  "problem_keywords": ["epidemic", "network", "prediction", "intervention"],
  "domain": "epidemiology",
  "suggested_methods": ["SIR", "network analysis", "optimization"]
}
```

---

### Phase 0.1: External Resource Processing (NEW)

**Runs parallel to Phase 0.2**

**Workflow**:
```
User drops files in inbox/
    └── .py, .m, .cpp, .md, .pdf, .csv, etc.

Director triggers @resource_ingestor
    └── Monitor inbox/ folder
    └── Process manual uploads
    └── Generate metadata + SHA-256 hash
    └── Move to staging/

@quality_checker reviews staging/
    └── Syntax check for code (HARD CONSTRAINT)
    └── Score each resource (40% actionability for code)
    └── Migrate approved to active/
    └── Reject low-quality or syntax failures

@knowledge_curator updates index
    └── Index new resources
    └── Update summary_for_agents.md (context overlay)
```

**Timing**:
- Start: Immediately after Phase 0 completes
- Duration: 10-30 minutes
- Parallel with: Phase 0.2
- Does NOT gate: Phase 0.2 or Phase 0.5

---

### Phase 0.2: Knowledge Retrieval

**Integration**:
- @knowledge_librarian reads `summary_for_agents.md` before starting
- Merge internal (HMML 2.0) with approved external resources
- External resources are SUPPLEMENTARY - internal takes priority

**Updated Output**:
```markdown
# Suggested Methods

## Internal Methods (HMML 2.0)
1. SIR Model - from knowledge_library/methods/
2. Network Analysis - from knowledge_library/methods/

## External Resources (from summary_for_agents.md)
1. MAN_001 - Network SIR implementation (8.5/10)
   - Enhances our SIR approach with hub identification
   - Path: active/MAN_001/content.py
2. MAN_007 - Bayesian inference guide (8.1/10)
   - Provides uncertainty quantification framework
   - Path: active/MAN_007/content.md

## Recommended Combination
Use internal SIR foundation + MAN_001 network extension + MAN_007 UQ framework
```

---

### Phase 0.5: Methodology Gate

**Integration**:
- @advisor and @validator read `summary_for_agents.md` before starting
- External resources inform methodology validation

**Context from summary_for_agents.md**:
```
From summary_for_agents.md Quick Reference:
| Agent | Recommended Resources | Priority |
|-------|----------------------|----------|
| @advisor | MAN_001, MAN_003 | HIGH |
| @validator | MAN_002 | MEDIUM |
```

**Validator Check Addition**:
- If external resources support methodology → note as strength
- If methodology contradicts external resources → note as concern
- Verify SHA-256 hashes if citing specific data

---

### Phase 1: Model Design

**Integration**:
- @modeler reads `summary_for_agents.md` before starting (MANDATORY)
- Check "Quick Reference" for recommended resources
- Resources are SUPPLEMENTARY - internal HMML 2.0 takes priority

**Before Starting Work**:
```markdown
## @modeler Pre-Work Checklist

1. Read `output/external_resources/active/summary_for_agents.md`
2. Check "Quick Reference" for @modeler resources
3. If relevant resources exist:
   - Read the summary for Phase 1
   - Access content files if needed (paths provided)
4. Proceed with model design
```

**In Model Design Output**:
```markdown
## Model Foundation

Our network-based SIR model builds on established formulations.

### Mathematical Formulation
Following the approach documented in [MAN_001], we define...
(See: active/MAN_001/content.py for implementation reference)

### Uncertainty Quantification
We adopt the Bayesian framework from [MAN_007] with priors...
(See: active/MAN_007/content.md for methodology details)
```

---

### Phase 1.5: Time Validation

**Integration**:
- @time_validator reads `summary_for_agents.md` to understand external references
- If model incorporates complex external methods → adjust time estimates

**New Check**:
```markdown
## External Resource Complexity Check

Referenced external resources:
- MAN_001: Network SIR (adds ~30 min implementation time)
- MAN_007: Bayesian framework (adds ~60 min for MCMC setup)

Total external resource overhead: ~90 minutes

## Hash Verification
Run: python docs/newplan/10_tools/indexer.py verify
All file hashes: VALID
```

---

### Phase 3: Data Processing

**Integration**:
- @data_engineer reads `summary_for_agents.md` before starting
- Check for external datasets in "By Phase" section
- External data sources may supplement problem data

**Before Starting**:
```markdown
## @data_engineer Pre-Work Checklist

1. Read `output/external_resources/active/summary_for_agents.md`
2. Check "Phase 3: Data Processing" section for relevant resources
3. If external datasets exist:
   - Verify hash integrity before use
   - Document source in data_prep_1.py
4. Proceed with data processing
```

**Usage**:
- External datasets used for validation (not primary)
- Must document source in data_prep_1.py
- Verify hash: `python docs/newplan/10_tools/indexer.py verify-one <resource_id>`

---

### Phase 4: Code Translation

**Integration**:
- @code_translator reads `summary_for_agents.md` before starting
- Check for code resources in "Phase 4: Code Translation" section
- External code is REFERENCE, not copy-paste

**Usage Guidelines**:
```markdown
## External Implementation References

When referencing external code (e.g., MAN_001 Python implementation):

✅ ALLOWED:
- Use as conceptual reference
- Adapt algorithm structure
- Cite in comments: "# Based on approach in MAN_001"

❌ NOT ALLOWED:
- Direct copy-paste
- Using without understanding
- Skipping our model design to use external implementation
```

**Code Resource Note**: External code files (.py, .m, .cpp) have been syntax-validated before approval. Actionability weight is 40%.

---

### Phase 4.5: Implementation Fidelity

**Integration**:
- @time_validator verifies external references are properly adapted
- Check that code implements OUR model, not just external example

**New Check**:
```markdown
## External Reference Fidelity

If code references external resources:
- [ ] External code adapted, not copied
- [ ] Implements our model_design.md, not external model
- [ ] External reference noted in comments
- [ ] Our parameters used, not external defaults
```

---

### Phase 5: Model Training

**Integration**:
- Minimal external resource usage (focus on execution)
- May reference external for troubleshooting convergence

---

### Phase 5.5: Data Authenticity

**Integration**:
- @time_validator may cross-reference external data for sanity checks

**New Check**:
```markdown
## External Validation Cross-Check

If external resources contain comparable data:
- Compare our predictions with external benchmarks
- Flag if results diverge significantly from literature
```

---

### Phase 7: Paper Writing

**Integration**:
- @writer reads `summary_for_agents.md` before starting
- Check "Phase 7: Paper Writing" section for citation resources
- @knowledge_curator has tagged resources by phase

**Citation Format**:
```markdown
## References Section

### External Resources
[MAN_001] bayesian_sir_model.py, local resource, 2026.
[MAN_007] optimization_paper.md, local resource, 2026.

### In-Text Citations
"Our network formulation follows established approaches [MAN_001]..."
```

**Protocol 21 Applies**:
- All external resource citations must be accurate
- Data quoted from external sources must match original content
- **SHA-256 hash verification** ensures file integrity
- Run: `python docs/newplan/10_tools/indexer.py verify`

---

### Phase 9: Polish

**Integration**:
- @editor verifies external citations
- @validator checks Protocol 21 (data consistency)

**Protocol 21 Checklist**:
- [ ] All MAN_xxx citations have matching entries in references
- [ ] Data quoted from external sources matches content.md
- [ ] No broken/stale resource references
- [ ] **SHA-256 hashes verified**: `python docs/newplan/10_tools/indexer.py verify`
- [ ] File integrity maintained after any manual edits

---

## Director Orchestration

### Phase 0 Completion
```
# After Phase 0 completes:
1. Check if user has dropped files in inbox/
2. Start Phase 0.1 (@resource_ingestor) in PARALLEL with Phase 0.2
3. Do NOT wait for Phase 0.1 to complete before proceeding
```

### Parallel Execution
```
Timeline:
00:00 - Phase 0 completes
00:01 - Start Phase 0.1 AND Phase 0.2 simultaneously
00:15 - Phase 0.2 completes
00:25 - Phase 0.1 completes (may be after 0.2)
00:26 - Start Phase 0.5 (has external resources available via summary_for_agents.md)
```

### Resource Availability Check
Before phases that may use external resources:
```python
def check_resources_available():
    """Check if external resources are ready for consultation."""
    index = load_index()
    if index["total_resources"] > 0:
        return True, f"{index['total_resources']} resources available"
    else:
        return False, "No external resources yet (Phase 0.1 may still be running)"
```

---

## Consultation Triggers (Passive Model)

| Phase | Trigger | Action |
|-------|---------|--------|
| 0 → 0.1 | User drops files in inbox/ | @resource_ingestor processes them |
| 0.1 → All | Resources approved | @knowledge_curator updates summary_for_agents.md |
| Any phase start | Agent begins work | Agent reads summary_for_agents.md (MANDATORY) |
| 7 start | @writer needs citations | Check summary_for_agents.md "Phase 7" section |
| 9 | @validator checks consistency | Apply Protocol 21, run hash verification |

---

## Fallback: No External Resources

If Phase 0.1 produces no resources (no files in inbox/):

```markdown
## Fallback Procedure

1. @resource_ingestor reports: "inbox/ is empty, no resources to process"
2. Director logs: "Proceeding without external resources"
3. All subsequent phases use internal HMML 2.0 only
4. summary_for_agents.md shows: "No external resources available"
5. Paper writing: No external citations (internal references only)
```

This is acceptable - external resources are SUPPLEMENTARY, not mandatory.
