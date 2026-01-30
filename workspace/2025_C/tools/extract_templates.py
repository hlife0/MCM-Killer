#!/usr/bin/env python3
"""
Extract prompt templates from MM_Assets_Export/template.py
and save to individual .txt files in knowledge_library/

Usage:
    python extract_templates.py [source_file] [output_base]

    source_file: Path to template.py (default: knowledge_library/templates/template.py)
    output_base: Output directory (default: knowledge_library/templates/prompts)
"""

import os
import re
import json
import sys
from pathlib import Path

# Default paths - can be overridden by command line arguments
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "knowledge_library" / "templates" / "template.py"
DEFAULT_OUTPUT = ROOT / "knowledge_library" / "templates" / "prompts"

SOURCE_FILE = os.environ.get("TEMPLATE_SOURCE", str(DEFAULT_SOURCE))
OUTPUT_BASE = os.environ.get("TEMPLATE_OUTPUT", str(DEFAULT_OUTPUT))

# Template patterns to extract with their output filenames
# Based on actual constants found in template.py
TEMPLATES = {
    "problem_analysis": {
        "PROBLEM_ANALYSIS_PROMPT": "analysis_general.txt",
        "PROBLEM_ANALYSIS_CRITIQUE_PROMPT": "analysis_deep.txt",
        "PROBLEM_ANALYSIS_IMPROVEMENT_PROMPT": "analysis_comprehensive.txt"
    },
    "method_evaluation": {
        "METHOD_CRITIQUE_PROMPT": "critique_five_dimensions.txt",
    },
    "modeling": {
        "PROBLEM_MODELING_PROMPT": "modeling_basic.txt",
        "PROBLEM_MODELING_CRITIQUE_PROMPT": "modeling_advanced.txt",
        "PROBLEM_MODELING_IMPROVEMENT_PROMPT": "solution_formulation.txt"
    },
    "task_decomposition": {
        "TASK_DECOMPOSE_PROMPT": "task_decompose.txt",
        "TASK_DEPENDENCY_ANALYSIS_PROMPT": "dependency_analysis.txt"
    }
}

def extract_template(content, template_name):
    """Extract a single template constant from Python file"""
    # Try to match triple-quoted strings
    patterns = [
        rf'{template_name}\s*=\s*"""(.+?)"""',
        rf'{template_name}\s*=\s*\'\'\'(.+?)\'\'\'',
        rf'{template_name}\s*=\s*"(.+?)"\n',
        rf'{template_name}\s*=\s*\'(.+?)\'\n'
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = match.group(1).strip()
            # Unescape common escapes
            content = content.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace("\\'", "'")
            return content
    return None

def main():
    # Read source file
    print(f"Reading source file: {SOURCE_FILE}")
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    extracted_count = 0
    failed_count = 0

    # Extract and save templates
    for category, templates in TEMPLATES.items():
        for template_const, filename in templates.items():
            template_content = extract_template(content, template_const)

            if template_content:
                # Create output path
                output_path = os.path.join(OUTPUT_BASE, category, filename)

                # Save template
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as out:
                    out.write(template_content)

                print(f"[OK] Extracted {template_const} -> {output_path}")
                extracted_count += 1
            else:
                print(f"[FAIL] Failed to extract {template_const}")
                failed_count += 1

    print(f"\n=== Extraction Summary ===")
    print(f"Successfully extracted: {extracted_count}")
    print(f"Failed: {failed_count}")
    print(f"Total: {extracted_count + failed_count}")

if __name__ == "__main__":
    main()
