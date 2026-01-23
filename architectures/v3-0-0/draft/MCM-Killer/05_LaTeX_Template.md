# MCM-Killer: LaTeX 论文模板

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/05_LaTeX_Template.md`
> **重要程度**: ⭐⭐⭐ 论文输出标准
> **迁移价值**: **高** - 论文格式的硬性要求，必须严格遵守

本目录包含 MCM/ICM 竞赛专用的 LaTeX 论文模板，该模板完全符合竞赛格式要求，确保生成的论文无需手动调整格式。mcmthesis.cls 是自定义的 LaTeX 文档类，定义了页面布局（1 英寸页边距）、字体设置（Times New Roman 正文、Arial 标题）、行距（1.5 倍）、标题样式、章节格式、摘要页设置、控制编号规则等关键格式要素。使用该模板可以避免因格式问题导致扣分，是系统输出的最终呈现形式，直接影响竞赛评审的第一印象。

**迁移价值**：LaTeX 模板定义了论文的硬性格式要求，这些要求在扩容后依然适用。在迁移时，mcmthesis.cls 文档类及其相关的样式文件（mcmthesis-demo.tex、figures/、code/）必须完整保留，确保生成的论文符合竞赛要求。mcmthesis-demo.tex 提供了完整的使用示例，展示了如何编写标题页、摘要页、章节、图表、公式、引用、参考文献等各个元素，是学习和使用模板的最佳参考。对于迁移工作来说，这个模板可以作为基础，然后根据扩容后的需求（如更多章节、更多图表、更复杂的引用）进行适当的扩展。

---

### `mcmthesis.cls` ⭐⭐⭐
**MCM/ICM 论文文档类**，绝对路径：`D:/migration/MCM-Killer/LaTeX__Template_for_MCM_ICM/mcmthesis.cls`。自定义 LaTeX 文档类，完全符合 MCM/ICM 竞赛格式要求。定义了页面布局（页边距 1 英寸、页眉页脚、控制编号页码）、字体设置（Times New Roman 正文、Arial 标题）、行距（1.5 倍行距）、标题样式（章节格式、摘要页设置）、控制编号规则（摘要页无页码、正文从第 1 页开始编号）等关键内容。

**迁移价值**：这是论文格式的核心定义文件，在迁移时必须完整保留。文档类中的格式定义是竞赛的硬性要求，任何修改都可能导致扣分。在扩容到更多章节时，可能需要在文档类中添加新的章节样式或编号规则，但核心格式（页边距、字体、行距）必须保持不变。

---

### `mcmthesis-demo.tex` ⭐⭐⭐
**模板示例文件**，绝对路径：`D:/migration/MCM-Killer/LaTeX__Template_for_MCM_ICM/mcmthesis-demo.tex`。展示如何使用 mcmthesis 文档类编写论文的完整示例。包含标题页（Team Control Number, Problem Chosen）、摘要页（Abstract, Keywords）、章节（Section, Subsection, Subsubsection，支持多级标题）、图表（Figure, Table，自动编号，支持中英文双语标题）、公式（Equation，自动编号，支持多行公式对齐）、引用（Citation，参考文献自动编号）、参考文献（Bibliography，BibTeX 集成）等所有学术论文要素的使用方法。

**迁移价值**：这是学习和使用 LaTeX 模板的最佳参考，展示了论文的完整结构和各个要素的编写方法。在迁移时，这个示例文件可以作为基础模板，然后根据扩容后的需求进行修改。例如，如果需要更多的章节，可以参考现有的章节结构添加新的 section；如果需要更多的图表，可以参考现有的图表代码添加新的 figure/table。

---

### `figures/` 目录 ⭐⭐
**图片资源目录**，绝对路径：`D:/migration/MCM-Killer/LaTeX__Template_for_MCM_ICM/figures/`。包含 example-image-a/b/c.pdf（测试图片）、mcmthesis-logo.pdf（Logo）、qrcodewechat.jpg（二维码）等图片资源。

**迁移价值**：图片资源目录在扩容时需要支持更多的图片文件。需要建立图片命名规范（如 figure_01.png, figure_02.png）、图片分类（如 diagrams/, screenshots/）、图片版本管理。

---

### `code/` 目录 ⭐⭐
**代码示例目录**，绝对路径：`D:/migration/MCM-Killer/LaTeX__Template_for_MCM_ICM/code/`。包含 mcmthesis-matlab1.m（MATLAB 代码示例）、mcmthesis-sudoku.cpp（C++ 代码示例）。

**迁移价值**：代码示例在扩容时可能需要支持更多的编程语言（如 Python, R, Julia）和更复杂的代码示例。

---

## 模板特性

### 格式规范 ⭐⭐⭐
- **页面尺寸**：8.5in × 11in（US Letter）
- **页边距**：1 英寸（符合 MCM/ICM 要求）
- **字体**：Times New Roman（正文）、Arial（标题）
- **行距**：1.5 倍行距
- **页面编号**：从摘要页开始编号

### 摘要页 ⭐⭐⭐
- **单独的摘要页**
- **不含页码**
- **包含题目、摘要正文、关键词**
- **团队控制编号格式**

### 章节结构 ⭐⭐⭐
- **支持多级标题**（section, subsection, subsubsection）
- **自动编号**（1, 1.1, 1.1.1）
- **符合学术论文规范**

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
