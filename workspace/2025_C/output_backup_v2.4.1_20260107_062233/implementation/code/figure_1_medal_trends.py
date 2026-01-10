import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from visualize import FIGURE_DIR

def plot_historical_medal_trends(df, top_n=10):
    """绘制历史奖牌趋势图"""
    # 选择奖牌总数最多的 top_n 国家
    top_countries = df.groupby('NOC')['Total'].sum().nlargest(top_n).index.tolist()
    df_top = df[df['NOC'].isin(top_countries)]

    plt.figure(figsize=(14, 8))
    for country in top_countries:
        country_data = df_top[df_top['NOC'] == country].sort_values('Year')
        plt.plot(country_data['Year'], country_data['Total'],
                marker='o', label=country, linewidth=2, markersize=5)

    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Total Medals', fontsize=12)
    plt.title('Historical Medal Trends (Top 10 Countries)', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / 'figure_1_medal_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 图表 1 已保存: figure_1_medal_trends.png")

if __name__ == '__main__':
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    plot_historical_medal_trends(df, top_n=10)
