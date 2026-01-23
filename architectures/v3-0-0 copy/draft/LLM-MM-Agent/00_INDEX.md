# LLM-MM-Agent 文件结构文档

> Path: `clean version/LLM-MM-Agent/`

## 文档导航

| 文档 | 描述 |
|------|------|
| [01_Project_Root.md](01_Project_Root.md) | 项目根目录文件（config.yaml, README, run.py等） |
| [02_MMAgent_Core.md](02_MMAgent_Core.md) | MMAgent核心模块（main.py, core/, engine/等） |
| [03_Agents.md](03_Agents.md) | Agent模块（coordinator, task_solving, 各种agent） |
| [04_Utilities.md](04_Utilities.md) | 工具集（utils/下40+工具模块） |
| [05_HMML.md](05_HMML.md) | HMML数学建模知识库 |
| [06_MMBench.md](06_MMBench.md) | MMBench数据集和评估系统 |
| [07_Test_Infrastructure.md](07_Test_Infrastructure.md) | 测试基础设施（35+测试） |

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
