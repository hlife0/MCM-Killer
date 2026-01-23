# Part III: Task Decomposition Protocol (Revised)

> **Prompt 链，不是 JSON 任务定义**
> **Core Principle**: 元指令驱动，不是编排系统
> **Philosophy**: 引导流程，不控制细节
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
Python 编排系统：

tasks.json:
{
  "task_id": "T4_1_model_training",
  "dependencies": ["T3_2"],
  "agent": "@code_translator",
  "instruction": {...}
}

Python 读取 JSON → 检查依赖 → 分配 Agent → 执行
```

**问题**：
- 过度工程化（Over-engineered）
- JSON 维护成本高
- 缺乏灵活性

### 新范式（正确）

```
自然语言元指令：

User: "开始 Phase 1：科学家模式，分析问题并设计模型"

Claude Code:
→ 切换到科学家思维
→ 读取 docs/math_models_cheatsheet.md
→ 提出假设
→ 设计实验
→ 输出 execution_plan.md

User: "批准。进入 Phase 2：工程师模式，实现模型"

Claude Code:
→ 切换到工程师思维
→ 编写代码
→ 运行测试
→ 输出 artifacts/
```

**优势**：
- 简单直接
- 易于调整
- Claude Code 自主决策

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | 替代方案 |
|------|--------|------|----------|
| **JSON 任务定义** | tasks.json schema | 过度复杂 | 自然语言指令 |
| **Python 依赖检查** | DAG topology | Claude Code 足够聪明 | 直接告诉 Claude 依赖 |
| **Agent 分配器** | assign_agent(task) | 不需要 | 元认知模式自动切换 |
| **任务状态跟踪** | task_status.json | 冗余 | Claude Code 报告进度 |
| **错误重试循环** | while retry: | Claude 自动修复 | 自然语言告诉 Claude 重试 |

---

## 第二部分：Prompt 链设计

### 标准 Prompt 链模板

```markdown
# 任务分解元指令

**Claude Code，当你接到任何问题时，必须按以下流程思考**：

## 第一步：科学家思维 - 假设驱动

**指令**：
1. 阅读 docs/math_models_cheatsheet.md
2. 提出核心假设（例如："数据具有周期性"）
3. 设计最小可行实验（MVP）验证假设
4. 输出到：execution_plan.md

**输出格式**：
```markdown
# 执行计划

## 核心假设
[你的假设]

## 验证方法
- 实验 1：[设计]
- 实验 2：[设计]

## 预期结果
- 如果假设正确：[观察]
- 如果假设错误：[替代方案]
```

---

## 第二步：工程师思维 - 健壮执行

**指令**：
1. 根据 execution_plan.md 编写代码
2. **工具使用规范**：
   - 写代码前：写单元测试（pytest 或 assert）
   - 处理数据：使用 BOM-safe 加载
   - 运行模型：先用小数据集验证逻辑
3. 运行测试，确保通过
4. 输出到：artifacts/

**关键检查点**：
- [ ] 代码有单元测试吗？
- [ ] 参考 docs/anti_patterns.md 避免错误了吗？
- [ ] 参考 global_memory/lessons_learned.md 了吗？

---

## 第三步：批评家思维 - 质量把关

**指令**：
1. 检查 docs/anti_patterns.md，确认没有踩坑
2. 验证结果：
   - R² > 0.6？
   - 统计检验通过？
   - 没有明显过拟合？
3. 如果不满足：阅读 docs/optimization_strategies.md
4. 自动优化（最多 3 次重试）

**验证清单**：
- [ ] RMSE < 阈值？
- [ ] R² > 0.6？
- [ ] Shapiro-Wilk p > 0.05？
- [ ] Durbin-Watson 1.5 < DW < 2.5？
- [ ] 没有踩反模式？

**如果验证失败**：
→ 回到第一步，重新设计模型

---

## 第四步：作家思维 - 学术表达

**指令**：
1. 参考 docs/mcm_o_prize_style_guide.md
2. 使用观察-洞察模式写图表说明
3. 确保包含灵敏度分析
4. 输出 LaTeX 章节

**图表标题模板**：
```
Figure X: [标题]
[Observation] 图表显示的模式...
[Implication] 这意味着...
[Statistics] 统计显著性...
```

**关键**：以上流程是**自动循环**的，不需要我每步指令。
```

---

## 第三部分：典型任务 Prompt 链

### 任务 1：数据分析与特征工程

```markdown
# 任务：数据分析与特征工程

Claude Code，请执行以下流程：

## Phase 1: 科学家模式

**目标**：理解数据，设计特征

**步骤**：
1. 加载数据：data/2025_Problem_C/summerOly_medal_counts.csv
2. 分析数据特征：
   - 样本量？
   - 缺失值比例？
   - 数据类型？
   - 异常值？
3. 提出假设：
   - 哪些特征可能重要？
   - 数据有什么模式？
4. 设计特征工程方案：
   - 需要哪些特征？
   - 如何处理缺失值？
   - 如何归一化？

**输出**：data_analysis_report.md

---

## Phase 2: 工程师模式

**目标**：实现特征工程

**步骤**：
1. 编写代码：
   - 加载数据（BOM-safe）
   - 处理缺失值
   - 创建特征
   - 归一化
2. **关键**：先写单元测试
   ```python
   def test_feature_engineering():
       df = load_data()
       assert df['host_country'].isna().sum() == 0
       assert df['medal_count'].min() >= 0
   ```
3. 运行测试，确保通过
4. 保存特征：artifacts/data/features.csv

**参考**：
- docs/anti_patterns.md（数据处理错误）
- global_memory/lessons_learned.md（历史错误）

---

## Phase 3: 批评家模式

**目标**：验证数据质量

**检查**：
- [ ] 缺失值 < 5%？
- [ ] 没有异常值？
- [ ] 特征相关性合理？
- [ ] 数据分布合理？

**输出**：data_quality_report.json

**如果不通过**：
→ 回到 Phase 2，修正特征工程
```

### 任务 2：模型训练与对比

```markdown
# 任务：模型训练与对比

Claude Code，请执行以下流程：

## Phase 1: 科学家模式

**目标**：选择合适的模型

**步骤**：
1. 阅读 docs/math_models_cheatsheet.md
2. 分析问题类型：
   - 预测问题？分类问题？
   - 数据特征？
3. 选择 2-3 个候选模型：
   - 模型 A：为什么适合？
   - 模型 B：为什么适合？
   - 模型 C：为什么适合？
4. 设计对比实验：
   - 评估指标：RMSE, MAE, R²
   - 交叉验证：5-fold

**输出**：model_selection_plan.md

---

## Phase 2: 工程师模式

**目标**：训练模型

**步骤**：
1. 使用 tools/arena.py 训练多个模型：
   ```bash
   python tools/arena.py \
     --input artifacts/data/features.csv \
     --models ZINB,Poisson,ARIMA \
     --output artifacts/results/arena_results.json \
     --cv-folds 5
   ```
2. 查看结果：
   - 哪个模型最好？
   - 指标是否满足要求？

**输出**：
- artifacts/models/DATE_model.pkl（最优模型）
- artifacts/results/DATE_predictions.csv
- artifacts/results/arena_results.json

---

## Phase 3: 批评家模式

**目标**：验证模型

**检查**：
1. 运行统计检验：
   ```bash
   python tools/validate_statistics.py \
     --predictions artifacts/results/predictions.csv \
     --output artifacts/validation/statistical_tests.json
   ```
2. 检查结果：
   - [ ] Shapiro-Wilk p > 0.05？
   - [ ] Durbin-Watson 1.5 < DW < 2.5？
   - [ ] Breusch-Pagan p > 0.05？
   - [ ] RMSE < 阈值？
   - [ ] R² > 0.6？

**输出**：validation_report.md

**如果验证失败**：
→ 参考 docs/optimization_strategies.md
→ 回到 Phase 1，选择其他模型
→ 最多重试 3 次

---

## Phase 4: 作家模式

**目标**：撰写结果章节

**步骤**：
1. 参考 docs/mcm_o_prize_style_guide.md
2. 生成图表（使用 tools/chart_generator.py）
3. 撰写 Results 章节：
   - 模型对比表
   - 图表说明（观察-洞察模式）
   - 统计检验结果

**输出**：artifacts/paper/results.tex
```

### 任务 3：灵敏度分析

```markdown
# 任务：灵敏度分析

Claude Code，请执行以下流程：

## Phase 1: 科学家模式

**目标**：设计灵敏度分析

**步骤**：
1. 识别关键参数：
   - 哪些参数最重要？
   - 变化范围是多少？
2. 设计扰动方案：
   - ±5%, ±10%, ±20%
3. 预期影响：
   - 哪些参数最敏感？
   - 合理的灵敏度范围？

**输出**：sensitivity_plan.md

---

## Phase 2: 工程师模式

**目标**：执行灵敏度分析

**步骤**：
1. 使用 tools/validate_sensitivity.py：
   ```bash
   python tools/validate_sensitivity.py \
     --model artifacts/models/zinb_model.pkl \
     --data artifacts/data/features.csv \
     --output artifacts/validation/sensitivity_report.json \
     --perturbations 5,10,20
   ```
2. 生成龙卷风图

**输出**：
- artifacts/figures/DATE_tornado.png
- artifacts/validation/sensitivity_report.json

---

## Phase 3: 批评家模式

**目标**：验证鲁棒性

**检查**：
- [ ] 龙卷风图生成？
- [ ] 参数变化 < 10% 输出变化？
- [ ] 没有单一参数主导？
- [ ] 符合 O-Prize 标准？

**输出**：robustness_report.md

**如果灵敏度过高**：
→ 回到科学家模式，重新设计模型
→ 添加正则化或简化模型
```

---

## 第四部分：人工干预指令

### 何时需要人工干预

```markdown
# 人工干预指令

**Claude Code，在以下情况下暂停向我汇报**：

1. **模型选择有疑问**：
   - 多个模型性能接近
   - 需要权衡复杂度与性能

2. **验证失败**：
   - 统计检验不通过
   - 尝试了 3 次仍失败

3. **数据异常**：
   - 缺失值 > 20%
   - 发现异常模式

4. **超时**：
   - 模型训练超过 30 分钟
   - 代码执行超过 10 分钟

**汇报格式**：
```markdown
## 问题报告

**当前阶段**：[Phase X: 模式名]

**遇到的问题**：
- [描述]

**已尝试的方案**：
1. [方案 1]
2. [方案 2]

**需要决策**：
- 选项 A：[描述]
- 选项 B：[描述]

**建议**：[你的建议]
```

### 人工干预示例

```markdown
# 示例：模型选择冲突

**Claude Code 报告**：

## 问题报告

**当前阶段**：Phase 2: 工程师模式（模型训练）

**遇到的问题**：
- ZINB: RMSE=4.2, R²=0.78, 但收敛警告
- Poisson: RMSE=4.5, R²=0.75, 稳定收敛

**已尝试的方案**：
1. 增加 ZINB 迭代次数（仍收敛警告）
2. 调整 ZINB 初始值（仍收敛警告）

**需要决策**：
- 选项 A：使用 ZINB（性能更好，但有警告）
- 选项 B：使用 Poisson（稍差，但稳定）

**建议**：选项 B - 稳定性更重要，O-Prize 重视模型可靠性

---

**User 指令**：

"批准选项 B。使用 Poisson 模型，继续执行。"

**Claude Code 继续**：
→ 切换到工程师模式
→ 使用 Poisson 模型
→ 继续验证流程
```

---

## 第五部分：与原计划的对比

### 任务分解对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **任务定义** | JSON schema | Prompt 模板 |
| **依赖管理** | Python DAG | 自然语言告诉 Claude |
| **Agent 分配** | JSON field | 元认知模式自动切换 |
| **状态跟踪** | task_status.json | Claude Code 报告 |
| **错误处理** | while retry | 自然语言告诉 Claude 重试 |
| **输出格式** | JSON | Markdown + CSV |

### 核心改变

1. **从"编排"到"引导"**
   - 不用 Python 编排任务
   - 用 Prompt 引导流程

2. **从"状态机"到"思维流"**
   - 不跟踪任务状态
   - 切换思维模式

3. **从"自动化"到"半自主"**
   - 不追求完全自动化
   - 保留人工干预点

---

## 第六部分：完整任务指令示例

### 端到端任务：从问题到论文

```markdown
# 完整任务：2025_C 奥运奖牌预测

## 初始化

Claude Code，请：

1. **读取知识库**：
   - Read: docs/math_models_cheatsheet.md
   - Read: docs/anti_patterns.md
   - Read: docs/mcm_o_prize_style_guide.md
   - Read: global_memory/lessons_learned.md

2. **确认理解**：
   - 你理解了哪些反模式？
   - 你记住了哪些历史错误？

确认后开始。

---

## Phase 1: 科学家模式（问题分析）

**指令**：
"以科学家思维分析 2025_C 问题：
1. 读取 2025_Problem_C.pdf
2. 提出核心假设
3. 设计最小可行实验
4. 参考 docs/math_models_cheatsheet.md 选择 2-3 个候选模型
5. 输出 execution_plan.md"

---

## Phase 2: 工程师模式（数据处理）

**指令**：
"切换到工程师模式：
1. 加载 summerOly_medal_counts.csv（BOM-safe）
2. 处理缺失值
3. 创建特征（host_country, momentum, etc.）
4. **关键**：先写单元测试
5. 参考 global_memory/lessons_learned.md 避免历史错误
6. 输出 features.csv"

---

## Phase 3: 工程师模式（模型训练）

**指令**：
"继续工程师模式：
1. 使用 tools/arena.py 训练模型：
   - ZINB, Poisson, ARIMA
   - 5-fold cross-validation
2. 选择最优模型（基于 RMSE, R²）
3. 如果训练超过 30 分钟，暂停向我汇报
4. 输出：model.pkl, predictions.csv, arena_results.json"

---

## Phase 4: 批评家模式（验证）

**指令**：
"切换到批评家模式：
1. 运行 tools/validate_statistics.py
2. 检查所有必需检验：
   - Shapiro-Wilk (p > 0.05)
   - Durbin-Watson (1.5 < DW < 2.5)
   - Breusch-Pagan (p > 0.05)
3. 检查 docs/anti_patterns.md 确认没踩坑
4. 如果不通过，参考 docs/optimization_strategies.md
5. 最多重试 3 次
6. 输出 validation_report.json"

---

## Phase 5: 工程师模式（灵敏度分析）

**指令**：
"切换回工程师模式：
1. 使用 tools/validate_sensitivity.py
2. 扰动参数：±5%, ±10%, ±20%
3. 生成龙卷风图
4. 检查模型鲁棒性
5. 输出：tornado.png, sensitivity_report.json"

---

## Phase 6: 作家模式（撰写论文）

**指令**：
"切换到作家模式：
1. 参考 reference/best_paper_example/2023_C_OPrize.pdf
2. 参考 docs/mcm_o_prize_style_guide.md
3. 撰写 IMRaD 结构：
   - Introduction
   - Methods
   - Results（使用观察-洞察模式）
   - Discussion
4. 每个图表包含：描述 + 洞察 + 统计
5. 使用 tools/latex_builder.py 编译
6. 输出：paper.pdf"

---

## Phase 7: 复盘

**指令**：
"任务完成，请复盘：
1. 总结本次 Critical Errors
2. 提炼经验教训
3. 追加到 global_memory/lessons_learned.md
4. 格式：错误 → 根因 → 解决 → 预防"
```

---

## 快速开始

### 使用 Prompt 链

```markdown
# 启动指令

Claude Code，请：

1. **读取元指令**：
   - 阅读本文件（03_TASK_DECOMPOSITION_REVISED.md）
   - 理解 4 个模式的切换逻辑

2. **初始化上下文**：
   - Read: docs/math_models_cheatsheet.md
   - Read: docs/anti_patterns.md
   - Read: global_memory/lessons_learned.md

3. **开始任务**：
   - "以科学家思维开始分析这个问题：[你的问题]"

4. **自动循环**：
   - Claude Code 自动切换模式
   - 遇到问题暂停汇报
   - 人工决策后继续
```

---

**版本**: Revised
**核心理念**: Prompt 链驱动，不编排系统
**关键**: 元认知模式自动切换，自然语言指令，人工干预点

---

**END OF 03_TASK_DECOMPOSITION_REVISED.md**
