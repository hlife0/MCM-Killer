#!/usr/bin/env python3
"""
Phase 4: Data Loading and Preprocessing

Loads features_core.csv and prepares data for Stan models.
Implements all DATA Gate requirements:
- Filter special entities
- Handle NA values
- Time series split
- Convert to Stan format
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_and_preprocess_data(csv_path='output/implementation/data/features_core.csv'):
    """
    加载和预处理数据

    Returns:
        train: DataFrame, training data (year <= 2016)
        test: DataFrame, test data (year >= 2020)
        stan_data: dict, Stan data dictionary
        feature_cols: list, list of feature column names
    """
    print("=" * 60)
    print("Step 1: 加载和预处理数据")
    print("=" * 60)

    # 1. 加载数据
    print("\n1.1 加载 features_core.csv...")
    features = pd.read_csv(csv_path)
    print(f"   原始数据: {len(features)} 行 × {len(features.columns)} 列")

    # 2. 过滤特殊实体 (DATA Gate 要求)
    print("\n1.2 过滤特殊实体...")
    historical_entities = ['Mixed team', 'Australasia', 'Bohemia']
    n_before = len(features)
    features = features[~features['NOC'].isin(historical_entities)]
    n_after = len(features)
    print(f"   过滤前: {n_before} 行")
    print(f"   过滤后: {n_after} 行")
    print(f"   移除: {n_before - n_after} 行")

    # 3. 处理 NA 值 (填充 0)
    print("\n1.3 处理 NA 值...")
    na_columns = ['gold_lag1', 'gold_lag2', 'total_lag1', 'past_success']
    for col in na_columns:
        na_count = features[col].isna().sum()
        if na_count > 0:
            features[col] = features[col].fillna(0)
            print(f"   {col}: 填充 {na_count} 个 NA 值为 0")

    # 4. 时间序列划分 (DATA Gate 要求: 时间序列交叉验证)
    print("\n1.4 时间序列划分...")
    train = features[features['Year'] <= 2016].copy()
    test = features[features['Year'] >= 2020].copy()
    print(f"   训练集 (Year <= 2016): {len(train)} 行")
    print(f"   测试集 (Year >= 2020): {len(test)} 行")

    # 5. 准备特征矩阵
    print("\n1.5 准备特征矩阵...")
    feature_cols = [
        'gold_lag1', 'gold_lag2', 'total_lag1',
        'host_flag', 'events_count', 'year_normalized',
        'past_success', 'athlete_mobility', 'medal_surge', 'first_medal_year'
    ]

    X_train = train[feature_cols].values
    y_gold_train = train['Gold'].values
    y_total_train = train['Total'].values

    print(f"   特征数量: {len(feature_cols)}")
    print(f"   特征列: {feature_cols}")

    # 6. 转换为 Stan 格式
    print("\n1.6 转换为 Stan 格式...")
    stan_data = {
        'N': X_train.shape[0],
        'K': len(feature_cols),
        'X': X_train,
        'y_gold': y_gold_train,
        'y_total': y_total_train
    }
    print(f"   Stan 数据字典:")
    print(f"     N (观测数): {stan_data['N']}")
    print(f"     K (特征数): {stan_data['K']}")
    print(f"     X shape: {stan_data['X'].shape}")
    print(f"     y_gold shape: {stan_data['y_gold'].shape}")

    # 7. 验证数据完整性
    print("\n1.7 验证数据完整性...")
    assert stan_data['N'] > 0, "训练集为空"
    assert stan_data['K'] == len(feature_cols), f"特征数不匹配: {stan_data['K']} vs {len(feature_cols)}"
    assert stan_data['y_gold'].min() >= 0, "金牌数有负值"
    assert stan_data['y_total'].min() >= 0, "总奖牌数有负值"
    assert np.all(np.isfinite(stan_data['X'])), "特征矩阵有非有限值"
    print("   ✅ 所有验证通过")

    return train, test, stan_data, feature_cols


def create_country_index(train_data):
    """
    为分层模型创建国家索引

    Returns:
        country_idx: array, country index for each observation
        country_to_idx: dict, mapping from NOC to index
    """
    print("\n创建国家索引...")
    unique_countries = sorted(train_data['NOC'].unique())
    country_to_idx = {country: idx + 1 for idx, country in enumerate(unique_countries)}
    country_idx = train_data['NOC'].map(country_to_idx).values

    print(f"   国家数量: {len(unique_countries)}")
    print(f"   索引范围: 1-{len(unique_countries)}")

    return country_idx, country_to_idx


if __name__ == '__main__':
    # 测试数据加载
    train, test, stan_data, feature_cols = load_and_preprocess_data()
    country_idx, country_to_idx = create_country_index(train)

    print("\n" + "=" * 60)
    print("数据加载完成!")
    print("=" * 60)
    print(f"\n训练集统计:")
    print(f"  观测数: {len(train)}")
    print(f"  国家数: {train['NOC'].nunique()}")
    print(f"  年份范围: {train['Year'].min()} - {train['Year'].max()}")
    print(f"  金牌均值: {train['Gold'].mean():.2f}")
    print(f"  零金牌比例: {(train['Gold'] == 0).mean():.1%}")
