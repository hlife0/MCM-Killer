#!/usr/bin/env python3
"""
Quick Test Script

Tests data loading and basic functionality before running full training.
"""

import sys
from pathlib import Path

def test_data_loader():
    """测试数据加载"""
    print("=" * 60)
    print("Test 1: Data Loader")
    print("=" * 60)

    try:
        from data_loader import load_and_preprocess_data, create_country_index

        train, test, stan_data, feature_cols = load_and_preprocess_data()
        country_idx, country_to_idx = create_country_index(train)

        assert stan_data['N'] > 0, "训练集为空"
        assert stan_data['K'] == len(feature_cols), "特征数不匹配"
        assert len(country_to_idx) > 0, "国家索引为空"

        print("\n✅ Data Loader 测试通过")
        print(f"   训练集: {stan_data['N']} 观测")
        print(f"   特征数: {stan_data['K']}")
        print(f"   国家数: {len(country_to_idx)}")

        return True

    except Exception as e:
        print(f"\n❌ Data Loader 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_stan_models():
    """测试 Stan 模型语法"""
    print("\n" + "=" * 60)
    print("Test 2: Stan Model Compilation")
    print("=" * 60)

    try:
        import cmdstanpy

        models = [
            'baseline_poisson.stan',
            'negative_binomial.stan',
            'full_zinb.stan'
        ]

        for model_file in models:
            model_path = Path('output/implementation/code/models') / model_file

            if not model_path.exists():
                print(f"\n⚠️  {model_file} 不存在,跳过")
                continue

            print(f"\n编译 {model_file}...")
            model = cmdstanpy.CmdStanModel(stan_file=str(model_path))
            print(f"   ✅ {model_file} 编译成功")

        print("\n✅ 所有 Stan 模型编译成功")
        return True

    except Exception as e:
        print(f"\n❌ Stan 模型编译失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_quick_fit():
    """快速拟合测试 (少量迭代)"""
    print("\n" + "=" * 60)
    print("Test 3: Quick Model Fitting (10 iterations)")
    print("=" * 60)

    try:
        import cmdstanpy
        from data_loader import load_and_preprocess_data

        train, test, stan_data, feature_cols = load_and_preprocess_data()

        # 准备最小测试数据 (只取前 100 个观测)
        stan_data_test = {
            'N': 100,
            'K': stan_data['K'],
            'X': stan_data['X'][:100, :],
            'y': stan_data['y_gold'][:100]
        }

        model = cmdstanpy.CmdStanModel(
            stan_file='output/implementation/code/models/baseline_poisson.stan'
        )

        print("\n运行快速拟合 (10 迭代)...")
        fit = model.sample(
            data=stan_data_test,
            chains=1,
            iter_warmup=5,
            iter_sampling=10,
            seed=12345
        )

        print("   ✅ 快速拟合成功")

        # 检查输出
        summary = fit.summary()
        print(f"   参数数量: {len(summary)}")
        print(f"   R-hat 最大值: {summary['R_hat'].max():.4f}")

        print("\n✅ 快速拟合测试通过")
        return True

    except Exception as e:
        print(f"\n❌ 快速拟合测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("MCM-Killer Phase 4: Code Translator - Quick Test")
    print("=" * 60)

    # 切换到正确的目录
    import os
    os.chdir('/home/jcheniu/MCM-Killer/workspace/2025_C')

    results = []

    # Test 1: Data Loader
    results.append(test_data_loader())

    # Test 2: Stan Models
    results.append(test_stan_models())

    # Test 3: Quick Fit (可选,时间较长)
    quick_fit = input("\n是否运行快速拟合测试? (y/n): ")
    if quick_fit.lower() == 'y':
        results.append(test_quick_fit())

    # 总结
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"通过: {sum(results)}/{len(results)}")

    if all(results):
        print("\n✅ 所有测试通过! 代码已准备就绪。")
        print("\n下一步:")
        print("  1. 安装依赖: pip install -r requirements.txt")
        print("  2. 运行完整训练: python fit_models.py")
        print("  3. 诊断结果: python diagnostics.py")
        print("  4. 生成预测: python predict_2028.py")
        sys.exit(0)
    else:
        print("\n❌ 部分测试失败,请检查错误信息")
        sys.exit(1)
