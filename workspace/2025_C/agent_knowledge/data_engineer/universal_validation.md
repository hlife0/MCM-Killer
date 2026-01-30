# Universal Data Validation Protocol

> **Purpose**: This file contains the universal data validation protocol that applies to ALL data processing tasks, not just problem-specific validation. This prevents entire classes of bugs by validating reference data, mappings, and categorical assignments against authoritative sources.

---

## Step 3.5: Universal Data Validation

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
