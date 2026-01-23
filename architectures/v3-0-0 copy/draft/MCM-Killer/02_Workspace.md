# MCM-Killer: Workspace 工作目录

> Path: `MCM-Killer/workspace/2025_C/`

---

## 核心文件

### `CLAUDE.md`
Claude Code指导文档，定义18阶段工作流程、13+专业Agent职责、7个验证门控规则、三层数据权威层级。是MCM-Killer系统的操作手册，指导如何按顺序执行各个阶段，如何在验证门控处停下来检查质量，以及如何确保数据的权威性。

### `.mcp.json`
MCP (Model Context Protocol) 配置文件，定义模型上下文协议的参数和设置。

### `.claude/settings.local.json`
Claude Code本地配置，存储2025_C工作空间特定的Claude设置。

---

## 问题文件

### `2025_MCM_Problem_C.pdf`
2025年MCM问题C的PDF文件，包含完整的问题陈述、要求、背景信息。

### `2025_Problem_C_Data.zip`
问题C数据压缩包，包含所有相关的数据文件。解压后得到2025_Problem_C_Data目录。

---

## 数据文件 (`2025_Problem_C_Data/`)

### `summerOly_hosts.csv`
夏季奥运会主办城市数据，包含历届夏奥会的主办城市、国家、年份等信息。

### `summerOly_athletes.csv`
夏季奥运会运动员数据，包含参赛运动员的个人信息、国家、项目、成绩等。

### `summerOly_medal_counts.csv`
夏季奥运会奖牌统计，记录各国在各届夏奥会获得的奖牌数量（金、银、铜）。

### `summerOly_programs.csv`
夏季奥运会比赛项目数据，包含各届夏奥会的比赛项目、规则变化等信息。

### `data_dictionary.csv`
数据字典，说明各数据文件的字段含义、数据类型、取值范围。是理解和使用数据的参考文档。

---

## 参考论文 (`reference_papers/`)

包含50+篇学术论文PDF，涉及奥林匹克建模、体育分析、预测方法等相关领域。文件名格式为数字编号.pdf（如2002116.pdf, 2425454.pdf）。这些论文为问题解决提供理论基础和方法参考。

---

## LaTeX模板 (`latex_template/`)

### `mcmthesis.cls`
MCM/ICM论文文档类，定义页面格式、标题样式、章节格式、摘要页设置等。

### `mcmthesis-demo.tex`
模板示例文件，展示如何使用mcmthesis文档类，包含各种元素（章节、图表、公式、引用）的使用示例。

### `mcmthesis-demo.pdf`
编译后的示例PDF，展示模板的最终效果。

### `mcmthesis.pdf`
模板使用说明文档，详细说明模板的功能和使用方法。

### `figures/`
图片资源目录，包含示例图片和logo。

### `code/`
代码示例目录，包含MATLAB和C++代码示例。

---

## Agent定义 (`.claude/agents/`)

### `advisor.md`
顾问Agent，提供战略建议和方向指导。在关键决策点提供建议，帮助选择合适的方法和路径。

### `code_translator.md`
代码翻译Agent，将模型设计转换为可执行代码。理解设计文档，生成符合规范的代码。

### `data_engineer.md`
数据工程师Agent，负责数据清洗、预处理、特征工程。处理数据质量问题，准备建模所需的数据。

### `editor.md`
编辑Agent，负责论文的语言优化和格式修正。改进表达、修正语法、统一风格。

### `feasibility_checker.md`
可行性检查Agent，评估方案的可行性。分析时间、资源、技术可行性，识别潜在风险。

### `model_trainer.md`
模型训练Agent，负责机器学习模型的训练与调优。选择算法、调参、评估模型性能。

### `modeler.md`
建模Agent，负责数学模型的构建与设计。根据问题特点设计合适的数学模型。

### `reader.md`
阅读Agent，负责问题理解和数据读取。解析问题陈述，理解要求，加载数据文件。

### `researcher.md`
研究Agent，负责文献调研和方法研究。搜索相关文献，总结方法，提供研究建议。

### `summarizer.md`
总结Agent，负责内容摘要和要点提炼。生成长文档的摘要，提取关键信息。

### `time_validator.md`
时间验证Agent，控制进度和时间。评估各阶段耗时，确保在时间限制内完成。

### `validator.md`
验证Agent，负责结果验证和质量检查。检查结果的正确性、一致性、合理性。

### `visualizer.md`
可视化Agent，负责图表设计和生成。根据分析结果生成清晰、有效的可视化图表。

### `writer.md`
写作Agent，负责论文撰写和报告生成。按照学术规范撰写论文各部分。

---

## 输出目录 (`output/`)

### `VERSION_MANIFEST.json`
版本清单，单一数据来源。记录版本号、最后更新时间、各阶段状态、Agent签名、校验和等。确保数据的可追溯性和一致性。

### `problem/`
问题文件目录，存储问题陈述、问题摘要、理解笔记。

### `docs/`
文档目录，包含：
- `consultations/`：咨询记录，记录与Advisor的对话
- `validations/`：验证报告，记录各验证门控的检查结果
- `reports/`：阶段报告，记录各阶段的输出和总结

### `model/`
模型设计目录，存储模型设计方案、方法选择文档、可行性报告。

### `implementation/`
实现目录，包含：
- `code/`：源代码文件
- `data/`：数据文件（CSV/PKL），Level 1最高权威
- `logs/`：执行日志
- `models/`：训练好的模型文件
- `.venv/`：隔离Python环境

### `paper/`
论文目录，包含：
- `paper.tex`：LaTeX源文件
- `figures/`：图片文件
- `summary.md`：摘要
- `paper.pdf`：最终PDF，Level 3最低权威

---

**文档版本**: v1.0
