# MCM-Killer v3.1.0 架构文档索引

> **Version**: v3.1.0-Ultimate (Cognitive Narrative & Adversarial Evolution)
> **Date**: 2026-01-24
> **Status**: Final Architecture Specification
> **Core Philosophy**: "叙事即计算" - Transforming struggles into scientific insights

---

## 快速导航

### 🎯 我是谁？我需要读什么？

| 角色 | 推荐阅读路径 | 时间 | 目的 |
|------|-------------|------|------|
| **架构师** | ① → ② → ③ | 3小时 | 理解完整架构和实施细节 |
| **Agent开发者** | ① → ④ | 1小时 | 获取Agent Prompt模板 |
| **工具开发者** | ① → ⑤ | 30分钟 | 获取Python工具代码 |
| **项目经理** | ① → ⑥ | 30分钟 | 评估升级价值和可行性 |
| **新手入门** | ⑥ → ① → ② | 4小时 | 从概述到详细实施 |

---

## 📚 核心文档目录

### ① [MCM-Killer v3.1.0 终极架构白皮书](A_CORE_ARCHITECTURE/00_ultimate_whitepaper.md)
**⭐⭐⭐⭐⭐⭐ 必读 - 最核心文档 (2000+ 行)**

**内容概览**:
- Part I: 哲学基础 - "叙事即计算"范式
- Part II: 18-Agent生态系统详解
- Part III: 13-Phase工作流
- Part IV: 三大新协议 (Protocol 13-15)
- Part V: HMML 2.0动态知识库
- Part VI: 三大Python工具 (完整代码)
- Part VII: Workspace结构规范
- Part VIII: 15天实施路线图
- Part IX: 风险评估与缓解
- Part X: 质量保证与测试

**适合**: 所有角色必读

---

### ② [认知叙事框架](A_CORE_ARCHITECTURE/02_cognitive_narrative_framework.md)
**⭐⭐⭐⭐ 深度理解论文如何"讲故事"**

**核心内容**:
- Hero's Journey模板 - "困难→洞察"叙事弧
- Observation-Implication协议 - 观察必须配解释
- 技术错误→物理意义映射表
- 具体写作示例 (v3.0.0 vs v3.1.0对比)

**适合**: @writer, @narrative_weaver, @metacognition_agent

---

### ③ [Sprint实施指南 (3个)](B_IMPLEMENTATION_GUIDES/)
**⭐⭐⭐⭐⭐ 实施必读 - 包含代码和具体操作**

#### [Sprint 1: Foundation & Eyes (Days 1-3)](B_IMPLEMENTATION_GUIDES/01_sprint_1_foundation.md)
- 目录结构初始化代码
- HMML 2.0迁移脚本 (migrate_hmml.py)
- style_analyzer.py完整实现
- ANTI_PATTERNS.md模板

#### [Sprint 2: Brain & Soul (Days 4-8)](B_IMPLEMENTATION_GUIDES/02_sprint_2_brain_soul.md)
- @metacognition_agent完整Prompt
- @narrative_weaver完整Prompt
- log_analyzer.py完整实现
- @visualizer双模式 (Mode A + Mode B) 详细说明

#### [Sprint 3: Fangs & Shield (Days 9-14)](B_IMPLEMENTATION_GUIDES/03_sprint_3_adversarial.md)
- @judge_zero三人格Prompt
- @knowledge_librarian双模式Prompt
- mmbench_score.py完整实现
- DEFCON 1状态机详解

**适合**: 开发者、实施工程师

---

### ④ [Agent Prompt规范] (从白皮书Part II提取)
**⭐⭐⭐⭐ Agent开发者必读**

**包含**:
- @metacognition_agent: 侦探式反思者 (完整Prompt)
- @narrative_weaver: 故事导演 (完整Prompt)
- @knowledge_librarian: 学术馆长 (完整Prompt)
- @judge_zero: 红队评审 (完整Prompt三人格)

**位置**: 白皮书Part II: Module 2.2

**适合**: 直接复制使用

---

### ⑤ [Python工具参考] (从白皮书Part VI提取)
**⭐⭐⭐ 工具开发者必读**

**包含**:
- tools/style_analyzer.py - 分析O奖论文生成style_guide.md
- tools/log_analyzer.py - 压缩GB日志为JSON摘要
- tools/mmbench_score.py - 自动评分0-100分

**位置**: 白皮书Part VI: Module 6

**适合**: 直接复制使用

---

### ⑥ [版本对比与路线图](A_CORE_ARCHITECTURE/01_version_comparison.md)
**⭐⭐⭐ 快速了解变化**

**核心表格**:
- Agents: 14 → 18 (+4新Agent)
- Phases: 10 → 13 (+3新Phase)
- Protocols: 12 → 15 (+3新Protocol)
- 叙事质量: 从"正确"到"深刻"

**适合**: 快速了解升级范围

---

## 🔍 按主题查找

### 主题1: 认知叙事 (Cognitive Narrative)
**文档**:
- 白皮书 Part I, Part III
- 认知叙事框架 (独立文档)

**关键概念**:
- "错误不是垃圾，是洞察的原材料"
- Hero's Journey: Call → Ordeal → Revelation → Resolution → Treasure
- Observation-Implication协议

---

### 主题2: 对抗评审 (Adversarial Review)
**文档**:
- 白皮书 Part II (Module 2.2 @judge_zero)
- 白皮书 Part IV (Protocol 13)
- Sprint 3指南

**关键概念**:
- 三人格评审: 统计学家+领域专家+疲惫编辑
- DEFCON 1状态机
- Mercy Rule防死循环

---

### 主题3: 动态知识库 (HMML 2.0)
**文档**:
- 白皮书 Part V
- Sprint 1指南 (HMML迁移脚本)

**关键概念**:
- 从单文件到结构化目录
- YAML Front Matter元数据
- narrative_value字段 (O奖叙事价值)

---

### 主题4: 实施路线图
**文档**:
- 白皮书 Part VIII
- Sprint 1-3指南 (详细)

**时间表**:
- Sprint 1 (Days 1-3): 基础+视觉
- Sprint 2 (Days 4-8): 大脑+灵魂
- Sprint 3 (Days 9-14): 獠牙+盾牌

---

## 📊 文档关系图

```
                    ┌──────────────────────────┐
                    │ 00_ultimate_whitepaper   │ (核心，2000+行)
                    │   (Part I-X 完整架构)    │
                    └───────────┬──────────────┘
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
    ┌───────▼──────┐    ┌───────▼──────┐   ┌──────▼──────┐
    │ 认知叙事框架  │    │ 实施指南      │   │ Agent规范   │
    │ (Part III)   │    │ (Part VIII)   │   │ (Part II)   │
    └──────────────┘    └───────┬──────┘   └─────────────┘
                                 │
                     ┌───────────┼───────────┐
                     │           │           │
             ┌───────▼──┐  ┌───▼─────┐  ┌──▼────────┐
             │ Sprint 1 │  │ Sprint 2│  │ Sprint 3  │
             │ Days 1-3 │  │ Days 4-8│  │ Days 9-14 │
             └──────────┘  └─────────┘  └───────────┘
```

---

## 🚀 实施步骤

### Step 1: 理解架构 (Day 0)
1. 阅读"版本对比" (15分钟)
2. 阅读白皮书"Executive Summary" (30分钟)
3. 阅读白皮书"Part I: 哲学基础" (30分钟)

### Step 2: Sprint 1实施 (Days 1-3)
1. 阅读Sprint 1指南 (1小时)
2. 执行Day 1-3任务 (创建目录、迁移HMML)
3. 验证: 目录建立、HMML可检索

### Step 3: Sprint 2实施 (Days 4-8)
1. 阅读Sprint 2指南 (1.5小时)
2. 执行Day 4-8任务 (创建Agent、工具)
3. 验证: Phase 5.8可生成narrative_arc

### Step 4: Sprint 3实施 (Days 9-14)
1. 阅读Sprint 3指南 (1.5小时)
2. 执行Day 9-14任务 (对抗评审、自进化)
3. 验证: 全链路测试通过

---

## 📝 文档命名规范

| 前缀 | 含义 | 示例 |
|------|------|------|
| `A_` | 核心架构 (CORE) | A_CORE_ARCHITECTURE/ |
| `B_` | 实施指南 (IMPLEMENTATION) | B_IMPLEMENTATION_GUIDES/ |
| `C_` | Agent规范 (AGENTS) | C_AGENT_SPECIFICATIONS/ |
| `D_` | 工具参考 (TOOLS) | D_TOOLS_REFERENCE/ |
| `00_` | 主文档 (PRIMARY) | 00_ultimate_whitepaper.md |
| `01_` | 次级文档 (SECONDARY) | 01_version_comparison.md |

---

## ⚠️ 重要提示

### 1. 版本一致性
所有文档标注 **v3.1.0-Ultimate**。如果看到v3.0.0字样，说明是旧版本。

### 2. 文档完整性
- ✅ **完整**: 10, 20-22号文档
- ❌ **已删除**: 00-02号初始版本 (已被10号替代)
- ⏳ **待创建**: Agent规范、工具参考 (可从白皮书提取)

### 3. 阅读顺序建议
**新手**: README → 00白皮书 → Sprint 1-3指南
**老手**: 直接查阅需要的章节

### 4. 交叉引用
所有文档使用相对路径交叉引用。如果移动文件，需要更新链接。

---

## 🔗 外部资源

### v3.0.0 参考文档
- `../00_architecture.md` - v3.0.0架构总览
- `../03_mcm_killer_architecture.md` - v3.0.0详细架构
- `../draft/VALUABLE/` - LLM-MM-Agent核心资产 (6星资源)

### 相关项目
- `D:/migration/clean version/LLM-MM-Agent/` - 参考实现 (NeurIPS 2025)
- `D:/migration/MCM-Killer/workspace/2025_C/` - 当前工作区

---

## 📮 反馈与更新

### 文档维护者
- **架构设计**: Claude (基于Gemini 4.txt优化)
- **实施细节**: 参考chat with claude 1-3.txt
- **整合方案**: 基于00_CONSOLIDATION_PLAN.md

### 版本历史
- **v1.0** (2026-01-24): 初始版本，完整v3.1.0规范
- 后续版本将根据实施反馈更新

---

**文档版本**: v1.0-Final
**最后更新**: 2026-01-24
**状态**: Ready for Implementation
