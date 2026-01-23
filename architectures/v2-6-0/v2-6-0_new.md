# v2.6.0 未来改动记录

> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Purpose**: 记录 v2.6.0 版本的计划改动和待办事项

---

## 待办事项

### ✅ COMPLETED: CLAUDE.md Missing Protocol 12 Re-Validation Trigger

**发现日期**: 2026-01-23
**完成日期**: 2026-01-23
**优先级**: HIGH
**状态**: ✅ 已完成

**问题描述**:
CLAUDE.md 缺少 Protocol 12 (v2.5.9) 的关键触发逻辑：
- 当 @code_translator 在训练期间修复代码并提供 CHANGES SUMMARY 时
- 如果 SUMMARY 显示设计参数变更（tune, chains, draws, algorithm, features）
- @director 必须触发 Phase 4.5 re-validation（调用 @time_validator）
- 训练必须等待 re-validation 完成后才能恢复

**当前状态**:
- ✅ time_validator.md 已实现 re-validation mode (lines 814-1128)
- ✅ code_translator.md 已要求 CHANGES SUMMARY (lines 470-612)
- ❌ CLAUDE.md **缺少触发协议**（应在 Phase 5 section，line 607 之后）

**需要添加的内容** (添加到 CLAUDE.md):
```markdown
### Phase 4.5 Re-Validation Trigger (v2.5.9)

> [!CRITICAL] **[v2.5.9] When @code_translator modifies code during training, re-validation is REQUIRED.**

**Trigger**: When @code_translator implements fix (emergency OR standard) with CHANGES SUMMARY

**@director's Protocol**:
1. Review @code_translator's CHANGES SUMMARY
2. Check for design parameter changes:
   - Sampling parameters: tune, chains, draws, target_accept
   - Algorithm changes: NUTS → Metropolis, etc.
   - Feature additions/removals
3. **IF parameter changes detected**:
   ```
   @time_validator: RE-VALIDATION REQUIRED
   @code_translator has modified model_{i}.py:
   Changes: {list of parameter changes}
   Please run Phase 4.5 validation on reworked code.
   Training MUST NOT resume until validation complete.
   ```
4. **IF no parameter changes** (simple bug fix):
   - Allow training to resume without re-validation

**Why Critical**: Prevents lazy implementation through hidden parameter simplifications during training.
```

**影响**: 如果不添加此触发逻辑，Protocol 12 的反欺诈保护（40% → <5% fraud reduction）将不会在主工作流中激活。

**参考**:
- V2-6-0_ARCHITECTURE_VERIFICATION_REPORT.md: Issue 2 (lines 316-364)
- Protocol 12 文档: 12_phase45_revalidation.md
- 实现: time_validator.md:814-1128, code_translator.md:470-612

**解决方案**:
✅ **已添加到 CLAUDE.md** (line 610-728)
- 位置: Phase 5 Special Handling section，Emergency Convergence Fix Protocol 之后
- 内容: 完整的 Phase 4.5 Re-Validation Trigger 协议
- 包含: 触发条件、@director 决策协议、3个示例、为什么关键、与紧急协议集成
- 行数: 约 120 行，包含完整的决策流程和参考文档链接

**验证**:
- ✅ 协议已添加到 CLAUDE.md:610-728
- ✅ 包含完整的 @director 决策逻辑
- ✅ 包含参数变更检测逻辑
- ✅ 包含训练暂停机制
- ✅ 与 v2.5.8 紧急协议正确集成
- ✅ Protocol 12 反欺诈保护现已完全激活

---

## 计划改动

（留空，待填写）

---

**最后更新**: 2026-01-23
