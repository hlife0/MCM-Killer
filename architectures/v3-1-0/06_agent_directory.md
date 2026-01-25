# Agent Directory: All 18 Agents

> **Purpose**: Quick reference index to all MCM-Killer agents
> **Organization**: By execution order, cluster, and role
> **Date**: 2026-01-25

---

## 📋 Quick Reference Table

| # | Agent | File | Lines | Cluster | Phase | Priority |
|---|-------|------|-------|---------|-------|----------|
| 1 | @reader | reader.md | 391 | Thinkers | 0 | P0 |
| 2 | @researcher | researcher.md | 418 | Thinkers | 0.5 | P0 |
| 3 | @modeler | modeler.md | 698 | Thinkers | 1.5 | P0 |
| 4 | @feasibility_checker | feasibility_checker.md | 1194 | Critics | 1.0 | P0 |
| 5 | @data_engineer | data_engineer.md | 1010 | Executors | 2 | P0 |
| 6 | @code_translator | code_translator_enhancement.md | 353 | Executors | 4-5A | P0 |
| 7 | @model_trainer | model_trainer.md | 401 | Executors | 5B | P0 |
| 8 | @validator | validator.md | 453 | Critics | 6 | P0 |
| 9 | @visualizer | visualizer_enhancement.md | 571 | Storytellers | 8 | P0 |
| 10 | @writer | writer_enhancement.md | 109 | Storytellers | 9 | P0 |
| 11 | @editor | editor.md | 478 | Storytellers | 9 | P0 |
| 12 | @summarizer | summarizer.md | 347 | Storytellers | 9.5 | P1 |
| 13 | @advisor | advisor.md | 265 | Critics | On-call | P1 |
| 14 | @time_validator | time_validator.md | 290 | Critics | Continuous | P0 |
| 15 | @director | director.md | 357 | Executors | Continuous | P0 |
| 16 | @metacognition_agent | metacognition_agent.md | 385 | Thinkers | 5.8 | P1 |
| 17 | @narrative_weaver | narrative_weaver.md | 588 | Storytellers | 7 | P1 |
| 18 | @knowledge_librarian | knowledge_librarian.md | 366 | Knowledge | -1, 0.2 | P1 |
| 19 | @judge_zero | judge_zero.md | 605 | Critics | 9.1 | P1 |

**Total**: 18 agents, 8,884 lines

**Priority Legend**:
- **P0**: Must-have for minimum viable system (10 agents)
- **P1**: Strongly recommended for O Award quality (9 agents)

---

## 🔄 Execution Order by Phase

### Phase -1: Style Guide Generation (Pre-Competition)
**Agent**: @knowledge_librarian
**File**: `agents/knowledge_librarian.md`
**Role**: Generate style_guide.md from O-Prize papers
**Output**: style_guide.md (academic writing rules)

---

### Phase 0: Problem Analysis
**Agent**: @reader
**File**: `agents/reader.md`
**Role**: PDF reader, strategic framing
**Input**: problem_statement.pdf
**Output**: problem_analysis.md

**O Award Focus**: Strategic problem framing (unique angle required)

---

### Phase 0.2: Protocol-Invoked Consultation
**Agent**: @knowledge_librarian
**File**: `agents/knowledge_librarian.md`
**Role**: Consult on advanced methods (On-Demand)
**Input**: Context request from Researcher
**Output**: suggested_methods.md

**O Award Focus**: Anti-mediocrity (provide rigorous options when asked)

---

### Phase 0.5: Method Selection
**Primary Agent**: @researcher
**File**: `agents/researcher.md`
**Role**: Method justification vs. ≥2 alternatives
**Input**: problem_analysis.md, suggested_methods.md
**Output**: method_selection.md

**Supporting Agent**: @feasibility_checker
**File**: `agents/feasibility_checker.md`
**Role**: Verify method is implementable in 72 hours
**Output**: feasibility_report.md

**O Award Focus**: Method choice justified, complexity matches data

---

### Phase 1.5: Mathematical Modeling
**Agent**: @modeler
**File**: `agents/modeler.md`
**Role**: Rigorous mathematical formulation
**Input**: method_selection.md
**Output**: model_design.md

**O Award Focus**: Clean notation, parameter interpretation, assumption transparency

---

### Phase 2: Data Engineering
**Agent**: @data_engineer
**File**: `agents/data_engineer.md`
**Role**: Clean, prepare, document data preprocessing
**Input**: problem_data files
**Output**: data/processed/, preprocessing_log.md

**O Award Focus**: Reproducibility (document ALL steps)

---

### Phase 4-5A: Code Implementation
**Agent**: @code_translator
**File**: `agents/code_translator_enhancement.md`
**Role**: Translate model to Python code
**Input**: model_design.md, data/processed/
**Output**: code/, dev_diary.md

**O Award Focus**: Struggle documentation (for metacognition)

---

### Phase 5B: Model Training
**Agent**: @model_trainer
**File**: `agents/model_trainer.md`
**Role**: Train/fit model, document failures
**Input**: code/, data/processed/
**Output**: results/, training_history.csv, dev_diary.md (updated)

**O Award Focus**: Physical interpretation of technical failures

---

### Phase 5.8: Insight Extraction
**Agent**: @metacognition_agent
**File**: `agents/metacognition_agent.md`
**Role**: Extract insights from dev_diary.md, training logs
**Input**: dev_diary.md, training_full.log
**Output**: narrative_arc.md

**O Award Focus**: Transform struggles → research insights (Iterative Refinement)

---

### Phase 6: Validation
**Agent**: @validator
**File**: `agents/validator.md`
**Role**: Multi-paradigm validation (statistical + physical + comparative)
**Input**: results/
**Output**: validation_report.md

**O Award Focus**: ≥2 validation methods, confidence intervals, sensitivity analysis

---

### Phase 7: Narrative Weaving
**Agent**: @narrative_weaver
**File**: `agents/narrative_weaver.md`
**Role**: Outline Coordinator (Non-dramatic organization)
**Input**: narrative_arc.md, validation_report.md
**Output**: paper_outline.md

**O Award Focus**: Conciseness (≤3 sentences for struggles), Observation-Implication

---

### Phase 8: Visualization
**Agent**: @visualizer
**File**: `agents/visualizer_enhancement.md`
**Role**: Create figures (Mode A: data, Mode B: concepts)
**Input**: results/, model_design.md
**Output**: figures/

**O Award Focus**: 300+ DPI, conclusionary captions (Protocol 15)

---

### Phase 9: Paper Writing
**Primary Agent**: @writer
**File**: `agents/writer_enhancement.md`
**Role**: Generate LaTeX paper from outline
**Input**: paper_outline.md, all previous outputs
**Output**: paper.tex

**Supporting Agent**: @editor
**File**: `agents/editor.md`
**Role**: LaTeX polish, Protocol 14/15 enforcement
**Output**: paper.pdf (compiled)

**O Award Focus**: LaTeX perfection (10-11pt font, booktabs, no blanks)

---

### Phase 9.1: Mock Judging (Adversarial Review)
**Agent**: @judge_zero
**File**: `agents/judge_zero.md`
**Role**: Red team review (3-persona system)
**Input**: paper.pdf
**Output**: judgment_report.md (PASS/REJECT)

**O Award Focus**: MANDATORY training (study ≥3 O Award papers before review)

**If REJECT** → Protocol 13 (DEFCON 1) activated

---

### Phase 9.5: Executive Summary
**Agent**: @summarizer
**File**: `agents/summarizer.md`
**Role**: One-page memo for decision-makers
**Input**: paper.pdf, validation_report.md
**Output**: one_page_memo.pdf

**O Award Focus**: Quantitative density (≥15 numbers), actionable recommendations

---

### Phase 10: Final Assembly
**Agent**: @director
**File**: `agents/director.md`
**Role**: Orchestrate all phases, enforce protocols
**Operates**: Continuously across all phases
**Output**: orchestration_log.md

**Responsibilities**:
- Phase sequencing & handoffs
- Protocol enforcement (all 15)
- Quality gate management
- Timeline tracking
- DEFCON 1 state machine (if @judge_zero rejects)

---

## 🎭 Organization by Cluster

### Cluster 1: Thinkers (认知与洞察) — The Brain

**Purpose**: Cognitive insight and analysis

| Agent | File | Role |
|-------|------|------|
| @reader | reader.md | Strategic problem framing |
| @researcher | researcher.md | Method selection & justification |
| @modeler | modeler.md | Mathematical formulation |
| @metacognition_agent | metacognition_agent.md | Insight extraction from failures |

**Key Strength**: Transform problems into solvable models with narrative value

---

### Cluster 2: Storytellers (叙事与表达) — The Soul

**Purpose**: Narrative communication and presentation

| Agent | File | Role |
|-------|------|------|
| @narrative_weaver | narrative_weaver.md | Outline Coordinator |
| @writer | writer_enhancement.md | LaTeX paper generation |
| @editor | editor.md | Style enforcement, Protocol 14/15 |
| @visualizer | visualizer_enhancement.md | Dual-mode visualization |
| @summarizer | summarizer.md | Executive memo creation |

**Key Strength**: Convert technical analysis into compelling O Award narratives

---

### Cluster 3: Critics (质量与对抗) — The Immune System

**Purpose**: Quality assurance and adversarial validation

| Agent | File | Role |
|-------|------|------|
| @judge_zero | judge_zero.md | Red team adversarial reviewer |
| @validator | validator.md | Multi-paradigm validation |
| @advisor | advisor.md | Strategic guidance when stuck |
| @feasibility_checker | feasibility_checker.md | Reality check gatekeeper |
| @time_validator | time_validator.md | Anti-fraud time auditor |

**Key Strength**: Prevent mediocrity, catch errors before submission

---

### Cluster 4: Executors (执行与实现) — The Body

**Purpose**: Hands-on implementation and orchestration

| Agent | File | Role |
|-------|------|------|
| @director | director.md | Pipeline orchestrator |
| @data_engineer | data_engineer.md | Data preprocessing |
| @code_translator | code_translator_enhancement.md | Math→code translation |
| @model_trainer | model_trainer.md | Model training & debugging |

**Key Strength**: Execute plans reliably, document struggles

---

### Cluster 5: Knowledge Management

**Purpose**: Curate and push advanced methods

| Agent | File | Role |
|-------|------|------|
| @knowledge_librarian | knowledge_librarian.md | HMML 2.0 consultant (On-Demand) |

**Key Strength**: Push team toward sophisticated O Award methods

---

## 🎯 Organization by Role

### Quality Gates (Must Pass Before Next Phase)

- **@feasibility_checker** (Phase 0.5): Block infeasible methods
- **@validator** (Phase 6): Block unvalidated results
- **@time_validator** (Continuous): Reject unrealistic time estimates
- **@judge_zero** (Phase 9.1): Final gatekeeper before submission

---

### On-Call Consultants

- **@advisor**: Called when agents get stuck (low confidence, time pressure)
- **@director**: Called for protocol violations, phase conflicts

---

### Continuous Monitors

- **@director**: Monitors all phases for sequencing, quality gates, timeline
- **@time_validator**: Monitors all estimates for realism

---

### Single-Phase Specialists

All other agents operate in specific phases (see execution order above)

---

## 📊 Agent Statistics

### By File Size (Lines of Code)

**Largest Agents** (most detailed):
1. @feasibility_checker - 1,194 lines (4-dimension analysis)
2. @data_engineer - 1,010 lines (comprehensive preprocessing)
3. @modeler - 698 lines (mathematical rigor)

**Focused Agents** (concise, specific):
1. @writer - 109 lines (LaTeX quality focus, references external standards)
2. @advisor - 265 lines (strategic patterns)
3. @time_validator - 290 lines (benchmark-driven)

---

### By O Award Criterion Coverage

| Criterion | Agents Trained | Count |
|-----------|----------------|-------|
| Abstract quality (≥3 numbers) | writer, editor, summarizer, judge_zero | 4 |
| Strategic framing | reader, researcher, narrative_weaver | 3 |
| Mathematical sophistication | modeler, researcher, feasibility_checker | 3 |
| Multi-paradigm validation | validator, advisor, judge_zero | 3 |
| Insight depth | metacognition_agent, narrative_weaver, model_trainer | 3 |
| LaTeX presentation | writer, editor, visualizer | 3 |
| Sensitivity analysis | validator, model_trainer, judge_zero | 3 |
| Assumption transparency | modeler, researcher, judge_zero | 3 |
| Code reproducibility | code_translator, data_engineer, model_trainer | 3 |
| Policy implications | summarizer, narrative_weaver, writer | 3 |

**Total O Award Coverage**: 10/10 criteria ✅

---

## 🔍 Finding the Right Agent

### By Problem Type

**"My method won't converge"**
→ @advisor (strategic guidance) + @model_trainer (debugging)

**"I don't know which method to use"**
→ @knowledge_librarian (push methods) + @researcher (justify selection)

**"My paper was rejected"**
→ @judge_zero (judgment report) + Protocol 13 (DEFCON 1)

**"My LaTeX looks unprofessional"**
→ @editor (LaTeX verification) + templates/writing/latex_formatting_standards.md

**"I'm running out of time"**
→ @time_validator (realistic estimates) + @director (activate Protocol 4)

**"My validation failed"**
→ @validator (multi-paradigm) + @advisor (simplify vs. debug decision)

---

### By Input/Output

**Need**: problem_analysis.md
→ **Use**: @reader

**Have**: method_selection.md → **Need**: feasibility_report.md
→ **Use**: @feasibility_checker

**Have**: model_design.md → **Need**: code/
→ **Use**: @code_translator

**Have**: dev_diary.md → **Need**: narrative_arc.md
→ **Use**: @metacognition_agent

**Have**: paper.tex → **Need**: judgment_report.md
→ **Use**: @judge_zero

---

## 📝 Agent File Naming Notes

### Standard Pattern (15 agents)
- Lowercase with underscores: `agent_name.md`
- Examples: reader.md, researcher.md, modeler.md

### Enhancement Suffix (3 agents)
- Pattern: `agent_name_enhancement.md`
- Agents: code_translator, visualizer, writer
- **Reason**: These agents have additional enhancement layers beyond base functionality

### Legacy Files
- `code_translator.md` (old version) - superseded by code_translator_enhancement.md
- `IMPLEMENTATION_STATUS.md` - tracking file, not agent prompt

---

## 🚀 Minimum Viable System (10 Agents)

**For basic MCM competition** (without O Award optimization):

1. @reader - Problem analysis
2. @researcher - Method selection
3. @modeler - Mathematical formulation
4. @data_engineer - Data preprocessing
5. @code_translator - Implementation
6. @model_trainer - Training
7. @validator - Validation
8. @writer - Paper writing
9. @director - Orchestration
10. @time_validator - Time management

**Estimated Setup Time**: 2-3 hours

---

## 🏆 O Award Quality System (All 18 Agents)

**For O Award targeting** (includes cognitive narrative + adversarial review):

- All 10 above **PLUS**:
11. @feasibility_checker - Reality checks
12. @editor - LaTeX polish
13. @visualizer - Professional figures
14. @summarizer - Executive memo
15. @advisor - Strategic guidance
16. @metacognition_agent - Insight extraction
17. @narrative_weaver - Outline Coordinator
18. @knowledge_librarian - Method consultant
19. @judge_zero - Adversarial review

**Estimated Setup Time**: 4-6 hours

---

## 🔗 Cross-References

**For detailed agent usage**:
- See: IMPLEMENTATION_GUIDE.md (3-sprint roadmap)
- See: AGENT_KNOWLEDGE_ACCESS.md (which agents need HMML 2.0)
- See: PROTOCOLS_COMPLETE.md (protocol enforcement by agent)

**For O Award training details**:
- See: O_AWARD_CRITERIA.md (10 critical characteristics)
- See: AGENT_ENHANCEMENT_SUMMARY.md (detailed enhancement notes)

**For integration**:
- See: INTEGRATION_SUMMARY.md (functional components usage)
- See: tools/system_prompts.py (get_system_prompt_for_agent function)

---

**Document Version**: 1.0
**Created**: 2026-01-25
**Total Agents**: 18
**Status**: Production Ready ✅
