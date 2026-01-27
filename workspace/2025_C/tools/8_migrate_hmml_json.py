#!/usr/bin/env python3
"""HMML 2.0 JSON-driven migrator.

- Reads the canonical HMML.json tree from the clean source directory
- Regenerates the entire knowledge_library/methods tree from JSON leaves
- Uses the same metadata and Markdown structure as tools/5_migrate_hmml.py
- Does NOT build hmml_summary.json or index.md (run tools/6_build_hmml_index.py separately)

Usage (from workspace root):

    python tools/8_migrate_hmml_json.py

"""

from __future__ import annotations

import json
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime
from importlib import util as importlib_util
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
LIB_ROOT = ROOT / "knowledge_library"
METHODS_ROOT = LIB_ROOT / "methods"
HMML_JSON_PATH = Path(r"D:\\migration\\clean version\\LLM-MM-Agent\\MMAgent\\HMML\\HMML.json")
LEGACY_MIGRATOR_PATH = ROOT / "tools" / "5_migrate_hmml.py"


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class HMMLLeaf:
    """Single leaf method extracted from HMML.json."""

    qualified_classes: Tuple[str, ...]
    method_name: str
    description: str


# ---------------------------------------------------------------------------
# Legacy migrator loading (for shared helpers)
# ---------------------------------------------------------------------------

def load_legacy_migrator():
    """Load tools/5_migrate_hmml.py as a module.

    We reuse its classification helpers and Markdown generator so that
    JSON-driven methods match the existing HMML 2.0 method format.
    """

    if not LEGACY_MIGRATOR_PATH.exists():
        print(f"[ERROR] Legacy migrator not found at {LEGACY_MIGRATOR_PATH}", file=sys.stderr)
        sys.exit(1)

    spec = importlib_util.spec_from_file_location("hmml_legacy_migrator", LEGACY_MIGRATOR_PATH)
    if spec is None or spec.loader is None:
        print("[ERROR] Could not load legacy migrator module spec", file=sys.stderr)
        sys.exit(1)

    module = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[arg-type]
    return module


# ---------------------------------------------------------------------------
# HMML.json loading and traversal
# ---------------------------------------------------------------------------

def load_hmml_json() -> Any:
    """Load HMML.json from the canonical clean source path."""

    if not HMML_JSON_PATH.exists():
        print(f"[ERROR] HMML.json not found at {HMML_JSON_PATH}", file=sys.stderr)
        sys.exit(1)

    text = HMML_JSON_PATH.read_text(encoding="utf-8")
    return json.loads(text)


def _collect_leaves(node: Any, prefix: Tuple[str, ...], out: List[HMMLLeaf]) -> None:
    """Recursive helper to collect HMMLLeaf records from HMML.json."""

    if isinstance(node, dict):
        if "children" in node:
            cls = node.get("method_class")
            new_prefix = prefix + (str(cls),) if cls else prefix
            for child in node.get("children", []):
                _collect_leaves(child, new_prefix, out)
        elif "method" in node:
            method_name = str(node.get("method", "")).strip()
            desc_raw = node.get("description")
            description = str(desc_raw).strip() if desc_raw is not None else ""
            if not description:
                # Fallback template when description is missing
                description = (
                    f"<modeling_method>: {method_name}.\n"
                    "<core_idea>: [To be detailed].\n"
                    "<application>: [To be detailed]."
                )
            out.append(HMMLLeaf(prefix, method_name, description))
    elif isinstance(node, list):
        for child in node:
            _collect_leaves(child, prefix, out)


def collect_leaf_methods(hmml_root: Any) -> List[HMMLLeaf]:
    """Collect all HMMLLeaf records from the HMML.json root object."""

    leaves: List[HMMLLeaf] = []
    _collect_leaves(hmml_root, prefix=(), out=leaves)
    return leaves


# ---------------------------------------------------------------------------
# Methods tree reset
# ---------------------------------------------------------------------------

def reset_methods_tree() -> None:
    """Delete and recreate knowledge_library/methods.

    This treats HMML.json as the sole source of truth. The entire
    methods tree is regenerated, so existing contents are removed.
    """

    if METHODS_ROOT.exists():
        if METHODS_ROOT.name != "methods":
            print(f"[ERROR] Refusing to remove unexpected directory: {METHODS_ROOT}", file=sys.stderr)
            sys.exit(1)
        shutil.rmtree(METHODS_ROOT)

    METHODS_ROOT.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Per-method parsing and Markdown generation
# ---------------------------------------------------------------------------

def build_parsed_from_leaf(leaf: HMMLLeaf, legacy) -> Dict[str, Any]:
    """Build a "parsed" dict compatible with legacy generate_method_file()."""

    # Combine description and class context to help domain/subdomain inference
    class_context = " / ".join(leaf.qualified_classes)
    overview_lines = [leaf.description]
    if class_context:
        overview_lines.append("")
        overview_lines.append(f"HMML classes: {class_context}")

    full_content = "\n".join(overview_lines).strip()

    # Use legacy helpers for classification
    domain = legacy.infer_domain(full_content, leaf.method_name)
    subdomain = legacy.infer_subdomain(domain, full_content)
    complexity = legacy.estimate_complexity(full_content, leaf.method_name)
    narrative = legacy.assess_narrative_value(leaf.method_name, domain, full_content)
    pitfalls = legacy.extract_pitfalls(full_content, leaf.method_name)

    get_oprize_examples = getattr(legacy, "get_oprize_examples", None)
    if callable(get_oprize_examples):
        oprize = get_oprize_examples(domain, full_content)
    else:
        oprize = []

    # Tags: domain, subdomain, complexity + any class labels (slugified)
    base_tags: List[str] = [domain, subdomain, complexity.lower().replace(" ", "_")]
    for cls in leaf.qualified_classes:
        slug = legacy.slugify(str(cls))
        if slug and slug not in base_tags:
            base_tags.append(slug)

    metadata: Dict[str, Any] = {
        "method_name": leaf.method_name,
        "domain": domain,
        "sub_domain": subdomain or "general",
        "complexity": complexity,
        "narrative_value": narrative["level"],
        "narrative_reason": narrative["reason"],
        "common_pitfalls": [p["name"] for p in pitfalls],
        "oprize_examples": [e["competition"] for e in oprize],
        "tags": base_tags,
        "version": "2.0",
        "last_updated": datetime.utcnow().strftime("%Y-%m-%d"),
    }

    sections: Dict[str, str] = {"Overview": full_content}

    parsed: Dict[str, Any] = {
        "metadata": metadata,
        "sections": sections,
        "filename": legacy.slugify(leaf.method_name),
        "pitfalls_detail": pitfalls,
        "oprize_detail": oprize,
    }

    return parsed


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main() -> None:
    print("HMML 2.0 JSON-driven Migrator")
    print("=" * 40)
    print(f"Root:        {ROOT}")
    print(f"HMML JSON:   {HMML_JSON_PATH}")
    print(f"Methods dir: {METHODS_ROOT}\n")

    hmml_root = load_hmml_json()
    leaves = collect_leaf_methods(hmml_root)
    print(f"Discovered {len(leaves)} method leaves in HMML.json")

    if not leaves:
        print("[WARN] No leaf methods found in HMML.json; nothing to do.")
        return

    # Reset methods tree before regeneration
    print("\nResetting methods tree ...")
    reset_methods_tree()

    legacy = load_legacy_migrator()

    from collections import Counter

    domain_counts: Counter[str] = Counter()
    used_rel_paths: set[str] = set()
    collisions: List[Tuple[str, str, str]] = []

    for idx, leaf in enumerate(leaves, start=1):
        parsed = build_parsed_from_leaf(leaf, legacy)
        meta = parsed["metadata"]

        domain = str(meta["domain"])
        subdomain = str(meta.get("sub_domain") or "general")
        base_filename = str(parsed["filename"]) or legacy.slugify(leaf.method_name)

        # Ensure unique path per method (handle duplicate method names)
        rel_dir = Path("methods") / domain / subdomain
        candidate_name = base_filename
        rel_path_str = str(rel_dir / f"{candidate_name}.md")

        if rel_path_str in used_rel_paths:
            # Try suffix based on last class label, then numeric disambiguation
            suffix_parts: List[str] = []
            if leaf.qualified_classes:
                suffix_parts.append(legacy.slugify(leaf.qualified_classes[-1]))

            counter = 2
            while rel_path_str in used_rel_paths:
                pieces = [base_filename]
                if suffix_parts:
                    pieces.extend([p for p in suffix_parts if p])
                if counter > 2:
                    pieces.append(str(counter))
                candidate_name = "_".join(pieces)
                rel_path_str = str(rel_dir / f"{candidate_name}.md")
                counter += 1

            collisions.append((leaf.method_name, str(rel_dir / f"{base_filename}.md"), rel_path_str))

        used_rel_paths.add(rel_path_str)
        domain_counts[domain] += 1

        out_path = METHODS_ROOT / domain / subdomain / f"{candidate_name}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)

        file_content = legacy.generate_method_file(parsed)
        out_path.write_text(file_content, encoding="utf-8")

        print(f"[{idx:3d}] {leaf.method_name}")
        print(f"      → {domain}/{subdomain}/{candidate_name}.md")

    print("\nRegeneration complete.")
    print(f"Total methods written: {len(leaves)}")
    print("Domain distribution:")
    for domain, count in sorted(domain_counts.items()):
        print(f"  - {domain}: {count}")

    if collisions:
        print("\nNote: filename collisions detected and resolved:")
        for method_name, original, resolved in collisions:
            print(f"  * {method_name!r}: {original} → {resolved}")


if __name__ == "__main__":
    main()
