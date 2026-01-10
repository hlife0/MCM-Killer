import pandas as pd
import matplotlib.pyplot as plt
from visualize import FIGURE_DIR

def plot_proxy_variables(df):
    """绘制代理变量"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # 1. Athlete Mobility
    df_mobility = df.dropna(subset=['athlete_mobility'])
    df_mobility = df_mobility[df_mobility['athlete_mobility'] > 0]

    axes[0].scatter(df_mobility['athlete_mobility'], df_mobility['Gold'],
                   alpha=0.5, s=50, edgecolors='black', linewidths=0.5)
    axes[0].set_xlabel('Athlete Mobility Count', fontsize=12)
    axes[0].set_ylabel('Gold Medals', fontsize=12)
    axes[0].set_title('Athlete Mobility vs Gold Medals', fontsize=14, fontweight='bold')
    axes[0].grid(True, alpha=0.3)

    # 2. Medal Surge
    df_surge = df[df['medal_surge'] == 1]
    df_no_surge = df[df['medal_surge'] == 0]

    surge_data = [df_no_surge['Gold'].dropna(), df_surge['Gold'].dropna()]
    bp = axes[1].boxplot(surge_data, labels=['No Surge', 'Surge'],
                         patch_artist=True, showmeans=True)

    # 美化 boxplot
    for patch, color in zip(bp['boxes'], ['steelblue', 'coral']):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    axes[1].set_ylabel('Gold Medals', fontsize=12)
    axes[1].set_title('Medal Surge Impact', fontsize=14, fontweight='bold')
    axes[1].grid(True, alpha=0.3, axis='y')

    # 3. First Medal Year
    df_first = df.dropna(subset=['first_medal_year'])
    df_first = df_first[df_first['first_medal_year'] > 0]
    df_first['decade'] = (df_first['first_medal_year'] // 10) * 10
    decade_medals = df_first.groupby('decade')['Gold'].mean()

    axes[2].bar(decade_medals.index, decade_medals.values, width=8,
                color='steelblue', alpha=0.7, edgecolor='black')
    axes[2].set_xlabel('Decade of First Medal', fontsize=12)
    axes[2].set_ylabel('Average Gold Medals', fontsize=12)
    axes[2].set_title('First Medal Decade vs Performance', fontsize=14, fontweight='bold')
    axes[2].grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig(FIGURE_DIR / 'figure_5_proxy_variables.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 图表 5 已保存: figure_5_proxy_variables.png")

if __name__ == '__main__':
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    plot_proxy_variables(df)
