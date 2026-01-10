#!/usr/bin/env python3
"""
Phase 3 特征工程验证脚本
在特征工程后必须运行
"""

import pandas as pd
import sys

def validate_features():
    errors = []
    warnings = []

    # 加载特征数据
    try:
        features = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    except FileNotFoundError:
        errors.append("❌ 特征数据文件不存在: data/features_core.csv")
        return False

    print(f"✅ 成功加载特征数据: {len(features)} 行 × {len(features.columns)} 列")

    # 1. 检查核心特征列
    required_features = [
        'gold_lag1', 'gold_lag2', 'total_lag1',
        'host_flag', 'events_count', 'year_normalized', 'past_success'
    ]

    missing_features = set(required_features) - set(features.columns)
    if missing_features:
        errors.append(f"❌ 缺失核心特征: {missing_features}")
    else:
        print(f"✅ 所有 7 个核心特征存在")

    # 2. 检查代理变量列
    proxy_features = ['athlete_mobility', 'medal_surge', 'first_medal_year']
    missing_proxies = set(proxy_features) - set(features.columns)
    if missing_proxies:
        warnings.append(f"⚠️ 缺失代理变量: {missing_proxies}")
    else:
        print(f"✅ 所有 3 个代理变量存在")

    # 3. 检查缺失值
    for col in required_features:
        if col in features.columns and features[col].isnull().any():
            null_count = features[col].isnull().sum()
            # lag 特征和 past_success 可以有 NA
            if 'lag' in col or col == 'past_success':
                print(f"✅ 特征 {col} 有 {null_count} 个 NA（预期）")
            else:
                errors.append(f"❌ 特征 {col} 有 {null_count} 个缺失值")

    # 4. 检查 lag 特征的合理性
    # gold_lag1 的前几个观测应该有 NaN
    if not features['gold_lag1'].isnull().any():
        warnings.append("⚠️ gold_lag1 没有 NaN 值，可能计算有误")
    else:
        print(f"✅ gold_lag1 有 {features['gold_lag1'].isnull().sum()} 个 NA（符合预期）")

    # 5. 检查 host_flag 的范围
    if features['host_flag'].max() != 1 or features['host_flag'].min() != 0:
        errors.append(f"❌ host_flag 范围异常: [{features['host_flag'].min()}, {features['host_flag'].max()}]")
    else:
        print(f"✅ host_flag 范围正确: [{features['host_flag'].min()}, {features['host_flag'].max()}]")

    # 6. 检查 year_normalized 的范围
    if features['year_normalized'].max() != 1.0 or features['year_normalized'].min() != 0.0:
        errors.append(f"❌ year_normalized 范围异常: [{features['year_normalized'].min()}, {features['year_normalized'].max()}]")
    else:
        print(f"✅ year_normalized 范围正确: [{features['year_normalized'].min()}, {features['year_normalized'].max()}]")

    # 7. 检查代理变量的计算
    if 'athlete_mobility' in features.columns:
        if features['athlete_mobility'].max() > 1 or features['athlete_mobility'].min() < 0:
            errors.append(f"❌ athlete_mobility 范围异常（应在 [0, 1]）")
        else:
            print(f"✅ athlete_mobility 范围正确: [{features['athlete_mobility'].min():.3f}, {features['athlete_mobility'].max():.3f}]")

    if 'medal_surge' in features.columns:
        surge_count = features['medal_surge'].sum()
        if surge_count < 70 or surge_count > 100:
            warnings.append(f"⚠️ medal_surge 事件数量异常: {surge_count}（预期 ~82）")
        else:
            print(f"✅ medal_surge 事件数量: {int(surge_count)}（符合预期）")

    # 8. 检查数据量
    expected_rows = 1435
    if len(features) != expected_rows:
        warnings.append(f"⚠️ 特征数据量异常: {len(features)}（预期 {expected_rows}）")
    else:
        print(f"✅ 特征数据量正确: {len(features)} 行")

    # 汇报结果
    print("\n" + "=" * 50)
    print("特征工程验证报告")
    print("=" * 50)

    if errors:
        print("\n🔴 错误（必须修复）:")
        for error in errors:
            print(f"  {error}")

    if warnings:
        print("\n🟡 警告（建议处理）:")
        for warning in warnings:
            print(f"  {warning}")

    if not errors and not warnings:
        print("\n✅ 所有特征检查通过！")

    return len(errors) == 0

if __name__ == "__main__":
    success = validate_features()
    sys.exit(0 if success else 1)
