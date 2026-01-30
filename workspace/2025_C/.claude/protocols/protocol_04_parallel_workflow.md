# Protocol 4: Phase 5 Sequential Workflow

> **Purpose**: Ensure complete, accurate training results before paper writing begins
> **Owner**: @director
> **Scope**: Phase 5 (Training) → Phase 5.5 (Validation) → Phase 6-7 (Paper writing)

## Problem Statement

Parallel workflow created tolerance for incomplete data:

```
OLD (Parallel):
Phase 5A (30 min, quick results) → Phase 6-7 (paper with quick results)
    ↓
Phase 5B (6-12 hours, background) → Update paper later
```

**Problem**:
- Encourages using incomplete "quick results" for paper
- Tolerates data make-up or estimation
- Phase 5.5 validation may run before Phase 5B completes
- Time pressure justifies compromises in data accuracy

## Key Changes

### Key Change 1: Single Training Phase (No Quick Results)

**Sequential workflow**:
```
Phase 5 (6-48+ hours): Complete training for ALL models
    ↓
    WAIT for completion (no shortcuts)
    ↓
Phase 5.5: Validate complete results
    ↓
Phase 5.8: Extract insights
    ↓
Phase 6: Generate figures from complete results
    ↓
Phase 7: Write paper with complete, verified results
```

### Key Change 2: Zero Tolerance Policy

**Absolute Requirements**:
1. ALL models must complete training successfully
2. NO data make-up or estimation tolerated
3. NO quick results or parallel shortcuts
4. NO automatic fallbacks for long training times
5. Training failures = STOP and FIX (do NOT proceed)

**What Changed**:
- **Phase 5A deleted** - no more quick training
- **Phase 5B renamed to Phase 5** - full training is the only training
- **Phase 5 is BLOCKING** - paper writing CANNOT start until training completes
- **No time limit** - training may take 6-48+ hours (this is acceptable)

## Per-Model Time Expectations

**Time ranges for Phase 5 (Complete Training)**:
- **Typical**: 6-12 hours
- **Extended**: 12-24 hours (acceptable)
- **Maximum**: 48+ hours (acceptable with @director notification)

**Impact**: Paper writing waits for complete results (data accuracy is paramount)

## Implementation

### Step 1: Phase 5 Execution

**@model_trainer**:
- Execute complete training for ALL models
- Use full dataset, full iterations, full convergence
- Monitor progress (report every few hours if slow)
- Generate `results_{i}.csv` for EACH model
- Report completion ONLY when ALL models succeed

**@director decision**: WAIT for Phase 5 to complete before Phase 5.5

### Step 2: Phase 5.5 Validation

**@time_validator**:
- Verify ALL models completed (no partial results)
- Check results_{i}.csv exists for every model
- Validate training duration ≥ expected time
- Verify algorithm match, feature completeness, convergence
- AUTO-REJECT if ANY model incomplete or fabricated

**@director decision**: ONLY proceed to Phase 6 after Phase 5.5 passes

### Step 3: Paper Writing with Complete Results

**Phase 6**: @visualizer generates figures from `results_{i}.csv` (complete results)
**Phase 7**: @writer writes paper with complete, verified results

**No updates needed** - paper is written once with final results

## Quality Considerations

**Complete results (Phase 5)**:
- Full convergence, complete data → Publication quality
- No estimation, no make-up → 100% authentic
- Verified by Phase 5.5 → Data integrity guaranteed

**Paper writing strategy**:
- Write ALL sections with complete results
- No need to update later (results are final)
- Quality over speed

## Error Resolution

**If training fails**:
```
@model_trainer reports error → @director delegates fix
  - Implementation error → @code_translator
  - Data error → @data_engineer
  - Design issue → @modeler
Fix applied → Re-run training → WAIT for completion
```

**If training is slow**:
```
@model_trainer reports progress every few hours
@director acknowledges, allows training to continue
Paper writing WAITS (no shortcuts tolerated)
```

## Timeline Example

**Without Protocol 4 (Old Parallel)**:
```
Day 1: Phases 0-3 (8 hours)
Day 2: Phase 4 (2h) + Phase 5A (0.5h) → Phase 6-7 (4h) with quick results
       Phase 5B parallel (12h) → Update paper later
Total: 14.5 hours execution + 12h parallel
```

**With Protocol 4 (New Sequential)**:
```
Day 1: Phases 0-3 (8 hours)
Day 2: Phase 4 (2 hours) + Phase 5 (6-18 hours, BLOCKING)
Day 3: Phase 5.5-5.8 (1h) + Phase 6-7 (4h) with complete results
Total: 21-33 hours (longer but data is 100% accurate)
```

**Trade-off**: Time increases but data accuracy is guaranteed (worth it)

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture (parallel workflow)
- **v2.0** (2026-01-30): Restructured to sequential workflow (zero tolerance for incomplete data)
