import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 设置中文字体（如果需要）
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建输出目录
FIGURE_DIR = Path('/home/jcheniu/MCM-Killer/workspace/2025_C/output/paper/figures')
FIGURE_DIR.mkdir(exist_ok=True, parents=True)

def load_data():
    """加载数据"""
    df = pd.read_csv('/home/jcheniu/MCM-Killer/workspace/2025_C/output/implementation/data/features_core.csv')
    print(f"数据加载完成: {len(df)} 行 × {len(df.columns)} 列")
    return df

if __name__ == '__main__':
    df = load_data()
    print(f"年份范围: {df['Year'].min()} - {df['Year'].max()}")
    print(f"国家数量: {df['NOC'].nunique()}")
