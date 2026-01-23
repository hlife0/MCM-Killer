# MCM-Killer: Workspace 工作目录

> Path: `MCM-Killer/workspace/2025_C/`
> **重要程度**: ⭐⭐⭐ 活跃工作空间

本目录是 MCM-Killer 系统的活跃开发空间，包含当前竞赛（2025_C）的完整工作环境。所有 Agent 执行、数据存储、结果输出都在此目录进行。

---

## 核心文件

### `CLAUDE.md` ⭐⭐⭐
**Claude Code 指导文档**，MCM-Killer 系统的操作手册。定义 18 阶段工作流程（Phase 0 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5 → 5.5 → 6 → 6.5 → 7 → 7.5 → 8 → 9 → 9.5 → 10）、13+ 专业 Agent 职责（Reader, Researcher, Modeler, Feasibility Checker, Data Engineer, Code Translator, Model Trainer, Validator, Visualizer, Writer, Editor, Advisor, Time Validator, Summarizer）、7 个验证门控规则（Phase 0.5, 1.5, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9, 9.5, 10）、三层数据权威层级（CSV Level 1 > Agent Reports Level 2 > Paper Level 3）。是使用 MCM-Killer 系统的必读文档，指导如何按顺序执行各个阶段、在验证门控处停下来检查质量、确保数据的权威性。

### `.mcp.json` ⭐⭐
**MCP (Model Context Protocol) 配置文件**，定义模型上下文协议的参数和设置。控制 LLM 上下文窗口、Token 限制、超时设置等。

### `.claude/settings.local.json` ⭐⭐
**Claude Code 本地配置**，存储 2025_C 工作空间特定的 Claude 设置。可以覆盖全局配置，针对当前竞赛进行定制。

---

## 问题文件

### `2025_MCM_Problem_C.pdf` ⭐⭐⭐
**2025 年 MCM 问题 C 的 PDF 文件**，包含完整的问题陈述、背景信息、具体要求、数据描述。是系统分析和求解的目标，所有工作都围绕解决这个问题展开。

### `2025_Problem_C_Data.zip` ⭐⭐⭐
**问题 C 数据压缩包**，包含所有相关的数据文件。解压后得到 2025_Problem_C_Data 目录，包含多个 CSV 数据文件（summerOly_hosts.csv, summerOly_athletes.csv, summerOly_medal_counts.csv, summerOly_programs.csv）和数据字典（data_dictionary.csv）。是问题求解的数据基础。

---

## 数据文件 (`2025_Problem_C_Data/`)

### `summerOly_hosts.csv` ⭐⭐⭐
**夏季奥运会主办城市数据**，包含历届夏奥会的主办城市、国家、年份、届次等信息。是分析奥运会历史和地理分布的基础数据。

### `summerOly_athletes.csv` ⭐⭐⭐
**夏季奥运会运动员数据**，包含参赛运动员的个人信息（姓名、性别、年龄）、国家信息、项目信息、成绩信息（奖牌、名次）。是分析运动员参与和表现的核心数据。

### `summerOly_medal_counts.csv` ⭐⭐⭐
**夏季奥运会奖牌统计**，记录各国在各届夏奥会获得的奖牌数量（金、银、铜、总计）。是评估国家体育表现的关键指标。

### `summerOly_programs.csv` ⭐⭐
**夏季奥运会比赛项目数据**，包含各届夏奥会的比赛项目、规则变化、新增/取消项目等信息。是分析奥运会项目演变的数据源。

### `data_dictionary.csv` ⭐⭐⭐
**数据字典**，说明各数据文件的字段含义、数据类型、取值范围、编码说明。是理解和使用数据的参考文档，确保数据解读的正确性。

---

## 参考论文 (`reference_papers/`)

### 学术论文 PDF 集合 ⭐⭐
**包含 50+ 篇学术论文 PDF**，涉及奥林匹克建模、体育分析、预测方法、时间序列分析、回归分析、排名系统等相关领域。文件名格式为数字编号.pdf（如 2002116.pdf, 2425454.pdf）。这些论文为问题解决提供理论基础、方法参考、案例借鉴。是 Researcher Agent 进行文献调研的主要资源。

---

## LaTeX 模板 (`latex_template/`)

### `mcmthesis.cls` ⭐⭐⭐
**MCM/ICM 论文文档类**，自定义 LaTeX 文档类，完全符合 MCM/ICM 竞赛格式要求。定义页面布局（页边距、页眉页脚）、字体设置（Times New Roman）、行距（1.5 倍）、标题样式、章节格式、摘要页设置、控制编号规则等。

### `mcmthesis-demo.tex` ⭐⭐
**模板示例文件**，展示如何使用 mcmthesis 文档类编写论文。包含完整的使用示例：标题页、摘要、关键词、章节、图表、公式、引用、参考文献等各元素。

### `mcmthesis-demo.pdf` ⭐⭐
**编译后的示例 PDF**，展示模板编译后的最终效果。可直接查看各元素的样式和布局，作为论文样式的参考。

### `mcmthesis.pdf` ⭐⭐
**模板使用说明文档**，详细说明模板的功能、使用方法、自定义选项。包含安装指南、基本用法、高级功能、常见问题解答。

### `figures/` ⭐
**图片资源目录**，包含示例图片和 logo。如 example-image-a/b/c.pdf（测试图片）、mcmthesis-logo.pdf（Logo）、qrcodewechat.jpg（二维码）。

### `code/` ⭐
**代码示例目录**，包含 MATLAB 和 C++ 代码示例。mcmthesis-matlab1.m 展示 MATLAB 代码插入，mcmthesis-sudoku.cpp 展示 C++ 代码插入和算法伪代码。

---

## Agent 定义 (`.claude/agents/`)

### 13+ 专业 Agent 定义 ⭐⭐⭐
每个 Agent 都有独立的 Markdown 文件，定义其职责、输入输出、工作流程、协作关系。详见"Agent 定义"文档（03_Agents.md）。包括：
- **advisor.md**：顾问 Agent，提供战略建议
- **code_translator.md**：代码翻译 Agent，将设计转换为代码
- **data_engineer.md**：数据工程师 Agent，数据清洗和特征工程
- **editor.md**：编辑 Agent，语言优化和格式修正
- **feasibility_checker.md**：可行性检查 Agent，评估方案可行性
- **model_trainer.md**：模型训练 Agent，机器学习模型训练与调优
- **modeler.md**：建模 Agent，数学模型构建与设计
- **reader.md**：阅读 Agent，问题理解和数据读取
- **researcher.md**：研究 Agent，文献调研和方法研究
- **summarizer.md**：总结 Agent，内容摘要和要点提炼
- **time_validator.md**：时间验证 Agent，进度控制和时间管理
- **validator.md**：验证 Agent，结果验证和质量检查
- **visualizer.md**：可视化 Agent，图表设计和生成
- **writer.md**：写作 Agent，论文撰写和报告生成

---

## 输出目录 (`output/`)

### `VERSION_MANIFEST.json` ⭐⭐⭐
**版本清单**，单一数据来源（Single Source of Truth）。记录版本号、最后更新时间、各阶段状态、Agent 签名、校验和（MD5/SHA256）。确保数据的可追溯性和一致性，是输出管理的核心。

### `problem/` ⭐⭐
**问题文件目录**，存储问题陈述（PDF）、问题摘要（Markdown）、理解笔记（分析报告）。

### `docs/` ⭐⭐⭐
**文档目录**，包含：
- `consultations/`：咨询记录，记录与 Advisor Agent 的对话和建议
- `validations/`：验证报告，记录各验证门控的检查结果和问题发现
- `reports/`：阶段报告，记录各阶段的输出、总结和决策

### `model/` ⭐⭐⭐
**模型设计目录**，存储模型设计方案（Markdown）、方法选择文档、可行性报告、数学公式（LaTeX）。

### `implementation/` ⭐⭐⭐
**实现目录**，包含：
- `code/`：源代码文件（Python/MATLAB）
- `data/`：数据文件（CSV/PKL），**Level 1 最高权威**
- `logs/`：执行日志（DEBUG/INFO/WARNING/ERROR）
- `models/`：训练好的模型文件（PKL/H5/PTH）
- `.venv/`：隔离 Python 环境（依赖管理）

### `paper/` ⭐⭐⭐
**论文目录**，包含：
- `paper.tex`：LaTeX 源文件
- `figures/`：图片文件（PNG/PDF/EPS）
- `summary.md`：摘要
- `paper.pdf`：最终 PDF，**Level 3 最低权威**

**重要原则**：Paper 必须始终与 CSV 数据一致。如果 Paper 和 CSV 不同，Paper 是错的。

---

**文档版本**: v1.0
