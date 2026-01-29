# Prompt Template Index

This index catalogs all prompt templates available in the knowledge library for agent reference.

## Problem Analysis

Location: `knowledge_library/templates/prompts/problem_analysis/`

| Template File | Template Constant | Purpose | Usage Phase |
|---------------|-------------------|---------|-------------|
| `analysis_general.txt` | PROBLEM_ANALYSIS_PROMPT | Quick initial problem assessment | Phase 0 |
| `analysis_deep.txt` | PROBLEM_ANALYSIS_CRITIQUE_PROMPT | Detailed multi-angle analysis | Phase 0 |
| `analysis_comprehensive.txt` | PROBLEM_ANALYSIS_IMPROVEMENT_PROMPT | Full-spectrum problem understanding | Phase 0 |

**Primary Agent:** @reader
**Secondary Agents:** @researcher

---

## Method Evaluation

Location: `knowledge_library/templates/prompts/method_evaluation/`

| Template File | Template Constant | Purpose | Usage Phase |
|---------------|-------------------|---------|-------------|
| `critique_five_dimensions.txt` | METHOD_CRITIQUE_PROMPT | 5-dimensional method critique | Phase 0-1 |

**Note:** Additional evaluation templates (scoring, comparison, selection_rationale, feasibility_check) to be created based on the 5-dim framework in `critique_five_dimensions.txt`.

**Primary Agent:** @knowledge_librarian
**Secondary Agents:** @modeler, @judge_zero

---

## Modeling

Location: `knowledge_library/templates/prompts/modeling/`

| Template File | Template Constant | Purpose | Usage Phase |
|---------------|-------------------|---------|-------------|
| `modeling_basic.txt` | PROBLEM_MODELING_PROMPT | Basic modeling approach | Phase 1-2 |
| `modeling_advanced.txt` | PROBLEM_MODELING_CRITIQUE_PROMPT | Advanced multi-paradigm modeling | Phase 1-2 |
| `solution_formulation.txt` | PROBLEM_MODELING_IMPROVEMENT_PROMPT | Solution development & refinement | Phase 2-3 |

**Note:** `validation.txt` to be created for model validation strategies.

**Primary Agent:** @modeler
**Secondary Agents:** @researcher, @code_translator

---

## Task Decomposition

Location: `knowledge_library/templates/prompts/task_decomposition/`

| Template File | Template Constant | Purpose | Usage Phase |
|---------------|-------------------|---------|-------------|
| `task_decompose.txt` | TASK_DECOMPOSE_PROMPT | Break down complex problems | Phase 0-1 |
| `dependency_analysis.txt` | TASK_DEPENDENCY_ANALYSIS_PROMPT | Analyze subtask dependencies | Phase 0-1 |

**Related Resource:** `task_decomposition/decompose_prompt.json` contains 6 problem type templates (A-F) with pre-built subtask patterns.

**Primary Agent:** @researcher
**Secondary Agent:** @director

---

## Method Scoring

Location: `knowledge_library/method_scoring/`

| File | Purpose | Usage Phase |
|------|---------|-------------|
| `scoring_rubric.md` | 5-dimensional evaluation criteria | Phase 0-1 |
| `README.md` | Usage guide | Reference |

**Related Tool:** `tools/method_scorer.py` - Reference implementation for automated scoring

**Primary Agent:** @knowledge_librarian
**Secondary Agents:** @researcher, @judge_zero

---

## Usage Guidelines

### For @researcher
1. Use `task_decompose.txt` when breaking down new problems
2. Reference `decompose_prompt.json` for problem type patterns (A-F)
3. Apply `dependency_analysis.txt` to map subtask relationships
4. Use modeling templates when formulating solution approaches

### For @knowledge_librarian
1. Run `method_scorer.py` to generate scored method lists
2. Reference `scoring_rubric.md` for evaluation criteria
3. Use `critique_five_dimensions.txt` for detailed method analysis
4. Provide top-k recommendations to @researcher

### For @modeler
1. Start with `modeling_basic.txt` for single-paradigm models
2. Use `modeling_advanced.txt` for multi-paradigm approaches
3. Apply `solution_formulation.txt` when translating models to solutions
4. Reference @knowledge_librarian's scored recommendations

### For @reader
1. Begin with `analysis_general.txt` for initial problem understanding
2. Progress to `analysis_deep.txt` for detailed analysis
3. Use `analysis_comprehensive.txt` for critical/novel problems
4. Feed analysis results into @researcher's task decomposition

---

## Template Selection Flowchart

```
New Problem
    ↓
[@reader] Problem Analysis
    ├→ Simple → analysis_general.txt
    ├→ Complex → analysis_deep.txt
    └→ Critical → analysis_comprehensive.txt
        ↓
[@researcher] Task Decomposition
    ├→ Use task_decompose.txt
    ├→ Reference decompose_prompt.json (types A-F)
    └→ Apply dependency_analysis.txt
        ↓
[@knowledge_librarian] Method Selection
    ├→ Run method_scorer.py
    ├→ Use critique_five_dimensions.txt
    └→ Generate top-k scored methods
        ↓
[@modeler] Solution Formulation
    ├→ Use modeling_basic.txt OR modeling_advanced.txt
    ├→ Apply solution_formulation.txt
    └→ Validate with scoring rubric
```

---

## Maintenance Notes

- **Last Updated:** 2025-01-29
- **Source:** MM_Assets_Export/template.py
- **Total Templates:** 9 extracted + 1 JSON resource
- **Status:** ✅ Extraction complete
- **Pending:** Create additional evaluation templates (scoring, comparison, selection_rationale, feasibility_check, validation)
