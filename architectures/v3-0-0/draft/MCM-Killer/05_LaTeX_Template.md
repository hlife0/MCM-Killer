# MCM-Killer: LaTeX 论文模板

> Path: `MCM-Killer/LaTeX__Template_for_MCM_ICM/`
> **重要程度**: ⭐⭐⭐ 论文输出标准

本目录包含 MCM/ICM 竞赛专用的 LaTeX 论文模板。该模板完全符合竞赛格式要求，确保生成的论文无需手动调整格式。是系统输出的最终呈现形式，直接影响竞赛评审的第一印象。

---

## 核心文件

### `mcmthesis.cls` ⭐⭐⭐
**MCM/ICM 论文文档类**，自定义 LaTeX 文档类，完全符合 MCM/ICM 竞赛格式要求。定义了以下关键内容：
- **页面布局**：页边距（1 英寸）、页眉页脚（控制编号、页码）
- **字体设置**：Times New Roman（正文）、Arial（标题）
- **行距**：1.5 倍行距
- **标题样式**：章节格式、摘要页设置
- **控制编号规则**：摘要页无页码，正文从第 1 页开始编号

使用该文档类可确保论文格式符合竞赛要求，避免因格式问题导致扣分。**迁移价值**：这是论文输出的标准格式，需要确保 Claude Code 生成的论文符合此格式要求。

---

### `mcmthesis-demo.tex` ⭐⭐⭐
**模板示例文件**，展示如何使用 mcmthesis 文档类编写论文。包含完整的使用示例：
- 标题页（Team Control Number, Problem Chosen）
- 摘要页（Abstract, Keywords）
- 章节（Section, Subsection, Subsubsection）
- 图表（Figure, Table，自动编号）
- 公式（Equation，自动编号，支持多行公式对齐）
- 引用（Citation，参考文献自动编号）
- 参考文献（Bibliography，BibTeX 集成）

**迁移价值**：这是论文结构和格式的参考范例，Claude Code 需要按照此结构生成论文。

---

### `mcmthesis-demo.pdf` ⭐⭐
**编译后的示例 PDF**，展示模板编译后的最终效果。可直接查看各元素的样式和布局，作为论文样式的视觉参考。

---

### `mcmthesis.pdf` ⭐⭐
**模板使用说明文档**，详细说明模板的功能、使用方法、自定义选项。包含：
- 安装指南（如何安装文档类）
- 基本用法（如何开始编写论文）
- 高级功能（自定义样式、宏包使用）
- 常见问题解答（编译错误、格式调整）

---

## Figures 目录 (`figures/`)

### `example-image-a.pdf` ⭐
示例图片 A，用于测试图片插入功能。

### `example-image-b.pdf` ⭐
示例图片 B，用于测试图片插入功能。

### `example-image-c.pdf` ⭐
示例图片 C，用于测试图片插入功能。

### `mcmthesis-logo.pdf` ⭐
MCM thesis logo 图片，可用于论文封面或页眉。

### `qrcodewechat.jpg` ⭐
微信二维码图片，模板中用于演示图片插入和定位。

---

## Code 目录 (`code/`)

### `mcmthesis-matlab1.m` ⭐
**MATLAB 代码示例**，展示如何在论文中插入和格式化 MATLAB 代码。包含代码高亮、行号、注释等样式。

---

### `mcmthesis-sudoku.cpp` ⭐
**C++ 代码示例**（数独求解算法），展示如何在论文中插入和格式化 C++ 代码。演示算法伪代码和实际代码的排版。

---

## 模板特性

### 格式规范 ⭐⭐⭐
- **页面尺寸**：8.5in × 11in（US Letter）
- **页边距**：1 英寸（符合 MCM/ICM 要求）
- **字体**：Times New Roman（正文）、Arial（标题）
- **行距**：1.5 倍行距
- **页面编号**：从摘要页开始编号

**迁移价值**：这些格式规范是竞赛的硬性要求，Claude Code 生成的论文必须严格遵守。

---

### 摘要页 ⭐⭐⭐
- **单独的摘要页**
- **不含页码**
- **包含题目、摘要正文、关键词**
- **团队控制编号格式**（Team Control Number: XXXXX）

**迁移价值**：摘要是评审的第一印象，必须严格按照此格式生成。

---

### 章节结构 ⭐⭐⭐
- **支持多级标题**（section, subsection, subsubsection）
- **自动编号**（1, 1.1, 1.1.1）
- **符合学术论文规范**

**迁移价值**：章节结构是论文的逻辑框架，Claude Code 需要按照此结构组织论文内容。

---

### 图表支持 ⭐⭐⭐
- **图表自动编号**（Figure 1, Table 1）
- **图表标题中英文双语**
- **灵活的图表布局**（支持跨页图表）
- **图表引用**（如图 1 所示）

**迁移价值**：图表是论文的重要组成部分，Claude Code 需要能够正确生成图表代码和引用。

---

### 公式支持 ⭐⭐⭐
- **行内公式**（$ ... $）
- **块级公式**（\begin{equation} ... \end{equation}）
- **公式自动编号**（(1), (2), ...）
- **支持多行公式、对齐**（\begin{align} ... \end{align}）

**迁移价值**：数学公式是数学建模论文的核心，Claude Code 需要能够正确生成 LaTeX 公式。

---

### 引用支持 ⭐⭐⭐
- **参考文献自动编号**（[1], [2], ...）
- **支持多种引用格式**（APA, MLA, IEEE）
- **BibTeX 集成**（.bib 文件管理参考文献）

**迁移价值**：引用体现学术严谨性，Claude Code 需要能够正确管理引用。

---

## 使用方法

### 基本使用 ⭐⭐⭐
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

**迁移价值**：这是 Claude Code 生成论文时需要遵循的基本模板结构。

---

### 编译 ⭐⭐
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

**迁移价值**：Claude Code 需要能够自动执行这些编译命令，确保论文正确生成。

---

## 与 LLM-MM-Agent 的关系

### LLM-MM-Agent 的输出
LLM-MM-Agent 使用 Omni-Survival Kit 生成 PDF 报告，但格式不一定完全符合 MCM/ICM 竞赛要求。

### MCM-Killer 的改进
MCM-Killer 使用专门的 LaTeX 模板（mcmthesis.cls），确保生成的论文完全符合竞赛格式要求。

**迁移价值**：MCM-Killer 的 LaTeX 模板是对 LLM-MM-Agent 的重要改进，Claude Code 需要采用这个模板。

---

## 关键注意事项

### 1. 格式严格性 ⭐⭐⭐
MCM/ICM 竞赛对论文格式有严格要求，格式错误可能导致扣分甚至取消资格。Claude Code 生成的论文必须完全符合 mcmthesis.cls 定义的格式。

### 2. 摘要页重要性 ⭐⭐⭐
摘要是评审的第一印象，必须按照模板格式生成，包含所有必需元素。

### 3. 图表质量 ⭐⭐⭐
图表必须清晰、专业、符合学术规范。Claude Code 生成的图表代码必须能够编译通过且视觉效果良好。

### 4. 公式正确性 ⭐⭐⭐
数学公式必须语法正确、排版美观。Claude Code 生成的 LaTeX 公式必须能够正确编译。

### 5. 编译成功 ⭐⭐⭐
最终生成的 PDF 必须能够成功编译，无错误、无警告。Claude Code 需要确保生成的 LaTeX 代码完全正确。

---

**文档版本**: v1.0
