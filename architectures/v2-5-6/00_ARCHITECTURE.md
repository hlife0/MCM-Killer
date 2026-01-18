# MCM-Killer v2.5.6 System Architecture

> **Authoritative Architecture Definition** — All Agent prompts should be derived from this document.
> **Version**: v2.5.6
> **Date**: 2026-01-18
> **Critical Enhancements**: **[v2.5.6] 4 Critical Fixes + 1 New Rewind - Feedback file standardization, Phase 5.5 anti-fraud, Phase 0.5 model quality gate, Image file naming standardization**

---

## Document Relationships

| Document | Purpose |
|----------|---------|
| **`00_ARCHITECTURE.md`** (this document) | **Defines architecture and Agent contracts** |
| **`01_SUMMARY.md`** | **[v2.5.6] Complete summary of all v2.5.6 changes** |
| **`02_feedback_file_standardization.md`** | **[v2.5.6 NEW] Systematic feedback file naming and positioning rules** |
| **`03_phase_5.5_anti_fraud.md`** | **[v2.5.6 NEW] Enhanced Phase 5.5 anti-fraud checks** |
| **`04_phase_0.5_model_quality_gate.md`** | **[v2.5.6 NEW] Model methodology quality gate before Phase 1** |
| **`05_image_naming_standards.md`** | **[v2.5.6 NEW] Image file naming and storage standards** |

Reading order: **01_SUMMARY.md** → **02_feedback_file_standardization** → **03_phase_5.5_anti_fraud** → **04_phase_0.5_model_quality_gate** → **05_image_naming_standards** → **00_ARCHITECTURE.md**

> **CRITICAL v2.5.6 ENHANCEMENTS**: 4 critical fixes to prevent agent collaboration failures, detect training fraud, ensure model quality, and fix file naming issues.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.5.3 | 2026-01-15 | YAML frontmatter enforcement, agent loading fix |
| v2.5.4 | 2026-01-16 | 4 critical bug fixes (LaTeX, editor, multi-agent, modeler) |
| v2.5.5 | 2026-01-17 | 6 enhancements + @time_validator agent |
| **v2.5.6** | **2026-01-18** | **4 fixes: Feedback files, Phase 5.5, Phase 0.5, Image naming** |

---

## v2.5.6 Critical Fixes

### Problem: 4 Critical Issues Discovered in v2.5.5 Operation

**Issue 1: Feedback Files Not Found / Wrong Location**
- **Symptom**: @modeler tries to read `output/docs/consultations/feedback_model_1_*_researcher.md` but files don't exist. Then tries `output/consultations/feedback_*_researcher.md` but still not found.
- **Root Cause**:
  1. No systematic file naming convention for consultation feedback
  2. Path inconsistency (some agents use `output/consultations/`, others use `output/docs/consultations/`)
  3. Agents (@researcher, @feasibility_checker, @data_engineer, @code_translator, @advisor) may not be writing feedback files at all, or writing to wrong location
- **Solution**: **Feedback File Standardization Protocol** (see `02_feedback_file_standardization.md`)
  - Define canonical path: `output/docs/consultations/`
  - Define naming convention: `feedback_model_{model_number}_{agent_name}.md`
  - MANDATE all consulted agents MUST write feedback files
  - Add verification step: @director confirms all 5 feedback files exist before @modeler reads them

**Issue 2: Phase 5.5 Anti-Fraud Insufficient**
- **Symptom**: @time_validator only checks file timestamps and sizes, doesn't verify training actually occurred
- **Root Cause**: Phase 5.5 was added in v2.5.5 but doesn't check:
  - Whether training was skipped (agent claims training complete but no actual training happened)
  - Whether training duration is reasonable (claimed 4h but actually 2 minutes)
  - Whether training data is authentic (results match what code should produce)
- **Solution**: **Enhanced Phase 5.5 Anti-Fraud Protocol** (see `03_phase_5.5_anti_fraud.md`)
  - Check training logs for actual start/end timestamps
  - Verify training duration matches expected (2-6 hours for intensive methods)
  - Verify results match model complexity (Bayesian MCMC should produce posterior distributions, not point estimates)
  - Add "skip detection": Check if @model_trainer actually ran training iterations

**Issue 3: Model Methodology Quality Not Validated Early Enough**
- **Symptom**: @modeler implements a weak model (e.g., simple linear regression) based on @researcher's suggestions, but this is only discovered in Phase 10 (@advisor review) when it's too late
- **Root Cause**: No quality gate on model methodology BEFORE @modeler starts implementation
- **Impact**: Wasted time on weak models that don't meet O-Prize standards
- **Solution**: **New Phase 0.5: Model Methodology Quality Gate** (see `04_phase_0.5_model_quality_gate.md`)
  - After @researcher provides methods but BEFORE @modeler designs models
  - @advisor and @validator evaluate the proposed methodology's quality
  - If grade < 9/10, rewind to Phase 0.5 for @researcher to brainstorm better methods
  - Ensures only high-quality model approaches reach implementation

**Issue 4: Image File Naming Causes Errors**
- **Symptom**: Command `ls -lh output/figures/*..png` fails with "No such file or directory"
- **Root Cause**: Wildcard pattern `*..png` is incorrect (should be `*.png`)
- **Impact**: Image quality verification fails, cannot detect corrupted images
- **Solution**: **Image File Naming Standards** (see `05_image_naming_standards.md`)
  - Define standard naming: `{model_number}_{figure_type}_{description}.png`
  - Fix verification commands to use correct wildcards
  - Add image quality check protocol

---

## Agent System (v2.5.6)

### Agent Overview (Updated v2.5.6)

| Agent | Responsibility | v2.5.6 Changes | Validation Participation |
|-------|---------------|----------------|------------------------|
| `reader` | Read PDF, extract requirements | (inherited v2.5.5) | MODEL, DATA, PAPER |
| `researcher` | Method suggestions | **[v2.5.6] New Phase 0.5 evaluation** | MODEL |
| `modeler` | Design mathematical models | **[v2.5.6] Feedback file path fixed** | DATA, CODE, TRAINING |
| `feasibility_checker` | Feasibility check | **[v2.5.6] Feedback file path fixed** | MODEL, CODE |
| `data_engineer` | Data processing | **[v2.5.6] Feedback file path fixed** | - |
| `code_translator` | Code translation | **[v2.5.6] Feedback file path fixed** | CODE, TRAINING |
| `model_trainer` | Model training | **[v2.5.6] Phase 5.5 anti-fraud checks** | - |
| `validator` | Result validation | **[v2.5.6] Phase 0.5 methodology evaluation** | DATA, TRAINING, FINAL |
| `visualizer` | Generate figures | **[v2.5.6] Image naming standards** | - |
| `writer` | Write papers | (inherited v2.5.4) | PAPER |
| `summarizer` | Create summary | - | - |
| `editor` | Polish documents | (inherited v2.5.4) | - |
| `advisor` | Quality assessment | **[v2.5.6] Phase 0.5 methodology evaluation** | MODEL, PAPER, FINAL |
| `time_validator` | Time validation, anti-lazy, anti-fraud | **[v2.5.6] Enhanced Phase 5.5 checks** | Called after MODEL, CODE, TRAINING |

> **Total**: 14 agents (same as v2.5.5, with enhanced responsibilities)

---

## Phase Overview (Updated v2.5.6)

| Phase | Name | Main Agent | Validation Gate | v2.5.6 Changes |
|-------|------|-----------|-----------------|----------------|
| **0** | Problem Understanding | reader, researcher | - | (inherited) |
| **0.5** | **Model Methodology Quality Gate** | **@advisor, @validator** | **✅ METHODOLOGY** | **[v2.5.6 NEW]** |
| 1 | Model Design | modeler | ✅ MODEL (5 agents) | **[v2.5.6] Feedback path fixed** |
| 1.5 | Time Estimate Validation | @time_validator | ✅ TIME_CHECK | (inherited v2.5.5) |
| 2 | Feasibility Check | feasibility_checker | - | - |
| 3 | Data Processing | data_engineer | ✅ DATA | - |
| 4 | Code Translation | code_translator | ✅ CODE (2 agents) | (inherited v2.5.5) |
| 4.5 | Implementation Fidelity | @time_validator | ✅ FIDELITY | (inherited v2.5.5) |
| 5 | Model Training | model_trainer | ✅ TRAINING (2 agents) | (inherited v2.5.5) |
| **5.5** | **Data Authenticity Gate** | **@time_validator** | **✅ ANTI_FRAUD** | **[v2.5.6] Enhanced** |
| 6 | Visualization | visualizer | - | **[v2.5.6] Image naming** |
| 6.5 | Visual Quality Gate | visualizer, Director | ✅ VISUAL | (inherited v2.5.4) |
| 7 | Paper Writing | writer | ✅ PAPER (4 agents) | - |
| 7.5 | LaTeX Compilation Gate | writer, Director | ✅ LATEX | (inherited v2.5.4) |
| 8 | Summary | summarizer | ✅ SUMMARY (2 agents) | - |
| 9 | Polish | editor | ✅ FINAL (3 agents) | - |
| 9.5 | Editor Feedback Enforcement | Director, multiple agents | ✅ EDITOR | (inherited v2.5.4) |
| 10 | Final Review | advisor | - | - |

> **[v2.5.6 NEW]** Phase 0.5 evaluates model methodology quality before implementation
> **[v2.5.6 ENHANCED]** Phase 5.5 now includes comprehensive anti-fraud checks

---

## v2.5.6 Directory Structure Contract

```
output/
├── VERSION_MANIFEST.json        # Version control metadata
│
├── docs/                        # ALL documentation goes here (MANDATORY)
│   ├── consultations/           # Inter-agent consultation feedback
│   │   ├── feedback_model_1_researcher.md
│   │   ├── feedback_model_1_feasibility_checker.md
│   │   ├── feedback_model_1_data_engineer.md
│   │   ├── feedback_model_1_code_translator.md
│   │   ├── feedback_model_1_advisor.md
│   │   └── methodology_evaluation_1.md  # Phase 0.5 evaluation
│   ├── rewind/                  # Rewind recommendation reports
│   └── validation/              # Validation reports
│       ├── time_validator_{i}.md
│       ├── time_validator_code_{i}.md
│       └── time_validator_data_{i}.md
│
├── model/                       # Model design
│   ├── research_notes.md
│   ├── model_proposals/         # Draft proposals for consultation
│   │   ├── model_1_draft.md
│   │   ├── model_2_draft.md
│   │   └── model_3_draft.md
│   ├── model_design.md          # Final model design (after consultation)
│   └── feasibility_{i}.md
│
├── implementation/              # Implementation-related
│   ├── .venv/                   # Python virtual environment
│   ├── data/                    # Data files
│   │   ├── features_{i}.pkl
│   │   ├── features_{i}.csv
│   │   └── results_{i}.csv
│   ├── code/                    # Code
│   │   ├── model_{i}.py
│   │   └── test_{i}.py
│   └── logs/                    # Run logs
│       └── training_{i}.log
│
└── figures/                     # Figures (v2.5.6 standardized naming)
    ├── model_1_scatter_predictions.png
    ├── model_1_histogram_residuals.png
    ├── model_2_bar_feature_importance.png
    └── ...
```

> **[v2.5.6 CRITICAL]** All consultation feedback MUST go to `output/docs/consultations/` with naming `feedback_model_{X}_{agent}.md`

---

## New v2.5.6 Phases

### Phase 0.5: Model Methodology Quality Gate (NEW)

**Purpose**: Evaluate the quality of @researcher's proposed methods BEFORE @modeler starts implementation

**Trigger**: After @researcher completes `research_notes.md`, before @modeler writes draft proposal

**Participants**: @advisor, @validator

**Tasks**:
1. Read `output/research_notes.md`
2. Evaluate each proposed method:
   - Sophistication level (basic / moderate / advanced)
   - Computational intensity (expected training time)
   - O-Prize competitiveness (weak / moderate / strong)
3. Assign grade (1-10) for each method
4. Provide feedback on weak methods

**Decision Criteria**:
- **Average grade >= 9/10**: ✅ PROCEED to Phase 1 (@modeler starts design)
- **Average grade 7-8/10**: ⚠️ ADVISE @researcher to enhance methods (optional)
- **Average grade < 7/10**: ❌ REWIND to Phase 0.5 (@researcher MUST brainstorm better methods)

**Output**: `output/docs/validation/methodology_evaluation_{i}.md`

**Integration**:
```
Phase 0: @reader, @researcher complete
  ↓
Phase 0.5: @advisor + @validator evaluate methodology quality
  ↓
If grade < 7/10:
  Rewind to Phase 0.5 → @researcher provides better methods
  ↓
If grade >= 9/10:
  Proceed to Phase 1: @modeler starts design
```

See `04_phase_0.5_model_quality_gate.md` for full specification.

### Phase 5.5: Enhanced Data Authenticity Gate (ENHANCED)

**Purpose**: Comprehensive anti-fraud verification after training

**Trigger**: After @model_trainer completes training and @modeler + @validator validate

**Participants**: @time_validator (primary), @director (review)

**Enhanced Checks** (beyond v2.5.5):

1. **Training Skip Detection** (NEW):
   - Verify training log contains actual iteration progress
   - Check if epochs/iterations were actually executed
   - Look for "faked" logs (copied output without real training)

2. **Training Duration Verification** (ENHANCED):
   - Calculate expected duration based on method complexity
   - Compare to actual training duration
   - Flag if training was suspiciously fast (< 30% of expected)

3. **Result Authenticity** (ENHANCED):
   - Verify results match model type (Bayesian should have uncertainty, not point estimates)
   - Check if convergence criteria were actually met
   - Validate intermediate results (checkpoints if available)

4. **Code-Result Consistency** (ENHANCED):
   - Spot-check: Run code on subset, compare to CSV
   - Verify randomness (if random seed set, results should be reproducible)

**Decision Criteria**:
- **All checks pass**: ✅ AUTHENTIC → Proceed to Phase 6
- **1-2 checks fail**: ⚠️ SUSPICIOUS → Investigate, may request re-run
- **3+ checks fail**: ❌ FABRICATED → Re-run with verification

**Output**: `output/docs/validation/time_validator_data_{i}.md`

See `03_phase_5.5_anti_fraud.md` for full specification.

---

## v2.5.6 Feedback File Standardization

### Problem Summary

In v2.5.5, feedback files had these issues:
1. No canonical path (some used `output/consultations/`, others `output/docs/consultations/`)
2. No enforced naming convention
3. Agents might not write feedback files at all
4. @modeler reads from multiple paths, but files might not exist

### v2.5.6 Solution

**Canonical Path** (MANDATORY):
```
output/docs/consultations/
```

**Naming Convention** (MANDATORY):
```
feedback_model_{model_number}_{agent_name}.md
```

**Examples**:
- `feedback_model_1_researcher.md`
- `feedback_model_1_feasibility_checker.md`
- `feedback_model_1_data_engineer.md`
- `feedback_model_1_code_translator.md`
- `feedback_model_1_advisor.md`

**Protocol** (see `02_feedback_file_standardization.md`):
1. @modeler writes draft to `output/model_proposals/model_X_draft.md`
2. @director sends draft to 5 agents in PARALLEL
3. Each agent MUST write feedback to `output/docs/consultations/feedback_model_X_{agent}.md`
4. @director verifies all 5 files exist
5. @director confirms to @modeler: "All 5 feedback files received"
6. @modeler reads all 5 feedback files
7. @modeler writes final design to `output/model_design.md`

**Verification**:
```bash
# @director runs this to confirm all feedback files exist
ls -1 output/docs/consultations/feedback_model_1_*.md | wc -l
# Expected: 5
```

---

## v2.5.6 Image Naming Standards

### Problem Summary

In v2.5.5:
- Command `ls output/figures/*..png` uses wrong wildcard (`*..png` instead of `*.png`)
- No standardized naming for images
- Difficult to track which model created which figure

### v2.5.6 Solution

**Naming Convention** (MANDATORY):
```
{model_number}_{figure_type}_{description}.png
```

**Examples**:
- `model_1_scatter_predictions_vs_actual.png`
- `model_1_histogram_residuals.png`
- `model_2_bar_feature_importance.png`
- `model_3_line_convergence.png`

**Figure Types**:
- `scatter` - Scatter plots
- `line` - Line plots
- `bar` - Bar charts
- `histogram` - Histograms
- `heatmap` - Heatmaps
- `boxplot` - Box plots
- `violin` - Violin plots
- `diagram` - Flowcharts/diagrams

**Verification Command** (FIXED):
```bash
# Count images (v2.5.6 - CORRECTED)
ls -1 output/figures/*.png | wc -l

# Verify image quality (v2.5.6 - CORRECTED)
python3 -c "
from PIL import Image
import os
for f in os.listdir('output/figures'):
    if f.endswith('.png'):
        img = Image.open(os.path.join('output/figures', f))
        img.verify()
        print(f'{f}: {img.size} - OK')
"
```

See `05_image_naming_standards.md` for full specification.

---

## Inherited v2.5.5 Components

All v2.5.5 enhancements are fully inherited in v2.5.6:

### v2.5.5 Enhancements (Still Active)
1. **Strict Re-verification Standards** - 3+ sentences, specific evidence required
2. **All Agents Re-verify** - ALL relevant agents re-verify, not just rejecters
3. **Reader Mandatory Requirements** - Selective requirements are MANDATORY
4. **Modeler Time Pressure Protocol** - Must consult @director before simplifying
5. **Director Systematic Role** - Master checklist, priority hierarchy, decision matrices
6. **@time_validator Agent** - Time validation, lazy detection, anti-fraud

---

## Key Improvements Summary (v2.5.5 → v2.5.6)

| Issue | v2.5.5 | v2.5.6 | Impact |
|-------|--------|--------|--------|
| Feedback files not found | No systematic standard | Canonical path + naming enforced | Agent collaboration works |
| Training fraud possible | Basic timestamp checks | Comprehensive anti-fraud | Detect fake training |
| Weak models not caught early | Only caught in Phase 10 | Phase 0.5 quality gate | Saves time, better models |
| Image naming errors | Wrong wildcard pattern | Fixed + standards | Verification works |

---

## Testing Checklist (v2.5.6)

Before deploying v2.5.6, verify:

- [ ] Feedback file standardization protocol documented
- [ ] Phase 0.5 methodology quality gate specified
- [ ] Phase 5.5 enhanced anti-fraud checks specified
- [ ] Image naming standards documented
- [ ] All agent prompts updated with correct feedback file paths
- [ ] @modeler reads feedback from `output/docs/consultations/`
- [ ] All consulted agents write to `output/docs/consultations/`
- [ ] @director verifies all 5 feedback files exist
- [ ] Image verification commands use correct wildcards
- [ ] Workspace synchronized with architecture

---

**Document Version**: v2.5.6
**Last Updated**: 2026-01-18
**Status**: Complete

**For detailed specifications**, see:
- **01_SUMMARY.md** - Complete v2.5.6 summary
- **02_feedback_file_standardization.md** - Feedback file naming and positioning
- **03_phase_5.5_anti_fraud.md** - Enhanced anti-fraud checks
- **04_phase_0.5_model_quality_gate.md** - Methodology quality gate
- **05_image_naming_standards.md** - Image naming standards
