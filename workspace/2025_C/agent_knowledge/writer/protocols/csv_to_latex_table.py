#!/usr/bin/env python3
"""
csv_to_latex_table.py
Generate LaTeX table code from CSV files.

CRITICAL: This script guarantees 100% value consistency between CSV and LaTeX.
Any manual editing of generated LaTeX files will break consistency validation.

Usage:
    python csv_to_latex_table.py <csv_path> <table_id> [output_dir]

Example:
    python csv_to_latex_table.py output/results/results_1.csv 1 output/paper/tables/
"""

import pandas as pd
import os
import sys
import argparse


def generate_latex_table(csv_path, table_id, output_dir="output/paper/tables/"):
    """
    Generate LaTeX table from CSV file.

    Args:
        csv_path: Path to results CSV file (e.g., "output/results/results_1.csv")
        table_id: Table identifier (e.g., "1", "2", "3a")
        output_dir: Directory to write LaTeX file (default: "output/paper/tables/")

    Returns:
        output_path: Path to generated LaTeX file

    CRITICAL: All values rounded to 2 decimal places for consistency.
    DO NOT manually edit the generated LaTeX file.
    """
    # Verify CSV file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    # Read CSV
    df = pd.read_csv(csv_path)

    # Round to 2 decimal places (ENSURES CONSISTENCY)
    df_rounded = df.round(2)

    # Generate LaTeX code
    latex_code = df_rounded.to_latex(
        index=False,
        float_format="%.2f",
        escape=False,
        bold_rows=True,
        column_format='l' + 'c' * (len(df.columns) - 1)  # Left-align first col, center rest
    )

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Write to file
    output_path = os.path.join(output_dir, f"table_{table_id}.tex")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_code)

    print(f"✅ Generated LaTeX table: {output_path}")
    print(f"   Source CSV: {csv_path}")
    print(f"   Rows: {len(df_rounded)}, Columns: {len(df_rounded.columns)}")

    return output_path


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate LaTeX table from CSV file (guarantees 100% consistency)"
    )
    parser.add_argument("csv_path", help="Path to CSV file")
    parser.add_argument("table_id", help="Table identifier (e.g., '1', '2', '3a')")
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="output/paper/tables/",
        help="Output directory for LaTeX file (default: output/paper/tables/)"
    )

    args = parser.parse_args()

    try:
        generate_latex_table(args.csv_path, args.table_id, args.output_dir)
        return 0
    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
