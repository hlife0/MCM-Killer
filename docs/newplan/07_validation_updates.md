# Validation Updates

> **Version**: 3.2.0
> **Purpose**: Define updates to validator and time_validator for external resources

---

## Protocol 21: External Resource Data Consistency

### Location

`D:\mcmkiller\MCM-Killer\workspace\2025_C\.claude\protocols\protocol_21_external_resource_consistency.md`

### Purpose

Ensure data cited from external resources matches the source content.

### When Applied

- Phase 7 (Paper Writing)
- Phase 8 (Summary)
- Phase 9 (Polish)
- Phase 9.1 (Mock Judging)

---

### Protocol Specification

```markdown
# Protocol 21: External Resource Data Consistency

## Purpose
Prevent data inconsistencies and ensure file integrity for external resources.

## Trigger
- Phase 0.1: After resource processing (hash storage)
- Phase 7+: When external resources are cited (hash verification + data check)

## Checks

### 0. Hash Verification (CRITICAL - Run First)
Since `output/external_resources/` is gitignored, verify file integrity:

```bash
# Run before any other validation
python docs/newplan/10_tools/indexer.py verify
```

**AUTO-REJECT if any hash fails** - indicates file corruption or unauthorized modification.

### 1. Citation Verification
Every external resource referenced in the paper must have:
- Valid resource ID (MAN_xxx format for manual uploads)
- Entry in references section
- Resource exists in active/ folder
- Hash verified (from step 0)

### 2. Data Accuracy
Numbers, formulas, or claims attributed to external resources must match source:
- Compare paper text with content file (content.py, content.md, etc.)
- Verify mathematical expressions
- Check statistical values

### 3. Methodology Attribution
Methods described as "following [MAN_xxx]" must accurately represent source:
- No mischaracterization
- No cherry-picking of partial methods
- Proper adaptation noted

### 4. Source Availability
All cited resources must be:
- In active/ folder (not rejected/archived)
- Quality score >= 5.0 (approved or conditional)
- Hash verified

## Validation Process

```python
def validate_external_citations(paper_path: str) -> dict:
    """Validate external resource citations in paper with hash verification."""
    import subprocess

    results = {
        "passed": True,
        "checks": [],
        "issues": []
    }

    # Step 0: Verify all hashes first
    hash_result = subprocess.run(
        ["python", "docs/newplan/10_tools/indexer.py", "verify"],
        capture_output=True, text=True
    )

    if "FAILURES DETECTED" in hash_result.stdout:
        results["issues"].append("HASH FAILURE: " + hash_result.stdout)
        results["passed"] = False
        return results  # Stop immediately on hash failure

    results["checks"].append("HASH: All resources verified")

    paper = read_file(paper_path)
    citations = extract_citations(paper)  # Find all MAN_xxx references

    for citation in citations:
        resource_id = citation["id"]

        # Check 1: Resource exists
        resource_path = f"output/external_resources/active/{resource_id}"
        if not exists(resource_path):
            results["issues"].append(f"MISSING: {resource_id} not in active/")
            results["passed"] = False
            continue

        # Check 2: Data accuracy
        content = read_content_file(resource_path)  # Handles .py, .md, .csv
        for claim in citation["claims"]:
            if not verify_claim(claim, content):
                results["issues"].append(f"MISMATCH: {resource_id} - '{claim}'")
                results["passed"] = False

        results["checks"].append(f"VERIFIED: {resource_id}")

    return results
```

## Verdict Criteria

| Condition | Verdict |
|-----------|---------|
| Hash verified, all citations verified, data matches | ✅ APPROVED |
| Minor formatting differences only | ⚠️ CONDITIONAL |
| Hash failure | ❌ AUTO-REJECT (stop immediately) |
| Missing citations or data mismatch | ❌ REJECTED |

## Auto-Reject Conditions

- **Hash verification fails** (file integrity compromised)
- Resource ID not found in active/
- Quoted number differs from source by >5%
- Methodology misattributed
- Resource was REJECTED but still cited
```

---

## Validator Agent Updates

### Add to `workspace/2025_C/.claude/agents/validator.md`:

```markdown
## External Resource Validation (Protocol 21)

### When to Apply
During DATA, PAPER, SUMMARY, and FINAL validation stages.

### Pre-Check: Hash Verification

**CRITICAL**: Run this BEFORE any other external resource validation:

```bash
python docs/newplan/10_tools/indexer.py verify
```

If any hash fails:
- AUTO-REJECT the validation
- Report which resource(s) have integrity issues
- Request investigation before proceeding

### Checks

#### 1. Citation Completeness
```
For each external resource mentioned:
- [ ] Resource ID follows MAN_xxx format (manual) or WEB_xxx format (web)
- [ ] Entry exists in references section
- [ ] Resource file exists in output/external_resources/active/
- [ ] Resource hash verified (from pre-check)
```

#### 2. Data Consistency
```
For each claim attributed to external resource:
- [ ] Read source content file (content.py, content.md, etc.)
- [ ] Compare quoted value with source
- [ ] Verify within acceptable tolerance (±5%)
```

#### 3. Cross-Reference Check
```python
# Pseudo-validation code
# First verify hashes
if not verify_all_hashes():
    REJECT("Hash verification failed - file integrity compromised")

for citation in paper_citations:
    resource = load_resource(citation.id)
    if resource is None:
        REJECT("Missing resource: " + citation.id)

    for quoted_value in citation.values:
        source_value = find_in_content(resource.content, quoted_value)
        if abs(quoted_value - source_value) / source_value > 0.05:
            REJECT(f"Data mismatch: paper={quoted_value}, source={source_value}")
```

### Validation Report Addition

```markdown
## External Resource Consistency (Protocol 21)

### Hash Verification
Status: ✅ All 15 resources verified

### Citations Found
| Resource ID | Title | Status | Data Match |
|-------------|-------|--------|------------|
| MAN_001 | Bayesian SIR | ✅ Active | ✅ Verified |
| MAN_007 | Optimization | ✅ Active | ✅ Verified |
| MAN_003 | Statistics | ⚠️ Conditional | ✅ Verified |

### Data Checks
| Paper Location | Claimed Value | Source Value | Match |
|----------------|---------------|--------------|-------|
| Section 3.2, Eq.5 | β=0.3 | β=0.3 (MAN_001, line 45) | ✅ |
| Table 4, R₀ | 2.5 | 2.5 (MAN_007, line 112) | ✅ |

### Issues Found
None

### Protocol 21 Verdict: ✅ PASSED
```

---

## Time Validator Updates

### Add to `workspace/2025_C/.claude/agents/time_validator.md`:

```markdown
## Phase 0.1 Time Validation (External Resources)

### Time Requirements
| Metric | Value |
|--------|-------|
| Minimum | 10 minutes |
| Expected | 15-30 minutes |
| Maximum | 45 minutes |

### Valid Time Activities
- Processing files from inbox/
- Auto-generating metadata and SHA-256 hashes
- Quality review and scoring
- Syntax checking for code files
- Index updates
- Updating summary_for_agents.md

### Invalid Time Activities
- Waiting excessively when inbox is empty
- Repeated failed syntax checks without fixing issues
- Over-processing irrelevant files

### RED FLAGS (Auto-Consideration for Reject)
- Phase 0.1 completed in < 5 minutes with resources
  - Likely insufficient quality checking
- No resources processed despite 30+ minutes
  - inbox may be empty or files unsupported
- All code resources failed syntax check
  - Quality of provided files needs review

### Time Check Report
```markdown
## Phase 0.1 Time Analysis

**Duration**: 18 minutes
**Minimum Required**: 10 minutes
**Status**: ✅ MEETS MINIMUM

**Activity Breakdown**:
- Files processed from inbox: 5
- Quality reviews completed: 5
- Syntax checks passed: 3/4 code files
- Resources approved: 4
- Resources rejected: 1 (syntax failure)
- Quality reviews completed: 12
- Resources approved: 9

**Efficiency**: Good - 9 approved resources in 22 minutes

**Verdict**: ✅ APPROVED
```

---

## External Resource Complexity in Time Estimates

### Phase 1.5 Addition

When external resources are referenced in model design:

```markdown
## External Resource Complexity Adjustment

If model_design references external resources:

1. Identify complexity level:
   - Simple reference (conceptual): +0 minutes
   - Moderate adaptation (formulas): +30 minutes
   - Complex integration (full methodology): +60 minutes

2. Adjust time estimates accordingly:
   Original estimate: 4 hours
   External resource overhead: +30 minutes (moderate adaptation)
   Adjusted estimate: 4.5 hours

3. Note in validation:
   "Time estimate includes 30 minutes for WEB_001/WEB_007 adaptation"
```

---

## Phase 4.5 Addition: External Reference Fidelity

```markdown
## External Reference Implementation Check

If code_translator used external resources as reference:

### Verification Checklist
- [ ] Code implements OUR model_design, not external model
- [ ] External code adapted, not copied verbatim
- [ ] Parameters from our design, not external defaults
- [ ] Comments cite external reference appropriately

### AUTO-REJECT Conditions
- Code structure identical to external with only variable renames
- External model parameters used instead of our design
- No adaptation visible - pure copy-paste

### Acceptable Usage
- Algorithm structure inspired by external
- Comments reference external for clarity
- Our parameters and constraints applied
- Modifications documented
```

---

## Phase 5.5 Addition: External Validation Cross-Check

```markdown
## External Data Cross-Validation

If external resources contain comparable results:

### Cross-Check Process
1. Identify overlapping metrics between our results and external data
2. Compare values (with appropriate tolerance)
3. Flag significant divergence for investigation

### Example
```
Our prediction: USA Gold Medals 2028 = 42 ± 5
External reference (WEB_005): USA historical average = 38

Divergence: +4 (within prediction interval)
Status: ✅ Reasonable - prediction slightly above average
```

### RED FLAGS
- Our predictions wildly diverge from all external benchmarks
- Results contradict established literature without explanation
- Uncertainty intervals unrealistically narrow vs external studies
```

---

## Summary of Validation Changes

| Agent | Phase | Addition |
|-------|-------|----------|
| @validator | All | Protocol 21 citation checks |
| @validator | PAPER, FINAL | Data consistency cross-check |
| @time_validator | 0.1 (new) | External resource gathering time |
| @time_validator | 1.5 | External complexity adjustment |
| @time_validator | 4.5 | External reference fidelity |
| @time_validator | 5.5 | External cross-validation |
