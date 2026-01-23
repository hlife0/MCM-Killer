# 两大项目文件结构文档索引

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/README.md`
> **重要程度**: ⭐⭐⭐ 文档导航总入口

---

## 项目列表

| 项目 | 定位 | 文档目录 | 迁移重点 | 扩容影响 |
|------|------|----------|----------|----------|
| **LLM-MM-Agent** | 学术研究原型 (NeurIPS/ICML 2025) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/` | HMML 知识库扩展、DAG 调度扩展 | **极高** - 知识库需扩展 4 倍 |
| **MCM-Killer** | 竞赛优化系统 | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/` | 工作流扩展、Agent 规范标准化 | **极高** - Agent/阶段需扩展 4 倍 |

---

## 快速导航

### LLM-MM-Agent 文档

| 文档 | 绝对路径 | 描述 | 重要程度 | 扩容影响 |
|------|----------|------|----------|----------|
| [总索引](LLM-MM-Agent/00_INDEX.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/00_INDEX.md` | 文档导航 | ⭐⭐⭐ | 高 - 文档结构需支持扩展 |
| [项目根目录](LLM-MM-Agent/01_Project_Root.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/01_Project_Root.md` | config.yaml, requirements.txt | ⭐⭐ | 中 - 配置需支持更多模块 |
| [MMAgent 核心](LLM-MM-Agent/02_MMAgent_Core.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/02_MMAgent_Core.md` | main.py, core/, engine/ | ⭐⭐⭐ | **极高** - 核心架构需可扩展 |
| [Agent 模块](LLM-MM-Agent/03_Agents.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/03_Agents.md` | coordinator, task_solving | ⭐⭐⭐ | **极高** - Agent 协作需扩展 |
| [工具集](LLM-MM-Agent/04_Utilities.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/04_Utilities.md` | utils/ 下 40+ 工具 | ⭐ | 低 - Claude Code 可处理 |
| [HMML 知识库](LLM-MM-Agent/05_HMML.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/05_HMML.md` | HMML 数学建模知识库 | ⭐⭐⭐ | **极高** - 需扩展到 400+ 方法 |
| [MMBench 数据集](LLM-MM-Agent/06_MMBench.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/06_MMBench.md` | MMBench 数据集 | ⭐⭐ | 中 - 测试数据需增加 |
| [测试基础设施](LLM-MM-Agent/07_Test_Infrastructure.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/07_Test_Infrastructure.md` | 35+ 测试文件 | ⭐ | 低 - 测试可动态生成 |

---

### MCM-Killer 文档

| 文档 | 绝对路径 | 描述 | 重要程度 | 扩容影响 |
|------|----------|------|----------|----------|
| [总索引](MCM-Killer/00_INDEX.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/00_INDEX.md` | 文档导航 | ⭐⭐⭐ | 高 - 文档结构需扩展 |
| [项目根目录](MCM-Killer/01_Project_Root.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/01_Project_Root.md` | README, architectures | ⭐⭐ | 中 - 目录结构需扩展 |
| [Workspace 工作目录](MCM-Killer/02_Workspace.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/02_Workspace.md` | workspace/2025_C/ | ⭐⭐⭐ | **极高** - 18 阶段 → 72 阶段 |
| [Agent 定义](MCM-Killer/03_Agents.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/03_Agents.md` | 13+ Agent 定义 | ⭐⭐⭐ | **极高** - 13 Agent → 52 Agent |
| [Architectures 架构历史](MCM-Killer/04_Architectures.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/04_Architectures.md` | 版本演进记录 | ⭐⭐⭐ | **极高** - 架构需支持扩展 |
| [LaTeX 模板](MCM-Killer/05_LaTeX_Template.md) | `D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/05_LaTeX_Template.md` | LaTeX 模板 | ⭐⭐⭐ | 中 - 模板需支持更多章节 |

---



**创建日期**: 2026-01-23
**最后更新**: 2026-01-24
**文档版本**: v3.0
