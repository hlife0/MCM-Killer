# External Resources Pipeline

> **Version**: 3.2.0
> **Purpose**: Complete documentation for external resource handling

---

## Overview

External resources are **SUPPLEMENTARY**. Internal knowledge (HMML 2.0) takes priority.

The pipeline enables users to provide external papers, code, and data that can enhance the modeling process without disrupting the core workflow.

---

## Agents

| Agent | Role | Phase | Trigger |
|-------|------|-------|---------|
| `@resource_ingestor` | Monitor inbox/, process manual uploads | 0.1 | Files in inbox/ |
| `@quality_checker` | Validate quality, syntax check code | 0.1 | Files in staging/ |
| `@knowledge_curator` | Index, tag, maintain summary_for_agents.md | On-demand | After quality check |
| `@resource_manager` | Folder structure, lifecycle, hash verification | Background | Continuous |

---

## Folder Structure

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
ALL agents read `external_resources/active/summary_for_agents.md` before starting their tasks.

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
# Agent startup
cat external_resources/active/summary_for_agents.md
# Check for relevant resources for this phase
```

### After Phase Completion
```bash
# Verify no new resources added during phase
python docs/newplan/10_tools/indexer.py verify
```

### In Paper Writing (Phase 7+)
- Cite all used external resources
- Include in references
- Note: External = supplementary, not primary
