# MCM-Killer v3.1.0: Workspace Execution Guide

> **Purpose**: Step-by-step guide to execute the v3.1.0 architecture into `D:\migration\MCM-Killer\workspace`
> **Philosophy**: Add files incrementally, minimal deletion/rewrite
> **Prerequisites**: Python 3.9+, v3-1-0 architecture documents available
> **Date**: 2026-01-26

---

## Overview

This document provides **15 detailed steps** to execute the MCM-Killer v3.1.0 architecture from `D:\migration\MCM-Killer\architectures\v3-1-0` into the workspace `D:\migration\MCM-Killer\workspace`.

**Key Principle**: Each step specifies:
1. **Documents to Read** (from v3-1-0)
2. **Files to Add** (to workspace)
3. **Actions to Perform**
4. **Verification Checklist**

---

## Step 1: Understand the Architecture (Pre-Execution)

**Goal**: Familiarize yourself with v3.1.0 before any workspace changes.

### Documents to Read (v3-1-0)

| Document | Location | Read Time | Purpose |
|----------|----------|-----------|---------|
| `00_start_here.md` | Root | 5 min | Entry point, navigation |
| `00_readme.md` | Root | 5 min | System overview |
| `02_architecture_overview.md` | Root | 15 min | 18-Agent Grid, 6 subsystems |
| `01_version_comparison.md` | Root | 10 min | What's new in v3.1.0 |

### Actions

1. Read `00_start_here.md` to understand document organization
2. Read `00_readme.md` for system capabilities
3. Skim `02_architecture_overview.md` to understand the 18 agents and 6 subsystems
4. Note the 5 new phases: Pre-Competition, 0.2, 5.8, 9.1, 11

### Verification Checklist

- [ ] Understand the 4 agent clusters (Thinkers, Storytellers, Critics, Executors)
- [ ] Know the 13 phases (0 through 11 with sub-phases)
- [ ] Identify the 4 new agents: @metacognition_agent, @knowledge_librarian, @narrative_weaver, @judge_zero

---

## Step 2: Initialize Workspace Directory Structure

**Goal**: Create the v3.1.0-compliant directory structure in workspace.

### Documents to Read (v3-1-0)

| Document | Location | Section |
|----------|----------|---------|
| `04_architecture_narrative.md` | Root | Part 6: Workspace Structure (lines 237-410) |
| `tools/4_init_workspace.py` | tools/ | Full file |

### Files to Add (to workspace/{year}_{problem}/)

```
workspace/{year}_{problem}/
├── .claude/
│   └── agents/                    # Will hold agent prompts
├── knowledge_library/
│   ├── academic_writing/          # style_guide.md destination
│   ├── methods/                   # HMML 2.0 structure
│   │   ├── optimization/
│   │   ├── differential_equations/
│   │   ├── statistics/
│   │   ├── network_science/
│   │   ├── machine_learning/
│   │   └── simulation/
│   └── templates/
│       └── narrative_arcs/
├── reference_papers/              # O-Prize PDFs go here
├── tools/                         # Python tools
├── output/
│   ├── docs/
│   │   ├── insights/              # narrative_arc files
│   │   ├── knowledge/             # suggested_methods
│   │   ├── validation/            # judgment reports
│   │   ├── requirements/          # problem statement
│   │   ├── consultations/
│   │   └── reports/
│   ├── model/
│   ├── implementation/
│   │   ├── code/
│   │   ├── data/
│   │   │   ├── raw/
│   │   │   └── processed/
│   │   ├── logs/
│   │   └── models/
│   ├── figures/
│   ├── paper/
│   └── package/
├── benchmarks/
├── checkpoints/
├── VERSION_MANIFEST.json
└── config.yaml
```

### Actions

1. Navigate to `D:\migration\MCM-Killer\workspace`
2. Create problem folder: `mkdir 2025_C` (or appropriate year/problem)
3. Run initialization script:
   ```bash
   python "D:\migration\MCM-Killer\architectures\v3-1-0\tools\4_init_workspace.py"
   ```
   OR manually create directories as shown above

### Verification Checklist

- [ ] `output/docs/insights/` directory exists
- [ ] `output/docs/validation/` directory exists
- [ ] `knowledge_library/methods/` has 6 subdirectories
- [ ] `VERSION_MANIFEST.json` created with v3.1.0 metadata

---

## Step 3: Copy Agent Prompts to Workspace

**Goal**: Deploy the 18 agent prompts to the workspace.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `06_agent_directory.md` | Root | Complete agent index |
| `agents/00_implementation_status.md` | agents/ | Agent status tracking |

### Files to Add (to workspace/.claude/agents/)

Copy ALL files from `v3-1-0/agents/` to `workspace/{year}_{problem}/.claude/agents/`:

| Source File | Purpose |
|-------------|---------|
| `01_reader.md` | Problem analysis |
| `02_researcher.md` | Method selection |
| `03_modeler.md` | Mathematical formulation |
| `04_feasibility_checker.md` | Feasibility validation |
| `05_data_engineer.md` | Data preprocessing |
| `06_code_translator.md` | Code implementation |
| `07_model_trainer.md` | Model training |
| `08_validator.md` | Result validation |
| `09_visualizer.md` | Figure generation |
| `10_writer.md` | Paper writing |
| `11_editor.md` | LaTeX editing |
| `12_summarizer.md` | Memo creation |
| `13_advisor.md` | Strategic guidance |
| `14_time_validator.md` | Time management |
| `15_director.md` | Orchestration |
| `16_metacognition_agent.md` | Insight extraction (NEW) |
| `17_narrative_weaver.md` | Outline coordination (NEW) |
| `18_knowledge_librarian.md` | Method consultation (NEW) |
| `19_judge_zero.md` | Adversarial review (NEW) |

### Actions

```bash
# Copy all agent files
xcopy "D:\migration\MCM-Killer\architectures\v3-1-0\agents\*.md" "D:\migration\MCM-Killer\workspace\{year}_{problem}\.claude\agents\" /Y
```

### Verification Checklist

- [ ] 19 files in `.claude/agents/` (18 agents + 1 status file)
- [ ] New agents present: `16_metacognition_agent.md`, `17_narrative_weaver.md`, `18_knowledge_librarian.md`, `19_judge_zero.md`

---

## Step 4: Copy Templates to Workspace

**Goal**: Deploy narrative arc templates, writing templates, and knowledge base templates.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `04_architecture_narrative.md` | Root | Template specifications |

### Files to Add

**Narrative Arc Templates** (to `workspace/knowledge_library/templates/narrative_arcs/`):

| Source | Destination |
|--------|-------------|
| `templates/narrative_arcs/1_iterative_refinement.md` | Same path in workspace |
| `templates/narrative_arcs/2_onion_peeling.md` | Same path |
| `templates/narrative_arcs/3_comparative_evolution.md` | Same path |
| `templates/narrative_arcs/4_observation_implication.md` | Same path |

**Writing Templates** (to `workspace/output/templates/writing/`):

| Source | Destination |
|--------|-------------|
| `templates/writing/1_abstract_template.md` | Same path |
| `templates/writing/2_paper_outline_template.md` | Same path |
| `templates/writing/3_dev_diary_entry.md` | Same path |
| `templates/writing/4_judgment_report_template.md` | Same path |
| `templates/writing/5_latex_formatting_standards.md` | Same path |
| `templates/writing/6_anti_patterns.md` | → `knowledge_library/academic_writing/ANTI_PATTERNS.md` |

**Knowledge Base Templates** (to `workspace/knowledge_library/`):

| Source | Destination |
|--------|-------------|
| `templates/knowledge_base/1_method_file_template.md` | Same path |
| `templates/knowledge_base/2_suggested_methods_template.md` | Same path |

### Actions

```bash
# Copy narrative arc templates
xcopy "D:\migration\MCM-Killer\architectures\v3-1-0\templates\narrative_arcs\*" "D:\migration\MCM-Killer\workspace\{year}_{problem}\knowledge_library\templates\narrative_arcs\" /Y

# Copy writing templates
xcopy "D:\migration\MCM-Killer\architectures\v3-1-0\templates\writing\*" "D:\migration\MCM-Killer\workspace\{year}_{problem}\output\templates\writing\" /Y

# Copy knowledge base templates
xcopy "D:\migration\MCM-Killer\architectures\v3-1-0\templates\knowledge_base\*" "D:\migration\MCM-Killer\workspace\{year}_{problem}\knowledge_library\templates\knowledge_base\" /Y

# Copy ANTI_PATTERNS to academic_writing
copy "D:\migration\MCM-Killer\architectures\v3-1-0\templates\writing\6_anti_patterns.md" "D:\migration\MCM-Killer\workspace\{year}_{problem}\knowledge_library\academic_writing\ANTI_PATTERNS.md"
```

### Verification Checklist

- [ ] 4 narrative arc templates in `knowledge_library/templates/narrative_arcs/`
- [ ] 5 writing templates in `output/templates/writing/`
- [ ] `ANTI_PATTERNS.md` in `knowledge_library/academic_writing/`
- [ ] 2 knowledge base templates in `knowledge_library/templates/knowledge_base/`

---

## Step 5: Copy Python Tools to Workspace

**Goal**: Deploy functional Python tools for automation.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `22_integration_summary.md` | Root | Tool usage patterns |
| `04_architecture_narrative.md` | Root | Part 7: Python Toolchain |

### Files to Add (to workspace/tools/)

| Source | Purpose |
|--------|---------|
| `tools/1_system_prompts.py` | Modular prompts (P0) |
| `tools/2_safe_template.py` | Crash-proof formatting (P0) |
| `tools/3_journal_prompts.py` | Metacognition prompts (P1) |
| `tools/4_init_workspace.py` | Directory initialization |
| `tools/5_migrate_hmml.py` | HMML 1.0 → 2.0 conversion |
| `tools/6_style_analyzer.py` | Reference paper analysis |
| `tools/7_log_analyzer.py` | Training log compression |
| `tools/8_mmbench_score.py` | Automated scoring |

### Actions

```bash
# Copy all Python tools
xcopy "D:\migration\MCM-Killer\architectures\v3-1-0\tools\*.py" "D:\migration\MCM-Killer\workspace\{year}_{problem}\tools\" /Y
```

### Verification Checklist

- [ ] 8 Python files in `tools/`
- [ ] Verify syntax: `python -m py_compile tools/1_system_prompts.py`
- [ ] Verify syntax: `python -m py_compile tools/2_safe_template.py`
- [ ] P0 tools present: `1_system_prompts.py`, `2_safe_template.py`

---

## Step 6: Set Up HMML 2.0 Knowledge Library

**Goal**: Create the structured knowledge base for method retrieval.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `11_knowledge_library_spec.md` | Root | HMML 2.0 specification |
| `12_agent_knowledge_access.md` | Root | Agent → knowledge mapping |

### Files to Add (to workspace/knowledge_library/)

**Create `index.md`** at `knowledge_library/index.md`:

```markdown
# HMML 2.0 Master Catalog

> **Last Updated**: YYYY-MM-DD
> **Total Methods**: 0 (pending migration)

---

## Quick Navigation

- [Optimization](#optimization)
- [Differential Equations](#differential-equations)
- [Statistics](#statistics)
- [Network Science](#network-science)
- [Machine Learning](#machine-learning)
- [Simulation](#simulation)

---

## Optimization

*Methods pending...*

---

## Differential Equations

*Methods pending...*

---

[Continue for other domains...]
```

**Create `hmml_summary.json`** at `knowledge_library/hmml_summary.json`:

```json
{
  "version": "2.0",
  "last_updated": "YYYY-MM-DD",
  "total_methods": 0,
  "domains": {
    "optimization": {"count": 0, "categories": []},
    "differential_equations": {"count": 0, "categories": []},
    "statistics": {"count": 0, "categories": []},
    "network_science": {"count": 0, "categories": []},
    "machine_learning": {"count": 0, "categories": []},
    "simulation": {"count": 0, "categories": []}
  },
  "methods": []
}
```

### Actions

1. Create `index.md` and `hmml_summary.json` as shown above
2. If you have existing HMML.md, run migration:
   ```bash
   python tools/5_migrate_hmml.py --input HMML.md --output knowledge_library/methods/ --generate-index
   ```

### Verification Checklist

- [ ] `knowledge_library/index.md` exists
- [ ] `knowledge_library/hmml_summary.json` exists
- [ ] 6 domain subdirectories in `knowledge_library/methods/`

---

## Step 7: Add Reference Papers (Pre-Competition)

**Goal**: Prepare O-Prize winning papers for style analysis.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `05_protocols_complete.md` | Root | Pre-Competition phase (lines 956-1026) |

### Files to Add (to workspace/reference_papers/)

Add 3-5 O-Prize winning papers (PDF format):

```
reference_papers/
├── 2024_Problem_C_O_Prize.pdf
├── 2023_Problem_D_O_Prize.pdf
├── 2022_Problem_F_Finalist.pdf
└── ... (more papers as available)
```

### Actions

1. Download O-Prize papers from MCM/ICM archives
2. Place PDFs in `workspace/{year}_{problem}/reference_papers/`
3. Run style analyzer:
   ```bash
   python tools/6_style_analyzer.py --input "reference_papers/*.pdf" --output knowledge_library/academic_writing/style_guide.md
   ```

### Verification Checklist

- [ ] At least 3 PDF files in `reference_papers/`
- [ ] `style_guide.md` generated in `knowledge_library/academic_writing/`
- [ ] `style_guide.md` contains "High-Value Verbs" section
- [ ] `style_guide.md` contains "Abstract Rules" section

---

## Step 8: Create VERSION_MANIFEST.json

**Goal**: Initialize the version tracking file.

### Documents to Read (v3-1-0)

| Document | Location | Section |
|----------|----------|---------|
| `04_architecture_narrative.md` | Root | Section 6.2 VERSION_MANIFEST.json (lines 408-460) |

### File to Add

Create `VERSION_MANIFEST.json` at workspace root:

```json
{
  "mcm_killer_version": "3.1.0",
  "workspace_version": "1.0",
  "problem": {
    "year": 2025,
    "type": "C",
    "title": "[Problem Title]"
  },
  "team": {
    "team_id": "[Your Team ID]",
    "institution": "[Your Institution]"
  },
  "phases_completed": [],
  "defcon_history": [],
  "agents_invoked": [],
  "checkpoints": [],
  "final_submission": null
}
```

### Verification Checklist

- [ ] `VERSION_MANIFEST.json` exists at workspace root
- [ ] `mcm_killer_version` is "3.1.0"
- [ ] Problem metadata filled in

---

## Step 9: Create config.yaml

**Goal**: Configure system settings for the competition run.

### Documents to Read (v3-1-0)

| Document | Location | Section |
|----------|----------|---------|
| `04_architecture_narrative.md` | Root | Section 6.3 config.yaml (lines 465-553) |

### File to Add

Create `config.yaml` at workspace root:

```yaml
# MCM-Killer v3.1.0 Configuration

system:
  version: "3.1.0"
  llm_provider: "anthropic"
  default_model: "claude-sonnet-4"

agents:
  "@director": "claude-sonnet-4"
  "@reader": "claude-haiku-4"
  "@metacognition_agent": "claude-sonnet-4"
  "@narrative_weaver": "claude-sonnet-4"
  "@judge_zero": "claude-sonnet-4"
  "@writer": "claude-sonnet-4"
  "@knowledge_librarian": "claude-haiku-4"

tools:
  style_analyzer:
    path: "tools/6_style_analyzer.py"
    output: "knowledge_library/academic_writing/style_guide.md"
  log_analyzer:
    path: "tools/7_log_analyzer.py"
    compression_target: 10240

protocols:
  protocol_13_defcon:
    max_iterations: 3
    mercy_rule_enabled: true
  protocol_14_style:
    style_guide_path: "knowledge_library/academic_writing/style_guide.md"
  protocol_15_interpretation:
    max_descriptive_only_pct: 30

phase_gates:
  gate_9.1_mock_judging:
    pass_threshold: 95
    fail_action: "trigger_protocol_13"

checkpoints:
  enabled: true
  auto_checkpoint_phases: ["1", "5", "7"]
```

### Verification Checklist

- [ ] `config.yaml` exists at workspace root
- [ ] Protocol 13 settings configured
- [ ] Protocol 14/15 paths correct

---

## Step 10: Execute Phase 0 - Problem Understanding

**Goal**: Parse problem PDF and extract requirements.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `03_architecture_phases.md` | Root | Phase 0 details |
| `agents/01_reader.md` | agents/ | @reader prompt |
| `agents/02_researcher.md` | agents/ | @researcher prompt |
| `30_execution_plan.md` | Root | Step 1: Problem Intake |

### Files to Add

1. **Input**: Place `problem.pdf` at workspace root
2. **Output**: Create `output/docs/requirements/problem_statement.md`

### Actions

1. Invoke `@reader` with problem PDF:
   - Extract explicit constraints
   - Identify data sources
   - Note submission requirements

2. Invoke `@researcher` to:
   - Extract implicit O-Prize requirements
   - Identify domain keywords (for Phase 0.2)

### Output Template (problem_statement.md)

```markdown
# Problem Statement: [Year] Problem [Letter]

## Explicit Requirements
1. [Requirement 1]
2. [Requirement 2]

## Implicit Requirements (O-Prize)
1. [Inferred requirement 1]
2. [Inferred requirement 2]

## Data Sources
- [Data file 1]: [Description]
- [Data file 2]: [Description]

## Domain Keywords
- Keyword 1
- Keyword 2
```

### Verification Checklist

- [ ] `problem.pdf` at workspace root
- [ ] `output/docs/requirements/problem_statement.md` created
- [ ] Domain keywords extracted for Phase 0.2

---

## Step 11: Execute Phase 0.2 - Method Consultation

**Goal**: Get advanced method suggestions from HMML 2.0.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `05_protocols_complete.md` | Root | Phase 0.2 specification (lines 1028-1067) |
| `agents/18_knowledge_librarian.md` | agents/ | @knowledge_librarian prompt |
| `11_knowledge_library_spec.md` | Root | HMML 2.0 structure |

### Files to Add

**Output**: Create `output/docs/knowledge/suggested_methods.md`

### Actions

1. `@researcher` sends domain keywords to `@knowledge_librarian`
2. `@knowledge_librarian` queries `knowledge_library/hmml_summary.json`
3. Generate method recommendations with star ratings

### Output Template (suggested_methods.md)

```markdown
# Suggested Methods

**Problem**: [Year] Problem [Letter]
**Domain**: [Primary Domain]
**Generated**: [Date]

---

## Recommended Methods

### Method 1: [Name] ⭐⭐⭐⭐⭐
- **Domain**: [Domain]
- **Complexity**: High
- **Narrative Value**: Very High
- **O-Prize Examples**: [Year, Problem]
- **Path**: `knowledge_library/methods/[domain]/[method].md`

### Method 2: [Name] ⭐⭐⭐⭐
...

---

## Comparison Matrix

| Method | Complexity | Time | Narrative Value |
|--------|------------|------|-----------------|
| Method 1 | High | 12h | Very High |
| Method 2 | Medium | 6h | High |
```

### Verification Checklist

- [ ] `suggested_methods.md` in `output/docs/knowledge/`
- [ ] At least one "High" complexity method suggested
- [ ] Methods include HMML 2.0 paths

---

## Step 12: Execute Phases 1-5 - Core Modeling

**Goal**: Design, implement, and train models.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `03_architecture_phases.md` | Root | Phases 1-5 details |
| `05_protocols_complete.md` | Root | Protocol 2 (Strict Mode), Protocol 5 (Idealistic Mode) |
| `30_execution_plan.md` | Root | Steps 4-7 |

### Files to Add

**Phase 1 (Design)**:
- `output/model/model_1/design.md` - Mathematical specification

**Phase 2-3 (Data)**:
- `output/implementation/data/processed/train.csv`
- `output/implementation/data/processed/test.csv`

**Phase 4 (Code)**:
- `output/implementation/code/main_1.py`
- `output/docs/insights/dev_diary_1.md` **[CRITICAL for Phase 5.8]**

**Phase 5 (Training)**:
- `output/implementation/models/model_1.pkl`
- `output/implementation/logs/training_full.log`
- `output/implementation/logs/training_history.csv`

### Key Protocol Enforcement

**Protocol 5 (Idealistic Mode)**: `@code_translator` MUST:
- Never simplify without @director approval
- Document ALL struggles in `dev_diary_1.md`
- Use template from `templates/writing/3_dev_diary_entry.md`

### Dev Diary Entry Template

```markdown
## Struggle Entry [N]

**Timestamp**: [YYYY-MM-DD HH:MM]
**Phase**: [4 or 5]
**Severity**: [Minor/Medium/Critical]

### Symptom
[What went wrong? Error message, unexpected behavior]

### Context
[What were you trying to do? Code snippet if relevant]

### Attempted Fixes
1. [Fix 1] → [Result]
2. [Fix 2] → [Result]

### Resolution
[Final fix and why it worked]

### Physical Insight (if applicable)
[What does this reveal about the problem domain?]
```

### Verification Checklist

- [ ] `design.md` has Parameter Table and Assumption List
- [ ] `dev_diary_1.md` has at least 3 entries
- [ ] `training_full.log` is non-empty
- [ ] Model artifact saved

---

## Step 13: Execute Phase 5.8 - Insight Extraction

**Goal**: Transform technical struggles into research insights.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `05_protocols_complete.md` | Root | Phase 5.8 specification (lines 1068-1151) |
| `agents/16_metacognition_agent.md` | agents/ | @metacognition_agent prompt |
| `04_architecture_narrative.md` | Root | Part 5: Cognitive Narrative Framework |
| `templates/narrative_arcs/1_iterative_refinement.md` | templates/ | Narrative template |

### Files to Add

**Input**:
- `output/implementation/logs/training_full.log`
- `output/docs/insights/dev_diary_1.md`

**Output**:
- `output/implementation/logs/summary.json` (via `7_log_analyzer.py`)
- `output/docs/insights/narrative_arc_1.md`

### Actions

1. Run log analyzer:
   ```bash
   python tools/7_log_analyzer.py output/implementation/logs/training_full.log output/implementation/logs/summary.json
   ```

2. Invoke `@metacognition_agent` with:
   - `summary.json`
   - `dev_diary_1.md`
   - Narrative arc template

3. Generate `narrative_arc_1.md` following Iterative Refinement structure

### Narrative Arc Template

```markdown
# Narrative Arc: Model 1 - [Theme]

## 1. Baseline Model
[Initial approach and rationale]

## 2. Observed Limitation (The Struggle)
- **Symptom**: [Technical issue from logs]
- **Log Evidence**: training_full.log:[line numbers]
- **Dev Diary**: [Reference to dev_diary entry]

## 3. Mechanism Insight
[Physical/domain explanation of WHY the issue occurred]
**This is not a bug—it is the system revealing [insight].**

## 4. Model Refinement
- **Technical Fix**: [What changed]
- **Physical Justification**: [Why this makes sense]
- **Result**: [Performance improvement]

## 5. Research Value
- **Methodological**: [What we learned about modeling]
- **Domain-Specific**: [What we learned about the problem]
- **Policy Implications**: [Actionable insights]

## Narrative Hook for Abstract
"[One-sentence insight for abstract inclusion]"
```

### Quality Rules

**NEVER say**:
- "We fixed a bug"
- "We corrected an error"

**ALWAYS say**:
- "We refined the model to better capture [physical reality]"
- "The divergence revealed [fundamental insight]"

### Verification Checklist

- [ ] `summary.json` generated from logs
- [ ] `narrative_arc_1.md` follows Iterative Refinement structure
- [ ] Contains ≥3 distinct insights
- [ ] No "bug fixing" language
- [ ] Has "Narrative Hook for Abstract"

---

## Step 14: Execute Phases 6-9 - Paper Generation

**Goal**: Create visualization, paper, and summary.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `03_architecture_phases.md` | Root | Phases 6-9 details |
| `05_protocols_complete.md` | Root | Protocol 14 (Style), Protocol 15 (Interpretation) |
| `agents/17_narrative_weaver.md` | agents/ | @narrative_weaver prompt |
| `agents/10_writer.md` | agents/ | @writer prompt |
| `templates/writing/5_latex_formatting_standards.md` | templates/ | LaTeX rules |

### Files to Add

**Phase 6 (Visualization)**:
- `output/figures/results_plot.png` (Mode A)
- `output/figures/methodology_flow.png` (Mode B - Mermaid diagram)

**Phase 7 (Paper)**:
- `output/paper/paper_outline.md` (from @narrative_weaver)
- `output/paper/main.tex` (from @writer)
- `output/paper/paper.pdf` (compiled)

**Phase 9 (Summary)**:
- `output/paper/summary.pdf` (1-page memo)

### Protocol 14 Enforcement (Style Alignment)

All text-generating agents MUST:
1. Load `knowledge_library/academic_writing/style_guide.md` as System Context
2. Use recommended verbs (demonstrate, elucidate, quantify)
3. Avoid banned words (show, get, say)
4. Include ≥3 numbers in abstract

### Protocol 15 Enforcement (Interpretation over Description)

**BANNED**:
```
Figure 1 shows X vs Y.
```

**REQUIRED**:
```
Figure 1 demonstrates that X increases with Y (p<0.001),
indicating strong positive correlation with implications for [domain].
```

### Verification Checklist

- [ ] Abstract contains ≥3 quantitative metrics
- [ ] All figure captions are conclusionary (Observation → Implication)
- [ ] No banned words in paper
- [ ] LaTeX compiles without errors
- [ ] 1-page memo created

---

## Step 15: Execute Phase 9.1 - Mock Judging (GATE 5)

**Goal**: Adversarial review before submission.

### Documents to Read (v3-1-0)

| Document | Location | Purpose |
|----------|----------|---------|
| `05_protocols_complete.md` | Root | Phase 9.1 (lines 1154-1234), Protocol 13 (lines 576-706) |
| `agents/19_judge_zero.md` | agents/ | @judge_zero prompt |
| `10_o_award_criteria.md` | Root | O Award characteristics |
| `templates/writing/4_judgment_report_template.md` | templates/ | Report template |

### Files to Add

**Input**: `output/paper/paper.pdf`

**Output**: `output/docs/validation/judgment_report.md`

### Three-Persona Scoring

| Persona | Weight | Focus |
|---------|--------|-------|
| Statistician | 40% | Statistical rigor, uncertainty, p-values |
| Domain Skeptic | 40% | Physical plausibility, mechanism explanation |
| Exhausted Editor | 20% | Figure captions, abstract quality, formatting |

### Scoring Formula

```
Final Score = 0.4 × Score_A + 0.4 × Score_B + 0.2 × Score_C
```

### Decision Logic

```
IF Score >= 95 AND No Fatal Flaws:
    Verdict = PASS → Proceed to Phase 9.5
ELSE:
    Verdict = REJECT → Trigger Protocol 13 (DEFCON 1)
```

### Protocol 13 (DEFCON 1) Workflow

If REJECT:

1. **Declare DEFCON 1**: Halt all forward progress
2. **Generate Kill List**: Extract issues from judgment report
3. **Assign Tickets**:
   - Abstract empty → `@writer`
   - Missing sensitivity → `@modeler` + `@validator`
   - Figure caption → `@visualizer`
4. **Execute Repairs**: Time-boxed fixes
5. **Re-Judge**: Loop (max 3 iterations)
6. **Exit Conditions**:
   - Score ≥ 95: Exit DEFCON 1, proceed
   - 3 failures with Score ≥ 80: Mercy Rule (conditional pass)

### Judgment Report Template

```markdown
# Mock Judging Report

**Date**: [YYYY-MM-DD]
**Judge**: @judge_zero
**Verdict**: PASS / REJECT

---

## Overall Score: X/100

- **Persona A (Statistician)**: Y/100 (40%)
- **Persona B (Domain Skeptic)**: Z/100 (40%)
- **Persona C (Exhausted Editor)**: W/100 (20%)

**Calculation**: 0.4×Y + 0.4×Z + 0.2×W = X

---

## Kill List (if REJECT)

| Priority | Issue | Severity | Assigned To | Deadline |
|----------|-------|----------|-------------|----------|
| 1 | [Issue] | FATAL | @agent | 30 min |
| 2 | [Issue] | SEVERE | @agent | 1 hour |

---

## Detailed Feedback

### Persona A: Statistician
[Feedback...]

### Persona B: Domain Skeptic
[Feedback...]

### Persona C: Exhausted Editor
[Feedback...]
```

### Verification Checklist

- [ ] `judgment_report.md` in `output/docs/validation/`
- [ ] All 3 personas evaluated
- [ ] Score calculated correctly
- [ ] If REJECT: Kill List generated
- [ ] If PASS: Ready for Phase 9.5

---

## Final Workspace Structure (After All Steps)

```
workspace/{year}_{problem}/
├── .claude/
│   └── agents/                    # 19 agent files
├── knowledge_library/
│   ├── academic_writing/
│   │   ├── style_guide.md         # Generated from reference papers
│   │   └── ANTI_PATTERNS.md       # Kill list for @judge_zero
│   ├── methods/                   # HMML 2.0 (6 domains)
│   │   └── index.md
│   └── templates/
│       └── narrative_arcs/        # 4 templates
├── reference_papers/              # O-Prize PDFs
├── tools/                         # 8 Python tools
├── output/
│   ├── docs/
│   │   ├── insights/
│   │   │   ├── dev_diary_1.md
│   │   │   └── narrative_arc_1.md
│   │   ├── knowledge/
│   │   │   └── suggested_methods.md
│   │   ├── validation/
│   │   │   └── judgment_report.md
│   │   └── requirements/
│   │       └── problem_statement.md
│   ├── model/
│   │   └── model_1/
│   │       └── design.md
│   ├── implementation/
│   │   ├── code/
│   │   │   └── main_1.py
│   │   ├── data/processed/
│   │   ├── logs/
│   │   │   ├── training_full.log
│   │   │   └── summary.json
│   │   └── models/
│   │       └── model_1.pkl
│   ├── figures/
│   │   ├── results_plot.png
│   │   └── methodology_flow.png
│   ├── paper/
│   │   ├── paper_outline.md
│   │   ├── main.tex
│   │   ├── paper.pdf
│   │   └── summary.pdf
│   └── package/
│       └── submission.zip
├── benchmarks/
├── checkpoints/
├── problem.pdf
├── VERSION_MANIFEST.json
└── config.yaml
```

---

## Quick Reference: Document Index

| Step | Key Documents (v3-1-0) |
|------|------------------------|
| 1. Understand | `00_start_here.md`, `02_architecture_overview.md` |
| 2. Initialize | `04_architecture_narrative.md` (Part 6), `tools/4_init_workspace.py` |
| 3. Agents | `06_agent_directory.md`, `agents/*.md` |
| 4. Templates | `templates/narrative_arcs/`, `templates/writing/` |
| 5. Tools | `22_integration_summary.md`, `tools/*.py` |
| 6. HMML 2.0 | `11_knowledge_library_spec.md` |
| 7. Pre-Comp | `05_protocols_complete.md` (Pre-Competition) |
| 8. Manifest | `04_architecture_narrative.md` (Section 6.2) |
| 9. Config | `04_architecture_narrative.md` (Section 6.3) |
| 10. Phase 0 | `03_architecture_phases.md`, `agents/01_reader.md` |
| 11. Phase 0.2 | `05_protocols_complete.md`, `agents/18_knowledge_librarian.md` |
| 12. Phases 1-5 | `03_architecture_phases.md`, `05_protocols_complete.md` |
| 13. Phase 5.8 | `04_architecture_narrative.md` (Part 5), `agents/16_metacognition_agent.md` |
| 14. Phases 6-9 | `05_protocols_complete.md` (Protocol 14/15), `agents/17_narrative_weaver.md` |
| 15. Phase 9.1 | `05_protocols_complete.md` (Protocol 13), `agents/19_judge_zero.md` |

---

## Troubleshooting

| Issue | Phase | Solution | Reference |
|-------|-------|----------|-----------|
| `style_guide.md` missing | Pre-Comp | Run `tools/6_style_analyzer.py` | Step 7 |
| Method not found | 0.2 | Update HMML 2.0 index | Step 6 |
| Template crash | Any | Use `tools/2_safe_template.py` | Step 5 |
| Judge REJECTs | 9.1 | Follow Kill List (Protocol 13) | Step 15 |
| No insights | 5.8 | Check `dev_diary` has entries | Step 12 |

---

**Document Version**: 1.0
**Created**: 2026-01-26
**Architecture Version**: v3.1.0
**Status**: Production Ready
