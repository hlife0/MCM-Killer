# MCM-Killer v2.5.5 System Architecture

> **Authoritative Architecture Definition** — All Agent prompts should be derived from this document.
> **Version**: v2.5.5
> **Date**: 2026-01-17
> **Critical Enhancements**: **[v2.5.5] 6 Critical Enhancements + 1 New Agent - Strict re-verification, All agents re-verify, Mandatory selective requirements, Modeler consultation protocol, Systematic director, Time validation**

---

## Document Relationships

| Document | Purpose |
|----------|---------|
| **`architecture.md`** (this document) | **Defines architecture and Agent contracts** |
| **`SUMMARY.md`** | **[v2.5.5] Complete summary of all v2.5.5 changes** |
| `agent_format_spec.md` | Agent file format specification with YAML frontmatter |
| **`re_verification_strict_standards.md`** | **[v2.5.5 NEW] Strict re-verification approval standards** |
| **`all_agents_reverify_protocol.md`** | **[v2.5.5 NEW] All agents (not just rejecters) must re-verify** |
| **`reader_mandatory_requirements.md`** | **[v2.5.5 NEW] Selective requirements are MANDATORY** |
| **`modeler_time_pressure_protocol.md`** | **[v2.5.5 NEW] Modeler must consult @director before simplifying** |
| **`director_systematic_role.md`** | **[v2.5.5 NEW] Director's systematic protocols and priority hierarchy** |
| **`time_validator_spec.md`** | **[v2.5.5 NEW] @time_validator agent specification** |
| `latex_compilation_gate.md` | LaTeX compilation verification gate (v2.5.4) |
| `multi_agent_rework_protocol.md` | Enhanced multi-agent parallel rework (v2.5.4) |
| `editor_feedback_enforcement.md` | Editor feedback mandatory enforcement (v2.5.4) |
| `modeler_anti_simplification.md` | Modeler quality requirements (v2.5.4) |

Reading order: **SUMMARY.md** → **re_verification_strict_standards** → **all_agents_reverify_protocol** → **reader_mandatory_requirements** → **modeler_time_pressure_protocol** → **director_systematic_role** → **time_validator_spec** → architecture

> **CRITICAL v2.5.5 ENHANCEMENTS**: 6 critical mechanisms + 1 new agent to prevent quality regression and ensure systematic decision-making.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.5.3 | 2026-01-15 | YAML frontmatter enforcement, agent loading fix |
| v2.5.4 | 2026-01-16 | 4 critical bug fixes (LaTeX, editor, multi-agent, modeler) |
| **v2.5.5** | **2026-01-17** | **6 enhancements + @time_validator agent** |

---

## v2.5.5 Critical Enhancements

### Problem: 6 Critical Issues Discovered in v2.5.4 Operation

**Issue 1: Re-verification Approval Too Easy**
- **Symptom**: Re-verification often passes on first attempt with minimal review ("looks good, approved")
- **Root Cause**: No strict standards for re-verification thoroughness
- **Solution**: **Strict Re-verification Standards** (see `re_verification_strict_standards.md`)
  - Minimum 3 sentences, specific evidence required
  - Director enforcement of detailed approvals
  - Lazy approvals rejected and queried

**Issue 2: Only Rejecting Agents Re-verify**
- **Symptom**: When 3 of 5 agents reject work, only those 3 re-verify. Agents who approved don't see revisions.
- **Root Cause**: Protocol only requires rejecters to re-verify
- **Impact**: Revisions may break what was previously approved
- **Solution**: **All Agents Re-verify Protocol** (see `all_agents_reverify_protocol.md`)
  - Re-verification set = ALL relevant agents (primary + secondary)
  - Secondary agents verify revisions don't break their approval
  - Only proceed when ALL agents approve

**Issue 3: Selective Requirements Ignored**
- **Symptom**: @reader treats "选择性/加分项/附加项" as optional, skips looking for data
- **Example**: "Coach Effect Attribution: Without explicit coaching data..." → @reader marks as optional, skips
- **Root Cause**: No mechanism to mark selective requirements as MANDATORY for quality
- **Solution**: **Reader Mandatory Requirements Protocol** (see `reader_mandatory_requirements.md`)
  - ALL requirements are MANDATORY for high-quality papers
  - Unclear data → MUST search reliable sources
  - Impossible → Document and flag for @advisor

**Issue 4: Modeler Unilateral Simplification**
- **Symptom**: @modeler estimates 2-6h, works 20min, then unilaterally "simplifies for time"
- **Root Cause**: @modeler abuses "degrade don't skip" principle, no consultation protocol
- **Solution**: **Modeler Time Pressure Protocol** (see `modeler_time_pressure_protocol.md`)
  - @modeler MUST consult @director before simplifying
  - @director calls @time_validator for analysis
  - Tier 2/3 degradation requires approval

**Issue 5: Director's Role Unclear in Gates**
- **Symptom**: Phase X.5 Gates don't clearly define @director's tasks, decision logic, exit conditions
- **Root Cause**: Gate definitions focus on agent responsibilities, not @director's role
- **Solution**: **Director Systematic Role** (see `director_systematic_role.md`)
  - Master checklist for every phase
  - Priority hierarchy (1=Data Integrity, ..., 6=Polish)
  - Decision matrices for all gates
  - Clear entry/exit conditions

**Issue 6: Time Estimation Fraud & Lazy Implementation**
- **Symptom**: @modeler estimates 2-6h, @code_translator implements simplified version (runs in 20min), @validator checks "does it work" (yes), no one notices 90% complexity reduction
- **Root Cause**: No one validates time estimates match implementation
- **Solution**: **NEW @time_validator Agent** (see `time_validator_spec.md`)
  - Validates @modeler's time estimates (algorithmic analysis)
  - Detects @code_translator lazy implementation (compare design vs code)
  - Prevents data fabrication (timestamps, file sizes, statistical checks)

---

## Agent System (v2.5.5)

### Agent Overview (Updated v2.5.5)

| Agent | Responsibility | v2.5.5 Changes | Validation Participation |
|-------|---------------|----------------|------------------------|
| `reader` | Read PDF, extract requirements | **[v2.5.5] Selective requirements = MANDATORY** | MODEL, DATA, PAPER |
| `researcher` | Method suggestions | - | MODEL |
| `modeler` | Design mathematical models | **[v2.5.5] Consult @director before simplifying** | DATA, CODE, TRAINING |
| `feasibility_checker` | Feasibility check | - | MODEL, CODE |
| `data_engineer` | Data processing | - | - |
| `code_translator` | Code translation | **[v2.5.5] @time_validator watches for lazy work** | CODE, TRAINING |
| `model_trainer` | Model training | - | - |
| `validator` | Result validation | - | DATA, TRAINING, FINAL |
| `visualizer` | Generate figures | - | - |
| `writer` | Write papers | [v2.5.4] Must compile LaTeX before submission | PAPER |
| `summarizer` | Create summary | - | - |
| `editor` | Polish documents | [v2.5.4] Must categorize issues by agent | - |
| `advisor` | Quality assessment | - | MODEL, PAPER, FINAL |
| **`time_validator`** | **Time validation, anti-lazy, anti-fraud** | **[v2.5.5 NEW] Specialized validation agent** | **Called after MODEL, CODE, TRAINING** |

> **Total**: 14 agents (13 from v2.5.4 + 1 new in v2.5.5)

### Agent File Format (CRITICAL - Inherited from v2.5.3)

Every agent file MUST begin with:

```yaml
---
name: agent_name
description: Brief description of agent's purpose
tools: Tool1, Tool2, Tool3, ...
model: opus
---
```

**Required Fields**:
- `name`: Unique identifier (lowercase, underscores allowed)
- `description`: One-line description of agent's role
- `tools`: Comma-separated list of available tools
- `model`: AI model to use (opus, sonnet, haiku)

**Example** (v2.5.5 new agent):
```yaml
---
name: time_validator
description: Validates time estimates, detects lazy implementation, prevents data fabrication
tools: Read, Glob, Bash, mcp__zread__search_doc, mcp__zread__read_file
model: opus
---
```

---

## v2.5.5 Re-verification Enhancements

### Enhancement 1: Strict Approval Standards

**Protocol**: See `re_verification_strict_standards.md`

**Key Changes**:
- **FORBIDDEN**: One-sentence approvals ("looks good, approved")
- **REQUIRED**: Detailed evidence-based approvals (3+ sentences, specific locations, evidence)

**Template**:
```markdown
## Re-verification Verdict: ✅ APPROVED

### Issues Raised (Original)
1. [Issue 1]
2. [Issue 2]

### Verification Process
**Issue 1**: Checked lines 45-67, found [specific evidence], RESOLVED
**Issue 2**: Checked Table 2, compared to CSV, values match, RESOLVED

### Regression Check
- [ ] No new issues introduced
- [ ] Previously working parts still work

### Conclusion
All issues resolved, no regressions. **APPROVED**.
```

**Director Enforcement**:
- If verdict < 300 characters → Query for details
- If no "checked:" or "evidence:" → Query for details
- If no specific locations → Query for details

### Enhancement 2: All Agents Re-verify

**Protocol**: See `all_agents_reverify_protocol.md`

**Key Changes**:
- **v2.5.4**: Only agents who rejected → re-verify
- **v2.5.5**: ALL relevant agents → re-verify
  - Primary agents: Those who rejected (made revisions)
  - Secondary agents: Those who approved (verify no regression)
  - Re-verification set: Primary ∪ Secondary

**Example**:
```
Original validation:
  @researcher:          APPROVED     → Secondary (re-verify)
  @feasibility_checker: NEEDS_REVISION → Primary (re-verify own revisions)
  @data_engineer:       APPROVED     → Secondary (re-verify)
  @code_translator:     APPROVED     → Secondary (re-verify)
  @advisor:             NEEDS_REVISION → Primary (re-verify own revisions)

Re-verification set: ALL 5 agents
```

**Rationale**: Agents who approved must verify revisions don't break what they approved.

---

## v2.5.5 Agent-Specific Enhancements

### @reader Enhancement: Mandatory Selective Requirements

**Protocol**: See `reader_mandatory_requirements.md`

**Key Changes**:
- **v2.5.4**: Treats "选择性/加分项/附加项" as optional
- **v2.5.5**: ALL requirements are MANDATORY for quality

**Classification**:
- **Category 1**: Explicit requirements (clearly stated tasks)
- **Category 2**: Contextual requirements (hinted, "we cannot X without Y")
- **Category 3**: Data requirements (find or flag, never skip)

**Output Format**:
```markdown
## Category 2: Contextual Requirements (MANDATORY for Quality)

2. [ ] Coach Effect Attribution Analysis
   - Source: Page 7, "Without explicit coaching data, we cannot..."
   - Interpretation: This is a HINT that analysis is important
   - Data needed: Coaching, funding, infrastructure data
   - Feasibility: ⚠️ NEEDS RESEARCH
   - Priority: 🔴 HIGH (judges will notice if missing)
   - Action: Request @researcher to search
```

**Data Missing Protocol**:
- If data unclear → **NEEDS RESEARCH** (not optional)
- Must search reliable sources via @researcher
- If impossible → Document and flag for @advisor
- Never mark as "skip"

### @modeler Enhancement: Consultation Before Simplifying

**Protocol**: See `modeler_time_pressure_protocol.md`

**Key Changes**:
- **v2.5.4**: @modeler can unilaterally degrade to Tier 2/3
- **v2.5.5**: @modeler MUST consult @director before degrading

**Protocol**:
```
@modeler feels time pressure
  ↓
STOP! Do NOT simplify unilaterally
  ↓
Create proposal (Options A, B, C, D)
  ↓
Consult @director
  ↓
@director calls @time_validator for analysis
  ↓
@director makes decision
  ↓
@modeler proceeds with approved option
  ↓
Documents approval in feasibility report
```

**Forbidden vs Allowed**:
- ❌ "Time running out, using simple method instead."
- ✅ "Time pressure detected. Creating proposal for @director. Waiting for decision."

**Tier System**:
- Tier 1: No approval needed (standard)
- Tier 2: @director approval required
- Tier 3: @director approval + @time_validator analysis required

### @time_validator Agent (NEW)

**Specification**: See `time_validator_spec.md`

**Responsibilities**:

1. **Time Estimate Validation** (Phase 1.5 - after MODEL gate)
   - Read model designs
   - Analyze algorithmic complexity
   - Estimate actual runtime
   - Compare to @modeler's estimates
   - Flag discrepancies > 2x

2. **Implementation Fidelity Check** (Phase 4.5 - after CODE gate)
   - Compare design vs code
   - Detect simplifications:
     - Algorithm changed (e.g., PyMC → sklearn)
     - Iterations reduced (e.g., 10000 → 1000)
     - Features missing
     - Ensemble size reduced
   - Flag unauthorized simplifications

3. **Data Authenticity Verification** (Phase 5.5 - after TRAINING)
   - Timestamp verification (CSV created after training?)
   - File size verification (not too small?)
   - Statistical sanity checks (reasonable ranges?)
   - Pattern detection (repeating values? too perfect?)
   - Flag suspicious or fabricated data

**Integration Points**:
```
MODEL validation complete → Call @time_validator (validate estimates)
CODE validation complete → Call @time_validator (check implementation)
TRAINING complete → Call @time_validator (verify data)
```

---

## v2.5.5 Director Enhancements

### Systematic Role Protocol

**Specification**: See `director_systematic_role.md`

**Key Components**:

1. **Master Checklist** (use at start of EVERY phase)
   - Step 1: Verify entry conditions
   - Step 2: Call agent
   - Step 3: Review output
   - Step 4: Execute validation gate
   - Step 5: Make decision (using matrix)
   - Step 6: Execute action
   - Step 7: Update manifest

2. **Priority Hierarchy** (for decisions)
   - Priority 1: Data Integrity (ABSOLUTE - never compromise)
   - Priority 2: Model Completeness (CRITICAL)
   - Priority 3: Code Correctness (CRITICAL)
   - Priority 4: Paper Quality (HIGH)
   - Priority 5: Efficiency (MEDIUM)
   - Priority 6: Polish (LOW)

   **Rule**: When multiple requirements conflict, follow priority. Never sacrifice higher for lower.

3. **Decision Matrices** (for all Phase X.5 Gates)
   - Entry criteria (what before entering)
   - @director's tasks (step-by-step)
   - Scoring system (weight × score)
   - Decision rules (score ranges → actions)
   - Exit conditions (what before proceeding)

**Example: Phase 7.5 LaTeX Compilation Gate**

```markdown
### Entry Criteria
- [ ] @writer reports "paper complete"
- [ ] paper_{i}.tex exists
- [ ] File > 10 KB

### Decision Matrix

| Criterion | Weight | Score (0-10) | Weighted Score |
|-----------|--------|-------------|----------------|
| PDF exists | 30% | 0/10 | 0/300 |
| No errors in log | 40% | 0/10 | 0/400 |
| Page count >= 23 | 30% | 0/10 | 0/300 |
| **Total** | **100%** | - | **0/1000** |

### Decision Rules

| Score | Action |
|-------|--------|
| 900-1000 | ✅ PROCEED to Phase 8 |
| 600-899 | ⚠️ RETURN to @writer |
| 300-599 | ⏸️ CONSULT @feasibility_checker |
| 0-299 | ⏪ REWIND to Phase 7 |

### Exit Conditions
- [ ] PDF exists and > 100 KB
- [ ] No errors in .log
- [ ] Page count >= 23
- [ ] All figures render correctly
```

---

## Inherited v2.5.4 Components

The following v2.5.4 components are fully inherited in v2.5.5:

### v2.5.4 Critical Fixes (Still Active)

1. **Phase 7.5: LaTeX Compilation Gate** (`latex_compilation_gate.md`)
   - @writer must compile before submission
   - 3 compilation attempts max
   - PDF verification required

2. **Phase 9.5: Editor Feedback Enforcement** (`editor_feedback_enforcement.md`)
   - @editor verdict triggers action
   - Multi-agent rework for CRITICAL_ISSUES
   - Re-verification loop until APPROVED

3. **Multi-Agent Parallel Rework** (`multi_agent_rework_protocol.md`)
   - Parallel rework for 2-3 agents
   - All agents re-verify (enhanced in v2.5.5)
   - Loop until all approve (max 3 iterations)

4. **Modeler Anti-Simplification** (`modeler_anti_simplification.md`)
   - Minimum work standards (2-6 hours, 50-120k tokens)
   - Required model components (6 mandatory)
   - Forbidden simplifications

### v2.5.3 Critical Fix (Still Active)

**YAML Frontmatter Requirement** (`agent_format_spec.md`)
- Every agent file MUST have YAML frontmatter
- English language for all agent content
- Format validation checklist

---

## Phase Overview (Updated v2.5.5)

| Phase | Name | Main Agent | Validation Gate | v2.5.5 Additions |
|-------|------|-----------|-----------------|-----------------|
| 0 | Problem Understanding | reader, researcher | - | @reader: Selective = MANDATORY |
| 1 | Model Design | modeler | ✅ MODEL (5 agents) | +@time_validator validates estimates |
| 2 | Feasibility Check | feasibility_checker | - | - |
| 3 | Data Processing | data_engineer | ✅ DATA | - |
| 4 | Code Translation | code_translator | ✅ CODE (2 agents) | +@time_validator checks implementation |
| 5 | Model Training | model_trainer | ✅ TRAINING (2 agents) | +@time_validator verifies data |
| 6 | Visualization | visualizer | - | - |
| 7 | Paper Writing | writer | ✅ PAPER (4 agents) | - |
| **7.5** | **LaTeX Compilation Gate** | **writer, Director** | **✅ LATEX (MANDATORY)** | **[v2.5.4] Inherited** |
| 8 | Summary | summarizer | ✅ SUMMARY (2 agents) | - |
| 9 | Polish | editor | ✅ FINAL (3 agents) | - |
| **9.5** | **Editor Feedback Enforcement** | **Director, multiple agents** | **✅ EDITOR (MANDATORY)** | **[v2.5.4] Inherited + [v2.5.5] All re-verify** |
| 10 | Final Review | advisor | - | - |

> **[v2.5.5 NEW]** @time_validator called after Phases 1, 4, 5

---

## Validation Gates (Updated v2.5.5)

### MODEL Gate (Phase 1.5)

**Participants**: @researcher, @feasibility_checker, @data_engineer, @code_translator, @advisor

**v2.5.5 Enhanced Protocol**:
1. 5 agents validate in parallel
2. Collect verdicts
3. **[NEW]** Call @time_validator to validate time estimates
4. If any NEEDS_REVISION → Parallel rework
5. **[NEW]** Re-verification with ALL 5 agents (not just rejecters)
6. **[NEW]** Strict approval standards (3+ sentences, evidence required)
7. If ALL approve → Proceed to Phase 2

### CODE Gate (Phase 4.5)

**Participants**: @modeler, @validator

**v2.5.5 Enhanced Protocol**:
1. 2 agents validate in parallel
2. Collect verdicts
3. **[NEW]** Call @time_validator to check implementation fidelity
4. If any NEEDS_REVISION → Rework
5. **[NEW]** Re-verification with both agents
6. **[NEW]** @time_validator flags unauthorized simplifications
7. If ALL approve → Proceed to Phase 5

### TRAINING Gate (Phase 5.5)

**Participants**: @modeler, @validator

**v2.5.5 Enhanced Protocol**:
1. 2 agents validate in parallel
2. Collect verdicts
3. **[NEW]** Call @time_validator to verify data authenticity
4. If @time_validator flags suspicious/fabricated → Re-run
5. If any NEEDS_REVISION → Rework
6. **[NEW]** Re-verification with both agents
7. If ALL approve → Proceed to Phase 6

---

## Directory Structure Contract (Inherited)

```
output/
├── VERSION_MANIFEST.json        # Version control metadata
│
├── problem/                     # Problem-related
│   ├── original/                # Original problem files
│   ├── problem_full.md          # Complete problem Markdown
│   └── problem_requirements_{i}.md  # Reader's requirement extraction
│
├── docs/                        # Documents
│   ├── consultation/            # Inter-agent consultation
│   ├── validation/              # Validation reports
│   └── report/                  # Agent → Director reports
│
├── model/                       # Model design
│   ├── research_notes_{i}.md
│   ├── model_design_{i}.md
│   └── feasibility_{i}.md
│
├── implementation/              # Implementation-related
│   ├── .venv/                   # Python virtual environment
│   ├── data/                    # Data files
│   ├── code/                    # Code
│   ├── logs/                    # Run logs
│   └── analysis/                # Implementation Agent summaries
│
└── paper/                       # Paper-related
    ├── paper_{i}.tex
    ├── paper_{i}.pdf
    ├── figures/
    └── summary/
```

> **[v2.5.5 NEW]** Task start: Auto-create docs/, implementation/, output/ folders

---

## Core Rules (Inherited)

### Data Authority Hierarchy
```
Level 1: Code Output (CSV/PKL) — Highest authority
Level 2: Agent Reports (MD)     — Must reflect Level 1
Level 3: Paper Documents (TEX)  — Must match Level 1
```

### File System Rules
- ❌ Modify files outside `output/`
- ❌ Write to `reference_papers/`, `latex_template/`, `.claude/`
- ❌ Use `_final`, `_backup`, `_old` suffixes

### Completeness Mandate
- **No Skipping**: No Phase may be completely skipped
- **Degrade Don't Skip**: Tier 2/3 with @director approval
- **Quality > Efficiency**: Simplify description, not results

---

## Version Management

All output files must have version numbers: `{name}_{i}.{ext}`

**VERSION_MANIFEST.json** tracks:
- Current version of each file
- Creation history
- Agent call counts

---

## Collaboration Contracts

### Consultation
- **Definition**: Agent requests information from other agents
- **Characteristics**: Bidirectional, blocking
- **File**: `docs/consultation/{i}_{from}_{to}.md`

### Validation
- **Definition**: Multi-perspective quality check
- **Participants**: Multiple agents from different perspectives
- **File**: `docs/validation/{i}_{stage}_{agent}.md`

### Report
- **Definition**: Agent reports to Director after call
- **Status**: SUCCESS / PARTIAL / FAILED
- **File**: `docs/report/{agent_name}_{i}.md`

---

## Testing Checklist (v2.5.5)

Before deploying v2.5.5, verify:

- [ ] @time_validator agent defined and configured
- [ ] Re-verification strict standards documented
- [ ] All agents re-verify protocol documented
- [ ] Reader mandatory requirements protocol added
- [ ] Modeler time pressure protocol added
- [ ] Director systematic protocols defined
- [ ] Master checklist created
- [ ] Priority hierarchy defined
- [ ] Decision matrix template created
- [ ] All Phase X.5 gates have decision matrices
- [ ] All agent prompts updated
- [ ] Workspace synchronized with architecture

---

## Key Improvements Summary (v2.5.4 → v2.5.5)

| Issue | v2.5.4 | v2.5.5 | Impact |
|-------|--------|--------|--------|
| Re-verification too easy | "Looks good" sufficient | 3+ sentences + evidence required | Higher quality |
| Only rejecters re-verify | Only those who rejected | ALL agents re-verify | Prevent regression |
| Selective requirements | Treated as optional | MANDATORY for quality | No missing reqs |
| Modeler simplifies | Unilateral decision | Must consult @director | No unauthorized degrade |
| Director unclear role | Patches scattered | Systematic protocols | Consistent decisions |
| Time estimation fraud | No validation | @time_validator checks | Detect lazy/fraud |

---

**Document Version**: v2.5.5
**Last Updated**: 2026-01-17
**Status**: Complete

**For detailed specifications**, see:
- **SUMMARY.md** - Complete v2.5.5 summary
- **re_verification_strict_standards.md** - Strict approval standards
- **all_agents_reverify_protocol.md** - All agents re-verify
- **reader_mandatory_requirements.md** - Selective = MANDATORY
- **modeler_time_pressure_protocol.md** - Consult before simplifying
- **director_systematic_role.md** - Systematic director protocols
- **time_validator_spec.md** - @time_validator agent spec
