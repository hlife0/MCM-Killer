# MCM-Killer v2.5.0: Agent 契约定义

> **定义每个 Agent 的输入、输出、职责和验证角色**
>
> **版本**: v2.5.0
> **最后更新**: 2026-01-07

---

## 一、Agent 概览

### 1.1 Agent 列表（规范名称）

| # | Agent | 职责 | 参与验证 |
|---|-------|------|---------|
| 0 | director | 编排所有 Agent，管理 workflow | - |
| 1 | reader | 读取 PDF，提取需求 | MODEL, DATA, TRAINING, PAPER, SUMMARY, FINAL |
| 2 | researcher | 方法建议 | MODEL |
| 3 | modeler | 设计数学模型 | DATA, CODE, TRAINING |
| 4 | feasibility_checker | 可行性检查 | MODEL, CODE |
| 5 | data_engineer | 数据处理 | - |
| 6 | code_translator | 代码翻译 | CODE, TRAINING |
| 7 | model_trainer | 模型训练 | - |
| 8 | validator | 结果验证 | DATA, TRAINING, PAPER, SUMMARY, FINAL |
| 9 | visualizer | 生成图表 | - |
| 10 | writer | 撰写论文 | PAPER |
| 11 | summarizer | 创建摘要 | - |
| 12 | editor | 润色文档 | - |
| 13 | advisor | 质量评估 | MODEL, PAPER, FINAL |

> **重要**：所有文档必须使用上述规范名称。

### 1.2 Agent 契约属性

每个 Agent 的契约包含：
- **职责**：核心任务
- **输入**：需要读取的文件
- **输出**：需要产生的文件
- **写入目录**：允许写入的目录
- **参与的 Validation**：作为验证者参与哪些 Stage

---

## 二、Agent 详细契约

### 2.1 Director Agent

**职责**：
- 编排所有其他 Agent
- 管理 10 阶段 workflow
- 触发 Validation Gate
- 处理返工
- 管理 VERSION_MANIFEST.json
- **Token 监控和检查点保存**（v2.5.0 新增）

**输入**：
- 用户指令
- Agent 汇报
- 验证报告

**输出**：
- `output/VERSION_MANIFEST.json`
- `output/.checkpoint_phase{i}.json`（检查点）
- `output/PROJECT_COMPLETION_SUMMARY.md`（最终）

**写入目录**：
- `output/`（所有）

**参与的 Validation**：无（编排者）

**特殊职责**：
- Token 监控（每阶段后检查）
- 检查点保存（每阶段结束时）
- 用户决策请求（当遇到冲突时）

---

### 2.2 Reader Agent

**职责**：
- 读取 PDF，转换为 Markdown
- 提取问题和需求

**输入**：
- `problem/original/*.pdf`

**输出**：
- `problem/problem_full.md`
- `problem/problem_requirements_{i}.md`

**写入目录**：
- `output/problem/`
- `output/docs/`

**参与的 Validation**：MODEL, DATA, TRAINING, PAPER, SUMMARY, FINAL

**验证视角**：题意符合性、Sanity check

---

### 2.3 Researcher Agent

**职责**：
- 文献/方法调研
- 提供方法建议

**输入**：
- `problem/problem_requirements_{i}.md`

**输出**：
- `model/research_notes_{i}.md`

**写入目录**：
- `output/model/`
- `output/docs/`

**参与的 Validation**：MODEL

**验证视角**：方法论可行性、文献支撑

---

### 2.4 Modeler Agent

**职责**：
- 设计数学模型

**输入**：
- `problem/problem_requirements_{i}.md`
- `model/research_notes_{i}.md`

**输出**：
- `model/model_design_{i}.md`

**写入目录**：
- `output/model/`
- `output/docs/`

**参与的 Validation**：DATA, CODE, TRAINING

**验证视角**：模型设计一致性

---

### 2.5 Feasibility Checker Agent

**职责**：
- 可行性检查（技术、时间、资源）

**输入**：
- `model/model_design_{i}.md`

**输出**：
- `model/feasibility_{i}.md`

**写入目录**：
- `output/model/`
- `output/docs/`

**参与的 Validation**：MODEL, CODE

**验证视角**：技术可行性

---

### 2.6 Data Engineer Agent

**职责**：
- 数据处理
- 特征工程
- **数据完整性自检**（v2.5.0 强制）

**输入**：
- `problem/problem_requirements_{i}.md`
- `model/model_design_{i}.md`
- `problem/original/` 下的数据

**输出**：
- `implementation/data/features_{i}.pkl`
- `implementation/data/features_{i}.csv`
- `implementation/code/data_prep_{i}.py`

**写入目录**：
- `output/implementation/data/`
- `output/implementation/code/`
- `output/docs/`

**参与的 Validation**：无

**特殊要求**：
- 必须包含 `check_data_quality()` 函数
- CSV 必须只包含标量值

---

### 2.7 Code Translator Agent

**职责**：
- 将数学模型翻译为代码

**输入**：
- `model/model_design_{i}.md`

**输出**：
- `implementation/code/model_{i}.py`
- `implementation/code/test_{i}.py`

**写入目录**：
- `output/implementation/code/`
- `output/docs/`

**参与的 Validation**：CODE, TRAINING

**验证视角**：代码正确性

---

### 2.8 Model Trainer Agent

**职责**：
- 模型训练
- **两阶段训练**（v2.5.0 新增）

**输入**：
- `model/model_design_{i}.md`
- `implementation/data/features_{i}.pkl`

**输出**：
- `implementation/data/results_quick_{i}.csv`（5A，mandatory）
- `implementation/data/results_{i}.csv`（5B，optional）
- `implementation/logs/training_{i}.log`

**写入目录**：
- `output/implementation/data/`
- `output/implementation/logs/`
- `output/docs/`

**参与的 Validation**：无

**特殊要求**：
- **必须**完成 Phase 5A（快速验证，≤30 min）
- 可选完成 Phase 5B（完整训练，4-6 小时）

---

### 2.9 Validator Agent

**职责**：
- 结果验证（合理性、是否造假）

**输入**：
- `implementation/data/results_{i}.csv`
- 被验证的文件

**输出**：
- `docs/validation/{i}_{stage}_validator.md`

**写入目录**：
- `output/docs/validation/`

**参与的 Validation**：DATA, TRAINING, PAPER, SUMMARY, FINAL

**验证视角**：结果合理性

**特殊要求**：
- 必须运行自动化预检查脚本（如有）
- 检查数据一致性

---

### 2.10 Visualizer Agent

**职责**：
- 生成图表

**输入**：
- `paper/paper_{i}.md`（草稿）
- `implementation/data/results_{i}.csv`

**输出**：
- `paper/figures/figure_{name}_{i}.png`
- `paper/figures/figure_index.md`

**写入目录**：
- `output/paper/figures/`
- `output/docs/`

**参与的 Validation**：无

---

### 2.11 Writer Agent

**职责**：
- 撰写论文

**输入**：
- `problem/problem_requirements_{i}.md`
- `model/model_design_{i}.md`
- `implementation/data/results_{i}.csv`
- `paper/figures/figure_*.png`

**输出**：
- `paper/paper_{i}.md`

**写入目录**：
- `output/paper/`
- `output/docs/`

**参与的 Validation**：PAPER

**验证视角**：表达清晰性

---

### 2.12 Summarizer Agent

**职责**：
- 创建摘要

**输入**：
- `paper/paper_{i}.md`

**输出**：
- `paper/summary/summary_1page.md`

**写入目录**：
- `output/paper/summary/`
- `output/docs/`

**参与的 Validation**：无

---

### 2.13 Editor Agent

**职责**：
- 润色文档

**输入**：
- `paper/paper_{i}.md`
- `paper/summary/summary_1page.md`

**输出**：
- `paper/paper_revised.md`

**写入目录**：
- `output/paper/`
- `output/docs/`

**参与的 Validation**：无

---

### 2.14 Advisor Agent

**职责**：
- 质量评估

**输入**：
- 所有产出文件

**输出**：
- `docs/validation/{i}_{stage}_advisor.md`
- `PROJECT_COMPLETION_SUMMARY.md`

**写入目录**：
- `output/docs/validation/`
- `output/`

**参与的 Validation**：MODEL, PAPER, FINAL

**验证视角**：创新度/质量

---

## 三、Agent 通信格式

### 3.1 完成任务后

```
Director，任务完成。
状态：SUCCESS
产出：{file_paths}
报告：docs/report/{agent}_{i}.md
```

### 3.2 需要咨询时

```
Director，我需要咨询 @{agent}，文件：docs/consultation/{i}_{from}_{to}.md
```

### 3.3 遇到问题时

```
Director，{问题描述}。
```

---

## 四、通用规则

### 4.1 所有 Agent 必须遵守

- ✅ 只写入允许的目录
- ✅ 所有输出文件带版本号
- ✅ 完成后汇报给 Director
- ✅ 遇到问题立即上报
- ❌ 禁止写入 `output/` 以外的文件

### 4.2 作为验证者时

- ✅ 独立判断，禁止 Consultation
- ✅ 以同样标准验证返工版本
- ❌ 禁止降低验证标准

---

**版本**: v2.5.0
**最后更新**: 2026-01-07
