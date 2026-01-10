import pandas as pd
import matplotlib.pyplot as plt
from visualize import FIGURE_DIR

def plot_host_effect(df):
    """绘制主办国效应"""
    host_years = df[df['host_flag'] == 1]['Year'].unique()

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    plot_idx = 0
    for year in sorted(host_years)[-4:]:  # 最近 4 届
        if plot_idx >= 4:
            break

        # 获取该年的主办国
        host_rows = df[df['Year'] == year]
        if len(host_rows) == 0:
            continue

        # 找到主办国（可能有多行，取第一个）
        host_country = None
        for _, row in host_rows.iterrows():
            if row['host_flag'] == 1:
                host_country = row['NOC']
                break

        if host_country is None:
            continue

        # 该国前后多届的数据
        country_data = df[df['NOC'] == host_country].copy()
        country_data = country_data[(country_data['Year'] >= year - 12) &
                                    (country_data['Year'] <= year + 12)].sort_values('Year')

        if len(country_data) == 0:
            continue

        ax = axes[plot_idx]
        colors = ['red' if y == year else 'steelblue' for y in country_data['Year']]
        ax.bar(country_data['Year'], country_data['Total'], color=colors, alpha=0.7, edgecolor='black')
        ax.axvline(year, color='green', linestyle='--', linewidth=2, label='Hosted')
        ax.set_xlabel('Year', fontsize=10)
        ax.set_ylabel('Total Medals', fontsize=10)
        ax.set_title(f'{host_country} Host Effect ({year})', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')

        plot_idx += 1

    # 隐藏多余的子图
    for i in range(plot_idx, 4):
        axes[i].axis('off')

    plt.tight_layout()
    plt.savefig(FIGURE_DIR / 'figure_3_host_effect.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 图表 3 已保存: figure_3_host_effect.png")

if __name__ == '__main__':
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    plot_host_effect(df)
