# External Resources Pipeline: Architecture Overview

> **Version**: 3.2.0
> **Last Updated**: 2026-01-31

---

## Executive Summary

The External Resources Pipeline extends MCM-Killer with manual resource management capabilities. It introduces:

1. **4 New Agents** for processing, validating, curating, and managing external resources
2. **New Phase 0.1** for parallel resource processing
3. **Quality Gateway** with **syntax checking for code** and weighted scoring
4. **Passive Consultation** via `summary_for_agents.md` (context injection)
5. **Enhanced Validation** with Protocol 21 for data consistency (**SHA-256 hash verification**)

**Key Design Decisions**:
- Resources are provided **manually** (dropped in inbox/) not auto-fetched
- External resources folder is **gitignored** - hashes ensure integrity
- Code files get **40% actionability weight** and **syntax validation**
- Agents read `summary_for_agents.md` for **passive context** (no active queries)

---

## Architecture Diagram

```
                                    ┌─────────────────────────────────────┐
                                    │         USER MANUAL DROPS           │
                                    │   .py, .m, .cpp, .md, .csv files    │
                                    └───────────────┬─────────────────────┘
                                                    │
                                                    ▼
                                             ┌─────────────┐
                                             │   inbox/    │
                                             │ (drop zone) │
                                             └──────┬──────┘
                                                    │
┌───────────────────────────────────────────────────────────────────────────┐
│                            Phase 0.1 (Parallel)                            │
│  ┌────────────────────┐                        ┌──────────────────────┐   │
│  │ @resource_ingestor │──── process ───────────│      staging/        │   │
│  │  - Auto metadata   │                        │  (temp storage)      │   │
│  │  - SHA-256 hash    │                        │  + metadata.json     │   │
│  └────────────────────┘                        └──────────┬───────────┘   │
│                                                           │               │
│                                                           ▼               │
│                                                ┌──────────────────────┐   │
│                                                │  @quality_checker    │   │
│                                                │  Score >= 7.0?       │   │
│                                                │  CODE: Syntax check  │   │
│                                                │  CODE: 40% action wt │   │
│                                                └──────────┬───────────┘   │
│                                                           │               │
│                             ┌──────────────┬──────────────┼──────────────┐
│                             │              │              │              │
│                             ▼              ▼              ▼              │
│                        rejected/      conditional     active/           │
│                        (< 5.0)        (5.0-6.9)      (>= 7.0)           │
│                        + syntax fail  + warnings     + indexed          │
└───────────────────────────────────────────────────────────────────────────┘
                                                            │
                                                            ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                         Resource Management Layer                          │
│  ┌───────────────────┐                          ┌───────────────────────┐ │
│  │ @knowledge_curator│                          │   @resource_manager   │ │
│  │  - Index/Tag      │                          │   - Lifecycle mgmt    │ │
│  │  - Maintain:      │                          │   - Cleanup           │ │
│  │    summary_for_   │                          │   - Statistics        │ │
│  │    agents.md      │                          │   - Hash verification │ │
│  └─────────┬─────────┘                          └───────────────────────┘ │
└────────────┼──────────────────────────────────────────────────────────────┘
             │
             ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                 Context Injection Layer (Passive Consultation)             │
│                                                                            │
│                    active/summary_for_agents.md                            │
│                    ┌─────────────────────────────┐                         │
│                    │ - Quick Reference by Agent  │                         │
│                    │ - Resources by Phase        │                         │
│                    │ - High-Value Resources      │                         │
│                    │ - Usage Recommendations     │                         │
│                    └──────────────┬──────────────┘                         │
│                                   │                                        │
│        ┌──────────────────────────┼──────────────────────────┐            │
│        ▼              ▼           ▼            ▼             ▼            │
│   @advisor      @modeler    @data_eng    @code_tr      @writer           │
│   (reads)       (reads)     (reads)      (reads)       (reads)           │
│                                                                            │
│   All agents read summary_for_agents.md before starting tasks             │
└───────────────────────────────────────────────────────────────────────────┘
             │
             ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                         Validation Layer                                   │
│                                                                            │
│   Protocol 21: External Resource Data Consistency                          │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │  @validator checks:                                                  │ │
│   │  - SHA-256 hash verification (file integrity)                       │ │
│   │  - Citation accuracy (quoted data matches source)                   │ │
│   │  - Citation completeness (all resources cited)                      │ │
│   │  - Methodology alignment (methods described correctly)              │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## Component Summary

### New Agents

| Agent | Purpose | Tools | Invocation |
|-------|---------|-------|------------|
| `resource_ingestor` | Monitor inbox, process manual uploads, generate metadata | Read, Write, Bash, Glob | Phase 0.1 |
| `quality_checker` | Validate quality, **syntax check code**, weighted scoring | Read, Write, Bash, Glob | Phase 0.1 (after processing) |
| `knowledge_curator` | Index, tag, **maintain summary_for_agents.md** | Read, Write, Bash, Glob | On-demand |
| `resource_manager` | Folder structure, lifecycle, **hash verification** | Read, Write, Bash, Glob | Background |

### Folder Structure

```
output/external_resources/       # GITIGNORED
├── inbox/            # Drop zone for manual file uploads
├── staging/          # Temporary: awaiting quality check
├── active/           # Approved: ready for agent use
│   └── summary_for_agents.md  # Context overlay (read by all agents)
├── rejected/         # Failed: quality < 5.0 or syntax failure
├── archived/         # Historical: unused > 7 days
├── by_domain/        # Index shortcuts by domain
├── by_phase/         # Index shortcuts by phase
├── index.json        # Master index (with SHA-256 hashes)
├── config.json       # Pipeline configuration
└── statistics.json   # Usage analytics
```

### Quality Pipeline

```
User drops file → inbox/ → @resource_ingestor processes → staging/
→ @quality_checker validates → active/ (or rejected/)
→ @knowledge_curator updates summary_for_agents.md
→ Agents read context overlay
```

**Standard Scoring (Documents)**:
- Source Credibility: 25%
- Content Relevance: 30%
- Content Quality: 25%
- Actionability: 20%

**Code Scoring (.py, .m, .cpp)**:
- Source Credibility: 15%
- Content Relevance: 25%
- Content Quality: 20%
- **Actionability: 40%** (syntax check required)

**Thresholds**:
- APPROVED: >= 7.0/10
- CONDITIONAL: 5.0-6.9/10
- REJECTED: < 5.0/10 **or syntax failure**

### Context Injection (Passive Consultation)

Instead of active agent-to-agent queries:

```
@knowledge_curator maintains → active/summary_for_agents.md
                              (updated when resources change)
                                        ↓
All agents read this file before starting their tasks
(mandated by CLAUDE.md)
                                        ↓
Agent decides whether external resources are useful
(resources are SUPPLEMENTARY)
```

### Validation Integration

**Protocol 21** adds to existing validation:
- **SHA-256 hash verification** (file integrity in gitignored folder)
- Citation accuracy (quoted data matches source)
- Citation completeness (all used resources cited)
- Methodology alignment (correct attribution)

---

## Phase Integration

| Existing Phase | Integration Point |
|----------------|-------------------|
| 0 (Problem Understanding) | Trigger initial resource search |
| **0.1 (NEW - parallel)** | Fetch and quality-check resources |
| 0.2 (Knowledge Retrieval) | Include external resources in suggestions |
| 0.5 (Methodology Gate) | Reference external resources in review |
| 1 (Model Design) | Consult external for formulations |
| 3 (Data Processing) | Consult external datasets |
| 4 (Code Translation) | Consult external implementations |
| 7 (Paper Writing) | Cite external resources |
| 9 (Polish) | Validate citations (Protocol 21) |

---

## Key Principles

1. **Non-Blocking**: Phase 0.1 runs in parallel - never blocks critical path
2. **Quality Gateway**: Only approved resources reach agents (code must pass syntax)
3. **Passive Consultation**: Agents read summary file, no active queries needed
4. **Manual Input**: Resources provided by user, not auto-fetched
5. **Data Integrity**: SHA-256 hashes verify file integrity (gitignored folder)
6. **Traceable**: All resources indexed with metadata and usage logs
7. **Consistent**: Protocol 21 ensures data accuracy in citations

---

## Related Documents

- `02_agents/` - Detailed agent specifications
- `03_folder_structure.md` - Folder design details
- `04_quality_pipeline.md` - Quality checking workflow
- `05_consultation_format.md` - Consultation templates
- `06_integration.md` - 22-phase workflow integration
- `07_validation_updates.md` - Validator changes
- `08_claude_md_updates.md` - CLAUDE.md additions
- `09_implementation_steps.md` - Step-by-step guide
- `10_tools/` - Python utility scripts
