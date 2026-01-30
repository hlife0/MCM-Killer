# -*- coding: utf-8 -*-
"""
Link Verification Script for Agent Prompt Files
Checks all external knowledge file references in agent prompts
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# Agent files to check
AGENT_FILES = [
    "advisor.md",
    "code_translator.md",
    "data_engineer.md",
    "model_trainer.md",
    "modeler.md",
    "time_validator.md",
    "writer.md"
]

AGENTS_DIR = Path(r"D:\MCM-Killer\MCM-Killer\workspace\2025_C\.claude\agents")
BASE_DIR = Path(r"D:\MCM-Killer\MCM-Killer\workspace\2025_C")

# Pattern to match references like: ../../agent_knowledge/[agent]/[file].md
LINK_PATTERN = r'`?\.\./\.\./(agent_knowledge/[^`\s]+\.md)`?'

def extract_links(file_path):
    """Extract all agent_knowledge references from a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    matches = re.findall(LINK_PATTERN, content)
    return matches

def verify_link(agent_file, relative_ref):
    """
    Verify if a link exists
    agent_file: e.g., "advisor.md"
    relative_ref: e.g., "agent_knowledge/advisor/safe_placeholder_pattern.md"
    """
    # From .claude/agents/advisor.md, ../../agent_knowledge/ points to workspace/2025_C/agent_knowledge/
    # Also check .claude/agent_knowledge/ (duplicate location)

    # Try both locations
    possible_paths = [
        BASE_DIR / relative_ref,  # workspace/2025_C/agent_knowledge/...
        BASE_DIR / ".claude" / relative_ref,  # workspace/2025_C/.claude/agent_knowledge/...
    ]

    for path in possible_paths:
        if path.exists():
            return True, str(path)

    return False, None

def main():
    """Main verification logic"""
    results = {
        'total_links': 0,
        'working_links': 0,
        'broken_links': 0,
        'agent_details': {}
    }

    broken_links_details = []
    working_links_details = []

    for agent_file in AGENT_FILES:
        agent_path = AGENTS_DIR / agent_file

        if not agent_path.exists():
            print(f"❌ Agent file not found: {agent_file}")
            continue

        print(f"\n📄 Checking {agent_file}...")

        links = extract_links(agent_path)
        agent_name = agent_file.replace('.md', '')

        results['agent_details'][agent_name] = {
            'total': len(links),
            'working': 0,
            'broken': 0,
            'links': []
        }

        results['total_links'] += len(links)

        for link in links:
            exists, actual_path = verify_link(agent_file, link)

            link_info = {
                'reference': link,
                'exists': exists,
                'actual_path': actual_path if exists else "NOT FOUND"
            }

            results['agent_details'][agent_name]['links'].append(link_info)

            if exists:
                results['working_links'] += 1
                results['agent_details'][agent_name]['working'] += 1
                working_links_details.append({
                    'agent': agent_name,
                    'reference': link,
                    'path': actual_path
                })
                print(f"  ✅ {link}")
            else:
                results['broken_links'] += 1
                results['agent_details'][agent_name]['broken'] += 1
                broken_links_details.append({
                    'agent': agent_name,
                    'reference': link,
                    'expected_paths': [
                        str(BASE_DIR / link),
                        str(BASE_DIR / ".claude" / link)
                    ]
                })
                print(f"  ❌ {link}")

    # Generate report
    print("\n" + "="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    print(f"Total links found: {results['total_links']}")
    print(f"Working links: {results['working_links']}")
    print(f"Broken links: {results['broken_links']}")
    print()

    if results['broken_links'] > 0:
        print("BROKEN LINKS DETAILS:")
        print("-" * 80)
        for item in broken_links_details:
            print(f"\nAgent: {item['agent']}")
            print(f"Reference: {item['reference']}")
            print(f"Expected locations:")
            for path in item['expected_paths']:
                print(f"  - {path}")

    # Write detailed report
    report_path = BASE_DIR / "LINK_VERIFICATION_REPORT.md"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Link Verification Report\n\n")
        f.write(f"**Generated**: {Path(__file__).name}\n\n")
        f.write("---\n\n")

        # Summary
        f.write("## Summary\n\n")
        f.write(f"- **Total Links**: {results['total_links']}\n")
        f.write(f"- **Working Links**: {results['working_links']}\n")
        f.write(f"- **Broken Links**: {results['broken_links']}\n")
        f.write(f"- **Success Rate**: {results['working_links']/results['total_links']*100:.1f}%\n\n")

        f.write("---\n\n")

        # Per-agent breakdown
        f.write("## Per-Agent Breakdown\n\n")
        for agent, data in results['agent_details'].items():
            f.write(f"### {agent}\n\n")
            f.write(f"- Total references: {data['total']}\n")
            f.write(f"- Working: {data['working']}\n")
            f.write(f"- Broken: {data['broken']}\n\n")

            if data['broken'] > 0:
                f.write("**Broken links:**\n\n")
                for link in data['links']:
                    if not link['exists']:
                        f.write(f"- ❌ `{link['reference']}`\n")
                f.write("\n")

            if data['working'] > 0:
                f.write("**Working links:**\n\n")
                for link in data['links']:
                    if link['exists']:
                        f.write(f"- ✅ `{link['reference']}`\n")
                        f.write(f"  - Actual path: `{link['actual_path']}`\n")
                f.write("\n")

        f.write("---\n\n")

        # Broken links section
        if results['broken_links'] > 0:
            f.write("## Broken Links Analysis\n\n")

            for item in broken_links_details:
                f.write(f"### {item['agent']} → `{item['reference']}`\n\n")
                f.write("**Expected locations:**\n\n")
                for path in item['expected_paths']:
                    f.write(f"- `{path}`\n")

                # Try to suggest fixes
                filename = Path(item['reference']).name
                f.write(f"\n**Suggested fixes:**\n\n")
                f.write(f"1. Check if file exists with different name in agent_knowledge/\n")
                f.write(f"2. Create missing file: `{item['reference']}`\n")
                f.write(f"3. Update reference in `{item['agent']}.md` if file moved\n\n")

        f.write("---\n\n")

        # Working links section
        f.write("## All Working Links\n\n")
        for item in working_links_details:
            f.write(f"- **{item['agent']}** → `{item['reference']}`\n")
            f.write(f"  - Path: `{item['path']}`\n\n")

    print(f"\n✅ Detailed report written to: {report_path}")

    return results

if __name__ == "__main__":
    main()
