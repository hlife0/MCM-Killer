# Quality Checking Pipeline

> **Version**: 3.2.0
> **Purpose**: Define the quality validation workflow for external resources

---

## Pipeline Overview

```
┌─────────────────┐
│  @web_crawler   │
│  fetches to     │
│  staging/       │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────┐
│                  QUALITY GATEWAY                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │              @quality_checker                      │  │
│  │                                                    │  │
│  │  1. Source Credibility (25%)                      │  │
│  │  2. Content Relevance (30%)                       │  │
│  │  3. Content Quality (25%)                         │  │
│  │  4. Actionability (20%)                           │  │
│  │                                                    │  │
│  │  Total = Weighted Sum                             │  │
│  └───────────────────────────────────────────────────┘  │
└────────┬──────────────────┬──────────────────┬──────────┘
         │                  │                  │
    >= 7.0             5.0-6.9              < 5.0
         │                  │                  │
         ▼                  ▼                  ▼
   ┌──────────┐      ┌──────────────┐    ┌──────────┐
   │ APPROVED │      │ CONDITIONAL  │    │ REJECTED │
   │ active/  │      │ active/      │    │ rejected/│
   │          │      │ (warnings)   │    │          │
   └──────────┘      └──────────────┘    └──────────┘
```

---

## Scoring Rubrics

### 1. Source Credibility (25% weight)

Measures the trustworthiness and academic rigor of the source.

| Score | Criteria | Examples |
|-------|----------|----------|
| **10** | Peer-reviewed journal, official government data | Nature, Science, PNAS, data.gov, CDC |
| **8** | Preprint server, top university, established org | arXiv, NIH, MIT, WHO reports |
| **6** | Industry white paper, recognized organization | McKinsey, Gartner, IEEE proceedings |
| **4** | Expert blog with citations, verified author | TowardsDataScience with refs, known researcher |
| **2** | General blog, forum, Q&A site | Medium without refs, Stack Overflow |
| **0** | Unknown source, no author, no citations | Anonymous blog, social media |

**Automatic scoring hints**:
```python
HIGH_CREDIBILITY = ["nature.com", "science.org", "pnas.org", "data.gov", "cdc.gov", "who.int"]
MEDIUM_HIGH = ["arxiv.org", "ieee.org", "springer.com", "sciencedirect.com"]
MEDIUM = ["github.com", "towardsdatascience.com", "medium.com"]
LOW = ["stackoverflow.com", "reddit.com", "quora.com"]
BLOCKED = ["facebook.com", "twitter.com", "instagram.com"]
```

---

### 2. Content Relevance (30% weight)

Measures how directly the content applies to the current problem.

| Score | Criteria |
|-------|----------|
| **10** | Directly addresses our exact problem type, methodology, or domain |
| **8** | Same domain, closely related methodology, transferable approach |
| **6** | Related domain, general methodology applicable with adaptation |
| **4** | Tangentially related, requires significant interpretation |
| **2** | Minimal connection, mostly for background context |
| **0** | Not relevant to our current problem or approach |

**Relevance assessment process**:
1. Read problem requirements from `output/problem/problem_requirements_1.md`
2. Read proposed methodology from `output/model/research_notes_1.md`
3. Compare resource content against problem keywords and methods
4. Assess direct applicability vs. background value

---

### 3. Content Quality (25% weight)

Measures the completeness and usability of the extracted content.

| Score | Criteria |
|-------|----------|
| **10** | Complete extraction, all sections clear, proper formatting, no errors |
| **8** | Good extraction, minor formatting issues, all key content present |
| **6** | Adequate extraction, some sections incomplete, readable |
| **4** | Partial extraction, significant gaps, some sections unreadable |
| **2** | Poor extraction, most content missing or garbled |
| **0** | Extraction failed, content unusable |

**Quality checklist**:
- [ ] Abstract/summary present and complete
- [ ] Methodology section extracted
- [ ] Formulas/equations rendered (if applicable)
- [ ] Code blocks preserved (if applicable)
- [ ] References/citations included
- [ ] No truncation or "continues on next page" artifacts

---

### 4. Actionability (20% weight)

Measures practical utility for implementation.

| Score | Criteria |
|-------|----------|
| **10** | Ready-to-use: formulas, code, or data that can be directly applied |
| **8** | Clear methodology: step-by-step process, implementable with effort |
| **6** | Conceptual guidance: useful principles, need to develop implementation |
| **4** | Background context: useful for understanding, no direct application |
| **2** | Minimal utility: interesting but not actionable |
| **0** | Not actionable: purely theoretical or unrelated |

**Actionability indicators**:
- Contains code examples or pseudocode → +2
- Contains mathematical formulas → +1
- Contains data or data sources → +2
- Contains step-by-step methodology → +1
- Contains worked examples → +1

---

## Score Calculation

```python
def calculate_quality_score(scores: dict) -> float:
    """Calculate weighted quality score."""
    weights = {
        "credibility": 0.25,
        "relevance": 0.30,
        "quality": 0.25,
        "actionability": 0.20
    }

    total = sum(scores[k] * weights[k] for k in weights)
    return round(total, 1)

# Example
scores = {
    "credibility": 8,      # arXiv preprint
    "relevance": 9,        # directly addresses our approach
    "quality": 7,          # good extraction, minor issues
    "actionability": 8     # clear methodology
}

total = (8 * 0.25) + (9 * 0.30) + (7 * 0.25) + (8 * 0.20)
# = 2.0 + 2.7 + 1.75 + 1.6 = 8.05 → APPROVED
```

---

## Threshold Decisions

| Score Range | Verdict | Action | Notification |
|-------------|---------|--------|--------------|
| **>= 7.0** | APPROVED | Migrate to `active/` | "Resource approved and available" |
| **5.0 - 6.9** | CONDITIONAL | Migrate with warnings | "Resource approved with cautions" |
| **< 5.0** | REJECTED | Move to `rejected/` | "Resource rejected, see reasons" |

---

## Quality Report Format

Each reviewed resource gets a quality report:

```markdown
# Quality Report: WEB_20260131_abc123

## Resource Information
- **Title**: Network-Based SIR Models for Epidemic Prediction
- **Source**: https://arxiv.org/abs/2401.12345
- **Type**: Academic Paper
- **Reviewed By**: @quality_checker
- **Review Date**: 2026-01-31T14:00:00Z

---

## Scoring

| Criterion | Weight | Raw Score | Weighted | Justification |
|-----------|--------|-----------|----------|---------------|
| Source Credibility | 25% | 8/10 | 2.00 | arXiv preprint, known research group |
| Content Relevance | 30% | 9/10 | 2.70 | Directly addresses our SIR-Network approach |
| Content Quality | 25% | 7/10 | 1.75 | Good extraction, minor LaTeX rendering issues |
| Actionability | 20% | 8/10 | 1.60 | Includes Python pseudocode, clear steps |

## **Total Score: 8.05/10**

---

## Verdict: ✅ APPROVED

---

## Detailed Assessment

### Strengths
1. Peer-reviewed equivalent (arXiv with citations)
2. Directly applicable to our epidemic modeling approach
3. Includes implementation guidance in Appendix A
4. Recent publication (2024)

### Weaknesses
1. Some LaTeX formulas not fully rendered
2. Missing convergence analysis details
3. Code is pseudocode, not complete implementation

### Recommendations for Consumers
- @modeler: Focus on Section 3 for mathematical formulation
- @code_translator: Appendix A has pseudocode (needs adaptation)
- Verify formula in Equation 12 (rendering issue)

---

## Migration Details
- **Source**: output/external_resources/staging/WEB_20260131_abc123/
- **Target**: output/external_resources/active/WEB_20260131_abc123/
- **Index Updated**: Yes
- **Consumers Notified**: Yes
```

---

## Automated Quality Checks

Some checks can be automated before human scoring:

### Pre-Check Script

```python
def automated_pre_check(resource_path: str) -> dict:
    """Run automated quality pre-checks."""
    results = {
        "passed": True,
        "checks": {},
        "auto_reject": False
    }

    # Check 1: Content exists and has minimum size
    content_path = f"{resource_path}/content.md"
    if not os.path.exists(content_path):
        results["checks"]["content_exists"] = False
        results["passed"] = False
        results["auto_reject"] = True
    else:
        size = os.path.getsize(content_path)
        results["checks"]["content_exists"] = True
        results["checks"]["content_size_kb"] = size / 1024
        if size < 1000:  # Less than 1KB
            results["checks"]["content_sufficient"] = False
            results["passed"] = False

    # Check 2: Metadata is valid JSON
    metadata_path = f"{resource_path}/metadata.json"
    try:
        with open(metadata_path) as f:
            metadata = json.load(f)
        results["checks"]["metadata_valid"] = True
    except:
        results["checks"]["metadata_valid"] = False
        results["passed"] = False

    # Check 3: Source URL is from allowed domain
    if "source_url" in metadata:
        domain = extract_domain(metadata["source_url"])
        config = load_config()
        if domain in config["domains"]["blocked"]:
            results["checks"]["domain_allowed"] = False
            results["auto_reject"] = True
        else:
            results["checks"]["domain_allowed"] = True

    # Check 4: Not a duplicate
    existing = check_duplicate(metadata.get("source_url", ""))
    results["checks"]["is_duplicate"] = existing is not None
    if existing:
        results["auto_reject"] = True

    return results
```

---

## Batch Processing

When multiple resources are in staging:

```markdown
# Quality Check Batch Report

## Batch Information
- **Batch ID**: BATCH_20260131_001
- **Timestamp**: 2026-01-31T14:30:00Z
- **Total Resources**: 9
- **Reviewer**: @quality_checker

---

## Summary

| Verdict | Count | Percentage |
|---------|-------|------------|
| APPROVED | 6 | 67% |
| CONDITIONAL | 2 | 22% |
| REJECTED | 1 | 11% |

---

## Results by Resource

| ID | Title | Score | Verdict | Key Issue |
|----|-------|-------|---------|-----------|
| WEB_001 | Network SIR Models | 8.5 | APPROVED | - |
| WEB_002 | Bayesian Tutorial | 7.2 | APPROVED | - |
| WEB_003 | Optimization Methods | 7.0 | APPROVED | - |
| WEB_004 | WHO Data Portal | 6.5 | CONDITIONAL | Incomplete data dictionary |
| WEB_005 | Blog Post Analysis | 5.8 | CONDITIONAL | No citations |
| WEB_006 | Unknown Blog | 3.8 | REJECTED | No credibility, low relevance |
...

---

## Actions Taken

1. **Migrated to active/**: WEB_001, WEB_002, WEB_003, WEB_004, WEB_005, WEB_007
2. **Added warnings**: WEB_004 (data incomplete), WEB_005 (verify claims)
3. **Moved to rejected/**: WEB_006

## Index Updated
- 8 new entries added
- Last updated: 2026-01-31T14:35:00Z
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Content extraction failed | Score Content Quality as 0, likely REJECTED |
| Metadata missing | Auto-reject, log error |
| Duplicate detected | Auto-reject with "DUPLICATE" reason |
| Blocked domain | Auto-reject with "BLOCKED_DOMAIN" reason |
| Score exactly 5.0 | Treat as CONDITIONAL (lower bound) |
| Reviewer uncertain | Default to lower score, add note |
