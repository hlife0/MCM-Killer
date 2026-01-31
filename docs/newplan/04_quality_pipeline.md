# Quality Checking Pipeline

> **Version**: 3.2.0
> **Purpose**: Define the quality validation workflow for external resources

---

## Pipeline Overview

```
┌─────────────────────┐
│ User drops files in │
│      inbox/         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ @resource_ingestor  │
│  processes to       │
│  staging/           │
│  + SHA-256 hash     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────┐
│                     QUALITY GATEWAY                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              @quality_checker                          │  │
│  │                                                        │  │
│  │  FOR CODE FILES (.py, .m, .cpp):                      │  │
│  │  ⚠️ SYNTAX CHECK FIRST (HARD CONSTRAINT)              │  │
│  │  If syntax fails → AUTO-REJECT (skip scoring)         │  │
│  │                                                        │  │
│  │  DOCUMENTS:                  CODE:                     │  │
│  │  1. Credibility (25%)       1. Credibility (15%)      │  │
│  │  2. Relevance (30%)         2. Relevance (25%)        │  │
│  │  3. Quality (25%)           3. Quality (20%)          │  │
│  │  4. Actionability (20%)     4. Actionability (40%)    │  │
│  │                                                        │  │
│  │  Total = Weighted Sum                                  │  │
│  └───────────────────────────────────────────────────────┘  │
└────────┬──────────────────┬──────────────────┬──────────────┘
         │                  │                  │
    >= 7.0             5.0-6.9              < 5.0 OR
    + syntax OK        + syntax OK          syntax FAIL
         │                  │                  │
         ▼                  ▼                  ▼
   ┌──────────┐      ┌──────────────┐    ┌──────────┐
   │ APPROVED │      │ CONDITIONAL  │    │ REJECTED │
   │ active/  │      │ active/      │    │ rejected/│
   │          │      │ (warnings)   │    │          │
   └──────────┘      └──────────────┘    └──────────┘
```

---

## Code Syntax Check (HARD CONSTRAINT)

**For code files (.py, .m, .cpp, .c, .java, .r, .jl), syntax must pass BEFORE scoring.**

```python
import ast
import subprocess

def check_syntax(filepath: str, language: str) -> tuple[bool, str]:
    """Check syntax of code file. Returns (passed, error_message)."""

    if language == "python":
        try:
            with open(filepath, encoding='utf-8') as f:
                ast.parse(f.read())
            return True, "Syntax OK"
        except SyntaxError as e:
            return False, f"Python SyntaxError: {e.msg} at line {e.lineno}"

    elif language == "matlab":
        # MATLAB syntax check via mlint if available
        try:
            result = subprocess.run(
                ["mlint", "-id", filepath],
                capture_output=True, text=True, timeout=30
            )
            if "Error" in result.stdout or result.returncode != 0:
                return False, f"MATLAB errors: {result.stdout[:200]}"
            return True, "MATLAB syntax OK"
        except FileNotFoundError:
            return True, "MATLAB mlint not available, syntax check skipped"

    elif language in ["cpp", "c"]:
        # C/C++ syntax check via gcc -fsyntax-only
        try:
            result = subprocess.run(
                ["gcc", "-fsyntax-only", filepath],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode != 0:
                return False, f"C/C++ errors: {result.stderr[:200]}"
            return True, "C/C++ syntax OK"
        except FileNotFoundError:
            return True, "GCC not available, syntax check skipped"

    else:
        return True, f"Syntax check not implemented for {language}"
```

**AUTO-REJECT on Syntax Failure**: If syntax check fails, resource is REJECTED without scoring.

---

## Scoring Weights

### Standard Weights (Documents)

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Source Credibility | 25% | Academic rigor, institutional backing |
| Content Relevance | 30% | Direct applicability to problem |
| Content Quality | 25% | Completeness, readability |
| Actionability | 20% | Practical utility |

### Code Weights (.py, .m, .cpp, etc.)

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Source Credibility | **15%** | Less important for code |
| Content Relevance | **25%** | Applicable to our problem |
| Content Quality | **20%** | Readability, documentation |
| **Actionability** | **40%** | **Can it run? Does it work?** |

**Rationale**: Code that doesn't run is useless regardless of other qualities.

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
def calculate_quality_score(scores: dict, is_code: bool = False) -> float:
    """Calculate weighted quality score based on resource type."""

    # Select weights based on resource type
    if is_code:
        weights = {
            "credibility": 0.15,
            "relevance": 0.25,
            "quality": 0.20,
            "actionability": 0.40
        }
    else:
        weights = {
            "credibility": 0.25,
            "relevance": 0.30,
            "quality": 0.25,
            "actionability": 0.20
        }

    total = sum(scores[k] * weights[k] for k in weights)
    return round(total, 1)

# Example - Document
doc_scores = {
    "credibility": 8,      # arXiv preprint
    "relevance": 9,        # directly addresses our approach
    "quality": 7,          # good extraction, minor issues
    "actionability": 8     # clear methodology
}
# = (8 * 0.25) + (9 * 0.30) + (7 * 0.25) + (8 * 0.20)
# = 2.0 + 2.7 + 1.75 + 1.6 = 8.05 → APPROVED

# Example - Code
code_scores = {
    "credibility": 7,      # GitHub repo
    "relevance": 9,        # directly applicable
    "quality": 8,          # well-documented
    "actionability": 9     # runs, has tests
}
# = (7 * 0.15) + (9 * 0.25) + (8 * 0.20) + (9 * 0.40)
# = 1.05 + 2.25 + 1.6 + 3.6 = 8.5 → APPROVED
```

---

## Threshold Decisions

| Score Range | Verdict | Action | Notification |
|-------------|---------|--------|--------------|
| **>= 7.0** + syntax OK | APPROVED | Migrate to `active/` | "Resource approved and available" |
| **5.0 - 6.9** + syntax OK | CONDITIONAL | Migrate with warnings | "Resource approved with cautions" |
| **< 5.0** | REJECTED | Move to `rejected/` | "Resource rejected, see reasons" |
| **Syntax FAIL** | **AUTO-REJECT** | Move to `rejected/` | "SYNTAX FAILURE: {error}" |

**Code Hard Constraint**: Syntax failure = AUTO-REJECT regardless of other scores.

---

## Quality Report Format

Each reviewed resource gets a quality report:

### Document Report Example

```markdown
# Quality Report: MAN_20260131_abc123

## Resource Information
- **Title**: Network-Based SIR Models for Epidemic Prediction
- **Source**: local://inbox/network_sir.md
- **Type**: Document
- **Reviewed By**: @quality_checker
- **Review Date**: 2026-01-31T14:00:00Z

---

## Scoring (Document Weights)

| Criterion | Weight | Raw Score | Weighted | Justification |
|-----------|--------|-----------|----------|---------------|
| Source Credibility | 25% | 8/10 | 2.00 | arXiv preprint, known research group |
| Content Relevance | 30% | 9/10 | 2.70 | Directly addresses our SIR-Network approach |
| Content Quality | 25% | 7/10 | 1.75 | Good extraction, minor LaTeX rendering issues |
| Actionability | 20% | 8/10 | 1.60 | Includes Python pseudocode, clear steps |

## **Total Score: 8.05/10**

---

## Verdict: ✅ APPROVED
```

### Code Report Example

```markdown
# Quality Report: MAN_20260131_def456

## Resource Information
- **Title**: bayesian_sir_model
- **Source**: local://inbox/bayesian_sir_model.py
- **Type**: Code (Python)
- **Reviewed By**: @quality_checker
- **Review Date**: 2026-01-31T14:00:00Z

---

## Syntax Check (HARD CONSTRAINT)
- **Status**: ✅ PASSED
- **Message**: Python syntax OK

---

## Scoring (Code Weights - 40% Actionability)

| Criterion | Weight | Raw Score | Weighted | Justification |
|-----------|--------|-----------|----------|---------------|
| Source Credibility | 15% | 7/10 | 1.05 | User-provided, assumed relevant |
| Content Relevance | 25% | 9/10 | 2.25 | Directly applicable to our model |
| Content Quality | 20% | 8/10 | 1.60 | Well-documented, has docstrings |
| Actionability | 40% | 9/10 | 3.60 | Runs, has main entry point, imports work |

## **Total Score: 8.5/10**

---

## Verdict: ✅ APPROVED

---

## Code Analysis
- **Lines**: 245
- **Functions**: fit_model, predict, plot_results, validate
- **Imports**: numpy, scipy, pymc
- **Has Entry Point**: Yes (if __name__ == "__main__")
```

### Syntax Failure Report Example

```markdown
# Quality Report: MAN_20260131_xyz789

## Resource Information
- **Title**: broken_model
- **Source**: local://inbox/broken_model.py
- **Type**: Code (Python)
- **Reviewed By**: @quality_checker
- **Review Date**: 2026-01-31T14:00:00Z

---

## Syntax Check (HARD CONSTRAINT)
- **Status**: ❌ FAILED
- **Message**: SyntaxError: invalid syntax at line 45

---

## Scoring
**SKIPPED** - Syntax check failed (auto-reject)

---

## Verdict: ❌ REJECTED (SYNTAX FAILURE)

---

## Required Fix
Fix syntax error at line 45 before resubmitting.
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
| **Syntax check fails (code)** | **Auto-reject, skip scoring, log error** |
| Content extraction failed | Score Content Quality as 0, likely REJECTED |
| Metadata missing | Auto-reject, log error |
| Duplicate detected | Auto-reject with "DUPLICATE" reason |
| Blocked domain | Auto-reject with "BLOCKED_DOMAIN" reason |
| Score exactly 5.0 | Treat as CONDITIONAL (lower bound) |
| Reviewer uncertain | Default to lower score, add note |
| Empty file | Generate warning, score quality as 0 |
| Encoding error | Try UTF-8, then latin-1, then reject |
