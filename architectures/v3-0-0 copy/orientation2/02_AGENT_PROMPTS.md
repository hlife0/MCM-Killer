# Part II: Agent Prompt Enhancement (Revised)

> **元认知指令，不是角色切换**
> **Core Principle**: 单一 Agent，多重思维模式
> **Philosophy**: 引导认知，不控制执行
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
Python Runtime 切换角色：

if task.type == 'modeling':
    activate_agent('@modeler')
elif task.type == 'coding':
    activate_agent('@code_translator')
...

@modeler 执行 → @code_translator 执行 → @validator 执行
```

**问题**：
- 角色割裂，缺乏连贯性
- Python 控制，不自然
- 重复传递上下文

### 新范式（正确）

```
单一 Claude Code，在不同阶段切换思维模式：

科学家模式 → 工程师模式 → 批评家模式 → 作家模式

Claude Code 自主切换，无需 Python 控制
```

**优势**：
- 上下文连贯
- 自然语言引导
- Claude Code 自主决策

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | Claude Code 替代方案 |
|------|--------|------|---------------------|
| **Python 角色切换** | `activate_agent('@modeler')` | 不自然 | 直接告诉 Claude："用科学家思维思考" |
| **角色提示词文件** | `.claude/agents/*.md` (14个) | 过度细分 | 元认知指令（4个模式） |
| **角色间通信** | JSON message passing | 冗余 | 单一上下文，无需传递 |
| **工作流编排** | Python DAG | 不必要 | 自然语言指令链 |

---

## 第二部分：元认知模式（Metacognition Modes）

### 模式定义

```markdown
# 系统指令（Session 启动时注入）

Claude Code，你将身兼数职，在任务的不同阶段切换思维模式：

## 🔬 科学家模式 (Scientist Mode)

**启用时机**：接到问题、选择模型、设计实验时

**思维重点**：
- 优先理论依据，不是实用主义
- 提出假设（Hypothesis），不是直接动手
- 查阅 docs/math_models_cheatsheet.md
- 质疑：这个方法真的适合吗？有更好的吗？

**输出**：
- 研究计划（execution_plan.md）
- 模型选择理由（Why this method?）
- 实验设计（How to validate?）

**典型指令**：
```
"以科学家思维分析这个问题：
1. 提出核心假设
2. 设计最小可行实验（MVP）验证假设
3. 阅读 docs/math_models_cheatsheet.md 选择合适方法
4. 说明为什么选择这个方法（理论依据）
"
```

---

## 🔧 工程师模式 (Engineer Mode)

**启用时机**：编写代码、处理数据时

**思维重点**：
- 代码健壮性 > 简洁性
- 参考 docs/anti_patterns.md 避免常见错误
- **工具使用规范**：
  - 写代码前：先写单元测试（pytest 或 assert）
  - 处理数据：先用 `pd.to_datetime(..., errors='coerce')`
  - 运行模型：先用小数据集验证逻辑

**输出**：
- 可运行的代码
- 测试结果（validation_report.json）

**典型指令**：
```
"切换到工程师模式：
1. 编写代码实现科学家设计的模型
2. **关键**：在运行前先写单元测试
3. 参考 docs/coding_best_practices.md
4. 如果遇到错误，查看 global_memory/lessons_learned.md
"
```

---

## 👮 批评家模式 (Critic Mode)

**启用时机**：检查结果、验证模型时

**思维重点**：
- 质疑一切，包括自己的工作
- 对比 O-Prize 标准（docs/mcm_o_prize_style_guide.md）
- 查阅 docs/anti_patterns.md 确认没有踩坑
- 找出：哪里不够好？哪里可能有问题？

**输出**：
- 改进建议（critique_report.md）
- 潜在问题清单（issues.md）

**典型指令**：
```
"切换到批评家模式：
1. 检查模型是否满足所有 O-Prize 标准
2. 验证是否踩了反模式中的坑
3. 质疑：这个结果真的可信吗？
4. 如果不满足，提出具体改进方案
"
```

---

## 📝 作家模式 (Writer Mode)

**启用时机**：撰写论文时

**思维重点**：
- 参考 docs/mcm_o_prize_style_guide.md
- 使用观察-洞察模式（Observation-Implication）
- IMRaD 结构
- 学习 reference/best_paper_example/ 的完整风格

**输出**：
- 学术论文章节（LaTeX）
- 图表说明（Explanatory captions）

**典型指令**：
```
"切换到作家模式：
1. 阅读参考论文 (reference/best_paper_example/)
2. 使用 IMRaD 结构撰写 Results 章节
3. 每个图表使用观察-洞察模式写说明
4. 包含所有必需的统计检验结果
"
```

---

## 模式切换协议

### 自动切换流程

```markdown
# 模式切换指令

**Claude Code，当你完成一个阶段的任务后，自动切换到下一个模式**：

## 标准流程

科学家 → 工程师 → 批评家 → (如果通过) → 作家
                              ↓
                         (如果不通过)
                              ↓
                        科学家（重新设计）

## 根据需要跳转

- 如果工程师发现数据问题 → 回到科学家重新设计特征
- 如果批评家发现代码 bug → 回到工程师修复
- 如果批评家发现写作问题 → 跳到作家改进
```

### 人工干预切换

```markdown
# 人工模式切换指令

**User**: "停下。你的模型过拟合了。
参考 docs/math_models_cheatsheet.md 中的正则化方法，
使用 L1/L2 penalty 重新训练。"

**Claude Code 自动**:
→ 读取文档，应用正则化
→ 重新训练
→ 验证改进
```

---

## 第三部分：工具使用规范

### 工具调用协议

**不写 Python 包装器**，直接自然语言指令：

```markdown
# 工具使用规范

## 训练模型时

**指令**：
"使用 tools/arena.py 训练多个模型并进行对比：
- 模型：ZINB, Poisson, ARIMA
- 数据：output/implementation/data/features.csv
- 指标：RMSE, MAE, R2
- 交叉验证：5-fold

**关键**：如果训练超过 30 分钟，暂停向我汇报。"

## 生成图表时

**指令**：
"生成学术风格的散点图：
- 参考 docs/mcm_o_prize_style_guide.md 中的图表标准
- 使用参考论文的配色方案
- 包含误差棒
- 保存为 artifacts/figures/YYYYMMDD_figure_name.png
- 文件名带时间戳防止覆盖

**标题要求**：使用观察-洞察模式
- 描述：图表显示什么
- 洞察：这意味着什么
- 统计：置信区间、显著性"

## 验证模型时

**指令**：
"运行完整的统计检验：
- 使用 tools/validate_statistics.py
- 必需检验：Shapiro-Wilk, Durbin-Watson, Breusch-Pagan
- 参考 docs/mcm_o_prize_style_guide.md 的报告格式
- 输出：output/validation/statistical_tests.json

**如果检验失败**：
- 参考 docs/optimization_strategies.md
- 尝试修正（数据转换、正则化等）
- 最多重试 3 次"
```

---

## 第四部分：任务指令模板

### 完整任务指令（从开始到结束）

```markdown
# 任务指令：2025_C 奥运奖牌预测

## Phase 1: 科学家模式（问题分析）

**Claude Code，以科学家思维分析这个问题**：

1. **阅读问题陈述**：
   - 读取 2025_Problem_C.pdf
   - 提取关键要求

2. **提出假设**：
   - 核心问题是什么？
   - 数据有什么特征？（时间序列？计数数据？）
   - 可能的模型有哪些？

3. **查阅知识**：
   - Read: docs/math_models_cheatsheet.md
   - 选择 2-3 个候选模型
   - 说明选择理由

4. **设计实验**：
   - 如何验证假设？
   - 成功标准是什么？
   - 输出到：execution_plan.md

---

## Phase 2: 工程师模式（数据处理与建模）

**现在切换到工程师模式**：

1. **读取计划**：
   - Read: execution_plan.md

2. **处理数据**：
   - 加载数据（注意 BOM 处理）
   - 特征工程
   - **关键**：处理前检查 global_memory/lessons_learned.md
   - 参考 docs/anti_patterns.md 避免错误

3. **编写代码**：
   - 实现模型（科学家选择的）
   - **必须**：先写单元测试
   - 运行测试，确保逻辑正确

4. **训练模型**：
   - 使用 tools/arena.py 训练多个模型
   - 对比性能
   - 选择最优模型

5. **输出**：
   - 模型对象：artifacts/models/DATE_model.pkl
   - 预测结果：artifacts/results/DATE_predictions.csv

---

## Phase 3: 批评家模式（验证与批评）

**现在切换到批评家模式**：

1. **验证统计**：
   - 运行 tools/validate_statistics.py
   - 检查是否满足所有 O-Prize 标准
   - Read: docs/mcm_o_prize_style_guide.md

2. **检查反模式**：
   - Read: docs/anti_patterns.md
   - 确认没有踩坑
   - 列出潜在问题

3. **灵敏度分析**：
   - 运行 tools/validate_sensitivity.py
   - 生成龙卷风图
   - 检查模型鲁棒性

4. **输出**：
   - 验证报告：artifacts/validation/DATE_validation.json
   - 改进建议：critique_report.md

**如果验证失败**：
→ 回到科学家模式，重新设计模型
→ 或回到工程师模式，修正代码

**如果验证通过**：
→ 进入作家模式

---

## Phase 4: 作家模式（撰写论文）

**现在切换到作家模式**：

1. **学习风格**：
   - Read: reference/best_paper_example/2023_C_OPrize.pdf
   - Read: docs/mcm_o_prize_style_guide.md
   - 提取：结构、配色、风格

2. **撰写章节**（按 IMRaD）：
   - Introduction：问题背景、动机
   - Methods：模型设计、公式推导
   - Results：图表、统计结果（使用观察-洞察模式）
   - Discussion：结果解释、局限性、未来工作

3. **图表说明**：
   - 每个图表：描述 + 洞察 + 统计
   - 示例：
     ```
     Figure 1: Historical medal counts (1896-2024).
     [Observation] Exponential growth evident post-1980 (R²=0.89).
     [Implication] This suggests compounding advantages in athletic infrastructure.
     [Statistics] Shaded region represents 95% CI from ZINB model.
     ```

4. **编译 LaTeX**：
   - 使用 tools/latex_builder.py
   - 生成 PDF

5. **输出**：
   - LaTeX 源码：artifacts/paper/paper.tex
   - PDF：artifacts/paper/paper.pdf

---

## Phase 5: 复盘（Session 结束）

**任务完成，请执行复盘**：

1. **总结错误**：
   - 本次任务中出现了哪些 Critical Errors？
   - 根因是什么？

2. **提炼经验**：
   - 格式：错误 → 根因 → 解决 → 预防
   - 具体到代码级别

3. **追加记忆**：
   - Append: global_memory/lessons_learned.md
   - 格式参见现有条目
```

---

## 第五部分：工具脚本（极简）

### 必需工具（6个）

```
tools/
├── arena.py                  # 模型对比（多模型训练）
├── validate_statistics.py    # 统计检验套件
├── validate_sensitivity.py   # 灵敏度分析（龙卷风图）
├── journal_helper.py         # 研究日记辅助
├── latex_builder.py          # LaTeX 编译 + 错误修复
└── chart_generator.py        # 学术风格图表
```

### 工具调用方式

```bash
# ❌ 错误：Python 包装器
subprocess.run(["python", "tools/arena.py", "--model", "ZINB"])

# ✅ 正确：自然语言指令
"使用 tools/arena.py 训练 ZINB 模型，输入 features.csv，输出 results.json"

# Claude Code 自动转换为：
cd workspace/2025_C
python tools/arena.py --model ZINB --input features.csv --output results.json
```

---

## 第六部分：与原计划的对比

### Agent 对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **角色数量** | 14 个独立 Agent | 4 个思维模式 |
| **切换方式** | Python 代码控制 | 自然语言指令 |
| **上下文** | 分散在各自 Agent | 单一连续上下文 |
| **通信** | JSON message passing | 无需通信（同一上下文） |
| **提示词** | 14 个 .md 文件 | 1 个元认知指令 |
| **工作流** | Python DAG 编排 | 自然语言指令链 |

### 核心改变

1. **从"角色"到"模式"**
   - 不切换 Agent
   - 切换思维模式

2. **从"控制"到"引导"**
   - 不控制 Claude Code 执行细节
   - 提供思维框架和知识

3. **从"自动"到"半自主"**
   - Claude Code 自主切换模式
   - 人工干预关键决策

---

## 快速开始

### 初始化指令

```markdown
# Session 启动指令

Claude Code，请：

1. **阅读知识库**：
   - Read: docs/math_models_cheatsheet.md
   - Read: docs/anti_patterns.md
   - Read: docs/mcm_o_prize_style_guide.md

2. **理解元认知模式**：
   - 科学家模式：问题分析、假设驱动
   - 工程师模式：代码实现、健壮性
   - 批评家模式：质量把关、找茬
   - 作家模式：学术表达、IMRaD

3. **读取历史经验**：
   - Read: global_memory/lessons_learned.md
   - 严格避免重复历史错误

4. **准备工具**：
   - 确认 tools/ 目录下有 6 个工具脚本
   - 理解每个工具的用途

确认后，开始执行任务。
```

---

**版本**: Revised
**核心理念**: 元认知引导，不控制执行
**关键**: 4 个思维模式，自然语言切换，单一上下文

---

**END OF 02_AGENT_PROMPTS_REVISED.md**
