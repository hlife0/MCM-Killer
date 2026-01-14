# v2.5.1 → v2.5.2 迁移指南

> **版本**: v2.5.2
> **日期**: 2026-01-14
> **作者**: jcheniu

---

## 概览

v2.5.2 是 v2.5.1 的重大升级，引入了**自适应Phase跳转机制 (Adaptive Phase Jump)**。

**核心改进**：
1. **Agent驱动的Rewind**：Agent可以主动建议回退到上游Phase
2. **Phase依赖图**：明确定义Phase之间的跳转规则
3. **智能决策**：Director基于规则而非直觉做出跳转决策
4. **增量修复**：保留已有成果，避免完全重做

---

## 一、新增概念

### 1.1 Rewind Recommendation（回退建议）

**定义**：Agent在执行过程中发现上游问题时，主动建议Director回退到之前的Phase。

**文档**：`docs/rewind/rewind_rec_{i}_{from_agent}_phase{target}.md`

**对比v2.5.1**：

| 方面 | v2.5.1 | v2.5.2 |
|------|-------|-------|
| 问题发现时机 | Validation Gate | 执行过程中 |
| 返工范围 | 当前Phase | 可以是上游任意Phase |
| 发起者 | 被动（Validator） | 主动（任何Agent） |
| 决策 | 返工 vs 不返工 | Rewind vs 返工 vs 继续 |

### 1.2 Phase Dependency Graph（Phase依赖图）

**定义**：有向图，定义Phase之间的前向依赖和Rewind关系。

**新增字段**：
- `E_forward`: 前向依赖边（Phase i → Phase j）
- `E_rewind`: Rewind边（Phase j → Phase i）

### 1.3 Rewind vs 返工

| 方面 | 返工 (v2.5.1) | Rewind (v2.5.2) |
|------|---------------|-----------------|
| 触发 | Validation Gate REJECTED | Agent主动发现 |
| 目标 | 当前Phase | 可能是上游Phase |
| 文档 | `docs/validation/` | `docs/rewind/` |
| 目的 | 修复当前产出 | 修复根本原因 |

**两者协同**：
- Rewind优先于返工
- 返工可以演变成Rewind
- Validation Gate也可以触发Rewind

---

## 二、架构变更

### 2.1 新增文件/目录

**架构文档**：
```
architectures/v2-5-2/
├── architecture.md          # [更新] 新增Phase跳转章节
├── phase_jump_design.md     # [NEW] Phase跳转详细设计
├── adaptive_workflow.md     # [NEW] 自适应工作流
└── agents/
    ├── code_translator.md   # [更新] 展示Rewind能力
    └── ...                  # 其他Agent也需要更新
```

**输出目录**：
```
output/
├── VERSION_MANIFEST.json    # [更新] 新增rewind相关字段
├── docs/
│   ├── rewind/              # [NEW] Rewind建议文档
│   │   └── rewind_rec_{i}_{from}_{to}.md
│   ├── consultation/
│   ├── validation/
│   └── report/
└── ...
```

### 2.2 VERSION_MANIFEST.json 变更

**v2.5.1**：

```json
{
  "version": "2.5.1",
  "current_phase": 5,
  "files": {...},
  "agent_calls": {...},
  "consultation_count": 5,
  "validation_count": 12,
  "checkpoints": []
}
```

**v2.5.2**：

```json
{
  "version": "2.5.2",
  "current_phase": 5,
  "workflow_state": "normal",  // [NEW]
  "rewind_history": [           // [NEW]
    {
      "rewind_id": 1,
      "from_phase": 4,
      "to_phase": 1,
      "reason": "模型设计有根本性缺陷",
      "timestamp": "2026-01-14 01:00:00",
      "preserved_files": ["problem/*"],
      "redone_phases": [1, 2, 3, 4]
    }
  ],
  "files": {
    "problem/problem_requirements": {
      "current": 2,
      "history": [
        {
          "version": 1,
          "created_at": "2026-01-14 00:10:00",
          "created_by": "reader",
          "preserved": true    // [NEW]
        }
      ]
    }
  },
  "agent_calls": {...},
  "consultation_count": 5,
  "validation_count": 12,
  "rewind_count": 1,     // [NEW]
  "skip_count": 0,       // [NEW]
  "checkpoints": []
}
```

**新增字段说明**：
- `workflow_state`: 工作流状态（"normal", "rewinding", "recovering"）
- `rewind_history`: Rewind历史记录数组
- `rewind_count`: 总Rewind次数
- `skip_count`: 总Skip次数
- `preserved`: 文件是否在Rewind中保留

---

## 三、Agent Prompt 变更

### 3.1 通用变更（所有Agent）

**新增章节**：

```markdown
## [v2.5.2 NEW] Phase跳转能力

### 3.1 你的Rewind权限

**可以建议Rewind到**：
- Phase {X}: 当{condition}
- Phase {Y}: 当{condition}

### 3.2 何时应该建议Rewind

- ✅ {condition_1}
- ✅ {condition_2}

### 3.3 如何发起Rewind建议

{格式化的Rewind建议模板}

### 3.4 何时不应该建议Rewind

- ❌ {condition_1}
- ❌ {condition_2}
```

**更新Report格式**：

```markdown
## 问题与风险

**上游问题**：
- 是否发现上游Phase的问题：是/否
- 是否建议Rewind：是/否
- 详情：{如果有}
```

### 3.2 特定Agent的Rewind权限

| Agent | 可以Rewind到 | 条件 |
|-------|-------------|------|
| **code_translator** | Phase 1 | 模型设计无法实现 |
| **code_translator** | Phase 3 | 特征数据缺失 |
| **model_trainer** | Phase 1 | 模型方法论错误 |
| **model_trainer** | Phase 3 | 特征不足 |
| **model_trainer** | Phase 4 | 代码实现有问题 |
| **writer** | Phase 5 | 结果不合理 |
| **advisor** | Phase 1 | 模型方法论问题 |
| **advisor** | Phase 5 | 结果质量问题 |

---

## 四、Director Prompt 变更

### 4.1 新增职责

```markdown
## 1.1 核心职责

1. 编排执行：按 10 阶段 workflow 调度 Agent
2. 协调协作：处理 Consultation 请求
3. 触发验证：在 Gate 位置调用多人验证
4. 处理返工：根据验证结果决定返工
5. **[v2.5.2 NEW] 处理Rewind：根据Agent建议决定Phase跳转**
6. 追踪状态：维护 VERSION_MANIFEST.json
7. Token 监控：监控 Token 使用，提前预警
8. 检查点管理：保存检查点，支持恢复
9. 用户决策：在冲突时请求用户决策
```

### 4.2 新增章节

```markdown
## [v2.5.2 NEW] Phase跳转处理

### 处理Rewind建议

1. 收到Agent的Rewind建议
2. 分析：
   - 问题是否真实存在？
   - Rewind是否是最优方案？
   - 代价是否可接受？
   - 依赖图是否允许？
3. 决策：
   - ACCEPT：执行Rewind
   - REJECTED：说明理由
   - MODIFY：调整目标Phase
4. 执行：
   - 更新VERSION_MANIFEST.json
   - 标记保留文件
   - 跳转到目标Phase
   - 调用相应Agent
```

### 4.3 更新决策流程

**v2.5.1**：

```
Agent完成 → Validation Gate → APPROVED/REJECTED → 返工或继续
```

**v2.5.2**：

```
Agent执行中
    ↓
发现上游问题？
    ↓ 是
发起Rewind建议
    ↓
Director决策
    ↓
    ├─→ ACCEPT: Rewind到目标Phase
    ├─→ REJECTED: 继续当前Phase
    └─→ MODIFY: 调整方案
    ↓
继续执行
```

---

## 五、代码/脚本变更

### 5.1 无需修改

v2.5.2主要是**协议和流程**的改进，不涉及代码工具的修改。

**原因**：
- Phase跳转是AI编排层的行为
- 不改变Python代码、数据处理等技术实现
- VERSION_MANIFEST.json的扩展是向后兼容的

### 5.2 可选增强

如果想要更好的支持，可以添加：

**工具函数（可选）**：

```python
def check_rewind_permission(current_phase: int, target_phase: int) -> bool:
    """检查是否允许从current_phase Rewind到target_phase"""
    # 实现依赖图检查逻辑
    pass

def estimate_rewind_cost(from_phase: int, to_phase: int) -> dict:
    """估算Rewind代价"""
    # 返回{time: hours, files_to_redo: list, preserved: list}
    pass

def create_rewind_recommendation(agent: str, current: int, target: int,
                                 problem: str, reason: str, urgency: str) -> str:
    """生成Rewind建议文档"""
    # 生成Markdown文档
    pass
```

但这些是**可选的**，AI可以直接生成文档，不需要代码支持。

---

## 六、升级步骤

### 6.1 架构文档升级

```bash
# 1. 创建v2-5-2目录
mkdir -p architectures/v2-5-2/agents

# 2. 复制v2-5-1文档作为基础
cp architectures/v2-5-1/architecture.md architectures/v2-5-2/
cp -r architectures/v2-5-1/agents/* architectures/v2-5-2/agents/

# 3. 手动更新（或使用AI辅助）
# - 添加Phase跳转章节
# - 更新Agent prompts
# - 创建phase_jump_design.md
```

### 6.2 Agent Prompt升级

**对于每个Agent**：

1. **添加"可以Rewind到"章节**
   - 确定该Agent可以建议Rewind到哪些Phase
   - 参考本文档3.2节的表格

2. **添加"何时应该建议Rewind"章节**
   - 列出具体的触发条件
   - 提供示例场景

3. **添加"如何发起Rewind建议"章节**
   - 提供Rewind建议模板
   - 包含完整的格式示例

4. **更新"执行流程"章节**
   - 添加"发现问题时的流程"
   - 明确何时使用Consultation vs Rewind

5. **更新Report格式**
   - 添加"上游问题"字段
   - 记录是否建议Rewind

### 6.3 Director Prompt升级

1. **添加"Phase跳转处理"章节**
   - 详细的决策流程
   - 决策矩阵
   - 专家系统规则

2. **更新"处理验证结果"章节**
   - Validation Gate也可以触发Rewind
   - 返工可以演变成Rewind

3. **添加"Phase依赖图"章节**
   - 可视化依赖图
   - 允许的Rewind路径表
   - 代价估算

### 6.4 VERSION_MANIFEST.json升级

**不需要立即升级**，v2.5.2格式向后兼容。

**建议**：
- 新项目使用v2.5.2格式
- 现有项目在首次Rewind时自动升级

---

## 七、兼容性

### 7.1 向后兼容

**v2.5.2 完全向后兼容 v2.5.1**：

- v2.5.1的输出文件可以直接在v2.5.2中使用
- VERSION_MANIFEST.json v2.5.1格式有效
- v2.5.1的Agent prompts仍然可以工作

**升级路径**：

```
v2.5.1项目
    ↓
复制到v2.5.2环境
    ↓
可以直接使用
    ↓
首次Rewind时自动升级VERSION_MANIFEST.json
```

### 7.2 前向兼容

**新增字段**：

- v2.5.1读取v2.5.2的VERSION_MANIFEST.json会忽略新增字段
- 建议使用v2.5.2读取所有项目

---

## 八、测试建议

### 8.1 单元测试场景

**场景1：Code Translator建议Rewind到Phase 1**

```
Given: Phase 4执行中
When: Code Translator发现模型设计无法实现
Then: 应该生成Rewind建议文档
And: Director应该评估并决策
```

**场景2：Director接受Rewind**

```
Given: 收到Rewind建议，问题严重度高，代价低
When: Director决策
Then: 应该ACCEPT Rewind
And: 更新VERSION_MANIFEST.json
And: 跳转到目标Phase
```

**场景3：Director拒绝Rewind**

```
Given: 收到Rewind建议，问题轻微，代价高
When: Director决策
Then: 应该REJECT Rewind
And: 说明理由
And: 当前Phase继续执行
```

### 8.2 集成测试场景

**场景4：完整的Rewind流程**

```
Given: 项目在Phase 4
When: Code Translator建议Rewind到Phase 1
And: Director接受
And: Modeler修复设计
And: 重新执行Phase 1-4
Then: 所有Phase成功完成
And: VERSION_MANIFEST.json正确记录
```

**场景5：Validation Gate触发Rewind**

```
Given: Phase 4 Validation Gate REJECTED
When: Validator发现根本原因在Phase 1
Then: 应该建议Rewind到Phase 1
And: Director应该评估（不同于返工Phase 4）
```

---

## 九、常见问题

### Q1: v2.5.2是否破坏了v2.5.1的流程？

**A**: 不破坏。v2.5.2在v2.5.1基础上**增强**，不改变原有流程。

- v2.5.1的线性流程仍然支持
- 新增的Rewind是**可选的优化路径**
- 如果Agent从不建议Rewind，行为与v2.5.1相同

### Q2: Rewind是否会导致无限循环？

**A**: 不会。有多个保护机制：

1. **代价分析**：高代价Rewind会被拒绝
2. **Rewind计数**：同一位置Rewind超过2次会触发警告
3. **Director决策**：基于规则而非随机
4. **用户干预**：必要时可以请求用户决策

### Q3: 如何防止滥用Rewind？

**A**: 多重约束：

1. **Agent规则**：明确何时可以/不可以建议Rewind
2. **Director评估**：严格验证问题真实性
3. **代价收益分析**：确保Rewind是值得的
4. **优先级**：Consultation优先于Rewind

### Q4: v2.5.2是否需要重新训练？

**A**: 不需要。v2.5.2的所有改进都是**协议层面**的：

- Agent如何通信
- Director如何决策
- 文档如何组织

不涉及模型、算法等技术实现。

### Q5: 是否可以逐步迁移？

**A**: 可以。有两种策略：

**策略1：保守迁移**
- 先使用v2.5.2架构
- Agent prompts保持v2.5.1
- 逐步添加Phase跳转能力

**策略2：完整迁移**
- 一次性升级所有组件
- 立即启用Phase跳转
- 推荐用于新项目

---

## 十、最佳实践

### 10.1 Agent设计

**好的Agent应该**：

1. **主动发现**：在执行中检查上游产出物
2. **清晰证据**：提供充分的问题证据
3. **权衡代价**：考虑Rewind的代价
4. **优先Consultation**：快速澄清优于Rewind

**不好的Agent**：

1. 被动等待Validation Gate
2. 模糊的问题描述
3. 轻易建议Rewind
4. 忽视代价

### 10.2 Director配置

**好的Director应该**：

1. **基于规则决策**：不依赖AI直觉
2. **快速响应**：及时处理Rewind建议
3. **记录理由**：便于后续分析
4. **质量优先**：不为了避免麻烦而拒绝

### 10.3 项目管理

**建议**：

1. 新项目直接使用v2.5.2
2. 现有项目逐步迁移
3. 监控Rewind频率，避免滥用
4. 记录Rewind历史，优化流程

---

## 十一、资源

### 11.1 相关文档

| 文档 | 内容 |
|------|------|
| `architecture.md` | v2.5.2核心架构 |
| `phase_jump_design.md` | Phase跳转详细设计 |
| `agents/code_translator.md` | Agent示例（含Rewind能力） |

### 11.2 示例

| 示例 | 描述 |
|------|------|
| `示例1` | Code Translator发现模型错误 |
| `示例2` | Writer发现结果异常 |
| `示例3` | Model Trainer发现特征不足 |

---

**版本**: v2.5.2
**日期**: 2026-01-14
**作者**: jcheniu
**目标**: 帮助用户从v2.5.1平滑升级到v2.5.2
