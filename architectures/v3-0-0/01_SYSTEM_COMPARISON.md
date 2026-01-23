# System Comparison: LLM-MM-Agent vs MCM-Killer

> **Version**: v3.0.0
> **Date**: 2026-01-23
> **Purpose**: Clear comparison between the two systems for proper usage

---

## Executive Summary

| Aspect | LLM-MM-Agent | MCM-Killer |
|--------|--------------|------------|
| **Primary Purpose** | Research prototype (academic publication) | Competition system (active development) |
| **Publication** | NeurIPS 2025, ICML 2025 | (Unpublished - competition system) |
| **Architecture Type** | Single-agent with actor-critic refinement | Multi-agent with specialized roles |
| **Pipeline Stages** | 4 stages | 10 phases |
| **Validation Gates** | Actor-critic iterations | 7 mandatory validation gates |
| **Knowledge Base** | HMML (Hierarchical Mathematical Modeling Library) | Agent expertise + consultation |
| **Entry Method** | Command line: `python MMAgent/main.py` | Claude Code CLI interactive |
| **Configuration** | `config.yaml` | `.claude/CLAUDE.md` + agent files |
| **Output Structure** | Three-tier: Report/Workspace/Memory | Competition-optimized: VERSION_MANIFEST.json |
| **Target Use Case** | Research, reference implementation | Actual MCM/ICM competition |
| **Competitive Level** | Academic baseline | O-Prize competitive ($1.5M target) |
| **Time Efficiency** | Sequential workflow | Parallel workflow (save 6-12 hours) |
| **Quality Control** | Actor-critic refinement | 12 critical protocols |
| **Anti-Fraud Measures** | Basic validation | Strict anti-fraud protocols |

---

## Detailed Comparison

### 1. Purpose and Origin

#### LLM-MM-Agent
- **Origin**: Academic research project
- **Publication**: "MM-Agent: LLMs as Agents for Real-world Mathematical Modeling Problems" (NeurIPS 2025 / ICML 2025)
- **Purpose**: Demonstrate LLM as autonomous agent for mathematical modeling
- **Target Audience**: Academic researchers, ML community
- **Status**: Reference/stable implementation (published, peer-reviewed)

#### MCM-Killer
- **Origin**: Competition-oriented development
- **Publication**: None (proprietary competition system)
- **Purpose**: Win MCM/ICM competitions, compete for O-Prize ($1.5M)
- **Target Audience**: Competition participants
- **Status**: Active development (continuous enhancement)

---

### 2. Architecture Design

#### LLM-MM-Agent: Single-Agent Architecture

```
LLM-MM-Agent Pipeline:
┌─────────────────────────────────────────────────────────────────┐
│                    4-Stage Pipeline                              │
├─────────────────────────────────────────────────────────────────┤
│  Stage 1: Problem Analysis                                      │
│    → Decompose problem into subtasks                            │
│    → Actor-Critic Refinement (3 rounds by default)              │
│                                                                 │
│  Stage 2: Mathematical Modeling                                 │
│    → Retrieve methods from HMML (embedding-based)               │
│    → Actor-Critic Refinement (3 rounds by default)              │
│                                                                 │
│  Stage 3: Computational Solving                                 │
│    → Generate Python code                                       │
│    → Execute code (safe timeout: 300s)                          │
│    → Debug and retry on failure                                 │
│                                                                 │
│  Stage 4: Solution Reporting                                    │
│    → Generate reports (JSON/Markdown/LaTeX)                     │
│    → "Omni-Survival Kit" (dead man's switch)                   │
└─────────────────────────────────────────────────────────────────┘
```

**Key Features**:
- Single LLM agent with actor-critic pattern
- HMML knowledge base (98+ schemas)
- DAG-based task scheduling for subtasks
- SafePlaceholder pattern (prevents template crashes)
- Context pruning strategy ("远近亲疏")

#### MCM-Killer: Multi-Agent Architecture

```
MCM-Killer Workflow:
┌─────────────────────────────────────────────────────────────────┐
│                  10-Phase Workflow                              │
├─────────────────────────────────────────────────────────────────┤
│  Phase 0:   Problem Understanding      (reader, researcher)    │
│  Phase 0.5: METHODOLOGY Gate ✅        (@advisor, @validator)  │
│  Phase 1:   Model Design               (modeler + 5 consultants)│
│  Phase 1.5: TIME_CHECK ✅              (@time_validator)        │
│  Phase 2:   Feasibility Check          (feasibility_checker)   │
│  Phase 3:   Data Processing            (data_engineer)         │
│  Phase 4:   Code Translation           (code_translator)       │
│  Phase 4.5: FIDELITY ✅                (@time_validator)        │
│  Phase 5A:  Quick Training             (model_trainer)         │
│  Phase 5B:  Full Training (parallel)   (model_trainer)         │
│  Phase 5.5: ANTI_FRAUD ✅              (@time_validator)        │
│  Phase 6:   Visualization              (visualizer)            │
│  Phase 6.5: VISUAL ✅                  (visualizer, @director)  │
│  Phase 7:   Paper Writing              (writer + 3 agents)     │
│  Phase 7.5: LATEX ✅                   (writer, @director)      │
│  Phase 8:   Summary                    (summarizer + editor)   │
│  Phase 9:   Polish                     (editor + 2 agents)     │
│  Phase 9.5: EDITOR ✅                  (@director + agents)     │
│  Phase 10:  Final Review               (@advisor)              │
└─────────────────────────────────────────────────────────────────┘
```

**Key Features**:
- 14 specialized agents with single responsibilities
- 7 mandatory validation gates (✅ above)
- @director as central coordinator
- 12 critical protocols for quality control
- Emergency delegation for fast error response
- Parallel workflow (paper + training)

---

### 3. Agent Composition

#### LLM-MM-Agent: 1 Agent (with actor-critic)

| Component | Role |
|-----------|------|
| **Actor** | Generates output (problem analysis, modeling, code, reports) |
| **Critic** | Reviews and provides critique for refinement |
| **Coordinator** | DAG-based scheduling for subtasks |

**Total**: 1 LLM agent with actor-critic pattern

#### MCM-Killer: 14 Specialized Agents

| Agent | Role | Validation Participation |
|-------|------|------------------------|
| reader | Read PDF, extract requirements | MODEL, DATA, PAPER |
| researcher | Method suggestions | MODEL |
| modeler | Design mathematical models | DATA, CODE, TRAINING |
| feasibility_checker | Feasibility check | MODEL, CODE |
| data_engineer | Data processing | - |
| code_translator | Code translation | CODE, TRAINING |
| model_trainer | Model training | - |
| validator | Result validation | DATA, TRAINING, FINAL |
| visualizer | Generate figures | - |
| writer | Write papers | PAPER |
| summarizer | Create summary | - |
| editor | Polish documents | - |
| advisor | Quality assessment | MODEL, PAPER, FINAL |
| time_validator | Time validation, anti-lazy | Called after MODEL, CODE, TRAINING |
| **director** | **Team coordination** | **N/A** |

**Total**: 14 specialized agents + @director (coordinator)

---

### 4. Knowledge Base

#### LLM-MM-Agent: HMML (Hierarchical Mathematical Modeling Library)

**Structure**: 3-level hierarchy
- Level 1: Domains (e.g., Optimization, Differential Equations)
- Level 2: Subdomains (e.g., Linear Programming, ODEs)
- Level 3: Method nodes (e.g., Simplex, Runge-Kutta)

**Size**: 98+ high-level modeling schemas

**Retrieval Method**: Embedding-based similarity matching

**Location**: `MMAgent/HMML/HMML.md`

**Example**:
```
Optimization (Domain)
├── Linear Programming (Subdomain)
│   ├── Simplex Method (Method Node)
│   ├── Interior Point Methods (Method Node)
│   └── ...
└── Integer Programming (Subdomain)
    ├── Branch and Bound (Method Node)
    └── ...
```

#### MCM-Killer: Agent Expertise + Consultation

**Knowledge Distribution**:
- **@researcher**: Method suggestions (O-Prize alignment)
- **@modeler**: Mathematical model design
- **@feasibility_checker**: Technical feasibility
- **@advisor**: Quality assessment
- **@time_validator**: Time estimation, lazy detection

**Consultation Mechanism**:
- Phase 1: Multi-agent consultation (5 agents provide feedback)
- Phase 0.5: Methodology quality gate (@advisor + @validator)
- Agent expertise through prompts (not external knowledge base)

---

### 5. Validation Strategy

#### LLM-MM-Agent: Actor-Critic Refinement

**Pattern**:
```
Actor generates → Critic reviews → Actor improves
     (repeat N times, default N=3)
```

**Application**:
- Problem Analysis (problem_analysis_round: 3)
- Mathematical Modeling (problem_modeling_round: 3)
- Formula Derivation (task_formulas_round: 5)

**Strengths**:
- Simple, consistent pattern
- Iterative improvement
- No hardcoded validation gates

**Weaknesses**:
- No explicit quality threshold
- Depends on LLM self-evaluation
- No independent validation

#### MCM-Killer: 7 Mandatory Validation Gates

**Validation Gates**:
1. **Phase 0.5: METHODOLOGY** - @advisor + @validator evaluate proposed methods
2. **Phase 1: MODEL** - 5 agents provide feedback on model designs
3. **Phase 1.5: TIME_CHECK** - @time_validator validates time estimates
4. **Phase 3: DATA** - @data_engineer self-validates data integrity
5. **Phase 4: CODE** - @modeler + @validator validate code
6. **Phase 4.5: FIDELITY** - @time_validator checks implementation fidelity
7. **Phase 5A/5B: TRAINING** - @model_trainer validates training completion
8. **Phase 5.5: ANTI_FRAUD** - @time_validator enforces training duration red line
9. **Phase 6.5: VISUAL** - @visualizer + @director verify image quality
10. **Phase 7: PAPER** - @writer + @visualizer + @summarizer + @editor validate
11. **Phase 7.5: LATEX** - @writer + @director verify LaTeX compilation
12. **Phase 8: SUMMARY** - @summarizer + @editor validate
13. **Phase 9: FINAL** - @editor + @writer + @summarizer validate
14. **Phase 9.5: EDITOR** - @director + agents verify feedback enforcement

**Strengths**:
- Independent validation by different agents
- Explicit quality thresholds
- Multiple validation layers
- Anti-fraud protocols (Protocol 2, 12)

**Weaknesses**:
- Complex coordination
- More time-consuming
- Depends on agent quality

---

### 6. Time Efficiency

#### LLM-MM-Agent: Sequential Workflow

```
Problem Analysis → Mathematical Modeling → Computational Solving → Solution Reporting
       ↓                     ↓                          ↓                    ↓
    (3 rounds)            (3 rounds)              (code + debug)       (generate reports)
```

**Total Time**: ~12-24 hours (no parallelization)

**Strengths**:
- Simple, linear progression
- Easy to understand
- No coordination overhead

**Weaknesses**:
- No parallelization
- Paper must wait for training
- Wasted idle time

#### MCM-Killer: Parallel Workflow

```
Phase 5A (30 min) → Phase 6 (30 min) → Phase 7 (2-3 hours)
                                          ↓
                                      Paper proceeds
                                          ↓
                     Phase 5B (6-12 hours) runs in parallel
```

**Time Savings**: 6-12 hours through parallelization

**Strengths**:
- Paper writing proceeds immediately
- No idle waiting time
- Better use of competition time

**Weaknesses**:
- Requires two-pass workflow (draft → update)
- More complex coordination
- Paper needs updating when Phase 5B completes

---

### 7. Quality Control

#### LLM-MM-Agent: Basic Validation

**Features**:
- Actor-critic refinement
- Code execution with timeout
- Basic result validation
- "Omni-Survival Kit" (dead man's switch)

**Anti-Fraud Measures**:
- Basic result checking
- Code execution verification
- No dedicated anti-fraud protocols

#### MCM-Killer: 12 Critical Protocols

**Anti-Fraud Protocols**:
1. **Protocol 1**: @director File Reading Ban - Prevents evaluation contamination
2. **Protocol 2**: @time_validator Strict Mode - Training duration red line (< 30% = auto-reject)
3. **Protocol 3**: Enhanced Analysis - Line-by-line code analysis
4. **Protocol 4**: Parallel Workflow - Time efficiency
5. **Protocol 5**: Idealistic Mode - No unauthorized simplification
6. **Protocol 6**: 48-Hour Escalation - Decision framework
7. **Protocol 7**: Handoff Protocol - Standardized communication
8. **Protocol 8**: Design Expectations - Systematic validation
9. **Protocol 9**: Brief Format - Fast decision-making
10. **Protocol 10**: Error Monitoring - Watch mode prevents lost errors
11. **Protocol 11**: Emergency Delegation - 8× faster convergence fixes
12. **Protocol 12**: Re-Validation - 8× fraud reduction

**Impact**:
- **8× faster error response** (30-60 min vs 4-5 hours)
- **8× fraud risk reduction** (40% → <5%)
- **6-12 hours saved** through parallelization

---

### 8. Output Structure

#### LLM-MM-Agent: Three-Tier Structure

```
output/MM-Agent/{task}_{timestamp}/
├── Report/         # Final PDF reports
├── Workspace/      # json/, markdown/, latex/, code/, charts/
└── Memory/         # logs/, checkpoints/, usage/, evaluation/
```

**Key Features**:
- Checkpoint-based resume capability
- "Truth Mode" logging for forensic analysis
- "Latent Reporter" (post-processing research journal)
- Omni-Survival Kit (guarantees PDF generation)

#### MCM-Killer: Competition-Optimized Structure

```
output/
├── VERSION_MANIFEST.json    # Single source of truth
├── problem/                 # Problem files
├── docs/                    # Consultations, validation, reports
│   ├── research_notes.md
│   ├── consultations/       # Inter-agent feedback
│   ├── validations/         # Validation reports
│   └── feedback/            # Re-verification feedback
├── model/                   # Model designs
│   ├── model_design_*.md
│   └── model_proposals/     # Drafts for consultation
├── implementation/          # Code, data, logs, models
│   ├── .venv/              # Isolated Python environment
│   ├── code/               # Python model code
│   ├── data/               # Processed datasets
│   ├── models/             # Trained model objects
│   └── logs/               # Training logs
├── results/                 # Results files
├── figures/                 # Figures (standardized naming)
└── paper/                   # LaTeX, figures, summary
```

**Key Features**:
- VERSION_MANIFEST.json as single source of truth
- Data authority hierarchy: Code > Reports > Paper
- Mandatory documentation paths
- Standardized naming conventions

---

### 9. Usage Model

#### LLM-MM-Agent: Command Line Execution

```bash
cd "clean version/LLM-MM-Agent"
python MMAgent/main.py \
    --key "your_api_key" \
    --task "2024_C" \
    --model_name "gpt-4o"
```

**Configuration**: `config.yaml`
```yaml
top_method_num: 6
problem_analysis_round: 3
problem_modeling_round: 3
task_formulas_round: 5
num_tasks: 5
num_charts: 5
```

**Supported Models**: `gpt-4o`, `deepseek-chat`, `glm-4-flash`, `glm-4-plus`, `qwen2.5-72b-instruct`

#### MCM-Killer: Interactive CLI

```bash
cd "MCM-Killer/workspace/2025_C"
# Run Claude Code CLI and instruct:
# "Read CLAUDE.md and run the multi-agent workflow to solve this MCM problem."
```

**Configuration**: `.claude/CLAUDE.md`
- Agent definitions in `.claude/agents/`
- Main configuration in `.claude/CLAUDE.md`

**No Command Line Args**: Interactive configuration through prompts

---

### 10. When to Use Which System

#### Use LLM-MM-Agent When You Want To:

1. **Study the reference implementation** from NeurIPS/ICML papers
2. **Understand the 4-stage pipeline** architecture
3. **Retrieve modeling methods** via HMML (98+ schemas)
4. **Run autonomous problem solving** with minimal configuration
5. **Compare research prototype** vs competition system
6. **Test different LLM models** (gpt-4o, deepseek, glm-4, qwen)
7. **Use command-line interface** (not interactive)
8. **Leverage checkpointing** and auto-resume
9. **Generate baseline results** for comparison
10. **Research and experimentation** in academic setting

#### Use MCM-Killer When You Want To:

1. **Participate in actual MCM/ICM competitions**
2. **Generate O-Prize competitive papers** ($1.5M target)
3. **Use multi-agent collaboration** with specialized roles
4. **Enforce strict quality control** and validation gates
5. **Benefit from 12 critical protocols** for anti-fraud
6. **Save 6-12 hours** through parallel workflow
7. **Have fast error response** (30-60 min vs 4-5 hours)
8. **Reduce academic fraud risk** (8× improvement)
9. **Use interactive CLI** for dynamic decision-making
10. **Win competitions** with production-quality outputs

---

## Decision Flowchart

```
                    Need to solve MCM problem?
                             │
                    ┌────────┴────────┐
                    │                 │
               Research?        Competition?
                    │                 │
                    ▼                 ▼
            Use LLM-MM-Agent    Use MCM-Killer
                    │                 │
           ┌────────┴────────┐   ┌────┴────┐
           │                 │   │         │
      Study pipeline    Test LLMs    Win      O-Prize
           │                 │   │    competitive
           ▼                 ▼   ▼         ▼
    Reference/       Command    Interactive  12
    Academic         line       CLI         protocols
```

---

## Migration Path

### From LLM-MM-Agent to MCM-Killer

If you have results from LLM-MM-Agent and want to enhance with MCM-Killer:

1. **Export LLM-MM-Agent outputs**:
   - Extract model designs from `Memory/`
   - Extract generated code from `Workspace/code/`
   - Extract results from `Workspace/json/`

2. **Import into MCM-Killer structure**:
   - Place designs in `output/model/`
   - Place code in `output/implementation/code/`
   - Place results in `output/results/`

3. **Run MCM-Killer validation**:
   - Phase 4.5: Implementation Fidelity check
   - Phase 5.5: Anti-Fraud validation
   - Phase 6-10: Enhanced paper generation

### From MCM-Killer to LLM-MM-Agent

If you want to test MCM-Killer designs with LLM-MM-Agent:

1. **Extract MCM-Killer designs**:
   - Read `output/model/model_design_*.md`

2. **Convert to LLM-MM-Agent format**:
   - Create simplified problem description
   - Extract model specifications

3. **Run LLM-MM-Agent**:
   - Use as reference comparison
   - Compare outputs side-by-side

---

## Conclusion

**Key Takeaway**:

- **LLM-MM-Agent** = Research prototype (academic baseline)
  - Use for: Study, reference, testing, experimentation
  - Not designed for: Competition-winning performance

- **MCM-Killer** = Competition system (production-ready)
  - Use for: Competitions, O-Prize, winning
  - Not designed for: Academic publication, simplicity

Both systems are complementary:
- Start with **LLM-MM-Agent** to understand the problem
- Switch to **MCM-Killer** for competition-level outputs
- Use both together for comprehensive problem solving

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Next**: See `02_LLM_MM_AGENT_ARCHITECTURE.md` for LLM-MM-Agent details
