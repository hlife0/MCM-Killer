#!/usr/bin/env python3
"""
Phase 4: Model Diagnostics

Performs:
1. R-hat check (< 1.01)
2. ESS check (> 400)
3. Posterior predictive check
4. Model comparison (WAIC/LOO)
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json


def check_convergence(fit, model_name, output_dir):
    """
    检查模型收敛

    Args:
        fit: CmdStanMCMC object
        model_name: str, model name
        output_dir: Path, output directory

    Returns:
        bool: True if converged
    """
    print(f"\n{'=' * 60}")
    print(f"{model_name} 收敛诊断")
    print('=' * 60)

    summary = fit.summary()

    # 1. R-hat 检查
    rhat_column = summary['R_hat']
    rhat_max = rhat_column.max()
    bad_rhat_params = summary[rhat_column > 1.01].index.tolist()

    print(f"\n1. R-hat 检查 (阈值 < 1.01):")
    print(f"   最大 R-hat: {rhat_max:.4f}")

    if bad_rhat_params:
        print(f"   ❌ 失败: {len(bad_rhat_params)} 个参数未收敛")
        print(f"   问题参数 (前10个): {bad_rhat_params[:10]}")
    else:
        print(f"   ✅ 通过: 所有参数收敛")

    # 2. ESS 检查
    ess_column = summary['ESS_Bulk']
    ess_min = ess_column.min()
    ess_mean = ess_column.mean()
    bad_ess_params = summary[ess_column < 400].index.tolist()

    print(f"\n2. ESS 检查 (阈值 > 400):")
    print(f"   最小 ESS: {ess_min:.0f}")
    print(f"   平均 ESS: {ess_mean:.0f}")

    if bad_ess_params:
        print(f"   ❌ 失败: {len(bad_ess_params)} 个参数 ESS 不足")
        print(f"   问题参数 (前10个): {bad_ess_params[:10]}")
    else:
        print(f"   ✅ 通过: 所有参数 ESS 充足")

    # 3. 总体评估
    converged = (len(bad_rhat_params) == 0) and (len(bad_ess_params) == 0)

    print(f"\n{'=' * 60}")
    if converged:
        print("✅ 模型收敛性检查通过!")
    else:
        print("❌ 模型未收敛,需要调整")
    print('=' * 60)

    # 保存结果
    results = {
        'model': model_name,
        'rhat_max': float(rhat_max),
        'rhat_pass': len(bad_rhat_params) == 0,
        'ess_min': float(ess_min),
        'ess_mean': float(ess_mean),
        'ess_pass': len(bad_ess_params) == 0,
        'converged': converged
    }

    results_file = output_dir / f'{model_name}_convergence.json'
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    return converged


def posterior_predictive_check(fit, y_observed, model_name, output_dir):
    """
    后验预测检验

    Args:
        fit: CmdStanMCMC object
        y_observed: array, observed responses
        model_name: str, model name
        output_dir: Path, output directory
    """
    print(f"\n{'=' * 60}")
    print(f"{model_name} 后验预测检验")
    print('=' * 60)

    # 获取后验预测
    y_rep = fit.stan_variable('y_rep')

    # 计算统计量
    obs_zero_prop = np.mean(y_observed == 0)
    rep_zero_prop = np.mean(y_rep == 0)

    obs_mean = np.mean(y_observed)
    rep_mean = np.mean(y_rep)

    obs_std = np.std(y_observed)
    rep_std = np.std(y_rep)

    print(f"\n1. 零比例比较:")
    print(f"   观测: {obs_zero_prop:.3f}")
    print(f"   预测: {rep_zero_prop:.3f}")
    print(f"   差异: {abs(obs_zero_prop - rep_zero_prop):.3f}")

    if abs(obs_zero_prop - rep_zero_prop) < 0.05:
        print("   ✅ 零比例匹配良好")
    else:
        print("   ⚠️  零比例不匹配,可能需要零膨胀模型")

    print(f"\n2. 均值比较:")
    print(f"   观测: {obs_mean:.2f}")
    print(f"   预测: {rep_mean:.2f}")
    print(f"   差异: {abs(obs_mean - rep_mean):.2f}")

    print(f"\n3. 标准差比较:")
    print(f"   观测: {obs_std:.2f}")
    print(f"   预测: {rep_std:.2f}")
    print(f"   差异: {abs(obs_std - rep_std):.2f}")

    # 绘图
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # 直方图
    ax = axes[0]
    ax.hist(y_observed, bins=50, alpha=0.5, label='Observed', density=True, color='blue')
    ax.hist(y_rep.flatten(), bins=50, alpha=0.5, label='Replicated', density=True, color='red')
    ax.set_xlabel('Medal Count')
    ax.set_ylabel('Density')
    ax.set_title(f'{model_name}: Posterior Predictive Check')
    ax.legend()

    # 箱线图
    ax = axes[1]
    data_to_plot = [
        y_observed,
        y_rep.flatten()[np.random.choice(len(y_rep.flatten()), size=len(y_observed), replace=False)]
    ]
    bp = ax.boxplot(data_to_plot, labels=['Observed', 'Replicated'])
    ax.set_ylabel('Medal Count')
    ax.set_title(f'{model_name}: Distribution Comparison')

    plt.tight_layout()
    fig_file = output_dir / f'{model_name}_ppc.png'
    plt.savefig(fig_file, dpi=150)
    plt.close()

    print(f"\n✅ 图表保存至: {fig_file}")

    # 保存统计量
    stats = {
        'obs_zero_prop': float(obs_zero_prop),
        'rep_zero_prop': float(rep_zero_prop),
        'obs_mean': float(obs_mean),
        'rep_mean': float(rep_mean),
        'obs_std': float(obs_std),
        'rep_std': float(rep_std)
    }

    stats_file = output_dir / f'{model_name}_ppc_stats.json'
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)

    return stats


def compare_models_waic(fit_dict, output_dir):
    """
    模型比较 (WAIC)

    Args:
        fit_dict: dict, {model_name: fit_object}
        output_dir: Path, output directory
    """
    print(f"\n{'=' * 60}")
    print("模型比较 (WAIC)")
    print('=' * 60)

    waic_results = {}

    for model_name, fit in fit_dict.items():
        try:
            # 计算 WAIC
            log_lik = fit.stan_variable('log_lik')
            if log_lik is not None:
                # 简化版 WAIC 计算
                lppd = np.sum(np.log(np.mean(np.exp(log_lik), axis=0)))
                p_waic = np.sum(np.var(log_lik, axis=0))
                waic = -2 * (lppd - p_waic)

                waic_results[model_name] = {
                    'waic': waic,
                    'lppd': lppd,
                    'p_waic': p_waic
                }

                print(f"\n{model_name}:")
                print(f"   WAIC: {waic:.2f}")
                print(f"   Effective parameters: {p_waic:.2f}")
        except Exception as e:
            print(f"\n⚠️  {model_name}: 无法计算 WAIC ({e})")

    # 排序
    if waic_results:
        sorted_models = sorted(waic_results.items(), key=lambda x: x[1]['waic'])

        print(f"\n{'=' * 60}")
        print("WAIC 排名 (越小越好):")
        for i, (model, results) in enumerate(sorted_models, 1):
            print(f"   {i}. {model}: WAIC = {results['waic']:.2f}")

        # 保存结果
        results_file = output_dir / 'model_comparison_waic.json'
        with open(results_file, 'w') as f:
            json.dump(waic_results, f, indent=2)

    return waic_results


if __name__ == '__main__':
    # 示例: 加载拟合结果并诊断
    output_dir = Path('output/implementation/results')

    print("诊断脚本已准备就绪")
    print("请在 fit_models.py 运行完成后,使用此脚本诊断拟合结果")

    print("\n使用方法:")
    print("  python diagnostics.py")
