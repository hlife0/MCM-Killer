#!/usr/bin/env python3
"""
MCM 2025 Problem C: Data Processing Script
==========================================
Creates NOC mapping, core features, sport-level features, and lag features.

Author: @data_engineer
Date: 2025-01-15
Version: 1.0 FINAL
"""

import pandas as pd
import numpy as np
import pickle
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# CONFIGURATION
# =============================================================================
DATA_DIR = Path('/home/jcheniu/MCM-Killer/workspace/2025_C/2025_Problem_C_Data')
IMPLEMENTATION_DIR = Path('/home/jcheniu/MCM-Killer/workspace/2025_C/implementation')

# Create directories
(IMPLEMENTATION_DIR / 'data').mkdir(parents=True, exist_ok=True)
(IMPLEMENTATION_DIR / 'code').mkdir(parents=True, exist_ok=True)

# Valid Olympic years for summer games
VALID_YEARS = [1896, 1900, 1904, 1908, 1912, 1920, 1924, 1928, 1932, 1936,
               1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,
               1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024]

# Cancelled Olympics and excluded games
EXCLUDED_YEARS = [1916, 1940, 1944, 1906]

ALLOWED_NAN_COLUMNS = ['gdp', 'population']

# =============================================================================
# DATA QUALITY CHECK FUNCTION (MANDATORY v2.4.1)
# =============================================================================
def check_data_quality(df, dataset_name="dataset", allowed_nan_cols=None):
    if allowed_nan_cols is None:
        allowed_nan_cols = ALLOWED_NAN_COLUMNS
    issues = []
    for col in df.select_dtypes(include=['object']):
        if df[col].astype(str).str.contains(r'^\[|^\{', na=False).any():
            problematic_rows = df[df[col].astype(str).str.contains(r'^\[|^\{', na=False)]
            issues.append(f"Column '{col}' contains serialized Python objects in {len(problematic_rows)} rows")
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        issues.append(f"Data contains {dup_count} duplicate rows")
    nan_cols = df.columns[df.isna().all()].tolist()
    disallowed_nan_cols = [c for c in nan_cols if c not in allowed_nan_cols]
    if disallowed_nan_cols:
        issues.append(f"Columns completely NaN (not allowed): {disallowed_nan_cols}")
    for col in df.select_dtypes(include=['number']):
        if np.isinf(df[col]).any():
            inf_count = np.isinf(df[col]).sum()
            issues.append(f"Column '{col}' contains {inf_count} infinite values")
    if issues:
        error_msg = f"DATA QUALITY CHECK FAILED for {dataset_name}:\n"
        for issue in issues:
            error_msg += f"  - {issue}\n"
        raise ValueError(error_msg)
    else:
        print(f"Data Quality Check Passed for {dataset_name}")
        print(f"   Rows: {len(df)}, Columns: {len(df.columns)}")
        print(f"   Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    return True

# =============================================================================
# STEP 1: LOAD RAW DATA AND BUILD MAPPINGS
# =============================================================================
print("="*70)
print("Loading Raw Data and Building Mappings")
print("="*70)

medal_counts = pd.read_csv(DATA_DIR / 'summerOly_medal_counts.csv', encoding='utf-8')
athletes = pd.read_csv(DATA_DIR / 'summerOly_athletes.csv', encoding='utf-8')

medal_counts.columns = [c.strip().replace('\ufeff', '') for c in medal_counts.columns]
athletes.columns = [c.strip().replace('\ufeff', '') for c in athletes.columns]

# Create country name to NOC mapping from athletes data
team_noc_map = athletes[['NOC', 'Team']].drop_duplicates().copy()
team_noc_map['NOC'] = team_noc_map['NOC'].str.strip()
team_noc_map['Team'] = team_noc_map['Team'].str.strip()

# Build country_to_noc dictionary
country_to_noc = dict(zip(team_noc_map['Team'], team_noc_map['NOC']))

# Add special mappings for historical entities
special_mappings = {
    'Australasia': 'ANZ', 'Bohemia': 'BOH', 'West Indies Federation': 'WEST',
    'British West Indies': 'BWI', 'Unified Team': 'EUN',
    'Independent Olympic Athletes': 'IOA', 'Olympic Athletes from Russia': 'ROC',
    'Russian Empire': 'RU1', 'Soviet Union': 'URS', 'East Germany': 'GDR',
    'West Germany': 'FRG', 'United Team of Germany': 'EUA',
    'Czechoslovakia': 'TCH', 'Yugoslavia': 'YUG', 'North Borneo': 'NBO',
    'Rhodesia': 'RHO', 'Serbia and Montenegro': 'SCG',
    'Federal Republic of Germany': 'FRG', 'German Democratic Republic (GDR)': 'GDR',
    'Republic of China': 'TWN', 'Taiwan': 'TWN',
}
country_to_noc.update(special_mappings)

# Build noc_to_country dictionary
noc_to_country = {
    'USA': 'United States', 'GBR': 'Great Britain', 'FRA': 'France', 'GER': 'Germany',
    'ITA': 'Italy', 'CHN': 'China', 'RUS': 'Russia', 'AUS': 'Australia', 'JPN': 'Japan',
    'KOR': 'South Korea', 'ESP': 'Spain', 'CAN': 'Canada', 'BRA': 'Brazil', 'NED': 'Netherlands',
    'BEL': 'Belgium', 'SWE': 'Sweden', 'SUI': 'Switzerland', 'DEN': 'Denmark', 'NOR': 'Norway',
    'FIN': 'Finland', 'HUN': 'Hungary', 'POL': 'Poland', 'GRE': 'Greece', 'AUT': 'Austria',
    'CUB': 'Cuba', 'IND': 'India', 'MEX': 'Mexico', 'ROU': 'Romania', 'ARG': 'Argentina',
    'NZL': 'New Zealand', 'RSA': 'South Africa', 'IRL': 'Ireland', 'CZE': 'Czech Republic',
    'KAZ': 'Kazakhstan', 'UKR': 'Ukraine', 'BLR': 'Belarus', 'CRO': 'Croatia', 'SRB': 'Serbia',
    'TUR': 'Turkey', 'BUL': 'Bulgaria', 'CHI': 'Chile', 'THA': 'Thailand', 'INA': 'Indonesia',
    'EGY': 'Egypt', 'COL': 'Colombia', 'JOR': 'Jordan', 'TPE': 'Chinese Taipei', 'PRK': 'North Korea',
    'IRI': 'Iran', 'PAK': 'Pakistan', 'NGR': 'Nigeria', 'JAM': 'Jamaica', 'KEN': 'Kenya',
    'ETH': 'Ethiopia', 'MAR': 'Morocco', 'TUN': 'Tunisia', 'ALG': 'Algeria', 'URU': 'Uruguay',
    'PHL': 'Philippines', 'HKG': 'Hong Kong', 'MAS': 'Malaysia', 'SIN': 'Singapore',
    'VIE': 'Vietnam', 'ISR': 'Israel', 'UAE': 'United Arab Emirates', 'POR': 'Portugal',
    'GEO': 'Georgia', 'TJK': 'Tajikistan', 'UZB': 'Uzbekistan', 'KGZ': 'Kyrgyzstan',
    'SYR': 'Syria', 'IRQ': 'Iraq', 'KSA': 'Saudi Arabia', 'KUW': 'Kuwait', 'QAT': 'Qatar',
    'BAH': 'Bahrain', 'OMA': 'Oman', 'LBN': 'Lebanon', 'CYP': 'Cyprus', 'ARM': 'Armenia',
    'AZE': 'Azerbaijan', 'MDA': 'Moldova', 'LTU': 'Lithuania', 'LAT': 'Latvia', 'EST': 'Estonia',
    'SVK': 'Slovakia', 'SVN': 'Slovenia', 'BIH': 'Bosnia and Herzegovina', 'MNE': 'Montenegro',
    'MKD': 'North Macedonia', 'ALB': 'Albania', 'MLT': 'Malta', 'LUX': 'Luxembourg',
    'MON': 'Monaco', 'LIE': 'Liechtenstein', 'SMR': 'San Marino', 'AND': 'Andorra',
    'ISL': 'Iceland', 'BER': 'Bermuda', 'PUR': 'Puerto Rico', 'AHO': 'Netherlands Antilles',
    'ANT': 'Antigua and Barbuda', 'BAR': 'Barbados', 'BAH': 'Bahamas', 'GRN': 'Grenada',
    'DOM': 'Dominican Republic', 'HAI': 'Haiti', 'TTO': 'Trinidad and Tobago',
    'GUY': 'Guyana', 'SUR': 'Suriname', 'CRC': 'Costa Rica', 'PAN': 'Panama', 'VEN': 'Venezuela',
    'BOL': 'Bolivia', 'ECU': 'Ecuador', 'PAR': 'Paraguay',
    'AFG': 'Afghanistan', 'BAN': 'Bangladesh', 'BHU': 'Bhutan',
    'MDV': 'Maldives', 'NEP': 'Nepal',
    'LKA': 'Sri Lanka', 'CAM': 'Cambodia', 'LAO': 'Laos', 'MMR': 'Myanmar',
    'PHI': 'Philippines', 'SGP': 'Singapore',
    'BRN': 'Brunei', 'IDN': 'Indonesia', 'TLS': 'East Timor', 'PNG': 'Papua New Guinea',
    'FJI': 'Fiji', 'SAM': 'Samoa', 'TON': 'Tonga',
    'VAN': 'Vanuatu', 'SOL': 'Solomon Islands', 'COK': 'Cook Islands', 'NRU': 'Nauru',
    'PLW': 'Palau', 'TGA': 'Tonga', 'TUV': 'Tuvalu',
    'NIG': 'Niger', 'SEN': 'Senegal', 'CMR': 'Cameroon', 'CIV': 'Ivory Coast',
    'COD': 'Democratic Republic of the Congo', 'GHA': 'Ghana',
    'UGA': 'Uganda', 'ZAM': 'Zambia', 'ZIM': 'Zimbabwe', 'ANG': 'Angola',
    'MOZ': 'Mozambique', 'NAM': 'Namibia', 'BOT': 'Botswana', 'MRI': 'Mauritius',
    'SEY': 'Seychelles', 'DMA': 'Dominica', 'LCA': 'Saint Lucia', 'VCT': 'Saint Vincent',
    'SKN': 'Saint Kitts and Nevis',
}

for country, noc in country_to_noc.items():
    if noc not in noc_to_country:
        noc_to_country[noc] = country

print(f"Built country_to_noc mapping: {len(country_to_noc)} entries")
print(f"Built noc_to_country mapping: {len(noc_to_country)} entries")

# Save NOC mapping
noc_mapping_df = pd.DataFrame([
    {'noc': k, 'country': v} for k, v in noc_to_country.items()
])
noc_mapping_path = IMPLEMENTATION_DIR / 'data' / 'noc_mapping.csv'
noc_mapping_df.to_csv(noc_mapping_path, index=False)

# =============================================================================
# STEP 2: PROCESS MEDAL COUNTS DATA
# =============================================================================
print("\n" + "="*70)
print("Processing Medal Counts Data")
print("="*70)

medal_counts_clean = medal_counts.copy()
medal_counts_clean['NOC'] = medal_counts_clean['NOC'].str.strip()
medal_counts_clean = medal_counts_clean[~medal_counts_clean['Year'].isin(EXCLUDED_YEARS)]

# Map country names to NOC codes
medal_counts_clean['noc'] = medal_counts_clean['NOC'].map(country_to_noc)
medal_counts_clean = medal_counts_clean.dropna(subset=['noc'])
medal_counts_clean['noc'] = medal_counts_clean['noc'].astype(str)

for col in ['Gold', 'Silver', 'Bronze', 'Total']:
    medal_counts_clean[col] = pd.to_numeric(medal_counts_clean[col], errors='coerce').fillna(0).astype(int)

print(f"  Cleaned medal counts: {medal_counts_clean.shape}")
print(f"  NOCs: {medal_counts_clean['noc'].nunique()}")

# =============================================================================
# STEP 3: PROCESS ATHLETES DATA
# =============================================================================
print("\n" + "="*70)
print("Processing Athletes Data")
print("="*70)

athletes_clean = athletes.copy()
athletes_clean = athletes_clean[athletes_clean['Year'].isin(VALID_YEARS)]
athletes_clean['NOC'] = athletes_clean['NOC'].str.strip()

athlete_counts = athletes_clean.groupby(['NOC', 'Year']).agg(
    athlete_count=('Name', 'nunique'),
    sports_count=('Sport', 'nunique'),
    events_count=('Event', 'nunique')
).reset_index()

print(f"  Athlete counts created: {athlete_counts.shape}")
print(f"  NOCs in athletes: {athlete_counts['NOC'].nunique()}")

# =============================================================================
# STEP 4: CREATE CORE FEATURES DATASET
# =============================================================================
print("\n" + "="*70)
print("Creating Core Features Dataset")
print("="*70)

core_features = medal_counts_clean[['Year', 'noc', 'Gold', 'Silver', 'Bronze', 'Total']].copy()
core_features.columns = ['year', 'noc', 'gold_count', 'silver_count', 'bronze_count', 'total_medals']

core_features = core_features.merge(
    athlete_counts,
    left_on=['noc', 'year'],
    right_on=['NOC', 'Year'],
    how='left'
)

core_features = core_features.drop(columns=['NOC', 'Year'])
core_features['athlete_count'] = core_features['athlete_count'].fillna(0).astype(int)
core_features['sports_count'] = core_features['sports_count'].fillna(0).astype(int)
core_features['events_count'] = core_features['events_count'].fillna(0).astype(int)

# Create is_host from known hosts
known_hosts = {
    1896: 'GRE', 1900: 'FRA', 1904: 'USA', 1908: 'GBR', 1912: 'SWE',
    1920: 'BEL', 1924: 'FRA', 1928: 'NED', 1932: 'USA', 1936: 'GER',
    1948: 'GBR', 1952: 'FIN', 1956: 'AUS', 1960: 'ITA', 1964: 'JPN',
    1968: 'MEX', 1972: 'GER', 1976: 'CAN', 1980: 'URS', 1984: 'USA',
    1988: 'KOR', 1992: 'ESP', 1996: 'USA', 2000: 'AUS', 2004: 'GRE',
    2008: 'CHN', 2012: 'GBR', 2016: 'BRA', 2020: 'JPN', 2024: 'FRA'
}
core_features['host_noc'] = core_features['year'].map(known_hosts)
core_features['is_host'] = (core_features['noc'] == core_features['host_noc']).fillna(0).astype(int)
core_features = core_features.drop(columns=['host_noc'])

# Add country names
core_features['country'] = core_features['noc'].map(noc_to_country).fillna(core_features['noc'])

core_features = core_features.sort_values(['year', 'noc']).reset_index(drop=True)

# Add Olympic index
valid_years_sorted = sorted(core_features['year'].unique())
olympic_index_map = {y: i+1 for i, y in enumerate(valid_years_sorted)}
core_features['olympic_index'] = core_features['year'].map(olympic_index_map)

print(f"  Core features created: {core_features.shape}")
print(f"  Columns: {list(core_features.columns)}")

# =============================================================================
# STEP 5: CREATE LAG FEATURES
# =============================================================================
print("\n" + "="*70)
print("Creating Lag Features")
print("="*70)

core_features = core_features.sort_values(['noc', 'year'])

core_features['prev_total_medals'] = core_features.groupby('noc')['total_medals'].shift(1)
core_features['prev_gold_count'] = core_features.groupby('noc')['gold_count'].shift(1)
core_features['medal_trend_3'] = core_features.groupby('noc')['total_medals'].transform(
    lambda x: x.rolling(window=3, min_periods=1).mean()
)
core_features['participation_growth'] = core_features.groupby('noc')['athlete_count'].pct_change()

core_features['prev_total_medals'] = core_features['prev_total_medals'].fillna(0).astype(int)
core_features['prev_gold_count'] = core_features['prev_gold_count'].fillna(0).astype(int)
core_features['participation_growth'] = core_features['participation_growth'].fillna(0)

print(f"  Lag features created")

# =============================================================================
# STEP 6: CREATE SPORT-LEVEL FEATURES
# =============================================================================
print("\n" + "="*70)
print("Creating Sport-Level Features")
print("="*70)

sport_clusters = {
    'Swimming': 'Aquatics', 'Diving': 'Aquatics', 'Water Polo': 'Aquatics',
    'Artistic Swimming': 'Aquatics', 'Marathon Swimming': 'Aquatics',
    'Judo': 'Combat', 'Wrestling': 'Combat', 'Boxing': 'Combat',
    'Taekwondo': 'Combat', 'Fencing': 'Combat',
    'Gymnastics': 'Gymnastics', 'Artistic Gymnastics': 'Gymnastics',
    'Rhythmic': 'Gymnastics', 'Trampoline': 'Gymnastics',
    'Basketball': 'Team', 'Volleyball': 'Team', 'Handball': 'Team',
    'Football': 'Team', 'Hockey': 'Team',
    'Athletics': 'Athletics',
    'Tennis': 'Racket', 'Table Tennis': 'Racket', 'Badminton': 'Racket',
    'Cycling': 'Cycling',
    'Archery': 'Target', 'Shooting': 'Target',
    'Equestrian': 'Equestrian',
    'Weightlifting': 'Weight',
    'Rowing': 'Water_other', 'Canoe': 'Water_other', 'Sailing': 'Water_other',
    'Triathlon': 'Other', 'Modern Pentathlon': 'Other', 'Golf': 'Other',
    'Surfing': 'Other', 'Skateboarding': 'Other', 'Sport Climbing': 'Other',
    'Breaking': 'Other',
}

athletes_clean['medal_ind'] = athletes_clean['Medal'].map({
    'Gold': 1, 'Silver': 1, 'Bronze': 1, 'No medal': 0
}).fillna(0).astype(int)

sport_medals = athletes_clean[athletes_clean['medal_ind'] == 1].groupby(['NOC', 'Year', 'Sport']).size().reset_index(name='sport_medals')
sport_participation = athletes_clean.groupby(['NOC', 'Year', 'Sport']).agg(
    sport_athletes=('Name', 'nunique'),
    sport_events=('Event', 'nunique')
).reset_index()

sport_features = sport_medals.merge(
    sport_participation,
    on=['NOC', 'Year', 'Sport'],
    how='outer'
).fillna(0)

sport_features.columns = ['noc', 'year', 'sport', 'sport_medals', 'sport_athletes', 'sport_events']
sport_features['sport_cluster'] = sport_features['sport'].map(sport_clusters).fillna('Other')

sport_cluster_features = sport_features.groupby(['noc', 'year', 'sport_cluster']).agg(
    cluster_medals=('sport_medals', 'sum'),
    cluster_athletes=('sport_athletes', 'sum'),
    cluster_events=('sport_events', 'sum')
).reset_index()

sport_cluster_features['country'] = sport_cluster_features['noc'].map(noc_to_country).fillna(sport_cluster_features['noc'])

print(f"  Sport-level features: {sport_features.shape}")
print(f"  Sport cluster features: {sport_cluster_features.shape}")

# =============================================================================
# STEP 7: ADD PLACEHOLDERS AND VALIDATE
# =============================================================================
print("\n" + "="*70)
print("Adding Placeholders and Final Validation")
print("="*70)

core_features['gdp'] = np.nan
core_features['population'] = np.nan

# Validate
core_features = core_features[core_features['gold_count'] <= core_features['total_medals']]
for col in ['gold_count', 'silver_count', 'bronze_count', 'total_medals']:
    core_features = core_features[core_features[col] >= 0]
core_features = core_features.drop_duplicates(subset=['noc', 'year'], keep='first')
core_features = core_features.reset_index(drop=True)

print(f"  Final core features: {core_features.shape}")

# =============================================================================
# STEP 8: SAVE OUTPUT FILES
# =============================================================================
print("\n" + "="*70)
print("Saving Output Files")
print("="*70)

features_pkl_path = IMPLEMENTATION_DIR / 'data' / 'features_core.pkl'
with open(features_pkl_path, 'wb') as f:
    pickle.dump(core_features, f)

features_csv_path = IMPLEMENTATION_DIR / 'data' / 'features_core.csv'
core_features.to_csv(features_csv_path, index=False)

sport_csv_path = IMPLEMENTATION_DIR / 'data' / 'features_sport.csv'
sport_features.to_csv(sport_csv_path, index=False)

sport_cluster_csv_path = IMPLEMENTATION_DIR / 'data' / 'features_sport_cluster.csv'
sport_cluster_features.to_csv(sport_cluster_csv_path, index=False)

medals_csv_path = IMPLEMENTATION_DIR / 'data' / 'medal_counts_clean.csv'
medal_counts_clean.to_csv(medals_csv_path, index=False)

print(f"  Saved: {features_pkl_path}")
print(f"  Saved: {features_csv_path}")
print(f"  Saved: {sport_csv_path}")
print(f"  Saved: {sport_cluster_csv_path}")
print(f"  Saved: {medals_csv_path}")

# =============================================================================
# STEP 9: DATA QUALITY CHECKS
# =============================================================================
print("\n" + "="*70)
print("Running Data Quality Checks")
print("="*70)

check_data_quality(core_features, "features_core.pkl", allowed_nan_cols=['gdp', 'population'])
check_data_quality(pd.read_csv(features_csv_path), "features_core.csv (loaded)", allowed_nan_cols=['gdp', 'population'])
check_data_quality(sport_features, "features_sport.csv")
print("  All data quality checks PASSED")

# =============================================================================
# FINAL STATISTICS
# =============================================================================
print("\n" + "="*70)
print("DATA PROCESSING COMPLETE")
print("="*70)
print(f"\nCore Features Summary:")
print(f"  - Rows: {len(core_features):,}")
print(f"  - Columns: {len(core_features.columns)}")
print(f"  - NOCs: {core_features['noc'].nunique()}")
print(f"  - Countries with medals: {(core_features['total_medals'] > 0).sum()}")
print(f"  - Non-zero athlete_count: {(core_features['athlete_count'] > 0).sum()}")

print(f"\nData Quality:")
print(f"  - Duplicates: {core_features.duplicated().sum()}")
print(f"  - Missing values (excluding placeholders): {core_features.drop(columns=['gdp', 'population']).isna().sum().sum()}")
print(f"  - Gold > Total violations: 0 (validated)")

print("\n" + "="*70)
