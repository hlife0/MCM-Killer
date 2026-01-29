# Prompt to Agent Mapping Table

This document maps all prompt templates to their primary and secondary agents, along with usage phases and file locations.

## Problem Analysis Templates

| Template File | Template Constant | Primary Agent | Secondary Agents | Phase Usage | Purpose |
|---------------|-------------------|---------------|------------------|-------------|---------|
| `problem_analysis/analysis_general.txt` | PROBLEM_ANALYSIS_PROMPT | @reader | @researcher | Phase 0 | Quick initial problem assessment |
| `problem_analysis/analysis_deep.txt` | PROBLEM_ANALYSIS_CRITIQUE_PROMPT | @reader | @researcher | Phase 0 | Detailed multi-angle analysis |
| `problem_analysis/analysis_comprehensive.txt` | PROBLEM_ANALYSIS_IMPROVEMENT_PROMPT | @reader | @researcher | Phase 0 | Full-spectrum problem understanding |

**Location**: `knowledge_library/templates/prompts/problem_analysis/`

**Usage Pattern**:
```
Initial Problem
  ↓
1. Start with analysis_general.txt (quick assessment)
  ↓
2. If complex → analysis_deep.txt (detailed)
  ↓
3. If critical/novel → analysis_comprehensive.txt (exhaustive)
```

**Output To**: @researcher's task decomposition

---

## Method Evaluation Templates

| Template File | Template Constant | Primary Agent | Secondary Agents | Phase Usage | Purpose |
|---------------|-------------------|---------------|------------------|-------------|---------|
| `method_evaluation/critique_five_dimensions.txt` | METHOD_CRITIQUE_PROMPT | @knowledge_librarian | @modeler, @judge_zero | Phase 0-1 | Detailed 5-dimensional method critique |

**Location**: `knowledge_library/templates/prompts/method_evaluation/`

**Note**: Additional evaluation templates to be created:
- `evaluation_scoring.txt` - Quantitative scoring
- `comparison.txt` - Side-by-side method comparison
- `selection_rationale.txt` - Selection framework
- `feasibility_check.txt` - Practical feasibility assessment

**Five Dimensions**:
1. Applicability (适用性) - Problem fit
2. Feasibility (可行性) - Implementation practicality
3. Cost/Efficiency (成本/效率) - Resource requirements
4. Risk (风险) - Failure likelihood
5. Clarity (清晰度) - Implementation clarity

**Output To**: @researcher's method selection

---

## Modeling Templates

| Template File | Template Constant | Primary Agent | Secondary Agents | Phase Usage | Purpose |
|---------------|-------------------|---------------|------------------|-------------|---------|
| `modeling/modeling_basic.txt` | PROBLEM_MODELING_PROMPT | @modeler | @researcher | Phase 1-2 | Basic modeling approach |
| `modeling/modeling_advanced.txt` | PROBLEM_MODELING_CRITIQUE_PROMPT | @modeler | @researcher | Phase 1-2 | Advanced multi-paradigm modeling |
| `modeling/solution_formulation.txt` | PROBLEM_MODELING_IMPROVEMENT_PROMPT | @modeler | @code_translator | Phase 2-3 | Solution development & refinement |

**Location**: `knowledge_library/templates/prompts/modeling/`

**Note**: `validation.txt` to be created for model validation strategies

**Template Selection Guide**:
```
Simple Problem (Single Domain)
→ Use modeling_basic.txt
→ Focus on clarity, interpretability

Complex Problem (Multi-Domain)
→ Use modeling_advanced.txt
→ Emphasize novelty, sophistication
```

**Integration**: Consult @knowledge_librarian's scored recommendations before selecting template

---

## Task Decomposition Templates

| Template File | Template Constant | Primary Agent | Secondary Agents | Phase Usage | Purpose |
|---------------|-------------------|---------------|------------------|-------------|---------|
| `task_decomposition/decompose_prompt.json` | N/A (JSON structure) | @researcher | @director | Phase 0-1 | Subtask patterns for 6 problem types (A-F) |
| `task_decomposition/task_decompose.txt` | TASK_DECOMPOSE_PROMPT | @researcher | @director | Phase 0-1 | Break down complex problems |
| `task_decomposition/dependency_analysis.txt` | TASK_DEPENDENCY_ANALYSIS_PROMPT | @researcher | @director | Phase 0-1 | Analyze subtask dependencies |

**Location**: `knowledge_library/templates/task_decomposition/`

**Problem Types**:
- Type A: Continuous Optimization (objective function, constraints)
- Type B: Discrete/Combinatorial (integer variables, scheduling)
- Type C: Prediction/Forecasting (historical data, future values)
- Type D: Evaluation/Selection (multi-criteria, ranking)
- Type E: Simulation/Modeling (system dynamics, stochastic)
- Type F: Classification/Clustering (unsupervised/supervised learning)

**Usage Workflow**:
```markdown
1. @reader identifies problem type (A-F)
2. @researcher loads corresponding template from decompose_prompt.json
3. @researcher adapts template to specific problem requirements
4. @researcher uses task_decompose.txt for breakdown
5. @researcher uses dependency_analysis.txt for mapping relationships
```

---

## Method Scoring

| File | Purpose | Primary Agent | Secondary Agents | Phase Usage |
|------|---------|---------------|------------------|-------------|
| `method_scoring/scoring_rubric.md` | 5-dim evaluation criteria | @knowledge_librarian | @judge_zero | Phase 0-1 |
| `tools/method_scorer.py` | Automated scoring implementation | @knowledge_librarian | @researcher | Phase 0-1 |

**Location**: `knowledge_library/method_scoring/` and `tools/`

**Scoring Framework**:
- Each method scored on 5 dimensions (0-10 scale)
- Total score = average of all dimensions
- Methods ranked by total score
- Top-k methods (k=6-10) returned with justifications

**Integration**: @knowledge_librarian applies rubric when evaluating methods for @researcher

---

## Cross-Agent Workflow

### Phase 0: Problem Understanding

```
@reader (uses analysis templates)
  ↓
analysis_general.txt → quick assessment
  ↓ (if complex)
analysis_deep.txt → detailed analysis
  ↓ (if critical)
analysis_comprehensive.txt → exhaustive analysis
  ↓
Output: Problem type + domain + requirements
```

### Phase 0-1: Task Decomposition & Method Selection

```
@researcher (receives from @reader)
  ↓
Identify problem type (A-F)
  ↓
Load decompose_prompt.json (Type template)
  ↓
Use task_decompose.txt → breakdown
  ↓
Use dependency_analysis.txt → map dependencies
  ↓
Request method consultation from @knowledge_librarian
```

### Phase 0.2: Knowledge Retrieval

```
@knowledge_librarian (receives from @researcher)
  ↓
Query HMML 2.0 for candidate methods
  ↓
Apply scoring_rubric.md (5-dim evaluation)
  ↓
Use critique_five_dimensions.txt → detailed analysis
  ↓
Rank methods by total score
  ↓
Output: Top-k methods with scores + justifications
```

### Phase 1-2: Model Design

```
@modeler (receives from @researcher)
  ↓
Review @knowledge_librarian's scored methods
  ↓
Select appropriate template:
  - modeling_basic.txt (single-paradigm)
  - modeling_advanced.txt (multi-paradigm)
  ↓
Design mathematical model
  ↓
Use solution_formulation.txt → translate to solution
  ↓
Output: model_design.md with equations
```

---

## Template Selection Decision Trees

### For @reader: Problem Analysis

```
Problem Arrives
  ├→ Straightforward, single domain?
  │  └→ Use analysis_general.txt (quick)
  ├→ Multiple domains, hidden complexities?
  │  └→ Use analysis_deep.txt (detailed)
  └→ Critical, novel, highly ambiguous?
     └→ Use analysis_comprehensive.txt (exhaustive)
```

### For @researcher: Task Decomposition

```
Problem Type Identified (by @reader)
  ↓
Type A: Continuous Optimization → Load Type A template
Type B: Discrete/Combinatorial → Load Type B template
Type C: Prediction/Forecasting → Load Type C template
Type D: Evaluation/Selection → Load Type D template
Type E: Simulation/Modeling → Load Type E template
Type F: Classification/Clustering → Load Type F template
  ↓
Apply task_decompose.txt → breakdown
Apply dependency_analysis.txt → dependencies
  ↓
Output: Structured subtask list
```

### For @knowledge_librarian: Method Evaluation

```
Method Consultation Request
  ↓
Retrieve candidate methods from HMML 2.0
  ↓
Apply scoring_rubric.md (5-dim framework)
  ↓
Use critique_five_dimensions.txt → detailed analysis
  ↓
Score each method (0-10 per dimension)
  ↓
Rank by total score (average)
  ↓
Return top-k (k=6-10) with justifications
```

### For @modeler: Modeling Approach

```
Method Selected (from @knowledge_librarian)
  ↓
Problem Complexity Assessment
  ├→ Simple, single domain?
  │  └→ Use modeling_basic.txt
  │     - Focus on clarity
  │     - Standard approach
  │     - Interpretable results
  ├→ Complex, multi-domain?
  │  └→ Use modeling_advanced.txt
  │     - Emphasize sophistication
  │     - Novel combinations
  │     - O-Prize level
  ↓
Model design complete
  ↓
Use solution_formulation.txt → solution development
  ↓
Output: model_design.md
```

---

## Usage Metrics Tracking

### Template Usage Frequency

Track which templates are used most frequently:

| Template | Expected Usage | Actual Usage | Notes |
|----------|---------------|--------------|-------|
| analysis_general.txt | Every competition | TBD | |
| analysis_deep.txt | 60-70% of competitions | TBD | Complex problems |
| analysis_comprehensive.txt | 20-30% of competitions | TBD | Critical/novel problems |
| critique_five_dimensions.txt | Every consultation | TBD | Core evaluation |
| modeling_basic.txt | 40-50% of models | TBD | Standard approaches |
| modeling_advanced.txt | 50-60% of models | TBD | O-Prize attempts |
| decompose_prompt.json | Every competition | TBD | All 6 types |
| task_decompose.txt | Every competition | TBD | Core task breakdown |
| dependency_analysis.txt | 80-90% of competitions | TBD | Multi-model projects |

### Agent Satisfaction

Survey agents after each competition:

| Agent | Template Quality (1-5) | Suggestions |
|-------|----------------------|-------------|
| @reader | TBD | |
| @researcher | TBD | |
| @knowledge_librarian | TBD | |
| @modeler | TBD | |

---

## Future Template Additions

### Planned Templates

**Method Evaluation** (pending):
- `evaluation_scoring.txt` - Quantitative scoring methodology
- `comparison.txt` - Side-by-side method comparison framework
- `selection_rationale.txt` - Method selection justification template
- `feasibility_check.txt` - Implementation feasibility assessment

**Modeling** (pending):
- `validation.txt` - Model validation strategy template

**Documentation** (pending):
- Each template will have usage examples
- Best practices guide
- Common pitfalls and how to avoid them

---

## Summary

**Total Templates**: 9 currently integrated + 5 pending = 14 total

**Primary Agents**: 4 agents heavily use templates
- @reader (3 templates)
- @researcher (3 templates)
- @knowledge_librarian (1 template)
- @modeler (3 templates)

**Secondary Agents**: 3 agents occasionally reference templates
- @director (coordination awareness)
- @judge_zero (evaluation criteria)
- @code_translator (solution formulation)

**Impact**: Standardized approach across all phases of competition workflow

**Next Steps**:
1. Use templates in next competition
2. Collect usage data and feedback
3. Create pending templates based on needs
4. Iterate and improve based on experience

---

**Document Version**: 1.0
**Last Updated**: 2026-01-29
**Status**: Active
