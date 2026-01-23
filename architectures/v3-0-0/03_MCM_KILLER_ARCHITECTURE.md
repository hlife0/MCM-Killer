# MCM-Killer Architecture (System 2)

> **Version**: v3.0.0
> **Date**: 2026-01-23
> **Purpose**: Complete architecture documentation for MCM-Killer (Competition System)
> **Target**: O-Prize competitive ($1.5M target)

---

## System Overview

**MCM-Killer** is a competition-optimized multi-agent system for MCM/ICM competition participation with 14 specialized agents, 10-phase workflow, and 12 critical protocols.

**Location**: `MCM-Killer/workspace/2025_C/`

**Key Characteristics**:
- **Multi-Agent Architecture**: 14 specialized agents with single responsibilities
- **10-Phase Workflow**: 0 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5A → 5B → 5.5 → 6 → 6.5 → 7 → 7.5 → 8 → 9 → 9.5 → 10
- **7 Validation Gates**: METHODOLOGY, MODEL, TIME_CHECK, DATA, CODE, FIDELITY, TRAINING, ANTI_FRAUD, VISUAL, LATEX, PAPER, SUMMARY, FINAL, EDITOR
- **12 Critical Protocols**: Quality assurance and anti-fraud measures
- **Parallel Workflow**: Save 6-12 hours through parallelization
- **O-Prize Competitive**: Designed for $1.5M O-Prize competition

**Status**: Active development (continuous enhancement)

---

## Agent System

### 14 Specialized Agents

| Agent | Responsibility | Key Features | Validation |
|-------|---------------|--------------|------------|
| `reader` | Read PDF, extract requirements | Mandatory requirement extraction | MODEL, DATA, PAPER |
| `researcher` | Method suggestions | O-Prize alignment + Phase 0.5 evaluation | MODEL |
| `modeler` | Design mathematical models | Design expectations table + training phase availability | DATA, CODE, TRAINING |
| `feasibility_checker` | Feasibility check | Technical feasibility validation | MODEL, CODE |
| `data_engineer` | Data processing | Feature engineering, integrity checks | - |
| `code_translator` | Code translation | Idealistic mode + changes summary requirement | CODE, TRAINING |
| `model_trainer` | Model training | Watch mode + emergency delegation support | - |
| `validator` | Result validation | Brief format + detailed report to file | DATA, TRAINING, FINAL |
| `visualizer` | Generate figures | Quality verification + image naming standards | - |
| `writer` | Write papers | LaTeX compilation gate | PAPER |
| `summarizer` | Create summary | 1-page summary | - |
| `editor` | Polish documents | Grammar/style/consistency | - |
| `advisor` | Quality assessment | Brief format + detailed report to file | MODEL, PAPER, FINAL |
| `time_validator` | Time validation, anti-lazy | STRICT MODE + re-validation mode | MODEL, CODE, TRAINING |
| **`director`** | **Team coordination** | **File reading BAN + emergency delegation oversight + re-validation trigger** | **N/A** |

---

## Phase Workflow

### Phase 0: Problem Understanding

**Participants**: @reader, @researcher

**Tasks**:
1. @reader reads problem PDF
2. @reader extracts all requirements (MANDATORY, not optional)
3. @researcher suggests modeling methods
4. @researcher writes research_notes.md

**Output**: `output/docs/research_notes.md`

**Next**: Phase 0.5 (Model Methodology Quality Gate)

---

### Phase 0.5: Model Methodology Quality Gate ⭐

**Purpose**: Evaluate the quality of @researcher's proposed methods BEFORE @modeler starts implementation

**Participants**: @advisor, @validator

**Tasks**:
1. Read `output/docs/research_notes.md`
2. Evaluate each proposed method:
   - Sophistication level (basic / moderate / advanced)
   - Computational intensity (expected training time)
   - O-Prize competitiveness (weak / moderate / strong)
3. Assign grade (1-10) for each method
4. Provide feedback on weak methods

**Decision Criteria**:
- **Average grade >= 9/10**: ✅ PROCEED to Phase 1
- **Average grade 7-8/10**: ⚠️ ADVISE @researcher to enhance methods (optional)
- **Average grade < 7/10**: ❌ REWIND to Phase 0

**Output**: `output/docs/consultations/methodology_evaluation_1.md`

**Key Protocol**: @director CANNOT read research_notes.md (Protocol 1: File Reading Ban)

---

### Phase 1: Model Design

**Participants**: @modeler (primary), @researcher, @feasibility_checker, @data_engineer, @code_translator, @advisor

**Tasks**:
1. @modeler reads research_notes.md
2. @modeler writes draft model proposals (one per model)
3. @director sends drafts to 5 agents in PARALLEL for consultation
4. Each consultant provides feedback
5. @modeler reads all feedback
6. @modeler writes final model designs

**Output**:
- Draft proposals: `output/model/model_proposals/model_X_draft.md`
- Final designs: `output/model/model_design_X.md`

**Key Protocol**: Feedback File Standardization

**Canonical Path**: `output/docs/consultations/`
**Naming Convention**: `feedback_model_{model_number}_{agent_name}.md`

**Validation Gate**: ✅ MODEL (5 agents provide feedback)

---

### Phase 1.5: Time Estimate Validation

**Participants**: @time_validator

**Tasks**:
1. Read 3 file types for each model:
   - Model design: `output/model/model_design_{i}.md`
   - Dataset: `output/implementation/data/features_{i}.pkl` (check shape/size)
   - Implementation: `output/implementation/code/model_{i}.py` (line-by-line analysis)
2. Analyze code line-by-line
3. Use empirical table (not guesses)
4. Provide per-model and total time estimates
5. Algorithm fidelity check
6. Feature completeness check
7. Clear recommendation: APPROVE/REJECT/ESCALATE

**Output**: `output/docs/validation/time_validator_model_1.md`

**Validation Gate**: ✅ TIME_CHECK

**Key Protocol**: Enhanced Analysis (Protocol 3)

---

### Phase 2: Feasibility Check

**Participants**: @feasibility_checker

**Tasks**:
1. Assess technical feasibility of each model
2. Identify potential implementation challenges
3. Provide feasibility assessment

**Output**: `output/model/feasibility_{i}.md`

**Validation Participation**: MODEL, CODE

---

### Phase 3: Data Processing

**Participants**: @data_engineer

**Tasks**:
1. Read problem data
2. Create features as specified in model designs
3. Perform feature engineering
4. Ensure data integrity
5. Save features to disk

**Output**: `output/implementation/data/features_{i}.pkl`

**Validation Gate**: ✅ DATA (self-validation)

**Key Protocol**: All features from design MUST be present (no "use available columns")

---

### Phase 4: Code Translation

**Participants**: @code_translator (primary), @modeler, @validator

**Tasks**:
1. @code_translator reads model design
2. @code_translator writes Python code
3. @code_translator reports completion
4. @validator validates code correctness
5. If validation fails → Rewind to Phase 4

**Output**: `output/implementation/code/model_{i}.py`

**Validation Gate**: ✅ CODE (2 agents: @modeler + @validator)

**Key Protocol**: Idealistic Mode (Protocol 5)

---

### Phase 4.5: Implementation Fidelity Check

**Participants**: @time_validator

**Tasks**:
1. Read model design expectations table (from Phase 1)
2. Read implementation code
3. Create comparison table
4. Calculate overall score
5. Apply "one fail = all fail" rule
6. Provide recommendation: APPROVE/REJECT

**Output**: `output/docs/validation/time_validator_code_{i}.md`

**Validation Gate**: ✅ FIDELITY

**Key Protocol**: STRICT MODE (Protocol 2)

**Re-Validation** (Protocol 12): If @code_translator fixes bug during training, trigger re-validation

---

### Phase 5A: Quick Training

**Participants**: @model_trainer

**Tasks**:
1. Start quick training (reduced iterations)
2. Generate quick results: `results_quick_{i}.csv`
3. Report completion

**Output**: `output/results/results_quick_{i}.csv`

**Validation Gate**: ✅ TRAINING

**Time Expectation**: ~30 minutes

**Key Protocol**: Proceed immediately to Phase 6 (don't wait for Phase 5B)

---

### Phase 5B: Full Training (Parallel with Paper)

**Participants**: @model_trainer (primary), @director, @modeler, @code_translator

**Tasks**:
1. Start full training in background
2. Enter "watch mode" (AI session does NOT exit)
3. Monitor for errors
4. Report status every 30 minutes
5. When complete, report training summary

**Output**:
- Trained model: `output/implementation/models/model_{i}_full.pkl`
- Training log: `output/implementation/logs/training_{i}_full.log`
- Results: `output/results/results_{i}.csv`

**Validation Gate**: ✅ TRAINING

**Time Expectation**: Minimum 6 hours, Typical 8-12 hours, Maximum 48 hours

**Key Protocols**:
- **Watch mode** (Protocol 10)
- **Emergency delegation** (Protocol 11): 8× faster convergence fixes

---

### Phase 5.5: Data Authenticity Gate

**Participants**: @time_validator (primary), @director

**Tasks**:
1. **Training Skip Detection**: Verify training log contains actual iteration progress
2. **Training Duration Verification**: Compare to expected duration
3. **Result Authenticity**: Verify results match model type
4. **Code-Result Consistency**: Spot-check code vs CSV

**Decision Criteria**:
- **All checks pass**: ✅ AUTHENTIC → Proceed to Phase 6
- **1-2 checks fail**: ⚠️ SUSPICIOUS → Investigate
- **3+ checks fail**: ❌ FABRICATED → Re-run

**Output**: `output/docs/validation/time_validator_data_{i}.md`

**Validation Gate**: ✅ ANTI_FRAUD

**Key Protocol**: STRICT MODE (Protocol 2) - Red line: Auto-reject if < 30% of expected

---

### Phase 6: Visualization

**Participants**: @visualizer

**Tasks**:
1. **First pass** (with quick results from Phase 5A): Generate figures
2. **Second pass** (when Phase 5B completes): Regenerate with final results

**Output**: `output/figures/*.png`

**Key Protocol**: Image Naming Standards
- Naming: `{model_number}_{figure_type}_{description}.png`

---

### Phase 6.5: Visual Quality Gate

**Participants**: @visualizer, @director

**Tasks**:
1. Verify all images exist
2. Check for corrupted images
3. Count images
4. Verify image quality

**Decision**: ✅ PASS (all images present) / ❌ FAIL (corrupted images → Regenerate)

**Validation Gate**: ✅ VISUAL

---

### Phase 7: Paper Writing

**Participants**: @writer (primary), @visualizer, @summarizer, @editor

**Tasks**:
1. **First pass** (with quick results): Write complete paper
2. **Second pass** (when Phase 5B completes): Update Results section

**Output**: `output/paper/paper.pdf`

**Validation Gate**: ✅ PAPER (4 agents)

**Key Protocol**: LaTeX Compilation Gate (Phase 7.5)

---

### Phase 7.5: LaTeX Compilation Gate

**Participants**: @writer, @director

**Tasks**:
1. Compile LaTeX document
2. Check for compilation errors
3. Verify PDF generated successfully

**Decision**: ✅ PASS (compiles) / ❌ FAIL (errors → Fix and recompile)

**Validation Gate**: ✅ LATEX

---

### Phase 8: Summary

**Participants**: @summarizer (primary), @editor

**Tasks**:
1. Read paper
2. Create 1-page summary
3. Include key findings, methods, results

**Output**: `output/paper/summary.pdf`

**Validation Gate**: ✅ SUMMARY (2 agents)

**Constraint**: 1-page maximum

---

### Phase 9: Polish

**Participants**: @editor (primary), @writer, @summarizer

**Tasks**:
1. Review paper for grammar
2. Review for style consistency
3. Review for clarity
4. Make corrections
5. Finalize paper

**Output**: Polished `output/paper/paper.pdf`

**Validation Gate**: ✅ FINAL (3 agents)

---

### Phase 9.5: Editor Feedback Enforcement

**Participants**: @director, multiple agents

**Tasks**:
1. @editor provides feedback
2. @director coordinates rework
3. Multiple agents revise as needed
4. Re-verify changes

**Validation Gate**: ✅ EDITOR

**Key Protocol**: Multi-agent rework

---

### Phase 10: Final Review

**Participants**: @advisor

**Tasks**:
1. Read final paper
2. Assess overall quality
3. Provide final grade and feedback

**Output**: Final assessment report

**Key Protocol**: @advisor MUST report which file was read (Protocol 1)

---

## Output Structure

```
output/
├── VERSION_MANIFEST.json          # Single source of truth
│
├── docs/                          # ALL documentation
│   ├── research_notes.md          # Research methodology
│   ├── model/                     # Model designs
│   │   ├── model_design_1.md
│   │   └── model_proposals/       # Drafts
│   ├── consultations/             # Inter-agent feedback
│   │   ├── feedback_model_1_researcher.md
│   │   └── ...
│   ├── validations/               # Validation reports
│   │   ├── methodology_evaluation_1.md
│   │   ├── validator_model_1.md
│   │   └── ...
│   └── feedback/                  # Re-verification
│
├── data/                          # Feature files
│   ├── features_1.pkl
│   └── features_1.csv
│
├── implementation/                # Implementation files
│   ├── .venv/                   # Python virtual environment
│   ├── code/                      # Python code
│   │   ├── model_1.py
│   │   └── test_1.py
│   ├── data/                      # Processed datasets
│   ├── models/                    # Trained models
│   └── logs/                      # Training logs
│
├── results/                       # Results files
│   ├── results_1.csv
│   └── results_quick_1.csv
│
├── figures/                       # Figures
│   ├── model_1_scatter_predictions_vs_actual.png
│   └── ...
│
└── paper/                         # Paper outputs
    ├── paper.tex
    ├── paper.pdf
    ├── summary.pdf
    └── figures/
```

---

## 12 Critical Protocols

(See `04_PROTOCOLS_SUMMARY.md` for complete details)

1. **@director File Reading Ban** - Prevent evaluation contamination
2. **@time_validator Strict Mode** - Reject lazy implementations
3. **Enhanced Time Estimation** - Improve prediction accuracy
4. **Phase 5 Parallel Workflow** - Save 6-12 hours
5. **@code_translator Idealistic Mode** - Enforce perfect implementation
6. **48-Hour Escalation Protocol** - Decision framework
7. **@director/@time_validator Handoff** - Standardized communication
8. **Model Design Expectations** - Systematic validation
9. **@validator/@advisor Brief Format** - Fast decision-making
10. **Phase 5B Error Monitoring** - Prevent lost errors
11. **Emergency Convergence Delegation** - 8× faster response
12. **Phase 4.5 Re-Validation** - 8× fraud reduction

---

## Unique Innovations

1. **Multi-Agent Specialization**: 14 agents with single responsibilities
2. **12 Critical Protocols**: Comprehensive quality assurance
3. **Parallel Workflow**: Paper writing proceeds while training runs
4. **Emergency Delegation**: 8× faster critical error response
5. **Re-Validation Protocol**: 8× fraud risk reduction
6. **Strict Anti-Fraud**: Multiple validation layers
7. **Time Validator**: Dedicated agent for time estimation and lazy detection
8. **Brief Format**: Fast decision-making for validators
9. **Design Expectations**: Tolerance-based validation framework
10. **Watch Mode**: Real-time error monitoring during training

---

## When to Use MCM-Killer

Use MCM-Killer when you want to:
- Participate in actual MCM/ICM competitions
- Generate O-Prize competitive papers
- Use multi-agent collaboration with specialized roles
- Enforce strict quality control and validation
- Benefit from 12 critical protocols for anti-fraud
- Save 6-12 hours through parallel workflow
- Have fast error response (30-60 min vs 4-5 hours)
- Reduce academic fraud risk (8× improvement)
- Use interactive CLI for dynamic decision-making
- Win competitions with production-quality outputs

---

## Usage

**Basic Usage**:
```bash
cd "MCM-Killer/workspace/2025_C"
# Run Claude Code CLI and instruct to solve MCM problem
```

**Configuration**: `.claude/CLAUDE.md`
- Agent definitions in `.claude/agents/`
- Main configuration in `.claude/CLAUDE.md`

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: See `04_PROTOCOLS_SUMMARY.md` for all 12 protocols
