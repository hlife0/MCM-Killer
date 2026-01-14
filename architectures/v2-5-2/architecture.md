# v2.5.2 系统架构

> **权威架构定义** — 所有 Agent prompts 都应该从这份文档派生。
> **版本**: v2.5.2
> **日期**: 2026-01-14
> **核心改进**: **[v2.5.2 NEW] 自适应Phase跳转机制 (Adaptive Phase Jump)**

---

## 文档关系

| 文档 | 职责 |
|------|------|
| `retrospective.md` | 分析 v2.4.2 和 v2.5.0 的问题和改进 |
| `methodology.md` | 定义设计原则和方法论 |
| **`phase_jump_design.md`** | **[v2.5.2 NEW] Phase跳转机制详细设计** |
| **`architecture.md`（本文档）** | 定义具体架构和 Agent 契约 |

阅读顺序：retrospective → methodology → phase_jump_design → architecture

> ⚠️ **本文档是权威**。当 Agent prompt 与本文档冲突时，以本文档为准。

---

## 版本历史

| 版本 | 日期 | 关键变更 |
|------|------|----------|
| v2.4.0 | 2026-01-02 | 验证门机制、多 Agent 协作 |
| v2.4.1 | 2026-01-04 | 完整性强制令、数据完整性标准 |
| **v2.4.2** | **2026-01-05** | **返工重新验证、资源利用原则、质量门槛提升** |
| **v2.5.0** | **2026-01-07** | **架构分层化、反偷懒机制、Phase 5两阶段训练** |
| **v2.5.1** | **2026-01-10** | **合并 v2.4.2 和 v2.5.0 所有改进** |
| **v2.5.2** | **2026-01-14** | **[NEW] 自适应Phase跳转、回退建议机制、增量修复** |

---

## 一、文档说明

这份文档是 v2.5.2 的**具体架构定义**，完整继承 v2.5.1 的所有内容，并在 v2.5.1 基础上新增了以下核心内容：

1. **v2.5.1 完整内容**（保持不变）：
   - 系统的核心规则（唯一定义处）
   - 每个 Agent 的契约（输入/输出/触发/职责）
   - 目录结构契约
   - 命名规范
   - 验证方法
   - 反偷懒机制（v2.5.0）
   - Phase 5 两阶段训练（v2.5.0）
   - Token 监控和检查点（v2.5.0）
   - 返工必须重新验证（v2.4.2）
   - 资源利用原则（v2.4.2）
   - 质量门槛原则（v2.4.2）

2. **v2.5.2 新增内容**（见后续[v2.5.2 NEW]标记章节）：
   - Phase跳转协议（详见第四节）
   - Phase依赖图（详见第四节）
   - Rewind Recommendation机制（详见第五节）
   - Director的跳转决策逻辑（详见第十一节）
   - 自适应工作流（详见第十二节）

**使用方式**：创建或修改 Agent prompt 时，应该引用这份文档中的定义，而不是自己发明规则。


---

## 二、v2.5.2 核心改进概述 [v2.5.2 NEW]

### 2.1 问题诊断：为什么v2.5.1需要Phase跳转能力

**v2.5.1的局限**：
1. **线性执行**：Phase必须按顺序执行（0→1→2→...→10）
2. **被动验证**：问题只能在Validation Gate被发现
3. **返工固定**：返工总是返回同一Agent，而不是可能追溯到上游
4. **跳转受限**：不支持"向前跳过"或"向后回退多个Phase"

**实际场景中的问题**：
- Phase 4（Code）发现模型设计有缺陷 → 应该回Phase 1，但只能返工Phase 4
- Phase 7（Paper）发现数据异常 → 应该回Phase 3，但只能返工Phase 7
- Phase 5（Training）发现特征不足 → 应该回Phase 3，但只能返工Phase 5

### 2.2 v2.5.2 的解决方案

#### 核心机制：Agent驱动的Phase跳转

```
传统流程（v2.5.1）:
Phase 1 → Phase 2 → Phase 3 → Phase 4 → [Validation Gate发现太晚] → 返工Phase 4

新流程（v2.5.2）:
Phase 1 → Phase 2 → Phase 3 → Phase 4
    ↓ [Agent发现上游问题]
Rewind Recommendation → 回到Phase 1/2/3 → 修复后继续
```

#### 三大新特性

1. **Rewind Recommendation（回退建议）**
   - Agent在执行中发现上游问题时，可以主动建议回退
   - 通过`rewind_recommendation_{i}.md`文档提交建议
   - Director分析后决定是否接受回退

2. **Phase Dependency Graph（Phase依赖图）**
   - 明确定义哪些Phase之间可以跳转
   - 支持向后回退（Rewind）
   - 保护关键依赖，防止破坏已有成果

3. **Incremental Fix（增量修复）**
   - 回退后保留已有成果
   - 只修复受影响的部分
   - 避免完全重做

### 2.3 向后兼容性保证

**v2.5.2 完全继承 v2.5.1**：
- ✅ v2.5.1的所有规则保持有效
- ✅ v2.5.1的所有流程保持可用
- ✅ v2.5.1的所有Agent契约保持不变
- ✅ v2.5.1的所有文档格式保持不变
- ✅ v2.5.2的新特性是**可选的增强**

如果Agent从不使用Rewind功能，系统行为与v2.5.1完全一致。

---

## 三、系统核心规则

（本节完整继承自v2.5.1，所有细节保持不变）

## 二、系统核心规则

### 2.1 参与者

| 角色 | 数量 | 说明 |
|------|------|------|
| Director | 1 | **系统主 Agent**，由 CLAUDE.md 配置，负责编排其他 Agent |
| Agent | 13 | 专业化执行者，各有专门职责 |

**Agent 列表**（规范名称）：
1. `director` (编排者，非普通 Agent)
2. `reader`
3. `researcher`
4. `modeler`
5. `feasibility_checker`
6. `data_engineer`
7. `code_translator`
8. `model_trainer`
9. `validator`
10. `visualizer`
11. `writer`
12. `summarizer`
13. `editor`
14. `advisor`

> ⚠️ 在所有文档中必须使用上述规范名称，不得使用别名（如 `Coder`）。

### 2.2 数据权威等级

```
Level 1: 代码输出 (CSV/PKL) — 最高权威，其他文件必须与之一致
Level 2: Agent 报告 (MD)   — 必须反映 Level 1 的内容
Level 3: 论文文档 (TEX)    — 必须与 Level 1 一致，冲突时以 Level 1 为准
```

### 2.3 文件系统规则

**绝对禁止**：
- ❌ 修改 `output/` 以外的任何文件
- ❌ 写入 `reference_papers/`, `latex_template/`, `.claude/`
- ❌ 使用 `_final`, `_backup`, `_old` 等后缀

**版本控制**：
- ✅ 所有输出文件必须带版本号：`{name}_{i}.{ext}`（详见第三节）
- ✅ 每次写文件后更新 `VERSION_MANIFEST.json`

### 2.4 数据完整性标准 (v2.4.1)

鉴于 v2.4.0 实验中出现的严重数据污染，v2.4.1 引入严格的数据完整性标准：
- **标量原则**：CSV/Excel 输出必须仅包含标量值 (int, float, string, boolean)。**绝对禁止**存储序列化对象（List, Dict, Numpy Object）。
- **类型安全**：生成数据的代码必须包含 `check_data_quality()` 函数，输出前断言数据类型。
- **自我修正**：Data Engineer 必须在提交前运行自检，发现非标量列立即修复。

### 2.5 完整性强制令 (Completeness Mandate) (v2.4.1 + v2.5.0)

鉴于 v2.4.0 实验中出现的"简化"错误和 v2.5.0 实验中的"跳过"问题，v2.5.1 确立以下绝对规则：

- **禁止简化 (No Simplification)**：系统必须严格执行 10 个阶段的所有步骤。
- **禁止跳过 (No Skipping)**：即使代码通过测试，Validation Gate 也必须完整执行。
- **质量优先 (Quality > Efficiency)**：当 Token 接近限制时，**暂停并请求用户干预**（如轮换上下文），绝不允许为了省 Token 而降低输出质量、合并步骤或生成"摘要版"报告。
- **自动降级 (v2.5.0)**：当资源不足时，**自动降级**而不是跳过（见2.11节）

### 2.6 返工必须重新验证 (Rework Must Revalidate) (v2.4.2)

鉴于 v2.4.1 实验中出现的"返工后跳过验证"错误，v2.4.2 确立以下规则：

- **强制重新验证**：如果 Validation Gate 返回 REJECTED，返工完成后**必须**重新触发同一 Gate
- **不得跳过**：Director 没有任何理由可以跳过重新验证（包括时间紧迫、Token 不足）
- **循环次数**：每个 Gate 最多循环 3 次（REJECTED → 返工 → 重新验证），超过后暂停请求用户干预

> ⚠️ **这是 v2.4.2 的核心改进**。v2.4.1 实验失败的主要原因就是返工后跳过了重新验证。

### 2.7 资源利用原则 (Resource Utilization Principles) (v2.4.2)

Agent 应当积极利用项目提供的资源，而非仅凭自身知识工作。

#### 2.7.1 参考文献资源

**目录**：`./reference_papers/`

**适用 Agent**：
- `researcher`：**强烈鼓励**浏览参考论文，学习相关领域的方法论和最佳实践
- `modeler`：参考类似问题的建模方法
- `summarizer`：学习高质量 MCM 论文的摘要写法和结构
- `writer`：参考论文的写作风格和组织方式
- `advisor`：对比论文质量与参考论文

**原则**：
- ✅ 主动阅读和引用参考文献
- ✅ 从中汲取方法论灵感
- ✅ 引用时注明来源
- ❌ 不得直接复制内容

#### 2.7.2 LaTeX 模板资源

**目录**：`./latex_template/`

**适用 Agent**：`writer`

**强制规则**：

1. **禁止自创 LaTeX 文档**：
   - 必须将 `./latex_template/` 中的模板**复制**到 `output/paper/`
   - 在复制的模板基础上展开工作
   - ❌ 禁止从零创建新的 `.tex` 文件
   - ❌ 禁止修改模板的格式结构（如字体、页边距、章节样式）

2. **必须保证编译通过**：
   - 每次修改后必须尝试编译
   - 如果编译失败，首先检查是否是内容错误（自行修复）
   - 如果是**环境问题**（如字体缺失、包缺失）：
     - **必须通过 Consultation 协议请求 `feasibility_checker` 处理**
     - ❌ 禁止自行安装包或修改系统环境
     - ❌ 禁止使用 "no-font" 简化或其他绕过方案
     - ❌ 禁止降级模板要求

3. **文档长度要求**：
   - **最低 23 页**（不含附录）
   - 低于 23 页视为**不合格**，必须扩充内容
   - 验证者应检查页数，不足时返回 REJECTED

**检查清单**（writer 完成后自检）：
- [ ] 模板是从 `latex_template/` 复制的，不是自创的
- [ ] 编译通过，无错误
- [ ] 页数 >= 23 页
- [ ] 格式与原模板一致

#### 2.7.3 网络搜索

**适用 Agent**：`researcher`

**鼓励行为**：
- ✅ 搜索相关学术论文和方法
- ✅ 查找类似问题的解决方案
- ✅ 了解领域最新进展
- ❌ 不得依赖不可靠来源

### 2.8 质量门槛原则 (Quality Gate Principles) (v2.4.2)

Agent 应提高质量标准，严格拒绝不合格的产出。

#### 2.8.1 Modeler 严格标准

`modeler` 在 CODE Validation Gate 中应该：
- **严格审查**代码是否真正实现了设计的模型
- **拒绝**"能运行但不符合设计"的代码
- **拒绝**简化了核心数学逻辑的实现
- 发现严重偏差时，明确返回 REJECTED 并说明原因

> 不要因为"代码能跑"就放过质量问题。

#### 2.8.2 Advisor 独立验证（局外人视角）

> **核心原则**：你是"局外人"而非"参与者"。你不是这个团队的一员，你是来审查这个团队的。

**心态要求**：

1. **所有其他 Agent 都不可信**：
   - 不要相信 Director 的摘要
   - 不要相信 Validator 的"通过"报告
   - 不要相信任何 Agent 声称的数字
   - **假设这个比赛队伍可能有很多离谱的东西**

2. **以质疑者身份审查**：
   - 对每一个数据，问"这个数字对吗？"
   - 对每一个结论，问"真的是这样吗？"
   - **不要被漂亮的报告唬住**——报告写得再好，数据可能完全是错的

3. **独立验证**：
   - **亲自读取**预测文件（`predictions_*.csv`），不依赖任何人的汇报
   - **亲自检查**论文中的数字是否与文件一致
   - **亲自上网搜索**验证预测是否符合现实
     - 例如：搜索"USA Olympics 2024 medal count"，对比预测是否合理
     - 例如：搜索"host country Olympic advantage"，验证主办国效应方向

4. **常识 Sanity Check**：
   - 主办国预测应该高于往年，不是低于
   - 强国预测应该在历史范围附近，不应该暴跌 80%+
   - 预测区间的上界不应该小于均值

5. **与参考论文对比**：
   - **必须阅读几篇 `reference_papers/`** 中的论文
   - 对比本项目的论文质量与参考论文
   - 问自己：这份论文能和参考论文放在一起吗？
   - 如果差距太大，不要乐观，该 REJECT 就 REJECT

6. **极其严苛的高标准**：
   - **不要对拿到的东西过于乐观**——假设里面藏着问题
   - **敢于要求返工**——发现问题就 REJECT，不要"差不多就行"
   - **高标准高要求**——平庸的作品不值得高分
   - 宁可被认为苛刻，也不要让垃圾通过

**如果发现问题**：
- 立即降低评分（问题越多评分越低）
- 明确列出每个发现的问题
- 不要"为团队着想"而放过问题
- **敢于返回 REJECTED** 并要求修复

> ⚠️ **记住**：你的工作是找问题，不是找理由通过。一个诚实的 D 比一个虚假的 A+ 更有价值。

#### 2.8.3 Sanity Check 思维

所有 Agent 在验证时应具备 Sanity Check 思维：
- **常识判断**：预测结果是否符合常识？（如：主办国应该比平时表现更好）
- **历史对比**：与历史数据对比是否合理？
- **逻辑一致**：不同文件之间的数据是否一致？

### 2.9 输出一致性原则 (Output Consistency Principles) (v2.4.2)

鉴于 v2.4.1 实验中出现的数据不一致问题，v2.4.2 提醒所有 Agent：

- **唯一标识**：国家、变量等应使用统一的标识格式（NOC 代码或全名，不可混用）
- **避免覆盖**：不同模型/任务的输出应使用不同的文件名
- **验证日志-文件一致**：训练完成后，应检查日志中的关键数字与保存的文件内容一致

### 2.10 预测 Sanity Check (Prediction Sanity Check) (v2.4.2)

Phase 5 输出后必须执行自动化 Sanity Check，任一检查失败 → 阻塞进入 Phase 6：

**检查项**：
1. 无重复 NOC/国家名
2. 无已解散国家
3. 强国预测在合理范围（基于历史）
4. 主办国预测 > 非主办时期平均
5. Gold 预测 < Total 预测
6. Median 不应全为 0
7. 预测区间有效（PI_97.5 >= Mean >= PI_2.5）

### 2.11 反偷懒机制 (Anti-Laziness Mechanism) (v2.5.0)

鉴于 v2.5.0 之前实验中出现的"跳过 Phase 5"问题，v2.5.1 确立以下规则：

#### 2.11.1 强制执行规则

1. **禁止跳过（No Skipping）**
   - 每个阶段必须执行
   - 遇到资源限制时自动降级
   - 禁止 AI 自主决定跳过

2. **自动降级（Automatic Degradation）**
   - Phase 5 根据预计时间自动选择 Tier
   - 任何 Tier 都必须产生有效输出
   - 不允许输出 TODO 或占位符

3. **无需人工干预（No Human Intervention）**
   - AI 自动做出所有决策
   - 不请求用户指示是否跳过
   - 确保流畅执行到结束

4. **检查点机制（Checkpoint）**
   - 每个阶段结束保存状态
   - Token 接近限制时自动切换到轻量模式

#### 2.11.2 Phase 5 改进（两阶段训练）

**Phase 5A: 快速验证（MANDATORY, ≤30 min）**
- ✅ 必须执行
- 使用减少样本/迭代
- 确保代码可运行
- 输出：`results_quick_{i}.csv`

**Phase 5B: 完整训练（OPTIONAL, 4-6 hours）**
- ⚠️ 可选执行
- 完整 HMC 采样
- 输出：`results_{i}.csv`

**绝对禁止**：
- ❌ 完全跳过 Phase 5
- ❌ 理由"时间不足"就跳过
- ✅ 必须至少 Phase 5A
- ✅ 必须产生有效输出

### 2.12 Token 监控和检查点 (v2.5.0)

#### 2.12.1 Token 监控机制

**监控时机**：每个 Phase 结束时检查 Token 使用并记录到检查点。

**阈值和行动**：

| Token 使用率 | 行动 |
|-------------|------|
| < 80% | 正常执行，记录到检查点 |
| 80% - 90% | 发出警告，考虑压缩非关键输出 |
| > 90% | **必须**请求用户干预 |

#### 2.12.2 检查点机制

**保存时机**：每个 Phase 结束时保存到 `output/.checkpoint_phase{i}.json`

**检查点格式**：
```json
{
  "phase": 5,
  "completed_at": "2026-01-07 12:30:00",
  "token_usage": 95000,
  "token_percentage": 47.5,
  "outputs": ["implementation/data/results_quick_1.csv"],
  "next_phase": 6,
  "status": "5A completed, 5B skipped"
}
```


---

## 四、Phase依赖图与跳转规则 [v2.5.2 NEW]

### 4.1 Phase依赖图（详见 phase_jump_design.md）

完整的Phase依赖关系和允许的Rewind路径，请参考：
**architectures/v2-5-2/phase_jump_design.md**

核心要点：
- 每个Phase可以Rewind到特定的上游Phase
- Rewind必须基于依赖图规则
- Director根据代价收益分析决策

### 4.2 Agent的Rewind权限

| Agent | 可以Rewind到 | 触发条件 |
|-------|-------------|---------|
| **code_translator** | Phase 1, 3 | 模型设计错误/特征不足 |
| **model_trainer** | Phase 1, 3, 4 | 模型方法错误/特征问题/代码问题 |
| **writer** | Phase 5 | 结果不合理 |
| **advisor** | Phase 1, 5 | 模型/结果方法论问题 |

### 4.3 何时可以建议Rewind

**Agent可以建议Rewind（向后回退）**：
- ✅ 发现上游Phase的产出物有根本性缺陷
- ✅ 当前Phase无法继续，原因是上游问题
- ✅ 修复上游问题比在当前Phase补救更高效

**详见**: phase_jump_design.md 第五节

---

## 五、Phase跳转协议 [v2.5.2 NEW]

### 5.1 Agent发起Rewind建议

详见 phase_jump_design.md 第五节。

**协议格式**：
Director，我在Phase {current}执行中，发现需要Rewind到Phase {target}。

[包含问题描述、根本原因、影响分析、修复方案、紧急程度]

**Rewind Recommendation文档**：docs/rewind/rewind_rec_{i}_{from}_{to}.md

### 5.2 Director处理Rewind建议

详见 phase_jump_design.md 第五节。

**决策流程**：
1. 验证建议有效性
2. 检查依赖图
3. 分析代价收益
4. 考虑时机
5. 最终决策

### 5.3 执行Rewind

详见 phase_jump_design.md 第五节。

**步骤**：
1. Director确认Rewind
2. 更新VERSION_MANIFEST.json
3. 识别保留文件
4. 跳转到目标Phase
5. 调用Agent
6. 重新执行受影响Phase

---


## 三、版本管理契约

### 3.1 核心原则

1. **所有输出文件必须带版本号**：`{name}_{i}.{ext}`（`{i}` 从 1 开始）
2. **VERSION_MANIFEST.json 是唯一的版本状态记录**
3. **禁止使用语义模糊的后缀**：`_final`, `_backup`, `_old`, `_new`

### 3.2 版本号规则

| 文件类型 | 命名格式 | 示例 |
|---------|---------|------|
| Markdown 文档 | `{name}_{i}.md` | `problem_requirements_1.md`, `model_design_2.md` |
| Python 脚本 | `{name}_{i}.py` | `model_1.py`, `data_prep_2.py` |
| 数据文件 | `{name}_{i}.pkl/csv` | `features_1.pkl`, `results_3.csv` |
| 图表 | `fig_{name}_{i}.png/pdf` | `fig_trend_1.png` |
| 论文 | `paper_{i}.tex/pdf` | `paper_1.tex` |
| Agent 汇报 | `{agent}_{i}.md` | `reader_1.md`, `modeler_2.md` |
| 快速结果 | `results_quick_{i}.csv` | Phase 5A 输出 |

**特殊情况**：
- `problem_full.md` - 不带版本号（一次性生成）
- `figure_index.md` - 不带版本号（持续更新）
- `.venv/` - 不带版本号（环境目录）

### 3.3 VERSION_MANIFEST.json

**位置**：`output/VERSION_MANIFEST.json`

**结构**：

```json
{
  "created_at": "2026-01-04 00:00:00",
  "last_updated": "2026-01-04 01:30:00",

  "files": {
    "problem/problem_requirements": {
      "current": 2,
      "history": [
        {"version": 1, "created_at": "2026-01-04 00:10:00", "created_by": "reader"},
        {"version": 2, "created_at": "2026-01-04 00:45:00", "created_by": "reader"}
      ]
    }
  },

  "agent_calls": {
    "reader": 2,
    "researcher": 1,
    "modeler": 1,
    "data_engineer": 3
  },

  "consultation_count": 5,
  "validation_count": 12
}
```

### 3.4 Agent 操作规范

**写文件前**：
1. 读取 `VERSION_MANIFEST.json`
2. 查找该文件的当前版本号
3. 版本号 +1 作为新版本号

**写文件后**：
1. 更新 manifest 中该文件的 `current` 版本号
2. 在 `history` 数组中追加新版本记录
3. 更新 `last_updated` 时间戳
4. 更新 `agent_calls` 中该 Agent 的调用次数

**读文件时**：
1. 读取 `VERSION_MANIFEST.json`
2. 查找该文件的当前版本号
3. 读取 `{name}_{current}.{ext}`

**禁止**：
- ❌ 直接硬编码文件名（如 `features_1.pkl`）
- ❌ 覆盖已有版本文件
- ❌ 不更新 manifest 就写文件

### 3.5 版本回退

如果需要回退到旧版本：
1. 修改 manifest 中的 `current` 为目标版本号
2. **不要**删除任何版本文件
3. 在 `history` 中添加回退记录

---

## 四、目录结构契约

### 4.0 完整工作目录结构 (v2.4.2 + v2.5.0)

工作目录包含 output/ 以及多个**只读资源目录**，Agent 应充分利用这些资源。

```
workspace/2025_C/                 # 工作目录根
│
├── CLAUDE.md                     # Director Agent 系统提示词
├── .claude/                      # Agent 提示词目录
│   └── agents/                   # 各 Agent 的系统提示词（自包含）
│       ├── director.md
│       ├── reader.md
│       ├── researcher.md
│       └── ...
│
├── 2025_MCM_Problem_C.pdf        # [只读] 原始问题 PDF
├── 2025_Problem_C_Data/          # [只读] 原始数据目录
│   └── *.csv                     # 提供的数据文件
├── 2025_Problem_C_Data.zip       # [只读] 数据压缩包
│
├── reference_papers/             # [只读] 参考论文目录
│   └── *.pdf                     # O-Prize 及其他优秀论文
│                                 # ** researcher, modeler, summarizer, advisor 应阅读 **
│
├── latex_template/               # [只读] LaTeX 模板目录
│   ├── mcmthesis.cls             # 模板类文件
│   ├── mcmthesis.tex             # 模板主文件
│   └── figures/                  # 模板图片
│                                 # ** writer 必须复制此模板到 output/paper/ **
│
└── output/                       # [可写] Agent 输出目录（见下文详细结构）
```

**资源使用指南**：

| 资源目录 | 权限 | 适用 Agent | 用途 |
|---------|------|-----------|------|
| `2025_MCM_Problem_C.pdf` | 只读 | reader | 提取问题需求 |
| `2025_Problem_C_Data/` | 只读 | data_engineer | 原始数据处理 |
| `reference_papers/` | 只读 | researcher, modeler, summarizer, advisor | 学习方法论、摘要写法、质量标准 |
| `latex_template/` | 只读 | writer | **必须复制到 output/paper/ 使用** |
| `output/` | 可写 | 所有 Agent | 输出所有产出物 |

**架构文件位置**（仅前期协调参考，工作时不访问）：
```
architectures/                    # 架构定义（前期协调，设计参考）
└── v2-5-1/
    ├── architecture.md           # 权威架构定义（本文档）
    ├── methodology.md            # 设计原则和方法论
    ├── retrospective.md          # 版本回顾
    └── agents/                   # Agent 模板
```

> **关键原则**（v2.5.0）：
> - `architectures/` = 设计协调文档（开发时参考）
> - `workspace/.claude/agents/` = 工作执行指南（运行时使用）
> - Agent 文件必须**自包含**，不引用架构
> - 工作时 AI 只读取 `agents/*.md`，不访问 `architectures/`

---

### 4.1 output/ 输出目录结构

```
output/
├── VERSION_MANIFEST.json        # 版本控制元数据
├── .checkpoint_phase{i}.json    # 检查点文件（v2.5.0）
│
├── problem/                     # 问题相关
│   ├── original/                # 原始题目文件（copy）
│   ├── problem_full.md          # 完整题目 Markdown 版
│   └── problem_requirements_{i}.md
│
├── docs/                        # 文档（协作相关）
│   ├── consultation/            # Agent 间咨询
│   ├── validation/              # 验证报告
│   └── report/                  # Agent → Director 汇报
│
├── model/                       # 模型设计
│   ├── research_notes_{i}.md
│   ├── model_design_{i}.md
│   └── feasibility_{i}.md
│
├── implementation/              # 实现相关
│   ├── .venv/                   # Python 虚拟环境
│   ├── data/                    # 数据文件
│   │   ├── features_{i}.pkl
│   │   ├── results_quick_{i}.csv  # Phase 5A 输出（v2.5.0）
│   │   └── results_{i}.csv        # Phase 5B 输出
│   ├── code/                    # 代码
│   └── logs/                    # 日志
│
└── paper/                       # 论文相关
    ├── (从 latex_template/ 复制的模板文件)
    ├── paper_{i}.tex
    ├── figures/
    └── summary/
```

> **注意**：`{i}` 表示该文件的第几个版本/第几次调用，从 1 开始。

---

## 五、协作契约

本节定义 Agent 间协作的三种机制的**契约**（接口与格式）。

> **注意**：本节只定义"是什么"，不定义"何时用"。具体的调用时机在执行流程中定义。

### 5.1 核心原则

1. **单线程执行**：同一时间只有一个 Agent 工作
2. **所有协作 Blocking**：发起协作后立即处理，无异步
3. **Director 中转**：Agent 间不直接通信，通过 Director 协调
4. **文件记录**：所有协作写入 `docs/` 目录

### 5.2 Consultation（咨询）

**定义**：Agent 在执行中向其他 Agent 请求信息。

**特点**：
- 双向：A → B → A
- Blocking：发起后立即处理

**文件路径**：`docs/consultation/{i}_{from}_{to}.md`

**格式**：
```markdown
# Consultation #{i}: {from} → {to}

| 字段 | 值 |
|------|------|
| 编号 | {i} |
| 发起方 | {from} |
| 接收方 | {to} |
| 时间 | {timestamp} |
| 状态 | PENDING / ANSWERED

---

## 问题

{咨询内容}

---

## 回复

{回复内容}
```

### 5.3 Validation（验证）

**定义**：对产出物进行多视角质量检查。

**特点**：
- **多人参与**：每个 Stage 由多个 Agent 从不同角度验证
- **独立判断**：每个验证者只能根据自己知识判断
- **禁止咨询**：Validation 期间不允许发起 Consultation
- **并行执行**：Director 可并行调用多个验证者

**验证结果**：
- ✅ **APPROVED** → 通过
- ⚠️ **CONDITIONAL** → 有条件通过
- ❌ **REJECTED** → 未通过，需修复

**文件路径**：`docs/validation/{i}_{stage}_{agent}.md`

**格式**：
```markdown
# Validation #{i}: {stage} by {agent}

| 字段 | 值 |
|------|------|
| 编号 | {i} |
| 阶段 | {stage} |
| 验证者 | {agent} |
| 时间 | {timestamp} |
| 判定 | ✅ APPROVED / ⚠️ CONDITIONAL / ❌ REJECTED

---

## 验证视角

{该 Agent 从什么角度验证}

---

## 检查结果

| # | 检查项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | {item} | ✅/⚠️/❌ | {note} |

---

## 问题列表（如有）

| # | 问题 | 严重程度 | 建议 |
|---|------|---------|------|
| 1 | {issue} | HIGH/MEDIUM/LOW | {suggestion} |

---

## 结论

{验证结论}
```

### 5.4 Report（汇报）

**定义**：Agent 完成调用后向 Director 汇报。

**特点**：
- 单向：Agent → Director
- 强制：每次调用后必须汇报
- 私密：仅 Director 可见

**文件路径**：`docs/report/{agent_name}_{i}.md`

**格式**：
```markdown
# 汇报: {agent_name} #{i}

| 字段 | 值 |
|------|------|
| Agent | {agent_name} |
| 调用序号 | {i} |
| 开始时间 | {timestamp} |
| 结束时间 | {timestamp} |
| 耗时 | {duration} |
| 状态 | ✅ SUCCESS / ⚠️ PARTIAL / ❌ FAILED

---

## 任务摘要

{一句话描述}

---

## 执行内容

1. {做了什么}
2. {做了什么}

---

## 产出物

| 文件 | 路径 |
|------|------|
| {name} | {path} |

---

## 问题与风险

{遇到的问题、不确定性}

---

## 下一步建议

{建议 Director 接下来做什么}
```

---

## 六、Agent 契约定义

每个 Agent 的契约包含以下属性：

| 属性 | 说明 |
|------|------|
| 职责 | 核心任务 |
| 输入 | 需要读取的文件 |
| 输出 | 需要产生的文件 |
| 写入目录 | 允许写入的目录 |
| 参与的 Validation | 作为验证者参与哪些 Stage |

### 6.1 Agent 概览 (v2.5.1)

| Agent | 职责 | 核心变更 | 参与验证 |
|-------|------|---------|---------|
| **director** | 编排所有 Agent | [v2.5.0] Token监控、检查点、返工免验 | - |
| reader | 读取 PDF，提取需求 | - | MODEL, DATA, TRAINING, PAPER, SUMMARY, FINAL |
| **researcher** | 方法建议 | **[v2.4.2] 网络搜索、浏览 `reference_papers/`** | MODEL |
| **modeler** | 设计数学模型 | **[v2.4.2] CODE Gate严格拒绝低质量** | DATA, CODE, TRAINING |
| feasibility_checker | 可行性检查 | - | MODEL, CODE |
| **data_engineer** | 数据处理 | 强制Schema验证；禁止非标量输出 | - |
| code_translator | 代码翻译 | - | CODE, TRAINING |
| **model_trainer** | 模型训练 | **[v2.5.0] 两阶段训练（5A mandatory）** | - |
| **validator** | 结果验证 | 自动化预检查；**Sanity Check思维** | DATA, TRAINING, PAPER, SUMMARY, FINAL |
| visualizer | 生成图表 | - | - |
| **writer** | 撰写论文 | **[v2.4.2] 必须使用 `latex_template/`** | PAPER |
| **summarizer** | 创建摘要 | **[v2.4.2] 参考 `reference_papers/`** | - |
| editor | 润色文档 | - | - |
| **advisor** | 质量评估 | **[v2.4.2] 独立验证、局外人视角** | MODEL, PAPER, FINAL |

### 6.2 输入输出契约

详细的 Agent 契约见 `architectures/v2-5-1/agents/` 目录下的各 Agent prompt 文件。

> ⚠️ Agent prompt 必须与本文档保持一致。冲突时以本文档为准。

---

## 七、执行流程

### 7.1 阶段概览

| Phase | 名称 | 主要 Agent | Validation Gate | 说明 |
|-------|------|-----------|-----------------|------|
| 0 | Problem Understanding | reader, researcher | - | 信息收集 |
| 1 | Model Design | modeler | ✅ MODEL | 4 人验证 |
| 2 | Feasibility Check | feasibility_checker | - | 可行性评估 |
| 3 | Data Processing | data_engineer | ✅ DATA | 3 人验证 |
| 4 | Code Translation | code_translator | ✅ CODE | 3 人验证 |
| 5 | Model Training | model_trainer | ✅ TRAINING | 4 人验证 |
| | &nbsp; &nbsp; **Phase 5A** (快速验证) | **MANDATORY** | | ≤30 min |
| | &nbsp; &nbsp; **Phase 5B** (完整训练) | OPTIONAL | | 4-6 hours |
| 6 | Visualization | visualizer | - | 生成图表 |
| 7 | Paper Writing | writer | ✅ PAPER | 4 人验证 |
| 8 | Summary | summarizer | ✅ SUMMARY | 2 人验证 |
| 9 | Polish | editor | ✅ FINAL | 3 人验证 |
| 10 | Final Review | advisor | - | 最终审核 |

### 7.2 返工机制

1. **返工不免验**：返工后必须以同样标准重新验证
2. **返工计数**：每个 Gate 最多返工 3 次
3. **回退机制**：严重问题需回退到更早阶段

### 7.3 Phase 完整性检查清单

Director 在每个 Phase 结束时必须确认：
1. [ ] 是否生成了该 Phase 定义的所有文件？
2. [ ] 文件是否非空且有效（非 TODO 占位符）？
3. [ ] 是否执行了完整的 Validation Gate（如有）？
4. [ ] 是否有任何步骤被"简化"或"跳过"？
5. [ ] Token 使用是否在合理范围？
6. [ ] 检查点是否已保存？

**如果任何一项为 NO**：
→ 拒绝进入下一 Phase
→ 要求重新执行或降级
→ 记录问题

---

## 八、如何使用本文档

### 8.1 创建/修改 Agent prompt

1. 查找本文档中的定义
2. 确保 prompt 与本文档一致
3. 不要在 prompt 中重复定义规则
4. Agent 文件必须**自包含**，不引用外部架构

### 8.2 解决冲突

- **本文档是权威**
- 发现冲突时，修改 prompt 使其符合本文档

### 8.3 相关文档

| 文档 | 内容 | 位置 |
|------|------|------|
| `retrospective.md` | v2.4.2 和 v2.5.0 问题分析 | 独立文件 |
| `methodology.md` | 设计原则 | 独立文件 |
| `architecture.md` | 本文档 | **核心架构定义** |
| `agents/*.md` | Agent 模板（自包含） | agents/ 目录 |

---

**文档版本**: v2.5.1
**创建日期**: 2026-01-10
**作者**: jcheniu

---

## 九、v2.5.2 使用示例 [v2.5.2 NEW]

### 示例1：Code Translator发现模型错误

**场景**：Phase 4执行中，code_translator发现模型设计中的公式(3)无法实现

**流程**：
1. code_translator发起Rewind建议到Phase 1
2. Director分析：问题真实、代价可接受、依赖图允许
3. Director决策：ACCEPT
4. 跳转到Phase 1，modeler修复设计
5. 重新执行Phase 1-4

### 示例2：Writer发现结果异常

**场景**：Phase 7执行中，writer发现results_1.csv有异常预测值

**流程**：
1. writer发起Rewind建议到Phase 5
2. Director分析：问题真实、但先检查Phase 3
3. Director决策：ACCEPT（但先检查Phase 3特征）
4. 如特征有问题则Rewind到Phase 3，否则到Phase 5

**详见**: phase_jump_design.md 第九节

---

## 十、版本迁移指南 [v2.5.2 NEW]

从v2.5.1迁移到v2.5.2：

### 对于新项目
- 直接使用v2.5.2
- 更新Agent prompts添加Rewind能力
- 参考agents/code_translator.md示例

### 对于现有项目
- v2.5.2完全向后兼容
- 可以逐步启用Phase跳转特性
- VERSION_MANIFEST.json自动升级

**详见**: migration_guide.md

---

## 十一、快速参考

### 11.1 核心文档位置

| 文档 | 路径 | 用途 |
|------|------|------|
| **架构定义** | `architectures/v2-5-2/architecture.md` | 本文档 |
| **Phase跳转设计** | `architectures/v2-5-2/phase_jump_design.md` | Phase跳转详细机制 |
| **迁移指南** | `architectures/v2-5-2/migration_guide.md` | 升级指南 |
| **Agent示例** | `architectures/v2-5-2/agents/code_translator.md` | Agent配置示例 |

### 11.2 v2.5.2 关键改进点

1. **Agent可以主动发现问题** → 建议Rewind
2. **Director基于规则决策** → 不依赖直觉
3. **保留已有成果** → 增量修复
4. **标准化协议** → 清晰的文档格式

### 11.3 与v2.5.1的主要差异

| 方面 | v2.5.1 | v2.5.2 |
|------|-------|-------|
| 问题发现 | Validation Gate | 执行过程中 + Validation Gate |
| 返工范围 | 当前Phase | 可以是上游Phase |
| 跳转决策 | 返工 vs 不返工 | Rewind vs 返工 vs 继续 |
| 新文档类型 | validation/, consultation/ | rewind/ |
| VERSION_MANIFEST | 基础格式 | +rewind_history等 |

---

**文档版本**: v2.5.2
**创建日期**: 2026-01-14
**最后更新**: 2026-01-14
**作者**: jcheniu
**状态**: 🟢 稳定版本

> **v2.5.2 = v2.5.1 (完整保留) + 自适应Phase跳转机制 (新增)**

