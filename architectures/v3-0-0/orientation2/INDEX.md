# MCM-Killer v3.0 最终文档索引

> **版本**: 3.0-Final
> **日期**: 2026-01-23
> **状态**: ✅ 完成优化

---

## 文档结构

```
D:\migration\MCM-Killer\architectures\v3-0-0\orientation2/
│
├── 📋 核心架构文档
│   ├── 00_MAIN.md                           # 总体架构（修订版）
│   ├── 01_KNOWLEDGE_LIBRARY.md              # 知识库（修订版）
│   ├── 02_AGENT_PROMPTS.md                  # Agent 提示（修订版）
│   ├── 03_TASK_DECOMPOSITION.md              # 任务分解（修订版）
│   ├── 04_REFERENCE_LEARNING.md              # 参考学习（修订版）
│   ├── 05_SELF_EVOLUTION.md                  # 自进化（修订版）
│   ├── 06_FILE_MAPPING.md                    # 文件映射（修订版）
│   └── 07_ROADMAP.md                          # 实施路线图（修订版）
│
├── 📚 优化说明文档
│   ├── EXTRACTIONS_FROM_ORIENTATION.md      # 从 Orientation 提取的资产
│   └── OPTIMIZATION_SUMMARY.md               # 优化总结
│
└── 📖 原始参考文档
    └── chat_with_claude1.txt                 # 核心架构指导
```

---

## 快速导航

### 如果你是第一次阅读

**推荐阅读顺序**：

1. **00_MAIN.md** (10 分钟) - 理解总体架构和核心原则
2. **EXTRACTIONS_FROM_ORIENTATION.md** (10 分钟) - 了解从 Orientation 提取的资产
3. **01_KNOWLEDGE_LIBRARY.md** (15 分钟) - 知识库结构
4. **02_AGENT_PROMPTS.md** (15 分钟) - 4 个元认知模式
5. **OPTIMIZATION_SUMMARY.md** (5 分钟) - 快速总结

### 如果你要立即实施

**推荐阅读顺序**：

1. **00_MAIN.md** - 理解架构
2. **07_ROADMAP.md** - 10 分钟设置指南
3. **01_KNOWLEDGE_LIBRARY.md** - 准备知识库
4. **开始执行**

### 如果你想了解详细方案

**完整阅读所有文档**（~2 小时）

---

## 核心文档概览

### 00_MAIN.md - 总体架构

**核心内容**：
- 核心战略转变（Python Runtime → Markdown 指令集）
- 坚决舍弃的模块（FileManager、JSON repair 等）
- 核心资产（5 个知识库 MD 文件）
- 目录规范（极简版）

**关键原则**：
- 去工程化（De-Engineering）
- 重认知化（Re-Cognition）
- 从"架构师"到"指挥官"

---

### 01_KNOWLEDGE_LIBRARY.md - 知识库

**核心内容**：
- 知识库结构（5 个核心 MD 文件）
- 主动注入 vs 被动检索
- Anti-Patterns（反模式）- 新增
- Session 间记忆
- One-Shot 学习（完整范例）

**关键改变**：
- 300+ 文件 → 5 个核心 MD 文件
- 向量数据库 → 主动读取
- 新增 anti_patterns.md

---

### 02_AGENT_PROMPTS.md - Agent 提示

**核心内容**：
- 4 个元认知模式
- 科学家模式（问题分析、假设驱动）
- 工程师模式（代码实现、健壮性）
- 批评家模式（质量把关、找茬）
- 作家模式（学术表达、IMRaD）

**关键改变**：
- 14 个 Agent → 4 个思维模式
- Python 切换 → 自然语言切换
- 单一上下文，连贯执行

---

### 03_TASK_DECOMPOSITION.md - 任务分解

**核心内容**：
- Prompt 链设计
- 自然语言指令模板
- 完整任务流程（从问题到论文）
- 人工干预指令

**关键改变**：
- JSON 任务定义 → Prompt 链
- Python DAG → 自然语言依赖
- 4 个模式的自动循环

---

### 04_REFERENCE_LEARNING.md - 参考学习

**核心内容**：
- One-Shot 学习（1 篇完整论文）
- 参考论文目录结构
- 提取风格要素（结构、配色、LaTeX）
- 学习协议和使用方式

**关键改变**：
- 自动分析 44 篇 → 1 篇完整学习
- JSON 风格指南 → 完整论文
- Python 生成脚本 → 手动提取

---

### 05_SELF_EVOLUTION.md - 自进化

**核心内容**：
- Session 间记忆系统
- lessons_learned.md 格式
- Session 启动/复盘协议
- 人工审核流程

**关键改变**：
- 自动进化脚本 → Session 复盘
- MMBench 111 问题 → Session 内验证
- evolution_log.md → lessons_learned.md

---

### 06_FILE_MAPPING.md - 文件映射

**核心内容**：
- Directory Manifest（极简）
- artifacts/ 规范（时间戳文件名）
- 7 个目录的用途说明
- 使用协议

**关键改变**：
- Python 文件管理类 → 自然语言规范
- 复杂命名系统 → 时间戳
- 信任 Claude Code 遵守指令

---

### 07_ROADMAP.md - 实施路线

**核心内容**：
- 10 分钟设置计划
- 快速检查清单
- Session 启动指令
- 完整 Session 流程示例

**关键改变**：
- 10 天开发 → 10 分钟设置
- 工具开发 → 知识准备
- 复杂测试 → Session 内验证

---

## 优化文档

### EXTRACTIONS_FROM_ORIENTATION.md

**内容**：从 Orientation 提取的 3 个黄金资产

**资产**：
1. HMML 模型选择逻辑 → SOP 文档
2. 评估标准 → Python 验证脚本
3. 系统提示 → Markdown 文档

**删除**：
- JSON 修复系统
- 文件管理工具
- 复杂拆分脚本

---

### OPTIMIZATION_SUMMARY.md

**内容**：优化前后对比

**核心对比**：
- Orientation（原）：4/10，过度工程化
- Orientation2（优化后）：8/10，文档驱动

**关键指标**：
- 文件数：300+ → 15（-95%）
- 开发时间：10 天 → 10 分钟（-99.9%）
- Token 使用：降 40-50%

---

## 使用指南

### 第一次使用

```bash
# 1. 阅读 00_MAIN.md（了解架构）
# 2. 阅读 OPTIMIZATION_SUMMARY.md（了解优化）
# 3. 阅读 07_ROADMAP.md（开始设置）
```

### 设置流程

```bash
# 10 分钟设置
mkdir -p docs global_memory reference/best_paper_example artifacts/{code,figures,models,data,results,validation,paper}

# 准备知识库（从 orientation2 提取）
# 详见 01_KNOWLEDGE_LIBRARY.md

# 启动 Claude Code
claude
```

---

## 核心原则回顾

### ✅ 要做

1. **准备知识库**：5 个核心 MD 文件
2. **元认知模式**：4 个思维模式
3. **Prompt 链**：自然语言指令
4. **One-Shot 学习**：1 篇完整论文
5. **Session 复盘**：提炼经验教训
6. **时间戳文件名**：防止覆盖

### ❌ 不要做

1. **不写 Python 运行时**
2. **不开发工具脚本**（用 Claude 原生）
3. **不使用向量数据库**（主动读取）
4. **不用 JSON 控制流**（自然语言）
5. **不自动进化**（人工审核）
6. **不强制路径检查**（信任 Claude）

---

## 版本历史

- **v3.0-orientation2** (原始) - 过度工程化倾向
- **v3.0-Final** (当前) - 完成优化，文档驱动架构
- **v3.0-Revised** → **v3.0-Final** - 删除原文件，应用修订版

---

## 下一步

1. **阅读 00_MAIN.md** 开始
2. **阅读 07_ROADMAP.md** 进行设置
3. **阅读 EXTRACTIONS_FROM_ORIENTATION.md** 了解优化细节

---

**END OF INDEX.md**
