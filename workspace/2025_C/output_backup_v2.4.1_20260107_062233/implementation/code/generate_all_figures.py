from visualize import load_data, FIGURE_DIR
from figure_1_medal_trends import plot_historical_medal_trends
from figure_2_zero_inflation import plot_zero_inflation
from figure_3_host_effect import plot_host_effect
from figure_4_ranking_comparison import plot_ranking_comparison
from figure_5_proxy_variables import plot_proxy_variables
from figure_6_correlation_heatmap import plot_correlation_heatmap

def main():
    """生成所有图表"""
    print("=" * 60)
    print("Phase 6: Visualization")
    print("=" * 60)

    # 加载数据
    df = load_data()

    # 生成所有图表
    print("\n生成图表...")
    plot_historical_medal_trends(df, top_n=10)
    plot_zero_inflation(df)
    plot_host_effect(df)
    plot_ranking_comparison(df)
    plot_proxy_variables(df)
    plot_correlation_heatmap(df)

    print("\n" + "=" * 60)
    print(f"✅ 所有图表已保存到: {FIGURE_DIR}")
    print("=" * 60)

    # 列出生成的文件
    import os
    files = sorted(FIGURE_DIR.glob('*.png'))
    print(f"\n共生成 {len(files)} 个图表:")
    for f in files:
        print(f"  - {f.name}")

if __name__ == '__main__':
    main()
