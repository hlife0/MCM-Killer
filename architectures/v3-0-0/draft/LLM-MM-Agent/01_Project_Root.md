# LLM-MM-Agent: 项目根目录

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/01_Project_Root.md`
> **重要程度**: ⭐⭐⭐ 项目配置与文档中心
> **扩容影响**: 中 - 配置需支持更多模块

本目录包含 LLM-MM-Agent 项目的核心配置文件、依赖定义、文档说明和启动脚本。作为项目的顶层目录，它定义了系统的整体运行参数，管理项目依赖关系，提供用户文档和开发指南，并包含项目启动所需的各类初始化文件。开发者在此目录进行项目配置和环境搭建。

**迁移价值**：config.yaml 是系统运行的单一配置入口，在扩容时需要支持更多的配置项（如新的阶段配置、扩展的 HMML 配置、更多的 Agent 配置）。依赖管理需要支持新增的模块和库。文档需要更新以反映扩容后的系统架构。

---

## 配置文件

### `config.yaml` ⭐⭐⭐
**主配置文件**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/config.yaml`。控制整个系统的运行参数和行为模式。定义了核心迭代轮次配置（problem_analysis_round: 3, problem_modeling_round: 3, task_formulas_round: 5）、任务数量限制（num_tasks: 5, num_charts: 5）、方法检索数量（top_method_num: 6）、路径配置（paths.root_data: "MMBench", paths.output_root: "MMAgent/output"）、调试模式开关（debug_mode）以及代码执行超时设置。

**迁移价值**：在扩容到 400+ 方法和 8+ 阶段时，config.yaml 需要支持新增的配置项。例如，需要增加新的阶段配置参数（如 phase_5_round, phase_6_round 等），扩展 HMML 配置（如支持 5 层层级的配置），增加更多的 Agent 配置选项。配置结构需要采用更模块化的设计，支持配置继承和模板化。

### `requirements.txt` ⭐⭐⭐
**Python 依赖包清单**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/requirements.txt`。列出项目所需的所有第三方库及其版本要求。包含数据处理库（pandas, numpy, scipy）、可视化工具（matplotlib, seaborn, plotly）、LLM 接口（openai, anthropic）、日志系统（loguru）、科学计算（sklearn, statsmodels）、文档处理（markdown, pdfkit）等核心依赖。

**迁移价值**：在扩容时需要支持新增的依赖库。例如，如果引入新的 Agent 类型或新的数据处理方法，需要添加相应的依赖包。依赖管理需要更精细的版本控制策略，避免版本冲突。

---

## 文档

### `README.md` ⭐⭐⭐
**项目主文档**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/README.md`。面向国际用户的英文文档，包含项目简介、快速安装指南、基本使用示例、配置参数说明、常见问题解答。提供从零开始使用 LLM-MM-Agent 的完整入门教程，包括环境设置、API 密钥配置、运行第一个任务、理解输出结果等关键步骤。

**迁移价值**：在扩容后需要更新 README 以反映新的系统架构和使用方法。需要添加新的配置说明、新的阶段描述、扩展的 HMML 使用指南。

### `README_zh.md` ⭐⭐
**中文版 README**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/README_zh.md`。为中文用户提供更详细的本地化文档。包含完整的安装步骤（包括 conda 环境配置）、深度使用指南、故障排除方案、最佳实践建议。

**迁移价值**：与英文版 README 同步更新，确保文档一致性。

### `doc/User_Guide.md` ⭐⭐
**详细用户指南**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/doc/User_Guide.md`。比 README 更深入的技术文档。包含完整的安装说明（含依赖冲突解决）、工作流程详细解释（4 阶段管道的每个阶段）、各阶段参数详解、高级用法（自定义方法、批量处理、结果分析）、常见故障排除、性能优化建议等。

**迁移价值**：需要大幅更新以反映扩容后的系统。特别是工作流程部分，需要从 4 阶段扩展到 8+ 阶段的详细说明。

### `CLAUDE.md` ⭐⭐⭐
**Claude Code 指导文档**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/CLAUDE.md`。专为 AI 助手（Claude Code）设计的项目理解指南。提供项目架构概览、核心组件关系图、关键设计模式说明、重要代码路径标注、开发规范和最佳实践。

**迁移价值**：这是理解系统架构的关键文档。在扩容时需要更新以反映新的架构设计、新的 Agent 协作模式、扩展的 HMML 结构。这对于 AI 辅助开发扩容后的系统至关重要。

---

## 启动脚本

### `run.py` ⭐⭐⭐
**启动引导脚本**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/run.py`。自动设置 Python 路径环境并启动主程序。处理常见的导入路径问题（确保能正确导入 MMAgent 模块），验证环境配置，提供友好的错误提示，确保从任何目录都能正确运行系统。

**迁移价值**：在扩容后需要支持新增的模块和组件。需要更新路径设置以支持更多的子目录和模块。

### `__init__.py` ⭐
**包初始化文件**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/__init__.py`。将目录标记为 Python 包，允许使用 import 语句导入模块。

**迁移价值**：在扩容时可能需要添加新的子包初始化文件。

---

## 其他文件

### `LICENSE` ⭐
**开源许可证文件**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/LICENSE`。规定项目的使用、修改、分发条款。

**迁移价值**：不需要修改，许可证保持不变。

### `.DS_Store` ⭐
**Mac 系统自动生成的文件**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/.DS_Store`。

**迁移价值**：无，可以忽略。

### `.gitattributes` ⭐
**Git 属性配置文件**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/.gitattributes`。定义文件的换行符处理、差异比较工具等。

**迁移价值**：不需要修改。

### `logo.png` ⭐
**项目 Logo 图片**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/logo.png`。

**迁移价值**：不需要修改。

### `demo.mp4` ⭐⭐
**演示视频**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/demo.mp4`。展示系统运行的完整过程和用户交互流程。

**迁移价值**：在扩容后可能需要重新录制演示视频以反映新的功能和流程。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
