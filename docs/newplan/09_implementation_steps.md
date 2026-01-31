# Step-by-Step Implementation Guide

> **Version**: 3.2.0
> **Purpose**: Executable implementation steps for the external resources pipeline

---

## Implementation Overview

| Step | Description | Duration | Dependencies |
|------|-------------|----------|--------------|
| 1 | Folder structure (auto-created) | 0 min | None |
| 2 | Create agent files | 30 min | None |
| 3 | Create tool scripts | 20 min | None |
| 4 | Create Protocol 21 | 10 min | Step 2 |
| 5 | Update existing agents | 15 min | Step 4 |
| 6 | Update CLAUDE.md | 15 min | Step 2-5 |
| 7 | Update protocol index | 5 min | Step 4 |
| 8 | Update .gitignore | 2 min | None |
| 9 | Test pipeline | 20 min | Step 1-8 |
| 10 | Verify integration | 10 min | Step 9 |

---

## Step 1: Folder Structure (Dynamic Creation)

> [!IMPORTANT]
> **The folder structure is NOT pre-created.**
> It is created dynamically by @resource_manager during Phase 0.1 when the model starts working.

### 1.1 Dynamic Creation by @resource_manager

During Phase 0.1, @resource_manager automatically creates the folder structure:

```
output/external_resources/
├── inbox/             # Manual drop zone
├── staging/           # Awaiting quality check
├── active/            # Approved resources
│   └── summary_for_agents.md
├── rejected/          # Failed quality check
├── archived/          # Historical
├── by_domain/         # Symlinks by domain
├── by_phase/          # Symlinks by phase
├── index.json         # Master index
├── config.json        # Configuration
├── statistics.json    # Usage stats
└── README.md          # Usage instructions
```

### 1.2 When Folder is Created

The folder structure is created:
- **Trigger**: When user first drops files into the (not yet existing) inbox/ area
- **Alternative**: When @resource_manager is explicitly invoked during Phase 0.1
- **Initialization**: @resource_manager creates all directories and config files

### 1.3 Initialization Responsibility

@resource_manager handles:
1. Create all directories (inbox, staging, active, rejected, archived, by_domain, by_phase)
2. Initialize index.json with version 3.2.0
3. Initialize config.json with default thresholds
4. Initialize statistics.json
5. Create summary_for_agents.md template in active/
6. Create README.md with usage instructions

### 1.4 If Folder Doesn't Exist

When any agent checks `output/external_resources/active/summary_for_agents.md`:
- If folder doesn't exist → No external resources available → Proceed with internal knowledge
- This is expected during Phase 0 (before Phase 0.1 runs)

---

## Step 2: Create Agent Files

### 3.1 Copy agent templates

Copy from `docs/newplan/02_agents/` to `.claude/agents/`:

```bash
SRC="D:/mcmkiller/MCM-Killer/docs/newplan/02_agents"
DEST="D:/mcmkiller/MCM-Killer/workspace/2025_C/.claude/agents"

cp "$SRC/resource_ingestor.md" "$DEST/"
cp "$SRC/quality_checker.md" "$DEST/"
cp "$SRC/knowledge_curator.md" "$DEST/"
cp "$SRC/resource_manager.md" "$DEST/"
```

### 3.2 Verify agent files

```bash
ls -la "$DEST" | grep -E "(resource_ingestor|quality_checker|knowledge_curator|resource_manager)"
# Should show all 4 new agent files
```

---

## Step 4: Create Tool Scripts

### 4.1 Create quality check script

**Path**: `docs/newplan/10_tools/quality_check.py`

(See 10_tools/quality_check.py for full implementation with syntax validation and code weights)

### 4.2 Create indexer script

**Path**: `docs/newplan/10_tools/indexer.py`

(See 10_tools/indexer.py for full implementation with SHA-256 hashing and verify commands)

---

## Step 5: Create Protocol 21

**Path**: `workspace/2025_C/.claude/protocols/protocol_21_external_resource_consistency.md`

```markdown
# Protocol 21: External Resource Data Consistency

## Purpose
Prevent data inconsistencies between paper content and cited external resources.

## When Applied
- Phase 7 (Paper Writing)
- Phase 8 (Summary)
- Phase 9 (Polish)
- Phase 9.1 (Mock Judging)

## Checks

### 1. Citation Verification
- Resource ID follows MAN_xxx format
- Entry exists in references section
- Resource file exists in active/ folder

### 2. Data Accuracy
- Compare quoted values with source content.md
- Tolerance: ±5% for numerical values
- Exact match for text/methodology

### 3. Source Availability
- Resource must be in active/ (not rejected/archived)
- Quality score >= 5.0

### 4. SHA-256 Hash Verification
- Run: `python docs/newplan/10_tools/indexer.py verify`
- All file hashes must match stored values
- Hash mismatch = file tampering = AUTO-REJECT

## Verdict Criteria

| Condition | Verdict |
|-----------|---------|
| All verified, data matches, hashes valid | ✅ APPROVED |
| Minor formatting differences | ⚠️ CONDITIONAL |
| Missing citations, mismatch, or hash failure | ❌ REJECTED |

## Auto-Reject Conditions
- Resource ID not found in active/
- Quoted number differs by >5%
- Methodology misattributed
- Rejected resource cited
- **SHA-256 hash mismatch**

## Validation Report Template

```markdown
## External Resource Consistency (Protocol 21)

### Citations Found
| Resource ID | Title | Status | Data Match | Hash |
|-------------|-------|--------|------------|------|
| MAN_001 | ... | ✅ Active | ✅ | ✅ |

### Hash Verification
Run: python docs/newplan/10_tools/indexer.py verify
Result: X/Y files verified OK

### Issues Found
{list issues or "None"}

### Protocol 21 Verdict: ✅ PASSED / ❌ FAILED
```
```

---

## Step 6: Update Existing Agents

### 6.1 Update validator.md

Add to `workspace/2025_C/.claude/agents/validator.md`:

```markdown
## External Resource Validation (Protocol 21)

### Checks
1. Citation completeness (MAN_xxx in references)
2. Data consistency (values match source)
3. Resource availability (in active/)
4. **SHA-256 hash verification**

### Report Addition
Include "External Resource Consistency" section in validation reports.
```

### 6.2 Update time_validator.md

Add Phase 0.1 timing requirements (see 07_validation_updates.md).

---

## Step 7: Update CLAUDE.md

Add new sections as specified in `08_claude_md_updates.md`.

---

## Step 8: Update Protocol Index

Add to `workspace/2025_C/.claude/protocols/README.md`:

```markdown
| 21 | External Resource Data Consistency | Phase 7+ | ✅ |
```

---

## Step 9: Update .gitignore

Add to `workspace/2025_C/.gitignore` or root `.gitignore`:

```
# External resources (manual uploads, gitignored for SHA-256 integrity)
workspace/*/output/external_resources/
```

---

## Step 9: Test Pipeline

### 9.1 Test @resource_manager initialization

Before testing, invoke @resource_manager to create folder structure:

```bash
# @resource_manager creates this when invoked during Phase 0.1
# After initialization, verify:
ls -la output/external_resources/
# Should show: inbox, staging, active, rejected, archived, by_domain, by_phase
```

### 9.2 Test config loading (after initialization)

```python
import json
with open("output/external_resources/config.json") as f:
    config = json.load(f)
print(config["quality"]["threshold_approve"])  # Should print 7.0
```

### 9.3 Test index operations

```bash
python docs/newplan/10_tools/indexer.py stats
# Should return current statistics
```

### 9.4 Test hash verification

```bash
python docs/newplan/10_tools/indexer.py verify
# Should return "No resources to verify" or verification results
```

---

## Step 10: Verify Integration

### 10.1 Checklist

- [ ] All 4 agent files in `.claude/agents/`
- [ ] @resource_manager can create folder structure dynamically
- [ ] Protocol 21 in `.claude/protocols/`
- [ ] CLAUDE.md updated with new section
- [ ] Validator includes Protocol 21 checks
- [ ] All 23 existing agents have "External Resources Check" section
- [ ] Tool scripts in `docs/newplan/10_tools/`
- [ ] .gitignore updated

### 10.2 Smoke test

1. Invoke @resource_manager to initialize folder structure
2. Verify folder structure created at `output/external_resources/`
3. Verify inbox/ and active/summary_for_agents.md exist
4. Manually drop a test file in inbox/
5. Run @resource_ingestor to process
6. Run @quality_checker to validate
7. Verify migration to active/ works
8. Check index update with SHA-256 hash
9. Verify summary_for_agents.md updated

---

## Post-Implementation

After completing all steps:

1. **Commit changes**:
   ```bash
   git add .
   git commit -m "Add external resources pipeline (v3.2.0)"
   ```

2. **Update version in architectures**:
   - Create `architectures/v3-2-0/` if needed
   - Document changes

3. **Test with real workflow**:
   - Run Phase 0 → 0.1 → 0.2 sequence
   - Verify parallel execution works
   - Test context injection (agents reading summary_for_agents.md)
