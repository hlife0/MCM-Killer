# MMAgent: Engine 模块

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/06_MMAgent_Engine.md`
> **重要程度**: ⭐⭐⭐⭐ 引擎组件
> **迁移价值**: **中** - 特定功能引擎可复用

本目录（`MMAgent/engine/`）包含 LLM-MM-Agent 系统的 10 个引擎组件，每个引擎负责特定的专业功能。这些引擎提供了图表渲染、特征工程、知识检索、模型竞技场、鲁棒性测试、敏感度分析、验证套件等高级功能。

---

## 10 个引擎

### 1. `chart_renderer.py` ⭐⭐⭐
**图表渲染引擎**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/chart_renderer.py`。负责将数据和配置渲染为可视化图表。

---

### 2. `diagram_engine.py` ⭐⭐⭐
**图引擎**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/diagram_engine.py`。生成系统架构图、流程图等。

---

### 3. `feature_engineer.py` ⭐⭐⭐⭐⭐
**特征工程引擎**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/feature_engineer.py`。自动提取和构造特征。

**迁移价值**：特征工程是数据分析和机器学习的基础，可以复用到任何需要特征处理的系统。

---

### 4. `knowledge_retriever.py` ⭐⭐⭐⭐⭐
**知识检索器**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/knowledge_retriever.py`。从知识库检索相关信息。

**迁移价值**：知识检索是实现智能系统的基础技术。

---

### 5. `model_arena.py` ⭐⭐⭐
**模型竞技场**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/model_arena.py`。比较不同模型的性能。

**迁移价值**：模型评估模式可以用于任何需要模型选择的系统。

---

### 6. `robustness_tester.py` ⭐⭐⭐
**鲁棒性测试器**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/robustness_tester.py`。测试系统的鲁棒性和稳定性。

**迁移价值**：鲁棒性测试是质量保障的重要环节。

---

### 7. `scientific_renderer.py` ⭐⭐⭐
**科学渲染器**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/scientific_renderer.py`。生成科学论文格式的渲染输出。

---

### 8. `sensitivity_analyzer.py` ⭐⭐⭐
**敏感度分析器**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/sensitivity_analyzer.py`。分析模型对参数变化的敏感度。

**迁移价值**：敏感度分析是模型验证的重要工具。

---

### 9. `sensitivity_engine.py` ⭐⭐⭐
**敏感度引擎**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/sensitivity_engine.py`。执行敏感度分析计算。

---

### 10. `validation_suite.py` ⭐⭐⭐
**验证套件**，绝对路径：D:/migration/clean version/LLM-MM-Agent/MMAgent/engine/validation_suite.py`。提供一系列验证测试。

**迁移价值**：验证框架可以复用到任何系统。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
**引擎总数**: 10 个
