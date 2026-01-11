# MCM-Killer v2.5.1: Agent 契约定义

> **定义每个 Agent 的输入、输出、职责和验证角色**
>
> **版本**: v2.5.1
> **最后更新**: 2026-01-11

---

## 一、Agent 概览

### 1.1 Agent 列表（规范名称）

| # | Agent | 职责 | 参与验证 | LaTeX相关 |
|---|-------|------|---------|-----------|
| 0 | director | 编排所有 Agent，管理 workflow | - | - |
| 1 | reader | 读取 PDF，提取需求 | MODEL, DATA, TRAINING, PAPER, SUMMARY, FINAL | - |
| 2 | researcher | 方法建议 | MODEL | - |
| 3 | modeler | 设计数学模型 | DATA, CODE, TRAINING | - |
| 4 | feasibility_checker | 可行性检查 | MODEL, CODE | **处理LaTeX环境** |
| 5 | data_engineer | 数据处理 | - | - |
| 6 | code_translator | 代码翻译 | CODE, TRAINING | - |
| 7 | model_trainer | 模型训练 | - | - |
| 8 | validator | 结果验证 | DATA, TRAINING, PAPER, SUMMARY, FINAL | - |
| 9 | visualizer | 生成图表 | - | - |
| 10 | writer | 撰写论文 | PAPER | ✅ **生成.tex/.pdf** |
| 11 | summarizer | 创建摘要 | - | ✅ **生成summary_sheet.tex** |
| 12 | editor | 润色文档 | - | ✅ **处理.tex并重新编译** |
| 13 | advisor | 质量评估 | MODEL, PAPER, FINAL | - |

> **重要**：所有文档必须使用上述规范名称。

### 1.2 Agent 契约属性

每个 Agent 的契约包含：
- **职责**：核心任务
- **输入**：需要读取的文件
- **输出**：需要产生的文件
- **写入目录**：允许写入的目录
- **参与的 Validation**：作为验证者参与哪些 Stage
- **LaTeX要求**：v2.5.1新增字段

---

## 二、Agent 详细契约

### 2.1 Director Agent

**职责**：
- 编排所有其他 Agent
- 管理 10 阶段 workflow
- 触发 Validation Gate
- 处理返工
- 管理 VERSION_MANIFEST.json
- Token 监控和检查点保存
- **验证PDF产出**（v2.5.1新增）

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

**v2.5.1新增职责**：
- **验证Writer产出必须包含.tex和.pdf**
- **拒绝无PDF的论文提交**
- **验证PDF页数≥20页**

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
- **处理LaTeX编译环境问题**（v2.5.1新增）

**输入**：
- `model/model_design_{i}.md`
- **编译错误日志**（v2.5.1新增）

**输出**：
- `model/feasibility_{i}.md`
- **环境修复方案**（v2.5.1新增）

**写入目录**：
- `output/model/`
- `output/docs/`

**参与的 Validation**：MODEL, CODE

**验证视角**：技术可行性

**v2.5.1新增职责**：
- **解决LaTeX编译环境问题**
- **安装缺失的LaTeX包**
- **修复字体缺失问题**
- **通过Consultation响应Writer的编译错误**

---

### 2.6 Data Engineer Agent

**职责**：
- 数据处理
- 特征工程
- 数据完整性自检

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
- 两阶段训练

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
- `paper/paper_{i}.tex`（草稿）- **v2.5.1更新**
- `implementation/data/results_{i}.csv`

**输出**：
- `paper/figures/figure_{name}_{i}.png`
- `paper/figures/figure_index.md`

**写入目录**：
- `output/paper/figures/`
- `output/docs/`

**参与的 Validation**：无

---

### 2.11 Writer Agent ⭐ v2.5.1重大更新

**职责**：
- 撰写MCM论文
- **生成LaTeX源文件和PDF**（v2.5.1强制要求）
- **使用提供的LaTeX模板**（v2.5.1强制要求）

**输入**：
- `problem/problem_requirements_{i}.md`
- `model/model_design_{i}.md`
- `implementation/data/results_{i}.csv`
- `paper/figures/figure_*.png`
- **`latex_template/`**（只读模板，v2.5.1新增）

**输出**：
- **`paper/paper_{i}.tex`**（LaTeX源文件，**强制**）
- **`paper/paper_{i}.pdf`**（编译后的PDF，**强制**）
- **`paper/compile_{i}.log`**（编译日志，**强制**）
- `paper/paper_{i}.md`（Markdown备份，可选）

**写入目录**：
- `output/paper/`
- `output/docs/`

**参与的 Validation**：PAPER

**验证视角**：表达清晰性

**v2.5.1强制要求**：

1. **必须使用LaTeX模板**：
   - 复制 `latex_template/` 到 `output/paper/`
   - 在复制的模板基础上修改
   - ❌ 禁止从零创建.tex

2. **必须编译PDF**：
   - 使用 `xelatex paper_{i}.tex` 编译
   - PDF必须成功生成
   - PDF页数 ≥ 20页
   - 编译日志无ERROR

3. **编译错误处理**：
   - 遇到环境问题必须通过Consultation请求feasibility_checker
   - ❌ 禁止跳过编译
   - ❌ 禁止只输出.md文件
   - ❌ 禁止使用简化方案

**Report必须包含**：
- 编译状态（SUCCESS/FAILED）
- PDF页数
- 编译日志摘要
- 如有失败，详细的错误信息

---

### 2.12 Summarizer Agent ⭐ v2.5.1更新

**职责**：
- 创建摘要
- **生成LaTeX格式的summary sheet**（v2.5.1新增）

**输入**：
- **`paper/paper_{i}.tex`**（v2.5.1更新：读取.tex，不是.md）

**输出**：
- **`paper/summary/summary_sheet_{i}.tex`**（LaTeX格式，**强制**）
- `paper/summary/summary_1page.md`（Markdown格式）

**写入目录**：
- `output/paper/summary/`
- `output/docs/`

**参与的 Validation**：无

**v2.5.1新增要求**：
- **必须生成.tex格式的summary sheet**
- **参考latex_template/中的摘要格式**
- **摘要必须与主论文一致**

---

### 2.13 Editor Agent ⭐ v2.5.1重大更新

**职责**：
- 润色文档
- **处理LaTeX文件并重新编译**（v2.5.1强制要求）

**输入**：
- **`paper/paper_{i}.tex`**（v2.5.1更新：读取.tex）
- **`paper/summary/summary_sheet_{i}.tex`**（v2.5.1更新：读取.tex）

**输出**：
- **`paper/paper_{i+1}.tex`**（润色后的LaTeX，**强制**）
- **`paper/paper_{i+1}.pdf`**（重新编译的PDF，**强制**）
- **`paper/compile_{i+1}.log`**（编译日志，**强制**）
- **`paper/summary/summary_sheet_{i+1}.tex`**（润色后的摘要，**强制**）
- **`paper/summary/summary_sheet_{i+1}.pdf`**（编译的摘要PDF，**强制**）

**写入目录**：
- `output/paper/`
- `output/docs/`

**参与的 Validation**：无

**v2.5.1强制要求**：

1. **必须处理LaTeX文件**：
   - 输入是.tex，不是.md
   - 直接修改LaTeX源码
   - ❌ 禁止将.tex转.md处理

2. **必须重新编译**：
   - 修改后必须重新生成PDF
   - 验证编译通过
   - 验证PDF可读

3. **禁止行为**：
   - ❌ 改变论文核心内容
   - ❌ 删除章节或重要信息
   - ❌ 修改数据和结论
   - ❌ 跳过编译验证

**Report必须包含**：
- 润色类型（语法/表达/格式）
- 修改数量统计
- 编译验证状态

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

**v2.5.1新增检查**：
- **验证PDF文件存在且可读**
- **验证论文页数符合要求**
- **验证摘要PDF存在**

---

## 三、Agent 通信格式

### 3.1 完成任务后

```
Director，任务完成。
状态：SUCCESS
产出：{file_paths}
报告：docs/report/{agent}_{i}.md
```

**Writer特殊格式**（v2.5.1）：
```
Director，任务完成。
状态：SUCCESS
产出：
- output/paper/paper_1.tex
- output/paper/paper_1.pdf
- output/paper/compile_1.log
编译状态：SUCCESS
PDF页数：23页
报告：docs/report/writer_1.md
```

**Editor特殊格式**（v2.5.1）：
```
Director，任务完成。
状态：SUCCESS
产出：
- output/paper/paper_2.tex
- output/paper/paper_2.pdf
- output/paper/compile_2.log
- output/paper/summary/summary_sheet_2.pdf
编译验证：通过
润色修改：15处语法，8处表达
报告：docs/report/editor_1.md
```

### 3.2 需要咨询时

```
Director，我需要咨询 @{agent}，文件：docs/consultation/{i}_{from}_{to}.md
```

**Writer特殊咨询**（v2.5.1）：
```
Director，LaTeX编译失败，需要咨询 @feasibility_checker。

错误信息：Package xxx not found
文件：docs/consultation/1_writer_feasibility_checker.md

请协助解决编译环境问题。
```

### 3.3 遇到问题时

```
Director，{问题描述}。
```

**Writer问题示例**（v2.5.1）：
```
Director，xelatex编译失败，ERROR: Missing font。

已尝试：
1. 使用默认字体
2. 修改字体配置

需要通过Consultation请求feasibility_checker安装缺失字体。

当前产出：
- paper_1.tex（已完成）
- paper_1.pdf（编译失败）

建议：暂停当前Phase，等待环境修复。
```

---

## 四、通用规则

### 4.1 所有 Agent 必须遵守

- ✅ 只写入允许的目录
- ✅ 所有输出文件带版本号
- ✅ 完成后汇报给 Director
- ✅ 遇到问题立即上报
- ❌ 禁止写入 `output/` 以外的文件

### 4.2 LaTeX相关Agent必须遵守 (v2.5.1新增)

**Writer必须**：
- ✅ 生成.tex和.pdf文件
- ✅ 使用latex_template/模板
- ✅ 编译通过才能提交
- ✅ 记录编译日志
- ❌ 禁止只输出.md
- ❌ 禁止跳过编译

**Editor必须**：
- ✅ 处理.tex文件
- ✅ 重新编译验证
- ✅ 生成新的PDF
- ❌ 禁止只处理.md

**Summarizer必须**：
- ✅ 生成summary_sheet.tex
- ✅ 参考LaTeX模板
- ❌ 禁止只生成Markdown

### 4.3 作为验证者时

- ✅ 独立判断，禁止 Consultation
- ✅ 以同样标准验证返工版本
- ❌ 禁止降低验证标准

**v2.5.1 LaTeX验证新增**：
- ✅ 验证.tex和.pdf文件存在
- ✅ 验证PDF可读且页数足够
- ✅ 验证编译日志无ERROR
- ❌ 拒绝无PDF的论文

---

## 五、LaTeX工作流 (v2.5.1新增)

### 5.1 Phase 7: Paper Writing

```
Writer开始
  ↓
复制latex_template/到output/paper/
  ↓
在模板基础上撰写内容
  ↓
生成paper_{i}.tex
  ↓
尝试编译: xelatex paper_{i}.tex
  ↓
编译成功？
  ├─ 是 → 验证PDF质量
  │       ├─ 页数≥20？
  │       └─ PDF可读？
  │         ↓
  │       生成compile_{i}.log
  │         ↓
  │       提交Report（包含PDF信息）
  │
  └─ 否 → 记录错误到compile_{i}.log
           ↓
         通过Consultation请求feasibility_checker
           ↓
         feasibility_checker修复环境
           ↓
         Writer重新编译
```

### 5.2 Phase 8: Summary

```
Summarizer开始
  ↓
读取paper_{i}.tex
  ↓
提取关键信息
  ↓
生成summary_sheet_{i}.tex
  ↓
生成summary_1page.md
  ↓
提交Report
```

### 5.3 Phase 9: Polish

```
Editor开始
  ↓
读取paper_{i}.tex和summary_sheet_{i}.tex
  ↓
润色语言和格式
  ↓
生成paper_{i+1}.tex
  ↓
生成summary_sheet_{i+1}.tex
  ↓
编译验证:
  - xelatex paper_{i+1}.tex
  - xelatex summary_sheet_{i+1}.tex
  ↓
验证PDF质量
  ↓
生成compile_{i+1}.log
  ↓
提交Report（包含编译验证信息）
```

---

**版本**: v2.5.1
**最后更新**: 2026-01-11
**主要变更**:
- 修复Writer契约：强制输出.tex和.pdf
- 修复Editor契约：处理.tex并重新编译
- 修复Summarizer契约：生成summary_sheet.tex
- 新增LaTeX编译要求
- 新增编译错误处理流程
