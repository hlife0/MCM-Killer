# Protocol 18: Automated Value Injection Examples

**Agent**: @data_engineer
**Protocol**: 18 (Automated Value Injection)
**Purpose**: Show examples of script creation and usage

---

## Script 1: csv_to_latex_table.py

### Location
`output/implementation/code/csv_to_latex_table.py`

### Purpose
Generate LaTeX table code from CSV files automatically with 100% value consistency.

### Complete Script

```python
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
        column_format='l' + 'c' * (len(df.columns) - 1)
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
```

---

### Usage Example 1: Generate Single Table

```bash
# Generate table for Model 1 results
python output/implementation/code/csv_to_latex_table.py \
    output/results/results_1.csv \
    1 \
    output/paper/tables/
```

**Output**:
```
✅ Generated LaTeX table: output/paper/tables/table_1.tex
   Source CSV: output/results/results_1.csv
   Rows: 234, Columns: 8
```

---

### Usage Example 2: Generate Multiple Tables

```bash
# Generate all tables at once
python output/implementation/code/csv_to_latex_table.py output/results/results_1.csv 1
python output/implementation/code/csv_to_latex_table.py output/results/results_2.csv 2
python output/implementation/code/csv_to_latex_table.py output/results/results_3a.csv 3a
python output/implementation/code/csv_to_latex_table.py output/results/results_3b.csv 3b
python output/implementation/code/csv_to_latex_table.py output/results/results_4.csv 4
```

**Output**:
```
✅ Generated LaTeX table: output/paper/tables/table_1.tex
   Source CSV: output/results/results_1.csv
   Rows: 234, Columns: 8
✅ Generated LaTeX table: output/paper/tables/table_2.tex
   Source CSV: output/results/results_2.csv
   Rows: 234, Columns: 6
✅ Generated LaTeX table: output/paper/tables/table_3a.tex
   Source CSV: output/results/results_3a.csv
   Rows: 234, Columns: 5
✅ Generated LaTeX table: output/paper/tables/table_3b.tex
   Source CSV: output/results/results_3b.csv
   Rows: 10, Columns: 4
✅ Generated LaTeX table: output/paper/tables/table_4.tex
   Source CSV: output/results/results_4.csv
   Rows: 234, Columns: 10
```

---

## Script 2: validate_consistency.py

### Location
`output/implementation/code/validate_consistency.py`

### Purpose
Verify CSV values match LaTeX values exactly. Exit code 0 = consistent, Exit code 1 = mismatch.

### Complete Script

```python
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

        for idx, mismatch in enumerate(mismatches[:5], 1):
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
```

---

### Usage Example 1: Consistent Data (PASS)

```bash
python output/implementation/code/validate_consistency.py \
    output/results/results_1.csv \
    output/paper/tables/table_1.tex
```

**Output** (if consistent):
```
Validating consistency...
  CSV: output/results/results_1.csv
  LaTeX: output/paper/tables/table_1.tex
  Tolerance: 0.0
  CSV values: 234
  LaTeX values: 234

✅ All values consistent (234 values checked)
✅ SUBMISSION APPROVED: All values consistent
```

**Exit Code**: 0 (success) → APPROVE submission

---

### Usage Example 2: Inconsistent Data (REJECT)

```bash
python output/implementation/code/validate_consistency.py \
    output/results/results_1.csv \
    output/paper/tables/table_1.tex
```

**Output** (if inconsistent):
```
Validating consistency...
  CSV: output/results/results_1.csv
  LaTeX: output/paper/tables/table_1.tex
  Tolerance: 0.0
  CSV values: 234
  LaTeX values: 234

❌ DATA INCONSISTENCY DETECTED
   Found 1 mismatch(es):

   Mismatch 1:
     CSV value: 25.27
     LaTeX value: 25.40
     Difference: 0.13
     CSV location: Row 0, Col 'China_Gold'
     LaTeX location: Row 0, Col 0

❌ SUBMISSION REJECTED: Data inconsistency detected

ACTION REQUIRED:
  1. @writer: Regenerate all tables from CSV
  2. @validator: Re-run consistency check
  3. Loop until 100% consistency achieved
```

**Exit Code**: 1 (failure) → REJECT submission

---

## Integration with paper.tex

### Step 1: Generate LaTeX Tables

```bash
# Generate all tables
python output/implementation/code/csv_to_latex_table.py output/results/results_1.csv 1
python output/implementation/code/csv_to_latex_table.py output/results/results_2.csv 2
python output/implementation/code/csv_to_latex_table.py output/results/results_3b.csv 3b
```

### Step 2: Include in paper.tex

```latex
\begin{table}[htbp]
\centering
\caption{2028 Olympic Medal Forecasts (90\% Credible Intervals)}
\label{tab:forecasts_2028}
\input{../output/paper/tables/table_1.tex}
\end{table}

\begin{table}[htbp]
\centering
\caption{Model Comparison Metrics}
\label{tab:model_comparison}
\input{../output/paper/tables/table_2.tex}
\end{table}
```

### Step 3: Validate Before Submission

```bash
# Validate all tables
python output/implementation/code/validate_consistency.py \
    output/results/results_1.csv \
    output/paper/tables/table_1.tex

python output/implementation/code/validate_consistency.py \
    output/results/results_2.csv \
    output/paper/tables/table_2.tex

python output/implementation/code/validate_consistency.py \
    output/results/results_3b.csv \
    output/paper/tables/table_3b.tex
```

---

## Common Issues and Solutions

### Issue 1: CSV File Not Found

**Error**:
```
❌ CSV file not found: output/results/results_1.csv
```

**Solution**:
- Check CSV file path is correct
- Verify file was created by @model_trainer
- Run `ls output/results/` to see available files

---

### Issue 2: LaTeX File Not Generated

**Error**:
```
❌ LaTeX file not found: output/paper/tables/table_1.tex
```

**Solution**:
- Run csv_to_latex_table.py first
- Check output directory exists
- Verify script completed successfully

---

### Issue 3: Value Count Mismatch

**Error**:
```
❌ DATA INCONSISTENCY DETECTED
   Value count mismatch:
     CSV: 234 values
     LaTeX: 233 values
```

**Solution**:
- Regenerate LaTeX table: `python csv_to_latex_table.py output/results/results_1.csv 1`
- Check for missing rows in LaTeX file
- Verify CSV wasn't modified after generation

---

### Issue 4: Rounding Inconsistency

**Error**:
```
❌ DATA INCONSISTENCY DETECTED
   Found 5 mismatch(es):
   Mismatch 1:
     CSV value: 25.267
     LaTeX value: 25.27
```

**Solution**:
- csv_to_latex_table.py rounds to 2 decimal places (correct)
- Manual LaTeX editing may have occurred (incorrect)
- Regenerate table from CSV (do not manually edit)

---

## Testing Your Scripts

### Test 1: Create Sample CSV

```python
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
data = {
    'Country': ['China', 'USA', 'Great Britain'] * 3,
    'Gold': np.random.randn(9) * 10 + 25,
    'Silver': np.random.randn(9) * 8 + 20,
    'Bronze': np.random.randn(9) * 6 + 15
}
df = pd.DataFrame(data)
df.to_csv('output/results/test_results.csv', index=False)
```

### Test 2: Generate LaTeX Table

```bash
python output/implementation/code/csv_to_latex_table.py \
    output/results/test_results.csv \
    test
```

### Test 3: Validate Consistency

```bash
python output/implementation/code/validate_consistency.py \
    output/results/test_results.csv \
    output/paper/tables/table_test.tex
```

**Expected Output**:
```
✅ All values consistent (27 values checked)
✅ SUBMISSION APPROVED: All values consistent
```

---

**END OF PROTOCOL 18 EXAMPLES**
