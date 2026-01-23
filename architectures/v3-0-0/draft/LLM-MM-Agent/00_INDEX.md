# LLM-MM-Agent 文件结构文档

> Path: `clean version/LLM-MM-Agent/`
> **重要程度**: ⭐⭐⭐ 核心导航文档

本文档是 LLM-MM-Agent 项目的总索引，为开发者和研究人员提供完整的文件结构导航。LLM-MM-Agent 是一个发表于 NeurIPS 2025 和 ICML 2025 的学术研究原型系统，专注于使用大语言模型解决数学建模竞赛问题。通过本文档，用户可以快速定位和理解项目中各个模块的功能、位置和相互关系，是进入项目代码库的首要入口点。

## 文档导航

| 文档 | 描述 | 重要程度 |
|------|------|----------|
| [01_Project_Root.md](01_Project_Root.md) | 项目根目录文件（config.yaml, README, run.py等），包含配置管理、依赖定义、文档说明和启动脚本 | ⭐⭐⭐ |
| [02_MMAgent_Core.md](02_MMAgent_Core.md) | MMAgent核心模块（main.py, core/, engine/等），详细说明主入口、核心组件、引擎、数据处理、知识库、LLM接口等关键模块 | ⭐⭐⭐ |
| [03_Agents.md](03_Agents.md) | Agent模块（coordinator, task_solving, 各种agent），介绍所有Agent的职责、输入输出和工作流程 | ⭐⭐⭐ |
| [04_Utilities.md](04_Utilities.md) | 工具集（utils/下40+工具模块），涵盖安全验证、数据处理、图表生成、执行追踪等辅助功能 | ⭐⭐ |
| [05_HMML.md](05_HMML.md) | HMML数学建模知识库，系统的核心知识源，提供98+数学建模模式的层级化知识 | ⭐⭐⭐ |
| [06_MMBench.md](06_MMBench.md) | MMBench数据集和评估系统，包含历年竞赛题目、数据文件、评估框架 | ⭐⭐ |
| [07_Test_Infrastructure.md](07_Test_Infrastructure.md) | 测试基础设施（35+测试），确保系统正确性和鲁棒性的自动化测试套件 | ⭐⭐ |

## 项目概览

LLM-MM-Agent 是一个基于LLM的数学建模Agent系统，发表于NeurIPS 2025和ICML 2025。

### 核心特性
- **4阶段管道**: Problem Analysis → Mathematical Modeling → Computational Solving → Solution Reporting
- **HMML知识库**: 3层层级，98+数学建模模式
- **DAG任务调度**: 基于依赖关系的子任务编排
- **自动恢复**: 检查点机制支持中断恢复
- **Omni-Survival Kit**: 确保PDF生成的死手开关系统

### 目录结构概览

```
LLM-MM-Agent/
├── config.yaml              # 主配置文件
├── MMAgent/                 # 核心实现
│   ├── main.py             # 入口
│   ├── agent/              # Agent模块
│   ├── core/               # 核心组件
│   ├── engine/             # 引擎组件
│   ├── utils/              # 工具集
│   └── HMML/               # 知识库
├── MMBench/                # 数据集
└── test workplace/         # 测试
```

---

**文档版本**: v1.0
**最后更新**: 2026-01-23
