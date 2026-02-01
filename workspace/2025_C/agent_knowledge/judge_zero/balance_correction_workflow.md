# Balance Correction Workflow

**Agent**: @judge_zero (diagnosis), @director (routing), various agents (execution)
**Purpose**: Step-by-step process for correcting content imbalance issues
**Last Updated**: 2026-02-01

---

## 5-Step Correction Process

### Step 1: Diagnose Imbalance

**Actions**:
1. Calculate section proportions from compiled PDF
2. Compare against O-Prize targets:
   - Framework (Abstract, Intro): 10%
   - Models: 44%
   - Evidence (Data, Results): 24%
   - Analysis (Sensitivity, S/W): 10%
   - Synthesis (Discussion, Conclusions): 10%
   - Support (References, Appendix): 6%
3. Flag deviations >5%

**Output**: Imbalance diagnosis report

---

### Step 2: Classify Severity

| Deviation | Classification | Action Level |
|-----------|----------------|--------------|
| <5% | BALANCED | No action |
| 5-10% | MINOR | Recommend adjustment |
| 10-15% | SIGNIFICANT | Require adjustment |
| >15% | CRITICAL | Block progression |

---

### Step 3: Determine Correction Type

**Under-Represented Section** → Expansion Required
- Add content to bring section up to target proportion
- Use expansion strategies from `expansion_strategies.md`

**Over-Represented Section** → Consolidation Required
- Reduce content to bring section down to target proportion
- Use consolidation strategies from Protocol 16

---

### Step 4: Route to Appropriate Agent

| Imbalance Issue | Primary Agent | Phase to Revisit |
|-----------------|---------------|------------------|
| Models under-represented (<38%) | @writer | Phase 7B |
| Models over-represented (>50%) | @writer + @editor | Phase 7B |
| Results under-represented (<20%) | @writer + @visualizer | Phase 7C |
| Results over-represented (>30%) | @writer + @editor | Phase 7C |
| Analysis under-represented (<8%) | @writer + @validator | Phase 7D |
| Analysis over-represented (>14%) | @writer + @editor | Phase 7D |
| Synthesis under-represented (<8%) | @writer | Phase 7E |
| Synthesis over-represented (>14%) | @writer + @editor | Phase 7E |
| Framework under-represented (<8%) | @writer | Phase 7A |
| Framework over-represented (>12%) | @writer + @editor | Phase 7A |

---

### Step 5: Verify Correction

**Post-Correction Checklist**:
- [ ] Section now within target range (±5%)
- [ ] Total page count still 24-28 pages
- [ ] No new blank space issues
- [ ] Narrative flow maintained
- [ ] LaTeX compiles without errors
- [ ] Content quality maintained (not just resized)

---

## Expansion/Consolidation Routing Tables

### Expansion Routing (When Section is Under Target)

| Under-Represented | Expand How | Agent | Est. Gain |
|-------------------|------------|-------|-----------|
| Models (<38%) | Add derivations, assumptions, algorithms | @writer | +1-2 pages |
| Results (<20%) | Add interpretation, figures, tables | @writer + @visualizer | +1-2 pages |
| Analysis (<8%) | Add sensitivity details, robustness checks | @writer + @validator | +0.5-1 page |
| Synthesis (<8%) | Add discussion, implications, future work | @writer | +0.5-1 page |
| Framework (<8%) | Expand problem context, motivation | @writer | +0.5 page |
| Support (<4%) | Add appendix content, references | @writer | +0.5-1 page |

### Consolidation Routing (When Section is Over Target)

| Over-Represented | Consolidate How | Agent | Est. Reduction |
|------------------|-----------------|-------|----------------|
| Models (>50%) | Merge similar models, cite derivations | @writer + @editor | -1-2 pages |
| Results (>30%) | Consolidate figures, merge tables | @writer + @visualizer | -1-2 pages |
| Analysis (>14%) | Tabulate instead of prose, reduce redundancy | @writer + @editor | -0.5-1 page |
| Synthesis (>14%) | Tighten discussion, remove redundancy | @writer + @editor | -0.5-1 page |
| Framework (>12%) | Shorten introduction, reduce background | @writer + @editor | -0.5 page |
| Support (>10%) | Move to supplementary materials | @writer | -0.5-1 page |

---

## Decision Matrix for Priority

### When Multiple Imbalances Exist

| Situation | Priority Order |
|-----------|----------------|
| Page count OK (24-28) | Fix largest deviation first |
| Page count LOW (<24) | Expand under-represented sections first |
| Page count HIGH (>28) | Consolidate over-represented sections first |
| Both expansion and consolidation needed | Balance total pages while fixing |

### Priority Scoring

```
Priority Score = Deviation% × Impact_Weight

Impact_Weight:
- Models: 2.0 (most critical section)
- Results: 1.5 (second most critical)
- Analysis: 1.2
- Synthesis: 1.0
- Framework: 1.0
- Support: 0.5

Sort by Priority Score descending.
Fix highest score first.
```

---

## Balance Repair Ticket Format

```markdown
## Balance Repair Ticket #{number}

**Issue**: {section} {under/over}-represented by {X}%
**Current**: {Y}% of paper
**Target**: {Z}%
**Gap**: {±W}%

**Severity**: {MINOR/SIGNIFICANT/CRITICAL}
**Priority Score**: {calculated}

**Assigned To**: @{agent}
**Phase to Revisit**: Phase {X}

**Action Required**:
{Specific expansion or consolidation instructions}

**Success Criteria**:
- Section proportion: {target range}%
- Page impact: {expected change}
- Quality maintained: {verification method}

**Deadline**: Before Phase 9.5
```

---

## Common Imbalance Patterns and Fixes

### Pattern 1: "Results-Heavy Paper"
**Symptom**: Results >30%, Models <40%
**Cause**: Extensive tables/figures without proportional model detail
**Fix**:
1. Consolidate results tables (merge similar)
2. Expand model mathematical detail
3. Move detailed results to appendix

### Pattern 2: "Theory-Heavy Paper"
**Symptom**: Models >50%, Results <20%
**Cause**: Over-detailed methodology, thin results
**Fix**:
1. Cite standard derivations instead of including
2. Expand results interpretation
3. Add more result visualizations

### Pattern 3: "Front-Heavy Paper"
**Symptom**: Framework >15%, Synthesis <8%
**Cause**: Long introduction, short conclusions
**Fix**:
1. Trim background/motivation
2. Move context to appendix
3. Expand discussion and implications

### Pattern 4: "Back-Heavy Paper"
**Symptom**: Support >10%, Models <40%
**Cause**: Excessive appendices, thin main content
**Fix**:
1. Move essential appendix content to main text
2. Reduce appendix to truly supplementary material
3. Expand model sections with moved content

---

## Verification After Correction

### Balance Check Command

After correction, run balance verification:

1. Compile PDF: `xelatex paper.tex`
2. Count pages per section
3. Calculate proportions
4. Compare to targets
5. Confirm all deviations <5%

### Final Approval Criteria

- [ ] All sections within ±5% of target
- [ ] Total pages: 24-28
- [ ] No CRITICAL deviations remaining
- [ ] LaTeX compiles clean
- [ ] Quality verified by @editor

---

**END OF BALANCE CORRECTION WORKFLOW**
