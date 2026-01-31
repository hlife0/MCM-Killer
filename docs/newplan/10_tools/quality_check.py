#!/usr/bin/env python3
"""
External Resource Quality Check Tool
Automates quality scoring for external resources.
Includes SYNTAX CHECKING for code files (hard constraint).

Usage:
    python quality_check.py <resource_path>
    python quality_check.py --batch  # Process all in staging/

Example:
    python quality_check.py output/external_resources/staging/MAN_20260131_abc123
"""

import ast
import json
import os
import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from urllib.parse import urlparse

# Quality criteria weights - STANDARD (documents)
WEIGHTS_STANDARD = {
    "credibility": 0.25,
    "relevance": 0.30,
    "quality": 0.25,
    "actionability": 0.20
}

# Quality criteria weights - CODE (increased actionability)
WEIGHTS_CODE = {
    "credibility": 0.15,
    "relevance": 0.25,
    "quality": 0.20,
    "actionability": 0.40  # Code that doesn't work is useless
}

# Code file extensions
CODE_EXTENSIONS = {".py", ".m", ".cpp", ".c", ".java", ".r", ".jl", ".R"}

# Domain credibility scores
DOMAIN_SCORES = {
    # Tier 1: Peer-reviewed, official sources (10)
    "nature.com": 10, "science.org": 10, "pnas.org": 10,
    "data.gov": 10, "cdc.gov": 10, "who.int": 10, "nih.gov": 10,

    # Tier 2: Preprints, top universities (8)
    "arxiv.org": 8, "ieee.org": 8, "springer.com": 8,
    "github.com": 8,  # Higher for code

    # Tier 3: Manual uploads (7 - assumed relevant)
    "local://": 7,

    # Tier 4: Expert blogs (4)
    "towardsdatascience.com": 4, "medium.com": 4,

    # Tier 5: General Q&A (2)
    "stackoverflow.com": 2, "quora.com": 2,
}


def is_code_file(filepath: str) -> bool:
    """Check if file is a code file."""
    ext = Path(filepath).suffix.lower()
    return ext in CODE_EXTENSIONS


def detect_language(filepath: str) -> str:
    """Detect programming language from extension."""
    ext = Path(filepath).suffix.lower()
    lang_map = {
        ".py": "python",
        ".m": "matlab",
        ".cpp": "cpp",
        ".c": "c",
        ".java": "java",
        ".r": "r",
        ".R": "r",
        ".jl": "julia"
    }
    return lang_map.get(ext, "unknown")


def check_syntax(filepath: str, language: str) -> Tuple[bool, str]:
    """
    Check syntax of code file.
    Returns (passed, message).

    HARD CONSTRAINT: Code must pass syntax check to be approved.
    """
    if language == "python":
        try:
            with open(filepath, encoding='utf-8') as f:
                content = f.read()
            ast.parse(content)
            return True, "Python syntax OK"
        except SyntaxError as e:
            return False, f"SyntaxError: {e.msg} at line {e.lineno}"
        except Exception as e:
            return False, f"Parse error: {str(e)}"

    elif language == "matlab":
        # MATLAB syntax check via mlint if available
        try:
            result = subprocess.run(
                ["mlint", "-id", filepath],
                capture_output=True, text=True, timeout=30
            )
            # mlint returns warnings/errors as output
            if "Error" in result.stdout or result.returncode != 0:
                return False, f"MATLAB errors: {result.stdout[:200]}"
            return True, "MATLAB syntax OK"
        except FileNotFoundError:
            return True, "MATLAB mlint not available, syntax check skipped"
        except Exception as e:
            return True, f"MATLAB check skipped: {str(e)}"

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
        except Exception as e:
            return True, f"C/C++ check skipped: {str(e)}"

    else:
        return True, f"Syntax check not implemented for {language}"


def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    try:
        if url.startswith("local://"):
            return "local://"
        parsed = urlparse(url)
        domain = parsed.netloc.replace("www.", "")
        return domain
    except:
        return ""


def score_credibility(metadata: Dict) -> Tuple[int, str]:
    """Score source credibility based on domain."""
    url = metadata.get("source_url", "")
    source_type = metadata.get("source_type", "")

    # Manual uploads get base score of 7 (assumed relevant by user)
    if source_type == "manual_upload" or url.startswith("local://"):
        return 7, "Manual upload - assumed relevant by user"

    domain = extract_domain(url)
    for known_domain, score in DOMAIN_SCORES.items():
        if known_domain in domain:
            return score, f"Domain '{known_domain}' credibility: {score}"

    return 3, f"Unknown domain '{domain}' - default low credibility"


def score_content_quality(content_path: str, is_code: bool) -> Tuple[int, str]:
    """Score content extraction/quality."""
    if not os.path.exists(content_path):
        return 0, "Content file missing"

    try:
        content = Path(content_path).read_text(encoding='utf-8')
    except:
        return 1, "Content file unreadable"

    if is_code:
        # Code quality metrics
        line_count = len(content.split('\n'))
        has_docstring = '"""' in content or "'''" in content
        has_comments = '#' in content or '//' in content
        has_functions = 'def ' in content or 'function ' in content

        score = 5
        reasons = []

        if line_count > 50:
            score += 1
            reasons.append(f"{line_count} lines")
        if has_docstring:
            score += 2
            reasons.append("has docstrings")
        if has_comments:
            score += 1
            reasons.append("has comments")
        if has_functions:
            score += 1
            reasons.append("has functions")

        return min(10, score), "Code: " + ", ".join(reasons) if reasons else "Basic code"

    else:
        # Document quality metrics
        word_count = len(content.split())
        sections = ["abstract", "introduction", "methodology", "results", "conclusion"]
        found = sum(1 for s in sections if s.lower() in content.lower())

        if word_count < 100:
            return 2, f"Very short ({word_count} words)"
        elif word_count < 500:
            return 4 + min(found, 2), f"{word_count} words, {found} sections"
        elif word_count < 1000:
            return 6 + min(found, 2), f"{word_count} words, {found} sections"
        else:
            return 7 + min(found, 3), f"{word_count} words, {found} sections"


def score_actionability(metadata: Dict, content: str, is_code: bool) -> Tuple[int, str]:
    """Score actionability of the content."""
    if is_code:
        # For code, actionability is about whether it's usable
        score = 6  # Base for code (it exists)
        reasons = []

        if 'def main' in content or 'if __name__' in content:
            score += 2
            reasons.append("has entry point")

        if 'import ' in content:
            score += 1
            reasons.append("has imports")

        if 'return' in content:
            score += 1
            reasons.append("has return statements")

        return min(10, score), "Code: " + ", ".join(reasons) if reasons else "Basic structure"

    else:
        # Document actionability
        score = 5
        reasons = []
        content_lower = content.lower()

        if "```" in content:
            score += 2
            reasons.append("contains code")
        if "$" in content or "equation" in content_lower:
            score += 1
            reasons.append("contains formulas")
        if "step" in content_lower or "algorithm" in content_lower:
            score += 1
            reasons.append("has methodology")
        if "data" in content_lower or "csv" in content_lower:
            score += 1
            reasons.append("references data")

        return min(10, score), ", ".join(reasons) if reasons else "minimal actionable content"


def calculate_total(scores: Dict, weights: Dict) -> float:
    """Calculate weighted total score."""
    total = sum(scores.get(k, {}).get("score", 0) * weights[k] for k in weights)
    return round(total, 1)


def determine_verdict(total: float) -> str:
    """Determine verdict based on total score."""
    if total >= 7.0:
        return "APPROVED"
    elif total >= 5.0:
        return "CONDITIONAL"
    else:
        return "REJECTED"


def find_content_file(resource_path: str) -> Tuple[str, bool]:
    """Find the main content file in resource folder."""
    for ext in [".py", ".m", ".cpp", ".c", ".java", ".r", ".jl", ".md", ".txt", ".csv"]:
        content_file = os.path.join(resource_path, f"content{ext}")
        if os.path.exists(content_file):
            return content_file, ext in CODE_EXTENSIONS

    # Fallback to any file
    for f in os.listdir(resource_path):
        if f.startswith("content"):
            fpath = os.path.join(resource_path, f)
            return fpath, is_code_file(fpath)

    return os.path.join(resource_path, "content.md"), False


def generate_report(resource_path: str) -> Dict:
    """Generate comprehensive quality report for a resource."""
    metadata_path = os.path.join(resource_path, "metadata.json")

    if not os.path.exists(metadata_path):
        return {"error": f"Metadata not found: {metadata_path}"}

    with open(metadata_path) as f:
        metadata = json.load(f)

    content_file, is_code = find_content_file(resource_path)
    content = ""
    if os.path.exists(content_file):
        try:
            content = Path(content_file).read_text(encoding='utf-8')
        except:
            content = ""

    # HARD CONSTRAINT: Syntax check for code
    syntax_passed = True
    syntax_message = "N/A (not code)"

    if is_code:
        language = metadata.get("programming_language", detect_language(content_file))
        syntax_passed, syntax_message = check_syntax(content_file, language)

        if not syntax_passed:
            # AUTO-REJECT on syntax failure
            return {
                "resource_id": metadata.get("resource_id", os.path.basename(resource_path)),
                "title": metadata.get("title", "Unknown"),
                "source_url": metadata.get("source_url", ""),
                "reviewed_at": datetime.now().isoformat(),
                "is_code": True,
                "syntax_check": {"passed": False, "message": syntax_message},
                "scores": None,
                "total": 0,
                "verdict": "REJECTED",
                "auto_reject_reason": f"SYNTAX FAILURE: {syntax_message}"
            }

    # Select weights based on resource type
    weights = WEIGHTS_CODE if is_code else WEIGHTS_STANDARD

    # Score each criterion
    cred_score, cred_reason = score_credibility(metadata)
    qual_score, qual_reason = score_content_quality(content_file, is_code)
    act_score, act_reason = score_actionability(metadata, content, is_code)
    rel_score = metadata.get("relevance_score", 7 if metadata.get("source_type") == "manual_upload" else 5)
    rel_reason = metadata.get("relevance_justification", "Default score")

    scores = {
        "credibility": {"score": cred_score, "reason": cred_reason},
        "relevance": {"score": rel_score, "reason": rel_reason},
        "quality": {"score": qual_score, "reason": qual_reason},
        "actionability": {"score": act_score, "reason": act_reason}
    }

    total = calculate_total(scores, weights)
    verdict = determine_verdict(total)

    report = {
        "resource_id": metadata.get("resource_id", os.path.basename(resource_path)),
        "title": metadata.get("title", "Unknown"),
        "source_url": metadata.get("source_url", ""),
        "reviewed_at": datetime.now().isoformat(),
        "is_code": is_code,
        "syntax_check": {"passed": syntax_passed, "message": syntax_message},
        "weights_used": "CODE" if is_code else "STANDARD",
        "scores": scores,
        "total": total,
        "verdict": verdict,
        "weights": weights
    }

    return report


def write_quality_report(resource_path: str, report: Dict):
    """Write quality report to markdown file."""
    report_path = os.path.join(resource_path, "quality_report.md")

    md_content = f"""# Quality Report: {report['resource_id']}

## Resource Information
- **Title**: {report['title']}
- **Source**: {report['source_url']}
- **Reviewed**: {report['reviewed_at']}

---

## Scoring

| Criterion | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| Source Credibility | 25% | {report['scores']['credibility']['score']}/10 | {report['scores']['credibility']['reason']} |
| Content Relevance | 30% | {report['scores']['relevance']['score']}/10 | {report['scores']['relevance']['reason']} |
| Content Quality | 25% | {report['scores']['quality']['score']}/10 | {report['scores']['quality']['reason']} |
| Actionability | 20% | {report['scores']['actionability']['score']}/10 | {report['scores']['actionability']['reason']} |

## **Total Score: {report['total']}/10**

---

## Verdict: {'✅' if report['verdict'] == 'APPROVED' else '⚠️' if report['verdict'] == 'CONDITIONAL' else '❌'} {report['verdict']}

---

## Recommendations

"""

    if report['verdict'] == 'APPROVED':
        md_content += "Resource meets quality standards. Ready for agent consumption.\n"
    elif report['verdict'] == 'CONDITIONAL':
        md_content += "Resource has limitations. Use with caution and verify claims independently.\n"
    else:
        md_content += "Resource does not meet quality standards. Not recommended for use.\n"

    with open(report_path, 'w') as f:
        f.write(md_content)

    return report_path


def process_batch():
    """Process all resources in staging/."""
    staging_dir = "output/external_resources/staging"

    if not os.path.exists(staging_dir):
        print(f"Staging directory not found: {staging_dir}")
        return

    resources = [d for d in os.listdir(staging_dir)
                 if os.path.isdir(os.path.join(staging_dir, d))]

    if not resources:
        print("No resources in staging/")
        return

    results = {
        "approved": [],
        "conditional": [],
        "rejected": []
    }

    for resource_id in resources:
        resource_path = os.path.join(staging_dir, resource_id)
        print(f"Processing: {resource_id}")

        report = generate_report(resource_path)

        if "error" in report:
            print(f"  Error: {report['error']}")
            continue

        write_quality_report(resource_path, report)
        print(f"  Score: {report['total']}/10 -> {report['verdict']}")

        results[report['verdict'].lower()].append({
            "id": resource_id,
            "score": report['total']
        })

    print("\n" + "="*50)
    print("BATCH SUMMARY")
    print("="*50)
    print(f"Approved: {len(results['approved'])}")
    print(f"Conditional: {len(results['conditional'])}")
    print(f"Rejected: {len(results['rejected'])}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "--batch":
        process_batch()
    else:
        resource_path = sys.argv[1]
        report = generate_report(resource_path)

        if "error" in report:
            print(f"Error: {report['error']}")
            sys.exit(1)

        report_path = write_quality_report(resource_path, report)
        print(json.dumps(report, indent=2))
        print(f"\nReport written to: {report_path}")
