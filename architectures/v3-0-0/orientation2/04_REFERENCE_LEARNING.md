# Part IV: Reference Paper Learning (Revised)

> **One-Shot 学习，不是模式提取**
> **Core Principle**: 完整范例学习，自动化分析
> **Philosophy**: 参考整篇论文，不只是提取特征
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
自动化模式提取：

Python 读取 44 篇论文 → NLP 提取模式 → 生成 style_guide.json
- 摘要平均长度：248 词
- 图表类型分布：68% 流程图
- 过渡词频率："Consequently" 出现 3.2 次

↓

Claude Code 阅读 style_guide.json → 模仿模式
```

**问题**：
- 丢失论文的整体性和连贯性
- 模式是死的，论文是活的
- 无法学习论文的"灵魂"

### 新范式（正确）

```
One-Shot 完整学习：

选择 1 篇完美 O-Prize 论文 → Claude Code 完整阅读 → 内化风格
- 完整 PDF：学习结构
- LaTeX 源码：学习排版
- 图表：学习配色和绘图
- 代码：学习实现方式

↓

Claude Code 1:1 复制专业度
```

**优势**：
- 学习完整论文的"魂"
- 理解论文的连贯性
- 可以直接参考 LaTeX 代码

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | 替代方案 |
|------|--------|------|----------|
| **自动化模式提取** | NLP 分析 44 篇论文 | 过度工程，丢失整体性 | 选择 1 篇完整范例 |
| **JSON 风格指南** | style_guide.json | 僵化，不够灵活 | 直接阅读论文 |
| **统计模式提取** | 计算摘要长度、图表数量等 | 不重要 | 学习论文的风格 |
| **Python 生成脚本** | generate_style_guide.py | 不需要 | Claude Code 直接学习 |

---

## 第二部分：One-Shot 学习设置

### 参考论文目录

```
reference/best_paper_example/
├── README.md                   # 论文说明
├── 2023_C_OPrize.pdf           # 完整 PDF（必读）
├── 2023_C_OPrize.tex           # LaTeX 源码（必读）
├── figures/                    # 所有图表（提取）
│   ├── fig1_flowchart.png
│   ├── fig2_data_overview.png
│   ├── fig3_model_results.png
│   ├── fig4_sensitivity.png
│   └── fig5_predictions.png
├── code/                       # 代码片段（提取）
│   ├── data_processing.py
│   ├── model_training.py
│   └── sensitivity_analysis.py
└── style_extraction/           # 手动提取的关键要素
    ├── structure.md            # 论文结构
    ├── color_palette.md        # 配色方案（RGB）
    └── latex_packages.md       # 使用的宏包
```

### README.md 内容

```markdown
# O-Prize 参考论文

## 论文信息
- **题目**: Modeling Olympic Medal Counts Using Zero-Inflated Approaches
- **年份**: 2023
- **问题**: Problem C (Olympic medal prediction)
- **奖项**: Outstanding Winner

## 为什么选择这篇论文？
1. **结构完整**: IMRaD 结构清晰
2. **图表优秀**: 包含流程图、数据图、灵敏度图
3. **统计严谨**: 所有必需检验都包含
4. **写作规范**: 观察-洞察模式使用得当
5. **LaTeX 可用**: 有完整源码可以参考

## 如何使用？

### Claude Code 学习指令

**Claude Code，请执行以下学习**：

1. **完整阅读 PDF**：
   ```
   Read: reference/best_paper_example/2023_C_OPrize.pdf
   ```
   - 注意论文结构（目录、章节编号）
   - 注意图表类型和数量
   - 注意数学公式的写法
   - 注意引用格式

2. **阅读 LaTeX 源码**：
   ```
   Read: reference/best_paper_example/2023_C_OPrize.tex
   ```
   - 学习 LaTeX 宏包使用（\usepackage）
   - 学习图表排版（figure 环境）
   - 学习公式编号和引用（\label, \ref）
   - 学习参考文献格式（bibliography）

3. **提取风格特征**：
   ```
   Read: reference/best_paper_example/style_extraction/*.md
   ```
   - 目录结构：章节如何组织？
   - 配色方案：图表使用什么颜色？
   - 绘图代码：如何绘制类似图表？

4. **应用到当前问题**：
   ```
   我要与之 1:1 的专业度。
   参考：
   - 目录结构
   - LaTeX 宏包
   - 图表配色
   - TikZ 绘图代码（如果有）
   - 写作风格
   ```

## 关键学习点

### 1. 论文结构
- Abstract（250 词）
- Introduction（10-15%）
- Methods（20-25%）
- Results（35-40%）
- Discussion（20-25%）
- References

### 2. 图表类型
- Figure 1: 方法流程图（必需）
- Figure 2: 数据概览（折线图/散点图）
- Figure 3: 模型结果（对比表/图）
- Figure 4: 灵敏度分析（龙卷风图）
- Figure 5: 预测结果（时间序列预测）

### 3. 统计检验
- Shapiro-Wilk（正态性）
- Durbin-Watson（自相关）
- Breusch-Pagan（同方差性）
- 所有 p 值都报告

### 4. 写作风格
- 观察-洞察模式
- "Figure 1 shows... This suggests..."
- 使用过渡词："Consequently", "Furthermore", "In contrast"

## 代码片段

论文中的关键代码已提取到 `code/` 目录：
- `data_processing.py`: 数据加载和清洗
- `model_training.py`: ZINB 模型训练
- `sensitivity_analysis.py`: 灵敏度分析（龙卷风图）

可以参考这些代码的实现方式。
```

---

## 第三部分：手动提取的关键要素

### structure.md（论文结构）

```markdown
# 论文结构分析

## 目录结构
```
1. Introduction
   1.1 Background
   1.2 Problem Statement
   1.3 Objectives

2. Methods
   2.1 Data Collection
   2.2 Feature Engineering
   2.3 Model Formulation
   2.4 Statistical Validation

3. Results
   3.1 Exploratory Analysis
   3.2 Model Performance
   3.3 Sensitivity Analysis

4. Discussion
   4.1 Key Findings
   4.2 Limitations
   4.3 Future Work

5. Conclusion

6. References
```

## 章节长度分布
- Introduction: 1.5 pages (12%)
- Methods: 3 pages (24%)
- Results: 4 pages (32%)
- Discussion: 2.5 pages (20%)
- Conclusion: 0.5 pages (4%)
- References: 1 page (8%)

**Total**: 12.5 pages

## LaTeX 模板
```latex
\documentclass[12pt]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{hyperref}

% Title
\title{Modeling Olympic Medal Counts Using Zero-Inflated Approaches}
\author{Team \#12345}
\date{\today}

\begin{document}
\maketitle

% Abstract
\begin{abstract}
...
\end{abstract}

% Sections
\section{Introduction}
...
\section{Methods}
...
\section{Results}
...
\section{Discussion}
...
\section{Conclusion}
...

% References
\bibliographystyle{plain}
\bibliography{references}

\end{document}
```
```

### color_palette.md（配色方案）

```markdown
# 图表配色方案

## 提取的 RGB 值

### 主色调
- 深蓝（主数据）：RGB(31, 119, 180) - #1F77B4
- 橙色（对比）：RGB(255, 127, 14) - #FF7F0E
- 绿色（成功）：RGB(44, 160, 44) - #2CA02C
- 红色（警告）：RGB(214, 39, 40) - #D62728

### 辅助色
- 青色：RGB(23, 190, 207) - #17BECE
- 紫色：RGB(148, 103, 189) - #9467BD
- 粉色：RGB(227, 119, 194) - #E377C2
- 棕色：RGB(140, 86, 75) - #8C564B

### 灰度
- 浅灰（背景）：RGB(233, 233, 233) - #E9E9E9
- 深灰（文字）：RGB(77, 77, 77) - #4D4D4D

## Python 使用

```python
import matplotlib.pyplot as plt

# 定义颜色
COLORS = {
    'primary': '#1F77B4',
    'secondary': '#FF7F0E',
    'success': '#2CA02C',
    'warning': '#D62728',
}

# 使用
plt.plot(x, y, color=COLORS['primary'], label='Model')
plt.fill_between(x, y_low, y_high, color=COLORS['primary'], alpha=0.2)
```

## LaTeX TikZ 使用

```latex
\definecolor{primary}{RGB}{31,119,180}
\definecolor{secondary}{RGB}{255,127,14}
\definecolor{success}{RGB}{44,160,44}
\definecolor{warning}{RGB}{214,39,40}

% 使用
\fill[primary] (0,0) rectangle (1,1);
```

## 无障碍设计
- 所有配色都符合色盲友好标准
- 使用 ColorBrewer 2.0 配色方案
- 对比度 > 4.5:1（WCAG AA 标准）
```

### latex_packages.md（LaTeX 宏包）

```markdown
# LaTeX 宏包使用

## 必需宏包

### 基础
```latex
\usepackage[utf8]{inputenc}      % 编码
\usepackage[T1]{fontenc}          % 字体
\usepackage{geometry}             % 页面边距
\geometry{margin=1in}
```

### 数学
```latex
\usepackage{amsmath}              % 数学公式
\usepackage{amssymb}              % 数学符号
\usepackage{bm}                   % 粗体数学符号
```

### 图表
```latex
\usepackage{graphicx}             % 图片
\usepackage{float}                % 浮动体控制
\usepackage{subcaption}           % 子图
\usepackage{booktabs}             % 三线表
```

### 绘图
```latex
\usepackage{tikz}                 % 绘图
\usetikzlibrary{shapes,arrows,positioning}
\usepackage{pgfplots}             % 统计图
\pgfplotsset{compat=1.17}
```

### 参考文献
```latex
\usepackage{hyperref}             % 超链接
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue
}
```

## 模板代码

### 图表插入
```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.8\textwidth]{figures/fig1_flowchart.png}
\caption{Methodology flowchart. The proposed approach consists of three stages: data processing, model training, and validation.}
\label{fig:flowchart}
\end{figure}
```

### 三线表
```latex
\begin{table}[htbp]
\centering
\caption{Model comparison}
\label{tab:model_comparison}
\begin{tabular}{lccc}
\toprule
Model & RMSE & MAE & $R^2$ \\
\midrule
ZINB & 4.2 & 3.1 & 0.78 \\
Poisson & 5.1 & 3.8 & 0.72 \\
ARIMA & 4.8 & 3.5 & 0.75 \\
\bottomrule
\end{tabular}
\end{table}
```

### 流程图（TikZ）
```latex
\begin{figure}[htbp]
\centering
\begin{tikzpicture}[
    node distance=1.5cm,
    auto,
    block/.style={rectangle, draw, fill=blue!20, text width=5em, text centered, rounded corners, minimum height=3em},
    line/.style={draw, -latex'}
]
\node [block] (data) {Data};
\node [block, right=of data] (model) {Model};
\node [block, right=of model] (validate) {Validation};
\path [line] (data) -- (model);
\path [line] (model) -- (validate);
\end{tikzpicture}
\caption{Methodology flowchart}
\label{fig:tikz_flowchart}
\end{figure}
```
```

---

## 第四部分：使用协议

### Session 启动（One-Shot 学习）

```markdown
# One-Shot 学习指令

Claude Code，请执行以下学习：

## Step 1: 完整阅读参考论文

**Read**: reference/best_paper_example/2023_C_OPrize.pdf

**学习要点**：
1. 论文结构（IMRaD）
2. 图表类型和数量
3. 数学公式写法
4. 参考文献格式
5. 写作风格（观察-洞察模式）

## Step 2: 阅读 LaTeX 源码

**Read**: reference/best_paper_example/2023_C_OPrize.tex

**学习要点**：
1. 使用的宏包（\usepackage）
2. 图表排版方式
3. 公式编号和引用
4. 参考文献管理

## Step 3: 提取风格特征

**Read**: reference/best_paper_example/style_extraction/*.md

**学习要点**：
1. 目录结构（structure.md）
2. 配色方案（color_palette.md）
3. LaTeX 模板（latex_packages.md）

## Step 4: 应用到当前问题

**目标**：我要与之 **1:1 的专业度**。

**要求**：
1. 复制目录结构
2. 使用相同的配色方案
3. 使用相同的 LaTeX 宏包
4. 复制绘图代码（TikZ）
5. 使用相同的写作风格
6. 包含所有必需的统计检验

确认理解后，开始执行任务。
```

### 写作时的参考指令

```markdown
# 写作参考指令

Claude Code，撰写 Results 章节时：

1. **参考结构**：
   - Read: reference/best_paper_example/style_extraction/structure.md
   - 复制 Results 章节的子节结构

2. **参考风格**：
   - Read: reference/best_paper_example/2023_C_OPrize.pdf
   - 找到 Results 章节
   - 学习：
     - 如何引入图表
     - 如何描述结果
     - 如何使用观察-洞察模式

3. **参考配色**：
   - Read: reference/best_paper_example/style_extraction/color_palette.md
   - 使用相同的 RGB 值生成图表

4. **参考 LaTeX**：
   - Read: reference/best_paper_example/2023_C_OPrize.tex
   - 复制图表插入代码
   - 复制表格代码
   - 复制公式代码

5. **输出**：
   - 使用 tools/chart_generator.py 生成图表
   - 使用 tools/latex_builder.py 编译
   - 确保 PDF 与参考论文风格一致
```

---

## 第五部分：与原计划的对比

### 参考学习对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **学习方式** | 自动化提取 44 篇论文的模式 | One-Shot 学习 1 篇完整论文 |
| **输出** | JSON 风格指南 | 完整论文 + LaTeX 源码 |
| **内容** | 摘要长度、图表数量等统计 | 论文结构、配色、LaTeX 代码 |
| **Python 脚本** | generate_style_guide.py | 无 |
| **学习深度** | 浅层模式 | 深层理解 |
| **灵活性** | 僵化（基于统计） | 灵活（基于理解） |

### 核心改变

1. **从"统计"到"理解"**
   - 不计算摘要长度、图表数量
   - 理解论文为什么这样写

2. **从"提取"到"学习"**
   - 不用 NLP 提取模式
   - Claude Code 完整阅读并学习

3. **从"自动化"到"手动精选"**
   - 不自动分析 44 篇论文
   - 手工选择 1 篇最佳论文作为范例

---

## 快速开始

### 设置参考论文

```bash
# 1. 创建目录
mkdir -p reference/best_paper_example/{figures,code,style_extraction}

# 2. 选择论文
# 从 44 篇 O-Prize 论文中选择 1 篇最佳论文
# 标准：结构完整、图表优秀、统计严谨、LaTeX 可用

# 3. 复制文件
cp path/to/2023_C_OPrize.pdf reference/best_paper_example/
cp path/to/2023_C_OPrize.tex reference/best_paper_example/

# 4. 提取图表（手动）
# 从 PDF 中提取所有图表，保存到 figures/

# 5. 提取代码（手动）
# 从论文附录或 GitHub 提取代码，保存到 code/

# 6. 提取风格（手动）
# 创建 style_extraction/ 下的 3 个文件：
# - structure.md
# - color_palette.md
# - latex_packages.md

# 7. 创建 README.md
# 参见本文档的 README.md 内容
```

### 使用参考论文

```markdown
# 启动指令

Claude Code，请：

1. **One-Shot 学习**：
   - Read: reference/best_paper_example/2023_C_OPrize.pdf
   - Read: reference/best_paper_example/2023_C_OPrize.tex
   - Read: reference/best_paper_example/style_extraction/*.md

2. **确认理解**：
   - 你记住了论文的哪些结构？
   - 你记住了哪些配色方案？
   - 你记住了哪些 LaTeX 宏包？

3. **应用到当前问题**：
   - "开始撰写 2025_C 论文，我要与参考论文 1:1 的专业度"
```

---

**版本**: Revised
**核心理念**: One-Shot 完整学习，不是模式提取
**关键**: 1 篇完整论文，LaTeX 源码，手动提取风格要素

---

**END OF 04_REFERENCE_LEARNING_REVISED.md**
