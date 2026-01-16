# MCM-Killer v2.5.4 System Architecture

> **Authoritative Architecture Definition** — All Agent prompts should be derived from this document.
> **Version**: v2.5.4
> **Date**: 2026-01-16
> **Critical Fixes**: **[v2.5.4] 4 Critical Bug Fixes - LaTeX compilation gate, Multi-agent rework, Editor enforcement, Modeler anti-simplification**

---

## Document Relationships

| Document | Purpose |
|----------|---------|
| `retrospective.md` | Analysis of v2.4.2 and v2.5.0-v2.5.2 issues |
| `methodology.md` | Design principles and methodology |
| `phase_jump_design.md` | Phase jump mechanism detailed design |
| **`architecture.md` (this document)** | Defines architecture and Agent contracts |
| `agent_format_spec.md` | **[v2.5.3] Agent file format specification with YAML frontmatter** |
| `latex_compilation_gate.md` | **[v2.5.4 NEW] LaTeX compilation verification gate** |
| `multi_agent_rework_protocol.md` | **[v2.5.4 NEW] Enhanced multi-agent parallel rework** |
| `editor_feedback_enforcement.md` | **[v2.5.4 NEW] Editor feedback mandatory enforcement** |
| `modeler_anti_simplification.md` | **[v2.5.4 NEW] Modeler quality requirements** |

Reading order: retrospective → methodology → phase_jump_design → agent_format_spec → **latex_compilation_gate** → **multi_agent_rework_protocol** → **editor_feedback_enforcement** → **modeler_anti_simplification** → architecture

> **CRITICAL v2.5.4 FIXES**: 4 critical mechanisms added to prevent workflow breakdowns and quality issues.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.4.0 | 2026-01-02 | Validation gate mechanism, multi-agent collaboration |
| v2.4.1 | 2026-01-04 | Completeness mandate, data integrity standards |
| v2.4.2 | 2026-01-05 | Rework re-validation, resource utilization, quality gates |
| v2.5.0 | 2026-01-07 | Architecture layering, anti-lazy mechanisms, Phase 5 two-stage training |
| v2.5.1 | 2026-01-10 | Merged v2.4.2 and v2.5.0 improvements |
| v2.5.2 | 2026-01-14 | Adaptive Phase Jump, rewind recommendation, incremental fixes |
| v2.5.3 | 2026-01-15 | **[CRITICAL FIX] YAML frontmatter enforcement, agent loading fix** |
| **v2.5.4** | **2026-01-16** | **[CRITICAL FIXES] LaTeX gate, Multi-agent rework, Editor enforcement, Modeler quality** |

---

## v2.5.4 Critical Fixes

### Problem: 4 Critical Issues Discovered in v2.5.3 Operation

**Issue 1: LaTeX Compilation Deadlocks**
- **Symptom**: @writer generates non-compilable LaTeX, Director cannot detect, workflow deadlocks
- **Root Cause**: No LaTeX compilation verification gate after Phase 7
- **Solution**: Phase 7.5 LaTeX Compilation Gate (mandatory, see `latex_compilation_gate.md`)

**Issue 2: Editor Feedback Ignored**
- **Symptom**: @editor returns CRITICAL_ISSUES but no mandatory rework triggered
- **Root Cause**: No enforcement mechanism, no issue categorization by responsible agent
- **Solution**: Phase 9.5 Editor Feedback Enforcement (see `editor_feedback_enforcement.md`)

**Issue 3: Multi-Agent Rework Failures**
- **Symptom**: Multiple agents return NEEDS_REVISION, but Director only sends to one
- **Root Cause**: Auto-Reverification Protocol only handles single-agent rework
- **Solution**: Enhanced multi-agent parallel rework protocol (see `multi_agent_rework_protocol.md`)

**Issue 4: Modeler Oversimplification**
- **Symptom**: @modeler completes in 40min instead of 2-6h, models too lightweight
- **Root Cause**: No minimum complexity requirements, "degrade" principle abused
- **Solution**: Modeler anti-simplification requirements (see `modeler_anti_simplification.md`)

---

## v2.5.3 Critical Fix (Inherited)

### Problem: v2.5.0-v2.5.2 Agent Loading Failure

**Symptom**: Agents defined in architectures/v2-5-*/agents/ could not be called by Director.

**Root Cause**: Agent files were missing the required YAML frontmatter block that Claude Code needs to identify and load agents.

**Impact**:
- v2.5.0: Agents not recognized, system failed to load
- v2.5.1: Same issue as v2.5.0
- v2.5.2: Same issue as v2.5.0-v2.5.1

**Solution in v2.5.3**:
1. **Mandatory YAML frontmatter** for all agent files
2. **English language** for all agent content (was Chinese in v2.5.0-v2.5.2)
3. **Format specification document** (`agent_format_spec.md`) with examples
4. **Validation checklist** for agent file creation

### Agent File Format (CRITICAL)

Every agent file MUST follow this format:

```yaml
---
name: agent_name
description: Brief description of agent's purpose
tools: Tool1, Tool2, Tool3, ...
model: model_name
---
```

**Required Fields**:
- `name`: Unique identifier (lowercase, underscores allowed)
- `description`: One-line description of agent's role
- `tools`: Comma-separated list of available tools
- `model`: AI model to use (opus, sonnet, haiku)

**Example**:
```yaml
---
name: reader
description: Reads MCM problem PDFs using docling MCP and extracts ALL requirements into a structured checklist
tools: Write, Bash, Glob, LS, mcp__docling__convert_document_into_docling_document, mcp__docling__export_docling_document_to_markdown
model: opus
---
```

**After the frontmatter**, continue with the agent's detailed instructions in English.

---

## Table of Contents

1. [System Core Rules](#二system-core-rules)
2. [Version Management Contract](#三version-management-contract)
3. [Directory Structure Contract](#四directory-structure-contract)
4. [Collaboration Contracts](#五collaboration-contracts)
5. [Agent Contract Definitions](#六agent-contract-definitions)
6. [Execution Flow](#七execution-flow)
7. [Phase Jump Protocol (v2.5.2)](#八phase-jump-protocol-v252)

---

## 一、Document Description

This document is v2.5.3's **specific architecture definition**, fully inheriting all content from v2.5.2 with the critical v2.5.3 fix for agent loading.

**Inherited from v2.5.2**:
1. System core rules (single source of truth)
2. Each Agent's contract (input/output/triggers/responsibilities)
3. Directory structure contract
4. Naming conventions
5. Validation methods
6. Anti-lazy mechanisms (v2.5.0)
7. Phase 5 two-stage training (v2.5.0)
8. Token monitoring and checkpoints (v2.5.0)
9. Rework must revalidate (v2.4.2)
10. Resource utilization principles (v2.4.2)
11. Quality gate principles (v2.4.2)
12. Phase jump protocol (v2.5.2)
13. Rewind recommendation mechanism (v2.5.2)
14. Adaptive workflow (v2.5.2)

**New in v2.5.3**:
15. **[CRITICAL] Agent file format specification with YAML frontmatter**
16. **Agent loading fix documentation**
17. **English language requirement for agent content**

**Usage**: When creating or modifying Agent prompts, reference definitions in this document rather than inventing rules.

---

## 二、System Core Rules

### 2.1 Participants

| Role | Quantity | Description |
|------|----------|-------------|
| Director | 1 | **System Main Agent**, configured by CLAUDE.md, orchestrates other Agents |
| Agent | 13 | Specialized executors, each with specific responsibilities |

**Agent List** (standardized names):
1. `director` (orchestrator, not a regular agent)
2. `reader`
3. `researcher`
4. `modeler`
5. `feasibility_checker`
6. `data_engineer`
7. `code_translator`
8. `model_trainer`
9. `validator`
10. `visualizer`
11. `writer`
12. `summarizer`
13. `editor`
14. `advisor`

> **WARNING**: Must use standardized names above in all documents. No aliases (e.g., `Coder`).

### 2.2 Data Authority Hierarchy

```
Level 1: Code Output (CSV/PKL) — Highest authority, other files must match
Level 2: Agent Reports (MD)     — Must reflect Level 1 content
Level 3: Paper Documents (TEX)  — Must match Level 1, Level 1 prevails on conflict
```

### 2.3 File System Rules

**Absolutely Prohibited**:
- ❌ Modify any files outside `output/`
- ❌ Write to `reference_papers/`, `latex_template/`, `.claude/`
- ❌ Use suffixes like `_final`, `_backup`, `_old`

**Version Control**:
- ✅ All output files must have version numbers: `{name}_{i}.{ext}` (see Section 3)
- ✅ Update `VERSION_MANIFEST.json` after writing files

### 2.4 Data Integrity Standards (v2.4.1)

Given the severe data pollution in v2.4.0 experiments, v2.4.1 introduces strict data integrity standards:
- **Scalar Principle**: CSV/Excel outputs must contain ONLY scalar values (int, float, string, boolean). **Absolutely forbidden** to store serialized objects (List, Dict, Numpy Object).
- **Type Safety**: Code generating data must include `check_data_quality()` function to assert data types before output.
- **Self-Correction**: Data Engineer must run self-check before submission, immediately fix non-scalar columns.

### 2.5 Completeness Mandate (v2.4.1, Updated v2.5.0)

Given the "simplification" error in v2.4.0 and Phase 5 being completely skipped in v2.4.1, v2.5.0 establishes these absolute rules:

**Core Principles**:
- **No Skipping**: No Phase may be completely skipped (0% completion).
- **Degrade Don't Skip**: When resources are insufficient, must degrade to lightweight model, never skip entirely.
- **Quality > Efficiency**: When Token limits approach, **simplify description but not results**.

**Specific Requirements**:
- ✅ **Allowed**: Tier 2 lightweight model (reduce iterations/sampling)
- ✅ **Allowed**: Tier 3 minimal model (quick prototype algorithm)
- ❌ **Forbidden**: Skip Phase (e.g., "Skipped due to time constraints")
- ❌ **Forbidden**: Use TODO placeholders as output
- ❌ **Forbidden**: Generate only summary version reports

**Token Budget Management**:
1. Evaluate Token requirements before Phase starts
2. Switch to lower tier when insufficient detected mid-way
3. Simplify text descriptions, keep core code/data
4. Forbidden: Unilaterally decide to "skip non-critical steps"

### 2.6 Lightweight Model Grading Strategy (v2.5.0)

To completely eliminate Phase skipping behavior, v2.5.0 introduces a three-tier model system:

**Tier 1: Full Model** (standard)
- Standard parameter settings
- Full sampling/iterations
- Expected time: Depends on problem type (usually 4-8 hours)

**Tier 2: Lightweight Model** (fast)
- Reduce sampling to 50%
- Lower convergence standards
- Expected time: 1-2 hours
- Document degradation reason and impact in report

**Tier 3: Minimal Model** (prototype)
- Quick prototype algorithms (e.g., MAP estimation instead of HMC)
- Minimum necessary iterations
- Expected time: 10-30 minutes
- Must produce usable results (point estimates, simplified CI)
- Document limitations and impact in detail

**Decision Flow**:
```
Resource Assessment → Tier 1 (sufficient)
    ↓ Insufficient
Tier 2 (limited) → Record degradation
    ↓ Still insufficient
Tier 3 (urgent) → Document in detail
    ↓ Absolutely not
Skip Phase (FORBIDDEN)
```

**Scope**: Primarily for Model Trainer, other Agents may reference for resource-intensive tasks.

### 2.7 Rework Must Revalidate (v2.4.2)

Given the "rework skip validation" error in v2.4.1 experiments, v2.4.2 establishes these rules:

- **Mandatory Revalidation**: If Validation Gate returns REJECTED, rework completion **must** retrigger the same Gate
- **No Skipping**: Director has no reason to skip revalidation (including time urgency, Token shortage)
- **Loop Count**: Each Gate maximum 3 loops (REJECTED → rework → revalidation), after which pause for user intervention

> **This is v2.4.2's core improvement**. v2.4.1 experiment's main failure was skipping validation after rework.

### 2.8 Resource Utilization Principles (v2.4.2)

Agents should actively utilize resources provided by the project rather than working solely on their own knowledge.

#### 2.8.1 Reference Paper Resources

**Directory**: `./reference_papers/`

**Applicable Agents**:
- `researcher`: **Strongly encouraged** to browse reference papers, learn methodologies and best practices
- `modeler`: Reference similar problem modeling approaches
- `summarizer`: Learn summary writing style from high-quality MCM papers
- `writer`: Reference paper writing style and organization
- `advisor`: Compare quality against reference papers

**Principles**:
- ✅ Proactively read and cite reference materials
- ✅ Draw methodological inspiration
- ✅ Cite sources when using
- ❌ Do not directly copy content

#### 2.8.2 LaTeX Template Resources

**Directory**: `./latex_template/`

**Applicable Agents**: `writer`

**Mandatory Rules**:

1. **No Self-Created LaTeX Documents**:
   - Must **copy** template from `./latex_template/` to `output/paper/`
   - Work on the copied template
   - ❌ Forbidden to create new `.tex` files from scratch
   - ❌ Forbidden to modify template format structure (fonts, margins, section styles)

2. **Must Compile Successfully**:
   - Try compiling after each modification
   - If compilation fails due to content errors, fix yourself
   - If **environment issues** (missing fonts, missing packages):
     - **Must request `feasibility_checker` handling via Consultation protocol**
     - ❌ Forbidden to install packages or modify system environment yourself
     - ❌ Forbidden to use "no-font" workarounds or other bypasses
     - ❌ Forbidden to downgrade template requirements

3. **Document Length Requirements**:
   - **Minimum 23 pages** (excluding appendix)
   - Below 23 pages considered **unqualified**, must expand content
   - Validators should check page count, return REJECTED if insufficient

**Checklist** (writer self-check after completion):
- [ ] Template copied from `latex_template/`, not self-created
- [ ] Compiles successfully, no errors
- [ ] Page count >= 23 pages
- [ ] Format matches original template

#### 2.8.3 Web Search

**Applicable Agents**: `researcher`

**Encouraged Behaviors**:
- ✅ Search related academic papers and methods
- ✅ Find similar problem solutions
- ✅ Understand latest field developments
- ❌ Do not rely on unreliable sources

### 2.9 Quality Gate Principles (v2.4.2)

Agents should raise quality standards, strictly reject unqualified outputs.

#### 2.9.1 Modeler Strict Standards

`modeler` in CODE Validation Gate should:
- **Strictly review** whether code truly implements designed model
- **Reject** code that "runs but doesn't match design"
- **Reject** implementations that simplify core mathematical logic
- When finding serious deviations, clearly return REJECTED and explain

> Don't let quality issues pass because "code runs".

#### 2.9.2 Advisor Independent Verification (Outsider Perspective)

> **Core Principle**: You are an "outsider" not a "participant". You're not part of this team, you're here to review the team.

**Mindset Requirements**:

1. **All Other Agents Are Untrusted**:
   - Don't believe Director's summaries
   - Don't believe Validator's "passed" reports
   - Don't believe any Agent's claimed numbers
   - **Assume this competition team may have many ridiculous things**

2. **Review as Questioner**:
   - For each data point, ask "is this number correct?"
   - For each conclusion, ask "is this really true?"
   - **Don't be fooled by fancy reports** — reports may be well-written but data completely wrong

3. **Independent Verification**:
   - **Personally read** prediction files (`predictions_*.csv`), don't rely on anyone's report
   - **Personally check** whether paper numbers match files
   - **Personally search online** to verify predictions match reality
     - Example: Search "USA Olympics 2024 medal count", compare if predictions are reasonable
     - Example: Search "host country Olympic advantage", verify host effect direction

4. **Common Sense Sanity Check**:
   - Host country predictions should be higher than past years, not lower
   - Strong country predictions should be near historical range, not drop 80%+
   - Prediction interval upper bound shouldn't be less than mean

5. **Compare with Reference Papers**:
   - **Must read several papers from `reference_papers/`**
   - Compare project paper quality with reference papers
   - Ask yourself: can this paper sit with reference papers?
   - If gap too large, don't be optimistic, REJECT if needed

6. **Extremely Strict High Standards**:
   - **Don't be too optimistic about what you get** — assume problems inside
   - **Dare to demand rework** — find problems then REJECT, don't "good enough"
   - **High standards high requirements** — mediocre work doesn't deserve high scores
   - Better to be considered harsh than let garbage pass

**If Finding Problems**:
- Immediately lower score (more problems, lower score)
- Clearly list each discovered problem
- Don't let problems pass "for the team's sake"
- **Dare to return REJECTED** and demand fixes

> **Remember**: Your job is finding problems, not finding reasons to pass. An honest D is more valuable than a fake A+.

#### 2.9.3 Sanity Check Thinking

All Agents during validation should have Sanity Check thinking:
- **Common Sense Judgment**: Do prediction results match common sense? (e.g., host should perform better than usual)
- **Historical Comparison**: Reasonable compared to historical data?
- **Logical Consistency**: Is data consistent between different files?

### 2.10 Output Consistency Principles (v2.4.2)

Given the data inconsistency issues in v2.4.1 experiments, v2.4.2 reminds all Agents:

- **Unique Identifiers**: Countries, variables should use consistent identifier format (NOC code or full name, don't mix)
- **Avoid Overwrites**: Different models/tasks should use different filenames
- **Verify Log-File Consistency**: After training completes, check key numbers from logs match saved file content

---

## 三、Version Management Contract

### 3.1 Core Principles

1. **All output files must have version numbers**: `{name}_{i}.{ext}` (`{i}` starts from 1)
2. **VERSION_MANIFEST.json is the only version state record**
3. **Forbidden to use semantically ambiguous suffixes**: `_final`, `_backup`, `_old`, `_new`

### 3.2 Version Number Rules

| File Type | Naming Format | Example |
|-----------|---------------|---------|
| Markdown documents | `{name}_{i}.md` | `problem_requirements_1.md`, `model_design_2.md` |
| Python scripts | `{name}_{i}.py` | `model_1.py`, `data_prep_2.py` |
| Data files | `{name}_{i}.pkl/csv` | `features_1.pkl`, `results_3.csv` |
| Figures | `fig_{name}_{i}.png/pdf` | `fig_trend_1.png` |
| Papers | `paper_{i}.tex/pdf` | `paper_1.tex` |
| Agent reports | `{agent}_{i}.md` | `reader_1.md`, `modeler_2.md` |

**Special Cases**:
- `problem_full.md` - No version number (one-time generation)
- `figure_index.md` - No version number (continuously updated)
- `.venv/` - No version number (environment directory)

### 3.3 VERSION_MANIFEST.json

**Location**: `output/VERSION_MANIFEST.json`

**Structure**:
```json
{
  "created_at": "2026-01-04 00:00:00",
  "last_updated": "2026-01-04 01:30:00",

  "files": {
    "problem/problem_requirements": {
      "current": 2,
      "history": [
        {"version": 1, "created_at": "2026-01-04 00:10:00", "created_by": "reader"},
        {"version": 2, "created_at": "2026-01-04 00:45:00", "created_by": "reader"}
      ]
    },
    "model/model_design": {
      "current": 1,
      "history": [
        {"version": 1, "created_at": "2026-01-04 00:30:00", "created_by": "modeler"}
      ]
    },
    "implementation/data/features": {
      "current": 3,
      "history": [...]
    }
  },

  "agent_calls": {
    "reader": 2,
    "researcher": 1,
    "modeler": 1,
    "data_engineer": 3
  }
}
```

### 3.4 Agent Operation Norms

**Before writing file**:
1. Read `VERSION_MANIFEST.json`
2. Find current version number of that file
3. Version + 1 as new version number

**After writing file**:
1. Update `current` version in manifest for that file
2. Append new version record in `history` array
3. Update `last_updated` timestamp
4. Update call count in `agent_calls` for that Agent

**When reading file**:
1. Read `VERSION_MANIFEST.json`
2. Find current version number of that file
3. Read `{name}_{current}.{ext}`

**Forbidden**:
- ❌ Hardcode filenames directly (e.g., `features_1.pkl`)
- ❌ Overwrite existing version files
- ❌ Write files without updating manifest

### 3.5 Version Rollback

If needing to rollback to old version:
1. Modify manifest's `current` to target version number
2. **Don't** delete any version files
3. Add rollback record in `history`

---

## 四、Directory Structure Contract

```
output/
├── VERSION_MANIFEST.json        # Version control metadata
│
├── problem/                     # Problem-related
│   ├── original/                # Original problem files (copy)
│   │   ├── {year}_MCM_Problem_{letter}.pdf
│   │   └── {year}_Problem_{letter}_Data/
│   ├── problem_full.md          # Complete problem Markdown version (Reader from PDF)
│   └── problem_requirements_{i}.md  # Reader's requirement extraction
│
├── docs/                        # Documents (collaboration-related)
│   ├── consultation/            # Inter-agent consultation
│   │   └── {i}_{from}_{to}.md   # i = global consultation count
│   ├── validation/              # Validation reports
│   │   └── {i}_{stage}_{agent}.md  # i = global validation count
│   └── report/                  # Agent → Director reports
│       └── {agent_name}_{i}.md
│
├── model/                       # Model design
│   ├── research_notes_{i}.md    # Research notes
│   ├── model_design_{i}.md      # Mathematical model design
│   └── feasibility_{i}.md       # Feasibility analysis
│
├── implementation/              # Implementation-related
│   ├── .venv/                   # Python virtual environment (all Agents must use)
│   ├── data/                    # Data files
│   │   ├── raw/                 # Original data
│   │   ├── processed/           # Cleaned data
│   │   ├── features_{i}.pkl     # Feature data
│   │   └── results_{i}.csv      # Model output
│   ├── code/                    # Code
│   │   ├── data_prep_{i}.py
│   │   ├── model_{i}.py
│   │   └── test_{i}.py
│   ├── logs/                    # Run logs
│   │   └── training_{i}.log
│   └── analysis/                # Implementation Agent summaries
│       └── {agent_name}_summary_{i}.md
│
└── paper/                       # Paper-related (all LaTeX compilation related files)
    ├── paper_{i}.tex            # Paper source file
    ├── paper_{i}.pdf            # Paper PDF
    ├── figures/                 # Figures
    │   ├── fig_{name}_{i}.png
    │   ├── fig_{name}_{i}.pdf
    │   └── figure_index.md
    └── summary/                 # Summary
        ├── summary_sheet_{i}.tex
        └── summary_sheet_{i}.pdf
```

> **Note**: `{i}` indicates which version/which call of that file, starting from 1.

---

## 五、Collaboration Contracts

This section defines contracts for three collaboration mechanisms between Agents.

> **Note**: This section only defines "what", not "when to use". Specific call timings are defined in execution flow.

### 5.1 Core Principles

1. **Single-threaded execution**: Only one Agent works at a time
2. **All collaboration Blocking**: Initiate collaboration, process immediately, no async
3. **Director relay**: Agents don't communicate directly, coordinated through Director
4. **File records**: All collaboration written to `docs/` directory

### 5.2 Consultation

**Definition**: Agent requests information from other Agents during execution.

**Characteristics**:
- Bidirectional: A → B → A
- Blocking: Initiate then process immediately

**Initiator Guidelines**:

> **Encourage initiating consultation**: Any uncertain question should consult, don't guess.

- ✅ If uncertain, ask
- ✅ Explain your understanding, ask other to confirm or correct
- ❌ Forbidden to self-assume when uncertain
- ❌ Forbidden to fabricate information

**Responder Guidelines**:

> **Answer honestly**: Only answer what you know for sure, if don't know then say don't know.

- ✅ Answer what you know
- ✅ If unsure, clearly state, suggest initiating Agent consult other Agents
- ✅ Implementation-related Agents can run programs to verify
- ✅ Reader etc. can read files to get information
- ❌ **Forbidden to initiate third-party consultation when being consulted** (no nesting)
- ❌ Forbidden to fabricate unknown content

#### 5.2.1 Communication with Director

**Initiator** (concise, don't waste Director context):
```
Director, I need to consult @{agent}, file: docs/consultation/{i}_{from}_{to}.md
```

**Responder**:
```
Director, completed @{agent}'s consultation reply, file: docs/consultation/{i}_{from}_{to}.md
```

#### 5.2.2 File Contract

**Path**: `docs/consultation/{i}_{from}_{to}.md`

> `{i}` is **global consultation count** (not A→B count), from VERSION_MANIFEST.

```markdown
# Consultation #{i}: {from} → {to}

| Field | Value |
|-------|-------|
| Number | {i} |
| Initiator | {from} |
| Receiver | {to} |
| Time | {timestamp} |
| Status | PENDING / ANSWERED

---

## Question

{consultation content, initiator fills}

---

## Reply

{reply content, responder fills}

## Uncertainties

{responder's uncertain content, suggest initiator continue consulting other Agents}
```

### 5.3 Validation

**Definition**: Multi-perspective quality check on outputs.

**Characteristics**:
- **Multi-participant**: Each Stage validated by multiple Agents from different perspectives
- **Independent judgment**: Each validator only judges from own knowledge
- **No consultation**: Validation period forbids initiating Consultation
- **Parallel execution**: Director can call multiple validators in parallel

#### 5.3.1 Validator Perspectives

| Agent | Validation Perspective |
|-------|----------------------|
| reader | Requirement compliance, Sanity check |
| researcher | Methodology feasibility, literature support |
| modeler | Model design consistency |
| feasibility_checker | Technical/time feasibility |
| advisor | Innovation, quality assessment |
| code_translator | Code correctness |
| validator | Result rationality, fraud detection |

#### 5.3.2 Validation Results

| Result | Meaning |
|--------|---------|
| ✅ **APPROVED** | Passed |
| ⚠️ **CONDITIONAL** | Conditionally passed |
| ❌ **REJECTED** | Failed, needs fixing |

#### 5.3.3 Communication with Director

```
Director, completed {stage} validation, verdict: {result}, report: docs/validation/{i}_{stage}_{agent}.md
```

#### 5.3.4 File Contract

**Path**: `docs/validation/{i}_{stage}_{agent}.md`

> `{i}` is **global validation count**, from VERSION_MANIFEST.

```markdown
# Validation #{i}: {stage} by {agent}

| Field | Value |
|-------|-------|
| Number | {i} |
| Stage | {stage} |
| Validator | {agent} |
| Time | {timestamp} |
| Verdict | ✅ APPROVED / ⚠️ CONDITIONAL / ❌ REJECTED

---

## Validation Perspective

{which angle this Agent validates from}

---

## Check Results

| # | Check Item | Status | Note |
|---|-----------|--------|------|
| 1 | {item} | ✅/⚠️/❌ | {note} |

---

## Issue List (if any)

| # | Issue | Severity | Suggestion |
|---|-------|----------|------------|
| 1 | {issue} | HIGH/MEDIUM/LOW | {suggestion} |

---

## Conclusion

{validation conclusion}
```

### 5.4 Report

**Definition**: Agent reports to Director after call completion.

**Characteristics**:
- Unidirectional: Agent → Director
- Mandatory: Must report after each Agent call
- Private: Only Director visible
- Track call history: Record each Agent called how many times, did what

#### 5.4.1 Report Status

| Status | Meaning |
|--------|---------|
| ✅ **SUCCESS** | Task completed |
| ⚠️ **PARTIAL** | Partially completed, has leftovers |
| ❌ **FAILED** | Task failed |

#### 5.4.2 File Record

**Path**: `docs/report/{agent_name}_{i}.md`

```markdown
# Report: {agent_name} #{i}

| Field | Value |
|-------|-------|
| Agent | {agent_name} |
| Call Number | {i} |
| Start Time | {timestamp} |
| End Time | {timestamp} |
| Duration | {duration} |
| Status | ✅ SUCCESS / ⚠️ PARTIAL / ❌ FAILED

---

## Task Summary

{one-line description}

---

## Execution Content

1. {what was done}
2. {what was done}

---

## Outputs

| File | Path |
|------|------|
| {name} | {path} |

---

## Issues and Risks

{encountered problems, uncertainties}

---

## Next Steps

{suggest what Director should do next}
```

### 5.5 Problem Reporting

Agent encountering unsolvable problem must immediately report:

| Type | Format |
|------|--------|
| File missing | "Director, file {path} doesn't exist, cannot continue." |
| Tool failed | "Director, tool {tool} failed: {error}." |
| Data anomaly | "Director, data anomaly: {desc}." |
| Need confirmation | "Director, I'm unsure if should {action}, please confirm." |

**Forbidden**:
- ❌ Self-assume or fabricate
- ❌ Skip problem and continue
- ❌ Fail without reporting

---

## 六、Agent Contract Definitions

Each Agent's contract includes these attributes:

| Attribute | Description |
|-----------|-------------|
| Responsibility | Core task |
| Input | Files to read |
| Output | Files to produce |
| Write directories | Directories allowed to write |
| Participating Validations | Which Stages to validate as validator |

### 6.1 Agent Overview (Updated v2.5.4)

| Agent | Responsibility | Core Change (v2.4.2/v2.5.4) | Validation Participation |
|-------|---------------|---------------------|------------------------|
| reader | Read PDF, extract requirements | - | MODEL, DATA, ... |
| **researcher** | Method suggestions | **[v2.4.2] Encourage web search, browse `reference_papers/`** | MODEL |
| **modeler** | Design mathematical models | **[v2.5.4] Anti-simplification requirements, minimum quality standards** | DATA, CODE, ... |
| feasibility_checker | Feasibility check | - | MODEL, CODE |
| **data_engineer** | Data processing | Mandatory Schema validation; forbid non-scalar output | - |
| code_translator | Code translation | - | CODE, TRAINING |
| model_trainer | Model training | - | - |
| **validator** | Result validation | Must run automated pre-check; **Sanity Check thinking** | DATA, TRAINING, ... |
| visualizer | Generate figures | - | - |
| **writer** | Write papers | **[v2.4.2] Must use `latex_template/`**<br>**[v2.5.4] Must compile LaTeX before submission** | PAPER |
| **summarizer** | Create summary | **[v2.4.2] Reference `reference_papers/` for summary writing style** | - |
| **editor** | Polish documents | **[v2.5.4] Must categorize issues by responsible agent** | - |
| **advisor** | Quality assessment | **[v2.4.2] Must independently verify data files** | MODEL, PAPER, FINAL |

> **Director** responsibilities added:
> - **[v2.4.2]** Mandatory revalidation after rework; Token alert mechanism
> - **[v2.5.4]** Multi-agent parallel rework coordination; Phase 7.5/9.5 gate enforcement

### 6.2 Input Output Contracts

Detailed Agent contracts see individual Agent prompt files in `.claude/agents/`.

> **Agent prompts must match this document. Conflicts: this document prevails.**

---

## 七、Execution Flow

See `workflow_design.md` for details.

### 7.1 Phase Overview (Updated v2.5.4)

| Phase | Name | Main Agent | Validation Gate |
|-------|------|-----------|-----------------|
| 0 | Problem Understanding | reader, researcher | - |
| 1 | Model Design | modeler | ✅ MODEL |
| 2 | Feasibility Check | feasibility_checker | - |
| 3 | Data Processing | data_engineer | ✅ DATA |
| 4 | Code Translation | code_translator | ✅ CODE |
| 5 | Model Training | model_trainer | ✅ TRAINING |
| 6 | Visualization | visualizer | - |
| 7 | Paper Writing | writer | ✅ PAPER |
| **7.5** | **LaTeX Compilation Gate** | **writer, Director** | **✅ LATEX (MANDATORY)** |
| 8 | Summary | summarizer | ✅ SUMMARY |
| 9 | Polish | editor | ✅ FINAL |
| **9.5** | **Editor Feedback Enforcement** | **Director, multiple agents** | **✅ EDITOR (MANDATORY)** |
| 10 | Final Review | advisor | - |

> **[v2.5.4 NEW]** Phase 7.5 and 9.5 are **mandatory gates** that prevent workflow breakdowns.

### 7.2 Rework Mechanism

1. **Rework requires revalidation**: Reworked output must be revalidated at same standard
2. **Rework count**: Each Gate max 3 reworks
3. **Rewind mechanism**: Serious problems need rewind to earlier Phase

### 7.3 Completeness Checklist (v2.4.1)

Director must confirm at each Phase end:
1. [ ] All required files generated?
2. [ ] Complete Validation Gate executed (all validators)?
3. [ ] Any steps "simplified" or "skipped"? (If yes, serious violation, must rollback)

---

## 八、Phase Jump Protocol (v2.5.2)

### 8.1 Phase Dependency Graph

```
Phase 0 (Problem Understanding)
    ↓
Phase 1 (Model Design) ←── Rewind from 4,5,7
    ↓
Phase 2 (Feasibility Check)
    ↓
Phase 3 (Data Processing) ←── Rewind from 4,5,7
    ↓
Phase 4 (Code Translation) ←── Rewind from 5,7
    ↓
Phase 5 (Model Training)
    ↓
Phase 6 (Visualization)
    ↓
Phase 7 (Paper Writing)
    ↓
Phase 8 (Summary)
    ↓
Phase 9 (Polish)
    ↓
Phase 10 (Final Review)
```

### 8.2 Allowed Phase Transitions

| From | To | Condition | Example |
|------|-----|-----------|---------|
| Phase N | Phase N+1 | Normal completion | Always allowed |
| Phase N | Phase N-1, N-2, N-3 | Rewind recommended | Phase 5发现数据问题 → Rewind to Phase 3 |
| Phase N | Phase M | Complex rewind | Phase 7发现模型缺陷 → Rewind to Phase 1 |
| Validation Gate | Phase N-K | REJECTED with rewind | DATA Gate REJECT + rewind to Phase 1 |

### 8.3 Rewind Recommendation Mechanism

**Trigger**: Any Agent during execution discovers upstream problem

**Process**:
1. Agent writes `rewind_recommendation_{i}.md` documenting:
   - Current Phase
   - Problem discovered
   - Recommended rewind target Phase
   - Reason for rewind
   - Expected fixes
2. Director evaluates recommendation
3. If approved: rewind to target Phase, re-execute from there
4. If rejected: continue with rework in current Phase

**Format**:
```markdown
# Rewind Recommendation #{i}

| Field | Value |
|-------|-------|
| ID | {i} |
| Current Phase | {N} |
| Recommended Rewind To | {M} |
| Agent | {agent_name} |
| Time | {timestamp} |
| Status | PENDING / APPROVED / REJECTED |

---

## Problem Discovery

{describe what upstream problem was discovered}

---

## Recommended Rewind Target

**Target Phase**: {M}
**Reason**: {why Phase M needs to be redone}

---

## Expected Impact

{what will be fixed by rewinding}

---

## Alternative Approaches

{if not rewinding, what could be done instead}
```

### 8.4 Director's Jump Decision Logic

**Decision Flow**:
```
Agent reports problem or Validation REJECT
    ↓
Director analyzes problem source
    ↓
├── Local problem (current Phase)
│   └── Rework in current Phase
│
└── Upstream problem (earlier Phase)
    ├── Check Phase dependency graph
    ├── Evaluate rewind cost vs benefit
    └── Decision:
        ├── Rewind approved → Execute jump
        └── Rewind rejected → Local workaround
```

**Decision Criteria**:
| Factor | Rewind | No Rewind |
|--------|--------|-----------|
| Problem severity | CRITICAL/HIGH | MEDIUM/LOW |
| Root cause location | Upstream | Local |
| Fix complexity | Requires upstream change | Local fix possible |
| Time cost | Acceptable | Too expensive |
| Impact scope | Affects multiple downstreams | Limited |

---

## 九、How to Use This Document

### 9.1 Creating/Modifying Agent Prompts

1. Find definitions in this document
2. Ensure prompt matches this document
3. Don't repeat rules in prompt

### 9.2 Resolving Conflicts

- **This document is authoritative**
- When conflict found, modify prompt to match this document

### 9.3 Related Documents

| Document | Content | Location |
|----------|---------|----------|
| `agent_format_spec.md` | **[v2.5.3 NEW]** Agent file format specification with YAML frontmatter | Separate file |
| `retrospective.md` | v2.0-v2.3 problem analysis | Independent file |
| `methodology.md` | Design principles | Independent file |
| `architecture.md` | This document | **Core + Appendices** |
| `workflow_design` | Detailed execution flow | **Appendix A** |
| `validation_design` | Validation mechanism details | **Appendix B** |
| `phase_jump_design` | Phase jump mechanism details | **Appendix C** |

---

**Document Version**: v2.5.3
**Last Updated**: 2026-01-15
**Critical Changes**: YAML frontmatter enforcement, agent loading fix
