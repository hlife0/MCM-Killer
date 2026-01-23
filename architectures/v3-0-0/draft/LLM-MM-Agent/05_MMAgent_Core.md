# MMAgent: Core 模块

> 绝对路径：`D:/migration/MCM-Killer/architectures/v3-0-0/draft/LLM-MM-Agent/05_MMAgent_Core.md`
> **重要程度**: ⭐⭐⭐⭐ 核心组件
> **迁移价值**: **中** - 高级分析模块可复用

本目录（`MMAgent/core/`）包含 LLM-MM-Agent 系统的核心分析组件，实现了高级推理、批评、策略制定等功能。这些模块提供了超越基础 Agent 的能力，包括溯因推理、红队测试、研究策略制定等。核心组件使用 FSM（有限状态机）模式来管理复杂的推理流程。

---

## 核心文件

### `abduction_engine.py` ⭐⭐⭐⭐⭐⭐
**溯因引擎**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/core/abduction_engine.py`。实现溯因推理，从观察结果反推最可能的解释。

**功能**：
- 观察现象
- 生成可能解释
- 评估解释合理性
- 选择最佳解释

**迁移价值**：溯因推理模式可以用于任何需要诊断分析的系统，特别是错误诊断、根因分析等场景。

---

### `red_team_critic.py` ⭐⭐⭐⭐⭐⭐
**红队批评家**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/core/red_team_critic.py`。实现红队测试，对生成的方案进行批评和挑刺。

**功能**：
- 分析方案的弱点
- 提出潜在攻击
- 评估方案鲁棒性
- 提供改进建议

**迁移价值**：红队测试模式可以用于任何需要质量评估和风险识别的系统。

---

### `research_strategist.py` ⭐⭐⭐⭐⭐⭐
**研究策略家**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/core/research_strategist.py`。制定研究策略，决定下一步的研究方向。

**功能**：
- 分析当前进度
- 识别关键问题
- 制定下一步计划
- 优先级排序

**迁移价值**：策略制定模式可以用于任何需要动态规划的系统。

---

### `research_strategist_fsm.py` ⭐⭐⭐⭐⭐⭐
**研究策略 FSM**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/core/research_strategist_fsm.py`。研究策略的有限状态机实现。

**功能**：
- 定义状态转换规则
- 管理策略状态
- 处理状态转换事件

**迁移价值**：FSM 模式是管理复杂流程的经典模式。

---

### `state_manager.py` ⭐⭐⭐
**状态管理器**，绝对路径：`D:/migration/clean version/LLM-MM-Agent/MMAgent/core/state_manager.py`。管理系统状态，提供状态查询和更新接口。

**功能**：
- 状态存储
- 状态查询
- 状态更新
- 状态转换验证

**迁移价值**：状态管理模式是系统架构的基础组件。

---

**文档版本**: v1.0
**最后更新**: 2026-01-24
