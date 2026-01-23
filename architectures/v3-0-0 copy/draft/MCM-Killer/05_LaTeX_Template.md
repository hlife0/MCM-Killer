# MCM-Killer: LaTeX 论文模板

> Path: `MCM-Killer/LaTeX__Template_for_MCM_ICM/`

---

## 核心文件

### `mcmthesis.cls`
**MCM/ICM论文文档类** - 自定义LaTeX文档类，完全符合MCM/ICM竞赛格式要求。定义了页面布局（页边距、页眉页脚）、字体设置、行距、标题样式、章节格式、摘要页设置、控制编号规则等。使用该文档类可确保论文格式符合竞赛要求，无需手动调整格式。

### `mcmthesis-demo.tex`
**模板示例文件** - 展示如何使用mcmthesis文档类编写论文。包含完整的使用示例：标题页、摘要、关键词、章节、图表、公式、算法、引用、参考文献等各元素。是学习和使用模板的最佳参考。

### `mcmthesis-demo.pdf`
**编译后的示例PDF** - 展示模板编译后的最终效果。可直接查看各元素的样式和布局，作为论文样式的参考。

### `mcmthesis.pdf`
**模板使用说明文档** - 详细说明模板的功能、使用方法、自定义选项。包含安装指南、基本用法、高级功能、常见问题解答。

---

## Figures 目录 (`figures/`)

### `example-image-a.pdf`
示例图片A，用于测试图片插入功能。

### `example-image-b.pdf`
示例图片B，用于测试图片插入功能。

### `example-image-c.pdf`
示例图片C，用于测试图片插入功能。

### `mcmthesis-logo.pdf`
MCM thesis logo图片，可用于论文封面或页眉。

### `qrcodewechat.jpg`
微信二维码图片，模板中用于演示图片插入和定位。

---

## Code 目录 (`code/`)

### `mcmthesis-matlab1.m`
MATLAB代码示例，展示如何在论文中插入和格式化MATLAB代码。包含代码高亮、行号、注释等样式。

### `mcmthesis-sudoku.cpp`
C++代码示例（数独求解算法），展示如何在论文中插入和格式化C++代码。演示算法伪代码和实际代码的排版。

---

## 模板特性

### 格式规范
- 页面尺寸：8.5in × 11in（US Letter）
- 页边距：符合MCM/ICM要求
- 字体：Times New Roman（正文）、Arial（标题）
- 行距：1.5倍行距
- 页面编号：从摘要页开始编号

### 摘要页
- 单独的摘要页
- 不含页码
- 包含题目、摘要正文、关键词
- 团队控制编号格式

### 章节结构
- 支持多级标题（section, subsection, subsubsection）
- 自动编号
- 符合学术论文规范

### 图表支持
- 图表自动编号
- 图表标题中英文双语
- 灵活的图表布局
- 支持跨页图表

### 公式支持
- 行内公式和块级公式
- 公式自动编号
- 支持多行公式、对齐

### 引用支持
- 参考文献自动编号
- 支持多种引用格式
- BibTeX集成

---

## 使用方法

### 基本使用
```latex
\documentclass{mcmthesis}
\begin{document}
\title{Your Paper Title}
\author{Team \#12345}
\date{\today}
\maketitle

\begin{abstract}
Your abstract here...
\end{abstract}

\section{Introduction}
Your content...

\end{document}
```

### 编译
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

---

**文档版本**: v1.0
