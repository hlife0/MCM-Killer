# MCM-Killer v2.5.0 Changelog

**Release Date**: 2026-01-07
**Previous Version**: v2.4.1

---

## 核心改进

### 1. 架构重构:解决路径引用问题

**问题**: v2.4.1中workspace/agents无法访问architectures/目录

**解决方案**:
- Architecture文档现在部署在workspace内部
- 每个workspace是自包含的,包含完整架构定义
- architectures/目录保留为"模板和参考"

### 2. 反偷懒机制:强制轻量模型

**问题**: v2.4.1中Phase 5被完全跳过(0%完成)

**解决方案**:
- Model Trainer新增**轻量模型强制要求**
- 禁止跳过任何Phase
- 资源不足时必须使用降级方案,不允许跳过

### 3. 目录结构优化

**问题**: architectures和workspace并列导致依赖混乱

**解决方案**:
```
MCM-Killer/
├── architectures/          # 架构模板和参考
│   ├── v2-4-1/
│   └── v2-5-0/
├── workspace/
│   └── 2025_C/
│       ├── .claude/
│       │   ├── agents/     # Agent定义
│       │   ├── architecture/  # ← NEW: 本项目专用架构副本
│       │   └── settings.local.json
│       └── output/
```

---

## 新增功能

### 1. 轻量模型分级体系

**Model Trainer Agent新增**:
- **Tier 1 (完整模型)**: 标准资源需求
- **Tier 2 (轻量模型)**: 减少迭代/采样
- **Tier 3 (最小模型)**: 快速原型,至少要有结果

**规则**: 即使Tier 3,也必须产生可用的results.csv,不允许0%完成

### 2. Phase完整性检查点

**Director Agent新增**:
- 每个Phase结束时强制检查:
  - [ ] 是否生成了所有必需文件?
  - [ ] 文件是否非空且有效?
  - [ ] 是否有任何步骤被跳过?
- 跳过必须记录并要求用户确认

### 3. Token预算管理

**所有Agent新增**:
- Phase开始时评估Token需求
- 中途检测到Token不足时:
  1. 暂停当前任务
  2. 切换到轻量模式
  3. 记录降级原因
- 禁止擅自决定"跳过非关键步骤"

---

## 修复的Bug

### Bug #1: 路径引用循环依赖

**v2.4.1**:
```markdown
> **权威参考**: `architectures/v2-4-1/architecture.md`
```
但workspace中的AI无法读取这个路径。

**v2.5.0**:
```markdown
> **权威参考**: `.claude/architecture/architecture.md`
```
每个workspace包含自己的架构副本。

### Bug #2: Model Trainer可以跳过训练

**v2.4.1**:
- 没有明确的轻量模型选项
- AI可以选择"skip due to time constraints"

**v2.5.0**:
- 强制3-tier模型
- 禁止skip
- 必须至少产生Tier 3结果

### Bug #3: Completeness Mandate无执行机制

**v2.4.1**:
- 有规则但无检查点
- Phase 5被跳过后才发现

**v2.5.0**:
- 每Phase结束强制检查
- 跳过需要用户确认
- 自动降级而非跳过

---

## 向后兼容性

### 升级指南

从v2.4.1升级到v2.5.0:

1. **创建新目录结构**:
   ```bash
   mkdir -p workspace/2025_C/.claude/architecture
   ```

2. **复制架构文件**:
   ```bash
   cp architectures/v2-5-0/*.md workspace/2025_C/.claude/architecture/
   ```

3. **更新Agent引用**:
   - 所有`architectures/v2-4-1/` → `.claude/architecture/`
   - 更新版本号v2.4.1 → v2.5.0

4. **验证完整性**:
   - 检查所有agent引用路径
   - 确认architecture副本完整

---

## 文件变更清单

### 新增文件
- `architectures/v2-5-0/architecture.md` (重构)
- `architectures/v2-5-0/directory_structure.md` (新增)
- `architectures/v2-5-0/anti_lazy_mechanisms.md` (新增)

### 修改文件
- 所有Agent prompts (更新引用路径,添加轻量模型选项)
- `CLAUDE.md` (更新架构引用)

### 删除文件
- 无(向后兼容)

---

## 测试清单

升级后验证:
- [ ] workspace包含完整的architecture副本
- [ ] 所有agent能读取architecture路径
- [ ] Model Trainer有3-tier选项
- [ ] Director有Phase完整性检查
- [ ] 无跳过Phase的情况发生

---

**Maintainer**: jcheniu
**Review Status**: Pending
**Breaking Changes**: Yes (路径引用变更)
