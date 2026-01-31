# Folder Structure Design

> **Version**: 3.2.0
> **Purpose**: Define the external resources folder architecture

---

## Dynamic Creation

> **This folder structure is NOT pre-created.**
> It is created dynamically by @resource_manager during Phase 0.1 when the model starts working.

**Why dynamic creation?**
- Output folders should only exist when needed
- Prevents empty folder pollution in the codebase
- @resource_manager initializes all directories and config files


- Or when user first drops files and @resource_ingestor is invoked

**What if folder doesn't exist?**
- Agents checking `active/summary_for_agents.md` should gracefully handle missing folder
- No external resources = proceed with internal knowledge (HMML 2.0)

---

## Root Structure

```
output/external_resources/       # ADD TO .gitignore
│
├── inbox/                           # DROP ZONE: Manual file uploads
├── staging/                         # TEMPORARY: Awaiting quality check
├── active/                          # APPROVED: Ready for agent use
│   └── summary_for_agents.md        # CONTEXT: Agent overlay file
├── rejected/                        # FAILED: Quality < 5.0
├── archived/                        # HISTORICAL: No longer active
├── by_domain/                       # INDEX: Shortcuts by domain
├── by_phase/                        # INDEX: Shortcuts by phase
├── index.json                       # MASTER: Searchable index (with SHA-256 hashes)
├── statistics.json                  # ANALYTICS: Usage stats
├── config.json                      # SETTINGS: Pipeline config
└── README.md                        # DOCS: Structure documentation
```

**Note**: This entire folder should be added to `.gitignore` since resources are provided manually.

---

## Folder Descriptions

### inbox/

**Purpose**: Drop zone for manually provided files by the user.

**Lifecycle**:
- Files dropped by: User
- Processed by: @resource_ingestor
- Max age: Processed immediately on detection

**Expected file types**:
```
inbox/
├── my_bayesian_model.py        # Code file
├── optimization_paper.md       # Document
├── historical_data.csv         # Dataset
└── reference_implementation/   # Folder with multiple files
    ├── model.py
    └── utils.py
```

**Processing**: @resource_ingestor monitors this folder, auto-generates metadata, and moves to staging/.

---

### staging/

**Purpose**: Temporary storage for newly processed resources awaiting quality review.

**Lifecycle**:
- Created by: @resource_ingestor (from inbox/)
- Reviewed by: @quality_checker
- Max age: 24 hours (auto-rejected if exceeded)

**Contents per resource**:
```
staging/MAN_{timestamp}_{hash}/
├── content.py          # Code file (or .md, .csv, etc.)
├── metadata.json       # Auto-generated metadata (with SHA-256 hash)
├── summary.md          # Auto-generated summary
├── quality_report.md   # Added by @quality_checker
└── original/           # Original folder structure if any
```

---

### active/

**Purpose**: Approved resources available for agent consumption.

**Lifecycle**:
- Created by: @quality_checker (migration from staging)
- Used by: All agents via @knowledge_curator
- Archived after: 7 days if access_count < 5

**Contents per resource**:
```
active/WEB_{timestamp}_{hash}/
├── content.md          # Full extracted content
├── metadata.json       # Resource metadata (with quality_status)
├── summary.md          # Quick summary
├── quality_report.md   # Quality assessment
├── usage_log.json      # Access tracking
└── annotations/        # Agent notes (optional)
    ├── modeler_notes.md
    └── researcher_notes.md
```

---

### rejected/

**Purpose**: Resources that failed quality check (score < 5.0).

**Lifecycle**:
- Created by: @quality_checker (migration from staging)
- Retained for: 30 days (then auto-deleted)
- Purpose: Audit trail, avoid re-fetching

**Contents per resource**:
```
rejected/WEB_{timestamp}_{hash}/
├── metadata.json           # Original metadata
├── rejection_reason.md     # Why rejected
└── quality_report.md       # Quality scores
```

---

### archived/

**Purpose**: Historical resources no longer actively needed.

**Lifecycle**:
- Created by: @resource_manager (migration from active)
- Trigger: Unused > 7 days AND access_count < 5
- Can be: Restored to active if needed

**Contents**: Same as active/ (preserved completely)

---

### by_domain/

**Purpose**: Quick access to resources by domain category.

**Structure**:
```
by_domain/
├── epidemiology/
│   ├── WEB_001 -> ../../active/WEB_001/
│   └── WEB_005 -> ../../active/WEB_005/
├── optimization/
│   └── WEB_002 -> ../../active/WEB_002/
├── statistics/
│   └── WEB_003 -> ../../active/WEB_003/
├── machine_learning/
├── network_science/
├── differential_equations/
└── time_series/
```

**Implementation**: Symlinks or shortcut files pointing to active/ resources.

---

### by_phase/

**Purpose**: Quick access to resources by relevant phase.

**Structure**:
```
by_phase/
├── phase_0/           # Problem understanding
│   ├── WEB_001 -> ../../active/WEB_001/
│   └── WEB_003 -> ../../active/WEB_003/
├── phase_1/           # Model design
│   ├── WEB_002 -> ../../active/WEB_002/
│   └── WEB_006 -> ../../active/WEB_006/
├── phase_3/           # Data processing
│   └── WEB_004 -> ../../active/WEB_004/
├── phase_4/           # Code translation
│   └── WEB_008 -> ../../active/WEB_008/
└── phase_7/           # Paper writing
    └── WEB_001 -> ../../active/WEB_001/
```

---

## File Specifications

### metadata.json

```json
{
  "resource_id": "MAN_20260131_abc123",
  "title": "Bayesian SIR Model Implementation",
  "source_type": "manual_upload",
  "source_url": "local://inbox/bayesian_sir.py",
  "source_description": "Manually provided by user",
  "fetch_timestamp": "2026-01-31T12:00:00Z",
  "content_type": "code",
  "programming_language": "python",
  "domain": "statistics",
  "keywords": ["bayesian", "SIR", "epidemic", "inference"],
  "relevance_score": 7,
  "relevance_justification": "User-provided resource assumed relevant",
  "estimated_value": "HIGH",
  "suggested_consumers": ["@modeler", "@code_translator"],
  "file_hash_sha256": "a1b2c3d4e5f6...",
  "original_filename": "bayesian_sir.py",
  "file_size_bytes": 4523,
  "line_count": 245,
  "has_main": true,
  "functions": ["fit_model", "predict", "plot_results"],
  "imports": ["numpy", "scipy", "pymc"],
  "quality_status": "APPROVED",
  "quality_score": 8.5,
  "hash_verified_at": "2026-01-31T14:00:00Z"
}
```

### usage_log.json

```json
{
  "resource_id": "WEB_20260131_abc123",
  "created_at": "2026-01-31T14:00:00Z",
  "access_log": [
    {
      "agent": "@modeler",
      "timestamp": "2026-01-31T15:00:00Z",
      "phase": "1",
      "action": "read_summary"
    },
    {
      "agent": "@modeler",
      "timestamp": "2026-01-31T15:05:00Z",
      "phase": "1",
      "action": "read_content"
    },
    {
      "agent": "@writer",
      "timestamp": "2026-01-31T20:00:00Z",
      "phase": "7",
      "action": "cited"
    }
  ]
}
```

### index.json

See `02_agents/knowledge_curator.md` for full specification.

### config.json

See `02_agents/resource_manager.md` for full specification.

---

## Resource ID Format

**Pattern**: `MAN_{timestamp}_{hash}` (for manual uploads)

**Components**:
- `MAN`: Prefix identifying manual resources (vs WEB for web-fetched)
- `{timestamp}`: YYYYMMDD format (e.g., 20260131)
- `{hash}`: First 6 characters of SHA-256 hash of file content

**Examples**:
- `MAN_20260131_a1b2c3` (manual Python file)
- `MAN_20260131_d4e5f6` (manual document)

**Purpose**: Unique, sortable, traceable identifiers with data integrity via hash.

---

## Access Patterns

### For @resource_ingestor
```
Read:  inbox/*
Write: staging/{new_id}/
Delete: inbox/{processed_file}
```

### For @quality_checker
```
Read:  staging/{id}/
Write: staging/{id}/quality_report.md
Move:  staging/{id}/ -> active/{id}/ or rejected/{id}/
```

### For @knowledge_curator
```
Read:  active/*/
Write: index.json
Write: active/{id}/usage_log.json
```

### For @resource_manager
```
Read:  all folders
Write: all folders
Move:  active/{id}/ -> archived/{id}/
Delete: rejected/{id}/ (after 30 days)
```

### For Other Agents
```
Read:  active/{id}/summary.md
Read:  active/{id}/content.md
```

---

## Initialization Script

```bash
#!/bin/bash
# Initialize external resources structure

BASE="output/external_resources"

# Create directories
mkdir -p "$BASE"/{inbox,staging,active,rejected,archived}
mkdir -p "$BASE"/by_domain/{epidemiology,optimization,statistics,machine_learning,network_science}
mkdir -p "$BASE"/by_phase/{phase_0,phase_1,phase_3,phase_4,phase_7}

# Initialize files
echo '{"version":"3.2.0","last_updated":"","total_resources":0,"resources":{}}' > "$BASE/index.json"
echo '{"generated_at":"","totals":{}}' > "$BASE/statistics.json"

# Create README
cat > "$BASE/README.md" << 'EOF'
# External Resources (Gitignored)

This folder contains external resources provided manually by the user.

## Structure
- `inbox/` - Drop files here for processing
- `staging/` - Awaiting quality review
- `active/` - Approved for use
  - `summary_for_agents.md` - Read this for resource overview
- `rejected/` - Failed quality check
- `archived/` - No longer active

## Usage
1. Drop files in `inbox/`
2. @resource_ingestor processes them to `staging/`
3. @quality_checker reviews and migrates to `active/` or `rejected/`
4. All agents read `active/summary_for_agents.md` for context

## Data Integrity
SHA-256 hashes stored in index.json for Protocol 21 verification.
EOF

# Create context overlay template
cat > "$BASE/active/summary_for_agents.md" << 'EOF'
# External Resources Summary for Agents

> **Last Updated**: Not yet updated
> **Total Resources**: 0
> **Generated By**: @knowledge_curator

---

## Quick Reference

| Agent | Recommended Resources | Priority |
|-------|----------------------|----------|
| (none) | - | - |

---

*This file is updated by @knowledge_curator when resources are approved.*
EOF

echo "Structure initialized at $BASE"
echo "Add '$BASE/' to .gitignore"
```

---

## Verification Checklist

After initialization, verify:

- [ ] `inbox/` directory exists (for manual file drops)
- [ ] `staging/` directory exists
- [ ] `active/` directory exists
- [ ] `active/summary_for_agents.md` exists (context overlay)
- [ ] `rejected/` directory exists
- [ ] `archived/` directory exists
- [ ] `by_domain/` has 5+ subdirectories
- [ ] `by_phase/` has 5+ subdirectories
- [ ] `index.json` exists and is valid JSON (with version 3.2.0)
- [ ] `config.json` exists and is valid JSON
- [ ] `statistics.json` exists and is valid JSON
- [ ] `.gitignore` includes `output/external_resources/`
