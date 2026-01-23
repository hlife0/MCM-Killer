# LLM-MM-Agent: MMBench 数据集

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/06_MMBench.md`
> **重要程度**: ⭐⭐⭐ 测试与评估基础
> **迁移价值**: **中** - 数据集格式和评估框架可复用

MMBench 是专门为数学建模竞赛设计的数据集和评估系统，包含历年 MCM/ICM 竞赛题目、数据文件、评估框架。是系统测试、方法验证、性能评估的基础平台。数据集目录（dataset/）存储历年竞赛题目的原始数据文件，按年份和题目编号组织，从 2000 年到 2025 年，涵盖各类题型（连续型、数据洞察型、跨学科型）。问题目录（problem/）存储历年题目的 JSON 格式陈述，是系统的输入数据源。评估目录（evaluation/）包含评估模型、评估提示词、单次/批量评估运行器，提供了完整的评估框架。

**迁移价值**：MMBench 数据集的价值在于：1）标准化的数据格式（JSON 题目格式、CSV/XLS 数据格式）；2）完整的评估框架（评估模型、评估提示词、批量评估）；3）25 年的历史数据覆盖。在迁移时，这些标准化格式和评估框架可以复用。虽然具体的数据内容（2000-2025 年的题目）可能不适用于新场景，但数据组织方式、评估方法、JSON schema 设计等都值得借鉴。特别是 evaluation/ 目录的评估框架是独立于具体数据的，可以直接应用到其他评估场景。

---

### `README.md` ⭐⭐
**数据集说明文档**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMBench/README.md`。介绍 MMBench 的组织结构、数据格式、使用方法。

**迁移价值**：文档结构和组织方式可以参考。

---

### `dataset/` 目录 ⭐
**数据集目录**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMBench/dataset/`。存储历年竞赛题目的原始数据文件，包含 2000_C 到 2025_C 等多个年份的数据。关键年份数据（如 2006_C 的 WHO 数据、2019_C 的毒品数据、2021_C 的图像数据）展示了多样化的数据类型和规模。

**迁移价值**：数据集展示了竞赛题目的多样性。在迁移时，需要考虑支持更多类型的数据（文本、图像、视频、时间序列、图数据等）和更大的数据规模。

---

### `problem/` 目录 ⭐
**问题目录**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMBench/problem/`。存储历年题目的 JSON 格式陈述，文件命名规则为 {YEAR}_{LETTER}.json（如 2000_A.json, 2024_C.json）。

**迁移价值**：JSON schema 设计非常规范，包含 year、type、letter、title、description、requirements、data_files 等字段。这种结构化的题目表示方式值得借鉴。

---

### `evaluation/` 目录 ⭐⭐⭐⭐⭐⭐
**评估目录**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMBench/evaluation/`。包含 model.py（评估模型实现）、prompts.py（评估提示词）、run_evaluation.py（单次评估）、run_evaluation_batch.py（批量评估）。

**迁移价值**：评估框架是独立的，不依赖具体数据。可以直接应用到其他评估场景。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
