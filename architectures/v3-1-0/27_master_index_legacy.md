# MCM-Killer v3.1.0 - Master Index

> **Version**: v3.1.0 (Consolidated)
> **Date**: 2026-01-25
> **Purpose**: Complete index and navigation guide for v3.1.0 architecture

---

## Quick Navigation

### **Start Here**
- **[README.md](./README.md)** - Overview and introduction
- **[ARCHITECTURE_COMPLETE.md](./ARCHITECTURE_COMPLETE.md)** - Complete architecture specification

### **Version Comparison**
- **[01_version_comparison.md](./01_version_comparison.md)** - What's new in v3.1.0

### **Agents**
- **[ARCHITECTURE_COMPLETE.md](./ARCHITECTURE_COMPLETE.md)** - All 18 agents specified (Part 2)
- **[agents/](./agents/)** - Individual agent prompt files

### **Workflow**
- **[ARCHITECTURE_PART2_PHASES.md](./ARCHITECTURE_PART2_PHASES.md)** - Complete 13-phase workflow

### **Protocols**
- **[PROTOCOLS_COMPLETE.md](./PROTOCOLS_COMPLETE.md)** - All 15 protocols consolidated

### **Supporting Documents**
- **[ARCHITECTURE_PART3_NARRATIVE.md](./ARCHITECTURE_PART3_NARRATIVE.md)** - Narrative framework, workspace, tools
- **[knowledge_library_specification.md](./knowledge_library_specification.md)** - HMML 2.0 specification

---

## Document Hierarchy

```
v3-1-0/
├── README.md                          # Entry point
├── MASTER_INDEX.md                    # This file
│
├── Core Architecture
│   ├── ARCHITECTURE_COMPLETE.md       # Main architecture + 18 agents
│   ├── ARCHITECTURE_PART2_PHASES.md   # 13-phase detailed workflow
│   ├── ARCHITECTURE_PART3_NARRATIVE.md# Narrative, workspace, tools
│   └── PROTOCOLS_COMPLETE.md          # All 15 protocols
│
├── Reference Documents
│   ├── 01_version_comparison.md       # v3.0.0 vs v3.1.0
│   ├── knowledge_library_specification.md # HMML 2.0
│   ├── implementation_guide.md        # 3-sprint roadmap
│   └── testing_guide.md               # Testing strategy
│
├── agents/                            # Agent prompt files
│   ├── metacognition_agent.md
│   ├── narrative_weaver.md
│   ├── knowledge_librarian.md
│   ├── judge_zero.md
│   ├── code_translator_enhancement.md
│   └── visualizer_enhancement.md
│
├── templates/                         # Template files
│   ├── ANTI_PATTERNS.md
│   ├── narrative_arcs/
│   │   ├── iterative_refinement.md
│   │   ├── onion_peeling.md
│   │   ├── comparative_evolution.md
│   │   └── observation_implication.md
│   ├── writing/
│   │   ├── abstract_template.md
│   │   ├── dev_diary_entry.md
│   │   ├── judgment_report_template.md
│   │   └── paper_outline_template.md
│   └── knowledge_base/
│       ├── method_file_template.md
│       └── suggested_methods_template.md
│
└── tools/                             # Python tools
    ├── style_analyzer.py
    ├── log_analyzer.py
    ├── mmbench_score.py
    ├── init_workspace.py
    └── migrate_hmml.py
```

---

## Reading Guides

### For System Architects

**Goal**: Understand complete system design

**Reading Order**:
1. README.md - Overview
2. ARCHITECTURE_COMPLETE.md - Complete architecture (Parts 1-3)
3. ARCHITECTURE_PART2_PHASES.md - 13-phase workflow details
4. ARCHITECTURE_PART3_NARRATIVE.md - Cognitive narrative framework
5. knowledge_library_specification.md - HMML 2.0 knowledge base

---

### For Implementation Engineers

**Goal**: Implement the system

**Reading Order**:
1. README.md - Overview
2. ARCHITECTURE_PART2_PHASES.md - How phases work
3. ARCHITECTURE_COMPLETE.md - Agent specifications
4. implementation_guide.md - 3-sprint roadmap
5. testing_guide.md - Testing strategy

---

### For Competition Participants

**Goal**: Use the system in competition

**Reading Order**:
1. README.md - Overview
2. ARCHITECTURE_PART2_PHASES.md - Phase sequence
3. ARCHITECTURE_COMPLETE.md - Agent responsibilities
4. PROTOCOLS_COMPLETE.md - All 15 protocols

---

### For Prompt Engineers

**Goal**: Understand agent prompts and constraints

**Reading Order**:
1. ARCHITECTURE_COMPLETE.md - Agent specifications
2. agents/ - Individual agent prompts
3. PROTOCOLS_COMPLETE.md - Protocol enforcement (especially 13-15)
4. ARCHITECTURE_PART3_NARRATIVE.md - Narrative templates

---

## Key Concepts

### Cognitive Narrative Framework

**Documents**:
- ARCHITECTURE_PART3_NARRATIVE.md (Part 5)
- PROTOCOLS_COMPLETE.md (Phase 5.8, Protocol 15)

**Core Idea**: Transform technical struggles into research insights

**Key Agents**: @metacognition_agent, @narrative_weaver

---

### Adversarial Validation

**Documents**:
- PROTOCOLS_COMPLETE.md (Phase 9.1, Protocol 13)

**Core Idea**: Three-persona review catches flaws before submission

**Key Agent**: @judge_zero

---

### Anti-Mediocrity Enforcement

**Documents**:
- PROTOCOLS_COMPLETE.md (Phase 0.2)

**Core Idea**: Actively prevent choosing "safe but mediocre" methods

**Key Agent**: @knowledge_librarian

---

### Academic Style Alignment

**Documents**:
- PROTOCOLS_COMPLETE.md (Phase -1, Protocol 14, Protocol 15)

**Core Idea**: Enforce O-Prize-level writing quality

**Key Agents**: @writer, @editor, @narrative_weaver

---

## Quick Reference

### Agents (18 total)

**v3.0.0 Agents (14)**:
- @reader, @researcher, @modeler, @feasibility_checker
- @data_engineer, @code_translator, @model_trainer
- @validator, @visualizer, @writer, @summarizer
- @editor, @advisor, @time_validator
- **@director** (orchestrator)

**v3.1.0 New Agents (4)**:
- **@knowledge_librarian** - Style gen + Method pusher
- **@metacognition_agent** - Insight extraction
- **@narrative_weaver** - Story architecture
- **@judge_zero** - Adversarial reviewer

---

### Phases (13 total)

**Pre-Competition**:
- Phase -1: Deprecated (Style Guide Generation now on-demand)

**Understanding & Design**:
- Phase 0: Problem Understanding
- Phase 0.2: Active Knowledge Retrieval (NEW)
- Phase 0.5: Feasibility Check (GATE)
- Phase 1: Model Design
- Phase 1.5: Design Validation (GATE)

**Implementation**:
- Phase 2-3: Data Processing
- Phase 4: Code Translation
- Phase 4.5: Code Validation (GATE)
- Phase 5: Model Training
- Phase 5.5: Post-Training Validation (GATE)
- Phase 5.8: Insight Extraction (NEW)

**Results & Paper**:
- Phase 6: Result Generation
- Phase 7: Paper Generation
- Phase 9: Summary Generation
- Phase 9.1: Mock Judging (GATE, NEW)
- Phase 9.5: Final Package
- Phase 10: Submission

**Post-Competition**:
- Phase 11: Self-Evolution (NEW)

---

### Protocols (15 total)

**v3.0.0 Protocols (12)**:
1. @director File Reading Ban
2. @time_validator Strict Mode
3. Enhanced Time Estimation
4. Phase 5 Parallel Workflow
5. @code_translator Idealistic Mode
6. 48-Hour Escalation Protocol
7. @director/@time_validator Handoff
8. Model Design Expectations
9. @validator/@advisor Brief Format
10. Phase 5B Error Monitoring
11. Emergency Convergence Delegation
12. Phase 4.5 Re-Validation

**v3.1.0 New Protocols (3)**:
13. Mock Court Rewind (DEFCON 1)
14. Academic Style Alignment
15. Interpretation over Description

---

### Tools (5)

| Tool | Purpose | Phase |
|------|---------|-------|
| style_analyzer.py | Analyze O-Prize papers, generate style_guide.md | 0/On-demand |
| log_analyzer.py | Compress GB logs to JSON summary | 5.8 |
| mmbench_score.py | Automatically score MCM/ICM papers | 11 |
| init_workspace.py | Create v3.1.0 directory structure | Setup |
| migrate_hmml.py | Convert flat HMML.md to HMML 2.0 | Migration |

---

## Statistics

### Documentation Volume

- **Core Documents**: 12
- **Total Lines**: ~9,937
- **Agent Prompts**: 6
- **Templates**: 11
- **Python Tools**: 5

### Breakdown by Type

| Type | Count | Lines |
|------|-------|-------|
| Core Architecture | 4 | ~6,837 |
| Reference Docs | 4 | ~2,000 |
| Support Docs | 4 | ~1,100 |
| Agent Prompts | 6 | ~1,200 |
| Templates | 11 | ~500 |
| Tools | 5 | ~700 |

---

## Version History

### v3.1.0 (2026-01-25) - CURRENT

**Major Additions**:
- 4 new agents
- 5 new phases
- 3 new protocols
- Cognitive narrative framework
- Adversarial validation system
- HMML 2.0 knowledge base
- 5 Python tools

**Improvements**:
- Enhanced @code_translator (dev_diary.md)
- Enhanced @visualizer (dual-mode)
- Enhanced @writer (style constraint)
- Enhanced @editor (style constraint)

### v3.0.0 (Previous)

**Base System**:
- 14 agents
- 10 phases
- 12 protocols
- HMML 1.0 knowledge base

---

## Migration Path

### From v3.0.0 to v3.1.0

**Preserved Components**:
- All 14 v3.0.0 agents (4 enhanced)
- All 10 v3.0.0 phases
- All 12 v3.0.0 protocols

**New Components**:
- 4 new agents (specs in ARCHITECTURE_COMPLETE.md)
- 5 new phases (specs in PROTOCOLS_COMPLETE.md)
- 3 new protocols (specs in PROTOCOLS_COMPLETE.md)
- 5 Python tools (code in tools/)

**Migration Steps**:
1. Read ARCHITECTURE_COMPLETE.md (overview)
2. Read 01_version_comparison.md (what's new)
3. Read PROTOCOLS_COMPLETE.md (new protocols and phases)
4. Implement new agents (see agents/)
5. Test new phases (see ARCHITECTURE_PART2_PHASES.md)

---

## Quality Checklist

### For v3.1.0 Implementation

**Pre-Competition**:
- [ ] Phase -1: style_guide.md generated
- [ ] HMML 2.0 migrated from HMML 1.0
- [ ] All 5 tools tested (style_analyzer, log_analyzer, mmbench_score, init_workspace, migrate_hmml)
- [ ] Workspace initialized per ARCHITECTURE_PART3_NARRATIVE.md

**During Competition**:
- [ ] All 13 phases executed in order
- [ ] All 5 validation gates passed
- [ ] All 15 protocols followed
- [ ] VERSION_MANIFEST.json up-to-date

**Post-Competition**:
- [ ] Phase 11: Self-evolution completed
- [ ] Lessons learned documented
- [ ] Agent prompts refined
- [ ] Knowledge bases updated

---

## Support

### Questions?

**Architecture Questions**: See ARCHITECTURE_COMPLETE.md

**Implementation Questions**: See implementation_guide.md

**Protocol Questions**: See PROTOCOLS_COMPLETE.md

**Agent Questions**: See ARCHITECTURE_COMPLETE.md + agents/

**Workflow Questions**: See ARCHITECTURE_PART2_PHASES.md

---

## Summary

**MCM-Killer v3.1.0** is a complete autonomous AI system for mathematical modeling competitions featuring:

- **18 specialized agents** (14 preserved + 4 new)
- **13-phase workflow** (10 preserved + 5 inserted)
- **15 quality protocols** (12 preserved + 3 new)
- **Cognitive narrative framework** (transform struggles into insights)
- **Adversarial validation** (three-persona mock judging)
- **Anti-mediocrity enforcement** (active method pushing)
- **Continuous improvement** (self-evolution system)

**Vision**: Transform "correct" papers into "insightful" papers through cognitive narrative and adversarial quality control.

---

**Document**: MASTER_INDEX.md
**Version**: v3.1.0 (Consolidated)
**Last Updated**: 2026-01-25
**Status**: Complete

---

**End of Index**
