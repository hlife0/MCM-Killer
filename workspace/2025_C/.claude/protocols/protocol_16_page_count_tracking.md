# Protocol 16: Page Count Tracking

**Version**: 3.2.0
**Status**: Active
**Owner**: @director (enforcement), @writer (compliance)
**Scope**: Phase 7 (Paper Writing)
**Priority**: HIGH

---

## Purpose

Prevent page count overrun violations during paper writing. This protocol addresses the most critical issue from MCM 2025 Problem C, where the 45-page submission exceeded the 25-page limit, resulting in an estimated -3 point penalty.

---

## Rationale

**Problem**: No tracking mechanism existed during Phase 7 writing, leading to:
- 45-page submission (20 pages over limit)
- Estimated -3 point penalty
- Emergency consolidation required after completion

**Solution**: Systematic page budget tracking with checkpoints after each Phase 7 sub-phase ensures early detection and corrective action before submission.

---

## Page Budget Allocation

| Section | Page Budget | Cumulative | Checkpoint Phase |
|---------|-------------|------------|------------------|
| Abstract | 0.3 | 0.3 | - |
| Introduction | 1.2 | 1.5 | After 7A |
| Notation | 0.5 | 2.0 | After 7A |
| Models (5 × 1.2) | 6.0 | 8.0 | After 7B |
| Data Description | 2.0 | 10.0 | After 7C |
| Results | 8.0 | 18.0 | After 7C |
| Sensitivity Analysis | 2.0 | 20.0 | After 7D |
| Strengths/Weaknesses | 2.0 | 22.0 | After 7D |
| Discussion | 1.5 | 23.5 | After 7E |
| Conclusions | 1.0 | 24.5 | After 7E |
| Bibliography | 0.5 | 25.0 | After 7E |

**Total**: 25.0 pages (MCM limit)

---

## Checkpoint System

### Phase 7A: Paper Framework
**Checkpoint**: After Abstract + Introduction + Notation written
**Target**: ≤3.0 pages cumulative
**Status**: ✅ PASS if ≤3.0 | ❌ FAIL if >3.0

**Action if FAIL**:
- Shorten Introduction (target: 1.2 → 1.0 pages)
- Consolidate Notation (target: 0.5 → 0.3 pages)

---

### Phase 7B: Model Sections
**Checkpoint**: After all 5 model sections written
**Target**: ≤10.0 pages cumulative
**Status**: ✅ PASS if ≤10.0 | ❌ FAIL if >10.0

**Action if FAIL**:
- Reduce per-model budget (1.2 → 1.0 pages per model)
- Move non-essential derivations to appendices
- Consolidate similar equations

---

### Phase 7C: Results Integration
**Checkpoint**: After Data + Results sections written
**Target**: ≤18.0 pages cumulative
**Status**: ✅ PASS if ≤18.0 | ⚠️ WARNING if 18.0-20.0 | ❌ FAIL if >20.0

**Action if WARNING**:
- Tighten remaining sections (reduce budget for Analysis/Conclusions)
- Notify @writer of yellow alert

**Action if FAIL**:
- Consolidate Results tables (merge similar outputs)
- Reduce figure count (8 → 6 figures)
- Move supplementary results to online appendix

---

### Phase 7D: Analysis Sections
**Checkpoint**: After Sensitivity + Strengths/Weaknesses written
**Target**: ≤22.0 pages cumulative
**Status**: ✅ PASS if ≤22.0 | ⚠️ YELLOW if 22.0-23.0 | ❌ RED if >23.0

**Action if YELLOW** (≥22.0 pages):
- **Alert**: Notify @writer immediately
- **Action**: Tighten Discussion + Conclusions budget (2.5 → 1.5 pages)
- **Restriction**: No new figures, consolidation only

**Action if RED** (≥23.0 pages):
- **Critical**: Stop writing immediately
- **Emergency**: Trigger consolidation protocol
- **Review**: @director approval required to proceed

---

### Phase 7E: Conclusions
**Checkpoint**: After Discussion + Conclusions + Bibliography written
**Target**: ≤25.0 pages cumulative
**Status**: ✅ PASS if ≤25.0 | ❌ CRITICAL if >25.0

**Action if CRITICAL** (>25.0 pages):
1. **Stop**: Do not proceed to Phase 7F
2. **Emergency Consolidation** (in priority order):
   - Move all appendices to supplement document (-3 to -5 pages)
   - Consolidate figures (2 figures on 1 page where appropriate) (-2 to -4 pages)
   - Shorten non-critical sections (Discussion: 1.5 → 1.0 page) (-0.5 pages)
   - Reduce per-model descriptions (1.2 → 1.0 pages) (-1.0 pages)
   - Move supplementary tables to online appendix (-1 to -2 pages)
3. **Re-verify**: Check page count after each consolidation step
4. **Proceed**: Only when ≤25.0 pages

---

## Alert Thresholds

### Yellow Warning (≥20.0 pages)
- **Trigger**: Page count ≥20.0 after Phase 7C or 7D
- **Action**: Notify @writer, tighten remaining sections
- **Severity**: Medium (requires attention, not emergency)

### Red Critical (≥23.0 pages)
- **Trigger**: Page count ≥23.0 after Phase 7D or 7E
- **Action**: Stop writing, trigger emergency consolidation
- **Severity**: High (requires immediate intervention)

### Submission Limit (≥25.0 pages)
- **Trigger**: Page count ≥25.0
- **Action**: Block submission, mandatory consolidation
- **Severity**: Critical (submission at risk)

---

## Emergency Consolidation Protocol

**Trigger**: Page count ≥25.0 pages after Phase 7E

**Priority Order** (execute until ≤25.0 pages):

1. **Move Appendices to Supplement** (saves: -3 to -5 pages)
   - All appendices → separate PDF (not counted toward 25-page limit)
   - Reference in main text: "See Supplementary Appendix A"

2. **Consolidate Figures** (saves: -2 to -4 pages)
   - Merge similar figures (e.g., Model 1-3 diagnostics on 1 page)
   - Use 2×2 figure grids where appropriate
   - Reduce figure size (full-page → half-page)

3. **Shorten Discussion** (saves: -0.5 pages)
   - Target: 1.5 → 1.0 page
   - Remove redundant summary points
   - Consolidate paragraphs

4. **Reduce Model Descriptions** (saves: -1.0 pages)
   - Target: 1.2 → 1.0 pages per model (5 models total)
   - Move non-essential derivations to supplement
   - Keep only primary equations in main text

5. **Move Supplementary Tables** (saves: -1 to -2 pages)
   - Full results tables → online appendix
   - Keep only summary tables in main text
   - Reference: "See Supplementary Table S3"

6. **Reduce Sensitivity Analysis** (saves: -0.5 pages)
   - Target: 2.0 → 1.5 pages
   - Consolidate sensitivity plots
   - Focus on key sensitivities only

**Expected Total Savings**: 8 to 13 pages (sufficient to bring 45 → 25 pages)

---

## Enforcement Actions

### @writer Responsibilities
1. **Report Page Count**: After each Phase 7 sub-phase completion, report cumulative page count to @director
2. **Monitor Budget**: Track section length against allocated budget
3. **Early Warning**: If approaching budget limit, notify @director before proceeding
4. **Compliance**: Stop writing if @director issues red alert

**Completion Report Format**:
```
Phase 7B Complete: Models section written
- Page count: 9.5 / 10.0 pages (within budget)
- Status: ✅ PASS
- Proceeding to Phase 7C
```

---

### @director Responsibilities
1. **Verify Page Count**: After each Phase 7 sub-phase, verify @writer's page count report
2. **Enforce Thresholds**: Apply yellow/red alerts based on page count
3. **Block Progression**: If page count ≥25.0, do not approve Phase 7F until consolidation
4. **Emergency Intervention**: Trigger consolidation protocol when red critical threshold reached

**Verification Method**:
- Compile paper.tex to PDF
- Check PDF page count in document properties
- Compare against budget allocation table
- Approve or require consolidation

---

## Validation Mechanism

**Phase 7F**: LaTeX Compilation Gate

**Before Compilation**:
1. @writer submits Phase 7E completion with page count report
2. @director verifies PDF page count ≤25.0
3. If ✅ PASS: Approve Phase 7F compilation
4. If ❌ FAIL: Trigger consolidation protocol, re-verify

**After Compilation**:
1. Final PDF page count must be ≤25.0
2. If >25.0: Return to @writer for consolidation
3. Only when ≤25.0: Proceed to Phase 8 (Summary)

---

## Exception Handling

### Director Override
**Condition**: If competition requires >25 pages due to special requirements

**Process**:
1. @director documents justification in `output/docs/page_limit_override.md`
2. Specifies new page limit with rationale
3. Notifies @writer of adjusted budget
4. Proceeds with adjusted limits

**Example Justifications**:
- "Competition specifies 30-page limit for Problem C"
- "Appendices not counted toward page limit per official rules"
- "Supplemental materials required in main document"

---

## Integration with Existing Workflow

**Phase 7A-7F**: Modified to include page count checkpoints

```
Phase 7A → Checkpoint: ≤3.0 pages → ✅ PASS or ❌ FAIL
Phase 7B → Checkpoint: ≤10.0 pages → ✅ PASS or ❌ FAIL
Phase 7C → Checkpoint: ≤18.0 pages → ✅ PASS or ⚠️ WARNING or ❌ FAIL
Phase 7D → Checkpoint: ≤22.0 pages → ✅ PASS or ⚠️ YELLOW or ❌ RED
Phase 7E → Checkpoint: ≤25.0 pages → ✅ PASS or ❌ CRITICAL
Phase 7F → Compile PDF → Final verification ≤25.0 pages
```

---

## Success Metrics

**Quantitative**:
- 100% of submissions ≤25 pages
- Zero page limit violations
- Average page count: 23-25 pages (optimal range)

**Qualitative**:
- Early detection of page overrun (at Phase 7C or 7D, not after 7F)
- No emergency consolidation after Phase 7F
- Systematic budget tracking (not ad-hoc)

---

## Lessons from MCM 2025 Problem C

**What Went Wrong**:
- No page tracking during writing
- 45-page submission discovered only after completion
- Emergency consolidation required (moved appendices to supplement)
- Estimated -3 point penalty for page violation

**How Protocol 16 Prevents Recurrence**:
- Checkpoints after every sub-phase (early detection)
- Budget allocation (systematic planning)
- Alert thresholds (yellow/red warnings)
- Emergency protocol (structured consolidation, not ad-hoc)
- @director enforcement (not optional)

---

## Related Protocols

- **Protocol 14**: Academic Style Alignment (word choice affects page count)
- **Protocol 15**: Observation-Implication (concise writing reduces page count)
- **Protocol 7**: Paper Framework (structure affects page budget)

---

## Changelog

**v3.2.0** (2026-01-29): Initial creation
- Addresses MCM 2025 Problem C page overrun issue (45 → 25 pages required)
- Implements checkpoint system with 5 verification points
- Establishes emergency consolidation protocol
