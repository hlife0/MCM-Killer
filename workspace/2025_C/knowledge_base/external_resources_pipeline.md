# External Resources Pipeline

> **Version**: 3.2.1
> **Purpose**: Complete documentation for external resource and past work handling

---

## Overview

External resources are **SUPPLEMENTARY**. Internal knowledge (HMML 2.0) takes priority.

The pipeline enables users to provide external papers, code, and data that can enhance the modeling process without disrupting the core workflow.

**NEW in v3.2.1**: Past Work Pipeline with higher priority (75/100 pre-approved).

---

## Agents

| Agent | Role | Phase | Trigger |
|-------|------|-------|---------|
| `@resource_ingestor` | Monitor inbox/ (both pipelines), process uploads | 0.1 | Files in inbox/ |
| `@quality_checker` | Validate quality, syntax check, pre-approve past_work | 0.1 | Files in staging/ |
| `@knowledge_curator` | Index, tag, maintain summary_for_agents.md (both) | On-demand | After quality check |
| `@resource_manager` | Folder structure, lifecycle, hash verification (both) | Background | Continuous |

---

## Folder Structure

### External Resources

```
external_resources/       # GITIGNORED
├── inbox/                       # User drops files here
│   └── (raw uploads)
├── staging/                     # Awaiting quality check
│   └── (processed, pending approval)
├── active/                      # Approved for use
│   ├── papers/                  # Academic papers
│   ├── code/                    # Code snippets/modules
│   ├── data/                    # External datasets
│   └── summary_for_agents.md   # Context overlay (READ THIS)
├── rejected/                    # Failed quality check
│   └── (with rejection reasons)
├── archived/                    # Historical resources
└── index.json                   # Master index (with SHA-256 hashes)
```

### Past Work (HIGHER PRIORITY)

```
past_work/                # GITIGNORED
├── inbox/                       # User drops past work files here
│   └── (previous submissions, verified code)
├── staging/                     # Brief processing (auto-approved)
│   └── (processed, syntax check pending for code)
├── active/                      # Ready for use (HIGH PRIORITY)
│   └── summary_for_agents.md   # Context overlay (READ FIRST)
├── rejected/                    # Only syntax failures (code)
│   └── (with rejection reasons)
├── archived/                    # Historical
└── index.json                   # Master index (with SHA-256 hashes)
```

---

## Workflow

### Step 1: User Upload
User drops files in `external_resources/inbox/`

Supported formats:
- Documents: `.pdf`, `.md`, `.txt`, `.docx`
- Code: `.py`, `.m`, `.cpp`, `.r`, `.jl`
- Data: `.csv`, `.json`, `.xlsx`

### Step 2: Ingestion (@resource_ingestor)
- Monitors inbox/ for new files
- Extracts metadata (title, author, date, type)
- Converts to standardized format if needed
- Moves to staging/ with metadata JSON

### Step 3: Quality Check (@quality_checker)
- Evaluates against quality criteria (see below)
- Code files: Runs syntax check
- Outputs: Quality score + justification
- Routes to active/ or rejected/

### Step 4: Curation (@knowledge_curator)
- Adds to index.json with SHA-256 hash
- Tags by relevance (agents, phases, topics)
- Updates summary_for_agents.md

### Step 5: Context Injection
ALL agents read BOTH summary files before starting their tasks:
1. `past_work/active/summary_for_agents.md` (READ FIRST - higher priority)
2. `external_resources/active/summary_for_agents.md`

---

## Past Work Pipeline (HIGHER PRIORITY)

> [!IMPORTANT] **Past work resources are PRE-APPROVED with 75/100 score.**
> They have HIGHER PRIORITY than external resources and should be consulted FIRST.

### Overview

Past work resources are **pre-approved references** from previous competitions or verified implementations. They receive:
- **Score**: 75/100 (equivalent to 7.5/10) - pre-set, not calculated
- **Status**: PRE_APPROVED - bypasses quality scoring
- **Syntax Check**: Still required for code files (hard constraint)
- **Priority**: Listed FIRST in summary_for_agents.md

### Resource ID Format

| Source | Prefix | Example |
|--------|--------|---------|
| External Resources | `MAN_` | `MAN_20260201_abc123` |
| Past Work | `PWK_` | `PWK_20260201_def456` |

### Processing Differences

| Step | External Resources | Past Work |
|------|-------------------|-----------|
| Inbox Monitoring | `external_resources/inbox/` | `past_work/inbox/` |
| Metadata Generation | Same | Same + `pre_approved: true` |
| Quality Scoring | Full 4-criterion scoring | **SKIP** (pre-set 75/100) |
| Syntax Check (code) | Required | Required |
| Score Threshold | >= 7.0 to pass | **Always 75/100** |
| Priority | Standard | **HIGH** (listed first) |

### When to Use Past Work

- Previous MCM competition submissions
- Tested and verified model implementations
- Reference code that has been run successfully
- Documents with known accuracy
- Approaches that have been validated

### Integration with summary_for_agents.md

Past work appears in a priority section at the TOP:

```markdown
# Past Work Resources Summary for Agents

> [!IMPORTANT] **Past work resources have HIGHER PRIORITY than external resources.**
> These are pre-approved references with score 75/100.

## PRIORITY RESOURCES: Past Work (Pre-Approved 75/100)

These resources are pre-approved and should be consulted FIRST:

1. **PWK_001** - previous_sir_model.py (CODE)
   - Pre-approved reference implementation
   - Path: `past_work/active/PWK_001/content.py`
   - Recommended for: @modeler, @code_translator

2. **PWK_002** - last_year_approach.md (DOCUMENT)
   - Previous competition methodology
   - Path: `past_work/active/PWK_002/content.md`
   - Recommended for: @researcher, @writer

---

## External Resources (Standard Scoring)
...
```

### Priority Order

When agents consult resources, they should follow this priority:

1. **Past Work (PWK_*)** - 75/100 pre-approved, consult FIRST
2. **External Resources >= 8.0** - High quality
3. **External Resources >= 7.0** - Standard approved
4. **Conditional (5.0-6.9)** - Use with caution, verify claims

---

## Quality Scoring

### Document Scoring

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Credibility | 25% | Source reputation, peer review status |
| Relevance | 30% | Direct applicability to current problem |
| Quality | 25% | Writing quality, methodology rigor |
| Actionability | 20% | Can be directly used or implemented |

**Threshold**: >= 7.0 to pass

### Code Scoring

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Credibility | 15% | Source, author reputation |
| Relevance | 25% | Applicable to current models |
| Quality | 20% | Code quality, documentation |
| **Actionability** | **40%** | Runnable, modifiable |

**Threshold**: >= 7.0 AND syntax pass

### Syntax Verification

| Language | Verification Method |
|----------|---------------------|
| Python | `ast.parse()` |
| MATLAB | Pattern-based check |
| R | `parse()` equivalent |
| C++ | Compiler syntax check |

**Syntax failure = AUTO-REJECT** (regardless of other scores)

---

## Context Injection: summary_for_agents.md

This file provides:

### 1. Quick Reference by Agent
```markdown
## For @modeler
- paper_gravity_model.pdf (score: 8.5) - Novel gravity model formulation
- code_gwr_implementation.py (score: 9.0) - Ready-to-use GWR code

## For @data_engineer
- paper_missing_data.pdf (score: 7.8) - Imputation strategies
```

### 2. Resources by Phase
```markdown
## Phase 1 (Model Design)
- [paper1.pdf] Relevant sections: 2.1, 3.4
- [code1.py] Can adapt: lines 45-89

## Phase 4 (Code Translation)
- [code2.py] Direct use with modification
```

### 3. High-Value Resources (score >= 8.0)
```markdown
## Priority Resources
1. gravity_model_extensions.pdf (9.2) - Must read for @modeler
2. tensor_decomposition.py (8.8) - Implement for temporal analysis
```

### 4. Usage Recommendations
```markdown
## How to Use
- Papers: Extract methodology, NOT data
- Code: Adapt, cite, verify
- Data: Secondary validation only (internal data primary)
```

---

## Protocol 21: External Resource Data Consistency

Added to validation phases. Ensures integrity of external resources.

### Checks Performed

1. **SHA-256 Hash Verification**
   - Compare current hash to index.json recorded hash
   - Detect file tampering or corruption
   - Fail if mismatch

2. **Citation Accuracy**
   - Data in paper matches cited source
   - Numbers are not misquoted
   - Context is preserved

3. **Citation Completeness**
   - All used resources are cited
   - No uncited code/data usage
   - Bibliography includes all references

### Verification Command

```bash
python docs/newplan/10_tools/indexer.py verify
```

### Output
```
Verification Results:
- Files checked: 12
- Hash matches: 12/12
- Citations verified: 8/8
- Status: PASS
```

---

## Phase 0.1: External Resource Processing

### Timeline

| Phase | Name | Agent | Time |
|-------|------|-------|------|
| 0 | Problem Understanding | reader, researcher | 30m |
| **0.1** | **External Resource Processing** | **resource_ingestor, quality_checker** | **10-30m** |
| 0.2 | Knowledge Retrieval | knowledge_librarian | 10-15m |

**Note**: Phase 0.1 runs **in parallel** with Phase 0.2. Non-blocking.

### Workflow
1. Check inbox/ for files
2. If files exist: Process through pipeline
3. If no files: Skip (log "No external resources")
4. Update summary_for_agents.md
5. Continue to Phase 0.5 (waits for both 0.1 and 0.2)

---

## Agent Specifications

Full agent specs available at:
- `.claude/agents/resource_ingestor.md`
- `.claude/agents/quality_checker.md`
- `.claude/agents/knowledge_curator.md`
- `.claude/agents/resource_manager.md`

---

## Integration Points

### Before Each Phase
```bash
# Agent startup - READ BOTH SUMMARIES
cat past_work/active/summary_for_agents.md         # READ FIRST (higher priority)
cat external_resources/active/summary_for_agents.md
# Check for relevant resources for this phase
```

### After Phase Completion
```bash
# Verify no new resources added during phase (both pipelines)
python docs/newplan/10_tools/indexer.py verify --all
```

### In Paper Writing (Phase 7+)
- Cite all used external resources and past work
- Include in references
- Note: External = supplementary, Past Work = reference implementation
- Past work has higher credibility (pre-approved)

---

## Summary Comparison

| Aspect | External Resources | Past Work |
|--------|-------------------|-----------|
| Location | `external_resources/inbox/` | `past_work/inbox/` |
| ID Prefix | `MAN_` | `PWK_` |
| Quality Score | Calculated (0-10 scale, threshold 7.0) | Pre-set 75/100 |
| Quality Check | Full 4-criterion scoring | SKIP (pre-approved) |
| Syntax Check | Required for code | Required for code |
| Priority | Standard | **HIGH** (listed first) |
| Use Case | New resources to evaluate | Verified references |
| Summary File | `external_resources/active/summary_for_agents.md` | `past_work/active/summary_for_agents.md` |
| Read Order | Second | **First** |
