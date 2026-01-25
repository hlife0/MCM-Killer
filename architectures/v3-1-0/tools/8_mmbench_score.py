#!/usr/bin/env python3
"""
MMBench Score: Automated rule-based scoring for MCM/ICM papers.

Usage:
    python mmbench_score.py <workspace_path> <output_json>

Example:
    python mmbench_score.py workspace/2025_C/ benchmarks/run_report_20260124.json

This script:
1. Scans workspace for required deliverables
2. Checks paper quality against O-Prize standards
3. Applies rule-based deductions (no LLM required)
4. Generates a score (0-100) with detailed breakdown
5. Tracks trends across multiple runs (for Phase 11 evolution)

Scoring Criteria:
- Memo/Summary exists and has content
- Sensitivity analysis present
- Abstract contains numbers (≥3 required)
- Code is runnable (main.py or similar exists)
- Figures have conclusionary captions
- Uncertainty quantification present
- Concept diagrams exist (Mode B)

This tool is used in Phase 11 (Self-Evolution) for post-competition analysis.
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from collections import defaultdict


# ============================================================================
# SCORING CONFIGURATION
# ============================================================================

# Maximum score
MAX_SCORE = 100

# Scoring weights (must sum to 100)
SCORING_WEIGHTS = {
    "memo_exists": 10,
    "sensitivity_analysis": 15,
    "abstract_quality": 15,
    "code_runnable": 10,
    "uncertainty_quantification": 15,
    "figure_captions": 10,
    "concept_diagrams": 10,
    "narrative_arc": 10,
    "documentation": 5
}

# Minimum thresholds
THRESHOLDS = {
    "abstract_numbers_min": 3,
    "figure_caption_min_words": 10,
    "memo_min_words": 200
}


# ============================================================================
# FILE DETECTION PATTERNS
# ============================================================================

FILE_PATTERNS = {
    "memo": [
        "memo*.md", "memo*.tex", "summary*.md", "summary*.tex",
        "paper*.tex", "main*.tex", "paper.pdf"
    ],
    "sensitivity_analysis": [
        "sensitiv*", "robust*", "stability*", "parameter_sweep*"
    ],
    "code_main": [
        "main.py", "run.py", "train.py", "model*.py",
        "main.ipynb", "notebook*.ipynb"
    ],
    "figures": [
        "*.png", "*.jpg", "*.pdf", "*.svg"
    ],
    "mermaid": [
        "*.mmd", "*flowchart*", "*diagram*"
    ],
    "narrative_arc": [
        "narrative_arc*.md", "insight*.md"
    ],
    "dev_diary": [
        "dev_diary*.md", "diary*.md"
    ]
}


# ============================================================================
# CHECKER FUNCTIONS
# ============================================================================

def find_files(workspace: str, patterns: List[str]) -> List[str]:
    """Find files matching any of the given patterns."""
    matches = []

    for root, dirs, files in os.walk(workspace):
        for filename in files:
            for pattern in patterns:
                # Simple glob matching
                pattern_re = pattern.replace("*", ".*").replace("?", ".")
                if re.match(pattern_re, filename, re.IGNORECASE):
                    matches.append(os.path.join(root, filename))
                    break

    return matches


def check_memo_exists(workspace: str) -> Dict[str, Any]:
    """Check if memo/paper exists and has sufficient content."""

    result = {
        "check": "memo_exists",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["memo_exists"],
        "details": {}
    }

    # Find memo files
    memo_files = find_files(workspace, FILE_PATTERNS["memo"])

    if not memo_files:
        result["details"]["message"] = "No memo or paper file found"
        return result

    # Check content of first memo file
    memo_path = memo_files[0]
    result["details"]["file_found"] = memo_path

    try:
        if memo_path.endswith('.pdf'):
            # Can't easily check PDF content without dependencies
            result["passed"] = True
            result["score"] = result["max_score"]
            result["details"]["message"] = "PDF file exists (content not verified)"
        else:
            with open(memo_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            word_count = len(content.split())
            result["details"]["word_count"] = word_count

            if word_count >= THRESHOLDS["memo_min_words"]:
                result["passed"] = True
                result["score"] = result["max_score"]
                result["details"]["message"] = f"Memo has {word_count} words"
            else:
                result["score"] = int(result["max_score"] * word_count / THRESHOLDS["memo_min_words"])
                result["details"]["message"] = f"Memo too short ({word_count} < {THRESHOLDS['memo_min_words']} words)"

    except Exception as e:
        result["details"]["error"] = str(e)

    return result


def check_sensitivity_analysis(workspace: str) -> Dict[str, Any]:
    """Check if sensitivity analysis is present."""

    result = {
        "check": "sensitivity_analysis",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["sensitivity_analysis"],
        "details": {}
    }

    # Find sensitivity files
    sens_files = find_files(workspace, FILE_PATTERNS["sensitivity_analysis"])

    if sens_files:
        result["passed"] = True
        result["score"] = result["max_score"]
        result["details"]["files_found"] = sens_files[:3]
        result["details"]["message"] = f"Found {len(sens_files)} sensitivity-related files"
        return result

    # Also check paper content for sensitivity section
    memo_files = find_files(workspace, FILE_PATTERNS["memo"])

    for memo_path in memo_files:
        if memo_path.endswith('.pdf'):
            continue

        try:
            with open(memo_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()

            if any(kw in content for kw in ["sensitivity analysis", "robustness check", "parameter sweep"]):
                result["passed"] = True
                result["score"] = result["max_score"]
                result["details"]["message"] = "Sensitivity analysis section found in paper"
                return result

        except Exception:
            pass

    result["details"]["message"] = "No sensitivity analysis found - FATAL for O-Prize"
    return result


def check_abstract_quality(workspace: str) -> Dict[str, Any]:
    """Check abstract contains sufficient numbers."""

    result = {
        "check": "abstract_quality",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["abstract_quality"],
        "details": {}
    }

    # Find paper files
    memo_files = find_files(workspace, FILE_PATTERNS["memo"])

    for memo_path in memo_files:
        if memo_path.endswith('.pdf'):
            continue

        try:
            with open(memo_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Try to find abstract section
            abstract_match = re.search(
                r'(?:abstract|summary)[\s:]*\n*(.*?)(?:\n\n|introduction|keywords|\\section)',
                content,
                re.IGNORECASE | re.DOTALL
            )

            if abstract_match:
                abstract = abstract_match.group(1)[:1500]
                result["details"]["abstract_length"] = len(abstract)

                # Count numbers
                numbers = re.findall(r'\d+\.?\d*', abstract)
                # Count percentages
                percentages = re.findall(r'\d+\.?\d*\s*%', abstract)
                # Count p-values
                pvalues = re.findall(r'p\s*[<>]\s*0\.\d+', abstract, re.IGNORECASE)

                total_quant = len(numbers)
                result["details"]["numbers_found"] = total_quant
                result["details"]["percentages_found"] = len(percentages)
                result["details"]["pvalues_found"] = len(pvalues)

                if total_quant >= THRESHOLDS["abstract_numbers_min"]:
                    result["passed"] = True
                    result["score"] = result["max_score"]
                    result["details"]["message"] = f"Abstract has {total_quant} numbers (good)"
                else:
                    # Partial credit
                    result["score"] = int(result["max_score"] * total_quant / THRESHOLDS["abstract_numbers_min"])
                    result["details"]["message"] = f"Abstract has {total_quant} numbers (need ≥{THRESHOLDS['abstract_numbers_min']})"

                return result

        except Exception as e:
            result["details"]["error"] = str(e)

    result["details"]["message"] = "Could not find or parse abstract"
    return result


def check_code_runnable(workspace: str) -> Dict[str, Any]:
    """Check if main code file exists."""

    result = {
        "check": "code_runnable",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["code_runnable"],
        "details": {}
    }

    # Find code files
    code_files = find_files(workspace, FILE_PATTERNS["code_main"])

    if not code_files:
        result["details"]["message"] = "No main code file found"
        return result

    result["details"]["files_found"] = [os.path.basename(f) for f in code_files[:5]]

    # Check if any Python file is non-trivial
    for code_path in code_files:
        if code_path.endswith('.py'):
            try:
                with open(code_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()

                lines = len([l for l in content.split('\n') if l.strip() and not l.strip().startswith('#')])

                if lines > 20:
                    result["passed"] = True
                    result["score"] = result["max_score"]
                    result["details"]["message"] = f"Found {code_path} with {lines} lines"
                    return result

            except Exception:
                pass

    # At least files exist
    result["passed"] = True
    result["score"] = result["max_score"] // 2
    result["details"]["message"] = "Code files exist but may be minimal"
    return result


def check_uncertainty_quantification(workspace: str) -> Dict[str, Any]:
    """Check for uncertainty quantification in results."""

    result = {
        "check": "uncertainty_quantification",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["uncertainty_quantification"],
        "details": {}
    }

    # Find paper files
    memo_files = find_files(workspace, FILE_PATTERNS["memo"])

    uq_patterns = [
        r'confidence interval',
        r'95%?\s*CI',
        r'p\s*[<>]\s*0\.\d+',
        r'standard error',
        r'uncertainty',
        r'credible interval',
        r'bootstrap',
        r'±\s*\d',
        r'\(\s*\d+\.?\d*\s*[-–]\s*\d+\.?\d*\s*\)',  # Range notation
    ]

    for memo_path in memo_files:
        if memo_path.endswith('.pdf'):
            continue

        try:
            with open(memo_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower()

            matches = 0
            found_patterns = []

            for pattern in uq_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    matches += 1
                    found_patterns.append(pattern)

            if matches >= 3:
                result["passed"] = True
                result["score"] = result["max_score"]
                result["details"]["message"] = f"Found {matches} uncertainty quantification patterns"
                result["details"]["patterns"] = found_patterns[:5]
                return result
            elif matches > 0:
                result["score"] = int(result["max_score"] * matches / 3)
                result["details"]["message"] = f"Found {matches} patterns (need 3+)"
                result["details"]["patterns"] = found_patterns

        except Exception as e:
            result["details"]["error"] = str(e)

    result["details"]["message"] = "No uncertainty quantification found"
    return result


def check_figure_captions(workspace: str) -> Dict[str, Any]:
    """Check figure caption quality."""

    result = {
        "check": "figure_captions",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["figure_captions"],
        "details": {}
    }

    # Find paper files
    memo_files = find_files(workspace, FILE_PATTERNS["memo"])

    for memo_path in memo_files:
        if memo_path.endswith('.pdf'):
            continue

        try:
            with open(memo_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Find figure captions
            caption_pattern = re.compile(
                r'(?:figure|fig\.?)\s*\d+[:\.\s]+([^.]+\.)',
                re.IGNORECASE
            )

            captions = caption_pattern.findall(content)
            result["details"]["captions_found"] = len(captions)

            if not captions:
                result["details"]["message"] = "No figure captions found"
                return result

            # Check caption quality
            good_captions = 0
            conclusionary_markers = ["reveals", "demonstrates", "shows that", "indicating", "suggesting", "implies"]

            for caption in captions:
                words = len(caption.split())
                has_marker = any(m in caption.lower() for m in conclusionary_markers)

                if words >= THRESHOLDS["figure_caption_min_words"] and has_marker:
                    good_captions += 1

            result["details"]["good_captions"] = good_captions
            quality_ratio = good_captions / len(captions) if captions else 0

            if quality_ratio >= 0.7:
                result["passed"] = True
                result["score"] = result["max_score"]
                result["details"]["message"] = f"{good_captions}/{len(captions)} captions are conclusionary"
            else:
                result["score"] = int(result["max_score"] * quality_ratio)
                result["details"]["message"] = f"Only {good_captions}/{len(captions)} captions are conclusionary"

            return result

        except Exception as e:
            result["details"]["error"] = str(e)

    result["details"]["message"] = "Could not analyze figure captions"
    return result


def check_concept_diagrams(workspace: str) -> Dict[str, Any]:
    """Check for concept diagrams (Mode B visualization)."""

    result = {
        "check": "concept_diagrams",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["concept_diagrams"],
        "details": {}
    }

    # Find mermaid/diagram files
    diagram_files = find_files(workspace, FILE_PATTERNS["mermaid"])

    if diagram_files:
        result["passed"] = True
        result["score"] = result["max_score"]
        result["details"]["files_found"] = [os.path.basename(f) for f in diagram_files[:5]]
        result["details"]["message"] = f"Found {len(diagram_files)} concept diagram files"
        return result

    # Also check figures directory for flowcharts
    figure_files = find_files(workspace, FILE_PATTERNS["figures"])
    flowchart_figs = [f for f in figure_files if any(kw in f.lower() for kw in ["flow", "diagram", "concept", "architecture"])]

    if flowchart_figs:
        result["passed"] = True
        result["score"] = result["max_score"]
        result["details"]["files_found"] = [os.path.basename(f) for f in flowchart_figs[:5]]
        result["details"]["message"] = f"Found {len(flowchart_figs)} concept diagram figures"
        return result

    result["details"]["message"] = "No concept diagrams found (Mode B visualization missing)"
    return result


def check_narrative_arc(workspace: str) -> Dict[str, Any]:
    """Check for narrative arc documentation."""

    result = {
        "check": "narrative_arc",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["narrative_arc"],
        "details": {}
    }

    # Find narrative arc files
    arc_files = find_files(workspace, FILE_PATTERNS["narrative_arc"])
    diary_files = find_files(workspace, FILE_PATTERNS["dev_diary"])

    if arc_files:
        result["passed"] = True
        result["score"] = result["max_score"]
        result["details"]["files_found"] = [os.path.basename(f) for f in arc_files[:3]]
        result["details"]["message"] = "Narrative arc documentation found"
        return result

    if diary_files:
        result["passed"] = True
        result["score"] = result["max_score"] // 2
        result["details"]["files_found"] = [os.path.basename(f) for f in diary_files[:3]]
        result["details"]["message"] = "Dev diary found (partial narrative)"
        return result

    result["details"]["message"] = "No narrative arc or dev diary found"
    return result


def check_documentation(workspace: str) -> Dict[str, Any]:
    """Check for general documentation quality."""

    result = {
        "check": "documentation",
        "passed": False,
        "score": 0,
        "max_score": SCORING_WEIGHTS["documentation"],
        "details": {}
    }

    # Check for README
    readme_files = find_files(workspace, ["README.md", "README.txt"])

    # Check for requirements
    req_files = find_files(workspace, ["requirements.txt", "environment.yml", "Pipfile"])

    # Check for VERSION_MANIFEST
    manifest_files = find_files(workspace, ["VERSION_MANIFEST.json", "manifest.json"])

    docs_found = 0
    doc_list = []

    if readme_files:
        docs_found += 1
        doc_list.append("README")

    if req_files:
        docs_found += 1
        doc_list.append("requirements")

    if manifest_files:
        docs_found += 1
        doc_list.append("manifest")

    result["details"]["docs_found"] = doc_list

    if docs_found >= 2:
        result["passed"] = True
        result["score"] = result["max_score"]
        result["details"]["message"] = "Good documentation coverage"
    elif docs_found == 1:
        result["score"] = result["max_score"] // 2
        result["details"]["message"] = "Partial documentation"
    else:
        result["details"]["message"] = "Missing documentation files"

    return result


# ============================================================================
# MAIN SCORING FUNCTION
# ============================================================================

def score_workspace(workspace: str) -> Dict[str, Any]:
    """Score a workspace and return comprehensive report."""

    report = {
        "meta": {
            "workspace": workspace,
            "generated": datetime.now().isoformat(),
            "version": "1.0",
            "max_score": MAX_SCORE
        },
        "score": 0,
        "passed": False,
        "checks": [],
        "summary": {},
        "deductions": [],
        "recommendations": []
    }

    # Run all checks
    checkers = [
        check_memo_exists,
        check_sensitivity_analysis,
        check_abstract_quality,
        check_code_runnable,
        check_uncertainty_quantification,
        check_figure_captions,
        check_concept_diagrams,
        check_narrative_arc,
        check_documentation
    ]

    total_score = 0

    for checker in checkers:
        result = checker(workspace)
        report["checks"].append(result)
        total_score += result["score"]

        if not result["passed"]:
            deduction = result["max_score"] - result["score"]
            if deduction > 0:
                report["deductions"].append({
                    "check": result["check"],
                    "deduction": deduction,
                    "message": result["details"].get("message", "Check failed")
                })

    report["score"] = total_score
    report["passed"] = total_score >= 95

    # Generate summary
    passed_checks = sum(1 for c in report["checks"] if c["passed"])
    total_checks = len(report["checks"])

    report["summary"] = {
        "score": total_score,
        "grade": get_grade(total_score),
        "checks_passed": f"{passed_checks}/{total_checks}",
        "status": "PASS" if report["passed"] else "NEEDS IMPROVEMENT"
    }

    # Generate recommendations
    if not any(c["check"] == "sensitivity_analysis" and c["passed"] for c in report["checks"]):
        report["recommendations"].append({
            "priority": "HIGH",
            "issue": "Missing sensitivity analysis",
            "action": "Add parameter sweep or robustness check section"
        })

    if not any(c["check"] == "abstract_quality" and c["passed"] for c in report["checks"]):
        report["recommendations"].append({
            "priority": "HIGH",
            "issue": "Abstract lacks quantitative results",
            "action": "Add ≥3 numerical metrics (RMSE, percentages, p-values)"
        })

    if not any(c["check"] == "concept_diagrams" and c["passed"] for c in report["checks"]):
        report["recommendations"].append({
            "priority": "MEDIUM",
            "issue": "Missing concept diagrams",
            "action": "Add Mermaid flowcharts showing model architecture"
        })

    return report


def get_grade(score: int) -> str:
    """Convert score to letter grade."""
    if score >= 95:
        return "A (O-Prize Ready)"
    elif score >= 85:
        return "B (Strong Submission)"
    elif score >= 75:
        return "C (Acceptable)"
    elif score >= 65:
        return "D (Needs Work)"
    else:
        return "F (Major Issues)"


def load_previous_runs(benchmarks_dir: str) -> List[Dict]:
    """Load previous benchmark runs for trend analysis."""
    previous = []

    if not os.path.exists(benchmarks_dir):
        return previous

    for filename in os.listdir(benchmarks_dir):
        if filename.startswith("run_report_") and filename.endswith(".json"):
            filepath = os.path.join(benchmarks_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    previous.append({
                        "file": filename,
                        "date": data.get("meta", {}).get("generated", ""),
                        "score": data.get("score", 0)
                    })
            except Exception:
                pass

    return sorted(previous, key=lambda x: x["date"])


def calculate_trend(current_score: int, previous_runs: List[Dict]) -> Dict[str, Any]:
    """Calculate trend from previous runs."""
    if not previous_runs:
        return {
            "direction": "N/A",
            "change": 0,
            "message": "First run - no trend data"
        }

    last_score = previous_runs[-1]["score"]
    change = current_score - last_score

    if change > 0:
        direction = "improving"
        symbol = "↑"
    elif change < 0:
        direction = "declining"
        symbol = "↓"
    else:
        direction = "stable"
        symbol = "→"

    return {
        "direction": direction,
        "change": change,
        "symbol": symbol,
        "previous_score": last_score,
        "message": f"{symbol}{abs(change)} ({direction})"
    }


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main(workspace: str, output_path: str) -> None:
    """Main scoring pipeline."""

    print(f"\nMMBench Score - Phase 11 Scorer")
    print(f"=" * 40)
    print(f"Workspace: {workspace}")
    print(f"Output: {output_path}\n")

    # Check workspace exists
    if not os.path.exists(workspace):
        print(f"  Error: Workspace not found: {workspace}")
        sys.exit(1)

    # Score workspace
    print("Running checks...")
    report = score_workspace(workspace)

    # Load previous runs for trend
    benchmarks_dir = os.path.dirname(output_path)
    previous_runs = load_previous_runs(benchmarks_dir)
    report["trend"] = calculate_trend(report["score"], previous_runs)

    # Write output
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    # Print summary
    print(f"\n  Results:")
    print(f"  {'='*30}")
    print(f"  Score: {report['score']}/100")
    print(f"  Grade: {report['summary']['grade']}")
    print(f"  Status: {report['summary']['status']}")
    print(f"  Trend: {report['trend']['message']}")
    print(f"  {'='*30}")

    # Print deductions
    if report["deductions"]:
        print(f"\n  Deductions:")
        for d in report["deductions"][:5]:
            print(f"    - {d['check']}: -{d['deduction']} ({d['message'][:50]})")

    # Print recommendations
    if report["recommendations"]:
        print(f"\n  Recommendations:")
        for r in report["recommendations"][:3]:
            print(f"    [{r['priority']}] {r['issue']}")
            print(f"           → {r['action']}")

    print(f"\n  Report saved: {output_path}")
    print(f"\n  Done!")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python mmbench_score.py <workspace_path> <output_json>")
        print("")
        print("Example:")
        print("  python mmbench_score.py workspace/2025_C/ benchmarks/run_report_20260124.json")
        print("")
        print("Scoring Criteria:")
        for check, weight in SCORING_WEIGHTS.items():
            print(f"  - {check}: {weight} points")
        print(f"  Total: {sum(SCORING_WEIGHTS.values())} points")
        sys.exit(1)
