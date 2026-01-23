# MCM-Killer: 项目根目录

> Path: `MCM-Killer/`

---

### `README.md`
项目主文档，介绍MCM-Killer系统的架构、功能、使用方法。包含快速开始指南、18阶段工作流概览、13+Agent介绍、验证门控说明。

---

### `.gitignore`
Git忽略文件配置，指定不需要版本控制的文件和目录。如输出目录、缓存文件、敏感信息等。

---

### `.git/`
Git版本控制目录，存储版本历史和配置。
- `HEAD`：当前分支引用
- `config`：仓库配置
- `description`：仓库描述
- `hooks/`：Git钩子脚本（applypatch-msg, commit-msg等）
- `objects/`：Git对象存储
- `refs/`：分支和标签引用

---

### `.claude/`
Claude Code配置目录。

### `.claude/settings.local.json`
Claude Code本地配置，存储项目特定的Claude设置。

---

### `architectures/`
架构版本历史目录，记录系统架构的演进历史。详见"Architectures"文档。

---

### `workspace/`
工作空间目录，包含各个竞赛年份的工作目录。详见"Workspace"文档。

---

### `LaTeX__Template_for_MCM_ICM/`
MCM/ICM论文LaTeX模板目录。详见"LaTeX模板"文档。

---

**文档版本**: v1.0
