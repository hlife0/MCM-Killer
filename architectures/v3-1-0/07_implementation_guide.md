# Implementation Guide: v3.1.0 (m-orientation)

> **Target**: MCM-Killer v3.1.0
> **Source**: m-orientation specifications
> **Organization**: 3 Sprints over 14 days
> **Philosophy**: Additive enhancement, no breaking changes

---

## Implementation Philosophy

### Core Principles

1. **ADDITIVE ONLY**: All v3.0.0 functionality preserved
2. **Sprint-Based**: 3 focused sprints with clear deliverables
3. **Verification-Driven**: Each sprint has testable success criteria
4. **Tool-First**: Python tools before agent prompts
5. **Test Early**: Integration tests after each sprint

---

## Sprint Overview

| Sprint | Days | Focus | Key Deliverables |
|--------|------|-------|------------------|
| **Sprint 1** | 1-3 | Foundation & Eyes | Tools, HMML 2.0, Style Guide |
| **Sprint 2** | 4-8 | Brain & Soul | @metacognition, @narrative_weaver (Iterative), Mode B |
| **Sprint 3** | 9-14 | Fangs & Shield | @judge_zero, @knowledge_librarian (Consultant), Phase 9.1 |

---

## Sprint 1: Foundation & Eyes (Days 1-3)

### Objective

Build the **infrastructure** and **observational capacity** to support cognitive narrative.

### Deliverables

#### Day 1: Workspace & Tools

**Tasks**:
1. Create complete directory structure
2. Implement `init_workspace.py`
3. Verify directory creation

**Files Created**:
- `tools/init_workspace.py` (~165 lines)
- All v3.1.0 directories

**Verification**:
```bash
python tools/init_workspace.py
ls -R output/  # Should see complete structure
```

---

#### Day 2: HMML 2.0 Migration

**Tasks**:
1. Implement `migrate_hmml.py`
2. Migrate existing HMML.md to hierarchical structure
3. Generate index and summary JSON

**Files Created**:
- `tools/migrate_hmml.py` (~450 lines)
- `knowledge_library/methods/**/*.md` (structured)
- `knowledge_library/index.md`
- `knowledge_library/hmml_summary.json`

**Verification**:
```bash
python tools/migrate_hmml.py \
    --input knowledge_library/HMML.md \
    --output knowledge_library/methods/

# Check output
ls knowledge_library/methods/differential_equations/epidemic/
# Should see: sir_basic.md, sir_network.md, etc.

# Verify JSON
cat knowledge_library/hmml_summary.json | jq '.total_methods'
```

---

#### Day 3: Style Analysis

**Tasks**:
1. Implement `style_analyzer.py`
2. Analyze O-Prize PDFs
3. Generate style guide

**Files Created**:
- `tools/style_analyzer.py` (~530 lines)
- `knowledge_library/academic_writing/style_guide.md`

**Verification**:
```bash
python tools/style_analyzer.py \
    --input reference_papers/*.pdf \
    --output knowledge_library/academic_writing/style_guide.md

# Check style guide content
grep "High-Value Verbs" knowledge_library/academic_writing/style_guide.md
grep "Abstract Rules" knowledge_library/academic_writing/style_guide.md
```

---

### Sprint 1 Success Criteria

- [ ] Complete directory structure exists
- [ ] HMML 2.0 has ≥50 method files
- [ ] `hmml_summary.json` is valid JSON
- [ ] `style_guide.md` contains ≥10 high-value verbs
- [ ] `style_guide.md` contains abstract quantitative rules

### Sprint 1 Deliverables Document

Create `output/docs/sprint_1_completion.md`:

```markdown
# Sprint 1 Completion Report

**Date**: YYYY-MM-DD
**Status**: COMPLETE

## Deliverables

1. ✅ Workspace structure (25+ directories)
2. ✅ HMML 2.0 (87 method files)
3. ✅ Style guide (15 high-value verbs, 8 abstract rules)

## Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Method files | ≥50 | 87 |
| High-value verbs | ≥10 | 15 |
| Abstract rules | ≥5 | 8 |

## Next: Sprint 2
```

---

## Sprint 2: Brain & Soul (Days 4-8)

### Objective

Implement the **cognitive** (Brain) and **narrative** (Soul) capabilities.

### Deliverables

#### Day 4-5: Metacognition Agent

**Tasks**:
1. Implement `log_analyzer.py`
2. Create `@metacognition_agent` prompt
3. Test on sample training log

**Files Created**:
- `tools/log_analyzer.py` (~480 lines)
- `agents/metacognition_agent.md` (~350 lines)
- `templates/narrative_arcs/iterative_refinement.md`
- `templates/narrative_arcs/onion_peeling.md`
- `templates/narrative_arcs/comparative_evolution.md`

**Verification**:
```bash
# Test log analyzer
python tools/log_analyzer.py \
    --input sample_logs/training_full.log \
    --output logs/summary.json

# Verify JSON
cat logs/summary.json | jq '.struggles'

# Test narrative arc generation (manual)
# 1. Create sample dev_diary.md
# 2. Run @metacognition_agent (via LLM)
# 3. Check narrative_arc_1.md output (Iterative Refinement style)
```

---

#### Day 6-7: Narrative Weaver

**Tasks**:
1. Create `@narrative_weaver` prompt
2. Create paper outline template
3. Test outline generation

**Files Created**:
- `agents/narrative_weaver.md` (~450 lines)
- `templates/writing/paper_outline_template.md`
- `templates/writing/abstract_template.md`
- `templates/narrative_arcs/observation_implication.md`

**Verification**:
```bash
# Manual test
# 1. Use narrative_arc_1.md as input
# 2. Run @narrative_weaver
# 3. Check paper_outline.md has:
#    - Red thread sentence
#    - Section-by-section structure
#    - Figure caption templates (Protocol 15 compliant)
```

---

#### Day 8: Visualizer Mode B

**Tasks**:
1. Create `@visualizer` Mode B enhancement
2. Test Mermaid diagram generation

**Files Created**:
- `agents/visualizer_enhancement.md` (~150 lines)

**Verification**:
```bash
# Test Mermaid rendering
# 1. Generate sample diagram via Mode B
# 2. Render with mermaid-cli:
mmdc -i diagram.mmd -o diagram.png

# Check output exists and is valid PNG
file diagram.png
```

---

### Sprint 2 Success Criteria

- [ ] `log_analyzer.py` compresses logs to <10KB JSON
- [ ] `narrative_arc_1.md` contains ≥3 insights
- [ ] Each insight has observation + mechanism + implication
- [ ] `paper_outline.md` has paragraph-level detail
- [ ] All figure captions use Observation-Implication pattern
- [ ] Mode B generates valid Mermaid syntax

### Sprint 2 Integration Test

**End-to-End Test Scenario**:

1. **Input**: Training log with gradient explosion at epoch 50
2. **Run `log_analyzer.py`**: Should detect oscillation
3. **Create `dev_diary.md`**: Document the struggle
4. **Run @metacognition_agent**: Should generate `narrative_arc.md`
5. **Run @narrative_weaver**: Should create `paper_outline.md`
6. **Verify**: Outline section 3.3 references the gradient issue

**Success**: The gradient explosion appears as an insight in Section 3.3 with physical interpretation.

---

## Sprint 3: Fangs & Shield (Days 9-14)

### Objective

Implement **quality assurance** (Fangs) and **anti-mediocrity** (Shield) systems.

### Deliverables

#### Day 9-10: Judge Zero

**Tasks**:
1. Create `@judge_zero` prompt
2. Create judgment report template
3. Implement scoring logic

**Files Created**:
- `agents/judge_zero.md` (~250 lines)
- `templates/writing/judgment_report_template.md`
- `templates/ANTI_PATTERNS.md`

**Verification**:
```bash
# Manual test
# 1. Create sample paper with abstract空洞 (0 numbers)
# 2. Run @judge_zero
# 3. Check judgment_report.md:
#    - Persona C should flag abstract issue
#    - Score should be < 70
#    - Kill List should contain the issue
```

---

#### Day 11-12: Knowledge Librarian

**Tasks**:
1. Create `@knowledge_librarian` prompt
2. Test domain classification
3. Test method recommendation

**Files Created**:
- `agents/knowledge_librarian.md` (~350 lines)
- `templates/knowledge_base/suggested_methods_template.md`

**Verification**:
```bash
# Test domain classification
# 1. Input: Problem with keywords "epidemic", "network", "spread"
# 2. Run @knowledge_librarian (Phase 0.2)
# 3. Check suggested_methods.md:
#    - Should classify as Epidemiology + Network Science
#    - Should recommend SIR-Network (⭐⭐⭐⭐⭐)
#    - Should ban basic SIR (unless justified)
```

---

#### Day 13: Protocol 13 (DEFCON 1)

**Tasks**:
1. Enhance Protocol 13 specification
2. Create DEFCON 1 log template
3. Test ticket generation

**Files Enhanced**:
- `v3-1-0_protocols/26_protocol_13_mock_court_rewind.md`

**Verification**:
```bash
# Integration test
# 1. @judge_zero REJECT triggers
# 2. @director creates tickets from Kill List
# 3. Verify ticket assignments match specification
```

---

#### Day 14: Automated Scoring

**Tasks**:
1. Implement `mmbench_score.py`
2. Test on sample paper

**Files Created**:
- `tools/mmbench_score.py` (~530 lines)

**Verification**:
```bash
python tools/mmbench_score.py \
    --paper output/paper/paper.pdf \
    --output output/docs/auto_score.json

# Check JSON output
cat output/docs/auto_score.json | jq '.final_score'
cat output/docs/auto_score.json | jq '.checks'
```

---

### Sprint 3 Success Criteria

- [ ] @judge_zero generates valid judgment reports
- [ ] @knowledge_librarian bans ≥3 mediocre methods per domain
- [ ] @knowledge_librarian recommends ≥2 O-Prize methods
- [ ] Protocol 13 tickets auto-assigned correctly
- [ ] `mmbench_score.py` outputs 0-100 score
- [ ] Automated checks detect Level 1 fatal flaws

### Sprint 3 Integration Test

**Full Pipeline Test**:

1. **Input**: 2024 Problem C (epidemic)
2. **Phase 0.2**: @knowledge_librarian recommends SIR-Network
3. **Phase 5.8**: @metacognition extracts insights from training (Iterative Refinement)
4. **Phase 7**: @narrative_weaver creates outline (Baseline/Limitation/Revision)
5. **Phase 9.1**: @judge_zero reviews paper
6. **If REJECT**: Protocol 13 activates
7. **After fixes**: Re-review passes

**Success**: Complete cycle from problem → paper → judgment → revision → approval

---

## Post-Implementation Tasks

### Documentation

Create final documentation:

1. **User Manual**: How to use v3.1.0 system
2. **Agent Reference**: Quick reference for all 18 agents
3. **Protocol Flowchart**: Visual workflow of all phases
4. **Troubleshooting Guide**: Common issues and fixes

### Code Quality

Run quality checks:

```bash
# Python linting
pylint tools/*.py

# Type checking
mypy tools/*.py

# Test coverage
pytest tests/ --cov=tools/
```

### Performance Benchmarks

Measure performance:

| Component | Target | Acceptance |
|-----------|--------|------------|
| `log_analyzer.py` | <30s for 1GB log | <60s |
| `style_analyzer.py` | <5min for 10 PDFs | <10min |
| `mmbench_score.py` | <10s for 20-page PDF | <30s |
| HMML 2.0 search | <1s for keyword query | <2s |

---

## Rollback Plan

If issues arise, rollback procedure:

1. **Preserve v3.0.0**: Keep v3.0.0 directory intact
2. **Feature Flags**: Disable v3.1.0 agents if needed
3. **Gradual Migration**: Enable features incrementally

**Rollback Command**:
```bash
# Disable v3.1.0 agents
mv agents/ agents_v3.1.0_disabled/

# Use v3.0.0 agents
cp -r ../v3-0-0/agents/ agents/
```

---

## Success Metrics

### Sprint Completion

- [ ] Sprint 1: All tools functional
- [ ] Sprint 2: Narrative pipeline works end-to-end
- [ ] Sprint 3: Quality gates functional

### System Integration

- [ ] All 18 agents defined
- [ ] All 5 new phases implemented
- [ ] All 3 new protocols functional
- [ ] HMML 2.0 has ≥80 methods
- [ ] Templates exist for all output formats

### Quality Gates

- [ ] No breaking changes to v3.0.0 functionality
- [ ] All Python tools have unit tests
- [ ] Integration test passes (Problem C scenario)
- [ ] Documentation complete

---

## Version History

- **v1.0** (2026-01-25): Initial implementation guide from plan
