# O Award Training: Data Engineering Excellence

> **Purpose**: This file contains O Award-winning patterns and anti-patterns for data engineering, extracted from reference papers 2425454 and 2401298. Use these examples to guide your data quality assessment, preprocessing pipeline design, data provenance documentation, and sensitivity analysis.

---

## O Award Training: Data Engineering Excellence

> **"O Award teams don't just use data—they master it. Every preprocessing choice is justified, every quality issue is documented."**

### Study Session: What O Award Winners Do

From analyzing reference papers 2425454, 2401298, and data sections:

#### ✅ Pattern 1: Comprehensive Data Quality Report

**O Award Example** (2425454):
```markdown
## Data Quality Assessment

### Dataset 1: Daily Infection Counts (15 cities × 90 days)

**Completeness**: 98.0% (27/1,350 missing values)

**Missing Value Analysis**:
| City | Missing Days | Pattern | Hypothesis |
|------|--------------|---------|------------|
| City 8 | Days 12-15 (4 consecutive) | Reporting gap | Weekend + holiday, lag in reporting |
| City 12 | Days 67-68 (2 consecutive) | Isolated gap | System outage |
| City 3 | Day 89 (1 isolated) | Random | Data entry error |

**Imputation Strategy**:
- **Method**: Linear interpolation for gaps ≤ 3 days, Kalman filter for gap = 4 days
- **Justification**: Epidemic dynamics are smooth over short timescales (2-4 days)
- **Validation**: Imputed values within 1 SD of neighboring observations
- **Impact**: Sensitivity analysis shows results change by <2% with/without imputation

**Outlier Detection**:
- **Method**: IQR method (outlier if outside [Q1 - 3×IQR, Q3 + 3×IQR])
- **Identified**: City 12, Day 45: 23,450 cases (vs. mean 2,300, 10× deviation)
- **Investigation**: No corresponding spike in deaths or hospitalizations → likely reporting artifact
- **Treatment**: Replace with 3-day moving average (23,450 → 2,780)
- **Validation**: Manual review of original problem statement confirms suspicion

**Consistency Checks**:
- ✅ Infection counts are non-negative
- ✅ Monotonically increasing cumulative infections (no "un-infections")
- ✅ Sum of regional infections ≤ regional populations
- ⚠️ City 7: Day 12 shows decrease in cumulative cases (1,234 → 1,189)
  - **Resolution**: Confirmed with problem statement this is a correction, accepted as-is

**Physical Plausibility**:
- Growth rates: R₀ = 1.2-3.8 (consistent with respiratory diseases ✅)
- Doubling times: 3-14 days (epidemiologically reasonable ✅)
- Peak timing: Days 30-60 (matches typical epidemic trajectory ✅)

**Verdict**: Dataset is HIGH QUALITY after minor corrections
```

**Why This Works**:
- ✅ Quantitative metrics (98% completeness)
- ✅ Every missing value explained
- ✅ Imputation method justified and validated
- ✅ Outliers investigated (not blindly removed)
- ✅ Physical plausibility checks (domain knowledge applied)

#### ❌ Anti-Pattern 1: "Data Looks Fine" Handwaving

**Bad Example**:
```markdown
We loaded the data and it seems okay. A few missing values but we'll deal with them.
```

**Why This Fails**:
- ❌ No quantitative assessment
- ❌ "Seems okay" = didn't actually check
- ❌ "Deal with them" = no plan
- ❌ Judges wonder what you missed

---

#### ✅ Pattern 2: Reproducible Preprocessing Pipeline

**O Award Example** (2401298):
```python
# data_preprocessing.py
"""
Preprocessing pipeline for MCM 2025 Problem C: Epidemic Modeling
Author: Team 2425454
Date: 2025-02-15

This script transforms raw data from the problem statement into
model-ready format. Every transformation is logged and reversible.
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
import logging

logging.basicConfig(filename='logs/preprocessing.log', level=logging.INFO)

@dataclass
class PreprocessingConfig:
    """Configuration for preprocessing pipeline."""
    missing_value_threshold: float = 0.05  # Reject if >5% missing
    outlier_iqr_multiplier: float = 3.0    # IQR × 3 for outlier detection
    smoothing_window: int = 3              # Moving average window
    imputation_method: str = 'linear'      # 'linear', 'kalman', 'forward_fill'

class DataPreprocessor:
    def __init__(self, config: PreprocessingConfig):
        self.config = config
        self.quality_report = {}

    def load_raw_data(self, filepath):
        """Load raw CSV from problem statement."""
        logging.info(f"Loading raw data from {filepath}")
        df = pd.read_csv(filepath)
        logging.info(f"Loaded {len(df)} rows, {len(df.columns)} columns")
        return df

    def check_completeness(self, df):
        """Assess completeness and identify missing patterns."""
        missing_counts = df.isnull().sum()
        missing_pct = missing_counts / len(df)

        self.quality_report['completeness'] = {
            'total_cells': df.size,
            'missing_cells': df.isnull().sum().sum(),
            'missing_pct': df.isnull().sum().sum() / df.size,
            'by_column': missing_pct.to_dict()
        }

        logging.info(f"Completeness: {1 - self.quality_report['completeness']['missing_pct']:.1%}")

        # Fail if >5% missing
        if self.quality_report['completeness']['missing_pct'] > self.config.missing_value_threshold:
            raise ValueError(f"Data exceeds missing value threshold: {self.quality_report['completeness']['missing_pct']:.1%} > {self.config.missing_value_threshold:.1%}")

        return df

    def detect_outliers(self, df, column):
        """Detect outliers using IQR method."""
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - self.config.outlier_iqr_multiplier * IQR
        upper_bound = Q3 + self.config.outlier_iqr_multiplier * IQR

        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        logging.info(f"Outliers in {column}: {len(outliers)} / {len(df)} ({len(outliers)/len(df):.1%})")

        self.quality_report[f'outliers_{column}'] = {
            'count': len(outliers),
            'indices': outliers.index.tolist(),
            'values': outliers[column].tolist()
        }

        return outliers

    def impute_missing(self, df, column):
        """Impute missing values with configured method."""
        missing_mask = df[column].isnull()
        n_missing = missing_mask.sum()

        if n_missing == 0:
            return df

        logging.info(f"Imputing {n_missing} missing values in {column} using {self.config.imputation_method}")

        if self.config.imputation_method == 'linear':
            df[column] = df[column].interpolate(method='linear')
        elif self.config.imputation_method == 'forward_fill':
            df[column] = df[column].fillna(method='ffill')
        else:
            raise ValueError(f"Unknown imputation method: {self.config.imputation_method}")

        # Log imputed values for transparency
        imputed_values = df.loc[missing_mask, column].tolist()
        self.quality_report[f'imputed_{column}'] = {
            'count': n_missing,
            'indices': missing_mask[missing_mask].index.tolist(),
            'values': imputed_values
        }

        return df

    def smooth_outliers(self, df, column, outlier_indices):
        """Replace outliers with smoothed values."""
        for idx in outlier_indices:
            # 3-day moving average
            window_start = max(0, idx - 1)
            window_end = min(len(df), idx + 2)
            smoothed_value = df.loc[window_start:window_end, column].mean()

            logging.info(f"Smoothing outlier at index {idx}: {df.loc[idx, column]:.0f} → {smoothed_value:.0f}")

            df.loc[idx, column] = smoothed_value

        return df

    def validate_physical_constraints(self, df):
        """Check physical plausibility of data."""
        # Example: Infection counts must be non-negative
        if (df['infections'] < 0).any():
            raise ValueError("Negative infection counts detected!")

        # Example: Growth rate within plausible range
        df['growth_rate'] = df.groupby('city')['infections'].pct_change()
        extreme_growth = df[df['growth_rate'] > 2.0]  # >200% daily growth is suspicious

        if len(extreme_growth) > 0:
            logging.warning(f"Extreme growth rates detected: {len(extreme_growth)} instances")
            self.quality_report['extreme_growth'] = extreme_growth[['city', 'day', 'growth_rate']].to_dict('records')

    def run_pipeline(self, input_path, output_path):
        """Execute full preprocessing pipeline."""
        # Load
        df = self.load_raw_data(input_path)

        # Quality checks
        df = self.check_completeness(df)

        # Detect outliers (before imputation, so we don't impute outliers)
        outliers_infection = self.detect_outliers(df, 'infections')

        # Impute missing
        df = self.impute_missing(df, 'infections')

        # Smooth outliers
        df = self.smooth_outliers(df, 'infections', outliers_infection.index.tolist())

        # Final validation
        self.validate_physical_constraints(df)

        # Save processed data
        df.to_csv(output_path, index=False)
        logging.info(f"Processed data saved to {output_path}")

        # Save quality report
        import json
        with open(output_path.replace('.csv', '_quality_report.json'), 'w') as f:
            json.dump(self.quality_report, f, indent=2)

        logging.info("Preprocessing complete!")

        return df, self.quality_report

# Usage
if __name__ == '__main__':
    config = PreprocessingConfig(
        missing_value_threshold=0.05,
        outlier_iqr_multiplier=3.0,
        imputation_method='linear'
    )

    preprocessor = DataPreprocessor(config)
    df, report = preprocessor.run_pipeline(
        input_path='data/raw/infections.csv',
        output_path='data/processed/infections_clean.csv'
    )

    print(f"Preprocessing complete. Quality report:")
    print(json.dumps(report, indent=2))
```

**Why This Works**:
- ✅ Fully reproducible (anyone can run this script and get same result)
- ✅ Configurable (change thresholds without editing code)
- ✅ Logged (every decision recorded)
- ✅ Validated (physical constraints checked)
- ✅ Documented (docstrings explain every function)

#### ❌ Anti-Pattern 2: Manual, Irreproducible Preprocessing

**Bad Example**:
```python
# I opened the CSV in Excel, found some weird values, deleted them, saved as CSV
df = pd.read_csv('data_manually_fixed.csv')
```

**Why This Fails**:
- ❌ Not reproducible (what did you delete? why?)
- ❌ Not auditable (judges can't verify your work)
- ❌ Not scalable (what if problem changes?)
- ❌ Excel may corrupt data (floating point errors, date formatting)

---

#### ✅ Pattern 3: Data Provenance Documentation

**O Award Example** (2425454):
```markdown
## Data Provenance

### Source Data

**Dataset 1: Daily Infection Counts**
- **Source**: Problem Statement, Table 2 (page 3)
- **Format**: CSV, 15 cities × 90 days
- **Units**: Count of confirmed infections per day
- **Collection Method**: Official health department reports (per problem statement)
- **Time Range**: Jan 1 - Mar 31, 2024
- **Granularity**: Daily, city-level
- **Known Limitations**:
  - Reporting delays (2-3 day lag typical)
  - Testing capacity constraints (may undercount true infections)
  - Definition changes (asymptomatic cases added on Day 20)

**Dataset 2: Air Traffic Network**
- **Source**: Problem Statement, Table 3 (page 5)
- **Format**: Adjacency matrix, 15×15
- **Units**: Passengers per day (pre-pandemic baseline)
- **Collection Method**: Airport authority data
- **Time Range**: 2019 average (pre-COVID baseline)
- **Known Limitations**:
  - Does not account for pandemic-induced travel restrictions
  - Seasonal variation not captured (annual average)

### Derived Data

**R_effective (Effective Reproduction Number)**
- **Derived From**: Daily infection counts (Dataset 1)
- **Method**: EpiEstim package (Cori et al. 2013)
- **Assumptions**: Serial interval ~ Gamma(mean=7, sd=3) days
- **Validation**: Compared with literature estimates for COVID-19 (matches within 10%)

**Network Centrality (Betweenness)**
- **Derived From**: Air traffic network (Dataset 2)
- **Method**: NetworkX betweenness_centrality() function
- **Interpretation**: Fraction of shortest paths passing through each city
- **Use**: Identifies hub cities for intervention targeting

### Transformations Log

| Date | Transformation | Rationale | Impact |
|------|----------------|-----------|--------|
| 2025-02-15 | Imputed 27 missing values (2%) | Enable complete time series analysis | RMSE of model changes by <1% |
| 2025-02-15 | Smoothed 1 outlier (City 12, Day 45) | 10× spike inconsistent with deaths data | Model convergence improves (R-hat: 1.3 → 1.02) |
| 2025-02-16 | Log-transformed infection counts | Stabilize variance for regression | Residuals become homoscedastic |
| 2025-02-16 | Normalized network weights (sum to 1) | Ensure transmission rates comparable across cities | Interpretability improvement |

### Data Versioning

- **v1.0**: Raw data as provided in problem statement
- **v1.1**: After missing value imputation (2025-02-15)
- **v1.2**: After outlier smoothing (2025-02-15)
- **v2.0**: After log-transform and normalization (2025-02-16) ← **Used in final model**

All versions stored in `data/versions/` with MD5 checksums for integrity verification.
```

**Why This Works**:
- ✅ Complete chain of custody (raw → processed)
- ✅ Every transformation justified and dated
- ✅ Limitations acknowledged (shows honesty)
- ✅ Versioned (can revert if needed)
- ✅ Reproducible (MD5 checksums ensure file integrity)

#### ❌ Anti-Pattern 3: Unknown Data Origins

**Bad Example**:
```markdown
We used infection data from the problem and some network data we found.
```

**Why This Fails**:
- ❌ "Some network data we found" = where? reliable?
- ❌ No documentation of transformations
- ❌ Judges can't verify validity

---

#### ✅ Pattern 4: Sensitivity to Preprocessing Choices

**O Award Example** (2401298):
```markdown
## Preprocessing Sensitivity Analysis

To ensure our results are robust to preprocessing choices, we tested alternatives:

### Experiment 1: Imputation Method

**Question**: Does imputation method affect conclusions?

**Methods Tested**:
- A. Linear interpolation (chosen method)
- B. Forward fill
- C. Kalman filter
- D. Remove rows with missing values

**Metric**: RMSE of model predictions on validation set

**Results**:
| Method | RMSE | Difference from (A) | Conclusion |
|--------|------|---------------------|------------|
| A. Linear | 4.2 | Baseline | — |
| B. Forward fill | 4.3 | +2.4% | Negligible difference |
| C. Kalman filter | 4.1 | -2.4% | Slightly better but more complex |
| D. Remove rows | 4.9 | +16.7% | Loses too much data |

**Decision**: Use linear interpolation (A) - simple, effective, well-understood

### Experiment 2: Outlier Treatment

**Question**: Should we smooth the outlier or keep it?

**Methods Tested**:
- A. 3-day moving average smoothing (chosen method)
- B. Keep outlier as-is
- C. Remove entire day from dataset

**Metric**: Model convergence (R-hat for Bayesian inference)

**Results**:
| Method | R-hat | Convergence | Conclusion |
|--------|-------|-------------|------------|
| A. Smoothing | 1.02 | ✅ Converged | — |
| B. Keep outlier | 1.37 | ❌ Diverged | Outlier causes numerical instability |
| C. Remove day | 1.05 | ✅ Converged | Acceptable but loses information |

**Decision**: Use smoothing (A) - preserves information while enabling convergence

### Experiment 3: Normalization

**Question**: Should we normalize network weights?

**Methods Tested**:
- A. Normalize to sum=1 (chosen method)
- B. Raw passenger counts

**Metric**: Interpretability of transmission parameter β

**Results**:
- A. Normalized: β = 0.35 (interpretable as "35% of contacts result in transmission")
- B. Raw: β = 2.8e-6 (difficult to interpret, units unclear)

**Decision**: Use normalization (A) - dramatically improves interpretability

### Overall Finding

**Robustness**: Model predictions vary by <5% across all reasonable preprocessing choices
**Conclusion**: Results are robust to preprocessing; not artifacts of data manipulation
```

**Why This Works**:
- ✅ Tests multiple alternatives (not just asserting one is best)
- ✅ Quantifies impact on results (not subjective)
- ✅ Shows robustness (builds confidence)
- ✅ Decisions justified by evidence

#### ❌ Anti-Pattern 4: Arbitrary Preprocessing Choices

**Bad Example**:
```markdown
We removed outliers because they looked weird.
```

**Why This Fails**:
- ❌ "Looked weird" = subjective, not rigorous
- ❌ No testing of alternatives
- ❌ No evidence results are robust

---

### Your O Award Checklist (Review Before Handoff)

**Data Quality**:
- [ ] Completeness quantified (% missing)?
- [ ] Every missing value explained or imputed with justification?
- [ ] Outliers detected and investigated (not blindly removed)?
- [ ] Physical plausibility checks performed?

**Reproducibility**:
- [ ] Preprocessing pipeline is scripted (not manual)?
- [ ] Every transformation logged with rationale?
- [ ] Configuration parameters documented?
- [ ] Data versioned with checksums?

**Provenance**:
- [ ] Source of every dataset documented?
- [ ] Known limitations acknowledged?
- [ ] Derived data calculations explained?
- [ ] Transformation log complete?

**Robustness**:
- [ ] Tested alternative preprocessing methods?
- [ ] Quantified sensitivity to choices?
- [ ] Results robust to reasonable variations?
