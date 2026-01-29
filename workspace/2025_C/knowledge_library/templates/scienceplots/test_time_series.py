# -*- coding: utf-8 -*-
"""
Test script for time series template with sample data
"""

import sys
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
years = np.arange(1992, 2025, 2)
predictions = 100 + 2 * (years - 1992) / 2 + np.random.normal(0, 5, len(years))
pi_lower = predictions - 10
pi_upper = predictions + 10

data = pd.DataFrame({
    'year': years,
    'predictions': predictions,
    'PI_2.5': pi_lower,
    'PI_97.5': pi_upper
})

# Save sample data
data.to_csv('output/sample_time_series.csv', index=False, encoding='utf-8')
print("Sample data created: output/sample_time_series.csv")
print(data.head())
