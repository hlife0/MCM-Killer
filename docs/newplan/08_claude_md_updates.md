# CLAUDE.md Updates

> **Version**: 3.2.0
> **Purpose**: Define additions to CLAUDE.md for external resources pipeline

---

## New Section to Add

Insert after the "22-Phase Workflow" section:

```markdown
---

## External Resources Pipeline (v3.2.0)

### Overview

The external resources pipeline processes manual file uploads, validates them, and integrates them into the workflow. External resources are SUPPLEMENTARY - they enhance but don't replace internal knowledge (HMML 2.0).

**Key Features**:
- Resources provided manually (dropped in `inbox/`)
- Folder is gitignored (SHA-256 hashes ensure integrity)
- Code files get 40% actionability weight + syntax validation
- Passive consultation via `summary_for_agents.md`

### New Agents

| Agent | Role | Phase |
|-------|------|-------|
| @resource_ingestor | Monitor inbox, process manual uploads | 0.1 (parallel) |
| @quality_checker | Validate quality, syntax check code | 0.1 (parallel) |
| @knowledge_curator | Index, tag, maintain summary_for_agents.md | All phases (on-demand) |
| @resource_manager | Folder structure, lifecycle, hash verification | All phases (background) |

### Folder Structure

```
output/external_resources/      # GITIGNORED
├── inbox/        # User drops files here
├── staging/      # Awaiting quality review
├── active/       # Approved for agent use
│   └── summary_for_agents.md  # Context overlay (READ THIS)
├── rejected/     # Failed quality check
├── archived/     # Historical, unused
├── index.json    # Master index (with SHA-256 hashes)
└── config.json   # Pipeline configuration
```

### Quality Gateway

All resources must pass quality review before reaching agents:

| Score | Verdict | Action |
|-------|---------|--------|
| >= 7.0 + syntax OK | APPROVED | Migrate to active/, available to agents |
| 5.0-6.9 + syntax OK | CONDITIONAL | Migrate with warnings |
| < 5.0 OR syntax FAIL | REJECTED | Move to rejected/, not available |

**Scoring Criteria (Documents)**:
- Source Credibility (25%)
- Content Relevance (30%)
- Content Quality (25%)
- Actionability (20%)

**Scoring Criteria (Code)**: Credibility 15%, Relevance 25%, Quality 20%, **Actionability 40%**

**Code Hard Constraint**: Syntax must pass (`ast.parse` for Python, `mlint` for MATLAB, `gcc -fsyntax-only` for C/C++).

### Context Injection (MANDATORY)

**All agents MUST read `output/external_resources/active/summary_for_agents.md` before starting their tasks.**

This replaces active agent-to-agent queries. The summary provides:
- Quick Reference by agent (which resources are relevant to you)
- Resources by phase
- High-value resources (score >= 8.0)
- Usage recommendations

### Integration Points

| Phase | Integration |
|-------|-------------|
| 0.1 (NEW) | Process manual uploads from inbox/ |
| 0.2 | Include external in method suggestions (read summary) |
| 0.5 | Reference external in methodology review |
| 1 | Read summary before model design |
| 3 | Check summary for external datasets |
| 4 | Check summary for code references |
| 7+ | Cite external resources, apply Protocol 21 |

### Protocol 21: External Resource Data Consistency

Applied during Phase 7+ validation:
- **SHA-256 hash verification** (file integrity)
- All citations must have valid resource in active/
- Quoted data must match source content
- Methodology attribution must be accurate

**Verify command**: `python docs/newplan/10_tools/indexer.py verify`

**Auto-Reject**:
- Missing resource references
- Data mismatch > 5%
- Methodology misattribution
- Hash verification failure

### Rules

1. External resources are OPTIONAL reference, not mandatory
2. HMML 2.0 internal methods take priority
3. Only APPROVED resources (score >= 7.0 + syntax OK for code) reach agents
4. All citations must be verifiable via Protocol 21
5. Phase 0.1 runs PARALLEL - never blocks critical path

### Phase 0.1 Timing

| Metric | Value |
|--------|-------|
| Minimum | 10 minutes |
| Expected | 10-30 minutes |
| Maximum | 45 minutes |
| Parallel with | Phase 0.2 |

---
```

---

## Phase Table Update

Update the existing 22-Phase Workflow table to include Phase 0.1:

```markdown
## 22-Phase Workflow (v3.2.0)

| Phase | Name | Agent | Gate | Time |
|-------|------|-------|------|------|
| 0 | Problem Understanding | reader, researcher | - | 30m |
| **0.1** | **External Resource Processing** | **resource_ingestor, quality_checker** | **-** | **10-30m (parallel)** |
| 0.2 | Knowledge Retrieval | knowledge_librarian | - | 10-15m |
| 0.5 | Methodology Gate | @advisor + @validator | ✅ METHODOLOGY | 15-20m |
| 1 | Model Design | modeler | - | 2-6h |
... (rest unchanged)
```

---

## Team Update

Update "Your Team" section:

```markdown
## Your Team (26 Members)

| Agent | Role | Notes |
|-------|------|-------|
| @reader | Problem Analyst | Selective reqs = MANDATORY |
| @researcher | Strategy Advisor | - |
| @knowledge_librarian | Method Curator | On-demand anytime |
| **@resource_ingestor** | **Manual Resource Processor** | **Phase 0.1** |
| **@quality_checker** | **Resource Quality Gate** | **Phase 0.1** |
| **@knowledge_curator** | **External Resource Librarian** | **On-demand** |
| **@resource_manager** | **Resource Infrastructure** | **Background** |
| @modeler | Math Architect | Consult before simplifying |
... (rest unchanged)
```

---

## Protocol Table Update

Update "Protocol Enforcement" section:

```markdown
## Protocol Enforcement (18 Protocols)

| # | Description | Point | Status |
|---|-------------|-------|--------|
| 1 | File Reading Ban (@director) | Phase 0.5 | ✅ |
... (existing protocols)
| 17 | Orchestration Log | ALL phases | ✅ |
| **21** | **External Resource Data Consistency** | **Phase 7+** | **✅** |
```

---

## CRITICAL RULES Addition

Add to existing CRITICAL RULES section:

```markdown
> [!CAUTION] **EXTERNAL RESOURCES CONTEXT**: ALL agents MUST read `output/external_resources/active/summary_for_agents.md` before starting their tasks. Resources are SUPPLEMENTARY.

> [!CAUTION] **PROTOCOL 21**: All external resource citations must be verified. Data from MAN_xxx sources must match content. SHA-256 hashes must verify. Auto-reject on mismatch.
```

---

## AUTOMATIC DECISION RULES Addition

Add to existing rules:

```markdown
| Rule | Trigger | Action |
|------|---------|--------|
| **6. External Resource Check** | Any agent starts | Read summary_for_agents.md, note relevant resources, continue |
| **7. No External Resources** | inbox/ empty at Phase 0.1 | Log and continue with HMML 2.0 only, acceptable |
```

---

## Phase Summaries Update

Add Phase 0.1 to phase summaries:

```markdown
| Phase | Purpose | Agent | Output | Gate |
|-------|---------|-------|--------|------|
| 0 | Extract requirements | @reader, @researcher | research_notes.md | → 0.1/0.2 |
| **0.1** | **Process manual resources** | **@resource_ingestor, @quality_checker** | **external_resources/active/**, **summary_for_agents.md** | **- (parallel)** |
| 0.2 | State-of-art methods | @knowledge_librarian | suggested_methods.md (≥3) | - |
... (rest unchanged)
```

---

## Director Master Checklist Update

Add Phase 0.1 handling:

```markdown
## Phase 0.1 Special Handling

Phase 0.1 is PARALLEL - special rules apply:

1. **After Phase 0**:
   - Check if user has dropped files in inbox/
   - Start Phase 0.1 AND Phase 0.2 simultaneously
   - Do NOT wait for 0.1 to complete

2. **During Phase 0.1/0.2**:
   - Both phases run concurrently
   - Phase 0.2 may complete first (expected)
   - Track both in orchestration log

3. **Before Phase 0.5**:
   - Check if Phase 0.1 completed
   - If yes: summary_for_agents.md has recommendations
   - If no: Proceed anyway, resources will become available later

4. **Phase 0.1 Time Gate**:
   - Minimum: 10 minutes
   - Maximum: 45 minutes (timeout if exceeds)
   - Does NOT count toward 8-hour minimum
```

---

## Quick Reference Update

Add to Quick Reference table:

```markdown
| Topic | Location |
|-------|----------|
| External Resources | docs/newplan/01_overview.md |
| External Agents | docs/newplan/02_agents/*.md |
| Quality Pipeline | docs/newplan/04_quality_pipeline.md |
| Protocol 21 | .claude/protocols/protocol_21_external_resource_consistency.md |
```
