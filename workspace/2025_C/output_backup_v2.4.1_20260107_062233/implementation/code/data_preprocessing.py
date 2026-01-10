#!/usr/bin/env python3
"""
Phase 3 数据预处理和特征工程脚本
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ============== 配置 ==============
BASE_DIR = Path('/home/jcheniu/MCM-Killer/workspace/2025_C/output')
DATA_DIR = BASE_DIR / 'problem' / 'original' / '2025_Problem_C_Data'
OUTPUT_DIR = BASE_DIR / 'implementation' / 'data'
CODE_DIR = BASE_DIR / 'implementation' / 'code'
LOG_FILE = BASE_DIR / 'implementation' / 'logs' / 'data_processing.log'

OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

# ============== 日志函数 ==============
def log(message):
    print(message)
    with open(LOG_FILE, 'a') as f:
        f.write(message + '\n')

# ============== 1. 数据清理 ==============
def clean_data():
    """清理数据文件：去除空格、标准化国家名称"""
    log("=" * 60)
    log("Step 1: 数据清理")
    log("=" * 60)

    # 1.1 清理 medal_counts.csv
    log("\n1.1 清理 summerOly_medal_counts.csv")
    medals = pd.read_csv(DATA_DIR / 'summerOly_medal_counts.csv')

    # 检查空格问题
    medals['NOC_stripped'] = medals['NOC'].str.strip()
    space_count = (medals['NOC'] != medals['NOC_stripped']).sum()
    log(f"  发现 {space_count} 条记录有空格")

    # 清理
    medals['NOC'] = medals['NOC'].str.strip()
    medals = medals.drop(columns=['NOC_stripped'])

    # 保存清理后的文件
    medals.to_csv(OUTPUT_DIR / 'summerOly_medal_counts_cleaned.csv', index=False)
    log(f"  ✅ 已保存: summerOly_medal_counts_cleaned.csv")
    log(f"  记录数: {len(medals)}")
    log(f"  国家数: {medals['NOC'].nunique()}")

    # 1.2 清理 hosts.csv 并解析国家
    log("\n1.2 清理和解析 summerOly_hosts.csv")
    hosts = pd.read_csv(DATA_DIR / 'summerOly_hosts.csv', encoding='utf-8-sig')

    # 清理空格
    hosts['Host'] = hosts['Host'].str.strip()

    # 解析 "City, Country" 格式
    def parse_host_country(host_str):
        """解析 Host 字段，提取国家名"""
        parts = host_str.split(',')
        if len(parts) == 2:
            return parts[1].strip()
        return host_str.strip()

    hosts['host_country'] = hosts['Host'].apply(parse_host_country)

    # 建立国家名映射（处理特殊情况）
    country_mapping = {
        'United Kingdom': 'Great Britain',  # UK → Great Britain
        'West Germany': 'Germany',
        'East Germany': 'Germany',
        'Soviet Union': 'Russia',
        'Russia': 'Russian Federation',
    }

    hosts['host_country'] = hosts['host_country'].replace(country_mapping)

    hosts.to_csv(OUTPUT_DIR / 'summerOly_hosts_cleaned.csv', index=False)
    log(f"  ✅ 已保存: summerOly_hosts_cleaned.csv")
    log(f"  记录数: {len(hosts)}")
    log(f"  主办国示例:\n{hosts.head(10)}")

    # 1.3 清理 athletes.csv（只清理 NOC 字段）
    log("\n1.3 清理 summerOly_athletes.csv（仅 NOC 字段）")
    # 分块读取以节省内存
    athletes_chunks = []
    for chunk in pd.read_csv(DATA_DIR / 'summerOly_athletes.csv', chunksize=50000):
        chunk['NOC'] = chunk['NOC'].str.strip()
        athletes_chunks.append(chunk)

    athletes = pd.concat(athletes_chunks, ignore_index=True)
    log(f"  ✅ 已清理 athletes.csv")
    log(f"  记录数: {len(athletes)}")

    # 保存清理后的 athletes（压缩以节省空间）
    athletes.to_csv(OUTPUT_DIR / 'summerOly_athletes_cleaned.csv', index=False)
    log(f"  ✅ 已保存: summerOly_athletes_cleaned.csv")

    # 1.4 清理 programs.csv
    log("\n1.4 清理 summerOly_programs.csv")
    # 尝试多种编码
    try:
        programs = pd.read_csv(DATA_DIR / 'summerOly_programs.csv', encoding='utf-8')
    except:
        try:
            programs = pd.read_csv(DATA_DIR / 'summerOly_programs.csv', encoding='utf-8-sig')
        except:
            programs = pd.read_csv(DATA_DIR / 'summerOly_programs.csv', encoding='latin1')

    # 检查是否有需要清理的字段
    programs.to_csv(OUTPUT_DIR / 'summerOly_programs_cleaned.csv', index=False, encoding='utf-8')
    log(f"  ✅ 已保存: summerOly_programs_cleaned.csv")

    return medals, hosts, athletes, programs

# ============== 2. 核心特征工程（Section 6.1） ==============
def create_core_features(medals, hosts, programs):
    """创建 7 个核心特征"""
    log("\n" + "=" * 60)
    log("Step 2: 核心特征工程（Section 6.1）")
    log("=" * 60)

    # 2.1 准备基础数据
    # 按 NOC 和 Year 排序
    medals = medals.sort_values(['NOC', 'Year']).copy()

    # 2.2 创建 lag 特征
    log("\n2.1 创建 lag 特征")
    medals['gold_lag1'] = medals.groupby('NOC')['Gold'].shift(1)
    medals['gold_lag2'] = medals.groupby('NOC')['Gold'].shift(2)
    medals['total_lag1'] = medals.groupby('NOC')['Total'].shift(1)

    log(f"  ✅ gold_lag1: {medals['gold_lag1'].notna().sum()} 个非 NA 值")
    log(f"  ✅ gold_lag2: {medals['gold_lag2'].notna().sum()} 个非 NA 值")
    log(f"  ✅ total_lag1: {medals['total_lag1'].notna().sum()} 个非 NA 值")

    # 2.3 创建 host_flag
    log("\n2.2 创建 host_flag")
    # 构建 year → host_country 映射
    year_to_host = dict(zip(hosts['Year'], hosts['host_country']))

    medals['host_flag'] = medals.apply(
        lambda row: 1 if row['NOC'] == year_to_host.get(row['Year'], '') else 0,
        axis=1
    )

    host_count = medals['host_flag'].sum()
    log(f"  ✅ host_flag: {host_count} 个主办国观测")

    # 2.4 创建 events_count
    log("\n2.3 创建 events_count")
    # 计算每年的总项目数
    # programs.csv 格式：每行是一个项目，列是各年份的项目数
    # 需要转换为数值类型
    year_columns = [str(y) for y in sorted(medals['Year'].unique()) if str(y) in programs.columns]

    events_per_year = {}
    for year in sorted(medals['Year'].unique()):
        if str(year) in programs.columns:
            # 转换为数值，处理可能的混合类型
            events_series = pd.to_numeric(programs[str(year)], errors='coerce')
            events_per_year[year] = events_series.sum()

    medals['events_count'] = medals['Year'].map(events_per_year)
    log(f"  ✅ events_count: 范围 [{medals['events_count'].min()}, {medals['events_count'].max()}]")

    # 2.5 创建 year_normalized
    log("\n2.4 创建 year_normalized")
    min_year = medals['Year'].min()
    max_year = medals['Year'].max()
    medals['year_normalized'] = (medals['Year'] - min_year) / (max_year - min_year)
    log(f"  ✅ year_normalized: 范围 [{medals['year_normalized'].min():.3f}, {medals['year_normalized'].max():.3f}]")

    # 2.6 创建 past_success
    log("\n2.5 创建 past_success")
    # 过去 4 届的获奖比例（rolling window）
    medals['won_medal'] = (medals['Gold'] > 0).astype(int)
    medals['past_success'] = medals.groupby('NOC')['won_medal'].transform(
        lambda x: x.rolling(window=4, min_periods=1).mean().shift(1)
    )

    log(f"  ✅ past_success: 范围 [{medals['past_success'].min():.3f}, {medals['past_success'].max():.3f}]")
    log(f"  NA 值: {medals['past_success'].isna().sum()}（第一届）")

    # 清理临时列
    medals = medals.drop(columns=['won_medal'])

    return medals

# ============== 3. 代理变量工程（Section 6.3） ==============
def create_proxy_features(medals, athletes):
    """创建 3 个教练效应代理变量"""
    log("\n" + "=" * 60)
    log("Step 3: 代理变量工程（Section 6.3）")
    log("=" * 60)

    # 3.1 athlete_mobility
    log("\n3.1 创建 athlete_mobility")

    # 预计算：所有跨国运动员
    log("  计算跨国运动员（可能需要几分钟）...")
    athlete_countries = athletes.groupby('Name')['NOC'].nunique()
    mobile_athletes = set(athlete_countries[athlete_countries > 1].index)
    log(f"  发现 {len(mobile_athletes)} 名跨国运动员")

    # 为每个观测计算 mobility
    def compute_mobility_for_country(noc, year):
        """计算某国到某年为止的跨国运动员比例"""
        # 该国到该年为止的所有运动员
        country_athletes = athletes[
            (athletes['NOC'] == noc) &
            (athletes['Year'] <= year)
        ]['Name'].unique()

        if len(country_athletes) == 0:
            return 0.0

        # 其中跨国运动员的数量
        mobile_count = len(set(country_athletes) & mobile_athletes)
        return mobile_count / len(country_athletes)

    # 按 NOC 和 Year 分组计算
    log("  为每个观测计算 mobility（可能需要几分钟）...")
    mobility_cache = {}
    for noc in medals['NOC'].unique():
        noc_data = athletes[athletes['NOC'] == noc]
        for year in medals[medals['NOC'] == noc]['Year'].unique():
            cache_key = f"{noc}_{year}"
            if cache_key not in mobility_cache:
                country_athletes = noc_data[noc_data['Year'] <= year]['Name'].unique()
                if len(country_athletes) == 0:
                    mobility_cache[cache_key] = 0.0
                else:
                    mobile_count = len(set(country_athletes) & mobile_athletes)
                    mobility_cache[cache_key] = mobile_count / len(country_athletes)

    medals['athlete_mobility'] = medals.apply(
        lambda row: mobility_cache.get(f"{row['NOC']}_{row['Year']}", 0.0),
        axis=1
    )

    log(f"  ✅ athlete_mobility: 范围 [{medals['athlete_mobility'].min():.4f}, {medals['athlete_mobility'].max():.4f}]")
    log(f"  平均值: {medals['athlete_mobility'].mean():.4f}")

    # 3.2 medal_surge
    log("\n3.2 创建 medal_surge")
    # 计算金牌变化
    medals['gold_change'] = medals.groupby('NOC')['Gold'].diff()
    medals['medal_surge'] = (medals['gold_change'] >= 5).astype(int)

    surge_count = medals['medal_surge'].sum()
    log(f"  ✅ medal_surge: {surge_count} 次激增事件")

    # 3.3 first_medal_year
    log("\n3.3 创建 first_medal_year")
    first_medal = medals[medals['Gold'] > 0].groupby('NOC')['Year'].min()

    def get_years_since_first(noc, year):
        """计算距离首次获奖的年数"""
        if noc not in first_medal:
            return -1  # 从未获奖
        return year - first_medal[noc]

    medals['first_medal_year'] = medals.apply(
        lambda row: get_years_since_first(row['NOC'], row['Year']),
        axis=1
    )

    countries_with_gold = medals[medals['first_medal_year'] >= 0]['NOC'].nunique()
    log(f"  ✅ first_medal_year: {countries_with_gold} 个国家有金牌记录")

    # 清理临时列
    medals = medals.drop(columns=['gold_change'])

    return medals

# ============== 4. 保存特征数据 ==============
def save_features(medals):
    """保存特征数据文件"""
    log("\n" + "=" * 60)
    log("Step 4: 保存特征数据")
    log("=" * 60)

    # 选择核心特征列
    core_features = medals[[
        'Year', 'NOC', 'Gold', 'Silver', 'Bronze', 'Total',
        'gold_lag1', 'gold_lag2', 'total_lag1',
        'host_flag', 'events_count', 'year_normalized', 'past_success',
        'athlete_mobility', 'medal_surge', 'first_medal_year'
    ]].copy()

    # 保存
    output_file = OUTPUT_DIR / 'features_core.csv'
    core_features.to_csv(output_file, index=False)

    log(f"\n✅ 已保存核心特征: {output_file}")
    log(f"  行数: {len(core_features)}")
    log(f"  列数: {len(core_features.columns)}")
    log(f"\n  特征列表:")
    for col in core_features.columns:
        na_count = core_features[col].isna().sum()
        log(f"    - {col}: {na_count} NA")

    return core_features

# ============== 5. 数据质量报告 ==============
def generate_quality_report():
    """生成数据质量报告"""
    log("\n" + "=" * 60)
    log("数据质量总结")
    log("=" * 60)

    # 加载清理后的数据
    medals = pd.read_csv(OUTPUT_DIR / 'summerOly_medal_counts_cleaned.csv')
    features = pd.read_csv(OUTPUT_DIR / 'features_core.csv')

    log(f"\n清理后数据:")
    log(f"  记录数: {len(medals)}")
    log(f"  国家数: {medals['NOC'].nunique()}")
    log(f"  年份范围: {medals['Year'].min()} - {medals['Year'].max()}")

    log(f"\n特征数据:")
    log(f"  记录数: {len(features)}")
    log(f"  特征数: {len(features.columns) - 6}")  # 减去基础列（Year, NOC, Gold, Silver, Bronze, Total）

    # 零膨胀检查
    zero_gold = (medals['Gold'] == 0).sum()
    zero_ratio = zero_gold / len(medals)
    log(f"\n零膨胀: {zero_gold}/{len(medals)} ({zero_ratio:.1%})")

    log(f"\n✅ 数据预处理完成！")

# ============== 主函数 ==============
def main():
    """主函数"""
    log("\n" + "=" * 60)
    log("Phase 3: 数据预处理和特征工程")
    log("=" * 60)
    log(f"开始时间: {pd.Timestamp.now()}")

    try:
        # Step 1: 数据清理
        medals, hosts, athletes, programs = clean_data()

        # Step 2: 核心特征工程
        medals = create_core_features(medals, hosts, programs)

        # Step 3: 代理变量工程
        medals = create_proxy_features(medals, athletes)

        # Step 4: 保存特征数据
        features = save_features(medals)

        # Step 5: 生成质量报告
        generate_quality_report()

        log(f"\n结束时间: {pd.Timestamp.now()}")
        log("\n✅ 所有步骤成功完成！")

    except Exception as e:
        log(f"\n❌ 错误: {str(e)}")
        import traceback
        log(traceback.format_exc())
        raise

if __name__ == "__main__":
    main()
