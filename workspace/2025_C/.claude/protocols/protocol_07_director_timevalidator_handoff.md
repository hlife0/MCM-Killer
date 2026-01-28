# Protocol 7: @director/@time_validator Handoff

> **Purpose**: Standardize communication between @director and @time_validator for consistent decision-making
> **Owner**: @director + @time_validator
> **Scope**: Phases 1.5, 4.5, 5.5

## Problem Statement

Inconsistent communication leads to misinterpretations and poor decisions:

```
@director: "Check if the time estimates look good"
@time_validator: "Looks fine" (what does "fine" mean?)
Result: Ambiguous decision-making
```

## Standardized Communication

### Step 1: @director's Call to @time_validator (Explicit)

**Template**:
```
"@time_validator: Validate time estimates for Phase 5B.

Read:
- output/model/model_design_*.md
- output/implementation/data/features_*.pkl
- output/implementation/code/model_*.py

Provide:
1. Per-model time estimate
2. Total time estimate
3. Algorithm fidelity check
4. Feature completeness check
5. Recommendation: APPROVE/REJECT/ESCALATE"
```

**Example call**:
```
"@time_validator: Validate time estimates for all 3 models.

Files:
- output/model/model_design_1.md
- output/model/model_design_2.md
- output/model/model_design_3.md
- output/implementation/data/features_*.pkl
- output/implementation/code/model_*.py

Provide:
1. Per-model breakdown (algorithm, dataset, iterations, estimated time)
2. Total time estimate with range
3. Algorithm fidelity (design vs code match?)
4. Feature completeness (all features present?)
5. Recommendation: APPROVE/REJECT/ESCALATE"
```

### Step 2: @time_validator's Response (Standardized)

**Template**:
```
Files Read Verification:
- Read: model_design_1.md (324 lines)
- Read: features_1.pkl (shape: (5000, 50))
- Read: model_1.py (215 lines)

Per-Model Breakdown:
- Model 1: PyMC hierarchical, 5000×50, 10000×4 chains
  - Estimated: 12-15 hours
  - Algorithm: Exact match (PyMC)
  - Features: All 15 present
  - Verdict: VALID

Total Estimate: 48 hours (range: 36-72 hours)
Recommendation: APPROVE (total < 48h threshold)
```

**Example response**:
```
Files Read Verification:
- Read: model_design_1.md (324 lines, last modified: 2026-01-28 10:30)
- Read: model_design_2.md (298 lines)
- Read: model_design_3.md (412 lines)
- Read: features_1.pkl (shape: (5000, 50), 8.2 MB)
- Read: features_2.pkl (shape: (5000, 50), 8.2 MB)
- Read: features_3.pkl (shape: (5000, 50), 8.2 MB)
- Read: model_1.py (215 lines)
- Read: model_2.py (198 lines)
- Read: model_3.py (242 lines)

Per-Model Breakdown:
- Model 1: PyMC hierarchical, 5000×50, 10000×4 chains
  - Estimated: 12-15 hours
  - Algorithm: Exact match (PyMC with NUTS sampler)
  - Features: All 15 present (Gold, Silver, Bronze, Host, etc.)
  - Verdict: VALID

- Model 2: PyMC hierarchical, 5000×50, 10000×4 chains
  - Estimated: 12-15 hours
  - Algorithm: Exact match (PyMC with NUTS sampler)
  - Features: All 15 present
  - Verdict: VALID

- Model 3: PyMC non-hierarchical, 5000×50, 15000×4 chains
  - Estimated: 18-20 hours
  - Algorithm: Exact match (PyMC with NUTS sampler)
  - Features: All 15 present
  - Verdict: VALID

Total Estimate: 48 hours (range: 36-72 hours)
Recommendation: APPROVE (total = 48h threshold, acceptable)
```

### Step 3: @director's Decision (Standardized)

**Decision logic**:
```
IF recommendation == "APPROVE" AND total_estimate <= 48 hours:
    RETURN "PROCEED to Phase 5B"
ELIF recommendation == "REJECT":
    RETURN "BLOCK - Address issues first"
ELIF recommendation == "ESCALATE":
    RETURN "CONSULT @modeler for decision"
ELSE:
    RETURN "QUERY - Need clarification"
```

## Communication Quality Standards

### @director's Call Quality

**REQUIRED elements**:
- [ ] Explicit file paths
- [ ] Clear request (time validation, fidelity check, etc.)
- [ ] Expected output format
- [ ] Decision context (Phase 1.5, 4.5, or 5.5?)

**FORBIDDEN**:
- [ ] "Check if it's good" (too vague)
- [ ] "Look at the models" (what models? what aspect?)
- [ ] "What do you think?" (no criteria)

### @time_validator's Response Quality

**REQUIRED elements**:
- [ ] Files read verification (path, size, timestamp)
- [ ] Per-model breakdown
- [ ] Total estimate with range
- [ ] Fidelity checks (algorithm, features, parameters)
- [ ] Clear recommendation (APPROVE/REJECT/ESCALATE)

**FORBIDDEN**:
- [ ] "Looks good" (no specifics)
- [ ] "Should work" (no analysis)
- [ ] "Seems fine" (no verification)

## Common Mistakes to Avoid

**MISTAKE 1**: Vague @director call
```
"@time_validator: Check the models"
Result: @time_validator doesn't know what to check
```

**MISTAKE 2**: Missing files in @time_validator response
```
"Model 1: 12 hours"
What about algorithm? Features? Fidelity?
Result: @director can't make informed decision
```

**MISTAKE 3**: No clear recommendation
```
"Total estimate: 52 hours"
So... approve or reject?
Result: Ambiguous decision-making
```

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
