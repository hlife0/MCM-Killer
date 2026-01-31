# Step-by-Step Implementation Guide

> **Version**: 3.2.0
> **Purpose**: Executable implementation steps for the external resources pipeline

---

## Implementation Overview

| Step | Description | Duration | Dependencies |
|------|-------------|----------|--------------|
| 1 | Create folder structure | 5 min | None |
| 2 | Create configuration files | 10 min | Step 1 |
| 3 | Create agent files | 30 min | Step 1 |
| 4 | Create tool scripts | 20 min | Step 1 |
| 5 | Create Protocol 21 | 10 min | Step 3 |
| 6 | Update existing agents | 15 min | Step 5 |
| 7 | Update CLAUDE.md | 15 min | Step 3-6 |
| 8 | Update protocol index | 5 min | Step 5 |
| 9 | Test pipeline | 20 min | Step 1-8 |
| 10 | Verify integration | 10 min | Step 9 |

**Total Estimated Time**: ~2.5 hours

---

## Step 1: Create Folder Structure

### 1.1 Create main directories

```bash
BASE="D:/mcmkiller/MCM-Killer/workspace/2025_C/output/external_resources"

mkdir -p "$BASE/staging"
mkdir -p "$BASE/active"
mkdir -p "$BASE/rejected"
mkdir -p "$BASE/archived"
```

### 1.2 Create index directories

```bash
mkdir -p "$BASE/by_domain/epidemiology"
mkdir -p "$BASE/by_domain/optimization"
mkdir -p "$BASE/by_domain/statistics"
mkdir -p "$BASE/by_domain/machine_learning"
mkdir -p "$BASE/by_domain/network_science"

mkdir -p "$BASE/by_phase/phase_0"
mkdir -p "$BASE/by_phase/phase_1"
mkdir -p "$BASE/by_phase/phase_3"
mkdir -p "$BASE/by_phase/phase_4"
mkdir -p "$BASE/by_phase/phase_7"
```

### 1.3 Verify structure

```bash
ls -la "$BASE"
# Should show: staging, active, rejected, archived, by_domain, by_phase
```

---

## Step 2: Create Configuration Files

### 2.1 Create index.json

**Path**: `output/external_resources/index.json`

```json
{
  "version": "3.2.0",
  "last_updated": "",
  "total_resources": 0,
  "by_domain": {},
  "by_type": {},
  "by_consumer": {},
  "by_phase": {},
  "resources": {}
}
```

### 2.2 Create config.json

**Path**: `output/external_resources/config.json`

```json
{
  "version": "3.2.0",
  "created_at": "2026-01-31T00:00:00Z",
  "lifecycle": {
    "max_staging_age_hours": 24,
    "max_active_resources": 50,
    "auto_archive_after_days": 7,
    "auto_delete_rejected_after_days": 30
  },
  "quality": {
    "threshold_approve": 7.0,
    "threshold_conditional": 5.0
  },
  "domains": {
    "allowed": [
      "arxiv.org",
      "scholar.google.com",
      "github.com",
      "data.gov",
      "who.int",
      "cdc.gov",
      "nature.com",
      "ieee.org",
      "sciencedirect.com",
      "springer.com"
    ],
    "blocked": [
      "facebook.com",
      "twitter.com",
      "pinterest.com",
      "instagram.com",
      "tiktok.com"
    ]
  },
  "limits": {
    "max_content_size_kb": 500,
    "max_resources_per_fetch": 10,
    "fetch_timeout_seconds": 30
  }
}
```

### 2.3 Create statistics.json

**Path**: `output/external_resources/statistics.json`

```json
{
  "generated_at": "",
  "totals": {
    "fetched": 0,
    "approved": 0,
    "conditional": 0,
    "rejected": 0,
    "archived": 0
  },
  "by_phase": {},
  "by_domain": {},
  "by_agent": {},
  "most_accessed": []
}
```

### 2.4 Create README.md

**Path**: `output/external_resources/README.md`

```markdown
# External Resources

This folder contains external resources fetched from the internet.

## Structure
- `staging/` - Awaiting quality review
- `active/` - Approved for agent use
- `rejected/` - Failed quality check
- `archived/` - No longer active

## Quality Thresholds
- APPROVED: >= 7.0/10
- CONDITIONAL: 5.0-6.9/10
- REJECTED: < 5.0/10

## Usage
Query @knowledge_curator for resource recommendations.

## Files
- `index.json` - Master searchable index
- `config.json` - Pipeline configuration
- `statistics.json` - Usage analytics
```

---

## Step 3: Create Agent Files

### 3.1 Copy agent templates

Copy from `docs/newplan/02_agents/` to `.claude/agents/`:

```bash
SRC="D:/mcmkiller/MCM-Killer/docs/newplan/02_agents"
DEST="D:/mcmkiller/MCM-Killer/workspace/2025_C/.claude/agents"

cp "$SRC/web_crawler.md" "$DEST/"
cp "$SRC/quality_checker.md" "$DEST/"
cp "$SRC/knowledge_curator.md" "$DEST/"
cp "$SRC/resource_manager.md" "$DEST/"
```

### 3.2 Verify agent files

```bash
ls -la "$DEST" | grep -E "(web_crawler|quality_checker|knowledge_curator|resource_manager)"
# Should show all 4 new agent files
```

---

## Step 4: Create Tool Scripts

### 4.1 Create quality check script

**Path**: `workspace/2025_C/tools/external_resource_quality_check.py`

```python
#!/usr/bin/env python3
"""
External Resource Quality Check Tool
Automates quality scoring for external resources.
"""

import json
import os
from pathlib import Path
from typing import Dict, Optional

# Quality criteria weights
WEIGHTS = {
    "credibility": 0.25,
    "relevance": 0.30,
    "quality": 0.25,
    "actionability": 0.20
}

# Domain credibility scores
DOMAIN_SCORES = {
    "nature.com": 10, "science.org": 10, "pnas.org": 10,
    "data.gov": 10, "cdc.gov": 10, "who.int": 10,
    "arxiv.org": 8, "ieee.org": 8, "springer.com": 8,
    "github.com": 6, "medium.com": 4,
    "stackoverflow.com": 2
}


def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    from urllib.parse import urlparse
    return urlparse(url).netloc.replace("www.", "")


def score_credibility(metadata: Dict) -> int:
    """Score source credibility based on domain."""
    url = metadata.get("source_url", "")
    domain = extract_domain(url)

    for known_domain, score in DOMAIN_SCORES.items():
        if known_domain in domain:
            return score
    return 2  # Default low score for unknown


def check_content_quality(content_path: str) -> int:
    """Score content extraction quality."""
    if not os.path.exists(content_path):
        return 0

    content = Path(content_path).read_text(encoding='utf-8')

    # Check for key sections
    sections = ["abstract", "methodology", "results", "references"]
    found = sum(1 for s in sections if s.lower() in content.lower())

    # Check content length
    word_count = len(content.split())

    if word_count < 100:
        return 2
    elif word_count < 500:
        return 4
    elif word_count < 1000:
        return 6
    elif found >= 3:
        return 8
    else:
        return 7


def calculate_total(scores: Dict) -> float:
    """Calculate weighted total score."""
    total = sum(scores.get(k, 0) * WEIGHTS[k] for k in WEIGHTS)
    return round(total, 1)


def generate_report(resource_path: str) -> Dict:
    """Generate quality report for a resource."""
    metadata_path = os.path.join(resource_path, "metadata.json")
    content_path = os.path.join(resource_path, "content.md")

    with open(metadata_path) as f:
        metadata = json.load(f)

    # Auto-score what we can
    scores = {
        "credibility": score_credibility(metadata),
        "quality": check_content_quality(content_path),
        "relevance": metadata.get("relevance_score", 5),  # From web_crawler
        "actionability": 5  # Default, needs manual review
    }

    total = calculate_total(scores)

    if total >= 7.0:
        verdict = "APPROVED"
    elif total >= 5.0:
        verdict = "CONDITIONAL"
    else:
        verdict = "REJECTED"

    return {
        "resource_id": metadata.get("resource_id"),
        "scores": scores,
        "total": total,
        "verdict": verdict
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python external_resource_quality_check.py <resource_path>")
        sys.exit(1)

    result = generate_report(sys.argv[1])
    print(json.dumps(result, indent=2))
```

### 4.2 Create indexer script

**Path**: `workspace/2025_C/tools/external_resource_indexer.py`

```python
#!/usr/bin/env python3
"""
External Resource Indexer
Maintains the master index of external resources.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List

INDEX_PATH = "output/external_resources/index.json"


def load_index() -> Dict:
    """Load the master index."""
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH) as f:
            return json.load(f)
    return {"resources": {}, "by_domain": {}, "by_type": {}, "by_consumer": {}}


def save_index(index: Dict):
    """Save the master index."""
    index["last_updated"] = datetime.now().isoformat()
    index["total_resources"] = len(index.get("resources", {}))

    with open(INDEX_PATH, "w") as f:
        json.dump(index, f, indent=2)


def add_resource(resource_id: str, metadata: Dict, quality_score: float):
    """Add a resource to the index."""
    index = load_index()

    # Add to main resources
    index["resources"][resource_id] = {
        "title": metadata.get("title", "Unknown"),
        "path": f"output/external_resources/active/{resource_id}/",
        "quality_score": quality_score,
        "domain": metadata.get("domain", "unknown"),
        "type": metadata.get("content_type", "unknown"),
        "tags": metadata.get("keywords", []),
        "suggested_consumers": metadata.get("suggested_consumers", []),
        "added_date": datetime.now().strftime("%Y-%m-%d")
    }

    # Update category indexes
    domain = metadata.get("domain", "unknown")
    if domain not in index["by_domain"]:
        index["by_domain"][domain] = []
    if resource_id not in index["by_domain"][domain]:
        index["by_domain"][domain].append(resource_id)

    content_type = metadata.get("content_type", "unknown")
    if content_type not in index["by_type"]:
        index["by_type"][content_type] = []
    if resource_id not in index["by_type"][content_type]:
        index["by_type"][content_type].append(resource_id)

    for consumer in metadata.get("suggested_consumers", []):
        if consumer not in index["by_consumer"]:
            index["by_consumer"][consumer] = []
        if resource_id not in index["by_consumer"][consumer]:
            index["by_consumer"][consumer].append(resource_id)

    save_index(index)
    return index


def remove_resource(resource_id: str):
    """Remove a resource from the index."""
    index = load_index()

    if resource_id in index["resources"]:
        del index["resources"][resource_id]

    for category in ["by_domain", "by_type", "by_consumer"]:
        for key in index.get(category, {}):
            if resource_id in index[category][key]:
                index[category][key].remove(resource_id)

    save_index(index)


def search(query: str) -> List[Dict]:
    """Search for resources by keyword."""
    index = load_index()
    results = []

    query_lower = query.lower()
    for resource_id, info in index.get("resources", {}).items():
        # Check title
        if query_lower in info.get("title", "").lower():
            results.append({"id": resource_id, **info})
            continue

        # Check tags
        if any(query_lower in tag.lower() for tag in info.get("tags", [])):
            results.append({"id": resource_id, **info})

    # Sort by quality score
    results.sort(key=lambda x: x.get("quality_score", 0), reverse=True)
    return results


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python external_resource_indexer.py add <resource_id> <metadata.json> <quality_score>")
        print("  python external_resource_indexer.py remove <resource_id>")
        print("  python external_resource_indexer.py search <query>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "search" and len(sys.argv) >= 3:
        results = search(sys.argv[2])
        print(json.dumps(results, indent=2))
    elif command == "add" and len(sys.argv) >= 5:
        with open(sys.argv[3]) as f:
            metadata = json.load(f)
        index = add_resource(sys.argv[2], metadata, float(sys.argv[4]))
        print(f"Added {sys.argv[2]} to index. Total: {index['total_resources']}")
    elif command == "remove" and len(sys.argv) >= 3:
        remove_resource(sys.argv[2])
        print(f"Removed {sys.argv[2]} from index.")
```

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
- Resource ID follows WEB_xxx format
- Entry exists in references section
- Resource file exists in active/ folder

### 2. Data Accuracy
- Compare quoted values with source content.md
- Tolerance: ±5% for numerical values
- Exact match for text/methodology

### 3. Source Availability
- Resource must be in active/ (not rejected/archived)
- Quality score >= 5.0

## Verdict Criteria

| Condition | Verdict |
|-----------|---------|
| All verified, data matches | ✅ APPROVED |
| Minor formatting differences | ⚠️ CONDITIONAL |
| Missing citations or mismatch | ❌ REJECTED |

## Auto-Reject Conditions
- Resource ID not found in active/
- Quoted number differs by >5%
- Methodology misattributed
- Rejected resource cited

## Validation Report Template

```markdown
## External Resource Consistency (Protocol 21)

### Citations Found
| Resource ID | Title | Status | Data Match |
|-------------|-------|--------|------------|
| WEB_001 | ... | ✅ Active | ✅ |

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
1. Citation completeness (WEB_xxx in references)
2. Data consistency (values match source)
3. Resource availability (in active/)

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

## Step 9: Test Pipeline

### 9.1 Test folder structure

```bash
ls -la output/external_resources/
# Verify all directories and files exist
```

### 9.2 Test config loading

```python
import json
with open("output/external_resources/config.json") as f:
    config = json.load(f)
print(config["quality"]["threshold_approve"])  # Should print 7.0
```

### 9.3 Test index operations

```bash
python tools/external_resource_indexer.py search "epidemic"
# Should return empty list initially
```

---

## Step 10: Verify Integration

### 10.1 Checklist

- [ ] All 4 agent files in `.claude/agents/`
- [ ] Folder structure at `output/external_resources/`
- [ ] Protocol 21 in `.claude/protocols/`
- [ ] CLAUDE.md updated with new section
- [ ] Validator includes Protocol 21 checks
- [ ] Tool scripts in `tools/`
- [ ] Config files initialized

### 10.2 Smoke test

1. Manually create a test resource in staging/
2. Run quality check script
3. Verify migration to active/ works
4. Check index update

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
   - Test consultation flow
