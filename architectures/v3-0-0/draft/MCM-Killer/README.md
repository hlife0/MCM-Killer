# MCM-Killer 文档结构总览

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/MCM-Killer/README.md`
> **最后更新**: 2026-01-24

本文档系列按照 **MCM-Killer 项目的实际目录结构** 组织，提供完整的导航和详细说明。MCM-Killer 是独立的数学建模竞赛多智能体系统，采用 18 阶段工作流、14 个专业 Agent、7 个验证门控的高级架构。

---

## 系统定位

**MCM-Killer** 与 **LLM-MM-Agent** 是两个**独立的系统**，各自有不同的设计目标：

| 特性 | LLM-MM-Agent | MCM-Killer |
|------|--------------|------------|
| **定位** | 学术研究原型 (NeurIPS/ICML 2025) | 竞赛实战系统 |
| **目标** | 探索 LLM 解决数学建模问题的可行性 | 最大化竞赛成绩和完成质量 |
| **工作流** | 4 阶段流水线 | 18 阶段工作流 + 7 个验证门控 |
| **Agent 数量** | 5 个基础 Agent | 14 个专业 Agent |
| **复杂度** | 相对简单，适合学习和研究 | 高度复杂，严格质量控制 |
| **参考位置** | `clean version/LLM-MM-Agent/` | `MCM-Killer/` |

**重要**: MCM-Killer **不是** LLM-MM-Agent 的优化版本或衍生系统，而是完全独立设计开发的竞赛系统。

---

## 完整目录树

```
MCM-Killer/
│
├── 📄 项目根文件
│   ├── README.md
│   └── CLAUDE.md                    # 项目主文档
│
├── 📁 architectures/ ⭐⭐⭐⭐⭐ 架构版本管理
│   ├── v2-3-0.md                   # v2.3.0 架构文档
│   │
│   ├── v2-4-0/                   # v2.4.0 架构
│   │   ├── architecture.md
│   │   ├── workflow_design.md
│   │   ├── validation_design.md
│   │   ├── consultation_design.md
│   │   ├── methodology.md
│   │   └── retrospective.md
│   │
│   ├── v2-4-1/                   # v2.4.1 架构
│   │   ├── architecture.md
│   │   ├── methodology.md
│   │   ├── retrospective.md
│   │   └── agents_backup/        # Agent 备份
│   │
│   ├── v2-4-2/                   # v2.4.2 架构
│   │   ├── architecture.md
│   │   ├── methodology.md
│   │   └── retrospective.md
│   │
│   ├── v2-5-0/                   # v2.5.0 架构（关键版本）
│   │   ├── 00_CHANGES.md           # 变更日志
│   │   ├── 01_README.md
│   │   ├── 02_core.md             # 核心文档
│   │   ├── 03_workflow.md         # 工作流
│   ├── 04_validation.md        # 验证设计
│   │   ├── 05_consultation.md     # 咨询设计
│   │   ├── 06_agents.md           # Agent 规范（13 个）
│   │   ├── 07_anti_laziness.md    # 反懒惰机制
│   │   ├── agents/               # Agent 详细文档
│   │   │   ├── reader.md
│   │   │   ├── researcher.md
│   │   │   ├── modeler.md
│   │   │   ├── code_translator.md
│   │   │   ├── model_trainer.md
│   │   │   ├── validator.md
│   │   │   ├── visualizer.md
│   │   │   ├── writer.md
│   │   │   ├── summarizer.md
│   │   │   ├── editor.md
│   │   │   ├── advisor.md
│   │   │   ├── director.md
│   │   │   └── feasibility_checker.md
│   │   ├── architecture.md
│   │   ├── ARCHITECTURE_v2.5.0.md
│   │   ├── CHANGELOG.md
│   │   ├── CLAUDE.template.md
│   │   ├── directory_structure.md
│   │   ├── SUMMARY.md
│   │   └── anti_lazy_mechanisms.md
│   │
│   ├── v2-5-1/ - v2-5-5/         # v2.5.x 系列迭代版本
│   │   ├── 01_core_rules.md       # 核心规则
│   │   ├── 02_agents_contract.md  # Agent 契约
│   │   ├── 03_director_file_reading_ban.md
│   │   ├── 04_phase_5.5_anti_fraud.md
│   │   ├── 05_phase_0.5_model_quality_gate.md
│   │   ├── 06_image_naming_standards.md
│   │   ├── 07_time_validator_strict_mode.md
│   │   ├── 08_phase_5_parallel_workflow.md
│   │   ├── 09_time_validator_enhanced_analysis.md
│   ├── 10_phase5b_error_monitoring.md
│   │   ├── 11_emergency_delegation.md
│   │   ├── 12_phase45_revalidation.md
│   │   ├── 13_editor_feedback_enforcement.md
│   │   ├── 14_code_translator_idealistic_mode.md
│   │   ├── 15_director_time_validator_handoff.md
│   │   ├── 16_model_design_expectations.md
│   │   ├── 17_validator_advisor_brief_format.md
│   │   ├── 18_modeler_time_pressure_protocol.md
│   │   ├── 19_re_verification_strict_standards.md
│   │   ├── 20_all_agents_reverify_protocol.md
│   │   ├── director_systematic_role.md
│   │   ├── modeler_anti_simplification.md
│   │   ├── reader_mandatory_requirements.md
│   │   ├── time_validator_spec.md
│   │   └── agents/               # Agent 文档
│   │
│   ├── v2-6-0/                   # v2.6.0 架构
│   │
│   └── v3-0-0/                   # v3.0.0 架构（当前）
│       ├── 00_ARCHITECTURE.md    # 总体架构
│       ├── 01_SYSTEM_COMPARISON.md # 系统对比
│       ├── 02_LLM_MM_AGENT_ARCHITECTURE.md # LLM-MM-Agent 架构
│       ├── 03_MCM_KILLER_ARCHITECTURE.md # MCM-Killer 架构
│       ├── 04_PROTOCOLS_SUMMARY.md # 协议总结
│       ├── 05_AGENT_SPECIFICATIONS.md # Agent 规范
│       ├── 06_PHASE_WORKFLOW.md    # 阶段工作流
│       ├── 07_VALIDATION_GATES.md # 验证门控
│       ├── 08_OUTPUT_STRUCTURE.md    # 输出结构
│       ├── draft/                # 草稿文档
│       │   ├── LLM-MM-Agent/   # LLM-MM-Agent 详细文档
│       │   └── MCM-Killer/     # MCM-Killer 详细文档
│       ├── 10_director_file_reading_ban.md
│       ├── 11_time_validator_strict_mode.md
│       ├── 12_phase_5_parallel_workflow.md
│       ├── 13_time_validator_enhanced_analysis.md
│       ├── 14_code_translator_idealistic_mode.md
│       ├── 15_director_time_validator_handoff.md
│       ├── 16_model_design_expectations.md
│       ├── 17_validator_advisor_brief_format.md
│       ├── 18_phase5b_error_monitoring.md
│       ├── 19_emergency_delegation.md
│       ├── 20_phase45_revalidation.md
│       ├── 30_WORKSPACE_CONFIGURATION.md
│       ├── README.md
│       └── m-orientation/         # 材料和指南
│
├── 📁 workspace/ ⭐⭐⭐⭐⭐ 竞赛工作空间
│   └── 2025_C/                   # 2025 C 题工作区
│       ├── CLAUDE.md             # 工作区指导
│       ├── problem/              # 题目文件
│       ├── docs/                 # 文档
│       ├── model/                # 模型设计
│       ├── implementation/       # 实现代码
│       │   ├── .venv/            # 虚拟环境
│       │   ├── code/             # 代码文件
│       │   ├── data/             # 数据文件
│       │   └── logs/             # 日志文件
│       └── paper/                # 论文输出
│
├── 📁 experiments/ ⭐⭐⭐⭐ 实验记录
│   ├── trail-0102/
│   ├── trail-Istanbul/
│   ├── trail2-2-0-0102c/
│   ├── trail2-2-0-0103a/
│   └── [实验复盘点]
│
├── 📁 problems and results/ ⭐⭐ 历年题目和结果
│   ├── 2020/ - 2025/           # 2020-2025 年
│   └── [PDF 题目和结果文件]
│
├── 📁 student paper/ ⭐⭐ 学生论文
│   ├── 2020/ - 2024/
│   └── [历年优秀论文 PDF]
│
└── 📁 LaTeX__Template_for_MCM_ICM/ ⭐⭐⭐ LaTeX 模板
    ├── mcmthesis.cls            # 文档类
    ├── mcmthesis-demo.tex       # 示例
    ├── code/                    # 代码示例
    └── figures/                 # 图片资源
```

---

## 文档导航

### 架构版本文档

#### v2.5.0 架构（关键版本）⭐⭐⭐⭐⭐

- **00_CHANGES.md** - 变更日志
- **01_README.md** - 架构说明
- **02_core.md** - 核心机制
- **03_workflow.md** - 工作流设计
- **04_validation.md** - 验证设计
- **05_consultation.md** - 咨询设计
- **06_agents.md** - Agent 规范（13 个 Agent）
- **07_anti_laziness.md** - 反懒惰机制

#### v2.5.1 - v2.5-7 系列迭代版本

每个版本都包含：
- 核心规则更新
- Agent 契约调整
- 新增协议（如 director_file_reading_ban, time_validator_strict_mode）
- 增强功能（如 parallel_workflow, enhanced_analysis）

#### v3-0.0 架构（当前版本）⭐⭐⭐⭐⭐

- **00_ARCHITECTURE.md** - 总体架构
- **01_SYSTEM_COMPARISON.md** - 系统对比（LLM-MM-Agent vs MCM-Killer）
- **02_LLM_MM_AGENT_ARCHITECTURE.md** - LLM-MM-Agent 架构详解
- **03_MCM_KILLER_ARCHITECTURE.md** - MCM-Killer 架构详解
- **04_PROTOCOLS_SUMMARY.md** - 18 阶段协议总结
- **05_AGENT_SPECIFICATIONS.md** - 14 个 Agent 规范
- **06_PHASE_WORKFLOW.md** - 18 阶段工作流详解
- **07_VALIDATION_GATES.md** - 7 个验证门控详解
- **08_OUTPUT_STRUCTURE.md** - 输出结构详解

---

## 关键组件

### 14 个专业 Agent

1. **Reader** - 读取题目和数据
2. **Researcher** - 文献研究
3. **Modeler** - 模型设计
4. **Code Translator** - 代码翻译
5. **Model Trainer** - 模型训练
6. **Validator** - 验证模型
7. **Visualizer** - 数据可视化
8. **Writer** - 论文写作
9. **Summarizer** - 内容总结
10. **Editor** - 论文编辑
11. **Advisor** - 咨询顾问
12. **Director** - 总协调员
13. **Feasibility Checker** - 可行性检查
14. **Time Validator** ⭐⭐⭐⭐⭐ v2.5.7 - 时间验证器（严格模式）

### 18 阶段工作流

Phase 0 → Phase 0.5 → Phase 1 → Phase 1.5 → Phase 2 → Phase 3 → Phase 4 → Phase 4.5 → Phase 5 → Phase 5.5 → Phase 6 → Phase 6.5 → Phase 7 → Phase 7.5 → Phase 8 → Phase 9 → Phase 9.5 → Phase 10

### 7 个验证门控

- Phase 0.5: Model Quality Gate
- Phase 1.5: Design Validation
- Phase 2: Feasibility Check
- Phase 3: Model Validation
- Phase 4: Code Validation
- Phase 5: Chart Validation
- Phase 6: Paper Validation

---

## 核心特性

1. **严格的顺序执行**：18 个阶段必须按顺序执行
2. **验证门控机制**：7 个验证门确保质量
3. **反懒惰机制**：防止 Agent 偷懒（如 Director 禁止读取文件）
4. **时间压力**：Time Validator 强制时间限制
5. **并行工作流**：Phase 5 部分阶段可并行

---

**文档版本**: v1.0
**创建时间**: 2026-01-24
**架构版本**: v3.0.0
**总文档数**: 100+ 文件
