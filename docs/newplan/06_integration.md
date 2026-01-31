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
| **0.1** | **External Resource Gathering** | **web_crawler, quality_checker** | **-** | **15-30m** | **NEW (parallel)** |
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

### Phase 0.1: External Resource Gathering (NEW)

**Runs parallel to Phase 0.2**

**Workflow**:
```
Director triggers @resource_manager
    └── Initialize folder structure
    └── Load config

Director triggers @web_crawler
    └── Receive keywords from Phase 0
    └── Execute search queries
    └── Fetch and stage resources

@quality_checker reviews staging/
    └── Score each resource
    └── Migrate approved to active/
    └── Reject low-quality

@knowledge_curator updates index
    └── Index new resources
    └── Prepare recommendations for Phase 0.5
```

**Timing**:
- Start: Immediately after Phase 0 completes
- Duration: 15-30 minutes
- Parallel with: Phase 0.2
- Does NOT gate: Phase 0.2 or Phase 0.5

---

### Phase 0.2: Knowledge Retrieval

**Integration**:
- @knowledge_librarian now also consults external resources
- Merge internal (HMML 2.0) with external recommendations

**Updated Output**:
```markdown
# Suggested Methods

## Internal Methods (HMML 2.0)
1. SIR Model - from knowledge_library/methods/
2. Network Analysis - from knowledge_library/methods/

## External Resources
1. WEB_001 - Network SIR paper (8.5/10)
   - Enhances our SIR approach with hub identification
2. WEB_007 - Bayesian inference guide (8.1/10)
   - Provides uncertainty quantification framework

## Recommended Combination
Use internal SIR foundation + WEB_001 network extension + WEB_007 UQ framework
```

---

### Phase 0.5: Methodology Gate

**Integration**:
- @advisor and @validator can reference external resources
- @knowledge_curator provides proactive recommendations

**Proactive Notification**:
```
Director, external resources relevant for methodology review:

HIGH PRIORITY:
- WEB_001: Validates our network approach (8.5/10)
- WEB_003: Methodology comparison study (7.8/10)

Recommend @advisor review WEB_001 Section 3 when evaluating methodology depth.
```

**Validator Check Addition**:
- If external resources support methodology → note as strength
- If methodology contradicts external resources → note as concern

---

### Phase 1: Model Design

**Integration**:
- @modeler can query @knowledge_curator for relevant resources
- Proactive recommendations provided at phase start

**Consultation Example**:
```
Director, I need external resource consultation.

**Requester**: @modeler
**Query**: Mathematical formulation for network-based SIR
**Urgency**: HIGH
```

**In Model Design Output**:
```markdown
## Model Foundation

Our network-based SIR model builds on established formulations (see WEB_001, Section 3).

### Mathematical Formulation
Following the approach in [WEB_001], we define...

### Uncertainty Quantification
We adopt the Bayesian framework from [WEB_007] with priors...
```

---

### Phase 1.5: Time Validation

**Integration**:
- @time_validator considers complexity of external references
- If model incorporates complex external methods → adjust time estimates

**New Check**:
```markdown
## External Resource Complexity Check

Referenced external resources:
- WEB_001: Network SIR (adds ~30 min implementation time)
- WEB_007: Bayesian framework (adds ~60 min for MCMC setup)

Total external resource overhead: ~90 minutes
```

---

### Phase 3: Data Processing

**Integration**:
- @data_engineer can query for external datasets
- External data sources may supplement problem data

**Query Example**:
```
Director, I need external resource consultation.

**Requester**: @data_engineer
**Query**: External datasets for epidemic validation
**Urgency**: MEDIUM
```

**Usage**:
- External datasets used for validation (not primary)
- Must document source in data_prep_1.py

---

### Phase 4: Code Translation

**Integration**:
- @code_translator can reference external implementations
- External code is REFERENCE, not copy-paste

**Usage Guidelines**:
```markdown
## External Implementation References

When referencing external code (e.g., WEB_012 PyMC3 tutorial):

✅ ALLOWED:
- Use as conceptual reference
- Adapt algorithm structure
- Cite in comments: "# Based on approach in WEB_012"

❌ NOT ALLOWED:
- Direct copy-paste
- Using without understanding
- Skipping our model design to use external implementation
```

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
- @writer cites external resources appropriately
- @knowledge_curator provides citation guidance

**Citation Format**:
```markdown
## References Section

### External Resources
[WEB_001] Author, "Title," arXiv:2401.12345, 2024.
[WEB_007] Author, "Title," Journal Name, 2023.

### In-Text Citations
"Our network formulation follows established approaches [WEB_001]..."
```

**Protocol 21 Applies**:
- All external resource citations must be accurate
- Data quoted from external sources must match

---

### Phase 9: Polish

**Integration**:
- @editor verifies external citations
- @validator checks Protocol 21 (data consistency)

**Protocol 21 Checklist**:
- [ ] All WEB_xxx citations have matching entries in references
- [ ] Data quoted from external sources matches content.md
- [ ] No broken/stale resource references

---

## Director Orchestration

### Phase 0 Completion
```
# After Phase 0 completes:
1. Extract problem keywords for @web_crawler
2. Start Phase 0.1 (external resources) in PARALLEL with Phase 0.2
3. Do NOT wait for Phase 0.1 to complete before proceeding
```

### Parallel Execution
```
Timeline:
00:00 - Phase 0 completes
00:01 - Start Phase 0.1 AND Phase 0.2 simultaneously
00:15 - Phase 0.2 completes
00:25 - Phase 0.1 completes (may be after 0.2)
00:26 - Start Phase 0.5 (has external resources available)
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

## Consultation Triggers

| Phase | Trigger | Action |
|-------|---------|--------|
| 0 → 0.1 | Problem keywords extracted | @web_crawler begins search |
| 0.1 → 0.5 | Resources approved | @knowledge_curator generates Phase 0.5 recommendations |
| 0.5 → 1 | Methodology passed | @knowledge_curator generates Phase 1 recommendations |
| 1 start | @modeler needs reference | Query @knowledge_curator |
| 3 start | @data_engineer needs data | Query @knowledge_curator |
| 4 start | @code_translator needs example | Query @knowledge_curator |
| 7 start | @writer needs citations | @knowledge_curator provides citation list |
| 9 | @validator checks consistency | Apply Protocol 21 |

---

## Fallback: No External Resources

If Phase 0.1 produces no resources:

```markdown
## Fallback Procedure

1. @web_crawler reports: "No relevant resources found"
2. Director logs: "Proceeding without external resources"
3. All subsequent phases use internal HMML 2.0 only
4. @knowledge_curator responds to queries with: "No external resources available"
5. Paper writing: No external citations (internal references only)
```

This is acceptable - external resources are SUPPLEMENTARY, not mandatory.
