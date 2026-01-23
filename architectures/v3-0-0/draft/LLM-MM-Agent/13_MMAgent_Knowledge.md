# MMAgent: Knowledge 模块

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/13_MMAgent_Knowledge.md`
> **重要程度**: ⭐⭐⭐ 知识库
> **迁移价值**: **中** - 知识库架构可复用

本目录（`MMAgent/knowledge/`）包含知识库相关模块，提供领域知识和历史知识的存储和检索功能。

---

## 核心文件

### `knowledge_base.py` ⭐⭐⭐⭐⭐
**知识库基类**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/knowledge/knowledge_base.py`。知识库的基础类，定义知识存储和检索的接口。

### `domain_knowledge.json` ⭐⭐⭐⭐⭐
**领域知识**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/knowledge/domain_knowledge.json`。存储数学建模领域的专业知识。

### `history_knowledge.json` ⭐⭐⭐⭐⭐
**历史知识**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/knowledge/history_knowledge.json`。存储历史竞赛的知识和经验。

**迁移价值**：知识库架构可以复用到任何需要知识管理的系统。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
