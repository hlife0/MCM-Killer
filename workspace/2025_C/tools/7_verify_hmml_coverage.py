#!/usr/bin/env python3
"""Verify HMML 2.0 coverage against original HMML.json.

- Reads HMML.json tree from clean source
- Reads canonical knowledge_library/hmml_summary.json
- Compares leaf method name coverage with simple normalization
- Prints a short report and exits with code 0 always (informational).
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

ROOT = Path(__file__).resolve().parents[1]
LIB_ROOT = ROOT / "knowledge_library"
SUMMARY_PATH = LIB_ROOT / "hmml_summary.json"
HMML_JSON_PATH = Path(r"D:\\migration\\clean version\\LLM-MM-Agent\\MMAgent\\HMML\\HMML.json")


def normalize_name(name: str) -> str:
    s = name.strip().lower()
    # Strip trailing punctuation and colons
    while s and s[-1] in ":：;。.!？?":
        s = s[:-1]
    # Collapse whitespace
    s = " ".join(s.split())
    return s


def collect_json_leaves(node: Dict, prefix: Tuple[str, ...] = ()) -> List[Tuple[str, str]]:
    leaves: List[Tuple[str, str]] = []
    if "children" in node:
        cls = node.get("method_class")
        new_prefix = prefix + (cls,) if cls else prefix
        for child in node["children"]:
            leaves.extend(collect_json_leaves(child, new_prefix))
    elif "method" in node:
        full_name = node["method"]
        leaves.append((" / ".join(prefix), full_name))
    return leaves


def main() -> None:
    if not HMML_JSON_PATH.exists():
        print(f"[WARN] HMML.json not found at {HMML_JSON_PATH}")
        sys.exit(0)
    if not SUMMARY_PATH.exists():
        print(f"[WARN] hmml_summary.json not found at {SUMMARY_PATH}")
        sys.exit(0)

    hmml_data = json.loads(HMML_JSON_PATH.read_text(encoding="utf-8"))
    # Root is a list of top-level method_class objects
    json_leaves: List[Tuple[str, str]] = []
    if isinstance(hmml_data, list):
        for root in hmml_data:
            json_leaves.extend(collect_json_leaves(root))
    else:
        json_leaves.extend(collect_json_leaves(hmml_data))

    json_norm: Set[str] = {normalize_name(name) for (_, name) in json_leaves}

    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    lib_norm: Set[str] = {normalize_name(m["name"]) for m in summary.get("methods", [])}

    missing = sorted(json_norm - lib_norm)
    extra = sorted(lib_norm - json_norm)

    print("HMML Coverage Report")
    print("====================")
    print(f"Total HMML.json leaves: {len(json_norm)}")
    print(f"Total library methods:  {len(lib_norm)}")
    print(f"Missing in library:     {len(missing)}")
    print(f"Extra in library:       {len(extra)}")
    print("")

    if missing:
        print("Sample missing methods (up to 20):")
        for name in missing[:20]:
            print(f"  - {name}")
        print("")

    if extra:
        print("Sample extra methods (up to 20):")
        for name in extra[:20]:
            print(f"  - {name}")
        print("")


if __name__ == "__main__":
    main()
