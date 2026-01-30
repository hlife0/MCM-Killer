#!/usr/bin/env python3
"""Build canonical HMML 2.0 index and summary for knowledge_library.

- Scans knowledge_library/methods/**.md
- Parses YAML front matter for metadata
- Emits:
  - knowledge_library/hmml_summary.json
  - knowledge_library/index.md

Paths in summary use `methods/...` relative to knowledge_library root.
"""

import json
from pathlib import Path
from typing import Any, Dict, List

import yaml

ROOT = Path(__file__).resolve().parents[1] / "knowledge_library"
METHODS_ROOT = ROOT / "methods"
SUMMARY_PATH = ROOT / "hmml_summary.json"
INDEX_PATH = ROOT / "index.md"


def load_front_matter(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    fm_text = parts[1]
    return yaml.safe_load(fm_text) or {}


def main() -> None:
    methods: List[Dict[str, Any]] = []
    domains: Dict[str, int] = {}
    by_complexity: Dict[str, int] = {}
    by_narrative: Dict[str, int] = {}

    for md_path in METHODS_ROOT.rglob("*.md"):
        # Skip local index or helper files inside methods tree
        if md_path.name in {"index.md"}:
            continue

        rel_from_root = md_path.relative_to(ROOT)
        if not str(rel_from_root).startswith("methods"):
            # We only catalog methods under methods/... by design
            rel_from_root = Path("methods") / md_path.relative_to(METHODS_ROOT)

        fm = load_front_matter(md_path)
        name = fm.get("method_name") or md_path.stem
        domain = fm.get("domain") or "unknown"
        sub = fm.get("sub_domain") or fm.get("subdomain") or "general"
        complexity = fm.get("complexity") or "Medium"
        narrative_value = fm.get("narrative_value") or "Medium"

        methods.append(
            {
                "name": str(name),
                "domain": str(domain),
                "subdomain": str(sub),
                "complexity": str(complexity),
                "narrative_value": str(narrative_value),
                "path": str(rel_from_root).replace("\\", "/"),
            }
        )

        domains[domain] = domains.get(domain, 0) + 1
        by_complexity[complexity] = by_complexity.get(complexity, 0) + 1
        by_narrative[narrative_value] = by_narrative.get(narrative_value, 0) + 1

    methods.sort(key=lambda m: (m["domain"], m["subdomain"], m["name"]))

    summary = {
        "version": "2.0",
        "generated": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "total_methods": len(methods),
        "domains": domains,
        "by_complexity": by_complexity,
        "by_narrative_value": by_narrative,
        "methods": [
            {
                "name": m["name"],
                "domain": m["domain"],
                "subdomain": m["subdomain"],
                "complexity": m["complexity"],
                "narrative_value": m["narrative_value"],
                "file": m["path"].replace("methods/", "")
                if m["path"].startswith("methods/")
                else m["path"],
            }
            for m in methods
        ],
    }

    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    # Build a simple Markdown index grouped by domain/subdomain
    lines: List[str] = []
    lines.append("# HMML 2.0 Method Index")
    lines.append("")
    lines.append("> **Version**: 2.0")
    lines.append(f"> **Total Methods**: {len(methods)}")
    lines.append("")
    lines.append("## Domain Summary")
    lines.append("")
    lines.append("| Domain | Count |")
    lines.append("|--------|-------|")
    for d, count in sorted(domains.items()):
        lines.append(f"| {d.replace('_', ' ').title()} | {count} |")
    lines.append("")

    # Group methods by domain/subdomain
    from collections import defaultdict

    grouped: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for m in methods:
        grouped[m["domain"]][m["subdomain"]].append(m)

    for domain in sorted(grouped.keys()):
        lines.append("")
        lines.append(f"## {domain.replace('_', ' ').title()}")
        lines.append("")
        for sub in sorted(grouped[domain].keys()):
            lines.append(f"### {sub.replace('_', ' ').title()}")
            lines.append("")
            lines.append("| Method | Complexity | Narrative Value |")
            lines.append("|--------|------------|-----------------|")
            for m in sorted(grouped[domain][sub], key=lambda x: x["name"]):
                link_path = m["path"]
                lines.append(
                    f"| [{m['name']}](" + link_path + f") | {m['complexity']} | {m['narrative_value']} |"
                )
            lines.append("")

    INDEX_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
