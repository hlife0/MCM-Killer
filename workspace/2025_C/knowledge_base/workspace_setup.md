# Workspace Setup

> **Source**: Extracted from CLAUDE.md v3.1.0
> **Purpose**: Directory initialization commands

## Workspace Initialization (MANDATORY)

> [!CRITICAL] **At START of EVERY competition, you MUST create all directories.**

### Create Directory Structure

```bash
mkdir -p output/docs/consultations output/docs/rewind output/docs/validation output/docs/insights
mkdir -p output/implementation/code output/implementation/data output/implementation/logs output/implementation/models
mkdir -p output/model output/model_proposals output/figures output/paper output/results
```

### Verification

**Verify**: `ls -la output/docs/ output/implementation/ output/model/ output/paper/`

**NEVER proceed to Phase 0 until all directories exist.**

---

*Reference: CLAUDE.md - Main operational documentation*
