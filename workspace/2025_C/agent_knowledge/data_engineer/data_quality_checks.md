# Data Quality Check Function and Validation Standards

> **Purpose**: This file contains the mandatory data quality check function and validation standards that MUST be included in all data processing scripts. This prevents data pollution (Python objects in CSV) and ensures data integrity.

---

## 🚨 [CRITICAL] Data Integrity Standards

> [!CAUTION]
> **Data pollution is a MAJOR issue. Experiments showed Python objects (lists, dicts) being serialized into CSV files, causing silent failures.**

### Scalar Principle (MANDATORY)

**CSV cells MUST be scalar only**:
```
✅ ALLOWED: int, float, str (pure), bool
❌ FORBIDDEN: lists, dicts, numpy objects, serialized strings
```

**Examples of POLLUTED data** (FORBIDDEN):
```csv
country,medals,years_won
USA,"[10, 20, 30]",2024
China,"{'gold': 5, 'silver': 3}",2024
```

**Examples of CLEAN data** (REQUIRED):
```csv
country,medals_gold,medals_silver,medals_bronze,year
USA,10,20,30,2024
China,5,3,2,2024
```

### Mandatory Self-Check Function

**Your code MUST include `check_data_quality(df)` function**:

```python
def check_data_quality(df, dataset_name="dataset"):
    """
    MANDATORY: Check data quality to prevent pollution.
    🛡️ Anti-Fraud Mechanism
    """
    issues = []

    # 1. Check for object types that might be serialized lists/dicts
    for col in df.select_dtypes(include=['object']):
        # Check if any value looks like serialized Python object
        if df[col].astype(str).str.contains(r'^\[|^\{', na=False).any():
            problematic_rows = df[df[col].astype(str).str.contains(r'^\[|^\{', na=False)]
            issues.append(f"Column '{col}' contains serialized Python objects in {len(problematic_rows)} rows")
            issues.append(f"Example: {problematic_rows[col].iloc[0]}")

    # 2. Check for duplicates
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        issues.append(f"Data contains {dup_count} duplicate rows")

    # 3. Check for all-NaN columns
    nan_cols = df.columns[df.isna().all()].tolist()
    if nan_cols:
        issues.append(f"Columns completely NaN: {nan_cols}")

    # 4. Check for infinite values in numeric columns
    for col in df.select_dtypes(include=['number']):
        if np.isinf(df[col]).any():
            inf_count = np.isinf(df[col]).sum()
            issues.append(f"Column '{col}' contains {inf_count} infinite values")

    if issues:
        error_msg = f"❌ DATA QUALITY CHECK FAILED for {dataset_name}:\n"
        for issue in issues:
            error_msg += f"  - {issue}\n"
        raise ValueError(error_msg)
    else:
        print(f"✅ Data Quality Check Passed for {dataset_name}")
        print(f"   Rows: {len(df)}, Columns: {len(df.columns)}")
        print(f"   Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
```

### Required File Outputs

**For each model {i}, you MUST produce**:

1. **`output/implementation/data/features_{i}.pkl`** - Feature DataFrame (allows complex index types)
2. **`output/implementation/data/features_{i}.csv`** - Human-readable, strictly scalar

**Both files MUST pass `check_data_quality()`**

---

## 🧠 Self-Awareness & Environment Exploration

> [!IMPORTANT]
> **ALWAYS explore your environment FIRST.**

### Step 0: Environment Exploration (MANDATORY)

```bash
# Check current directory and data availability
echo "Current workspace: $(pwd)"
ls -la 2025_Problem_C_Data/ 2>/dev/null || echo "Data not extracted yet"

# Check Python environment
python --version
pip list | grep -E "pandas|numpy|scipy|sklearn"
```

**Report findings to Director**:
```
Director, Environment exploration complete:
- Data files: [list available files]
- Python: [version]
- Key libraries: [available/missing]
```

---

## 📝 Data Processing Workflow

### Step 1: Extract Data (if not already done)

```bash
# Verify current directory
echo "Current workspace: $(pwd)"

# Unzip if data folder doesn't exist
if [ ! -d "2025_Problem_C_Data" ]; then
    echo "Extracting data files..."
    unzip ./2025_Problem_C_Data.zip
    echo "Data extraction complete"
else
    echo "Data directory already exists"
fi
```

### Step 2: Read Model Design

```
Read: output/model_design.md
```

**Extract feature requirements** - Look for sections like:
- "Required Features"
- "Variables"
- "Data Requirements"

### Step 3: Read Raw Data

```python
import pandas as pd
import numpy as np

# Read raw data files
athletes = pd.read_csv('2025_Problem_C_Data/summerOly_athletes.csv')
hosts = pd.read_csv('2025_Problem_C_Data/summerOly_hosts.csv')
medals = pd.read_csv('2025_Problem_C_Data/summerOly_medal_counts.csv')
programs = pd.read_csv('2025_Problem_C_Data/summerOly_programs.csv')
```

### Step 3.5: Universal Data Validation

> [!CRITICAL]
> **[MANDATORY] Validate ALL reference data, mappings, and categorical assignments.**
>
> This prevents entire classes of bugs (not just problem-specific issues).

```python
# Import universal validator
from implementation.data.validation import DataValidator

# Create validator instance
validator = DataValidator(data)

# Define schema for YOUR problem
schema = {
    'medal_count': ('int', (0, None)),      # Non-negative integers
    'year': ('int', (1896, 2024)),          # Reasonable year range
    'percentage': ('float', (0, 100)),      # Percentage in [0, 100]
}

# 1. Validate data types and ranges
validator.validate_ranges(schema)

# 2. Validate reference mapping completeness
# (e.g., all NOCs have continent assignments)
validator.validate_completeness(NOC_TO_CONTINENT, key_column='NOC')

# 3. Verify against authoritative sources
# (e.g., cross-reference with ISO standards, GeoNames)
auth_continents = load_authoritative_geonames()
discrepancies = validator.verify_authoritative(NOC_TO_CONTINENT, auth_continents)

# 4. Validate domain-specific consistency
# Geographic: Caribbean countries → Americas (not Africa)
# Temporal: No future dates in historical data
# Physical: Non-negative counts, valid coordinates
validator.validate_consistency(check_geographic_consistency, rule_name="geographic")

# Print validation report
print(validator.report())

# If validation fails, STOP and fix data
assert not validator.violations, f"Data validation failed: {validator.report()}"
```

**Mandatory Validation Checklist**:

1. **Reference Data Completeness**:
   - All dataset items have mapping entries
   - No orphan keys (foreign key violations)

2. **Geographic/Categorical Consistency**:
   - Caribbean countries → Americas (not Africa)
   - No impossible category assignments
   - Geographic groupings verified

3. **Authoritative Source Verification**:
   - Cross-reference mappings with trusted sources
   - ISO standards for geographic data
   - Official databases for scientific/historical data

4. **Data Type and Range Validation**:
   - Counts: non-negative integers
   - Percentages: [0, 100] or [0, 1]
   - Years: reasonable historical range
   - Coordinates: lat [-90, 90], lon [-180, 180]

5. **No Missing Values** (or documented):
   - All required columns present
   - Missing values documented and justified
   - Imputation strategy validated

**If validation fails**:
- DO NOT proceed to feature engineering
- Fix data issues first
- Re-run validation
- Only proceed when `validator.report()` returns "✅ ALL VALIDATIONS PASSED"

### Step 4: Clean and Process Data

**Key cleaning steps**:
1. Handle missing values
2. Remove duplicates
3. Fix data types
4. Standardize formats (country names, NOC codes, etc.)
5. Merge datasets appropriately

### Step 5: Create Features (per model_design.md)

**CRITICAL**: Features MUST match `model_design.md` specification exactly.

If model_design specifies:
- Feature: "GDP" → Create `gdp` column
- Feature: "Population" → Create `population` column
- Feature: "Host Nation" → Create `is_host` binary column

### Step 6: Save Data (Both Formats)

```python
import pickle

# Save as PKL (for Python consumption)
with open('output/implementation/data/features_1.pkl', 'wb') as f:
    pickle.dump(features_df, f)

# Save as CSV (for human readability + validation)
features_df.to_csv('output/implementation/data/features_1.csv', index=False)

# MANDATORY: Run quality check on both
check_data_quality(features_df, "features_1.pkl")
check_data_quality(pd.read_csv('output/implementation/data/features_1.csv'), "features_1.csv")
```

### Step 7: Save Processing Script

```python
# Save to output/implementation/code/data_prep_{i}.py
```

---

## ⚠️ Common Data Quality Issues to Watch For

### 1. Serialized Python Objects

**Symptom**: CSV cells contain `['a', 'b']` or `{'x': 1}` strings
**Fix**: Expand lists/dicts into separate scalar columns

### 2. Duplicate Rows

**Symptom**: Same (country, year) combination appears multiple times
**Fix**: Aggregate or deduplicate based on logic

### 3. Missing Critical Values

**Symptom**: NaN in required columns
**Fix**: Imputation (mean, median, mode) or flag columns

### 4. Inconsistent Naming

**Symptom**: "USA", "United States", "U.S.A." for same country
**Fix**: Standardize to single convention (e.g., NOC codes)

### 5. Type Mismatches

**Symptom**: Numeric columns stored as strings
**Fix**: Explicit type conversion `pd.to_numeric()`

---

## 🔄 Self-Correction Before Submission

> [!CAUTION]
> **Before reporting completion, verify your outputs.**

### Mandatory Verification Checklist

```bash
# 1. Check files exist
ls -lh output/implementation/data/features_1.*
ls -lh output/implementation/code/data_prep_1.py

# 2. Verify CSV is readable
head -20 output/implementation/data/features_1.csv

# 3. Check for data quality issues
python -c "
import pandas as pd
df = pd.read_csv('output/implementation/data/features_1.csv')
print(f'Shape: {df.shape}')
print(f'Dtypes:\n{df.dtypes}')
print(f'Missing values:\n{df.isna().sum()}')
"
```

### Data Quality Report Template

```markdown
# Data Engineering Report Model {i}

## Data Processing Complete

### Inputs
- Raw data files: [list files used]
- Model design: output/model_design.md

### Outputs
- `output/implementation/data/features_{i}.pkl` ✅
- `output/implementation/data/features_{i}.csv` ✅
- `output/implementation/code/data_prep_{i}.py` ✅

### Data Quality
- **check_data_quality()**: ✅ PASSED
- Rows: {count}
- Columns: {count}
- Memory: {MB}
- Missing values: {count or "None"}
- Duplicates: {count or "None"}

### Features Created
| Feature | Type | Description | Source |
|---------|------|-------------|---------|
| {feature} | {type} | {description} | {source} |

### Data Cleaning Steps
1. [Step 1]
2. [Step 2]
...

### Issues Found and Resolved
- [Issue]: [Resolution]

### Upstream Issues Found
- Found upstream problems: Yes/No
- Suggesting Rewind: Yes/No
- If Yes:
  - Target Phase: {phase number}
  - Problem: {description}
  - Rewind report: output/docs/rewind/rewind_rec_{i}_data_engineer_phase{target}.md

---

**Status**: READY for Phase 4 (Code Translation)
**Date**: {current_date}
**Processed by**: @data_engineer
```

---

## 🚨 MANDATORY: Report Problems Immediately

| Problem | Action |
|---------|--------|
| Raw data file missing | "Director, expected data at X but file missing. Check extraction." |
| Model design unclear | "Director, model_design.md doesn't specify feature X clearly. Consult @modeler." |
| Feature cannot be created | "Director, feature X requires data that doesn't exist. Need consultation." |
| Data quality issues severe | "Director, data has systematic issues. May need Rewind to Phase 1." |

**NEVER**:
- ❌ Skip `check_data_quality()`
- ❌ Save CSV with Python objects
- ❌ Create features that don't match model_design.md
- ❌ Hide data quality issues
