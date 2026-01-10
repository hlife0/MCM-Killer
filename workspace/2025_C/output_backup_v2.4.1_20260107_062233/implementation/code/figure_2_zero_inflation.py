import pandas as pd
import matplotlib.pyplot as plt
from visualize import FIGURE_DIR

def plot_zero_inflation(df):
    """绘制零膨胀分布"""
    zero_counts = df[df['Gold'] == 0].groupby('Year').size()
    total_counts = df.groupby('Year').size()
    zero_ratio = (zero_counts / total_counts * 100)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # 左图：零奖牌国家数量随时间
    ax1.plot(zero_ratio.index, zero_ratio.values, marker='o', linewidth=2, color='coral')
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Countries with Zero Gold (%)', fontsize=12)
    ax1.set_title('Zero-Inflation Over Time', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # 右图：2024 年奖牌分布
    df_2024 = df[df['Year'] == 2024]
    ax2.hist(df_2024['Gold'], bins=30, color='steelblue', alpha=0.7, edgecolor='black')
    ax2.axvline(df_2024['Gold'].mean(), color='red', linestyle='--', linewidth=2,
                label=f"Mean: {df_2024['Gold'].mean():.1f}")
    ax2.set_xlabel('Gold Medals', fontsize=12)
    ax2.set_ylabel('Number of Countries', fontsize=12)
    ax2.set_title('Distribution of Gold Medals (2024)', fontsize=14, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(FIGURE_DIR / 'figure_2_zero_inflation.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 图表 2 已保存: figure_2_zero_inflation.png")

if __name__ == '__main__':
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    plot_zero_inflation(df)
