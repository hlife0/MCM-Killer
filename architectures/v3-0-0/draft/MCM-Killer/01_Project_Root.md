# MCM-Killer: 项目根目录

> Path: `MCM-Killer/`
> **重要程度**: ⭐⭐⭐ 项目组织中心

MCM-Killer 项目根目录包含系统的顶层组织结构，包括版本控制、架构文档、工作空间、LaTeX 模板等核心组成部分。

---

### `README.md` ⭐⭐⭐
**项目主文档**，介绍 MCM-Killer 系统的完整架构、核心功能、使用方法。包含系统概述（18 阶段工作流、13+ Agent）、快速开始指南、核心规则说明、数据权威层级、与 LLM-MM-Agent 的区别对比。是新用户理解系统的首选文档。

---

### `.gitignore` ⭐⭐
**Git 忽略文件配置**，指定不需要版本控制的文件和目录。包括输出目录（output/）、缓存文件（__pycache__）、敏感信息（API 密钥）、临时文件等。确保仓库干净，避免提交不必要的文件。

---

### `.git/` ⭐
**Git 版本控制目录**，存储版本历史和配置。包含 HEAD（当前分支引用）、config（仓库配置）、objects（Git 对象存储）、refs（分支和标签引用）、hooks/（Git 钩子脚本）。是版本控制的核心。

---

### `.claude/` ⭐⭐
**Claude Code 配置目录**，存储 Claude Code 助手的项目特定配置和设置。用于定制 Claude 在该项目中的行为。

---

### `.claude/settings.local.json` ⭐⭐
**Claude Code 本地配置**，存储项目特定的 Claude 设置。包括模型选择、温度参数、最大 tokens、自定义提示词等。不同开发者可以有各自不同的本地配置。

---

### `architectures/` ⭐⭐⭐
**架构版本历史目录**，记录系统架构的演进历史。从 v2-3-0 到 v3-0-0 的各个版本，每个版本都有完整的架构文档。是理解系统设计演变的重要资源。详见"Architectures"文档。

---

### `workspace/` ⭐⭐⭐
**工作空间目录**，包含各个竞赛年份的工作目录。当前活跃的是 2025_C，包含问题文件、Agent 定义、输出目录、参考论文等。是系统运行的主要工作区域。详见"Workspace"文档。

---

### `LaTeX__Template_for_MCM_ICM/` ⭐⭐⭐
**MCM/ICM 论文 LaTeX 模板目录**，包含完全符合竞赛要求的论文模板。提供文档类（mcmthesis.cls）、示例文件（mcmthesis-demo.tex）、使用说明（mcmthesis.pdf）、图片资源（figures/）、代码示例（code/）。确保生成的论文格式符合竞赛要求，无需手动调整格式。详见"LaTeX 模板"文档。

---

**文档版本**: v1.0
