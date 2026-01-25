# MCM-Killer v3.1.0: START HERE

> **👋 Welcome!** This is your entry point to the complete MCM-Killer v3.1.0 architecture.
> **Version**: v3.1.0-O-trained
> **Status**: Production Ready
> **Date**: 2026-01-25

---

## 🚀 Quick Start (5 Minutes)

### New to MCM-Killer?

**Read these 4 files in order:**

1. **00_readme.md** (5 min) - System overview, what's new in v3.1.0
2. **02_architecture_overview.md** (10 min) - Complete system design, 18-Agent Grid
3. **06_agent_directory.md** (3 min) - Index to all agent prompts
4. **07_implementation_guide.md** (15 min) - Step-by-step implementation roadmap

**Total**: 33 minutes to understand the entire system

---

### Implementing MCM-Killer?

**Follow this path:**

1. **Setup Workspace**
   ```bash
   python tools/4_init_workspace.py
   ```

2. **Integrate Functional Components** (P0: Must-have)
   - `tools/1_system_prompts.py` - Modular prompts (87% token savings)
   - `tools/2_safe_template.py` - Crash-proof template formatting
   - See: `22_integration_summary.md` for usage

3. **Follow Implementation Guide**
   - Read: `07_implementation_guide.md`
   - 3-sprint approach (Foundation → Brain/Soul → Fangs/Shield)

4. **Test System**
   - Read: `08_testing_guide.md`
   - Validate on historical MCM problem

---

### Looking for Something Specific?

| Need | File | Time |
|------|------|------|
| **System Overview** | 00_readme.md | 5 min |
| **Architecture Details** | 02_architecture_overview.md | 10 min |
| **Phase Workflow** | 03_architecture_phases.md | 15 min |
| **Agent Prompts** | agents/ directory (19 files) | - |
| **Protocols (15 total)** | 05_protocols_complete.md | 10 min |
| **O Award Criteria** | 10_o_award_criteria.md | 8 min |
| **Python Tools** | tools/ directory (8 files) | - |
| **Templates** | templates/ directory | - |

---

## 📚 Documentation Structure

### TIER 1: Core Documents (Sequential Reading)

**Read in order for complete understanding:**

```
01. 00_readme.md                       → System overview
02. 01_version_comparison.md           → v3.0.0 vs v3.1.0 detailed comparison
03. 02_architecture_overview.md        → System design (Part 1)
04. 03_architecture_phases.md          → All phases detailed
05. 04_architecture_narrative.md       → Cognitive narrative framework
06. 05_protocols_complete.md           → All protocols
07. 06_agent_directory.md              → 19 agent prompts index
08. 07_implementation_guide.md         → 3-sprint implementation
09. 08_testing_guide.md                → Testing strategy
```

**Estimated Reading Time**: 2-3 hours for complete mastery

---

### TIER 2: Reference Documents (Lookup as Needed)

**Quick reference materials:**

```
10. 10_o_award_criteria.md             → 10 critical characteristics
11. 11_knowledge_library_spec.md        → HMML 2.0 specification
12. 12_agent_knowledge_access.md        → Agent→knowledge mapping
13. 13_structure_reference.md           → Navigation guide
```

**Use When**: Need detailed reference for specific topics

---

### TIER 3: Supporting Documents (Completion Records)

**Historical/completion summaries:**

```
20. 20_final_summary.md                → v3.1.0-O-trained completion summary
21. 21_agent_enhancement_summary.md    → All 18 agents enhancement details
22. 22_integration_summary.md          → Functional components integration
23. 23_all_agents_legacy.md            → Legacy consolidated agent file
24. 24_completion_summary.md           → Historical completion record
25. 25_consolidation_plan.md           → Consolidation strategy (historical)
26. 26_consolidation_status.md         → Consolidation tracking (historical)
27. 27_master_index_legacy.md          → Legacy index
```

**Use When**: Understanding development history, completion status

---

## 🗂️ Directory Organization

```
v3-1-0/
│
├── [ROOT] - 19 documentation files
│   ├── Core docs (01-09) - Read sequentially
│   ├── Reference (10-13) - Lookup as needed
│   └── Supporting (20-27) - Historical records
│
├── agents/ - 18 agent prompts + status files
│   ├── Core modeling: reader, researcher, modeler
│   ├── Execution: data_engineer, code_translator, model_trainer
│   ├── Quality: validator, feasibility_checker, advisor, time_validator
│   ├── Presentation: visualizer, writer, editor, summarizer
│   ├── Cognitive: metacognition_agent, narrative_weaver
│   ├── Adversarial: judge_zero
│   ├── Knowledge: knowledge_librarian
│   └── Orchestration: director
│
├── templates/ - Narrative arcs, writing templates, knowledge base
│   ├── narrative_arcs/ - 4 story templates
│   ├── writing/ - 5 writing templates + LaTeX standards
│   └── knowledge_base/ - 2 method templates
│
└── tools/ - 8 Python tools
    ├── P0 (must-have): system_prompts.py, safe_template.py
    ├── P1 (recommended): journal_prompts.py
    ├── Setup: init_workspace.py, migrate_hmml.py
    └── Phase-specific: style_analyzer.py, log_analyzer.py, mmbench_score.py
```

---

## 🎯 Common User Paths

### Path 1: "I want to understand the system"

1. 00_readme.md (overview)
2. 02_architecture_overview.md (system design)
3. Browse agents/ directory (see what each agent does)
4. 05_protocols_complete.md (understand rules)

---

### Path 2: "I want to implement this for my team"

1. 00_readme.md (quick skim)
2. 07_implementation_guide.md (detailed read)
3. Setup: Run tools/4_init_workspace.py
4. Integrate: Follow 22_integration_summary.md
5. Test: Follow 08_testing_guide.md

---

### Path 3: "I want to improve an existing agent"

1. Find agent in agents/ directory
2. Read agent's O Award training section
3. Check 12_agent_knowledge_access.md (does it need new knowledge?)
4. Update agent prompt
5. Test changes

---

### Path 4: "I need O Award quality paper"

1. 10_o_award_criteria.md (understand standards)
2. agents/19_judge_zero.md (mandatory training protocol)
3. templates/writing/5_latex_formatting_standards.md (LaTeX quality)
4. agents/17_narrative_weaver.md (conciseness mandate)
5. agents/10_writer.md + agents/11_editor.md (execution)

---

## 🔧 Implementation Priority

### Must Implement (P0)

1. **Functional Components**
   - tools/system_prompts.py
   - tools/safe_template.py

2. **Core Agents**
   - @director (orchestration)
   - @reader → @researcher → @modeler (problem analysis)
   - @code_translator → @model_trainer (execution)
   - @validator (quality gate)
   - @writer → @editor (output)

### Strongly Recommended (P1)

3. **Enhanced Features**
   - tools/journal_prompts.py (metacognition)
   - @metacognition_agent + @narrative_weaver (cognitive narrative)
   - @judge_zero (adversarial review)

4. **HMML 2.0**
   - knowledge_library_specification.md
   - @knowledge_librarian
   - tools/migrate_hmml.py

### Optional (P2)

5. **Advanced Features**
   - Phase -1 (style_guide generation)
   - Phase 11 (self-evolution)
   - Full Protocol 13 (DEFCON 1)

---

## ❓ FAQ

### Q: Which agents are mandatory?

**Minimum viable system** (10 agents):
- @reader, @researcher, @modeler
- @data_engineer, @code_translator, @model_trainer
- @validator, @writer
- @director, @time_validator

### Q: What's the difference between 23_all_agents_legacy.md and agents/ directory?

- **23_all_agents_legacy.md**: Legacy consolidated file (kept for reference)
- **agents/ directory**: Current individual agent prompts (use these)

### Q: Do I need all 15 protocols?

**Minimum** (5 critical):
- Protocol 1: File Reading Ban
- Protocol 2: Strict Time Validation
- Protocol 4: Parallel Phase 5
- Protocol 13: DEFCON 1 (if using @judge_zero)
- Protocol 14: Style Alignment (if using style_guide.md)

### Q: Can I use this without HMML 2.0?

**Yes**, but you lose:
- Advanced method suggestions from @knowledge_librarian
- Anti-mediocrity filter
- O-Prize method database

### Q: How do I know if my implementation is O Award quality?

Run through:
1. 10_o_award_criteria.md (10 characteristics checklist)
2. @judge_zero mandatory review
3. templates/writing/5_latex_formatting_standards.md (10-point check)

---

## 🆘 Need Help?

### Issues by Category

| Issue | Resource |
|-------|----------|
| **Architecture questions** | 02_architecture_overview.md + Parts 2-3 |
| **Agent not working** | agents/ directory (check agent file) |
| **Protocol unclear** | 05_protocols_complete.md (all 15 detailed) |
| **Implementation stuck** | 07_implementation_guide.md (3-sprint roadmap) |
| **LaTeX looks bad** | templates/writing/5_latex_formatting_standards.md |
| **Paper rejected by @judge_zero** | Protocol 13 (DEFCON 1), check 10_o_award_criteria.md |
| **Agent needs knowledge** | 12_agent_knowledge_access.md (verify access) |

### Still Stuck?

1. Check 28_organization_audit.md (file organization reference)
2. Search 20_final_summary.md (completion summary)
3. Review 21_agent_enhancement_summary.md (detailed agent docs)

---

## 📋 Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v3.0.0 | 2026-01-24 | Two-system architecture (14 agents, 10 phases, 12 protocols) |
| **v3.1.0** | **2026-01-25** | **Cognitive narrative + adversarial validation** |
| v3.1.0-consolidated | 2026-01-25 | Reorganization/consolidation |
| **v3.1.0-O-trained** | **2026-01-25** | **All 18 agents trained on O Award criteria** |

---

## ✅ System Readiness

- ✅ All 18 agents complete with O Award training
- ✅ All 15 protocols documented
- ✅ All 13 phases specified
- ✅ 650+ lines functional components integrated
- ✅ LaTeX quality standards established
- ✅ Judge mandatory training protocol active
- ✅ **PRODUCTION READY**

---

**Next Step**: Read 00_readme.md for system overview, then follow your user path above.

**Document Version**: 1.0
**Created**: 2026-01-25
**Last Updated**: 2026-01-25
