#!/usr/bin/env python3
"""
Workspace Initializer: Create complete v3.1.0 directory structure.

Usage:
    python init_workspace.py [workspace_path]

Example:
    python init_workspace.py workspace/2025_C/

This script creates the complete MCM-Killer v3.1.0 directory tree including:
- Knowledge library structure (HMML 2.0)
- Output directories (docs, implementation, figures, paper)
- Agent configuration directories
- Benchmark and reference directories
"""

import os
import sys
from pathlib import Path
from datetime import datetime


def create_structure(base_path: str) -> None:
    """Create complete v3.1.0 directory tree."""

    # Define structure
    directories = [
        # Knowledge base (HMML 2.0)
        "knowledge_library/academic_writing",
        "knowledge_library/methods/optimization/linear_programming",
        "knowledge_library/methods/optimization/nonlinear_programming",
        "knowledge_library/methods/optimization/heuristic",
        "knowledge_library/methods/differential_equations/epidemic",
        "knowledge_library/methods/differential_equations/pde",
        "knowledge_library/methods/differential_equations/sde",
        "knowledge_library/methods/statistics/bayesian",
        "knowledge_library/methods/statistics/time_series",
        "knowledge_library/methods/statistics/regression",
        "knowledge_library/methods/network_science/pathfinding",
        "knowledge_library/methods/network_science/centrality",
        "knowledge_library/methods/network_science/community",
        "knowledge_library/methods/machine_learning/trees",
        "knowledge_library/methods/machine_learning/neural_networks",
        "knowledge_library/methods/machine_learning/clustering",
        "knowledge_library/templates/narrative_arcs",
        "knowledge_library/templates/writing",

        # Reference materials
        "reference_papers",

        # Tools
        "tools",
        "tests",

        # Output structure (Phase outputs)
        "output/docs/insights",           # Phase 5.8 outputs
        "output/docs/knowledge",          # Phase 0.2 outputs
        "output/docs/validation",         # Phase 9.1 outputs
        "output/docs/requirements",       # Phase 0 outputs
        "output/docs/consultations",      # Feedback files
        "output/implementation/code",     # Phase 4 outputs
        "output/implementation/data/raw",
        "output/implementation/data/processed",
        "output/implementation/logs",     # Training logs
        "output/implementation/models",   # Saved models
        "output/figures",                 # Phase 6 outputs
        "output/paper",                   # Phase 7-9 outputs

        # Benchmarks (Phase 11)
        "benchmarks",

        # Agent configs
        ".claude/agents"
    ]

    created_count = 0

    # Create directories
    for dir_path in directories:
        full_path = os.path.join(base_path, dir_path)
        Path(full_path).mkdir(parents=True, exist_ok=True)
        print(f"  Created: {dir_path}")
        created_count += 1

    # Create .keep files for empty dirs that need to be preserved
    keep_dirs = ["reference_papers", "benchmarks", "tests"]
    for dir_path in keep_dirs:
        full_path = os.path.join(base_path, dir_path, ".keep")
        with open(full_path, 'w') as f:
            f.write("# Placeholder to preserve directory in git\n")

    # Create README files for key directories
    readme_contents = {
        "knowledge_library/README.md": """# Knowledge Library (HMML 2.0)

This directory contains the structured knowledge base for MCM-Killer v3.1.0.

## Structure

- `academic_writing/` - Style guide and anti-patterns
- `methods/` - Mathematical methods organized by domain
- `templates/` - Narrative and writing templates

## Usage

@knowledge_librarian reads from this directory in Phase 0.2.
@writer and @editor reference style_guide.md in Phase 7-9.
""",
        "output/docs/insights/README.md": """# Insight Documents

Phase 5.8 outputs from @metacognition_agent.

## Contents

- `narrative_arc_{i}.md` - Struggle-to-insight transformations for each model
""",
        "output/docs/validation/README.md": """# Validation Documents

Phase 9.1 outputs from @judge_zero.

## Contents

- `judgment_report.md` - Mock judging results
- `defcon_log.md` - DEFCON 1 recovery log (if triggered)
"""
    }

    for rel_path, content in readme_contents.items():
        full_path = os.path.join(base_path, rel_path)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Created: {rel_path}")

    # Create VERSION_MANIFEST.json
    manifest = {
        "version": "3.1.0",
        "created": datetime.now().isoformat(),
        "structure_version": "1.0",
        "directories_created": created_count,
        "phases": {
            "-1": "Style Guide Generation",
            "0": "Problem Understanding",
            "0.2": "Active Knowledge Retrieval",
            "0.5": "Feasibility Check",
            "1": "Model Design",
            "1.5": "Design Validation",
            "2-3": "Data Processing",
            "4": "Code Translation",
            "4.5": "Code Validation",
            "5": "Model Training",
            "5.5": "Post-Training Validation",
            "5.8": "Insight Extraction",
            "6": "Result Generation",
            "7": "Paper Generation",
            "9": "Summary Generation",
            "9.1": "Mock Judging",
            "9.5": "Final Package",
            "10": "Submission",
            "11": "Self-Evolution"
        }
    }

    import json
    manifest_path = os.path.join(base_path, "VERSION_MANIFEST.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    print(f"  Created: VERSION_MANIFEST.json")

    print(f"\n  Workspace structure created at: {base_path}")
    print(f"  Total directories: {created_count}")


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
    else:
        target_path = "workspace/2025_C/"

    print(f"\nMCM-Killer v3.1.0 Workspace Initializer")
    print(f"=" * 40)
    print(f"Target: {target_path}\n")

    create_structure(target_path)

    print(f"\n  Done! Workspace is ready for MCM-Killer v3.1.0")


if __name__ == "__main__":
    main()
