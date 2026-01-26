# MCM-Killer v3.1.0 System Execution Plan

> **Purpose**: Step-by-step operational guide for executing the MCM-Killer v3.1.0 architecture during a competition.
> **Scope**: From pre-competition setup to final submission (Phases 0 to 11).
> **Prerequisites**: System installation complete (see `07_implementation_guide.md`), Python environment active.

---

## Execution Workflow Overview

This document defines the standard operating procedure (SOP) for transforming a raw problem PDF into an O-Prize winning submission. The workflow is divided into **12 Executable Steps**.

**Key**:
- 📂 **Input**: Required templates, data, or previous outputs.
- 🤖 **Agent**: The primary agent responsible.
- ⚙️ **Action**: The specific command or prompt to run.
- 📄 **Output**: The artifact produced.

---

## Step 1: Problem Intake & Requirement Extraction (Phase 0)

**Timing**: Hour 0-2.
**Goal**: Convert problem PDF into structured requirements and identifying domain keywords.

*   **Agents**: `@reader`, `@researcher`
*   **Input**:
    *   📂 `problem.pdf` (Download from competition site)
    *   📂 `templates/knowledge_base/problem_breakdown_template.md` (Implicit)
*   **Action**:
    1.  Invoke `@reader` to parse text and identify explicit constraints.
    2.  Invoke `@researcher` to infer implicit O-Prize requirements and extract keywords.
    3.  *(Optional)* Invoke `@knowledge_librarian` to generate `style_guide.md` from reference papers if missing.
*   **Output**:
    *   📄 `output/docs/requirements/problem_statement.md`
    *   📄 `output/docs/requirements/data_inventory.md`
*   **Verification**: Ensure "Explicit Requirements" and "Implicit Requirements" sections are populated.

---

## Step 2: Method Consultation & Selection (Phase 0.2)

**Timing**: Hour 2-3.
**Goal**: Select high-fidelity mathematical models from the Knowledge Library.

*   **Agents**: `@knowledge_librarian`, `@researcher`
*   **Input**:
    *   📂 `output/docs/requirements/problem_statement.md` (Keywords)
    *   📂 `knowledge_library/methods/index.md` (HMML 2.0)
*   **Action**:
    1.  `@researcher` queries `@knowledge_librarian` with domain keywords (e.g., "network", "epidemic").
    2.  `@knowledge_librarian` returns `suggested_methods.md` filtered by narrative value.
*   **Output**:
    *   📄 `output/docs/knowledge/suggested_methods.md` (List of candidates like SIR-Network, Agent-Based Model, etc.)
*   **Verification**: Ensure at least one "High Complexity" method is suggested for O-Prize potential.

---

## Step 3: Feasibility Validation (Phase 0.5)

**Timing**: Hour 3-5.
**Goal**: Validate that selected methods can be implemented within 96 hours.

*   **Agents**: `@feasibility_checker`, `@advisor`
*   **Input**:
    *   📂 `output/docs/knowledge/suggested_methods.md`
    *   📂 `output/docs/requirements/data_inventory.md`
*   **Action**:
    1.  `@feasibility_checker` estimates data size vs. complexity (Time/Space analysis).
    2.  `@advisor` approves primary and backup models.
*   **Output**:
    *   📄 `output/docs/reports/feasibility_report.md` (Green/Yellow/Red light for each model)
*   **Verification**: Must have one "GREEN" primary model before proceeding.

---

## Step 4: Mathematical Design & Formulation (Phase 1)

**Timing**: Hour 5-9.
**Goal**: Create rigorous LaTeX formulation of the chosen model.

*   **Agent**: `@modeler`
*   **Input**:
    *   📂 `output/docs/reports/feasibility_report.md` (Approved model)
    *   📂 `templates/knowledge_base/1_method_file_template.md` (Format reference)
*   **Action**:
    1.  `@modeler` writes the mathematical specification (equations, assumptions, parameters).
    2.  Define 4-part assumption justification (Statement, Justification, Validity, Limitation).
*   **Output**:
    *   📄 `output/model/model_{i}/design.md` (Full LaTeX spec)
*   **Verification**: Check for "Parameter Table" and "Assumption List".

---

## Step 5: Data Engineering & Pipeline (Phase 2-3)

**Timing**: Hour 10-14.
**Goal**: Prepare clean datasets for the model.

*   **Agent**: `@data_engineer`
*   **Input**:
    *   📂 `data/raw/*` (Original files)
    *   📂 `output/model/model_{i}/design.md` (Variable requirements)
*   **Action**:
    1.  Write cleaning scripts (handle missing values, normalization).
    2.  Generate train/test splits.
*   **Output**:
    *   📄 `output/implementation/data/processed/train.csv`
    *   📄 `output/implementation/data/processed/test.csv`
    *   📄 `output/implementation/data/data_profile.json`
*   **Verification**: Ensure no `NaN` values in processed data.

---

## Step 6: Code Translation & Implementation (Phase 4)

**Timing**: Hour 14-18.
**Goal**: Translate mathematical design into executable Python code.

*   **Agent**: `@code_translator`
*   **Input**:
    *   📂 `output/model/model_{i}/design.md` (The "spec")
    *   📂 `output/implementation/data/processed/*` (The data)
    *   📂 `templates/writing/3_dev_diary_entry.md` (For documentation)
*   **Action**:
    1.  Implement `model_{i}.py` and `train_{i}.py`.
    2.  **CRITICAL**: Document every error/bug in `dev_diary_{i}.md`.
*   **Output**:
    *   📄 `output/implementation/code/main_{i}.py`
    *   📄 `output/docs/insights/dev_diary_{i}.md` (Struggle log)
*   **Verification**: Code must run without syntax errors. `dev_diary` must have entries.

---

## Step 7: Model Training & Logging (Phase 5)

**Timing**: Hour 19-27.
**Goal**: Train the model and capture detailed execution logs.

*   **Agent**: `@model_trainer`
*   **Input**:
    *   📂 `output/implementation/code/main_{i}.py`
*   **Action**:
    1.  Execute training loop.
    2.  Save full logs to disk (do not truncate).
*   **Output**:
    *   📄 `output/implementation/models/model_{i}.pkl` (Trained artifact)
    *   📄 `output/implementation/logs/training_full.log` (Raw log)
    *   📄 `output/implementation/logs/training_history.csv` (Metrics)
*   **Verification**: Check `training_full.log` size (>0KB).

---

## Step 8: Insight Extraction (Phase 5.8)

**Timing**: Hour 27-29.
**Goal**: Transform "bugs" and "logs" into "scientific insights" (The O-Prize differentiator).

*   **Agent**: `@metacognition_agent`
*   **Input**:
    *   📂 `output/implementation/logs/training_full.log`
    *   📂 `output/docs/insights/dev_diary_{i}.md`
    *   📂 `tools/log_analyzer.py`
    *   📂 `templates/narrative_arcs/*.md`
*   **Action**:
    1.  Run `tools/log_analyzer.py` to find anomalies (oscillations, divergences).
    2.  Correlate anomalies with `dev_diary` notes.
    3.  Generate a Narrative Arc (e.g., "Iterative Refinement").
*   **Output**:
    *   📄 `output/docs/insights/narrative_arc_{i}.md`
*   **Verification**: Insight must explain *why* a failure occurred using domain physics.

---

## Step 9: Dual-Mode Visualization (Phase 6)

**Timing**: Hour 28-32.
**Goal**: Generate publication-ready figures.

*   **Agent**: `@visualizer`
*   **Input**:
    *   📂 `output/implementation/logs/training_history.csv`
    *   📂 `output/model/model_{i}/design.md`
*   **Action**:
    1.  **Mode A**: Generate matplotlib/seaborn data plots (Results).
    2.  **Mode B**: Generate Mermaid diagrams (Methodology/Flow).
*   **Output**:
    *   📄 `output/figures/results_plot.png`
    *   📄 `output/figures/methodology_flow.png`
*   **Verification**: All figures must have captions following Protocol 15 (Observation-Implication).

---

## Step 10: Paper Drafting (Phase 7)

**Timing**: Hour 32-40.
**Goal**: Write the full LaTeX paper.

*   **Agents**: `@narrative_weaver`, `@writer`
*   **Input**:
    *   📂 `output/docs/insights/narrative_arc_{i}.md` (The story)
    *   📂 `output/model/model_{i}/design.md` (The math)
    *   📂 `output/figures/*` (The visuals)
    *   📂 `knowledge_library/academic_writing/style_guide.md` (The style)
    *   📂 `templates/writing/latex_formatting_standards.md`
*   **Action**:
    1.  `@narrative_weaver` compiles `paper_outline.md`.
    2.  `@writer` generates `main.tex` content section by section.
*   **Output**:
    *   📄 `output/paper/main.tex`
    *   📄 `output/paper/paper.pdf`
*   **Verification**: Abstract must contain ≥3 quantitative metrics.

---

## Step 11: Adversarial Mock Judging (Phase 9.1)

**Timing**: Hour 40-41.
**Goal**: Simulating a ruthless judge review to catch fatal flaws.

*   **Agent**: `@judge_zero`
*   **Input**:
    *   📂 `output/paper/paper.pdf`
    *   📂 `templates/ANTI_PATTERNS.md` (Kill List)
    *   📂 `templates/writing/judgment_report_template.md`
*   **Action**:
    1.  Evaluate paper against 3 personas (Statistician, Skeptic, Editor).
    2.  Calculate score (0-100).
*   **Output**:
    *   📄 `output/docs/validation/judgment_report.md`
*   **Decision**:
    *   **PASS** (Score > 90): Proceed to Step 12.
    *   **REJECT** (Score < 90): Trigger **Protocol 13 (DEFCON 1)** → Loop back to Step 10 (Writer) or Step 8 (Insight).

---

## Step 12: Final Packaging & Submission (Phase 9.5 - 10)

**Timing**: Hour 41-42.
**Goal**: Create the submission archive.

*   **Agent**: `@director`, `@summarizer`
*   **Input**:
    *   📂 `output/paper/paper.pdf`
    *   📂 `output/implementation/code/*`
*   **Action**:
    1.  `@summarizer` creates 1-page `summary.pdf` (Memo).
    2.  `@director` zips everything into `submission.zip`.
*   **Output**:
    *   📦 `output/package/submission.zip`
*   **Verification**: Check zip file size and contents against competition rules.

---

## Directory Reference
All paths are relative to the root of the MCM-Killer workspace.
- **Templates**: `D:\migration\MCM-Killer\architectures\v3-1-0\templates\`
- **Agents**: `D:\migration\MCM-Killer\architectures\v3-1-0\agents\`
- **Tools**: `D:\migration\MCM-Killer\architectures\v3-1-0\tools\`
