# MMAgent: Data 模块

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/12_MMAgent_Data.md`
> **重要程度**: ⭐⭐⭐ 数据模块
> **迁移价值**: **中** - 数据摄取可复用

本目录（`MMAgent/data/`）包含数据处理相关模块。

---

## 核心文件

### `data_ingestor.py` ⭐⭐⭐
**数据摄取器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/data/data_ingestor.py`。负责读取、清洗、转换数据。

**功能**：
- 多格式数据读取（CSV, Excel, JSON）
- 数据清洗和标准化
- 类型推断和转换
- 数据验证

**迁移价值**：数据摄取是任何数据处理系统的第一步。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
