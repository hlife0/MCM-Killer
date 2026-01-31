# Protocol 21: External Resource Data Consistency

> **Version**: 3.2.0
> **Purpose**: Ensure data integrity and citation accuracy for external resources

---

## Trigger

- **Phase 0.1**: After resource processing (hash storage)
- **Phase 7+**: When external resources are cited (hash verification + data check)

---

## Pre-Check: Hash Verification (CRITICAL)

Since `external_resources/` is gitignored, verify file integrity before any validation:

```bash
python docs/newplan/10_tools/indexer.py verify
```

**AUTO-REJECT if any hash fails** - indicates file corruption or unauthorized modification.

---

## Checks

### 1. Hash Verification
- Run `indexer.py verify` before any other checks
- Compare current SHA-256 hash with stored hash in index.json
- If mismatch detected: STOP and investigate

### 2. Citation Verification
Every external resource referenced in the paper must have:
- Valid resource ID (MAN_xxx format)
- Entry in references section
- Resource exists in active/ folder
- Hash verified (from step 1)

### 3. Data Accuracy
Numbers, formulas, or claims attributed to external resources must match source:
- Compare paper text with content file (content.py, content.md, etc.)
- Verify mathematical expressions
- Check statistical values (tolerance: ±5%)

### 4. Methodology Attribution
Methods described as "following [MAN_xxx]" must accurately represent source:
- No mischaracterization
- No cherry-picking of partial methods
- Proper adaptation noted

---

## Validation Process

```python
def validate_protocol_21(paper_path: str) -> dict:
    """Protocol 21: External Resource Data Consistency."""
    import subprocess

    results = {
        "passed": True,
        "checks": [],
        "issues": []
    }

    # Step 0: Verify all hashes first (CRITICAL)
    hash_result = subprocess.run(
        ["python", "docs/newplan/10_tools/indexer.py", "verify"],
        capture_output=True, text=True
    )

    if "FAILURES DETECTED" in hash_result.stdout:
        results["issues"].append("HASH FAILURE: " + hash_result.stdout)
        results["passed"] = False
        return results  # Stop immediately on hash failure

    results["checks"].append("HASH: All resources verified")

    # Step 1: Extract citations from paper
    paper = read_file(paper_path)
    citations = extract_citations(paper)  # Find all MAN_xxx references

    # Step 2: Verify each citation
    for citation in citations:
        resource_id = citation["id"]

        # Check resource exists
        resource_path = f"external_resources/active/{resource_id}"
        if not exists(resource_path):
            results["issues"].append(f"MISSING: {resource_id} not in active/")
            results["passed"] = False
            continue

        # Check data accuracy
        content = read_content_file(resource_path)
        for claim in citation.get("claims", []):
            if not verify_claim(claim, content):
                results["issues"].append(f"MISMATCH: {resource_id} - '{claim}'")
                results["passed"] = False

        results["checks"].append(f"VERIFIED: {resource_id}")

    return results
```

---

## Verdict Criteria

| Condition | Verdict |
|-----------|---------|
| Hash verified, all citations verified, data matches | APPROVED |
| Minor formatting differences only | CONDITIONAL |
| Hash failure | AUTO-REJECT (stop immediately) |
| Missing citations or data mismatch | REJECTED |

---

## Auto-Reject Conditions

1. **Hash verification fails** (file integrity compromised)
2. Resource ID not found in active/
3. Quoted number differs from source by >5%
4. Methodology misattributed
5. Resource was REJECTED but still cited

---

## Validation Report Template

```markdown
## External Resource Consistency (Protocol 21)

### Hash Verification
Status: ✅ All X resources verified

### Citations Found
| Resource ID | Title | Status | Data Match |
|-------------|-------|--------|------------|
| MAN_001 | Model Code | ✅ Active | ✅ Verified |

### Data Checks
| Paper Location | Claimed Value | Source Value | Match |
|----------------|---------------|--------------|-------|
| Section 3.2 | β=0.3 | β=0.3 (MAN_001:45) | ✅ |

### Issues Found
None

### Protocol 21 Verdict: ✅ PASSED
```

---

## Recovery Procedures

### On Hash Failure

1. **Identify** which resource(s) have hash mismatch
2. **Investigate** whether edit was intentional
3. If intentional: Run `indexer.py add` to update hash
4. If not intentional: Restore from original or re-process from inbox

### On Missing Resource

1. Check if resource was archived or rejected
2. If archived: Consider restoring to active
3. If rejected: Remove citation or find alternative

---

**Version**: 3.2.0
**Last Updated**: 2026-01-31
