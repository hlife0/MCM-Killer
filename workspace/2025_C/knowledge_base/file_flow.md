# File Flow Handoff

> **Source**: Extracted from CLAUDE.md v3.1.0
> **Purpose**: Shared files handoff reference

## Shared Files

All agents read/write to `output/`:

| File | Written By | Read By |
|------|------------|---------|
| requirements_checklist.md | @reader | Everyone |
| research_notes.md | @researcher | @modeler, @writer |
| model_design.md | @modeler | @feasibility_checker, @data_engineer, @code_translator, @writer |
| feasibility_{i}.md | @feasibility_checker | @modeler, @advisor |
| features_{i}.pkl/csv | @data_engineer | @code_translator, @model_trainer, @writer |
| model_{i}.py | @code_translator | @model_trainer, @validator, @writer |
| test_{i}.py | @code_translator | @validator |
| results_quick_{i}.csv | @model_trainer | @writer |
| figures/*.png | @visualizer | @writer |
| results_summary.md | @model_trainer | @writer |
| paper.tex | @writer | @advisor |
| advisor_review.md | @advisor | Director, @writer |

## Handoff Rules

1. **Explicit File Paths**: Always specify full path when delegating
2. **Verification**: @director must verify correct file was read
3. **No Parallel Writes**: One agent finishes → next starts
4. **Write-Then-Verify**: Write → Read back → Verify → If corrupted → delete/rewrite

---

*Reference: CLAUDE.md - Main operational documentation*
