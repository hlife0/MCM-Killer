# MM_Assets_Export to MCM-Killer Integration Plan

## Objective
Migrate specific components from MM_Assets_Export to MCM-Killer workspace, integrating them into agent knowledge bases and updating agent prompts with correct path references.

## Three-Part Plan Structure

### 1. Components to Migrate
### 2. Target File Locations
### 3. Agent Integration & Prompt Updates

---

## Part 1: Components to Migrate

### Component Set A: Task Decomposition System

| File | Size | Purpose | Migrate? |
|------|------|---------|----------|
| `decompose_prompt.json` | 62KB | Task breakdown templates (Problems A-F) | ✅ YES |
| `template.py` (decomposition sections) | ~20KB | Subtask decomposition prompts | ✅ YES |

**What's inside `decompose_prompt.json`:**
- 6 problem type templates (A, B, C, D, E, F)
- Each contains 3-5 subtask decomposition patterns
- Includes theoretical and practical approach variants
- Dependency analysis templates

### Component Set B: Prompt Template Library

| File | Size | Purpose | Migrate? |
|------|------|---------|----------|
| `template.py` (extraction) | 96KB total | Mathematical modeling prompts | ✅ YES (selective) |

**Templates to extract from `template.py`:**
1. **Problem Analysis Templates** (3):
   - `PROBLEM_ANALYSIS_GENERAL`
   - `PROBLEM_ANALYSIS_DEEP`
   - `PROBLEM_ANALYSIS_COMPREHENSIVE`

2. **Method Critique Templates** (5):
   - `METHOD_CRITIQUE_FIVE_DIMENSION`
   - `METHOD_EVALUATION_SCORING`
   - `METHOD_COMPARISON`
   - `METHOD_SELECTION_RATIONALE`
   - `METHOD_FEASIBILITY_CHECK`

3. **Modeling Solution Templates** (4):
   - `PROBLEM_MODELING_BASIC`
   - `PROBLEM_MODELING_ADVANCED`
   - `SOLUTION_FORMULATION`
   - `MODEL_VALIDATION`

4. **Task Decomposition Templates** (already in decompose_prompt.json)

**What NOT to extract from `template.py`:**
- DAG construction templates (incompatible with @director)
- Coordinator-related prompts

### Component Set C: Method Scoring System

| File | Size | Purpose | Migrate? |
|------|------|---------|----------|
| `retrieve_method.py` | 6.8KB | Method scoring algorithm | ✅ YES (adapt) |
| `中文自然语言.txt` | 1.6KB | Scoring rubric (Chinese) | ✅ YES (translate) |

**What `retrieve_method.py` contains:**
- Embedding-based semantic similarity scoring
- LLM-based 5-dimensional evaluation:
  - Assumptions compatibility
  - Structural fit
  - Variable alignment
  - Dynamics matching
  - Solvability assessment
- Hierarchical parent-child weight propagation
- Top-k method selection

### Component Set D: HMML Enrichment

| File | Size | Purpose | Migrate? |
|------|------|---------|----------|
| `HMML.json` | 177KB | Hierarchical method library | ✅ YES (via migration tool) |
| `HMML.md` | 162KB | Human-readable version | ✅ YES (reference) |

**What's inside `HMML.json`:**
- 150+ mathematical methods in hierarchical structure
- Categories: Operations Research, Optimization, Machine Learning, Prediction, Evaluation
- Each method: name, description, core ideas, applications

### Component Set E: Documentation Assets

| File | Size | Purpose | Migrate? |
|------|------|---------|----------|
| `伪代码.txt` (coordinator) | 2.2KB | DAG pseudocode | ❌ NO (incompatible) |
| `伪代码.txt` (retrieve) | 1.1KB | Retrieval pseudocode | ✅ YES (reference) |
| `assets.zip` | 133KB | Additional assets | ⚠️ INVESTIGATE first |

### Components NOT to Migrate

| File | Reason |
|------|--------|
| `coordinator.py` | Architectural conflict with @director |
| `constants.py` | Redundant with HMML 2.0 |
| DAG-related templates | Incompatible with 22-phase workflow |

---

## Part 2: Target File Locations

### Migrate To: MCM-Killer Knowledge Library

```
D:\migration\MCM-Killer\workspace\2025_C\knowledge_library\
├── templates/
│   ├── task_decomposition/
│   │   └── decompose_prompt.json              [NEW - from MM_Assets_Export]
│   │   └── README.md                          [NEW - usage guide]
│   ├── prompts/
│   │   ├── problem_analysis/                  [NEW DIRECTORY]
│   │   │   ├── analysis_general.txt          [NEW - from template.py]
│   │   │   ├── analysis_deep.txt             [NEW - from template.py]
│   │   │   └── analysis_comprehensive.txt    [NEW - from template.py]
│   │   ├── method_evaluation/                 [NEW DIRECTORY]
│   │   │   ├── critique_five_dimensions.txt  [NEW - from template.py]
│   │   │   ├── evaluation_scoring.txt        [NEW - from template.py]
│   │   │   ├── comparison.txt                [NEW - from template.py]
│   │   │   ├── selection_rationale.txt       [NEW - from template.py]
│   │   │   └── feasibility_check.txt         [NEW - from template.py]
│   │   ├── modeling/                          [NEW DIRECTORY]
│   │   │   ├── modeling_basic.txt            [NEW - from template.py]
│   │   │   ├── modeling_advanced.txt         [NEW - from template.py]
│   │   │   ├── solution_formulation.txt      [NEW - from template.py]
│   │   │   └── validation.txt                [NEW - from template.py]
│   │   └── PROMPT_INDEX.md                   [NEW - master index]
│   └── method_scoring/                        [NEW DIRECTORY]
│       ├── scoring_algorithm.py              [NEW - adapted from retrieve_method.py]
│       ├── scoring_rubric.md                 [NEW - translated from 中文自然语言.txt]
│       └── README.md                         [NEW - usage guide]
```

### Migrate To: Tools Directory

```
D:\migration\MCM-Killer\workspace\2025_C\tools\
├── method_scorer.py                           [NEW - adapted from retrieve_method.py]
├── 8_migrate_hmml_json.py                     [EXISTING - update source path]
└── hmml_enrichment/                           [NEW DIRECTORY]
    ├── HMML.json                              [COPY from MM_Assets_Export]
    ├── HMML.md                                [COPY from MM_Assets_Export]
    └── migration_log.md                       [NEW - track additions]
```

### Migrate To: Knowledge Base (HMML 2.0)

```
D:\migration\MCM-Killer\workspace\2025_C\knowledge_base\
└── HMML_2.0/
    ├── methods/                               [EXISTING]
    │   ├── [97 existing method .md files]
    │   └── [50+ new method .md files]        [NEW - via migration tool]
    ├── hmml_index.json                        [EXISTING - update]
    └── hmml_summary.json                      [EXISTING - update]
```

### Documentation Destination

```
D:\migration\MCM-Killer\docs\
├── MM_Assets_Integration_Report.md            [NEW - comprehensive report]
├── Component_Migration_Guide.md               [NEW - this implementation plan]
├── Prompt_Mapping_Table.md                    [NEW - template to agent mapping]
├── Method_Scorer_Integration_Guide.md         [NEW - scorer setup guide]
├── HMML_Enrichment_Log.md                    [NEW - new methods tracking]
└── Agent_Update_Checklist.md                 [NEW - which agents need updates]
```

---

## Part 3: Agent Integration & Prompt Updates

### 3.1 Agents Requiring Updates

#### Tier 1: Direct Integration (Primary Beneficiaries)

| Agent | Current Knowledge Gaps | MM_Assets Components to Add | Prompt Updates Required |
|-------|----------------------|----------------------------|------------------------|
| **@researcher** | No systematic task breakdown | `decompose_prompt.json` | Add path to task templates |
| **@knowledge_librarian** | Manual method search only | `method_scorer.py`, scoring rubric | Add tool usage instructions |
| **@modeler** | Basic modeling prompts | Modeling templates (4) | Add template paths |
| **@reader** | Basic problem analysis | Analysis templates (3) | Add deep analysis prompts |

#### Tier 2: Indirect Benefit (Secondary Beneficiaries)

| Agent | Enhancement | Prompt Updates |
|-------|------------|----------------|
| **@director** | Better task coordination visibility | Reference to decomposition templates |
| **@judge_zero** | Method evaluation criteria | Access to scoring rubric |
| **@advisor** | Enriched method recommendations | Reference to scorer output |

#### Tier 3: No Updates Required

| Agent | Reason |
|-------|--------|
| @writer, @editor, @narrative_weaver | Focus on writing, not method selection |
| @data_engineer, @code_translator | Implementation-focused |
| @visualizer, @summarizer | Output-focused |
| @validator, @feasibility_checker, @time_validator | Validation-focused |

### 3.2 Agent Prompt Update Details

#### @researcher (PRIMARY TARGET)

**Current file:** `D:\migration\MCM-Killer\workspace\2025_C\.claude\agents\researcher.md`

**Add to Knowledge Base section:**
```markdown
## Knowledge Base Access

### Task Decomposition Templates
- **Location:** `knowledge_library/templates/task_decomposition/decompose_prompt.json`
- **Usage:** When breaking down complex problems (Phase 0-1), reference appropriate problem type template (A-F)
- **Contains:** 3-5 subtask patterns with dependency structures

### Modeling Prompt Templates
- **Location:** `knowledge_library/templates/prompts/modeling/`
- **Files:**
  - `modeling_basic.txt` - For straightforward models
  - `modeling_advanced.txt` - For complex, multi-paradigm models
  - `solution_formulation.txt` - For solution development
  - `validation.txt` - For model validation approach
```

**Add to Procedures section:**
```markdown
## Phase 0-1: Enhanced Task Decomposition

1. **Identify problem type** (A-F)
2. **Load corresponding template** from `decompose_prompt.json`
3. **Adapt template** to specific problem requirements
4. **Generate 3-5 subtasks** with dependency analysis
5. **Use modeling templates** from `prompts/modeling/` for each subtask
```

#### @knowledge_librarian (PRIMARY TARGET)

**Current file:** `D:\migration\MCM-Killer\workspace\2025_C\.claude\agents\knowledge_librarian.md`

**Add to Tools section:**
```markdown
## Method Scoring Tool

### Tool Location
`tools/method_scorer.py`

### Usage
```bash
python tools/method_scorer.py --problem_description "PROBLEM_TEXT" --top_k 10
```

### Output
JSON with scored methods:
```json
{
  "methods": [
    {
      "method_name": "Linear Programming",
      "domain": "optimization",
      "total_score": 8.5,
      "dimension_scores": {
        "assumptions": 9.0,
        "structure": 8.0,
        "variables": 9.0,
        "dynamics": 8.0,
        "solvability": 9.0
      },
      "rationale": "..."
    }
  ]
}
```

### Scoring Rubric Reference
`knowledge_library/method_scoring/scoring_rubric.md` - 5-dimensional evaluation criteria
```

**Add to Knowledge Base section:**
```markdown
## Enhanced HMML Access

### HMML 2.0 Methods
- **Base location:** `knowledge_base/HMML_2.0/methods/`
- **Index:** `knowledge_library/hmml_summary.json`
- **New methods:** Check `hmml_enrichment/migration_log.md` for latest additions (50+ new methods added)

### Method Evaluation Templates
- **Location:** `knowledge_library/templates/prompts/method_evaluation/`
- **Available templates:**
  - `critique_five_dimensions.txt` - Detailed 5-dim analysis
  - `evaluation_scoring.txt` - Quantitative scoring
  - `comparison.txt` - Side-by-side method comparison
  - `selection_rationale.txt` - Justification framework
  - `feasibility_check.txt` - Practical feasibility assessment
```

#### @modeler (PRIMARY TARGET)

**Current file:** `D:\migration\MCM-Killer\workspace\2025_C\.claude\agents\modeler.md`

**Add to Templates section:**
```markdown
## Modeling Prompt Templates

### Available Templates
- **Location:** `knowledge_library/templates/prompts/modeling/`

### Template Usage Guide
1. **modeling_basic.txt** - Use for:
   - Single-paradigm models (e.g., pure optimization)
   - Well-defined problem structures
   - Standard methodological approaches

2. **modeling_advanced.txt** - Use for:
   - Multi-paradigm models (e.g., optimization + ML)
   - Novel combinations of methods
   - Complex, non-standard approaches

3. **solution_formulation.txt** - Use for:
   - Translating mathematical models into solutions
   - Algorithm design and implementation planning
   - Result interpretation frameworks

4. **validation.txt** - Use for:
   - Model validation strategy
   - Sensitivity analysis design
   - Robustness testing approach

### Integration with Method Selection
- Consult @knowledge_librarian's scored recommendations
- Use `method_evaluation/comparison.txt` to compare alternatives
- Reference `method_evaluation/feasibility_check.txt` before finalizing
```

#### @reader (SECONDARY TARGET)

**Current file:** `D:\migration\MCM-Killer\workspace\2025_C\.claude\agents\reader.md`

**Add to Analysis Templates section:**
```markdown
## Problem Analysis Templates

### Enhanced Analysis Framework
- **Location:** `knowledge_library/templates/prompts/problem_analysis/`

### Template Hierarchy
1. **analysis_general.txt** - Quick initial assessment
2. **analysis_deep.txt** - Detailed multi-angle analysis
3. **analysis_comprehensive.txt** - Full-spectrum problem understanding

### Usage Pattern
1. Start with `analysis_general.txt` for initial problem understanding
2. If problem is complex, progress to `analysis_deep.txt`
3. For critical or novel problems, use `analysis_comprehensive.txt`
4. Output feeds into @researcher's task decomposition
```

#### @director (TERTIARY TARGET)

**Current file:** `D:\migration\MCM-Killer\workspace\2025_C\.claude\agents\director.md`

**Add to Coordination Awareness section:**
```markdown
## Enhanced Coordination Visibility

### Task Decomposition Awareness
- **Location:** `knowledge_library/templates/task_decomposition/decompose_prompt.json`
- **Usage:** Reference to understand @researcher's subtask breakdown patterns
- **Benefit:** Better anticipation of multi-model coordination needs

### Method Selection Visibility
- **Tool:** `tools/method_scorer.py` outputs from @knowledge_librarian
- **Usage:** Review scored method lists when planning model parallelization
- **Benefit:** More informed phase sequencing decisions
```

### 3.3 Cross-Agent Path References

When updating agent prompts, ensure consistent path references:

**Standard path format (relative to workspace root `2025_C/`):**
```
knowledge_library/templates/task_decomposition/decompose_prompt.json
knowledge_library/templates/prompts/modeling/modeling_advanced.txt
knowledge_library/templates/prompts/method_evaluation/evaluation_scoring.txt
knowledge_library/method_scoring/scoring_rubric.md
tools/method_scorer.py
knowledge_library/hmml_summary.json
```

**Create master index:** `knowledge_library/templates/PROMPT_INDEX.md`
```markdown
# Prompt Template Index

## Problem Analysis
- `problem_analysis/analysis_general.txt` - Quick assessment
- `problem_analysis/analysis_deep.txt` - Detailed analysis
- `problem_analysis/analysis_comprehensive.txt` - Full spectrum

## Method Evaluation
- `method_evaluation/critique_five_dimensions.txt` - 5-dim critique
- `method_evaluation/evaluation_scoring.txt` - Quantitative scoring
- `method_evaluation/comparison.txt` - Side-by-side comparison
- `method_evaluation/selection_rationale.txt` - Selection framework
- `method_evaluation/feasibility_check.txt` - Feasibility assessment

## Modeling
- `modeling/modeling_basic.txt` - Basic modeling
- `modeling/modeling_advanced.txt` - Advanced modeling
- `modeling/solution_formulation.txt` - Solution development
- `modeling/validation.txt` - Validation strategy

## Task Decomposition
- `task_decomposition/decompose_prompt.json` - Subtask patterns (A-F)

## Method Scoring
- `method_scoring/scoring_rubric.md` - 5-dim scoring criteria
- `method_scoring/scoring_algorithm.py` - Scoring implementation
```

---

## Summary: What This Plan Delivers

### Files Created

**Knowledge Library (17 files):**
1. `knowledge_library/templates/task_decomposition/decompose_prompt.json`
2. `knowledge_library/templates/task_decomposition/README.md`
3. `knowledge_library/templates/prompts/problem_analysis/analysis_general.txt`
4. `knowledge_library/templates/prompts/problem_analysis/analysis_deep.txt`
5. `knowledge_library/templates/prompts/problem_analysis/analysis_comprehensive.txt`
6. `knowledge_library/templates/prompts/method_evaluation/critique_five_dimensions.txt`
7. `knowledge_library/templates/prompts/method_evaluation/evaluation_scoring.txt`
8. `knowledge_library/templates/prompts/method_evaluation/comparison.txt`
9. `knowledge_library/templates/prompts/method_evaluation/selection_rationale.txt`
10. `knowledge_library/templates/prompts/method_evaluation/feasibility_check.txt`
11. `knowledge_library/templates/prompts/modeling/modeling_basic.txt`
12. `knowledge_library/templates/prompts/modeling/modeling_advanced.txt`
13. `knowledge_library/templates/prompts/modeling/solution_formulation.txt`
14. `knowledge_library/templates/prompts/modeling/validation.txt`
15. `knowledge_library/templates/PROMPT_INDEX.md`
16. `knowledge_library/method_scoring/scoring_rubric.md`
17. `knowledge_library/method_scoring/README.md`

**Tools (5 files):**
18. `tools/extract_templates.py` (for template extraction)
19. `tools/method_scorer.py` (adapted from retrieve_method.py)
20. `tools/hmml_enrichment/HMML.json` (copied)
21. `tools/hmml_enrichment/HMML.md` (copied)
22. `tools/hmml_enrichment/migration_log.md`

**Agent Updates (5 files):**
23. `.claude/agents/researcher.md` (updated)
24. `.claude/agents/knowledge_librarian.md` (updated)
25. `.claude/agents/modeler.md` (updated)
26. `.claude/agents/reader.md` (updated)
27. `.claude/agents/director.md` (updated)

**Documentation (6 files):**
28. `docs/MM_Assets_Integration_Report.md`
29. `docs/Component_Migration_Guide.md`
30. `docs/Prompt_Mapping_Table.md`
31. `docs/Method_Scorer_Integration_Guide.md`
32. `docs/HMML_Enrichment_Log.md`
33. `docs/Agent_Update_Checklist.md`

**Total: 33 files created/updated**

### Key Benefits

1. **@researcher** can systematically decompose problems using proven templates
2. **@knowledge_librarian** can automate method selection with quantitative scoring
3. **@modeler** has comprehensive modeling prompt templates
4. **@reader** has structured problem analysis frameworks
5. **HMML 2.0** expands from 97 to 150+ methods
6. **All agents** have consistent, centralized prompt library

### Verification Checklist

Post-implementation, verify:

- [ ] All 33 files exist at specified paths
- [ ] Agent path references are correct and working
- [ ] `method_scorer.py --help` executes successfully
- [ ] `decompose_prompt.json` loads and parses correctly
- [ ] All prompt templates are readable text files
- [ ] HMML index updated with new methods (150+ total)
- [ ] Documentation is complete and accessible
- [ ] No agent files broken (validate YAML/MD syntax)

## What NOT To Do

### ❌ Do NOT integrate coordinator.py
**Reason:** Architectural incompatibility
- MCM-Killer uses human-supervised @director with 22 phases
- coordinator.py uses automated LLM-driven DAG construction
- Integrating would break all 15 protocols and eliminate quality gates

### ❌ Do NOT replace HMML 2.0
**Reason:** HMML 2.0 is superior
- HMML.json: Monolithic tree, minimal metadata
- HMML 2.0: 97 structured files with rich metadata
- Use migration tool instead of replacement

### ❌ Do NOT overlay entire MM_Assets_Export
**Reason:** Unfiltered integration causes conflicts
- Version conflicts (HMML vs HMML 2.0)
- Template conflicts
- No curation of content

## Success Criteria

The integration is successful if:
- [ ] Report created at `D:\migration\MCM-Killer\docs\MM_Assets_Integration_Report.md`
- [ ] Implementation guide provides clear step-by-step instructions
- [ ] All architectural incompatibilities are documented
- [ ] Risk assessment includes mitigation strategies
- [ ] Expected benefits are quantified (e.g., 83% time reduction)
- [ ] No regression to existing MCM-Killer workflow
