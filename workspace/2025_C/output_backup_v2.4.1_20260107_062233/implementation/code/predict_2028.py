#!/usr/bin/env python3
"""
Phase 4: 2028 Olympic Predictions

Generates predictions for 2028 Los Angeles Olympics using posterior predictive distribution.
Key features:
- Manual host_flag setting (USA = 1)
- 95% prediction intervals
- Extrapolation risk warning
"""

import numpy as np
import pandas as pd
import cmdstanpy
from pathlib import Path
from data_loader import load_and_preprocess_data
import json


def prepare_2028_features(test_data, feature_cols):
    """
    准备 2028 年特征数据

    注意事项:
    - 需要手动设置 USA 的 host_flag=1 (Los Angeles)
    - gold_lag1, gold_lag2 使用 2024 和 2020 数据
    - events_count 使用历史趋势或预测值
    """
    print("\n" + "=" * 60)
    print("Step 3.1: 准备 2028 年特征")
    print("=" * 60)

    # 使用 2024 年作为基础
    X_2028 = test_data[test_data['Year'] == 2024].copy()

    if len(X_2028) == 0:
        print("❌ 无法找到 2024 年数据,请检查数据")
        return None

    print(f"\n基础数据: 2024 年 ({len(X_2028)} 个国家)")

    # 更新 2028 年特征
    X_2028['Year'] = 2028

    # 标准化年份 (2028 - 1896) / (2024 - 1896)
    X_2028['year_normalized'] = (2028 - 1896) / (2024 - 1896)

    # 主办国标识 (Los Angeles, USA)
    X_2028['host_flag'] = 0  # 默认
    usa_idx = X_2028[X_2028['NOC'] == 'United States'].index
    if len(usa_idx) > 0:
        X_2028.loc[usa_idx, 'host_flag'] = 1
        print(f"\n✅ 已设置主办国: United States (host_flag = 1)")
    else:
        print(f"\n⚠️  警告: 无法找到 United States")

    # 项目数量 (假设与 2024 年相同,或使用趋势预测)
    # 这里使用 2024 年的值
    events_2024 = X_2028['events_count'].values[0]
    X_2028['events_count'] = events_2024 * 1.02  # 假设增加 2%
    print(f"项目数量: {X_2028['events_count'].values[0]:.0f} (假设比 2024 年增加 2%)")

    # 过滤特征列
    X_2028_features = X_2028[feature_cols].values

    print(f"\n2028 年特征矩阵: {X_2028_features.shape}")

    return X_2028, X_2028_features


def predict_2028(fit, X_2028, countries_2028, feature_cols, output_dir):
    """
    生成 2028 年预测

    Args:
        fit: CmdStanMCMC object
        X_2028: array, 2028 feature matrix
        countries_2028: list, country names
        feature_cols: list, feature names
        output_dir: Path, output directory

    Returns:
        DataFrame with predictions
    """
    print("\n" + "=" * 60)
    print("Step 3.2: 生成 2028 年预测")
    print("=" * 60)

    # 提取后验样本
    print("\n提取后验样本...")
    beta_samples = fit.stan_variable('beta')
    n_samples = beta_samples.shape[0]
    print(f"   后验样本数: {n_samples}")

    # 生成预测 (使用后验预测分布)
    print("\n生成预测...")
    predictions_2028 = []

    for i in range(len(X_2028)):
        X_i = X_2028[i]

        # 计算线性预测器
        mu_i = np.dot(beta_samples, X_i)

        # 生成负二项随机样本
        # 注意: 这里需要从 fit 中获取 theta 参数
        try:
            theta_samples = fit.stan_variable('theta')

            # 如果 theta 是标量,扩展为向量
            if theta_samples.ndim == 0:
                theta_samples = np.full(n_samples, theta_samples)

            # 生成负二项随机数
            pred_i = np.random.negative_binomial(
                n=theta_samples,
                p=theta_samples / (theta_samples + np.exp(mu_i))
            )

            predictions_2028.append(pred_i)
        except Exception as e:
            print(f"⚠️  无法提取 theta 参数,使用泊松近似")
            # 泊松近似
            pred_i = np.random.poisson(np.exp(mu_i))
            predictions_2028.append(pred_i)

    # 转换为 numpy array
    predictions_2028 = np.array(predictions_2028).T  # shape: (n_samples, n_countries)

    print(f"   预测样本: {predictions_2028.shape}")

    # 计算预测区间
    print("\n计算预测区间...")
    ci_2_5 = np.percentile(predictions_2028, 2.5, axis=0)
    ci_25 = np.percentile(predictions_2028, 25, axis=0)
    ci_50 = np.percentile(predictions_2028, 50, axis=0)
    ci_75 = np.percentile(predictions_2028, 75, axis=0)
    ci_97_5 = np.percentile(predictions_2028, 97.5, axis=0)

    # 创建结果 DataFrame
    results = pd.DataFrame({
        'NOC': countries_2028,
        'pred_2028_p2_5': ci_2_5,
        'pred_2028_p25': ci_25,
        'pred_2028_median': ci_50,
        'pred_2028_p75': ci_75,
        'pred_2028_p97_5': ci_97_5,
        'pred_2028_iqr': ci_75 - ci_25,
        'prob_zero': np.mean(predictions_2028 == 0, axis=0)
    })

    # 排序 (按中位数预测)
    results = results.sort_values('pred_2028_median', ascending=False)

    # 保存结果
    results_file = output_dir / 'predictions_2028.csv'
    results.to_csv(results_file, index=False)

    print(f"\n✅ 2028 年预测已保存至: {results_file}")

    # 显示前 10 名
    print("\n预测前 10 名:")
    print(results[['NOC', 'pred_2028_median', 'pred_2028_p2_5', 'pred_2028_p97_5']].head(10).to_string(index=False))

    # 保存后验样本
    samples_file = output_dir / 'predictions_2028_samples.npy'
    np.save(samples_file, predictions_2028)
    print(f"\n后验样本保存至: {samples_file}")

    return results


def analyze_changes_2024_2028(test_data, predictions_2028, output_dir):
    """
    分析 2024 → 2028 变化
    """
    print("\n" + "=" * 60)
    print("Step 3.3: 分析 2024 → 2028 变化")
    print("=" * 60)

    # 获取 2024 年实际数据
    data_2024 = test_data[test_data['Year'] == 2024][['NOC', 'Gold']].copy()
    data_2024 = data_2024.rename(columns={'Gold': 'gold_2024'})

    # 合并预测
    comparison = predictions_2028[['NOC', 'pred_2028_median', 'pred_2028_p2_5', 'pred_2028_p97_5']].copy()
    comparison = comparison.merge(data_2024, on='NOC', how='left')

    # 计算变化
    comparison['change_median'] = comparison['pred_2028_median'] - comparison['gold_2024']
    comparison['change_pct'] = (comparison['change_median'] / comparison['gold_2024'] * 100).round(1)

    # 分类
    comparison['trend'] = 'Stable'
    comparison.loc[comparison['change_median'] > 2, 'trend'] = 'Improving'
    comparison.loc[comparison['change_median'] < -2, 'trend'] = 'Declining'

    # 排序
    comparison = comparison.sort_values('change_median', ascending=False)

    # 保存结果
    comparison_file = output_dir / 'comparison_2024_2028.csv'
    comparison.to_csv(comparison_file, index=False)

    print(f"\n变化分析已保存至: {comparison_file}")

    # 显示进步最大的 10 个国家
    print("\n进步最大的 10 个国家:")
    print(comparison[['NOC', 'gold_2024', 'pred_2028_median', 'change_median', 'change_pct']].head(10).to_string(index=False))

    # 显示退步最大的 10 个国家
    print("\n退步最大的 10 个国家:")
    print(comparison[['NOC', 'gold_2024', 'pred_2028_median', 'change_median', 'change_pct']].tail(10).to_string(index=False))

    return comparison


def generate_prediction_report(predictions_2028, comparison, output_dir):
    """
    生成预测报告
    """
    print("\n" + "=" * 60)
    print("Step 3.4: 生成预测报告")
    print("=" * 60)

    report = {
        'title': '2028 Los Angeles Olympics Medal Predictions',
        'warning': '⚠️ Extrapolation Risk: Predictions beyond historical data range (1896-2024)',
        'top_10': predictions_2028[['NOC', 'pred_2028_median', 'pred_2028_p2_5', 'pred_2028_p97_5']].head(10).to_dict('records'),
        'most_improved': comparison.nlargest(5, 'change_median')[['NOC', 'change_median', 'change_pct']].to_dict('records'),
        'most_declined': comparison.nsmallest(5, 'change_median')[['NOC', 'change_median', 'change_pct']].to_dict('records'),
    }

    report_file = output_dir / 'prediction_report_2028.json'
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"\n预测报告已保存至: {report_file}")

    return report


if __name__ == '__main__':
    # 创建输出目录
    output_dir = Path('output/implementation/results')
    output_dir.mkdir(exist_ok=True, parents=True)

    # 加载数据
    print("=" * 60)
    print("Step 1: 加载数据")
    print("=" * 60)
    train, test, stan_data, feature_cols = load_and_preprocess_data()

    # 准备 2028 年特征
    X_2028_df, X_2028 = prepare_2028_features(test, feature_cols)

    if X_2028 is None:
        print("❌ 无法准备 2028 年特征,退出")
        exit(1)

    # 加载拟合的模型
    print("\n" + "=" * 60)
    print("Step 2: 加载拟合的模型")
    print("=" * 60)

    try:
        fit = cmdstanpy.from_csv(str(output_dir / 'full_zinb_samples-'))
        print("✅ 成功加载 ZINB 模型")
    except Exception as e:
        print(f"❌ 无法加载模型: {e}")
        print("   请先运行 fit_models.py 拟合模型")
        exit(1)

    # 生成预测
    countries_2028 = X_2028_df['NOC'].values
    predictions_2028 = predict_2028(fit, X_2028, countries_2028, feature_cols, output_dir)

    # 分析变化
    comparison = analyze_changes_2024_2028(test, predictions_2028, output_dir)

    # 生成报告
    report = generate_prediction_report(predictions_2028, comparison, output_dir)

    print("\n" + "=" * 60)
    print("2028 年预测完成!")
    print("=" * 60)
    print("\n⚠️  重要提醒:")
    print("1. 这些预测基于历史数据 (1896-2024)")
    print("2. 2028 年超出历史范围,外推不确定性高")
    print("3. 请使用 95% 预测区间而非点估计")
    print("4. 模型假设延续历史趋势,实际可能因各种因素而变化")
