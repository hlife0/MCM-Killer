# Part VII: Implementation Roadmap (Revised)

> **指令集准备，不是脚本开发**
> **Core Principle**: 准备知识和指令，不是编写工具
> **Philosophy**: 10 分钟设置，立即使用
> **Version**: 3.0-Revised

---

## 核心战略转变

### 旧范式（错误）

```
10 天开发计划：

Day 1-2: 创建目录结构
Day 3-4: 提取 HMML（98 个方法）
Day 5-6: 创建工具脚本（6 个 Python 脚本）
Day 7: 集成组件
Day 8-9: 测试
Day 10: 文档

总工作量：~80 小时
```

**问题**：
- 太重了，过度工程化
- 大部分时间在写代码
- 偏离了"去工程化"原则

### 新范式（正确）

```
10 分钟设置计划：

Step 1: 创建目录（2 分钟）
Step 2: 准备知识库（5 分钟）
Step 3: 准备参考论文（2 分钟）
Step 4: 启动 Claude Code（1 分钟）

总工作量：~10 分钟
```

**优势**：
- 快速启动
- 立即可用
- 符合"AI Native"原则

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 任务 | 原计划 | 原因 | 替代方案 |
|------|--------|------|----------|
| **HMML 提取脚本** | extract_hmml.py | 不需要 | 手动简化为 1 个 MD 文件 |
| **Prompt 提取脚本** | extract_prompts.py | 不需要 | 手动总结为 4 个 MD 文件 |
| **风格指南生成** | generate_style_guide.py | 不需要 | 手动选择 1 篇论文 |
| **工具脚本开发** | 6 个 Python 脚本 | 过度工程 | 使用 Claude Code 原生能力 |
| **集成测试** | 端到端测试 | 不必要 | Session 内验证 |
| **MMBench 评估** | 111 问题测试 | 太重了 | Session 内验证即可 |

---

## 第二部分：10 分钟设置计划

### Step 1: 创建目录（2 分钟）

```bash
# 1. 进入工作目录
cd D:\migration\MCM-Killer\workspace

# 2. 创建目录结构
mkdir -p docs global_memory reference/best_paper_example
mkdir -p artifacts/{code,figures,models,data,results,validation,paper}
mkdir -p data/2025_Problem_C

# 3. 初始化文件
echo "# Current Status\n\n" > current_status.md
echo "# Lessons Learned\n\n" > global_memory/lessons_learned.md

# 4. 验证
ls -R
```

**输出**：
```
workspace/
├── docs/
├── global_memory/
│   └── lessons_learned.md
├── reference/
│   └── best_paper_example/
├── artifacts/
│   ├── code/
│   ├── figures/
│   ├── models/
│   ├── data/
│   ├── results/
│   ├── validation/
│   └── paper/
├── data/
│   └── 2025_Problem_C/
└── current_status.md
```

---

### Step 2: 准备知识库（5 分钟）

#### 2.1 创建 math_models_cheatsheet.md（3 分钟）

**来源**：从 MM-Agent HMML 简化

**内容**：
```markdown
# 数学模型速查表

## 使用方法
Claude Code，当你接到问题时：
1. 阅读本文档
2. 根据问题类型匹配模型
3. 选择 2-3 个候选模型
4. 对比优缺点

---

## 预测模型

### ZINB (Zero-Inflated Negative Binomial)
**适用场景**：
- 计数数据 + 过多零值 (zero inflation > 30%)
- 样本量：n > 50
- O-Prize 先例：2023 Problem C

**验证要求**：
- VIF < 5 (no multicollinearity)
- Overdispersion test (p < 0.05)

**常见错误**：
❌ 对小样本 (n<30) 使用 ZINB → 过拟合

---

### ARIMA
**适用场景**：
- 时间序列，趋势性
- 样本量：n > 40

[... 其他模型 ...]
```

**操作**：
- 复制从 MM-Agent HMML 提取的核心内容
- 简化为 1 个 MD 文件（~2000 行）
- 保留：适用场景、验证要求、常见错误

#### 2.2 创建 anti_patterns.md（1 分钟）

**来源**：基于 MM-Agent 的常见错误

**内容**：
```markdown
# MCM 竞赛反模式

## 数据分析反模式

❌ 对小样本使用深度神经网络
✅ 使用简单模型 + 强正则化

❌ 用均值填充缺失值
✅ 使用 MICE 或 KNN

## 模型选择反模式

❌ 只报告最好的结果
✅ 报告所有尝试的模型

## 写作反模式

❌ "图1显示了X与Y的关系"
✅ "图1显示...这表明..."
```

**操作**：
- 从 orientation2/00_MAIN_REVISED.md 复制
- 粘贴到 docs/anti_patterns.md

#### 2.3 创建 mcm_o_prize_style_guide.md（1 分钟）

**来源**：从 orientation2/00_MAIN_REVISED.md 复制

**内容**：
```markdown
# O-Prize 风格指南

## 摘要标准
- 长度：200-300 词
- 必须包含具体数字

## 图表标准
- 必需：方法流程图
- 标题：描述 + 洞察 + 统计

## 统计检验标准
- Shapiro-Wilk, Durbin-Watson, Breusch-Pagan
```

**操作**：
- 从 00_MAIN_REVISED.md 复制
- 粘贴到 docs/mcm_o_prize_style_guide.md

---

### Step 3: 准备参考论文（2 分钟）

#### 3.1 选择论文

**标准**：
- O-Prize 论文
- 有 LaTeX 源码
- 结构完整
- 图表优秀

**示例**：2023 Problem C Outstanding Winner

#### 3.2 复制文件

```bash
# 1. 复制 PDF 和 LaTeX
cp path/to/2023_C_OPrize.pdf reference/best_paper_example/
cp path/to/2023_C_OPrize.tex reference/best_paper_example/

# 2. 创建 README
cat > reference/best_paper_example/README.md << 'EOF'
# O-Prize 参考论文

## 论文信息
- **题目**: Modeling Olympic Medal Counts...
- **年份**: 2023
- **问题**: Problem C
- **奖项**: Outstanding Winner

## 为什么选择这篇？
1. 结构完整（IMRaD）
2. 图表优秀
3. 统计严谨
4. LaTeX 可用

## 如何使用？

Claude Code，请：
1. Read: 2023_C_OPrize.pdf（学习结构）
2. Read: 2023_C_OPrize.tex（学习 LaTeX）
3. 复制风格到当前问题

我要与之 1:1 的专业度。
EOF
```

---

### Step 4: 启动 Claude Code（1 分钟）

```bash
# 1. 进入工作目录
cd D:\migration\MCM-Killer\workspace

# 2. 启动 Claude Code
claude
```

**第一次交互**：
```markdown
# Session 启动指令

Claude Code，请执行以下初始化：

## 1. 读取知识库

Read: docs/math_models_cheatsheet.md
Read: docs/anti_patterns.md
Read: docs/mcm_o_prize_style_guide.md

## 2. 读取历史经验

Read: global_memory/lessons_learned.md

## 3. 学习参考论文

Read: reference/best_paper_example/README.md
Read: reference/best_paper_example/2023_C_OPrize.pdf

## 4. 确认理解

请回答：
- 你记住了哪些反模式？
- 你记住了哪些历史错误？
- 你记住了 O-Prize 论文的哪些风格特征？

## 5. 准备开始

确认后，我将给你 2025_C 问题，开始执行任务。
```

---

## 第三部分：使用流程

### 完整 Session 流程

```markdown
# 完整 Session 流程（从开始到结束）

## Phase 0: 初始化（5 分钟）

**User**:
"Claude Code，请：

1. **读取知识库**：
   - Read: docs/math_models_cheatsheet.md
   - Read: docs/anti_patterns.md
   - Read: docs/mcm_o_prize_style_guide.md

2. **读取历史经验**：
   - Read: global_memory/lessons_learned.md

3. **学习参考论文**：
   - Read: reference/best_paper_example/2023_C_OPrize.pdf
   - Read: reference/best_paper_example/2023_C_OPrize.tex

4. **确认理解**"

**Claude Code**:
→ 读取所有文档
→ 内化为上下文
→ 确认理解

---

## Phase 1: 问题分析（30 分钟）

**User**:
"开始分析 2025_C 问题：
1. 读取 data/2025_Problem_C/2025_Problem_C.pdf
2. 提出核心假设
3. 参考 docs/math_models_cheatsheet.md 选择 2-3 个候选模型
4. 输出到 current_status.md"

**Claude Code**:
→ 科学家模式
→ 分析问题
→ 选择模型
→ 输出计划

---

## Phase 2: 数据处理（1 小时）

**User**:
"切换到工程师模式：
1. 加载数据（BOM-safe）
2. 处理缺失值
3. 创建特征
4. **关键**：参考 global_memory/lessons_learned.md 避免历史错误
5. 保存到 artifacts/data/20260123_features.csv"

**Claude Code**:
→ 工程师模式
→ 编写代码
→ 运行测试
→ 输出数据

---

## Phase 3: 模型训练（2 小时）

**User**:
"继续工程师模式：
1. 使用 Claude Code 原生能力训练 ZINB 模型
2. 对比 Poisson 和 ARIMA
3. 5-fold cross-validation
4. 保存到 artifacts/models/ 和 artifacts/results/
5. 如果超过 30 分钟，暂停向我汇报"

**Claude Code**:
→ 编写训练代码
→ 运行对比
→ 选择最优模型
→ 输出结果

---

## Phase 4: 验证（30 分钟）

**User**:
"切换到批评家模式：
1. 运行统计检验（Shapiro-Wilk, Durbin-Watson, Breusch-Pagan）
2. 检查 docs/anti_patterns.md 确认没踩坑
3. 如果不通过，参考 docs/optimization_strategies.md
4. 最多重试 3 次
5. 保存到 artifacts/validation/"

**Claude Code**:
→ 批评家模式
→ 运行检验
→ 验证通过
→ 输出报告

---

## Phase 5: 灵敏度分析（30 分钟）

**User**:
"继续工程师模式：
1. 扰动参数：±5%, ±10%, ±20%
2. 生成龙卷风图
3. 保存到 artifacts/figures/20260123_tornado.png
4. 保存到 artifacts/validation/20260123_sensitivity.json"

**Claude Code**:
→ 编写灵敏度分析代码
→ 生成图表
→ 输出结果

---

## Phase 6: 撰写论文（2 小时）

**User**:
"切换到作家模式：
1. 参考 reference/best_paper_example/ 的风格
2. 使用 IMRaD 结构撰写论文
3. 每个图表使用观察-洞察模式
4. 包含所有统计检验结果
5. 保存到 artifacts/paper/20260123_paper.tex
6. 编译 PDF"

**Claude Code**:
→ 作家模式
→ 撰写论文
→ 生成图表
→ 编译 LaTeX

---

## Phase 7: 复盘（15 分钟）

**User**:
"任务完成，请复盘：
1. 总结关键错误
2. 提炼经验教训
3. 追加到 global_memory/lessons_learned.md
4. 格式：[日期] - [任务名] / 错误 / 根因 / 解决 / 预防"

**Claude Code**:
→ 复盘整个任务
→ 提炼经验教训
→ 追加到文件

---

**总耗时**：~6-7 小时（包含思考和验证）
```

---

## 第四部分：与原计划的对比

### 实施计划对比

| 方面 | 原计划 (orientation2) | 调整后 (Revised) |
|------|----------------------|-------------------|
| **总时间** | 10 天（~80 小时） | 10 分钟设置 + 6-7 小时执行 |
| **HMML** | 提取 98 个文件 | 1 个速查表 |
| **知识库** | 300+ 文件 | 5 个 MD 文件 |
| **工具开发** | 6 个 Python 脚本 | 无（用 Claude 原生能力） |
| **参考论文** | 自动分析 44 篇 | 1 篇完整范例 |
| **测试** | MMBench 111 问题 | Session 内验证 |
| **人工介入** | 最少 | 关键决策点 |

### 核心改变

1. **从"开发"到"准备"**
   - 不开发工具脚本
   - 准备知识和指令

2. **从"自动化"到"半自主"**
   - 不追求完全自动化
   - 保留人工指挥官角色

3. **从"复杂"到"简单"**
   - 10 分钟设置，立即使用
   - 符合"AI Native"原则

---

## 第五部分：快速检查清单

### 设置完成检查

```bash
# 目录结构检查
✓ docs/ 目录存在
✓ global_memory/lessons_learned.md 存在
✓ reference/best_paper_example/ 存在
✓ artifacts/ 的 8 个子目录存在
✓ data/2025_Problem_C/ 存在
✓ current_status.md 存在

# 知识库检查
✓ docs/math_models_cheatsheet.md 存在
✓ docs/anti_patterns.md 存在
✓ docs/mcm_o_prize_style_guide.md 存在

# 参考论文检查
✓ reference/best_paper_example/README.md 存在
✓ reference/best_paper_example/2023_C_OPrize.pdf 存在
✓ reference/best_paper_example/2023_C_OPrize.tex 存在

# 总文件数检查
echo "预期总文件数：~15 个"
find . -type f | wc -l
```

### Session 启动检查

```markdown
# Claude Code 确认清单

## 读取检查
✓ 已读取 docs/math_models_cheatsheet.md
✓ 已读取 docs/anti_patterns.md
✓ 已读取 docs/mcm_o_prize_style_guide.md
✓ 已读取 global_memory/lessons_learned.md
✓ 已读取参考论文 README
✓ 已读取参考论文 PDF

## 理解检查
✓ 记住了反模式（列举 3 个）
✓ 记住了历史错误（列举 2 个）
✓ 记住了 O-Prize 风格（列举 3 个）

## 规范检查
✓ 理解 artifacts/ 存放中间产物
✓ 理解文件名需要时间戳
✓ 理解 data/ 只读，不修改

## 准备就绪
✓ 可以开始执行任务
```

---

## 第六部分：故障排除

### 常见问题

**Q1: Claude Code 说找不到文件**
```bash
# 检查文件是否存在
ls docs/math_models_cheatsheet.md

# 如果不存在，重新创建
echo "# Math Models Cheatsheet" > docs/math_models_cheatsheet.md
```

**Q2: Claude Code 不理解规范**
```markdown
# 重新明确指令

Claude Code，请重新理解目录规范：

## 关键规范
1. artifacts/：所有中间产物
   - 文件名格式：YYYYMMDD_名称.扩展名
   - 示例：20260123_predictions.csv

2. data/：只读数据
   - 不修改
   - 处理后的数据存 artifacts/data/

3. current_status.md：由你维护
   - 每个阶段更新
   - 记录问题和解决方案

确认理解。
```

**Q3: 复盘内容格式不对**
```markdown
# 重新明确格式

Claude Code，请按以下格式复盘：

## [YYYY-MM-DD] - [任务名]

### 错误
[具体描述，1-2 句话]

### 根因
[深入分析，为什么发生]

### 解决
[代码级别，如何修复]

### 预防
**Claude Code，今后...**：
[具体指令，如何避免]

追加到 global_memory/lessons_learned.md
```

---

## 总结

### 10 分钟设置 vs 10 天开发

| 阶段 | 原计划 | 调整后 |
|------|--------|--------|
| **设置** | 2 天 | 10 分钟 |
| **知识准备** | 2 天 | 5 分钟（手动复制） |
| **工具开发** | 2 天 | 无 |
| **集成测试** | 2 天 | Session 内验证 |
| **文档** | 2 天 | 已包含在知识库 |
| **总时间** | 10 天 | 10 分钟 + 执行时间 |

### 核心原则

1. **去工程化**：不开发 Python 脚本
2. **重认知化**：准备知识和指令
3. **AI Native**：使用 Claude Code 原生能力
4. **快速启动**：10 分钟设置，立即使用

---

**版本**: Revised
**核心理念**: 10 分钟设置，不是 10 天开发
**关键**: 准备知识库，不开发工具，立即使用

---

**END OF 07_ROADMAP_REVISED.md**
