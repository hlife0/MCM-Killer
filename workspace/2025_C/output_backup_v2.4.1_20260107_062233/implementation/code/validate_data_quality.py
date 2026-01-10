#!/usr/bin/env python3
"""
Phase 3 数据质量验证脚本
在特征工程前必须运行
"""

import pandas as pd
import sys

def validate_data_quality():
    errors = []
    warnings = []

    # 1. 检查空格问题（使用清理后的文件）
    try:
        medals = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/summerOly_medal_counts_cleaned.csv')
    except FileNotFoundError:
        print("⚠️ 清理后的文件不存在，检查原始文件...")
        medals = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/problem/original/2025_Problem_C_Data/summerOly_medal_counts.csv')

    athletes = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/summerOly_athletes_cleaned.csv')

    medals['NOC_stripped'] = medals['NOC'].str.strip()
    if (medals['NOC'] != medals['NOC_stripped']).any():
        errors.append("❌ 发现 NOC 字段有空格，必须先清理")
    else:
        print(f"✅ NOC 字段无空格问题")

    # 2. 检查缺失值
    if medals.isnull().any().any():
        errors.append(f"❌ medal_counts 有缺失值: {medals.isnull().sum()[medals.isnull().sum() > 0].to_dict()}")

    if athletes.isnull().any().any():
        errors.append(f"❌ athletes 有缺失值: {athletes.isnull().sum()[athletes.isnull().sum() > 0].to_dict()}")

    # 3. 检查零膨胀比例
    zero_gold_ratio = (medals['Gold'] == 0).sum() / len(medals)
    if not (0.33 <= zero_gold_ratio <= 0.35):
        warnings.append(f"⚠️ 零金牌比例异常: {zero_gold_ratio:.1%}（预期 ~33.9%）")
    else:
        print(f"✅ 零膨胀比例: {zero_gold_ratio:.1%}（符合预期）")

    # 4. 检查年份连续性
    expected_years = [1896, 1900, 1904, 1908, 1912, 1920, 1924, 1928, 1932, 1936,
                      1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984,
                      1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024]
    actual_years = sorted(medals['Year'].unique())
    if actual_years != expected_years:
        errors.append(f"❌ 年份不连续: 缺失 {set(expected_years) - set(actual_years)}")
    else:
        print(f"✅ 年份连续性检查通过（{len(actual_years)} 届）")

    # 5. 检查国家数量
    unique_nocs = medals['NOC'].nunique()
    if unique_nocs < 200 or unique_nocs > 250:
        warnings.append(f"⚠️ 国家数量异常: {unique_nocs}（预期 ~210）")
    else:
        print(f"✅ 国家数量: {unique_nocs}（符合预期）")

    # 6. 检查 host_flag 匹配度
    hosts = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/problem/original/2025_Problem_C_Data/summerOly_hosts.csv', encoding='utf-8-sig')
    # TODO: 实现国家名匹配检查
    warnings.append("⚠️ host_flag 匹配检查待实现（需要国家名标准化）")

    # 汇报结果
    print("=" * 50)
    print("数据质量验证报告")
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
        print("\n✅ 所有检查通过！")

    return len(errors) == 0

if __name__ == "__main__":
    success = validate_data_quality()
    sys.exit(0 if success else 1)
