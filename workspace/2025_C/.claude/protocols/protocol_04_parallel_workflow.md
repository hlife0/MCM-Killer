# Protocol 4: Phase 5 Parallel Workflow

> **Purpose**: Enable paper writing to proceed while full training runs in background, saving 6-12 hours
> **Owner**: @director
> **Scope**: Phase 5 (Training) → Phase 6-7 (Paper writing)

## Problem Statement

Sequential workflow wastes time:

```
Phase 5A (30 min) → Phase 5B (6-12 hours) → Phase 6 → Phase 7
@writer idle for 6-12 hours waiting for Phase 5B
```

## Key Changes

### Key Change 1: Phase 5A → Paper Writing Proceeds Immediately

**Parallel workflow**:
```
Phase 5A (30 min): Quick training with results_quick_*.csv
    |
Phase 6 (30 min): Generate figures from quick results
    |
Phase 7 (2-3 hours): Write paper with quick results
    |
Phase 5B (6-12 hours): Runs in parallel
```

### Key Change 2: When Phase 5B Completes

**Update process**:
1. @visualizer regenerates figures with final results
2. @writer updates Results section with final results
3. Recompile LaTeX with final figures

## Per-Model Time Expectations

**Time ranges for Phase 5B (Full Training)**:
- **Minimum**: 6 hours
- **Typical**: 8-12 hours
- **Maximum**: 48 hours (with @director approval)

**Impact**: Save 6-12 hours per competition through parallelization

## Implementation

### Step 1: Phase 5A Completion

**@model_trainer**:
- Run quick training (10-20% data, reduced iterations)
- Generate `results_quick_{i}.csv`
- Report completion

**@director decision**: ✅ PROCEED immediately to Phase 6 (don't wait for 5B)

### Step 2: Start Paper Writing in Parallel

**Phase 6**: @visualizer generates figures from `results_quick_{i}.csv`
**Phase 7**: @writer writes paper with quick results

### Step 3: Phase 5B Runs in Background

**@model_trainer**:
- Start full training in background
- Enter "watch mode" (monitor for errors)
- Report status every 30 minutes

**Phase 5B workflow**:
```
@model_trainer: "Starting Phase 5B full training in background.
Estimated: 8-12 hours.
Entering watch mode - will report errors immediately."
```

### Step 4: Update When Phase 5B Completes

**@model_trainer reports**: "Phase 5B complete for Model {i}. Results: results_{i}.csv"

**@director actions**:
1. Call @visualizer: "Regenerate figures with results_{i}.csv"
2. Call @writer: "Update Results section with final results"
3. Verify LaTeX compiles

## Quality Considerations

**Quick results (5A) vs Final results (5B)**:
- Quick: Reduced iterations, subset of data → Viable but not final
- Final: Full convergence, complete data → Publication quality

**Paper writing strategy**:
- Write Introduction, Methods, Discussion (unchanged)
- Write Results section with quick results → Update with final later
- Generate figures with quick results → Regenerate with final later

## Watch Mode (Protocol 10)

**Phase 5B runs with watch mode**:
- AI session does NOT exit
- Continuous monitoring for errors
- Immediate error notification to @director
- Fast error resolution (no restart from scratch)

**Error resolution workflow**:
```
@model_trainer detects error → Reports to @director
@director delegates fix:
  - Implementation error → @code_translator
  - Data error → @data_engineer
  - Design issue → @modeler
Fix applied → Resume training (no restart)
```

## Timeline Example

**Without Protocol 4 (Sequential)**:
```
Day 1: Phases 0-3 (8 hours)
Day 2: Phases 4-5B (14 hours)
Day 3: Phases 6-7 (4 hours)
Total: 26 hours
```

**With Protocol 4 (Parallel)**:
```
Day 1: Phases 0-3 (8 hours)
Day 2: Phase 4 (2 hours) + Phase 5A (0.5h) → Phase 6 (0.5h) + Phase 7 (3h) + Phase 5B parallel (12h)
Total: 14 hours (save 12 hours)
```

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
