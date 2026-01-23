# MM-Agent → MCM-Killer v3.0 Fusion Architecture (Revised)

> **AI Native 开发范式：从架构师到指挥官**
> **核心原则**: 去工程化（De-Engineering），重认知化（Re-Cognition）
> **Version**: 3.0-Fusion-Revised
> **Date**: 2026-01-23

---

## 核心战略转变

### 旧范式（错误）

```
Python Runtime (我控制一切)
├─ LLM Wrapper
├─ File Manager
├─ Context Manager
├─ Error Handler
└─ Task Scheduler
     ↓ (调用)
Claude Code (被调用者)
```

### 新范式（正确）

```
结构化 Markdown 指令集
├─ 知识库 (Domain Wisdom)
├─ 角色定义 (Metacognition)
├─ 工作流 (TOTE Logic)
└─ 风格指南 (O-Prize Standards)
     ↓ (阅读)
Claude Code (自主执行者)
     ↓ (反馈)
User (指挥官) → 规则更新 → 指令集优化
```

---

## 第一部分：坚决舍弃的模块

### ❌ 舍弃清单

| 模块 | 原计划 | 原因 | Claude Code 替代方案 |
|------|--------|------|---------------------|
| **文件管理类** | FileManager, ContextManager | 重复造轮子 | 原生 `read`, `edit`, `ls` |
| **语法修复循环** | While retry on SyntaxError | Claude 自动修复 | 内置自愈机制 |
| **JSON 控制流** | {"action": "..."} 控制执行 | 不自然 | 直接自然语言指令 |
| **上下文窗口** | 滑动窗口、Token 计数 | Claude 更智能 | `/compact` 自动压缩 |
| **AST 验证** | 静态代码分析 | 信任执行环境 | 直接运行，有问题再修 |
| **Python 包装器** | subprocess.call Claude | 多余 | 直接使用 CLI |

### 保留内容（大幅简化）

**从 06_FILE_MAPPING.md** 只保留：
- ✅ 目录结构定义
- ✅ 文件命名规范
- ❌ 删除所有 Python 实现类

---

## 第二部分：核心资产（Must Keep）

### 1. 知识库 → 主动注入

**原计划**：被动检索（向量数据库查询）

**新方案**：主动注入（会话启动时读取）

```
bootstrap.md:
"""
Claude Code，请阅读以下知识文档：

1. docs/math_models_cheatsheet.md
2. docs/anti_patterns.md (不要犯这些错误)
3. docs/mcm_o_prize_style_guide.md

作为你的领域知识背景。确认理解。
"""
```

**新增：Anti-Patterns（反模式）**

```markdown
# Anti-Patterns: MCM 竞赛中的致命错误

> **比"做什么"更重要的是"不做什么"**

## 数据分析反模式

❌ **错误**: 对小样本数据（n<50）使用深度神经网络
- **原因**: 过拟合，无法泛化
- **替代**: 使用简单模型（逻辑回归、决策树）+ 强正则化
- **参考**: 2019 Problem B M-Prize 论文

❌ **错误**: 直接用均值填充缺失值
- **原因**: 引入偏差，破坏数据分布
- **替代**: MICE 多重插补 或 KNN
- **参考**: 统计学最佳实践

❌ **错误**: 忽略时间序列的平稳性检验
- **原因**: 虚假回归，模型无效
- **替代**: ADF 检验，差分处理
- **参考**: 计量经济学标准流程

## 模型选择反模式

❌ **错误**: "随机森林最准确，就用它"
- **原因**: 缺乏理论依据，评委质疑
- **替代**: 必须对比 2-3 个模型，说明选择理由
- **参考**: 所有 O-Prize 论文都有模型对比表

❌ **错误**: 只报告最好的结果
- **原因**: 隐瞒失败实验，学术不端
- **替代**: 报告所有尝试的模型，包括失败的
- **参考**: O-Prize 诚信标准

## 写作反模式

❌ **错误**: "图1显示了X与Y的关系"
- **原因**: 没有洞察，只是描述
- **替代**: "图1显示...这表明...（Implication）"
- **参考**: O-Prize 观察洞察模式

❌ **错误**: 没有灵敏度分析
- **原因**: 模型鲁棒性未知，无法信任
- **替代**: 必须包含龙卷风图或参数扰动分析
- **参考**: O-Prize 100% 都有灵敏度分析
```

### 2. Agent 角色 → 元认知指令

**原计划**：Python 代码切换角色

**新方案**：单一 Agent，多重角色

```markdown
# 系统指令（会话启动时注入）

Claude Code，你将身兼数职，在任务的不同阶段切换思维模式：

## 🔬 科学家模式 (Scientist Mode)
**启用时机**：接到问题、选择模型、设计实验时
**思维重点**：
- 优先理论依据，不是实用主义
- 提出假设（Hypothesis），不是直接动手
- 查阅 docs/math_models_cheatsheet.md
- 输出：研究计划、模型选择理由

## 🔧 工程师模式 (Engineer Mode)
**启用时机**：编写代码、处理数据时
**思维重点**：
- 代码健壮性 > 简洁性
- **工具使用规范**：
  - 写代码前：先写单元测试
  - 处理数据：先用 `pd.to_datetime(..., errors='coerce')`
  - 运行模型：先用小数据集验证逻辑
- 输出：可运行的代码

## 👮 批评家模式 (Critic Mode)
**启用时机**：检查结果、验证模型时
**思维重点**：
- 质疑一切，包括自己的工作
- 对比 O-Prize 标准
- 查阅 docs/anti_patterns.md
- 输出：改进建议、潜在问题

## 📝 作家模式 (Writer Mode)
**启用时机**：撰写论文时
**思维重点**：
- 参考 docs/mcm_o_prize_style_guide.md
- 使用观察-洞察模式
- IMRaD 结构
- 输出：学术论文章节

## 模式切换协议

当你完成一个阶段的任务后，**自动**切换到下一个模式：
- 科学家 → 工程师 → 批评家 → 作家
- 或根据需要跳转
```

### 3. 任务分解 → Prompt 链

**原计划**：JSON 任务定义 + Python 编排

**新方案**：自然语言元指令

```markdown
# 任务分解元指令

**Claude Code，当你接到任何问题时，必须按以下流程思考**：

## 第一步：科学家思维 - 假设驱动
1. 阅读 docs/math_models_cheatsheet.md
2. 提出核心假设（例如："数据具有周期性"）
3. 设计最小可行实验（MVP）验证假设
4. 输出到 execution_plan.md

## 第二步：工程师思维 - 健壮执行
1. 根据 execution_plan.md 编写代码
2. **工具使用规范**：
   - 写代码前：写单元测试（pytest 或 assert）
   - 处理数据：使用 BOM-safe 加载
   - 运行模型：先用小数据集验证
3. 运行 tests/validation.py 自检
4. 输出到 results/

## 第三步：批评家思维 - 质量把关
1. 检查 docs/anti_patterns.md，确认没有踩坑
2. 验证结果：
   - R² > 0.6？
   - 统计检验通过？
   - 没有明显过拟合？
3. 如果不满足：阅读 docs/optimization_strategies.md
4. 自动优化（最多 3 次重试）

## 第四步：作家思维 - 学术表达
1. 参考 docs/mcm_o_prize_style_guide.md
2. 使用观察-洞察模式写图表说明
3. 确保包含灵敏度分析
4. 输出 LaTeX 章节

**关键**：以上流程是**自动循环**的，不需要我每步指令。
```

### 4. 参考论文 → One-Shot 学习

**原计划**：提取特征模式

**新方案**：完整范例学习

```
reference/
├── best_paper_example/
│   ├── 2023_C_OPrize.pdf
│   ├── 2023_C_OPrize.tex
│   ├── figures/           # 所有图表
│   └── code/              # 代码片段
└── README.md

指令：
"参考 reference/best_paper_example/ 的：
1. 目录结构
2. LaTeX 宏包使用
3. 图表配色（提取其 RGB 值）
4. TikZ 绘图代码

我要与之 1:1 的专业度。"
```

### 5. 自进化 → Session 间记忆

**原计划**：自动分析报告并更新

**新方案**：复盘指令 + 人工审核

```markdown
# Session 启动指令

**Claude Code，请执行以下初始化**：

1. 读取 global_memory/lessons_learned.md
2. 在本次任务中，**严格避免**重复以下错误：
   - [列出历史错误]

# Session 结束指令

**任务完成后，请执行复盘**：

1. 总结本次任务的 Critical Errors
2. 提炼经验教训
3. 追加写入 global_memory/lessons_learned.md
4. 格式：
   ```markdown
   ## [日期] - [任务名]

   **错误**：[具体描述]
   **根因**：[为什么发生]
   **解决**：[如何修复]
   **预防**：[下次如何避免]
   ```
```

---

## 第三部分：工具协议（简化）

### 工具调用规范

**不写 Python 包装器**，直接自然语言指令：

```markdown
# 工具调用规范

## 训练模型时
**指令**：
"训练 X 模型，使用以下配置：
- 数据：data/features.csv
- 参数：参见 docs/model_configs.md
- 验证：运行 tests/validation.py 后继续
- 超时预期：30 分钟

**关键**：如果训练超过 30 分钟，暂停向我汇报。"

## 生成图表时
**指令**：
"生成 Y 类型的图表，参考 docs/figure_styles.md：
- 使用学术配色（参考 paper_example/）
- 包含误差棒
- 保存为 artifacts/figures/YYYYMMDD_figure_name.png
- 时间戳文件名防止覆盖"
```

---

## 第四部分：目录规范（极简）

### Directory Manifest

```
workspace/
├── docs/                    # 所有知识库（主动注入）
│   ├── math_models_cheatsheet.md
│   ├── anti_patterns.md
│   ├── mcm_o_prize_style_guide.md
│   └── optimization_strategies.md
│
├── global_memory/           # Session 间记忆
│   └── lessons_learned.md
│
├── reference/               # 参考论文
│   └── best_paper_example/
│
├── data/                   # 只读数据
│   └── 2025_Problem_C_Data/
│
├── scripts/                # Python 工具脚本（可选）
│   ├── validate.py
│   └── compute_metrics.py
│
├── artifacts/              # **所有中间产物**
│   ├── code/              # 生成的代码
│   ├── figures/           # 时间戳文件名！
│   ├── models/            # 训练的模型
│   └── reports/           # 所有 JSON/CSV/MD
│
└── current_status.md       # 任务状态（由 Claude 维护）
```

**关键规范**：
- ❌ **不要**用 Python 代码强制路径检查
- ✅ **要**告诉 Claude Code："所有中间产物存 artifacts/，文件名必须带时间戳"
- ❌ **不要**写复杂的依赖管理
- ✅ **要**在会话开始时说清楚目录结构

---

## 第五部分：交互流程实战

### Step 1: 初始化（Bootstrap）

```
用户输入：
"Claude Code，请阅读 docs/ 下的所有文档。
确认理解后，为 Problem C 创建一个 execution_plan.md。"

Claude Code 输出：
✓ 读取了 5 个知识文档
✓ 理解了：反模式、模型选择、O-Prize 标准
→ 创建 execution_plan.md
```

### Step 2: 执行（Execution）

```
用户输入：
"批准计划。开始 Phase 1。
注意：上次在日期格式上出错，这次用 pd.to_datetime(errors='coerce')。
每步完成后运行 tests/validation.py。"

Claude Code 自动：
1. 科学家模式：查看 docs/ 选择合适模型
2. 工程师模式：编写代码 + 单元测试
3. 批评家模式：运行 tests/validation.py
4. 循环改进直到通过
```

### Step 3: 人工干预（Human-in-the-Loop）

```
Claude Code 卡住了或出错：

用户输入：
"停下。你的模型过拟合了。
参考 docs/math_models_cheatsheet.md 中的正则化方法，
使用 L1/L2 penalty 重新训练。"

Claude Code 调整策略：
→ 读取文档，应用正则化
→ 重新训练
→ 验证改进
```

### Step 4: 复盘（Debrief）

```
任务完成后：

用户输入：
"任务完成。请复盘本次 Critical Errors，
总结经验教训追加到 global_memory/lessons_learned.md"

Claude Code 输出：
→ 分析错误
→ 追加到 global_memory/lessons_learned.md
→ 下次 session 自动读取
```

---

## 第六部分：文件调整清单

### 需要修改的文件

| 文件 | 修改内容 | 删除内容 | 优先级 |
|------|---------|---------|--------|
| **01_KNOWLEDGE_LIBRARY.md** | 添加 Anti-Patterns，简化为主动注入 | - | ⭐⭐⭐⭐⭐ |
| **02_AGENT_PROMPTS.md** | 改为元认知指令，添加工具使用规范 | Python 切换代码 | ⭐⭐⭐⭐⭐ |
| **03_TASK_DECOMPOSITION.md** | 改为 Prompt 链，删除 JSON | Python 类定义 | ⭐⭐⭐⭐⭐ |
| **04_REFERENCE_LEARNING.md** | 添加 One-Shot 学习，完整范例 | - | ⭐⭐⭐⭐ |
| **05_SELF_EVOLUTION.md** | 改为 Session 间记忆，复盘指令 | 自动分析脚本 | ⭐⭐⭐⭐ |
| **06_FILE_MAPPING.md** | 简化为 Directory Manifest | Python 实现类 | ⭐⭐⭐ |
| **07_ROADMAP.md** | 删除 Python 脚本，改为指令集 | scripts/ 目录 | ⭐⭐⭐ |

### 新增文件

| 文件 | 内容 | 来源 |
|------|------|------|
| **docs/anti_patterns.md** | MCM 竞赛反模式 | 新增 |
| **docs/math_models_cheatsheet.md** | 模型速查表 | HMML 简化 |
| **docs/mcm_o_prize_style_guide.md** | O-Prize 风格指南 | 参考论文提取 |
| **global_memory/lessons_learned.md** | Session 间记忆 | 新增 |
| **reference/best_paper_example/** | 完整范例 | 现有论文 |

---

## 第七部分：总结对比

### 架构对比

| 方面 | 原计划（orientation2） | 调整后（Revised） |
|------|----------------------|-------------------|
| **控制流** | Python Runtime | Claude Code + 自然语言 |
| **知识检索** | 向量数据库 | Markdown 主动注入 |
| **角色切换** | Python 代码 | 元认知指令 |
| **任务定义** | JSON schema | Prompt 模板 |
| **文件管理** | FileManager | 目录规范 + Claude |
| **错误处理** | While 循环 | Claude 自动 + 人工干预 |
| **进化机制** | 自动分析脚本 | 复盘指令 + 人工审核 |

### 核心改变

1. **从 "写代码" 到 "写指令"**
   - 不写 Python 运行时
   - 写 Markdown 知识库
   - 写 Prompt 模板

2. **从 "控制" 到 "引导"**
   - 不控制 Claude Code 执行细节
   - 提供知识和规范
   - 人工干预关键决策

3. **从 "自动化" 到 "半自主"**
   - 不追求完全自动化
   - 保留人工指挥官角色
   - TOTE 循环通过 Prompt 实现

---

## 快速开始

### 10分钟设置

```bash
# 1. 创建目录
mkdir -p docs global_memory reference/best_paper_example

# 2. 准备知识库（从 MM-Agent 提取）
# - 将 HMML 转为 docs/math_models_cheatsheet.md
# - 创建 docs/anti_patterns.md

# 3. 准备参考论文
# - 复制一篇 O-Prize 论文到 reference/best_paper_example/

# 4. 初始化全局记忆
echo "# Lessons Learned\n\n" > global_memory/lessons_learned.md

# 5. 启动 Claude Code
cd workspace
claude
```

### 第一次交互

```markdown
Claude Code，请：

1. 阅读 docs/ 下的所有文档
2. 确认理解了：
   - MCM 竞赛的基本规则
   - 常见的反模式（Anti-Patterns）
   - O-Prize 论文的标准风格
3. 为 2025_C 问题创建 execution_plan.md
```

---

**版本**: Revised
**核心理念**: AI Native - 从架构师到指挥官
**关键**: 不写 Python，写指令；不控制流程，引导认知

---

**END OF 00_MAIN_REVISED.md**
