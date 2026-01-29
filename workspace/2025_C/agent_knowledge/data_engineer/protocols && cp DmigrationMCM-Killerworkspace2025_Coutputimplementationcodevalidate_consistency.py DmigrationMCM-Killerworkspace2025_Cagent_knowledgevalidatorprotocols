#!/usr/bin/env python3
"""
validate_consistency.py
Verify CSV values match LaTeX values exactly.

CRITICAL: Any mismatch triggers AUTOMATIC REJECTION.
This script enforces Protocol 18: Zero tolerance for data inconsistencies.

Usage:
    python validate_consistency.py <csv_path> <latex_path>

Example:
    python validate_consistency.py output/results/results_1.csv output/paper/tables/table_1.tex

Exit Codes:
    0: All values consistent → APPROVE submission
    1: Mismatch detected → REJECT submission
"""

import pandas as pd
import re
import sys
import os
import argparse


def extract_latex_values(latex_path):
    """
    Extract numerical values from LaTeX table file.

    Args:
        latex_path: Path to LaTeX table file

    Returns:
        values: List of numerical values (as floats)
        locations: List of location strings (for error reporting)
    """
    with open(latex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all numerical values from LaTeX table
    # Pattern: Matches numbers like 25.27, 1.50, etc.
    pattern = r'(\d+\.\d{2})'
    matches = re.findall(pattern, content)

    values = [float(m) for m in matches]

    # Extract row/column info for error reporting
    lines = content.split('\n')
    locations = []
    row_idx = 0
    for line in lines:
        if re.search(pattern, line):
            col_matches = re.findall(pattern, line)
            for col_idx, val in enumerate(col_matches):
                locations.append(f"Row {row_idx}, Col {col_idx}")
        row_idx += 1

    return values, locations


def extract_csv_values(csv_path):
    """
    Extract numerical values from CSV file.

    Args:
        csv_path: Path to CSV file

    Returns:
        values: List of numerical values (as floats, rounded to 2 decimals)
        locations: List of location strings (for error reporting)
    """
    df = pd.read_csv(csv_path)

    # Round to 2 decimal places (match LaTeX formatting)
    df_rounded = df.round(2)

    # Extract all numerical values
    values = []
    locations = []

    for row_idx in range(len(df_rounded)):
        for col_idx in range(len(df_rounded.columns)):
            val = df_rounded.iloc[row_idx, col_idx]
            if pd.notna(val) and isinstance(val, (int, float)):
                values.append(float(val))
                locations.append(
                    f"Row {row_idx}, Col '{df_rounded.columns[col_idx]}'"
                )

    return values, locations


def validate_consistency(csv_path, latex_path, tolerance=0.0):
    """
    Validate CSV values match LaTeX values exactly.

    Args:
        csv_path: Path to CSV results file
        latex_path: Path to generated LaTeX table file
        tolerance: Allowed difference (default: 0.0 for EXACT match)

    Returns:
        bool: True if consistent, False if mismatch

    CRITICAL: Any mismatch → Return False → Trigger automatic rejection
    """
    print(f"Validating consistency...")
    print(f"  CSV: {csv_path}")
    print(f"  LaTeX: {latex_path}")
    print(f"  Tolerance: {tolerance}")

    # Extract values
    csv_values, csv_locations = extract_csv_values(csv_path)
    latex_values, latex_locations = extract_latex_values(latex_path)

    print(f"  CSV values: {len(csv_values)}")
    print(f"  LaTeX values: {len(latex_values)}")

    # Check value count
    if len(csv_values) != len(latex_values):
        print(f"\n❌ DATA INCONSISTENCY DETECTED")
        print(f"   Value count mismatch:")
        print(f"     CSV: {len(csv_values)} values")
        print(f"     LaTeX: {len(latex_values)} values")
        return False

    # Check each value
    mismatches = []
    for i in range(len(csv_values)):
        csv_val = csv_values[i]
        latex_val = latex_values[i]

        if abs(csv_val - latex_val) > tolerance:
            mismatches.append({
                'csv_val': csv_val,
                'latex_val': latex_val,
                'csv_loc': csv_locations[i] if i < len(csv_locations) else "Unknown",
                'latex_loc': latex_locations[i] if i < len(latex_locations) else "Unknown",
                'diff': abs(csv_val - latex_val)
            })

    # Report results
    if mismatches:
        print(f"\n❌ DATA INCONSISTENCY DETECTED")
        print(f"   Found {len(mismatches)} mismatch(es):\n")

        for idx, mismatch in enumerate(mismatches[:5], 1):  # Show first 5
            print(f"   Mismatch {idx}:")
            print(f"     CSV value: {mismatch['csv_val']:.2f}")
            print(f"     LaTeX value: {mismatch['latex_val']:.2f}")
            print(f"     Difference: {mismatch['diff']:.2f}")
            print(f"     CSV location: {mismatch['csv_loc']}")
            print(f"     LaTeX location: {mismatch['latex_loc']}")
            print()

        if len(mismatches) > 5:
            print(f"   ... and {len(mismatches) - 5} more mismatch(es)\n")

        return False
    else:
        print(f"\n✅ All values consistent ({len(csv_values)} values checked)")
        return True


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Validate CSV vs LaTeX consistency (automatic rejection on mismatch)"
    )
    parser.add_argument("csv_path", help="Path to CSV file")
    parser.add_argument("latex_path", help="Path to LaTeX table file")
    parser.add_argument(
        "--tolerance",
        type=float,
        default=0.0,
        help="Allowed difference (default: 0.0 for EXACT match)"
    )

    args = parser.parse_args()

    # Verify files exist
    if not os.path.exists(args.csv_path):
        print(f"❌ CSV file not found: {args.csv_path}", file=sys.stderr)
        return 1

    if not os.path.exists(args.latex_path):
        print(f"❌ LaTeX file not found: {args.latex_path}", file=sys.stderr)
        return 1

    # Validate consistency
    if validate_consistency(args.csv_path, args.latex_path, args.tolerance):
        print("✅ SUBMISSION APPROVED: All values consistent")
        return 0
    else:
        print("❌ SUBMISSION REJECTED: Data inconsistency detected")
        print("\nACTION REQUIRED:")
        print("  1. @writer: Regenerate all tables from CSV")
        print("  2. @validator: Re-run consistency check")
        print("  3. Loop until 100% consistency achieved\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
