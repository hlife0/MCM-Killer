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

The external resources pipeline fetches, validates, and integrates internet resources into the workflow. External resources are SUPPLEMENTARY - they enhance but don't replace internal knowledge (HMML 2.0).

### New Agents

| Agent | Role | Phase |
|-------|------|-------|
| @web_crawler | Fetch external resources from internet | 0.1 (parallel) |
| @quality_checker | Validate resource quality | 0.1 (parallel) |
| @knowledge_curator | Index and recommend resources | All phases (on-demand) |
| @resource_manager | Folder structure and lifecycle | All phases (background) |

### Folder Structure

```
output/external_resources/
├── staging/      # Awaiting quality review
├── active/       # Approved for agent use
├── rejected/     # Failed quality check
├── archived/     # Historical, unused
├── index.json    # Master searchable index
└── config.json   # Pipeline configuration
```

### Quality Gateway

All fetched resources must pass quality review before reaching agents:

| Score | Verdict | Action |
|-------|---------|--------|
| >= 7.0 | APPROVED | Migrate to active/, available to agents |
| 5.0-6.9 | CONDITIONAL | Migrate with warnings |
| < 5.0 | REJECTED | Move to rejected/, not available |

**Scoring Criteria**:
- Source Credibility (25%)
- Content Relevance (30%)
- Content Quality (25%)
- Actionability (20%)

### Integration Points

| Phase | Integration |
|-------|-------------|
| 0.1 (NEW) | Parallel resource gathering |
| 0.2 | Include external in method suggestions |
| 0.5 | Reference external in methodology review |
| 1 | Consult external for formulations |
| 3 | Query external datasets |
| 4 | Reference external implementations |
| 7+ | Cite external resources, apply Protocol 21 |

### Consultation Protocol

**To request external resources**:
```
Director, I need external resource consultation.
**Query**: {specific question}
**Urgency**: HIGH/MEDIUM/LOW
```

**Response from @knowledge_curator**:
- Matching resources with relevance scores
- Access paths and recommended sections
- Usage guidance

### Protocol 21: External Resource Data Consistency

Applied during Phase 7+ validation:
- All citations must have valid resource in active/
- Quoted data must match source content
- Methodology attribution must be accurate

**Auto-Reject**:
- Missing resource references
- Data mismatch > 5%
- Methodology misattribution

### Rules

1. External resources are OPTIONAL reference, not mandatory
2. HMML 2.0 internal methods take priority
3. Only APPROVED resources (score >= 7.0) reach agents
4. All citations must be verifiable via Protocol 21
5. Phase 0.1 runs PARALLEL - never blocks critical path

### Phase 0.1 Timing

| Metric | Value |
|--------|-------|
| Minimum | 15 minutes |
| Expected | 15-30 minutes |
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
| **0.1** | **External Resource Gathering** | **web_crawler, quality_checker** | **-** | **15-30m (parallel)** |
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
| **@web_crawler** | **External Resource Collector** | **Phase 0.1** |
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
## Protocol Enforcement (21 Protocols)

| # | Description | Point | Status |
|---|-------------|-------|--------|
| 1 | File Reading Ban (@director) | Phase 0.5 | ✅ |
... (existing protocols)
| 20 | Orchestration Log | ALL phases | ✅ |
| **21** | **External Resource Data Consistency** | **Phase 7+** | **✅** |
```

---

## CRITICAL RULES Addition

Add to existing CRITICAL RULES section:

```markdown
> [!CAUTION] **EXTERNAL RESOURCES**: Phase 0.1 runs PARALLEL with Phase 0.2. Never wait for external resources to proceed. They are SUPPLEMENTARY, not blocking.

> [!CAUTION] **PROTOCOL 21**: All external resource citations must be verified. Data from WEB_xxx sources must match content.md. Auto-reject on mismatch.
```

---

## AUTOMATIC DECISION RULES Addition

Add to existing rules:

```markdown
| Rule | Trigger | Action |
|------|---------|--------|
| **6. External Resource Query** | Agent needs external reference | Route to @knowledge_curator, return matches, continue |
| **7. No External Resources** | Phase 0.1 produces nothing | Log and continue with HMML 2.0 only, acceptable |
```

---

## Phase Summaries Update

Add Phase 0.1 to phase summaries:

```markdown
| Phase | Purpose | Agent | Output | Gate |
|-------|---------|-------|--------|------|
| 0 | Extract requirements | @reader, @researcher | research_notes.md | → 0.1/0.2 |
| **0.1** | **Fetch external resources** | **@web_crawler, @quality_checker** | **external_resources/active/** | **- (parallel)** |
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
   - Extract problem keywords
   - Start Phase 0.1 AND Phase 0.2 simultaneously
   - Do NOT wait for 0.1 to complete

2. **During Phase 0.1/0.2**:
   - Both phases run concurrently
   - Phase 0.2 may complete first (expected)
   - Track both in orchestration log

3. **Before Phase 0.5**:
   - Check if Phase 0.1 completed
   - If yes: @knowledge_curator has recommendations
   - If no: Proceed anyway, resources will become available later

4. **Phase 0.1 Time Gate**:
   - Minimum: 15 minutes
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

---

## Full Updated CLAUDE.md Section

The complete new section to insert:

```markdown
---

## External Resources Pipeline (v3.2.0)

### Overview
Fetches, validates, and integrates internet resources. SUPPLEMENTARY to HMML 2.0.

### New Agents
| Agent | Role |
|-------|------|
| @web_crawler | Fetch from internet |
| @quality_checker | Quality gateway |
| @knowledge_curator | Index and recommend |
| @resource_manager | Infrastructure |

### Folder
```
output/external_resources/
├── staging/   # Awaiting review
├── active/    # Approved (>= 7.0)
├── rejected/  # Failed (< 5.0)
└── index.json # Master index
```

### Quality Thresholds
- APPROVED: >= 7.0/10
- CONDITIONAL: 5.0-6.9/10
- REJECTED: < 5.0/10

### Consultation
```
Director, I need external resource consultation.
**Query**: {question}
**Urgency**: HIGH/MEDIUM/LOW
```

### Protocol 21 (Phase 7+)
- Citations verified against active/
- Data matches source
- Auto-reject on mismatch

### Rules
1. SUPPLEMENTARY, not blocking
2. Phase 0.1 runs PARALLEL
3. HMML 2.0 takes priority
4. Only approved resources to agents

---
```
