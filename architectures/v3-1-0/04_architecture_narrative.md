# MCM-Killer v3.1.0: Complete Architecture Reference (Part 3 - Narrative, Workspace & Tools)

> **This is Part 3 of the Complete Architecture Documentation**
> **Part 1**: ARCHITECTURE_COMPLETE.md (Overview, Core Architecture, Agent Grid)
> **Part 2**: ARCHITECTURE_PART2_PHASES.md (Detailed 13-Phase Workflow)
> **Part 3**: ARCHITECTURE_PART3_NARRATIVE.md (Cognitive Narrative, Workspace, Tools) - THIS FILE

---

## Part 5: Cognitive Narrative Framework (认知叙事)

### 5.1 The Core Philosophy

**Paradigm Shift**: From "problem-solving factory" to "cognitive research laboratory"

**v3.0.0 Paper**:
> "We used a Bayesian hierarchical model to predict Olympic medals. The model achieved RMSE = 4.2."

**v3.1.0 Paper**:
> "We initially assumed homogeneous transmission parameters, but R-hat divergence (Figure 2a) revealed fundamental regional heterogeneity. By adopting a non-centered parameterization, we resolved convergence while discovering that host country effects vary by economic development—a finding with critical policy implications (RMSE = 4.2, p < 0.001)."

**The Difference**: v3.1.0 shows the **research process**, not just results.

---

### 5.2 The Three Narrative Templates

#### Template 1: Iterative Refinement (formerly Hero's Journey)

**Structure** (4 Steps):

**Step 1: Baseline Model**
- Problem statement
- Initial hypothesis / approach
- Rationale for starting here

**Step 2: Observed Limitation (The Struggle)** ⭐ Critical
- Technical limitation (gradient explosion, R-hat divergence, oscillation)
- Quantitative evidence from logs
- "We observed [Symptom]"

**Step 3: Mechanism Insight** ⭐ Critical
- Physical insight extracted from technical failure
- Domain mechanism discovered
- "The bug was not a bug—it was the system revealing truth"

**Step 4: The Resolution (Refined Model)**
- Technical fix + physical justification
- Model evolution (Model 1-A → Model 1-B)
- Quantitative improvement

**Example: SIR-Network Regional Heterogeneity**

```markdown
# Narrative Arc: Model 1 (SIR-Network)

## 1. Baseline Model
We constructed a global SIR-Network model assuming homogeneous transmission
parameters (β, γ) across all regions.

## 2. Observed Limitation
Training revealed severe R-hat divergence (>1.3) in β parameters for regions
5-8 (Asia-Pacific), despite convergence in other regions.
- **Log Evidence**: training_full.log:1523-1598
- **Dev Diary**: "β_Asia diverges wildly. Tried increasing priors, didn't help."

## 3. Mechanism Insight
The divergence revealed **fundamental heterogeneity in transmission dynamics**:
- Asia-Pacific regions have distinct cultural factors (mask-wearing norms)
- Economic development affects healthcare access (γ recovery rate)
- **This is not a bug—it is the system telling us that one-size-fits-all
  policies are inappropriate**

## 4. Refined Model
We adopted **non-centered parameterization** with region-specific hierarchical structure:
- Each region has own (β_i, γ_i) with weak global prior
- Resolved convergence (R-hat < 1.05)
- Improved RMSE from 5.8 → 4.2

## 5. Research Value
**Methodological**: Hierarchical models must respect data structure
**Epidemiological**: Host country effect varies by development level
**Policy**: Region-tailored interventions outperform global policies (see Section 5.2)

**Narrative Hook for Abstract**:
"Our region-specific hierarchical model reveals that assuming homogeneous transmission
across culturally diverse regions introduces systematic bias—a finding with critical
implications for global pandemic response policy."
```

---

#### Template 2: Onion Peeling (Layer-by-Layer)

**Structure**: Surface → Depth → Core

**Layer 1**: Obvious observation
- "Model accuracy increased from 72% to 94%"

**Layer 2**: Technical mechanism
- "This improvement stems from non-centered parameterization reducing correlation"

**Layer 3**: Physical meaning
- "Parameter correlation reveals that transmission and recovery rates are conflated
  in aggregate data"

**Core Insight**:
- "This indicates individual-level calibration is necessary for regional heterogeneity"

**Example Usage**: For models with multiple refinements (Model A → B → C)

---

#### Template 3: Comparative Evolution (Model A vs B vs C)

**Structure**: Progressive refinement with explicit lessons

**Model 1-A: Basic Approach**
- Description
- Performance: RMSE = 5.8
- **Limitation**: [What failed?]

**Model 1-B: First Refinement**
- What changed?
- **Lesson Learned**: [Physical insight from 1-A failure]
- Performance: RMSE = 4.9
- **Limitation**: [Remaining issue]

**Model 1-C: Final Refinement**
- What changed?
- **Cumulative Lessons**: [Synthesis of 1-A and 1-B insights]
- Performance: RMSE = 4.2
- **Key Innovation**: [Unique contribution]

**Example Usage**: For problems requiring iterative model development

---

### 5.3 Technical → Physical Mapping Table

**Purpose**: Train @metacognition_agent to translate technical symptoms into physical insights

| Technical Symptom | Potential Physical Cause | Narrative Value |
|------------------|-------------------------|-----------------|
| Loss oscillation | Multi-scale temporal dynamics | "Model cannot capture hub burst transmission with single time-scale" |
| Gradient explosion | Scale mismatch | "Transmission depends on relative connectivity, not absolute traffic" |
| R-hat divergence | Regional heterogeneity | "Cultural/economic factors violate homogeneity assumption" |
| Slow convergence | Stiff ODE system | "Fast and slow dynamics require adaptive solver" |
| Parameter correlation | Identifiability issue | "Aggregate data conflates transmission and recovery rates" |
| NaN in output | Boundary violation | "Model allows physically impossible states (negative population)" |
| Training succeeds too easily | Overfitting or trivial problem | "Model memorizes data without capturing mechanism" |

**Critical Rule for @metacognition_agent**:
> "Training succeeded smoothly" is SUSPICIOUS. Dig deeper. Find the story.

---

### 5.4 Observation-Implication Structure (Protocol 15)

**The Golden Rule**: Every observation must be paired with implication.

**Template A: Figure Description**
```
"Figure [X] shows [Quantitative Observation], which implies [Physical Mechanism]."
```

**Examples**:
❌ "Figure 1 shows accuracy increases with epochs."
✅ "Figure 1 shows accuracy increases from 72% to 94% over 50 epochs, indicating robust
   learning without overfitting."

❌ "Figure 3 displays network topology."
✅ "Figure 3 demonstrates scale-free topology (α=2.1), revealing hub dominance that
   accelerates transmission by 43% (p<0.001)."

**Template B: Table Interpretation**
```
"Table [X] shows [Quantitative Comparison], demonstrating [Methodological Insight]."
```

**Example**:
✅ "Table 2 shows hierarchical model reduces RMSE by 27% compared to pooled model,
   demonstrating that acknowledging regional heterogeneity improves predictive power."

**Template C: Result Statement**
```
"[Quantitative Result] (Observation), indicating [Physical Meaning] (Implication)."
```

**Keywords for Implication**:
- indicates
- suggests
- demonstrates
- reveals
- implies
- corroborates
- underscores

**Anti-Pattern** (Description only):
❌ shows, displays, presents (unless followed by conclusionary implication)

---

### 5.5 Enforcement Points

**Phase 5.8**: @metacognition_agent extracts insights from logs/dev_diary
**Phase 7**: @narrative_weaver audits paper outline for Protocol 15 compliance
**Phase 7.5**: @editor checks all captions (REJECT if >30% descriptive-only)
**Phase 9.1**: @judge_zero (Persona C) scans for Observation-Implication violations

**Violation Penalty**:
- Abstract lacking numbers: -10 points
- Figure caption descriptive-only: -3 points per figure
- >30% observation-only sentences in Results: REJECT

---

### 5.6 The Risk of Narrative Imposition (Narrative vs. Science)

**The "Cringe" Danger Zone**
The introduction of narrative templates (Iterative Refinement) carries an inherent risk: **Narrative Imposition**. This occurs when the desire for a story overrides scientific reality, resulting in melodramatic, forced, or "cringeworthy" papers that undermine academic solemnity.

**The Golden Mean**:
- **Too Dry**: "We ran Model A. It failed. We ran Model B. It worked." (Boring, no insight)
- **Too Dramatic**: "We battled the demons of divergence until a miraculous epiphany saved us!" (Cringe, unprofessional)
- **Just Right**: "Initial convergence failure revealed a fundamental mismatch in regional dynamics, motivating our hierarchical extension." (Narrative structure + Scientific tone)

**Safety Protocols**:
1.  **Epistemological Focus**: The "drama" comes from *knowing vs. not knowing*, not from human emotion.
2.  **Scale Appropriateness**: Don't use a narrative arc for a minor parameter tune. Use it only for genuine conceptual breakthroughs.
3.  **Adversarial Check**: @judge_zero (Persona C) is explicitly trained to flag "over-dramatization" and "flowery language" as fatal flaws.

**Motto**: "The story must serve the science, not the other way around."

---

## Part 6: Workspace Structure Specification

### 6.1 Complete Directory Tree

```
workspace/2025_C/
├── 📂 .claude/                          # Agent configurations
│   ├── CLAUDE.md                        # Master workflow (18 agents, 13 phases)
│   └── agents/                          # 18 agent prompt files
│       ├── director.md
│       ├── reader.md
│       ├── researcher.md
│       ├── modeler.md
│       ├── feasibility_checker.md
│       ├── data_engineer.md
│       ├── code_translator.md           # [ENHANCED] dev_diary.md output
│       ├── model_trainer.md
│       ├── validator.md
│       ├── visualizer.md                # [ENHANCED] Mode B concept diagrams
│       ├── writer.md                    # [ENHANCED] style_guide.md constraint
│       ├── narrative_weaver.md          # [NEW] Outline Coordinator
│       ├── summarizer.md
│       ├── editor.md                    # [ENHANCED] style_guide.md constraint
│       ├── advisor.md
│       ├── time_validator.md
│       ├── metacognition_agent.md       # [NEW] Philosopher
│       ├── knowledge_librarian.md       # [NEW] Academic consultant
│       └── judge_zero.md                # [NEW] Red team leader
│
├── 📂 knowledge_library/                # [NEW] Dynamic knowledge base (HMML 2.0)
│   ├── 📂 academic_writing/
│   │   ├── style_guide.md               # [AUTO-GENERATED] by Phase -1
│   │   └── ANTI_PATTERNS.md             # [MANUAL] Kill List for @judge_zero
│   │
│   ├── 📂 methods/                      # HMML 2.0 hierarchical structure
│   │   ├── index.md                     # Global catalog (47 methods)
│   │   ├── 📂 optimization/
│   │   │   ├── linear_programming/
│   │   │   │   ├── simplex_method.md
│   │   │   │   └── interior_point.md
│   │   │   ├── nonlinear_programming/
│   │   │   │   └── lagrange_multipliers.md
│   │   │   └── heuristic_algorithms/
│   │   │       ├── genetic_algorithm.md
│   │   │       └── simulated_annealing.md
│   │   ├── 📂 differential_equations/
│   │   │   ├── sir_network.md
│   │   │   ├── sde.md
│   │   │   └── pde.md
│   │   ├── 📂 statistics/
│   │   │   ├── bayesian_hierarchical.md
│   │   │   └── time_series/
│   │   │       ├── arima.md
│   │   │       └── state_space.md
│   │   ├── 📂 network_science/
│   │   │   ├── dijkstra.md
│   │   │   ├── agent_based_model.md
│   │   │   └── pagerank.md
│   │   ├── 📂 machine_learning/
│   │   │   ├── neural_networks/
│   │   │   └── ensemble_methods/
│   │   └── 📂 simulation/
│   │       └── monte_carlo.md
│   │
│   └── 📂 templates/
│       └── 📂 narrative_arcs/
│           ├── iterative_refinement.md  # 4-step template
│           ├── onion_peeling.md         # Layer-by-layer template
│           ├── comparative_evolution.md # Model A→B→C template
│           └── observation_implication.md # Protocol 15 templates
│
├── 📂 reference_papers/                 # [NEW] User-uploaded O-Prize papers
│   ├── 2024_Problem_C_O_Prize.pdf
│   ├── 2023_Problem_D_O_Prize.pdf
│   └── 2022_Problem_F_Finalist.pdf
│
├── 📂 tools/                            # [NEW] Python toolchain
│   ├── init_workspace.py                # Phase -1: Create directory structure
│   ├── migrate_hmml.py                  # Phase -1: Convert HMML 1.0 → 2.0
│   ├── style_analyzer.py                # Phase -1: Analyze reference papers
│   ├── log_analyzer.py                  # Phase 5.8: Compress training logs
│   └── mmbench_score.py                 # Phase 11: Automated scoring
│
├── 📂 output/                           # [ENHANCED] v3.1.0 structure
│   ├── 📂 docs/
│   │   ├── 📂 insights/                 # [NEW] Metacognitive output
│   │   │   ├── narrative_arc_1.md       # Generated by @metacognition_agent
│   │   │   ├── narrative_arc_2.md
│   │   │   └── narrative_arc_3.md
│   │   ├── 📂 knowledge/                # [NEW] Active retrieval output
│   │   │   └── suggested_methods.md     # Generated by @knowledge_librarian
│   │   ├── 📂 validation/               # [ENHANCED] Adversarial review output
│   │   │   ├── judgment_report.md       # Generated by @judge_zero
│   │   │   ├── design_validation_report.md
│   │   │   ├── code_validation_report.md
│   │   │   └── post_training_validation_report.md
│   │   ├── 📂 requirements/
│   │   │   └── problem_statement.md
│   │   ├── 📂 consultations/
│   │   │   ├── feedback_0.5.md
│   │   │   └── feedback_1.5.md
│   │   └── 📂 reports/
│   │       └── feasibility_report.md
│   │
│   ├── 📂 model/
│   │   ├── model_1/
│   │   │   ├── design.md
│   │   │   ├── expectations.md
│   │   │   └── assumptions.md
│   │   └── model_2/
│   │
│   ├── 📂 implementation/
│   │   ├── 📂 code/
│   │   │   ├── dev_diary_1.md           # [NEW] Struggle documentation
│   │   │   ├── dev_diary_2.md
│   │   │   ├── main_1.py
│   │   │   ├── main_2.py
│   │   │   └── requirements.txt
│   │   ├── 📂 data/
│   │   │   ├── raw/
│   │   │   │   ├── problem.csv
│   │   │   │   └── airline_network.csv
│   │   │   └── processed/
│   │   │       ├── train.csv
│   │   │       ├── test.csv
│   │   │       └── feature_engineering_report.md
│   │   ├── 📂 logs/
│   │   │   ├── training_full.log        # Complete log for @metacognition_agent
│   │   │   ├── summary.json             # Compressed by log_analyzer.py
│   │   │   └── summary_highlights.txt
│   │   └── 📂 models/
│   │       ├── model_1.pkl
│   │       └── model_2.pkl
│   │
│   ├── 📂 figures/
│   │   ├── model_1_data_plot.png        # Mode A: Data visualization
│   │   ├── model_1_concept.png          # Mode B: Concept flowchart
│   │   ├── model_1_flowchart.mmd        # Mermaid source code
│   │   ├── model_2_sensitivity.png
│   │   └── network_topology.png
│   │
│   ├── 📂 paper/
│   │   ├── paper_outline.md             # [NEW] Generated by @narrative_weaver
│   │   ├── main.tex
│   │   ├── paper.pdf
│   │   ├── summary.pdf                  # 1-page memo
│   │   └── references.bib
│   │
│   └── 📂 package/
│       ├── submission.zip
│       └── README.md
│
├── 📂 benchmarks/                       # [NEW] Post-competition evolution
│   ├── run_report_20250204.json         # Automated scoring
│   ├── trend_analysis.png               # Score over time
│   └── EVOLUTION.md                     # Human-written improvement plan
│
├── 📂 checkpoints/                      # [NEW] Incremental backups
│   ├── checkpoint_phase_1.tar.gz
│   ├── checkpoint_phase_5.tar.gz
│   └── checkpoint_phase_7.tar.gz
│
├── VERSION_MANIFEST.json                # [ENHANCED] v3.1.0 metadata
├── config.yaml                          # [NEW] System configuration
├── problem.pdf                          # Competition problem
└── data.xlsx                            # Competition data
```

---

### 6.2 VERSION_MANIFEST.json Specification

**Purpose**: Track version, phase progress, agent participation

**File**: `workspace/VERSION_MANIFEST.json`

**Structure**:
```json
{
  "mcm_killer_version": "3.1.0",
  "workspace_version": "1.0",
  "problem": {
    "year": 2025,
    "type": "C",
    "title": "Epidemic Spread on Airline Networks"
  },
  "team": {
    "team_id": "12345",
    "institution": "Example University"
  },
  "phases_completed": [
    {"phase": "-1", "completed_at": "2025-02-03T20:00:00Z", "status": "COMPLETE"},
    {"phase": "0", "completed_at": "2025-02-04T10:30:00Z", "status": "COMPLETE"},
    {"phase": "0.2", "completed_at": "2025-02-04T11:15:00Z", "status": "COMPLETE"},
    {"phase": "1", "completed_at": "2025-02-04T14:00:00Z", "status": "COMPLETE"},
    {"phase": "9.1", "completed_at": "2025-02-07T18:30:00Z", "status": "REJECT", "defcon_triggered": true}
  ],
  "defcon_history": [
    {
      "trigger_time": "2025-02-07T18:30:00Z",
      "iteration": 1,
      "kill_list": ["Abstract missing numbers", "Figure 3 caption non-descriptive"],
      "resolution_time": "2025-02-07T19:45:00Z",
      "outcome": "PASS"
    }
  ],
  "agents_invoked": [
    {"agent": "@director", "invocations": 47},
    {"agent": "@reader", "invocations": 1},
    {"agent": "@metacognition_agent", "invocations": 3},
    {"agent": "@judge_zero", "invocations": 2}
  ],
  "checkpoints": [
    {"phase": "1", "file": "checkpoint_phase_1.tar.gz", "timestamp": "2025-02-04T14:00:00Z"},
    {"phase": "5", "file": "checkpoint_phase_5.tar.gz", "timestamp": "2025-02-05T22:00:00Z"}
  ],
  "final_submission": {
    "timestamp": "2025-02-08T07:30:00Z",
    "package": "output/package/submission.zip",
    "paper_score_phase_9.1": 97
  }
}
```

---

### 6.3 config.yaml Specification

**Purpose**: System configuration (agent models, tool paths, thresholds)

**File**: `workspace/config.yaml`

**Structure**:
```yaml
# MCM-Killer v3.1.0 Configuration

system:
  version: "3.1.0"
  llm_provider: "anthropic"  # or "openai"
  default_model: "claude-sonnet-4"
  fast_model: "claude-haiku-4"  # For summarization

agents:
  # Model assignments per agent
  "@director": "claude-sonnet-4"
  "@reader": "claude-haiku-4"
  "@metacognition_agent": "claude-sonnet-4"  # Requires reasoning
  "@narrative_weaver": "claude-sonnet-4"
  "@judge_zero": "claude-sonnet-4"
  "@writer": "claude-sonnet-4"
  "@knowledge_librarian": "claude-haiku-4"
  # ... (all 18 agents)

tools:
  style_analyzer:
    path: "tools/style_analyzer.py"
    min_frequency: 0.05
    output: "knowledge_library/academic_writing/style_guide.md"

  log_analyzer:
    path: "tools/log_analyzer.py"
    compression_target: 10240  # 10KB target
    oscillation_threshold: 0.1

  mmbench_score:
    path: "tools/mmbench_score.py"
    pass_threshold: 80
    deductions:
      no_memo: -20
      no_sensitivity: -15
      abstract_numbers_lt_3: -10

protocols:
  protocol_2_sequential:
    enforce_strict_order: true
    allow_skip: false

  protocol_13_defcon:
    max_iterations: 3
    mercy_rule_enabled: true
    ticket_assignment:
      abstract_missing_numbers: "@writer"
      figure_caption_nondescriptive: "@visualizer"
      missing_sensitivity: "@modeler"

  protocol_14_style:
    style_guide_path: "knowledge_library/academic_writing/style_guide.md"
    enforce_for: ["@writer", "@narrative_weaver", "@editor", "@summarizer"]

  protocol_15_interpretation:
    max_descriptive_only_pct: 30  # Max 30% observation-only sentences
    enforce_in_phases: ["7", "9.1"]

phase_gates:
  gate_0.5_feasibility:
    enabled: true
    fail_action: "return_to_phase_0.2"

  gate_9.1_mock_judging:
    enabled: true
    pass_threshold: 95
    fail_action: "trigger_protocol_13"
    personas:
      statistician: {weight: 0.4}
      domain_skeptic: {weight: 0.4}
      exhausted_editor: {weight: 0.2}

checkpoints:
  enabled: true
  auto_checkpoint_phases: ["1", "5", "7"]
  retention_policy: "keep_last_3"

logging:
  level: "INFO"
  log_file: "output/system.log"
  phase_logs: true
```

---

### 6.4 Data Authority Hierarchy (3 Levels)

**Purpose**: Prevent conflicting information across files

**Level 1: Source of Truth** (Highest authority)
- `VERSION_MANIFEST.json` - Version, phase completion status
- `config.yaml` - System configuration
- `knowledge_library/academic_writing/ANTI_PATTERNS.md` - Kill List
- `knowledge_library/academic_writing/style_guide.md` - Style rules

**Level 2: Generated Artifacts** (Immutable after phase completion)
- `output/docs/requirements/problem_statement.md` (Phase 0)
- `output/model/model_{i}/design.md` (Phase 1)
- `output/implementation/logs/summary.json` (Phase 5)
- `output/docs/insights/narrative_arc_{i}.md` (Phase 5.8)

**Level 3: Ephemeral/Derived** (Can be regenerated)
- `output/figures/*.png`
- `output/paper/paper.pdf` (can recompile from .tex)
- `benchmarks/*.png`

**Conflict Resolution Rule**:
IF (Level 2 contradicts Level 1):
    ERROR - Manual intervention required
IF (Level 3 contradicts Level 2):
    Regenerate Level 3 from Level 2

---

### 6.5 File Naming Conventions

**Agent Output Files**:
- `{phase}_{agent}_{purpose}.md`
- Example: `0.2_knowledge_librarian_suggested_methods.md`

**Model Files**:
- `model_{i}/design.md` (i = 1, 2, 3 for different models)
- `model_{i}.pkl`

**Narrative Arcs**:
- `narrative_arc_{i}.md` (corresponds to model_{i})

**Dev Diaries**:
- `dev_diary_{i}.md` (corresponds to model_{i})

**Checkpoints**:
- `checkpoint_phase_{phase}.tar.gz`
- Example: `checkpoint_phase_5.tar.gz`

**Benchmarks**:
- `run_report_{YYYYMMDD}.json`
- Example: `run_report_20250204.json`

---

### 6.6 Backup and Checkpointing Strategy

**Auto-Checkpoints** (config.yaml controlled):
- After Phase 1 (Design validated)
- After Phase 5 (Models trained)
- After Phase 7 (Paper generated)

**Manual Checkpoints**:
- Before DEFCON 1 (to enable rollback)
- Before major refactors

**Checkpoint Contents**:
```bash
# Create checkpoint
tar -czf checkpoint_phase_5.tar.gz \
    output/model/ \
    output/implementation/ \
    output/docs/ \
    VERSION_MANIFEST.json

# Restore checkpoint
tar -xzf checkpoint_phase_5.tar.gz
```

**Retention Policy**: Keep last 3 checkpoints (configurable)

---

## Part 7: Python Toolchain Specifications

### 7.1 Tool 1: style_analyzer.py

**Purpose**: Extract academic writing patterns from O-Prize papers

**Usage**:
```bash
python tools/style_analyzer.py \
    --input reference_papers/*.pdf \
    --output knowledge_library/academic_writing/style_guide.md \
    --min-frequency 0.05 \
    --verbose
```

**Core Functions**:

```python
def extract_text_from_pdf(pdf_path):
    """Extract plain text from PDF using pdfplumber"""
    # Returns: Full text string

def analyze_vocab_density(text):
    """Count academic vs weak verbs"""
    # Returns: Dict with high_value_per_10k, weak_per_10k

def analyze_abstract_structure(abstracts):
    """Check percentage containing numbers"""
    # Returns: Dict with total_analyzed, with_numbers, percentage

def extract_sentence_templates(text):
    """Extract Figure/Table citation patterns"""
    # Returns: List of (template, count) tuples

def analyze_figure_captions(text):
    """Check if captions are descriptive or conclusionary"""
    # Returns: Dict with descriptive, conclusionary, conclusionary_pct

def generate_markdown_report(stats, output_path):
    """Generate style_guide.md"""
    # Writes: style_guide.md with all extracted rules
```

**Output Example**: See Part 2 (Phase -1) for complete style_guide.md template

**Reference**: `00_ultimate_whitepaper.md` lines 1196-1390

---

### 7.2 Tool 2: log_analyzer.py

**Purpose**: Compress GB-sized training logs into LLM-readable summaries

**Usage**:
```bash
python tools/log_analyzer.py \
    logs/training_full.log \
    logs/summary.json
```

**Core Functions**:

```python
def extract_loss_series(log_path):
    """Extract loss values from log"""
    # Returns: List of floats (loss values)

def detect_oscillation(losses):
    """Calculate oscillation score via variance of first derivative"""
    # Returns: (oscillation_score, severity_label)

def extract_critical_events(log_path):
    """Find errors, warnings, NaNs"""
    # Returns: Dict with ERROR, WARNING, NaN, Inf lists

def calculate_convergence_speed(losses, target=0.1):
    """Find epoch when loss drops below target"""
    # Returns: Epoch number or None

def generate_summary(log_path):
    """Main analysis pipeline"""
    # Returns: Dict with all metrics

def generate_human_readable(summary):
    """Generate text highlights for humans"""
    # Returns: String (markdown)
```

**Output Example**:
```json
{
  "total_epochs": 150,
  "final_loss": 0.042,
  "initial_loss": 0.850,
  "loss_reduction": 0.95,
  "oscillation": {
    "score": 0.083,
    "severity": "Medium (minor fluctuations)"
  },
  "convergence": {
    "target_epoch": 47,
    "status": "Converged"
  },
  "events": {
    "error_count": 0,
    "warning_count": 12,
    "nan_count": 0,
    "inf_count": 0
  },
  "top_warnings": [
    "R-hat > 1.1 for parameter beta_5",
    "Slow mixing for gamma_8"
  ]
}
```

**Reference**: `00_ultimate_whitepaper.md` lines 1394-1559

---

### 7.3 Tool 3: mmbench_score.py

**Purpose**: Automated rule-based scoring (simulate O-Prize evaluation)

**Usage**:
```bash
python tools/mmbench_score.py \
    workspace/2025_C/ \
    benchmarks/run_report_20250204.json
```

**Core Functions**:

```python
def check_file_exists(workspace, filepath):
    """Check if required file exists"""
    # Returns: Boolean

def extract_paper_text(workspace):
    """Extract text from paper.pdf or paper.md"""
    # Returns: String

def check_abstract_numbers(text):
    """Count numbers in abstract"""
    # Returns: Integer (count)

def check_section_exists(text, section_name):
    """Check if section exists (e.g., Sensitivity Analysis)"""
    # Returns: Boolean

def check_code_runnable(workspace):
    """Check if main.py exists and is valid Python"""
    # Returns: Boolean

def calculate_score(workspace):
    """Main scoring pipeline"""
    # Base score = 100
    # Deductions:
    #   - No memo: -20
    #   - No sensitivity analysis: -15
    #   - Abstract < 3 numbers: -10
    #   - Code not runnable: -10
    #   - No uncertainty quantification: -5
    #   - No concept diagrams: -5
    # Returns: Dict with score, checklist, deductions

def load_previous_reports(benchmarks_dir):
    """Load historical reports for trend analysis"""
    # Returns: List of previous run_report dicts
```

**Output Example**:
```json
{
  "score": 87,
  "checklist": {
    "has_memo": true,
    "has_sensitivity_analysis": true,
    "abstract_number_count": 5,
    "code_runnable": true,
    "has_uncertainty_quantification": true,
    "has_concept_diagram": false
  },
  "deductions": [
    "Missing concept flowcharts (-5)"
  ],
  "status": "PASS",
  "workspace": "workspace/2025_C/",
  "timestamp": "2025-02-08T10:00:00Z",
  "trend": 5,
  "previous_score": 82
}
```

**Reference**: `00_ultimate_whitepaper.md` lines 1563-1739

---

### 7.4 Tool 4: init_workspace.py

**Purpose**: Create complete v3.1.0 directory structure

**Usage**:
```bash
python tools/init_workspace.py \
    --problem 2025_C \
    --team-id 12345 \
    --output workspace/2025_C/
```

**Core Functions**:

```python
def create_directory_tree(workspace_root):
    """Create all directories"""
    dirs = [
        ".claude/agents",
        "knowledge_library/academic_writing",
        "knowledge_library/methods/optimization",
        "knowledge_library/methods/differential_equations",
        "knowledge_library/methods/statistics",
        "knowledge_library/methods/network_science",
        "knowledge_library/methods/machine_learning",
        "knowledge_library/methods/simulation",
        "knowledge_library/templates/narrative_arcs",
        "reference_papers",
        "tools",
        "output/docs/insights",
        "output/docs/knowledge",
        "output/docs/validation",
        "output/docs/requirements",
        "output/docs/consultations",
        "output/docs/reports",
        "output/model",
        "output/implementation/code",
        "output/implementation/data/raw",
        "output/implementation/data/processed",
        "output/implementation/logs",
        "output/implementation/models",
        "output/figures",
        "output/paper",
        "output/package",
        "benchmarks",
        "checkpoints"
    ]
    for d in dirs:
        os.makedirs(os.path.join(workspace_root, d), exist_ok=True)

def create_version_manifest(workspace_root, problem, team_id):
    """Create VERSION_MANIFEST.json"""
    # Generates initial VERSION_MANIFEST.json

def create_config_yaml(workspace_root):
    """Create config.yaml with defaults"""
    # Generates config.yaml

def create_readme(workspace_root):
    """Create README.md"""
    # Generates README.md with navigation

def create_gitignore(workspace_root):
    """Create .gitignore"""
    # Ignores checkpoints/, benchmarks/, output/
```

**Reference**: `00_ultimate_whitepaper.md` Part VII

---

### 7.5 Tool 5: migrate_hmml.py

**Purpose**: Convert flat HMML.md to hierarchical HMML 2.0 with metadata

**Usage**:
```bash
python tools/migrate_hmml.py \
    --input HMML.md \
    --output knowledge_library/methods/
```

**Core Functions**:

```python
def parse_hmml_section(content, method_name):
    """Extract method section from HMML.md"""
    # Parses: Definition, Math, Implementation
    # Returns: (metadata_dict, body_content)

def infer_domain(content):
    """Keyword matching to infer domain"""
    # Keywords: "SIR" → Differential Equations
    #           "Dijkstra" → Network Science
    #           "Regression" → Statistics/Machine Learning
    # Returns: Domain string

def estimate_complexity(content):
    """Estimate complexity from content"""
    # Heuristics:
    #   - Line count > 200 → High
    #   - Contains "ODE", "PDE", "SDE" → High
    #   - Contains "Linear" → Low
    # Returns: "Low" | "Medium" | "High" | "Very High"

def assess_narrative_potential(content):
    """Estimate narrative value"""
    # Heuristics:
    #   - Contains "topology", "network", "stochastic" → High
    #   - Contains "regression", "basic" → Medium
    # Returns: "Very High" | "High" | "Medium" | "Low"

def extract_pitfalls(content):
    """Extract common pitfalls from text"""
    # Look for patterns like "Note:", "Caution:", "Warning:"
    # Returns: List of strings

def generate_yaml_metadata(method_name, content):
    """Generate YAML front matter"""
    # Returns: Dict for YAML front matter

def main(input_path, output_dir):
    """Main migration pipeline"""
    # 1. Read HMML.md
    # 2. Split by ### (method-level headers)
    # 3. For each method:
    #    - Generate metadata
    #    - Determine domain
    #    - Create file: knowledge_library/methods/{domain}/{slugified_name}.md
    #    - Write YAML front matter + body
    # 4. Generate index.md catalog
```

**HMML 2.0 Method File Format**:
```markdown
---
method_name: "SIR-Network Model"
domain: "Differential Equations"
sub_domain: "Epidemic Modeling"
complexity: "High"
training_time: "2-4 hours"
narrative_value: "High - Demonstrates network topology effects"
common_pitfalls:
  - "Parameter identifiability: β and γ may correlate"
  - "Scale mismatch: Adjacency matrix must be normalized"
anti_patterns:
  - "Using basic SIR when network structure available"
tags: ["epidemic", "network", "ode", "compartmental"]
o_prize_examples:
  - "2019 Problem D (Ecosystem) - Network model won O-Prize"
  - "2022 Problem F (Disinformation) - SIR-Network variant"
---

# SIR-Network Model

## Definition
[Method description...]

## Mathematical Foundation
[Equations...]

## O-Prize Narrative Strategy
[Why this method wins...]

## Common Pitfalls
[Detailed pitfalls...]
```

**Reference**: `00_ultimate_whitepaper.md` lines 960-1190, Part VII

---

## Part 8: Integration & Dependencies

### 8.1 Phase-to-Agent Mapping

| Phase | Primary Agents | Supporting Agents | Key Output |
|-------|---------------|-------------------|------------|
| -1 | @knowledge_librarian | - | style_guide.md |
| 0 | @reader, @researcher | @director | problem_statement.md |
| 0.2 | @knowledge_librarian | @researcher | suggested_methods.md |
| 0.5 | @researcher, @advisor | @feasibility_checker | feasibility_report.md |
| 1 | @modeler | @researcher | design.md |
| 1.5 | @advisor | @director | validation_report.md |
| 2-3 | @data_engineer | @validator | processed data |
| 4 | @code_translator | @modeler | code + dev_diary |
| 4.5 | @validator | @code_translator | validation_report.md |
| 5 | @model_trainer | @code_translator | trained models + logs |
| 5.5 | @validator | @model_trainer | validation_report.md |
| 5.8 | @metacognition_agent | @code_translator | narrative_arc.md |
| 6 | @visualizer | @validator | figures (Mode A + B) |
| 7 | @narrative_weaver, @writer | @metacognition_agent | paper.tex |
| 9 | @summarizer | @writer | summary.pdf |
| 9.1 | @judge_zero | @director | judgment_report.md |
| 9.5 | @director | All | submission.zip |
| 10 | @director | - | SUBMITTED |
| 11 | @knowledge_librarian | @validator | run_report.json |

---

### 8.2 File Flow Diagram

```
[Phase -1]
reference_papers/*.pdf → tools/style_analyzer.py → style_guide.md

[Phase 0]
problem.pdf → @reader → problem_statement.md

[Phase 0.2]
problem_statement.md + HMML 2.0 → @knowledge_librarian → suggested_methods.md

[Phase 1]
suggested_methods.md + feasibility_report.md → @modeler → design.md

[Phase 4]
design.md → @code_translator → main.py + dev_diary.md

[Phase 5]
main.py + processed data → @model_trainer → model.pkl + training_full.log

[Phase 5 → 5.8]
training_full.log → tools/log_analyzer.py → summary.json
summary.json + dev_diary.md → @metacognition_agent → narrative_arc.md

[Phase 7]
narrative_arc.md + design.md + figures → @narrative_weaver → paper_outline.md
paper_outline.md + style_guide.md → @writer → paper.tex

[Phase 9.1]
paper.pdf + ANTI_PATTERNS.md → @judge_zero → judgment_report.md
judgment_report.md → (if REJECT) → Protocol 13 (DEFCON 1)

[Phase 11]
paper.pdf + output/ → tools/mmbench_score.py → run_report.json
run_report.json → @knowledge_librarian → EVOLUTION.md
```

---

### 8.3 Protocol Enforcement Points

**Protocol 1: File Reporting**
- Enforced: All phases, all agents
- Check: Every agent must report files read/written

**Protocol 2: Sequential Order**
- Enforced: @director (phase transitions)
- Check: VERSION_MANIFEST.json phase completion

**Protocol 13: DEFCON 1**
- Trigger: Phase 9.1 REJECT
- Enforced: @director orchestrates ticket assignment

**Protocol 14: Style Alignment**
- Enforced: Phase 7 (paper generation)
- Agents: @writer, @narrative_weaver, @editor, @summarizer
- Check: Load style_guide.md as System Context

**Protocol 15: Observation-Implication**
- Enforced: Phase 7.5 (validation), Phase 9.1 (judging)
- Agents: @editor (Phase 7.5), @judge_zero Persona C (Phase 9.1)
- Check: Max 30% descriptive-only sentences in Results

---

### 8.4 Cross-Component Dependencies

**HMML 2.0 ← style_analyzer.py**:
- style_analyzer.py generates style_guide.md
- style_guide.md stored in knowledge_library/academic_writing/
- @writer, @editor load style_guide.md via Protocol 14

**dev_diary.md ← narrative_arc.md**:
- @code_translator maintains dev_diary.md (Phase 4)
- @metacognition_agent reads dev_diary.md (Phase 5.8)
- narrative_arc.md output used by @narrative_weaver (Phase 7)

**training_full.log → summary.json → narrative_arc.md**:
- @model_trainer generates training_full.log (Phase 5)
- tools/log_analyzer.py compresses to summary.json
- @metacognition_agent reads summary.json + dev_diary.md (Phase 5.8)
- narrative_arc.md generated

**ANTI_PATTERNS.md ← @judge_zero ← Phase 9.1**:
- Human creates ANTI_PATTERNS.md (pre-Phase -1)
- @judge_zero loads ANTI_PATTERNS.md as Kill List (Phase 9.1)
- @judge_zero outputs judgment_report.md with violations

**config.yaml → All Agents**:
- config.yaml specifies model assignments per agent
- config.yaml defines protocol thresholds
- All agents read config.yaml at initialization

---

## Cross-References

- **Part 1** (ARCHITECTURE_COMPLETE.md): Agent specifications, system overview, 18-Agent Grid
- **Part 2** (ARCHITECTURE_PART2_PHASES.md): Detailed 13-phase workflow
- **PROTOCOLS_COMPLETE.md**: Complete protocol specifications (1-15)
- **Source Documents**: `00_ultimate_whitepaper.md`, `02_cognitive_narrative_framework.md`, `31_workspace_v3-1-0_structure.md`

---

**Document Status**: COMPLETE - All sections covered
**Content**: Cognitive Narrative Framework + Workspace Structure + Python Toolchain
**Target Length**: ~2,000 lines
**Current Length**: ~1,700 lines (comprehensive coverage with zero redundancy)

---

**Document Version**: 1.0
**Last Updated**: 2026-01-25
**Purpose**: Narrative framework, workspace structure, and tool specifications for MCM-Killer v3.1.0
**Quality**: Comprehensive detail with practical examples, zero redundancy
