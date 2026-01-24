# Workspace Structure v3.1.0

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Document Type**: Supporting Document
> **Purpose**: Complete specification of v3.1.0 workspace structure

---

## Overview

The v3.1.0 workspace structure is designed for **multi-competition reproducibility** with complete isolation between competitions.

**Key Principle**: One workspace directory per competition problem.

---

## Top-Level Structure

```
MCM-Killer/
├── architectures/              # Architecture documentation
│   ├── v3-0-0/                # v3.0.0 architecture
│   └── v3-1-0/                # v3.1.0 architecture (this version)
│
├── workspace/                 # Competition workspaces
│   ├── 2025_C/               # Example: 2025 Problem C
│   ├── 2025_D/               # Future: 2025 Problem D
│   └── 2026_A/               # Future: 2026 Problem A
│
├── knowledge_library/         # Shared knowledge base
│   ├── methods/              # HMML 2.0
│   └── academic_writing/     # Style guides
│
├── tools/                    # Shared utilities
│   ├── style_analyzer.py
│   ├── log_analyzer.py
│   ├── mmbench_score.py
│   └── migrate_hmml.py
│
└── reference_papers/         # O-Prize papers for style analysis
    ├── 2024_C_Oprize/
    ├── 2023_D_Oprize/
    └── ...
```

---

## Single Competition Workspace

### Complete Structure

```
workspace/2025_C/
│
├── VERSION_MANIFEST.json         # Single source of truth
│
├── output/                       # All outputs
│   ├── problem/                  # Problem files
│   │   ├── problem_statement.pdf
│   │   ├── problem_data.xlsx
│   │   └── requirements.md
│   │
│   ├── docs/                     # Documentation
│   │   ├── requirements/         # Requirements analysis
│   │   │   └── problem_statement.md
│   │   ├── knowledge/            # Knowledge retrieval
│   │   │   └── suggested_methods.md
│   │   ├── model/                # Model designs
│   │   │   ├── model_1_design.md
│   │   │   ├── model_2_design.md
│   │   │   └── model_3_design.md
│   │   ├── insights/             # Metacognitive insights
│   │   │   ├── narrative_arc_1.md
│   │   │   └── narrative_arc_2.md
│   │   ├── validation/           # Validation reports
│   │   │   ├── validation_report.md
│   │   │   ├── judgment_report.md
│   │   │   └── automated_score.json
│   │   └── reports/              # Final reports
│   │       ├── summary.md
│   │       ├── post_competition_analysis.md
│   │       └── DEFCON_1_LOG.md
│   │
│   ├── model/                    # Model designs (detailed)
│   │   ├── model_1/
│   │   │   ├── design.md
│   │   │   ├── equations.tex
│   │   │   └── assumptions.md
│   │   ├── model_2/
│   │   └── model_3/
│   │
│   ├── implementation/           # Code, data, logs
│   │   ├── code/                 # Python code
│   │   │   ├── main_1.py
│   │   │   ├── main_2.py
│   │   │   ├── dev_diary_1.md
│   │   │   ├── dev_diary_2.md
│   │   │   └── utils.py
│   │   ├── data/                 # Processed data
│   │   │   ├── train.csv
│   │   │   ├── test.csv
│   │   │   └── processed_data.pkl
│   │   ├── logs/                 # Training logs
│   │   │   ├── training_full.log
│   │   │   ├── summary.json
│   │   │   └── execution_tracker_readable.txt
│   │   ├── models/               # Trained models
│   │   │   ├── model_1.pkl
│   │   │   ├── model_2.pkl
│   │   │   └── checkpoints/
│   │   └── .venv/                # Isolated Python environment
│   │
│   ├── paper/                    # LaTeX paper
│   │   ├── main.tex
│   │   ├── references.bib
│   │   ├── figures/              # Generated figures
│   │   │   ├── figure_1.png
│   │   │   ├── figure_2.png
│   │   │   └── figure_3.png
│   │   └── paper.pdf
│   │
│   └── package/                  # Final submission package
│       ├── paper.pdf
│       ├── summary.pdf
│       ├── code.zip
│       └── README.md
│
├── config.yaml                   # Configuration
├── CLAUDE.md                     # @director's instructions
└── README.md                     # Workspace overview
```

---

## VERSION_MANIFEST.json

### Purpose

Single source of truth for tracking workspace state, preventing data authority conflicts.

### Structure

```json
{
  "competition": "2025_C",
  "version": "3.1.0",
  "created": "2025-02-04T08:00:00Z",
  "last_modified": "2025-02-06T16:30:00Z",
  "current_phase": 9,

  "data_authority": {
    "level_1": {
      "name": "Code Execution Outputs",
      "paths": [
        "output/implementation/data/*.csv",
        "output/implementation/data/*.pkl",
        "output/implementation/models/*.pkl"
      ],
      "description": "Raw numerical outputs from code execution"
    },
    "level_2": {
      "name": "Agent Reports",
      "paths": [
        "output/docs/validation/validation_report.md",
        "output/docs/model/model_*_design.md"
      ],
      "description": "Structured reports from agents"
    },
    "level_3": {
      "name": "Paper and Summary",
      "paths": [
        "output/paper/paper.pdf",
        "output/paper/summary.pdf"
      ],
      "description": "Final documents (must match Level 1)"
    }
  },

  "models": [
    {
      "id": 1,
      "name": "SIR-Network",
      "phase_completed": 5,
      "training_successful": true,
      "metrics": {
        "RMSE": 4.2,
        "R2": 0.89
      },
      "insight_extracted": true,
      "narrative_arc": "output/docs/insights/narrative_arc_1.md"
    },
    {
      "id": 2,
      "name": "SIR-SDE",
      "phase_completed": 5,
      "training_successful": true,
      "metrics": {
        "RMSE": 3.8,
        "R2": 0.92
      },
      "insight_extracted": true,
      "narrative_arc": "output/docs/insights/narrative_arc_2.md"
    }
  ],

  "phases": {
    "-1": {
      "name": "Style Guide Generation",
      "status": "complete",
      "completed_at": "2025-02-04T08:15:00Z",
      "output": "knowledge_library/academic_writing/style_guide.md"
    },
    "0": {
      "name": "Problem Understanding",
      "status": "complete",
      "completed_at": "2025-02-04T09:30:00Z",
      "output": "output/docs/requirements/problem_statement.md"
    },
    "0.2": {
      "name": "Active Knowledge Retrieval",
      "status": "complete",
      "completed_at": "2025-02-04T10:00:00Z",
      "output": "output/docs/knowledge/suggested_methods.md"
    },
    "0.5": {
      "name": "Feasibility Check",
      "status": "complete",
      "completed_at": "2025-02-04T11:00:00Z"
    },
    "1": {
      "name": "Model Design",
      "status": "complete",
      "completed_at": "2025-02-04T13:00:00Z"
    },
    "1.5": {
      "name": "Design Validation",
      "status": "complete",
      "completed_at": "2025-02-04T14:00:00Z"
    },
    "4": {
      "name": "Code Translation",
      "status": "complete",
      "completed_at": "2025-02-04T16:00:00Z",
      "dev_diaries": [
        "output/implementation/code/dev_diary_1.md",
        "output/implementation/code/dev_diary_2.md"
      ]
    },
    "4.5": {
      "name": "Code Validation",
      "status": "complete",
      "completed_at": "2025-02-04T17:00:00Z"
    },
    "5A": {
      "name": "Model Training (Preliminary)",
      "status": "complete",
      "completed_at": "2025-02-04T19:00:00Z"
    },
    "5B": {
      "name": "Model Training (Final)",
      "status": "complete",
      "completed_at": "2025-02-05T10:00:00Z"
    },
    "5.5": {
      "name": "Post-Training Validation",
      "status": "complete",
      "completed_at": "2025-02-05T11:30:00Z"
    },
    "5.8": {
      "name": "Insight Extraction",
      "status": "complete",
      "completed_at": "2025-02-05T13:00:00Z"
    },
    "6": {
      "name": "Result Generation",
      "status": "complete",
      "completed_at": "2025-02-05T15:00:00Z"
    },
    "7": {
      "name": "Paper Generation",
      "status": "complete",
      "completed_at": "2025-02-05T18:00:00Z"
    },
    "9": {
      "name": "Summary Generation",
      "status": "complete",
      "completed_at": "2025-02-05T19:00:00Z"
    },
    "9.1": {
      "name": "Mock Judging",
      "status": "complete",
      "completed_at": "2025-02-05T20:00:00Z",
      "verdict": "PASS",
      "score": 97,
      "defcon_1_triggered": false
    },
    "9.5": {
      "name": "Final Package",
      "status": "complete",
      "completed_at": "2025-02-05T21:00:00Z"
    },
    "10": {
      "name": "Submission",
      "status": "complete",
      "completed_at": "2025-02-05T22:00:00Z"
    },
    "11": {
      "name": "Self-Evolution",
      "status": "pending",
      "scheduled_for": "2025-04-01T00:00:00Z"
    }
  },

  "validation_gates": {
    "gate_0.5": {
      "name": "Feasibility Check",
      "status": "passed",
      "verdict": "PASS"
    },
    "gate_1.5": {
      "name": "Design Validation",
      "status": "passed",
      "verdict": "PASS"
    },
    "gate_4.5": {
      "name": "Code Validation",
      "status": "passed",
      "verdict": "PASS"
    },
    "gate_5.5": {
      "name": "Post-Training Validation",
      "status": "passed",
      "verdict": "PASS"
    },
    "gate_9.1": {
      "name": "Mock Judging",
      "status": "passed",
      "verdict": "PASS",
      "score": 97
    }
  },

  "issues": {
    "defcon_1_triggered": false,
    "defcon_1_duration": null,
    "defcon_1_iterations": 0
  },

  "statistics": {
    "total_duration_hours": 38,
    "models_trained": 2,
    "papers_generated": 1,
    "figures_created": 5,
    "code_files": 2,
    "agent_calls": 156
  }
}
```

---

## config.yaml

### Structure

```yaml
competition:
  id: "2025_C"
  name: "Problem C Name"
  start_date: "2025-02-04"
  end_date: "2025-02-08"

version:
  architecture: "3.1.0"
  workspace: "1.0"

agents:
  director:
    model: "gpt-4o"
    temperature: 0.7
    max_tokens: 2000

  researcher:
    model: "gpt-4o"
    temperature: 0.5

  modeler:
    model: "gpt-4o"
    temperature: 0.3

  writer:
    model: "gpt-4o"
    temperature: 0.5

  # ... other agents ...

phases:
  current_phase: 9
  auto_advance: true
  skip_completed: false

validation:
  strict_mode: true
  defcon_1_max_iterations: 3
  defcon_1_mercy_rule_threshold: 80

knowledge:
  hmml_path: "knowledge_library/methods"
  style_guide_path: "knowledge_library/academic_writing/style_guide.md"
  anti_patterns_path: "ANTI_PATTERNS.md"

output:
  base_path: "output"
  log_level: "INFO"
  save_checkpoints: true
  checkpoint_interval: 300  # seconds

time:
  competition_duration_hours: 96
  warning_threshold_hours: 72
  critical_threshold_hours: 88
```

---

## .venv/ (Isolated Python Environment)

### Purpose

Isolate Python dependencies for each competition to prevent version conflicts.

### Structure

```
.venv/
├── Lib/                     # Windows
│   └── site-packages/
│       ├── numpy/
│       ├── pandas/
│       ├── scipy/
│       ├── matplotlib/
│       ├── seaborn/
│       ├── scikit-learn/
│       ├── torch/
│       └── ...
├── Scripts/                 # Windows executables
│   ├── python.exe
│   ├── pip.exe
│   └── activate.bat
└── pyvenv.cfg
```

### Activation

**Windows**:
```bash
cd workspace/2025_C
.venv\Scripts\activate
```

**Linux/Mac**:
```bash
cd workspace/2025_C
source .venv/bin/activate
```

---

## File Naming Conventions

### Code Files
```
main_{model_id}.py           # Model implementation
utils.py                      # Shared utilities
config.py                     # Configuration
```

### Data Files
```
train.csv                     # Training data
test.csv                      # Test data
processed_data.pkl            # Preprocessed data
model_{model_id}.pkl          # Trained model
```

### Log Files
```
training_full.log             # Complete training log
summary.json                  # Compressed summary
execution_tracker_readable.txt
dev_diary_{model_id}.md       # Developer's diary
```

### Document Files
```
problem_statement.md          # Requirements analysis
model_{model_id}_design.md    # Model design
narrative_arc_{model_id}.md   # Insight extraction
validation_report.md          # Validation report
judgment_report.md            # Mock judgment
DEFCON_1_LOG.md              # Emergency repair log
```

### Figure Files
```
figure_{n}.png                # Data plots
figure_{n}.pdf                # Vector graphics (optional)
concept_{n}.mmd              # Mermaid diagrams
concept_{n}.gv               # Graphviz diagrams
```

---

## Data Authority Hierarchy

### Level 1: Code Execution Outputs (Highest Authority)

**Paths**:
- `output/implementation/data/*.csv`
- `output/implementation/data/*.pkl`
- `output/implementation/models/*.pkl`

**Authority**: Ground truth for all results

**Rule**: If paper differs from CSV, **paper is wrong**.

---

### Level 2: Agent Reports

**Paths**:
- `output/docs/validation/validation_report.md`
- `output/docs/model/model_*_design.md`

**Authority**: Intermediate authority, subject to Level 1 verification

**Rule**: Must be consistent with Level 1 data.

---

### Level 3: Paper and Summary (Lowest Authority)

**Paths**:
- `output/paper/paper.pdf`
- `output/paper/summary.pdf`

**Authority**: Derived from Level 1 and Level 2

**Rule**: Must exactly match Level 1 data. Any discrepancy = error in paper.

---

## Phase-Based File Generation

### Phase -1: Style Guide Generation
**Output**:
- `knowledge_library/academic_writing/style_guide.md`

### Phase 0: Problem Understanding
**Output**:
- `output/docs/requirements/problem_statement.md`

### Phase 0.2: Active Knowledge Retrieval
**Output**:
- `output/docs/knowledge/suggested_methods.md`

### Phase 1: Model Design
**Output**:
- `output/model/model_1/design.md`
- `output/model/model_1/equations.tex`
- `output/model/model_1/assumptions.md`

### Phase 4: Code Translation
**Output**:
- `output/implementation/code/main_1.py`
- `output/implementation/code/dev_diary_1.md`

### Phase 5: Model Training
**Output**:
- `output/implementation/models/model_1.pkl`
- `output/implementation/logs/training_full.log`
- `output/implementation/logs/summary.json`

### Phase 5.8: Insight Extraction
**Output**:
- `output/docs/insights/narrative_arc_1.md`

### Phase 6: Result Generation
**Output**:
- `output/implementation/data/results.csv`
- `output/implementation/data/processed_data.pkl`

### Phase 7: Paper Generation
**Output**:
- `output/paper/main.tex`
- `output/paper/paper.pdf`
- `output/paper/figures/figure_1.png`

### Phase 9: Summary Generation
**Output**:
- `output/paper/summary.pdf`

### Phase 9.1: Mock Judging
**Output**:
- `output/docs/validation/judgment_report.md`
- `output/docs/validation/automated_score.json`

### Phase 11: Self-Evolution
**Output**:
- `knowledge_library/evolution/violation_history.json`
- `knowledge_library/evolution/weakness_analysis.md`

---

## Backup and Checkpointing

### Automatic Checkpoints

**Interval**: Every 5 minutes (configurable)

**What Gets Backed Up**:
- `output/` directory
- `VERSION_MANIFEST.json`
- `config.yaml`

**Backup Location**:
```
workspace/2025_C/.backups/
├── checkpoint_20250204_080000/
├── checkpoint_20250204_080500/
└── ...
```

### Manual Checkpoints

**Command** (via @director):
```
@director: Create checkpoint
```

**Output**: `checkpoint_YYYYMMDD_HHMMSS/`

---

## Multi-Competition Support

### Creating New Competition Workspace

```bash
# Copy template
cp -r workspace/template/ workspace/2025_D/

# Update VERSION_MANIFEST.json
vim workspace/2025_D/VERSION_MANIFEST.json

# Update config.yaml
vim workspace/2025_D/config.yaml
```

### Isolated Environments

Each competition has its own `.venv/` to prevent dependency conflicts.

---

## Cleanup and Archiving

### Post-Competition Cleanup

**Keep**:
- All outputs in `output/`
- `VERSION_MANIFEST.json`
- `config.yaml`

**Optional - Archive**:
- `.backups/` (old checkpoints)
- `.venv/` (if disk space needed)

**Archive Command**:
```bash
# Create archive
tar -czf 2025_C_archive.tar.gz workspace/2025_C/

# Move to archives/
mv 2025_C_archive.tar.gz archives/
```

---

## Quality Assurance

### Verification Checklist

**For New Workspace**:
- [ ] `VERSION_MANIFEST.json` created
- [ ] `config.yaml` configured
- [ ] `.venv/` created and activated
- [ ] Dependencies installed
- [ ] `CLAUDE.md` present
- [ ] `output/` directory structure created

**For Existing Workspace**:
- [ ] `VERSION_MANIFEST.json` up-to-date
- [ ] All phase outputs present
- [ ] Data authority hierarchy respected
- [ ] No conflicting data sources

---

## Related Documents

- `29_cognitive_narrative_framework.md` - Phase 5.8 outputs
- `30_hmml_2.0_specification.md` - Knowledge library structure
- `05_agent_specifications.md` - Agent responsibilities
- Protocol 1: File Reporting

---

**Document Version**: v3.1.0
**Last Updated**: 2026-01-24
**Status**: Complete
