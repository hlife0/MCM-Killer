import pandas as pd
import matplotlib.pyplot as plt
from visualize import FIGURE_DIR

def plot_ranking_comparison(df):
    """绘制排名对比"""
    df_2024 = df[df['Year'] == 2024].copy()
    df_2020 = df[df['Year'] == 2020].copy()

    # 合并数据
    comparison = df_2024[['NOC', 'Gold', 'Total']].merge(
        df_2020[['NOC', 'Gold', 'Total']],
        on='NOC',
        suffixes=('_2024', '_2020')
    )

    # 计算排名
    comparison['rank_2024'] = comparison['Gold_2024'].rank(ascending=False)
    comparison['rank_2020'] = comparison['Gold_2020'].rank(ascending=False)
    comparison['rank_change'] = comparison['rank_2020'] - comparison['rank_2024']

    # 选择前 20 名
    top_2024 = comparison.nsmallest(20, 'rank_2024')

    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(top_2024['rank_2020'], top_2024['rank_2024'],
                         s=100, alpha=0.6, c=top_2024['rank_change'],
                         cmap='RdYlGn', edgecolors='black', linewidths=1)

    # 添加对角线
    max_rank = max(top_2024['rank_2020'].max(), top_2024['rank_2024'].max())
    plt.plot([1, max_rank], [1, max_rank], 'k--', alpha=0.5, linewidth=2, label='No Change')

    # 标注国家
    for _, row in top_2024.iterrows():
        plt.annotate(row['NOC'], (row['rank_2020'], row['rank_2024']),
                    fontsize=8, alpha=0.8)

    plt.xlabel('Rank in 2020', fontsize=12)
    plt.ylabel('Rank in 2024', fontsize=12)
    plt.title('Ranking Comparison: 2020 vs 2024 (Top 20)', fontsize=14, fontweight='bold')
    cbar = plt.colorbar(scatter)
    cbar.set_label('Rank Change (Positive = Improvement)', fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / 'figure_4_ranking_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 图表 4 已保存: figure_4_ranking_comparison.png")

if __name__ == '__main__':
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    plot_ranking_comparison(df)
