import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from visualize import FIGURE_DIR

def plot_correlation_heatmap(df):
    """绘制特征相关性热力图"""
    feature_cols = [
        'Gold', 'Total', 'gold_lag1', 'gold_lag2', 'total_lag1',
        'host_flag', 'events_count', 'year_normalized', 'past_success',
        'athlete_mobility', 'medal_surge', 'first_medal_year'
    ]

    # 只选择存在的列
    available_cols = [col for col in feature_cols if col in df.columns]
    corr_data = df[available_cols].copy()

    # 处理 first_medal_year（将 -1 替换为 NaN）
    if 'first_medal_year' in corr_data.columns:
        corr_data = corr_data.drop(columns=['first_medal_year'])

    # 确保所有数据都是数值型
    for col in corr_data.columns:
        corr_data[col] = pd.to_numeric(corr_data[col], errors='coerce')

    corr_matrix = corr_data.corr()

    plt.figure(figsize=(14, 12))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
                center=0, square=True, linewidths=1,
                cbar_kws={'shrink': 0.8}, annot_kws={'fontsize': 9})
    plt.title('Feature Correlation Heatmap', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / 'figure_6_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✅ 图表 6 已保存: figure_6_correlation_heatmap.png")

if __name__ == '__main__':
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    plot_correlation_heatmap(df)
