#!/usr/bin/env python3
"""
Phase 3 Schema 一致性验证脚本
检查跨文件的国家名一致性
"""

import pandas as pd
import sys

def validate_schema_consistency():
    errors = []
    warnings = []

    # 加载数据
    medals = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/problem/original/2025_Problem_C_Data/summerOly_medal_counts.csv')
    athletes = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/problem/original/2025_Problem_C_Data/summerOly_athletes.csv')
    hosts = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/problem/original/2025_Problem_C_Data/summerOly_hosts.csv', encoding='utf-8-sig')

    # 清理空格
    medals['NOC'] = medals['NOC'].str.strip()
    athletes['NOC'] = athletes['NOC'].str.strip()

    # 1. 检查 medals 和 athletes 的 NOC 重叠度
    medal_nocs = set(medals['NOC'].unique())
    athlete_nocs = set(athletes['NOC'].unique())

    in_medals_not_athletes = medal_nocs - athlete_nocs
    in_athletes_not_medals = athlete_nocs - medal_nocs

    if in_medals_not_athletes:
        warnings.append(f"⚠️ medal_counts 中有 {len(in_medals_not_athletes)} 个 NOC 不在 athletes 中")

    if in_athletes_not_medals:
        print(f"ℹ️ athletes 中有 {len(in_athletes_not_medals)} 个 NOC 不在 medal_counts 中（可能未获奖）")

    # 2. 检查特殊实体
    special_entities = ['Mixed team', 'Australasia', 'Bohemia']
    found_special = medal_nocs & set(special_entities)
    if found_special:
        warnings.append(f"⚠️ 发现特殊实体: {found_special}（建议处理）")

    # 3. 检查 hosts 国家解析
    # TODO: 实现国家名提取和匹配逻辑
    warnings.append("⚠️ hosts.csv 国家名匹配检查待实现")

    # 汇报结果
    print("=" * 50)
    print("Schema 一致性验证报告")
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
        print("\n✅ Schema 一致性检查通过！")

    return len(errors) == 0

if __name__ == "__main__":
    success = validate_schema_consistency()
    sys.exit(0 if success else 1)
