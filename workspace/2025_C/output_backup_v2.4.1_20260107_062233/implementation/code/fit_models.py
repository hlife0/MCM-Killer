#!/usr/bin/env python3
"""
Phase 4: Model Fitting

Fits 3 models in sequence:
1. Baseline Poisson (~10 min)
2. Negative Binomial (~2 hours)
3. Full ZINB (~6-8 hours)

DATA Gate Requirements:
- warmup=1500 (not 1000)
- R-hat < 1.01
- ESS > 400
"""

import cmdstanpy
import json
import numpy as np
from pathlib import Path
from datetime import datetime
from data_loader import load_and_preprocess_data, create_country_index


def fit_baseline_poisson(stan_data, output_dir):
    """
    拟合 Baseline Poisson 模型
    目标: 验证 overdispersion (如果方差 >> 均值,需要 NB)
    """
    print("\n" + "=" * 60)
    print("Step 2.1: 拟合 Baseline Poisson 模型")
    print("=" * 60)

    model = cmdstanpy.CmdStanModel(
        stan_file='output/implementation/code/models/baseline_poisson.stan'
    )

    # HMC 配置 (DATA Gate 要求: warmup=1500)
    print("\n2.1.1 开始采样...")
    print("   链数: 4")
    print("   Warmup: 1500 (DATA Gate 要求)")
    print("   Sampling: 1000")
    print("   预计时间: ~10 分钟")

    fit = model.sample(
        data=stan_data,
        chains=4,
        parallel_chains=4,
        iter_warmup=1500,              # DATA Gate 要求
        iter_sampling=1000,
        seed=12345,
        output_dir=output_dir,
        refresh=100
    )

    # 收敛诊断
    print("\n2.1.2 收敛诊断...")
    summary = fit.summary()
    rhat_max = summary['R_hat'].max()
    ess_min = summary['n_eff'].min()

    print(f"   R-hat 最大值: {rhat_max:.4f} (目标: < 1.01)")
    print(f"   ESS 最小值: {ess_min:.0f} (目标: > 400)")

    if rhat_max < 1.01 and ess_min > 400:
        print("   ✅ 收敛良好")
    else:
        print("   ❌ 收敛不佳,需要调整")

    # 检查 overdispersion
    print("\n2.1.3 检查 overdispersion...")
    dispersion = fit.stan_variable('dispersion')
    print(f"   方差/均值比: {dispersion:.2f}")
    if dispersion > 2:
        print("   ⚠️  存在明显 overdispersion,建议使用 Negative Binomial")
    else:
        print("   ✅ Overdispersion 不明显")

    # 保存摘要
    summary_file = output_dir / 'baseline_poisson_summary.json'
    with open(summary_file, 'w') as f:
        json.dump({
            'rhat_max': float(rhat_max),
            'ess_min': float(ess_min),
            'dispersion': float(dispersion),
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)

    print(f"\n✅ Baseline Poisson 拟合完成!")
    print(f"   摘要保存至: {summary_file}")

    return fit


def fit_negative_binomial(stan_data, output_dir):
    """
    拟合 Negative Binomial 模型
    目标: 验证 zero-inflation (如果零比例 > NB 预测,需要 ZINB)
    """
    print("\n" + "=" * 60)
    print("Step 2.2: 拟合 Negative Binomial 模型")
    print("=" * 60)

    model = cmdstanpy.CmdStanModel(
        stan_file='output/implementation/code/models/negative_binomial.stan'
    )

    # HMC 配置
    print("\n2.2.1 开始采样...")
    print("   链数: 4")
    print("   Warmup: 1500 (DATA Gate 要求)")
    print("   Sampling: 1000")
    print("   预计时间: ~2 小时")

    fit = model.sample(
        data=stan_data,
        chains=4,
        parallel_chains=4,
        iter_warmup=1500,              # DATA Gate 要求
        iter_sampling=1000,
        seed=12345,
        output_dir=output_dir,
        refresh=100
    )

    # 收敛诊断
    print("\n2.2.2 收敛诊断...")
    summary = fit.summary()
    rhat_max = summary['R_hat'].max()
    ess_min = summary['n_eff'].min()

    print(f"   R-hat 最大值: {rhat_max:.4f} (目标: < 1.01)")
    print(f"   ESS 最小值: {ess_min:.0f} (目标: > 400)")

    if rhat_max < 1.01 and ess_min > 400:
        print("   ✅ 收敛良好")
    else:
        print("   ❌ 收敛不佳,需要调整")

    # 检查 zero-inflation
    print("\n2.2.3 检查 zero-inflation...")
    zero_prop_obs = fit.stan_variable('zero_prop_obs')[0]
    y_rep = fit.stan_variable('y_rep')
    zero_prop_rep = np.mean(y_rep == 0)

    print(f"   观测零比例: {zero_prop_obs:.3f}")
    print(f"   预测零比例: {zero_prop_rep:.3f}")
    if zero_prop_obs > zero_prop_rep + 0.05:
        print("   ⚠️  存在明显 zero-inflation,建议使用 ZINB")
    else:
        print("   ✅ Zero-inflation 不明显")

    # 保存摘要
    summary_file = output_dir / 'negative_binomial_summary.json'
    with open(summary_file, 'w') as f:
        json.dump({
            'rhat_max': float(rhat_max),
            'ess_min': float(ess_min),
            'zero_prop_obs': float(zero_prop_obs),
            'zero_prop_rep': float(zero_prop_rep),
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)

    print(f"\n✅ Negative Binomial 拟合完成!")
    print(f"   摘要保存至: {summary_file}")

    return fit


def fit_full_zinb(stan_data, country_idx, output_dir):
    """
    拟合完整 ZINB 分层模型
    目标: 最终模型,用于预测
    """
    print("\n" + "=" * 60)
    print("Step 2.3: 拟合完整 ZINB 分层模型")
    print("=" * 60)

    # 添加国家索引
    stan_data_zinb = stan_data.copy()
    stan_data_zinb['J'] = len(set(country_idx))
    stan_data_zinb['country_idx'] = country_idx

    model = cmdstanpy.CmdStanModel(
        stan_file='output/implementation/code/models/full_zinb.stan'
    )

    # HMC 配置
    print("\n2.3.1 开始采样...")
    print("   链数: 4")
    print("   Warmup: 1500 (DATA Gate 要求)")
    print("   Sampling: 1000")
    print("   预计时间: ~6-8 小时")

    fit = model.sample(
        data=stan_data_zinb,
        chains=4,
        parallel_chains=4,
        iter_warmup=1500,              # DATA Gate 要求
        iter_sampling=1000,
        seed=12345,
        output_dir=output_dir,
        refresh=100
    )

    # 收敛诊断
    print("\n2.3.2 收敛诊断...")
    summary = fit.summary()
    rhat_max = summary['R_hat'].max()
    ess_min = summary['n_eff'].min()

    print(f"   R-hat 最大值: {rhat_max:.4f} (目标: < 1.01)")
    print(f"   ESS 最小值: {ess_min:.0f} (目标: > 400)")

    # 验证收敛标准 (DATA Gate 要求)
    if rhat_max >= 1.01:
        print("   ❌ R-hat > 1.01,模型未收敛")
        raise ValueError(f"模型未收敛: R-hat = {rhat_max:.4f}")
    if ess_min <= 400:
        print("   ❌ ESS < 400,样本量不足")
        raise ValueError(f"样本量不足: ESS = {ess_min:.0f}")

    print("   ✅ 所有收敛标准通过")

    # 保存后验样本
    print("\n2.3.3 保存后验样本...")
    fit.save_csvfiles(dir=str(output_dir / 'full_zinb_samples'))

    # 保存摘要
    summary_file = output_dir / 'full_zinb_summary.json'
    with open(summary_file, 'w') as f:
        json.dump({
            'rhat_max': float(rhat_max),
            'ess_min': float(ess_min),
            'timestamp': datetime.now().isoformat()
        }, f, indent=2)

    print(f"\n✅ 完整 ZINB 模型拟合完成!")
    print(f"   摘要保存至: {summary_file}")

    return fit


if __name__ == '__main__':
    # 创建输出目录
    output_dir = Path('output/implementation/results')
    output_dir.mkdir(exist_ok=True, parents=True)

    # 加载数据
    print("=" * 60)
    print("Step 1: 加载数据")
    print("=" * 60)
    train, test, stan_data, feature_cols = load_and_preprocess_data()
    country_idx, country_to_idx = create_country_index(train)

    print(f"\n训练集大小: {stan_data['N']}")
    print(f"特征数量: {stan_data['K']}")
    print(f"国家数量: {len(country_to_idx)}")

    # Step 1: Baseline Poisson
    try:
        fit_poisson = fit_baseline_poisson(stan_data, output_dir)
    except Exception as e:
        print(f"❌ Baseline Poisson 拟合失败: {e}")

    # Step 2: Negative Binomial
    try:
        fit_nb = fit_negative_binomial(stan_data, output_dir)
    except Exception as e:
        print(f"❌ Negative Binomial 拟合失败: {e}")

    # Step 3: Full ZINB
    try:
        fit_zinb = fit_full_zinb(stan_data, country_idx, output_dir)
    except Exception as e:
        print(f"❌ 完整 ZINB 拟合失败: {e}")

    print("\n" + "=" * 60)
    print("所有模型拟合完成!")
    print("=" * 60)
