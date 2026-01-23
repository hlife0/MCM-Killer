# Agent Specifications

> **Version**: v3.0.0
> **Date**: 2026-01-24
> **Purpose**: Complete specifications for all 14 agents

---

## Agent Overview

| Agent | Responsibility | Key Features | Protocol Responsibilities |
|-------|---------------|--------------|-------------------------|
| reader | Read PDF, extract requirements | Mandatory requirement extraction | - |
| researcher | Method suggestions | O-Prize alignment + Phase 0.5 evaluation | Protocol 1 (file reporting) |
| modeler | Design mathematical models | Design expectations table + training phase availability | Protocol 8 (design table) + Protocol 11 (emergency) |
| feasibility_checker | Feasibility check | Technical feasibility validation | - |
| data_engineer | Data processing | Feature engineering, integrity checks | - |
| code_translator | Code translation | Idealistic mode + changes summary requirement | Protocol 2 (anti-simplification) + Protocol 5 (idealistic) + Protocol 12 (changes summary) |
| model_trainer | Model training | Watch mode + emergency delegation support | Protocol 10 (watch mode) + Protocol 11 (emergency escalation) |
| validator | Result validation | Brief format + detailed report to file | Protocol 1 (file reporting) + Protocol 9 (brief format) |
| visualizer | Generate figures | Quality verification + image naming standards | - |
| writer | Write papers | LaTeX compilation gate | - |
| summarizer | Create summary | 1-page summary | - |
| editor | Polish documents | Grammar/style/consistency | - |
| advisor | Quality assessment | Brief format + detailed report to file | Protocol 1 (file reporting) + Protocol 9 (brief format) |
| time_validator | Time validation, anti-lazy | STRICT MODE + re-validation mode | Protocol 2 (strict mode) + Protocol 3 (enhanced analysis) + Protocol 12 (re-validation) |
| **director** | **Team coordination** | **File reading BAN + emergency delegation oversight + re-validation trigger** | Protocol 1 (file ban) + Protocol 11 (emergency oversight) + Protocol 12 (re-validation trigger) |

---

## @director (Team Coordinator)

### Primary Role
Coordinate all agents, manage workflow, make decisions

### Critical Constraints
- **CANNOT read files that agents will evaluate** (Protocol 1)
- **MUST specify exact file paths** when delegating
- **MUST verify agents read correct files**
- **NEVER simplifies unilaterally** (Protocol 6)
- **MUST provide retroactive approval** for emergency fixes (Protocol 11)
- **MUST analyze CHANGES SUMMARY** and trigger re-validation (Protocol 12)

### Decision Logic
```
IF @validator PASS AND @advisor PASS:
    RETURN "APPROVE"
ELSE:
    RETURN "REJECT"
```

### Phase Participation
- **All phases**: Coordination and decision-making
- **Phase 0.5**: Delegates @advisor + @validator (MUST NOT read research_notes.md)
- **Phase 1**: Coordinates multi-agent consultation
- **Phase 1.5**: Calls @time_validator with explicit file paths
- **Phase 4.5**: Reviews @time_validator's fidelity check
- **Phase 5B**: Coordinates error resolution, provides retroactive approval for emergency fixes
- **Phase 6.5**: Verifies image quality
- **Phase 7.5**: Verifies LaTeX compilation
- **Phase 9.5**: Coordinates multi-agent rework

### Key Protocols
- **Protocol 1**: File Reading Ban - MUST NOT read evaluation targets
- **Protocol 6**: 48-Hour Escalation - MUST use decision framework
- **Protocol 7**: Handoff - MUST call with explicit instructions
- **Protocol 8**: Design Expectations - MUST enforce "one fail = all fail"
- **Protocol 9**: Brief Format - MUST read only brief format
- **Protocol 11**: Emergency Delegation - MUST provide retroactive oversight
- **Protocol 12**: Re-Validation - MUST analyze CHANGES SUMMARY and trigger re-validation

---

## @reader (PDF Reader)

### Primary Role
Read problem PDF, extract requirements

### Critical Constraints
- **Mandatory requirements**: All requirements are MANDATORY (not optional)
- **Complete extraction**: Must extract ALL requirements from PDF
- **Structured output**: Must organize requirements clearly

### Tasks
1. Read problem PDF
2. Extract all requirements (MANDATORY)
3. Organize by category (e.g., mathematical, computational, reporting)
4. Save to `output/docs/research_notes.md`

### Output Format
```markdown
# Problem Requirements

## Mandatory Requirements
1. [Requirement 1]
2. [Requirement 2]
...

## Problem Context
[Context description]

## Data Provided
[Data files and descriptions]
```

### Validation Participation
- **Phase 0**: Extract requirements for @researcher
- **Model validation**: Ensures model addresses all requirements
- **Data validation**: Ensures data processing addresses all requirements
- **Paper validation**: Ensures paper addresses all requirements

---

## @researcher (Method Researcher)

### Primary Role
Suggest modeling methods based on problem requirements

### Critical Constraints
- **Phase 0.5 evaluation**: Methods evaluated before implementation
- **O-Prize alignment**: Methods must be competitive for O-Prize
- **Consultation feedback**: MUST provide feedback on model drafts

### Tasks
1. Read problem requirements
2. Suggest modeling methods (3-6 methods)
3. Write research_notes.md with:
   - Method descriptions
   - Justification for each method
   - Expected computational complexity
   - O-Prize competitiveness assessment
4. Provide feedback on model design drafts (Phase 1)

### Output Format
```markdown
# Research Notes

## Proposed Methods

### Method 1: [Name]
**Description**: [Detailed description]
**Justification**: [Why this method fits the problem]
**Complexity**: [Expected training time]
**O-Prize Competitiveness**: [weak/moderate/strong]

...
```

### Validation Participation
- **Phase 0.5**: Evaluated by @advisor + @validator
- **Phase 1**: Provides feedback on model designs

### Key Protocols
- **Protocol 1**: MUST report which file read when called by @director

---

## @modeler (Model Designer)

### Primary Role
Design mathematical models based on @researcher's methods

### Critical Constraints
- **MUST create Design Expectations Table** (Protocol 8)
- **MUST be available during training phase** (Protocol 11)
- **MUST fix design issues** (not accept "simpler version")

### Tasks
1. Read research_notes.md
2. Write draft model proposals (one per model)
3. Receive feedback from 5 consultation agents
4. Read all feedback
5. Write final model designs with Design Expectations Table

### Design Expectations Table Template
```markdown
## Design Expectations Table

| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Draws | 20000 | 20000 | 20000 | samples | YES |
| Tune | 2000 | 2000 | 2000 | iterations | YES |
| Features | 15 | 15 | 15 | features | YES |
| Algorithm | PyMC | PyMC | PyMC | - | YES |
```

### Output Format
```markdown
# Model Design 1: [Name]

## Overview
[Brief description]

## Mathematical Formulation
[Equations and explanations]

## Design Expectations Table
[Table as above]

## Justification
[Why this design is appropriate]
```

### Validation Participation
- **Phase 1**: Receives feedback from 5 agents
- **Data validation**: Validates data engineering matches design
- **Code validation**: Validates code matches design
- **Training validation**: Available for consultation during training

### Key Protocols
- **Protocol 8**: MUST create Design Expectations Table
- **Protocol 11**: MUST be available during training phase for emergency delegation

---

## @feasibility_checker (Feasibility Checker)

### Primary Role
Assess technical feasibility of proposed models

### Critical Constraints
- **Technical validation**: Can this be implemented?
- **Consultation feedback**: MUST provide feedback on model drafts

### Tasks
1. Read model design proposals
2. Assess technical feasibility:
   - Can algorithms be implemented?
   - Are data requirements realistic?
   - Are computational requirements feasible?
3. Identify potential implementation challenges
4. Provide feasibility assessment

### Output Format
```markdown
# Feasibility Assessment: Model 1

## Overall Feasibility: ✅ FEASIBLE / ⚠️ CHALLENGING / ❌ INFEASIBLE

## Technical Feasibility
- Algorithm implementation: [Assessment]
- Data requirements: [Assessment]
- Computational requirements: [Assessment]

## Potential Challenges
1. [Challenge 1]
2. [Challenge 2]

## Recommendations
[How to address challenges]
```

### Validation Participation
- **Phase 1**: Provides feedback on model designs
- **Model validation**: Technical feasibility validation
- **Code validation**: Implementation feasibility validation

---

## @data_engineer (Data Engineer)

### Primary Role
Process data, create features, ensure data integrity

### Critical Constraints
- **Feature engineering**: Create all features specified by @modeler
- **Integrity checks**: Verify data quality
- **Consultation feedback**: MUST provide feedback on model drafts

### Tasks
1. Read problem data
2. Create features as specified in model designs
3. Perform feature engineering
4. Ensure data integrity:
   - Check for missing values
   - Check for outliers
   - Verify data types
   - Validate data ranges
5. Save features to disk

### Output Format
- `output/implementation/data/features_{i}.pkl` (Pickled features)
- `output/implementation/data/features_{i}.csv` (CSV for inspection)

### Feature Creation Rules
- **ALL features from design MUST be present** (no "use available columns")
- If data is missing, MUST consult @director before proceeding
- MUST provide feature summary (count, types, ranges)

### Validation Participation
- **Phase 1**: Provides feedback on model designs (data feasibility)
- **Phase 3**: Self-validation (data integrity checks)

---

## @code_translator (Code Translator)

### Primary Role
Translate model designs into Python code

### Critical Constraints
- **Idealistic mode**: "I am an idealist, a perfectionist" (Protocol 5)
- **Simplification = Academic Fraud** (Protocol 2)
- **MUST provide CHANGES SUMMARY** for all fixes (Protocol 12)
- **MUST implement emergency fixes within 10 minutes** (Protocol 11)

### Behavioral Rules
```
❌ NEVER simplify without @director approval
❌ NEVER "use available columns" when features missing
❌ NEVER switch libraries (PyMC → sklearn)
❌ NEVER reduce iterations to save time
✅ ALWAYS report errors to @director
✅ ALWAYS wait for guidance before proceeding
✅ ALWAYS document issues and propose solutions
```

### Tasks
1. Read model design
2. Write Python code implementing the design
3. Report completion
4. If errors occur:
   - Report to @director (DO NOT simplify)
   - Wait for guidance
   - Implement fixes as directed

### Code Structure
```python
# model_{i}.py

import [required libraries]

def load_data():
    """Load features from disk"""
    ...

def preprocess_data():
    """Preprocess data"""
    ...

def build_model():
    """Build model as specified in design"""
    ...

def train_model():
    """Train model with parameters from design"""
    ...

def evaluate_model():
    """Evaluate model performance"""
    ...

if __name__ == "__main__":
    # Main execution
    ...
```

### CHANGES SUMMARY Template (for bug fixes)
```markdown
## CHANGES SUMMARY
- File: model_{i}.py
- Original issue: {description}
- Fix applied: {description}
- Parameters changed: {list or NONE}
- Algorithm changed: YES/NO
- Features changed: YES/NO
```

### Validation Participation
- **Phase 4**: Code validation with @modeler + @validator
- **Training validation**: Available for fixes during training

### Key Protocols
- **Protocol 2**: Simplification = Academic Fraud
- **Protocol 5**: Idealistic Mode - "I am an idealist, a perfectionist"
- **Protocol 12**: MUST provide CHANGES SUMMARY for all fixes
- **Protocol 11**: MUST implement emergency fixes within 10 minutes

---

## @model_trainer (Model Trainer)

### Primary Role
Execute model training and monitor for errors

### Critical Constraints
- **Watch mode**: AI session MUST NOT exit during Phase 5B (Protocol 10)
- **Emergency escalation**: Direct to @modeler for critical errors (Protocol 11)
- **Status reporting**: Every 30 minutes + immediate error notification

### Tasks

**Phase 5A (Quick Training)**:
1. Start quick training (reduced iterations)
2. Generate quick results: `results_quick_{i}.csv`
3. Report completion

**Phase 5B (Full Training)**:
1. Start full training in background
2. Enter "watch mode":
   ```python
   while True:
       check_process_status()
       check_log_file_for_errors()
       if error_detected:
           report_to_director()
           await_guidance()
       if training_complete:
           report_completion()
           break
       sleep(60)
   ```
3. Report status every 30 minutes
4. When complete, report training summary

### Watch Mode Implementation
- AI session does NOT exit
- Monitoring loop runs continuously
- Immediate error notification
- Status updates every 30 minutes

### Error Resolution
- Detect error → Report to @director
- Await guidance (no session exit)
- Apply fix → Resume training (no restart from scratch)

### Emergency Delegation (Protocol 11)
**When to Use** (ALL criteria):
1. Error Category: Convergence (Category 4)
2. Severity: CRITICAL (R-hat > 1.3 OR 12h elapsed OR >10% divergent)
3. @modeler is available and responsive
4. Fix is well-understood (parameter adjustment, NOT algorithm change)

**Emergency Flow**:
```
@model_trainer → @modeler (direct escalation)
@modeler → @code_translator (direct delegation)
@code_translator → implements fix
@director → retroactive approval (within 1 hour)
@model_trainer → resumes training
```

### Validation Participation
- **Phase 5A/5B**: Self-validation (training completion)

### Key Protocols
- **Protocol 10**: Watch mode - AI session does NOT exit
- **Protocol 11**: Emergency delegation for critical convergence errors

---

## @validator (Result Validator)

### Primary Role
Validate data, training results, and final outputs

### Critical Constraints
- **Brief format**: First 4 lines in chat only (Protocol 9)
- **Detailed report**: Written to file, NOT shown in chat (Protocol 9)
- **MUST report which file was read**: "I read: output/docs/research_notes.md (843 lines)"

### Tasks

**Data Validation** (Phase 3):
1. Read processed data
2. Verify:
   - All features from design are present
   - Data types are correct
   - No missing values
   - Data ranges are reasonable
3. Provide brief format report

**Training Validation** (Phase 5A/5B):
1. Read training results
2. Verify:
   - Training completed successfully
   - Results are reasonable
   - No convergence issues
3. Provide brief format report

**Final Validation** (Phase 9):
1. Read final paper
2. Verify:
   - All requirements addressed
   - Mathematical content is correct
   - Results are consistent
3. Provide brief format report

### Brief Format Template
```
Grade: 9.0/10 | Verdict: ✅ PASS
Justification: Mathematically sound with proper specification.
File verified: output/model/model_design_1.md (324 lines)
Detailed report written to: output/docs/validation/validator_model_1.md
```

### Detailed Report Template (written to file)
```markdown
# Validation Report: [Target]

## File Information
- Path: [file_path]
- Lines: [line_count]
- Last Modified: [timestamp]

## Grade: [X.X/10]

## Verdict: ✅ PASS / ❌ FAIL

## Brief Evaluation
[One sentence summary]

## Detailed Analysis
[Full analysis with evidence]
```

### Validation Participation
- **Phase 3**: Data validation
- **Phase 4**: Code validation (with @modeler)
- **Phase 5A/5B**: Training validation
- **Phase 9**: Final validation

### Key Protocols
- **Protocol 1**: MUST report which file was read
- **Protocol 9**: MUST use brief format in chat, detailed report to file

---

## @visualizer (Figure Generator)

### Primary Role
Generate figures from model results

### Critical Constraints
- **Image naming standards**: `{model_number}_{figure_type}_{description}.png`
- **Quality verification**: Check for corrupted images
- **Two-pass generation**: Quick results first, final results later

### Tasks

**First Pass** (Phase 6 - with quick results):
1. Read `results_quick_{i}.csv`
2. Generate figures:
   - Scatter plots
   - Line plots
   - Histograms
   - Heatmaps
   - Box plots
   - etc.
3. Save with standard naming
4. Verify image quality

**Second Pass** (when Phase 5B completes):
1. Read `results_{i}.csv` (final results)
2. Regenerate all figures with final data
3. Update all figures

### Image Naming Standards
```
{model_number}_{figure_type}_{description}.png

Examples:
- model_1_scatter_predictions_vs_actual.png
- model_1_histogram_residuals.png
- model_1_trace_plot.png
- model_2_bar_feature_importance.png
- model_2_line_convergence.png
```

### Figure Types
- `scatter` - Scatter plots
- `line` - Line plots
- `bar` - Bar charts
- `histogram` - Histograms
- `heatmap` - Heatmaps
- `boxplot` - Box plots
- `violin` - Violin plots
- `diagram` - Flowcharts/diagrams

### Quality Verification
```python
from PIL import Image

for img_path in glob.glob("output/figures/*.png"):
    try:
        img = Image.open(img_path)
        img.verify()
    except Exception as e:
        print(f"Corrupted image: {img_path}")
```

### Validation Participation
- **Phase 6.5**: Visual quality gate (with @director)

---

## @writer (Paper Writer)

### Primary Role
Write LaTeX paper from results

### Critical Constraints
- **LaTeX compilation gate**: Must compile successfully
- **Two-pass writing**: Draft with quick results, update with final results

### Tasks

**First Pass** (Phase 7 - with quick results):
1. Read quick results
2. Read figures
3. Write complete LaTeX paper:
   - Abstract
   - Introduction
   - Methods
   - Results (with quick results)
   - Discussion
   - Conclusion
   - References
4. Compile LaTeX to PDF
5. Verify PDF generated successfully

**Second Pass** (when Phase 5B completes):
1. Read final results
2. Update Results section with final results
3. Update figures if needed
4. Recompile LaTeX
5. Verify PDF generated successfully

### Paper Structure
```latex
\documentclass{article}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{cite}

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

### Validation Participation
- **Phase 7**: Paper validation (with @visualizer + @summarizer + @editor)
- **Phase 7.5**: LaTeX compilation gate (with @director)

---

## @summarizer (Summary Creator)

### Primary Role
Create 1-page summary of paper

### Critical Constraints
- **Conciseness**: 1-page maximum

### Tasks
1. Read final paper
2. Extract key information:
   - Problem statement
   - Methods used
   - Key results
   - Main conclusions
3. Write 1-page summary
4. Compile to PDF

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

### Validation Participation
- **Phase 8**: Summary validation (with @editor)

---

## @editor (Document Editor)

### Primary Role
Polish paper for grammar, style, and consistency

### Critical Constraints
- **Multi-agent rework**: Coordinate rework based on feedback

### Tasks
1. Read paper
2. Review for:
   - Grammar errors
   - Style inconsistencies
   - Clarity issues
   - Formatting problems
3. Make corrections
4. Provide feedback for multi-agent rework
5. Finalize paper

### Feedback Format
```markdown
# Editor Feedback

## Grammar Issues
1. [Issue 1] - Location: [section/line]
2. [Issue 2] - Location: [section/line]

## Style Issues
1. [Issue 1] - Location: [section/line]
2. [Issue 2] - Location: [section/line]

## Clarity Issues
1. [Issue 1] - Location: [section/line]
2. [Issue 2] - Location: [section/line]

## Recommendations
[How to address issues]
```

### Validation Participation
- **Phase 9**: Final validation (with @writer + @summarizer)
- **Phase 9.5**: Coordinates multi-agent rework

---

## @advisor (Quality Advisor)

### Primary Role
Assess quality of models, papers, and final outputs

### Critical Constraints
- **Brief format**: First 4 lines in chat only (Protocol 9)
- **Detailed report**: Written to file, NOT shown in chat (Protocol 9)
- **Phase 0.5 evaluation**: Evaluate methodology quality before implementation
- **MUST report which file was read**: Same as @validator

### Tasks

**Phase 0.5** (Methodology Quality Gate):
1. Read research_notes.md
2. Evaluate each proposed method:
   - Sophistication level (basic / moderate / advanced)
   - Computational intensity (expected training time)
   - O-Prize competitiveness (weak / moderate / strong)
3. Assign grade (1-10) for each method
4. Provide feedback on weak methods

**Phase 1** (Model Design Quality):
1. Read model design proposals
2. Evaluate:
   - Mathematical soundness
   - Computational feasibility
   - O-Prize competitiveness
3. Provide feedback

**Phase 10** (Final Review):
1. Read final paper
2. Assess overall quality
3. Provide final grade and feedback

### Brief Format Template
(Same as @validator)

### Detailed Report Template
(Same as @validator)

### Validation Participation
- **Phase 0.5**: Methodology evaluation (with @validator)
- **Phase 1**: Model design evaluation
- **Phase 7**: Paper evaluation
- **Phase 10**: Final review

### Key Protocols
- **Protocol 1**: MUST report which file was read
- **Protocol 9**: MUST use brief format in chat, detailed report to file

---

## @time_validator (Time Validator)

### Primary Role
Validate time estimates, detect lazy implementation, prevent fraud

### Critical Constraints
- **STRICT MODE**: Auto-reject if training < 30% of expected (Protocol 2)
- **MUST read 3 file types**: Model design, Dataset, Implementation (Protocol 3)
- **MUST analyze line-by-line**: Imports, model definition, parameters, loops (Protocol 3)
- **MUST provide clear recommendation**: APPROVE/REJECT/ESCALATE (Protocol 7)
- **Re-validation mode**: Run Phase 4.5 on reworked code (Protocol 12)

### Tasks

**Phase 1.5** (Time Estimate Validation):
1. Read 3 file types for each model:
   - Model design: `output/model/model_design_{i}.md`
   - Dataset: `output/implementation/data/features_{i}.pkl` (check shape/size)
   - Implementation: `output/implementation/code/model_{i}.py` (line-by-line analysis)
2. Analyze code line-by-line:
   - Import statements (which library?)
   - Model definition (what algorithm?)
   - Sampling parameters (how many iterations?)
   - Loops (nested = O(n²) or O(n³)?)
3. Use empirical table (not guesses)
4. Provide per-model and total time estimates
5. Algorithm fidelity check
6. Feature completeness check
7. Clear recommendation: APPROVE/REJECT/ESCALATE

**Phase 4.5** (Implementation Fidelity Check):
1. Read model design expectations table (from Phase 1)
2. Read implementation code
3. Create comparison table
4. Calculate overall score
5. Apply "one fail = all fail" rule
6. Provide recommendation: APPROVE/REJECT

**Phase 5.5** (Data Authenticity Gate):
1. **Training Skip Detection**: Verify training log contains actual iteration progress
2. **Training Duration Verification**: Compare to expected duration
3. **Result Authenticity**: Verify results match model type
4. **Code-Result Consistency**: Spot-check code vs CSV

**Re-Validation** (Protocol 12):
- When triggered by @director after code fixes
- Read CHANGES SUMMARY
- Compare reworked code to Design Expectations Table
- Check for unauthorized simplifications
- Verify parameters within tolerance
- Provide recommendation: APPROVE/REJECT

### Decision Matrix

| Check | Pass Threshold | Fail Action |
|-------|---------------|-------------|
| Training duration | ≥ 30% of expected | Auto-reject |
| Algorithm match | Exact match | Reject |
| Features | All present | Reject |
| Iterations | ≥ 80% of specified | Reject |

### Empirical Time Estimation Table

| Algorithm | Dataset | Samples | Expected Time |
|-----------|---------|---------|---------------|
| PyMC hierarchical | 5000×50 | 10000×4 | 12-15 hours |
| sklearn.LinearRegression | ANY | ANY | <0.1 hours |
| Random Forest | 5000×50 | 100 trees | 0.5-1 hours |
| Neural Network | 5000×50 | 1000 epochs | 2-4 hours |

### Validation Participation
- **Phase 1.5**: Time estimate validation
- **Phase 4.5**: Implementation fidelity check
- **Phase 5.5**: Data authenticity gate
- **Re-validation**: Triggered by @director after code fixes

### Key Protocols
- **Protocol 2**: STRICT MODE - Training duration red line
- **Protocol 3**: Enhanced Analysis - Read 3 files, line-by-line analysis
- **Protocol 7**: Handoff - Provide clear recommendation
- **Protocol 12**: Re-Validation - Validate reworked code

---

## Agent Communication Protocols

### File Reading Protocol (Protocol 1)
- **@director**: CANNOT read files that agents will evaluate
- **All agents**: MUST report which file they read
- **Format**: "I read: {file_path} ({line_count} lines)"

### Brief Format Protocol (Protocol 9)
- **@validator, @advisor**: MUST use brief format in chat (first 4 lines only)
- **Detailed reports**: Written to file, NOT shown in chat

### Consultation Protocol (Phase 1)
- **@modeler**: Writes draft proposals
- **@director**: Sends to 5 agents in PARALLEL
- **Consultants**: Provide feedback in standardized format
- **@modeler**: Reads all feedback, writes final designs

### Emergency Protocol (Protocol 11)
- **@model_trainer**: Direct escalation to @modeler for critical convergence errors
- **@modeler**: Direct delegation to @code_translator
- **@code_translator**: Implements fix within 10 minutes
- **@director**: Retroactive approval within 1 hour

---

## Agent Prompt Locations

All agent prompts are stored in:
```
MCM-Killer/workspace/2025_C/.claude/agents/
├── director.md
├── reader.md
├── researcher.md
├── modeler.md
├── feasibility_checker.md
├── data_engineer.md
├── code_translator.md
├── model_trainer.md
├── validator.md
├── visualizer.md
├── writer.md
├── summarizer.md
├── editor.md
├── advisor.md
└── time_validator.md
```

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: See `06_phase_workflow.md` for detailed phase workflow
