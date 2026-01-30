# MANDATORY Sanity Checks

> [!CAUTION]
> **Before saving results, you MUST verify outputs make sense.**
> **The #1 failure mode is generating results that are obviously wrong.**

## Required Sanity Checks

**1. First-Time Winner Verification**

If your model predicts a country will win their "first medal ever", VERIFY:

```python
# Check if country has historical medals
historical_medals = df[df['Country'] == country]['Total_Medals'].sum()
if historical_medals > 0:
    raise ValueError(f"ERROR: {country} has {historical_medals} historical medals - NOT a first-time winner!")
```

**Countries that are NEVER first-time winners** (major Olympic powers):
- USA, China, Great Britain, Russia, Germany, France, Italy, Australia, Japan, South Korea, Netherlands, Hungary, Spain, Canada, Brazil, Kenya, Jamaica, Cuba, Poland, Sweden, Norway, Switzerland

**2. Medal Count Bounds**

```python
# No country should predict > 200 total medals (US record is ~126)
assert predicted_total <= 200, f"Unrealistic: {country} predicted {predicted_total} medals"

# No country should predict > 50 golds (US/China record is ~40-48)
assert predicted_gold <= 60, f"Unrealistic: {country} predicted {predicted_gold} golds"
```

**3. Consistency Check**

```python
# Total = Gold + Silver + Bronze
assert predicted_total == predicted_gold + predicted_silver + predicted_bronze
```

**4. Prediction Interval Validation**

```python
# Confidence intervals must be valid
assert all(ci_upper >= ci_lower), "Invalid confidence intervals!"
assert all(ci_mean >= ci_lower), "Mean below lower bound!"
assert all(ci_mean <= ci_upper), "Mean above upper bound!"
```
