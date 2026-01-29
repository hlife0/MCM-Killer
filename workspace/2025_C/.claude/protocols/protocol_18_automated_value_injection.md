# Protocol 18: Automated Value Injection with Automatic Rejection

**Version**: 3.2.0
**Status**: Active
**Owner**: @data_engineer (create scripts), @writer (use generated tables), **@validator (enforce rejection)**
**Scope**: Phase 7 (Paper Writing)
**Priority**: CRITICAL

---

## Purpose

Ensure 100% data consistency between CSV results and LaTeX paper tables through automated table generation, with **automatic rejection** for any detected inconsistencies. This protocol eliminates manual transcription errors that undermine result credibility.

---

## CRITICAL POLICY - AUTOMATIC REJECTION

> **If there is a discrepancy between the values in `paper.tex` and those in the CSV file, the submission shall be REJECTED OUTRIGHT instead of being penalized with point deductions.**

**Rationale**:
- Data inconsistency completely invalidates results credibility
- Root cause: Manual transcription from CSV to LaTeX introduces typos
- Automated injection guarantees consistency OR triggers automatic rejection
- No compromise: Submission must have 100% consistent data OR be rejected

**Rejection Protocol**:
1. @validator runs automated consistency check before Phase 7.5 (LaTeX Gate)
2. If ANY mismatch detected:
   - @director is NOTIFIED immediately
   - Paper is marked as **REJECTED**
   - @writer must regenerate all tables from CSV
   - @validator re-runs consistency check
   - Loop continues until 100% consistency achieved
   - Only after consistency verified → submission proceeds

---

## Rationale

**Problem**: Manual data transcription creates inconsistencies:
- Example: CSV shows `China_Gold = 25.27`, LaTeX shows `China_Gold = 25.40` (typo)
- Impact: Results cannot be trusted, paper credibility undermined
- Root cause: @writer manually transcribes numbers from CSV to LaTeX
- Current fix: Point deductions for inconsistencies (inadequate)

**Solution**: Automated LaTeX table generation from CSV files guarantees 100% consistency OR triggers automatic rejection before submission.

---

## Python Scripts

### Script 1: csv_to_latex_table.py

**Purpose**: Generate LaTeX table code from CSV files automatically

**Location**: `output/implementation/code/csv_to_latex_table.py`

**CRITICAL Requirements**:
- All values rounded to 2 decimal places (ENSURES CONSISTENCY)
- No manual editing of generated LaTeX code
- Direct CSV → LaTeX conversion (no intermediate steps)

**Implementation**:
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
        column_format='l' + 'c' * (len(df.columns) - 1)  # Left-align first col, center rest
    )

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Write to file
    output_path = os.path.join(output_dir, f"table_{table_id}.tex")
    with open(output_path, 'w') as f:
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

**Usage Examples**:
```bash
# Generate table for Model 1 results
python output/implementation/code/csv_to_latex_table.py \
    output/results/results_1.csv \
    1 \
    output/paper/tables/

# Generate table for Model 2 results
python output/implementation/code/csv_to_latex_table.py \
    output/results/results_2.csv \
    2 \
    output/paper/tables/

# Generate table for Model 3B forecasts
python output/implementation/code/csv_to_latex_table.py \
    output/results/results_3b_forecasts.csv \
    3b \
    output/paper/tables/
```

**Expected Output**:
```
✅ Generated LaTeX table: output/paper/tables/table_1.tex
   Source CSV: output/results/results_1.csv
   Rows: 234, Columns: 8
```

---

### Script 2: validate_consistency.py

**Purpose**: Verify paper.tex values match CSV values exactly

**Location**: `output/implementation/code/validate_consistency.py`

**CRITICAL Behavior**:
- Exit code 0: All values consistent → Submission APPROVED
- Exit code 1: Mismatch detected → Submission REJECTED
- Any mismatch triggers automatic rejection

**Implementation**:
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
    with open(latex_path, 'r') as f:
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
```

**Usage**:
```bash
# Validate Model 1 table consistency
python output/implementation/code/validate_consistency.py \
    output/results/results_1.csv \
    output/paper/tables/table_1.tex

# Validate all tables (batch script)
for i in 1 2 3a 3b 4; do
    python output/implementation/code/validate_consistency.py \
        output/results/results_${i}.csv \
        output/paper/tables/table_${i}.tex
done
```

**Exit Codes**:
- `0` (success): All values consistent → APPROVE submission
- `1` (failure): Mismatch detected → REJECT submission

---

## Integration with paper.tex

### How @writer Uses Generated Tables

**Method 1: Direct \input{} (RECOMMENDED)**

In `paper.tex`:
```latex
\begin{table}[htbp]
\centering
\caption{2028 Olympic Medal Forecasts (90\% Credible Intervals)}
\label{tab:forecasts_2028}
\input{../output/paper/tables/table_1.tex}
\end{table}
```

**Advantages**:
- Automatic consistency (LaTeX directly reads generated file)
- No manual copying/pasting
- Easy to regenerate (re-run script, re-compile paper)

---

**Method 2: Copy-Paste (NOT RECOMMENDED)**

❌ **DO NOT DO THIS**:
```latex
% WRONG: Manually copying values from generated LaTeX file
\begin{tabular}{lcccc}
Country & Gold & Silver & Bronze & Total \\
China & 25.27 & 22.45 & 18.30 & 66.02 \\  % Manually transcribed
USA & 38.15 & 35.20 & 28.90 & 102.25 \\     % Manually transcribed
...
\end{tabular}
```

**Why Wrong**: Manual transcription breaks consistency guarantee

---

### Example Workflow

**Step 1: @data_engineer creates csv_to_latex_table.py**
```bash
# Script exists at: output/implementation/code/csv_to_latex_table.py
```

**Step 2: @writer generates LaTeX tables**
```bash
# Generate all tables
python output/implementation/code/csv_to_latex_table.py output/results/results_1.csv 1
python output/implementation/code/csv_to_latex_table.py output/results/results_2.csv 2
python output/implementation/code/csv_to_latex_table.py output/results/results_3b.csv 3b
python output/implementation/code/csv_to_latex_table.py output/results/results_4.csv 4

# Output:
# ✅ Generated LaTeX table: output/paper/tables/table_1.tex
# ✅ Generated LaTeX table: output/paper/tables/table_2.tex
# ✅ Generated LaTeX table: output/paper/tables/table_3b.tex
# ✅ Generated LaTeX table: output/paper/tables/table_4.tex
```

**Step 3: @writer includes tables in paper.tex**
```latex
% In paper.tex Results section

\section{Results}

\subsection{Model 1: Bayesian Hierarchical}
\begin{table}[htbp]
\centering
\caption{Model 1 Forecasts}
\label{tab:model1_forecasts}
\input{../output/paper/tables/table_1.tex}
\end{table}

\subsection{Model 2: Zero-Inflated Poisson}
\begin{table}[htbp]
\centering
\caption{Model 2 Forecasts}
\label{tab:model2_forecasts}
\input{../output/paper/tables/table_2.tex}
\end{table}
```

**Step 4: @validator runs consistency check (before Phase 7.5)**
```bash
# Validate all tables
python output/implementation/code/validate_consistency.py \
    output/results/results_1.csv \
    output/paper/tables/table_1.tex

# Output (if consistent):
# ✅ All values consistent (234 values checked)
# ✅ SUBMISSION APPROVED: All values consistent
# Exit code: 0

# Output (if inconsistent):
# ❌ DATA INCONSISTENCY DETECTED
#    Found 1 mismatch(es):
#    Mismatch 1:
#      CSV value: 25.27
#      LaTeX value: 25.40
#      Difference: 0.13
# ❌ SUBMISSION REJECTED: Data inconsistency detected
# Exit code: 1
```

**Step 5: @director approves or rejects based on exit code**
- Exit code 0 → ✅ Approve Phase 7.5 (LaTeX compilation)
- Exit code 1 → ❌ Reject, notify @writer to regenerate tables

---

## Rejection Protocol (Automatic)

### Trigger Conditions

**Any of the following triggers AUTOMATIC REJECTION**:
1. @validator detects value mismatch (CSV ≠ LaTeX)
2. @validator detects value count mismatch (CSV has 234 values, LaTeX has 233)
3. @validator detects NaN/Inf in LaTeX but not in CSV
4. @validator detects manual editing (formatting inconsistencies)

---

### Rejection Workflow

```
Phase 7F Complete: @writer compiles paper.tex
         ↓
@validator runs: python validate_consistency.py *.csv *.tex
         ↓
    Exit Code?
         ↓
    ┌────┴────┐
    0 (PASS)  1 (FAIL)
    ↓         ↓
✅ APPROVE  ❌ REJECT
    ↓         ↓
Phase 7.5   Notify @director
            ↓
            @writer regenerates all tables:
              python csv_to_latex_table.py *.csv
            ↓
            @validator re-runs consistency check
            ↓
            Loop until exit code = 0 (100% consistent)
            ↓
            Only then: Phase 7.5 proceeds
```

---

### Rejection Notification Format

**When @validator detects mismatch**:

```
❌ SUBMISSION REJECTED: Data inconsistency detected

Validator Report:
- Phase: 7.5 (LaTeX Compilation Gate)
- Timestamp: 2026-01-29 14:30:00
- Detected by: @validator (Protocol 18 enforcement)

Issue Details:
- Mismatch count: 1
- CSV value: 25.27 (China_Gold)
- LaTeX value: 25.40 (China_Gold)
- Difference: 0.13
- Location: Row 0, Col 'China_Gold'

Action Required:
1. @writer: Regenerate all tables from CSV
   Command: python output/implementation/code/csv_to_latex_table.py *.csv
2. @validator: Re-run consistency check
3. Loop until 100% consistency achieved

Submission Status: BLOCKED (cannot proceed to Phase 7.5 until resolved)

Enforcement: Protocol 18 (Automatic Rejection)
```

---

## Responsibilities

### @data_engineer Responsibilities
1. **Create csv_to_latex_table.py**: Implement script before Phase 7
2. **Create validate_consistency.py**: Implement validation script
3. **Test Scripts**: Verify scripts work on sample CSV files
4. **Document Usage**: Provide clear instructions for @writer

**Deliverables** (before Phase 7A):
- `output/implementation/code/csv_to_latex_table.py` ✅
- `output/implementation/code/validate_consistency.py` ✅
- Test report showing scripts work correctly ✅

---

### @writer Responsibilities
1. **Use csv_to_latex_table.py**: Generate ALL numerical tables via script
2. **Include via \input{}**: Use `\input{tables/table_X.tex}` in paper.tex
3. **NO Manual Transcription**: DO NOT manually copy values from CSV to LaTeX
4. **Regenerate on Rejection**: If @validator detects mismatch, regenerate all tables

**Prohibited Actions**:
- ❌ Manually typing numbers from CSV into LaTeX
- ❌ Editing generated LaTeX table files (breaks consistency)
- ❌ Rounding values differently than script (2 decimal places)
- ❌ Copy-pasting values from CSV to LaTeX

---

### @validator Responsibilities (**ENFORCEMENT AUTHORITY**)
1. **Run validate_consistency.py**: Execute before Phase 7.5 (LaTeX Gate)
2. **Check Exit Code**: 0 = APPROVE, 1 = REJECT
3. **Report Mismatches**: If detected, document exact discrepancies
4. **Enforce Rejection**: Block submission if ANY inconsistency found
5. **Re-Verify After Fix**: Re-run validation after @writer regenerates tables

**Rejection Authority**:
- If exit code = 1 (mismatch detected): Mark submission as REJECTED
- @director CANNOT override rejection (must fix inconsistency first)
- Only exit code = 0 (100% consistent) allows submission to proceed

---

### @director Responsibilities
1. **Verify Script Existence**: Check both scripts exist before Phase 7A
2. **Verify Script Execution**: Confirm @writer generated all tables via script
3. **Enforce Rejection**: If @validator reports mismatch, do NOT approve Phase 7.5
4. **Block Override**: Do NOT override @validator's rejection (must fix first)
5. **Approve Only After Consistency**: Only approve Phase 7.5 when exit code = 0

**Approval Criteria**:
```
□ csv_to_latex_table.py exists (verified by ls)
□ validate_consistency.py exists (verified by ls)
□ All tables generated via script (verified by @writer report)
□ @validator ran consistency check (exit code 0)
□ No mismatches detected (100% consistent)
□ Phase 7.5 approved
```

---

## Success Criteria

**Quantitative**:
- 100% of submissions pass consistency validation
- 0 data inconsistencies between CSV and LaTeX
- 0 manual transcription errors
- 0 automatic rejections (because consistency guaranteed by automation)

**Qualitative**:
- All numerical tables generated via script (not manual)
- @validator confirms consistency before every submission
- Zero tolerance for inconsistencies (automatic rejection policy enforced)

---

## Failure Scenarios & Recovery

### Scenario 1: Manual Typo in LaTeX

**Detection**:
```bash
$ python validate_consistency.py results_1.csv table_1.tex

❌ DATA INCONSISTENCY DETECTED
   Found 1 mismatch(es):
   Mismatch 1:
     CSV value: 25.27
     LaTeX value: 25.40  (Manual typo: @writer typed wrong number)
     Difference: 0.13
❌ SUBMISSION REJECTED: Data inconsistency detected
```

**Recovery**:
1. @writer identifies manually edited table
2. Deletes table_1.tex
3. Re-runs script: `python csv_to_latex_table.py results_1.csv 1`
4. @validator re-runs validation
5. Exit code: 0 ✅ (consistency restored)

**Time Lost**: <10 minutes (vs. submission penalty if undetected)

---

### Scenario 2: Rounding Inconsistency

**Detection**:
```bash
$ python validate_consistency.py results_2.csv table_2.tex

❌ DATA INCONSISTENCY DETECTED
   Found 5 mismatch(es):
   Mismatch 1:
     CSV value: 25.267 (rounded to 25.27)
     LaTeX value: 25.27 (correct)
   Mismatch 2:
     CSV value: 38.145 (rounded to 38.15)
     LaTeX value: 38.14 (incorrect rounding)
     Difference: 0.01
```

**Recovery**:
1. @writer checks csv_to_latex_table.py rounding logic
2. Verifies script uses `df.round(2)` and `float_format="%.2f"`
3. Re-generates table: `python csv_to_latex_table.py results_2.csv 2`
4. @validator re-runs validation
5. Exit code: 0 ✅

**Root Cause**: Manual rounding in LaTeX (script uses consistent rounding)

---

### Scenario 3: Missing Values

**Detection**:
```bash
$ python validate_consistency.py results_3b.csv table_3b.tex

❌ DATA INCONSISTENCY DETECTED
   Value count mismatch:
     CSV: 234 values
     LaTeX: 233 values
❌ SUBMISSION REJECTED: Data inconsistency detected
```

**Recovery**:
1. @writer checks table_3b.tex for missing row
2. Finds that one country's row was accidentally deleted
3. Re-generates table: `python csv_to_latex_table.py results_3b.csv 3b`
4. @validator re-runs validation
5. Exit code: 0 ✅

**Root Cause**: Manual editing deleted a row (script guarantees完整性)

---

## Related Protocols

- **Protocol 2**: Strict Time Validation (all validators must re-verify)
- **Protocol 14**: Academic Style Alignment (table formatting)
- **Protocol 16**: Page Count Tracking (tables affect page count)

---

## Changelog

**v3.2.0** (2026-01-29): Initial creation
- Implements automated LaTeX table generation from CSV
- Creates automatic rejection policy for data inconsistencies
- Establishes zero-tolerance standard for data credibility
- Provides csv_to_latex_table.py script for automated generation
- Provides validate_consistency.py script for validation
- Assigns enforcement authority to @validator
