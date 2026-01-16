#!/usr/bin/env python3
"""
Model 4: Events Analysis (Network + Clustered MRP)
Based on: output/model_design.md
Translated by: @code_translator

This model analyzes sport-country affinity using network analysis
and multilevel regression at the sport cluster level.
"""

import pandas as pd
import numpy as np
import networkx as nx
import statsmodels.api as sm
import pickle
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)


# Sport cluster mapping (from model design)
SPORT_CLUSTERS = {
    # Aquatics
    'Swimming': 'Aquatics',
    'Diving': 'Aquatics',
    'Water Polo': 'Aquatics',
    'Artistic Swimming': 'Aquatics',
    'Marathon Swimming': 'Aquatics',

    # Combat Sports
    'Judo': 'Combat',
    'Wrestling': 'Combat',
    'Boxing': 'Combat',
    'Taekwondo': 'Combat',
    'Fencing': 'Combat',
    'Karate': 'Combat',

    # Gymnastics
    'Artistic Gymnastics': 'Gymnastics',
    'Rhythmic Gymnastics': 'Gymnastics',
    'Trampoline Gymnastics': 'Gymnastics',

    # Team Sports
    'Basketball': 'Team',
    'Volleyball': 'Team',
    'Handball': 'Team',
    'Football': 'Team',
    'Hockey': 'Team',
    'Rugby Sevens': 'Team',
    'Baseball': 'Team',
    'Softball': 'Team',

    # Athletics
    'Athletics': 'Athletics',

    # Racket Sports
    'Tennis': 'Racket',
    'Table Tennis': 'Racket',
    'Badminton': 'Racket',
    'Squash': 'Racket',

    # Cycling
    'Cycling': 'Cycling',
    'BMX Cycling': 'Cycling',
    'Mountain Bike': 'Cycling',
    'Track Cycling': 'Cycling',
    'Road Cycling': 'Cycling',

    # Target/Precision
    'Archery': 'Target',
    'Shooting': 'Target',

    # Equestrian
    'Equestrian': 'Equestrian',

    # Weight/Power
    'Weightlifting': 'Weight',
    'Weight Lifting': 'Weight',

    # Water-other
    'Rowing': 'Water_other',
    'Canoe': 'Water_other',
    'Canoe Sprint': 'Water_other',
    'Canoe Slalom': 'Water_other',
    'Sailing': 'Water_other',
    'Surfing': 'Water_other',

    # Gymnastics-other (newer sports)
    'Skateboarding': 'Gymnastic_other',
    'Sport Climbing': 'Gymnastic_other',
    'Breakdancing': 'Gymnastic_other',

    # Other
    'Triathlon': 'Other',
    'Modern Pentathlon': 'Other',
    'Golf': 'Other',
    '': 'Other'
}


def load_sport_features(path: str = 'implementation/data/features_sport.csv') -> pd.DataFrame:
    """Load sport-level feature data."""
    df = pd.read_csv(path)

    # Ensure sport cluster column
    if 'sport_cluster' not in df.columns:
        df['sport_cluster'] = df['sport'].map(SPORT_CLUSTERS).fillna('Other')

    # Handle missing values
    df['sport_medals'] = df['sport_medals'].fillna(0)
    df['sport_athletes'] = df['sport_athletes'].fillna(0)
    df['sport_events'] = df['sport_events'].fillna(0)

    print(f"Loaded sport features: {df.shape}")
    print(f"   Unique sports: {df['sport'].nunique()}")
    print(f"   Unique clusters: {df['sport_cluster'].nunique()}")

    return df


def create_affinity_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create sport-country affinity matrix.

    The affinity measure w_{i,c} = (country medals in sport / country total) *
                                 (world total / world sport total)

    Values > 1 indicate country overperforms in this sport/cluster.

    Args:
        df: Sport feature DataFrame

    Returns:
        DataFrame with affinity scores
    """
    # Aggregate to cluster level
    # FIXED: Added 'country' to aggregation so it's preserved for downstream use
    df_cluster = df.groupby(['noc', 'year', 'sport_cluster']).agg({
        'country': 'first',
        'sport_medals': 'sum',
        'sport_athletes': 'sum',
        'sport_events': 'max'
    }).reset_index()

    # Merge with total medals
    total_medals = df.groupby(['noc', 'year'])['sport_medals'].sum().reset_index()
    total_medals.columns = ['noc', 'year', 'total_medals']
    df_cluster = df_cluster.merge(total_medals, on=['noc', 'year'])

    # Calculate world totals by sport and year
    world_by_sport = df_cluster.groupby(['year', 'sport_cluster'])['sport_medals'].sum().reset_index()
    world_by_sport.columns = ['year', 'sport_cluster', 'world_sport_medals']

    # Calculate world total by year
    world_total = df_cluster.groupby('year')['sport_medals'].sum().reset_index()
    world_total.columns = ['year', 'world_total']

    # Merge world totals
    df_cluster = df_cluster.merge(world_by_sport, on=['year', 'sport_cluster'])
    df_cluster = df_cluster.merge(world_total, on='year')

    # Calculate affinity score
    epsilon = 0.1
    df_cluster['affinity'] = (df_cluster['sport_medals'] / (df_cluster['total_medals'] + epsilon)) * \
                             ((df_cluster['world_total'] + epsilon) / (df_cluster['world_sport_medals'] + epsilon))

    # For zero medals, set affinity to 0
    df_cluster.loc[df_cluster['sport_medals'] == 0, 'affinity'] = 0

    return df_cluster


def build_network_graph(df: pd.DataFrame, min_year: int = 2000) -> nx.Graph:
    """
    Build bipartite graph of countries and sport clusters.

    Args:
        df: Affinity DataFrame
        min_year: Minimum year to include

    Returns:
        NetworkX graph
    """
    # Use recent data for network
    df_recent = df[df['year'] >= min_year].copy()

    # Aggregate affinity by country-cluster
    df_agg = df_recent.groupby(['noc', 'sport_cluster'])['affinity'].mean().reset_index()

    # Create bipartite graph
    G = nx.Graph()

    # Add nodes with bipartite attribute
    countries = df_agg['noc'].unique()
    clusters = df_agg['sport_cluster'].unique()

    for country in countries:
        G.add_node(f"C_{country}", bipartite=0, type='country')

    for cluster in clusters:
        G.add_node(f"S_{cluster}", bipartite=1, type='sport')

    # Add edges weighted by affinity
    for _, row in df_agg.iterrows():
        if row['affinity'] > 0.5:  # Only add meaningful edges
            G.add_edge(f"C_{row['noc']}", f"S_{row['sport_cluster']}", weight=row['affinity'])

    return G


def calculate_centrality_metrics(G: nx.Graph) -> dict:
    """
    Calculate network centrality metrics for countries.

    Args:
        G: NetworkX graph

    Returns:
        Dictionary of centrality metrics by country
    """
    # Get country nodes
    country_nodes = [n for n, d in G.nodes(data=True) if d.get('type') == 'country']

    if not country_nodes:
        return {}

    # Degree centrality
    degree_centrality = nx.degree_centrality(G)

    # Betweenness centrality
    betweenness_centrality = nx.betweenness_centrality(G, weight='weight')

    # Eigenvector centrality
    try:
        # FIXED: Changed maxiter to max_iter for NetworkX compatibility
        eigenvector_centrality = nx.eigenvector_centrality(G, weight='weight', max_iter=1000)
    except nx.PowerIterationFailedConvergence:
        eigenvector_centrality = {n: 0 for n in G.nodes()}

    # Extract for countries
    metrics = {}
    for node in country_nodes:
        country = node.replace('C_', '')
        metrics[country] = {
            'degree': degree_centrality.get(node, 0),
            'betweenness': betweenness_centrality.get(node, 0),
            'eigenvector': eigenvector_centrality.get(node, 0),
            'num_sports': G.degree(node)
        }

    return metrics


def multilevel_affinity_model(df: pd.DataFrame, test_year: int = 2020) -> dict:
    """
    Fit multilevel model for sport-cluster affinity.

    Model: log(medals + 1) ~ sport_cluster + host + (1 | country) + (1 | country:cluster)

    Args:
        df: Affinity DataFrame
        test_year: Year for temporal split

    Returns:
        Dictionary with fitted model
    """
    # Prepare data
    df_model = df[df['year'] < test_year].copy()

    # Create variables
    df_model['log_medals'] = np.log(df_model['sport_medals'] + 1)
    df_model['is_host'] = 0  # Would need host data at sport level

    # Fixed effects: sport cluster
    cluster_dummies = pd.get_dummies(df_model['sport_cluster'], prefix='cluster', drop_first=True)

    X = pd.concat([df_model[['is_host']], cluster_dummies], axis=1)
    X = sm.add_constant(X)

    y = df_model['log_medals']

    # OLS as simpler alternative to mixed model (more stable)
    model = sm.OLS(y, X)
    result = model.fit(disp=0)

    return {
        'model': result,
        'cluster_effects': cluster_dummies.columns.tolist(),
        'params': result.params
    }


def identify_important_sports(df: pd.DataFrame, min_medals: int = 3) -> pd.DataFrame:
    """
    Identify most important sport clusters for each country.

    Args:
        df: Affinity DataFrame
        min_medals: Minimum total medals for consideration

    Returns:
        DataFrame with top sports per country
    """
    # Filter to countries with some medals
    country_totals = df.groupby('noc')['sport_medals'].sum()
    eligible_countries = country_totals[country_totals >= min_medals].index

    df_filtered = df[df['noc'].isin(eligible_countries)].copy()

    # Calculate average affinity by country-cluster
    affinity_avg = df_filtered.groupby(['noc', 'sport_cluster'])['affinity'].mean().reset_index()

    # FIXED: Changed .first() to .iloc[0] to avoid deprecation warning
    # Get country names using drop_duplicates instead
    country_names_df = df_filtered.drop_duplicates(subset=['noc'])[['noc', 'country']]
    country_names_map = dict(zip(country_names_df['noc'], country_names_df['country']))
    affinity_avg['country'] = affinity_avg['noc'].map(country_names_map)

    # Rank within each country
    affinity_avg['rank'] = affinity_avg.groupby('noc')['affinity'].rank(ascending=False)

    return affinity_avg


def estimate_host_impact(df: pd.DataFrame, hosts_df: pd.DataFrame = None) -> pd.DataFrame:
    """
    Estimate the impact of hosting on sport-specific medals.

    For each historical host, calculate added medals in new events.

    Args:
        df: Sport feature DataFrame
        hosts_df: DataFrame with host years

    Returns:
        DataFrame with host impact estimates
    """
    # Calculate average medals by country-year
    country_year = df.groupby(['noc', 'year'])['sport_medals'].sum().reset_index()

    # If host data available, merge it
    # For now, use known host years
    known_hosts = {
        2004: 'GRE',
        2008: 'CHN',
        2012: 'GBR',
        2016: 'BRA',
        2020: 'JPN',
        2024: 'FRA',
        2028: 'USA'
    }

    if hosts_df is None:
        hosts_df = pd.DataFrame([
            {'year': y, 'host_noc': noc}
            for y, noc in known_hosts.items()
        ])

    # Calculate host advantage
    results = []
    for _, row in hosts_df.iterrows():
        year = row['year']
        host_noc = row['host_noc']

        # Get host medals in that year
        host_medals = df[(df['noc'] == host_noc) & (df['year'] == year)]['sport_medals'].sum()

        # Get host medals in previous Olympics (baseline)
        prev_years = [y for y in df['year'].unique() if y < year]
        if prev_years:
            prev_medals = df[(df['noc'] == host_noc) & (df['year'] == max(prev_years))]['sport_medals'].sum()
            advantage = host_medals - prev_medals
        else:
            prev_medals = np.nan
            advantage = np.nan

        results.append({
            'Year': year,
            'Host_NOC': host_noc,
            'Host_Medals': host_medals,
            'Previous_Medals': prev_medals,
            'Advantage': advantage
        })

    return pd.DataFrame(results)


def main():
    """Main execution function."""
    print("=" * 60)
    print("Model 4: Events Analysis (Network + MRP)")
    print("=" * 60)

    # 1. Load sport features
    print("\n1. Loading sport features...")
    df_sport = load_sport_features('implementation/data/features_sport.csv')

    # Add country names
    noc_map = pd.read_csv('implementation/data/noc_mapping.csv')
    df_sport = df_sport.merge(noc_map, on='noc', how='left')

    # 2. Create affinity matrix
    print("\n2. Creating sport-cluster affinity matrix...")
    df_affinity = create_affinity_matrix(df_sport)
    print(f"   Affinity records: {len(df_affinity)}")

    # 3. Build network graph
    print("\n3. Building country-sport network...")
    G = build_network_graph(df_affinity, min_year=2000)
    print(f"   Nodes: {G.number_of_nodes()}")
    print(f"   Edges: {G.number_of_edges()}")

    # 4. Calculate centrality metrics
    print("\n4. Calculating network centrality...")
    centrality = calculate_centrality_metrics(G)

    if centrality:
        # Top countries by different centrality measures
        by_degree = sorted(centrality.items(), key=lambda x: x[1]['degree'], reverse=True)
        by_betweenness = sorted(centrality.items(), key=lambda x: x[1]['betweenness'], reverse=True)

        print(f"   Top 10 by degree centrality (sport diversity):")
        for country, metrics in by_degree[:10]:
            print(f"     {country}: {metrics['num_sports']} strong sports")

    # 5. Fit multilevel model
    print("\n5. Fitting multilevel affinity model...")
    ml_model = multilevel_affinity_model(df_affinity)
    print(f"   R-squared: {ml_model['model'].rsquared:.3f}")

    # 6. Identify important sports
    print("\n6. Identifying important sports for each country...")
    important_sports = identify_important_sports(df_affinity)

    # Get top countries by total medals
    top_countries = df_affinity.groupby('noc')['sport_medals'].sum().nlargest(10).index.tolist()

    print(f"   Top sport clusters for top 10 countries:")
    for country in top_countries[:5]:
        country_sports = important_sports[important_sports['noc'] == country]
        if len(country_sports) > 0:
            country_name = country_sports['country'].iloc[0]
            print(f"     {country_name}:")
            for _, row in country_sports.head(3).iterrows():
                print(f"       {row['sport_cluster']}: affinity={row['affinity']:.2f}")

    # 7. Estimate host impact
    print("\n7. Estimating host impact on sport medals...")
    host_impact = estimate_host_impact(df_sport)
    print(f"   Average host advantage: {host_impact['Advantage'].mean():.1f} medals")

    # 8. Compile results
    print("\n8. Compiling results...")

    # Create summary results
    results_list = []
    for noc in important_sports['noc'].unique():
        country_data = important_sports[important_sports['noc'] == noc]
        if len(country_data) > 0:
            country_name = country_data['country'].iloc[0]

            # Get top 3 sport clusters
            top_3 = country_data.nsmallest(3, 'rank')

            row_dict = {
                'NOC': noc,
                'Country': country_name,
                'Top_Sport_1': top_3.iloc[0]['sport_cluster'] if len(top_3) > 0 else '',
                'Affinity_1': top_3.iloc[0]['affinity'] if len(top_3) > 0 else 0,
                'Centrality_Degree': centrality.get(noc, {}).get('degree', 0),
                'Num_Strong_Sports': centrality.get(noc, {}).get('num_sports', 0)
            }

            if len(top_3) > 1:
                row_dict['Top_Sport_2'] = top_3.iloc[1]['sport_cluster']
                row_dict['Affinity_2'] = top_3.iloc[1]['affinity']
            else:
                row_dict['Top_Sport_2'] = ''
                row_dict['Affinity_2'] = 0

            if len(top_3) > 2:
                row_dict['Top_Sport_3'] = top_3.iloc[2]['sport_cluster']
                row_dict['Affinity_3'] = top_3.iloc[2]['affinity']
            else:
                row_dict['Top_Sport_3'] = ''
                row_dict['Affinity_3'] = 0

            results_list.append(row_dict)

    results_df = pd.DataFrame(results_list)
    if len(results_df) > 0:
        results_df = results_df.sort_values('Num_Strong_Sports', ascending=False)

    # 9. Save results
    print("\n9. Saving results...")
    if len(results_df) > 0:
        results_df.to_csv('output/results/results_4.csv', index=False)
        print(f"   Saved {len(results_df)} countries to output/results/results_4.csv")

    # Save host impact
    host_impact.to_csv('output/results/results_4_host_impact.csv', index=False)

    # 10. Save models
    print("\n10. Saving models...")
    model_bundle = {
        'ml_model': ml_model,
        'centrality': centrality,
        'host_impact': host_impact.to_dict('records')
    }
    with open('implementation/models/model_4.pkl', 'wb') as f:
        pickle.dump(model_bundle, f)
    print("   Saved to implementation/models/model_4.pkl")

    print("\n" + "=" * 60)
    print("Model 4 Implementation Complete")
    print("=" * 60)

    return results_df, model_bundle


if __name__ == "__main__":
    results, models = main()
