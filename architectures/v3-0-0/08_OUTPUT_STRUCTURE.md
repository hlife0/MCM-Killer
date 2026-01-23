# Output Structure

> **Version**: v3.0.0
> **Date**: 2026-01-24
> **Purpose**: Complete specification of output directory structure

---

## Root Structure

```
output/
├── VERSION_MANIFEST.json          # Single source of truth
├── problem/                       # Problem files
├── docs/                          # ALL documentation (MANDATORY)
├── model/                         # Model designs
├── implementation/                # Code, data, logs, models
├── results/                       # Results files
├── figures/                       # Figures
└── paper/                         # LaTeX, figures, summary
```

---

## VERSION_MANIFEST.json

### Purpose
Single source of truth for version control, metadata, and data authority

### Structure
```json
{
  "version": "3.0.0",
  "problem": "2025_C",
  "start_time": "2026-01-23T10:00:00Z",
  "last_update": "2026-01-23T18:00:00Z",
  "current_phase": "Phase 7",
  "phases_completed": [
    "Phase 0",
    "Phase 0.5",
    "Phase 1",
    "Phase 1.5",
    "Phase 2",
    "Phase 3",
    "Phase 4",
    "Phase 4.5",
    "Phase 5A",
    "Phase 5B"
  ],
  "models": [
    {
      "model_id": 1,
      "name": "Bayesian Hierarchical Model",
      "status": "completed",
      "training_duration": "14.5 hours",
      "validation": "approved"
    },
    {
      "model_id": 2,
      "name": "Gradient Boosting Model",
      "status": "completed",
      "training_duration": "2.3 hours",
      "validation": "approved"
    }
  ],
  "emergency_fixes": [
    {
      "model_id": 1,
      "phase": "Phase 5B",
      "issue": "R-hat > 1.3",
      "fix": "Increased tune iterations from 2000 to 4000",
      "timestamp": "2026-01-23T15:30:00Z",
      "approved": true
    }
  ],
  "data_authority": {
    "level_1": "Code Execution Outputs (CSV/PKL)",
    "level_2": "Agent Reports",
    "level_3": "Paper/Summary"
  }
}
```

### Data Authority Hierarchy
1. **Level 1 (Highest)**: Code Execution Outputs (CSV/PKL)
2. **Level 2**: Agent Reports
3. **Level 3 (Lowest)**: Paper/Summary

**Rule**: Paper must always match CSV. If they differ, the Paper is wrong.

---

## problem/

### Purpose
Store problem PDF and related files

### Structure
```
problem/
├── problem.pdf                   # Original problem PDF
├── problem.txt                   # Extracted text (optional)
└── data/                         # Provided data files
    ├── data1.csv
    ├── data2.xlsx
    └── ...
```

---

## docs/

### Purpose
ALL documentation goes here (MANDATORY)

### Structure
```
docs/
├── research_notes.md             # Research methodology and notes
│
├── model/                        # Model design documents
│   ├── model_design_1.md
│   ├── model_design_2.md
│   ├── model_design_3.md
│   └── model_proposals/          # Draft proposals for consultation
│       ├── model_1_draft.md
│       ├── model_2_draft.md
│       └── model_3_draft.md
│
├── consultations/                # Inter-agent consultation feedback
│   ├── methodology_evaluation_1.md  # Phase 0.5 evaluation
│   │
│   ├── feedback_model_1_researcher.md
│   ├── feedback_model_1_feasibility_checker.md
│   ├── feedback_model_1_data_engineer.md
│   ├── feedback_model_1_code_translator.md
│   ├── feedback_model_1_advisor.md
│   │
│   ├── feedback_model_2_researcher.md
│   ├── feedback_model_2_feasibility_checker.md
│   └── ... (one file per agent per model)
│
├── validations/                  # Validation reports
│   ├── methodology_evaluation_1.md  # Phase 0.5 evaluation
│   │
│   ├── validator_model_1.md      # Phase 1 model validation
│   ├── validator_data_1.md       # Phase 3 data validation
│   ├── advisor_model_1.md        # Phase 1 model quality assessment
│   │
│   ├── time_validator_model_1.md     # Phase 1.5 time validation
│   ├── time_validator_code_1.md      # Phase 4.5 fidelity check
│   ├── time_validator_data_1.md      # Phase 5.5 authenticity check
│   │
│   └── ... (one per validation per model)
│
└── feedback/                     # Re-verification feedback
    ├── feedback_model_1.md
    └── ... (one per model)
```

### File Naming Conventions

**Consultations**:
- `feedback_model_{model_number}_{agent_name}.md`

**Validations**:
- `{agent_name}_{target}_{model_number}.md`
- Example: `time_validator_code_1.md`

---

## model/

### Purpose
Store model designs and feasibility assessments

### Structure
```
model/
├── model_design_1.md             # Final model design
├── model_design_2.md
├── model_design_3.md
│
├── model_proposals/              # Draft proposals
│   ├── model_1_draft.md
│   ├── model_2_draft.md
│   └── model_3_draft.md
│
├── feasibility_1.md              # Feasibility assessment
├── feasibility_2.md
└── feasibility_3.md
```

### Model Design Template
```markdown
# Model Design [N]: [Name]

## Overview
[Brief description]

## Mathematical Formulation
[Equations and explanations]

## Design Expectations Table

| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Draws | 20000 | 20000 | 20000 | samples | YES |

## Justification
[Why this design is appropriate]

## Expected Performance
[Expected metrics and benchmarks]
```

---

## implementation/

### Purpose
Store implementation files: code, data, models, logs

### Structure
```
implementation/
├── .venv/                        # Python virtual environment (isolated)
│   ├── bin/                      # (or Scripts on Windows)
│   ├── lib/
│   └── pyvenv.cfg
│
├── code/                         # Python model code
│   ├── model_1.py                # Model 1 implementation
│   ├── model_2.py                # Model 2 implementation
│   ├── model_3.py                # Model 3 implementation
│   ├── test_1.py                 # Test script for model 1
│   ├── test_2.py                 # Test script for model 2
│   └── test_3.py                 # Test script for model 3
│
├── data/                         # Processed datasets
│   ├── features_1.pkl            # Features for model 1 (pickled)
│   ├── features_2.pkl            # Features for model 2
│   ├── features_3.pkl            # Features for model 3
│   ├── features_1.csv            # Features for model 1 (CSV for inspection)
│   ├── features_2.csv            # Features for model 2
│   └── features_3.csv            # Features for model 3
│
├── models/                       # Trained model objects
│   ├── model_1_full.pkl          # Model 1 full training
│   ├── model_2_full.pkl          # Model 2 full training
│   └── model_3_full.pkl          # Model 3 full training
│
└── logs/                         # Training logs
    ├── training_1_full.log       # Model 1 training log
    ├── training_2_full.log       # Model 2 training log
    └── training_3_full.log       # Model 3 training log
```

### Virtual Environment (.venv/)
**Purpose**: Isolated Python environment for dependencies

**Creation**:
```bash
cd implementation
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Requirements**:
- PyMC3 / PyMC4 (for Bayesian models)
- scikit-learn (for ML models)
- pandas, numpy (for data)
- matplotlib, seaborn (for figures)
- All model-specific dependencies

### Code Structure Template
```python
# model_{i}.py

import [required libraries]

def load_data():
    """Load features from disk"""
    import pickle
    with open('../implementation/data/features_{i}.pkl', 'rb') as f:
        return pickle.load(f)

def preprocess_data(data):
    """Preprocess data"""
    ...

def build_model(data):
    """Build model as specified in design"""
    ...

def train_model(model, data):
    """Train model with parameters from design"""
    ...

def evaluate_model(model, data):
    """Evaluate model performance"""
    ...

def save_results(results, filename):
    """Save results to CSV"""
    import pandas as pd
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    # Main execution
    data = load_data()
    data = preprocess_data(data)
    model = build_model(data)
    model, results = train_model(model, data)
    metrics = evaluate_model(model, data)
    save_results(results, f'../output/results/results_{i}.csv')
```

---

## results/

### Purpose
Store results files (CSV format)

### Structure
```
results/
├── results_1.csv                 # Model 1 full training results
├── results_2.csv                 # Model 2 full training results
├── results_3.csv                 # Model 3 full training results
│
├── results_quick_1.csv           # Model 1 quick training results
├── results_quick_2.csv           # Model 2 quick training results
└── results_quick_3.csv           # Model 3 quick training results
```

### CSV Format
**Columns**: Vary by model type, but typically include:
- `sample_id` or `observation_id`
- `actual` (ground truth)
- `predicted` (model prediction)
- `residual` (error)
- Model-specific columns (e.g., `uncertainty` for Bayesian models)

### Data Authority (Level 1)
**Highest authority**: These CSV files are the ground truth
- Paper MUST match these results
- If paper differs, paper is wrong

---

## figures/

### Purpose
Store generated figures (PNG format)

### Structure
```
figures/
├── model_1_scatter_predictions_vs_actual.png
├── model_1_histogram_residuals.png
├── model_1_trace_plot.png
├── model_1_posterior_predictive.png
├── model_2_bar_feature_importance.png
├── model_2_line_convergence.png
├── model_3_heatmap_correlation.png
└── ... (standardized naming)
```

### Image Naming Standards
**Format**: `{model_number}_{figure_type}_{description}.png`

**Examples**:
- `model_1_scatter_predictions_vs_actual.png`
- `model_1_histogram_residuals.png`
- `model_2_bar_feature_importance.png`
- `model_3_heatmap_correlation.png`

**Figure Types**:
- `scatter` - Scatter plots
- `line` - Line plots
- `bar` - Bar charts
- `histogram` - Histograms
- `heatmap` - Heatmaps
- `boxplot` - Box plots
- `violin` - Violin plots
- `diagram` - Flowcharts/diagrams

### Quality Requirements
- **Format**: PNG
- **Resolution**: Minimum 300 DPI for publication
- **Size**: Reasonable file size (< 5MB per image)
- **Verification**: Use PIL to verify no corruption

---

## paper/

### Purpose
Store LaTeX source, compiled PDF, bibliography, figures, and summary

### Structure
```
paper/
├── paper.tex                     # LaTeX source
├── paper.pdf                     # Compiled PDF
├── paper.bib                     # Bibliography
├── references.bib                # Alternative bibliography file
│
├── figures/                      # Figures for paper (copied from output/figures/)
│   ├── figure_1.png
│   ├── figure_2.png
│   └── ...
│
└── summary.pdf                   # 1-page summary
```

### LaTeX Structure
```latex
\documentclass{article}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}
\usepackage{hyperref}

\title{[Title]}
\author{[Authors]}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
[Abstract]
\end{abstract}

\section{Introduction}
[Introduction]

\section{Methods}
[Methods]

\section{Results}
[Results]

\section{Discussion}
[Discussion]

\section{Conclusion}
[Conclusion]

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

### Compilation Process
```bash
cd output/paper
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### Summary Structure
```markdown
# Summary

## Problem
[Brief problem statement]

## Methods
[Methods used, 2-3 sentences]

## Key Results
[Main findings, bullet points]

## Conclusions
[Main conclusions, 2-3 sentences]
```

---

## File Creation Order

### Phase 0
```
docs/research_notes.md
```

### Phase 0.5
```
docs/validations/methodology_evaluation_1.md
```

### Phase 1
```
model/model_proposals/model_1_draft.md
model/model_proposals/model_2_draft.md
model/model_proposals/model_3_draft.md
docs/consultations/feedback_model_1_researcher.md
docs/consultations/feedback_model_1_feasibility_checker.md
docs/consultations/feedback_model_1_data_engineer.md
docs/consultations/feedback_model_1_code_translator.md
docs/consultations/feedback_model_1_advisor.md
... (repeat for models 2 and 3)
model/model_design_1.md
model/model_design_2.md
model/model_design_3.md
```

### Phase 1.5
```
docs/validations/time_validator_model_1.md
```

### Phase 2
```
model/feasibility_1.md
model/feasibility_2.md
model/feasibility_3.md
```

### Phase 3
```
implementation/data/features_1.pkl
implementation/data/features_1.csv
implementation/data/features_2.pkl
implementation/data/features_2.csv
implementation/data/features_3.pkl
implementation/data/features_3.csv
```

### Phase 4
```
implementation/code/model_1.py
implementation/code/model_2.py
implementation/code/model_3.py
```

### Phase 4.5
```
docs/validations/time_validator_code_1.md
docs/validations/time_validator_code_2.md
docs/validations/time_validator_code_3.md
```

### Phase 5A
```
results/results_quick_1.csv
results/results_quick_2.csv
results/results_quick_3.csv
```

### Phase 5B
```
implementation/models/model_1_full.pkl
implementation/models/model_2_full.pkl
implementation/models/model_3_full.pkl
implementation/logs/training_1_full.log
implementation/logs/training_2_full.log
implementation/logs/training_3_full.log
results/results_1.csv
results/results_2.csv
results/results_3.csv
```

### Phase 5.5
```
docs/validations/time_validator_data_1.md
docs/validations/time_validator_data_2.md
docs/validations/time_validator_data_3.md
```

### Phase 6
```
figures/model_1_scatter_predictions_vs_actual.png
figures/model_1_histogram_residuals.png
... (all figures)
```

### Phase 7
```
paper/paper.tex
paper/paper.bib
paper/figures/figure_1.png
paper/figures/figure_2.png
... (all paper figures)
paper/paper.pdf
```

### Phase 8
```
paper/summary.pdf
```

---

## File Size Guidelines

| File Type | Typical Size | Maximum Size |
|-----------|--------------|--------------|
| PDF (problem) | 1-5 MB | 20 MB |
| Markdown docs | 10-100 KB | 1 MB |
| CSV (results) | 100 KB - 10 MB | 50 MB |
| PKL (features) | 1-10 MB | 100 MB |
| PKL (models) | 10-100 MB | 500 MB |
| Logs (training) | 1-10 MB | 50 MB |
| PNG (figures) | 100 KB - 2 MB | 10 MB |
| PDF (paper) | 1-10 MB | 50 MB |
| PDF (summary) | 100-500 KB | 5 MB |

---

## Backup and Version Control

### VERSION_MANIFEST.json Update Schedule
- **After each phase**: Update `current_phase` and `phases_completed`
- **After training**: Update model status and duration
- **After emergency fixes**: Add to `emergency_fixes` array
- **Every hour**: Update `last_update` timestamp

### Backup Strategy
1. **Local backup**: Copy entire `output/` to backup location
2. **Remote backup**: Upload to cloud storage (if available)
3. **Version control**: Use git for VERSION_MANIFEST.json tracking

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: Return to `00_architecture.md` for complete system overview
