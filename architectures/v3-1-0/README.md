# MCM-Killer Architecture v3.1.0

> **Version**: v3.1.0 (Cognitive Narrative & Adversarial Evolution)
> **Date**: 2026-01-24
> **Purpose**: Complete detailed architecture with cognitive narrative and adversarial validation
> **Status**: Complete ✅

---

## Version Summary

**v3.1.0** is a major evolutionary release that:

1. **Adds Cognitive Narrative Layer**: Transform "errors and struggles" into "research insights"
2. **Adds Adversarial Quality System**: Red-blue team confrontation for地狱级 review
3. **Adds Dynamic Knowledge Base**: HMML 2.0 with active retrieval and metadata
4. **Adds Academic Style Alignment**: Learning from O-Prize reference papers
5. **Adds Self-Evolution Mechanism**: Continuous improvement through benchmarking
6. **Maintains Backward Compatibility**: All v3.0.0 protocols, agents, and phases preserved

---

## What's New in v3.1.0

### Quantitative Changes

| Dimension | v3.0.0 | v3.1.0 | Change |
|-----------|--------|--------|--------|
| **Agents** | 14 | 18 | +4 new (+28%) |
| **Phases** | 10 | 13 | +3 new (+30%) |
| **Protocols** | 12 | 15 | +3 new (+25%) |
| **Knowledge Base** | Static HMML | Dynamic HMML 2.0 | Restructured |
| **Output Quality** | Correct but flat | Insightful & deep | Narrative upgrade |
| **Validation** | Internal only | Adversarial red-blue | Quality leap |
| **Compute Overhead** | Baseline | ~105-110% | +5-10% for quality |

### Qualitative Changes

**v3.0.0**: "We get the right answer, efficiently and correctly."

**v3.1.0**: "We get the right answer, AND demonstrate deep thought process, AND validate ruthlessly, AND improve continuously."

### New Components

#### 4 New Agents
1. **@metacognition_agent** - Extract insights from training struggles
2. **@narrative_weaver** - Weave Hero's Journey narratives
3. **@knowledge_librarian** - Academic curator and method guardian
4. **@judge_zero** - Red team adversarial reviewer

#### 3 New Phases
- **Phase -1**: Style Guide Generation (pre-competition)
- **Phase 0.2**: Active Knowledge Retrieval (push advanced methods)
- **Phase 5.8**: Insight Extraction (metacognitive analysis)
- **Phase 6+**: Enhanced Visualization (Concept Weaver mode)
- **Phase 9.1**: Mock Judging (adversarial review)
- **Phase 11**: Self-Evolution (post-competition benchmarking)

#### 3 New Protocols
- **Protocol 13**: Mock Court Rewind (DEFCON 1 state machine)
- **Protocol 14**: Academic Style Alignment (mandatory style_guide.md loading)
- **Protocol 15**: Interpretation over Description (Observation-Implication enforcement)

---

## Document Structure

```
v3-1-0/
├── README.md                               # This file - Version overview and index
│
├── 00_architecture.md                      # Complete system overview (enhanced)
├── 01_version_comparison_v3-0_vs_v3-1.md  # Detailed version comparison
├── 02_llm_mm_agent_architecture.md         # Reference system (unchanged)
├── 03_mcm_killer_architecture.md          # Competition system (enhanced)
│
├── 04_protocols_summary.md                 # All 15 protocols summary
├── 05_agent_specifications.md              # All 18 agents overview
├── 06_phase_workflow.md                    # All 13 phases overview
├── 07_validation_gates.md                  # All validation gates overview
├── 08_output_structure.md                  # Output structure (enhanced)
├── 09_workspace_configuration.md           # Workspace execution guide (enhanced)
├── 10_data_authority.md                    # Data authority hierarchy (NEW)
│
├── v3-0-0_protocols/                        # v3.0.0 protocols (preserved)
│   ├── 10_director_file_reading_ban.md
│   ├── 11_time_validator_strict_mode.md
│   ├── 12_phase_5_parallel_workflow.md
│   ├── 13_time_validator_enhanced_analysis.md
│   ├── 14_code_translator_idealistic_mode.md
│   ├── 15_director_time_validator_handoff.md
│   ├── 16_model_design_expectations.md
│   ├── 17_validator_advisor_brief_format.md
│   ├── 18_phase5b_error_monitoring.md
│   ├── 19_emergency_delegation.md
│   └── 20_phase45_revalidation.md
│
├── v3-1-0_protocols/                        # v3.1.0 new protocols
│   ├── 21_phase_minus1_style_generation.md  # Phase -1 details
│   ├── 22_phase_0.2_active_retrieval.md      # Phase 0.2 details
│   ├── 23_phase_5.8_insight_extraction.md    # Phase 5.8 details
│   ├── 24_phase_9.1_mock_judging.md         # Phase 9.1 details
│   ├── 25_phase_11_self_evolution.md        # Phase 11 details
│   ├── 26_protocol_13_mock_court_rewind.md  # Protocol 13 details
│   ├── 27_protocol_14_style_alignment.md     # Protocol 14 details
│   └── 28_protocol_15_interpretation.md      # Protocol 15 details
│
├── 29_cognitive_narrative_framework.md       # Narrative framework deep dive
├── 30_hmml_2.0_specification.md             # Dynamic knowledge base spec
├── 31_workspace_v3-1-0_structure.md         # Enhanced workspace structure
│
└── m-orientation/                            # Design phase documents (reference)
    ├── README.md
    ├── A_CORE_ARCHITECTURE/
    │   ├── 00_ultimate_whitepaper.md
    │   ├── 01_version_comparison.md
    │   └── 02_cognitive_narrative_framework.md
    └── B_IMPLEMENTATION_GUIDES/
        ├── 01_sprint_1_foundation.md
        ├── 02_sprint_2_brain_soul.md
        └── 03_sprint_3_adversarial.md
```

---

## Core Philosophy: Narrative as Computation

### The Fundamental Shift

**v3.0.0 Papers**: "Flat narrative" - describing what was done
```
We used a Bayesian hierarchical model to predict Olympic medals.
The model achieved RMSE = 4.2.
```

**v3.1.0 Papers**: "Cognitive narrative" - showing the evolution of thought
```
We initially constructed a global hierarchical model (Model 1-A), but
encountered severe R-hat divergence (R-hat > 1.3, Figure 2a). This
divergence revealed fundamental data heterogeneity across regions, violating
the global pooling assumption. We refined the model with region-specific
partial pooling (Model 1-B), which both resolved convergence (R-hat < 1.05,
Figure 2b) and improved RMSE from 5.8 to 4.2.

This evolution demonstrates that 主办国效应 operates differently across
cultural/economic regions, suggesting that region-tailored policies are
more appropriate than global prescriptions (see Sensitivity Analysis, Section 4.2).
```

### Key Insight

**Errors, bugs, and struggles are NOT garbage—they are the raw material for "Model Limitations" and "Sensitivity Analysis" sections that distinguish O-Prize papers.**

---

## Two-System Architecture (Preserved)

### System 1: LLM-MM-Agent (Reference/Stable)

**Location**: `clean version/LLM-MM-Agent/`

**Purpose**: Research prototype published at NeurIPS 2025 and ICML 2025

**Status**: **UNCHANGED** in v3.1.0

### System 2: MCM-Killer (Competition → Enhanced)

**Location**: `MCM-Killer/workspace/2025_C/`

**Purpose**: Competition-optimized system with cognitive narrative and adversarial validation

**Status**: **ENHANCED** in v3.1.0 with:
- 4 new agents
- 3 new phases
- 3 new protocols
- Enhanced narrative quality
- Adversarial validation

---

## 15 Protocols Overview

### v3.0.0 Protocols (Preserved - 12 protocols)

**All 12 protocols from v3.0.0 are preserved without modification:**

1. **@director File Reading Ban** - Prevent evaluation contamination
2. **@time_validator Strict Mode** - Reject lazy implementations
3. **Enhanced Time Estimation** - Improve prediction accuracy
4. **Phase 5 Parallel Workflow** - Save 6-12 hours
5. **@code_translator Idealistic Mode** - Enforce perfect implementation
6. **48-Hour Escalation Protocol** - Decision framework
7. **@director/@time_validator Handoff** - Standardized communication
8. **Model Design Expectations** - Systematic validation
9. **@validator/@advisor Brief Format** - Fast decision-making
10. **Phase 5B Error Monitoring** - Prevent lost errors
11. **Emergency Convergence Delegation** - 8× faster response
12. **Phase 4.5 Re-Validation** - 8× fraud reduction

**Details**: See `v3-0-0_protocols/` directory

### v3.1.0 New Protocols (3 new)

13. **Mock Court Rewind** (Protocol 13) - DEFCON 1 adversarial review
14. **Academic Style Alignment** (Protocol 14) - Mandatory style_guide.md loading
15. **Interpretation over Description** (Protocol 15) - Observation-Implication enforcement

**Details**: See `v3-1-0_protocols/` directory

---

## 18 Agents Overview

### v3.0.0 Agents (14 - Preserved)

All 14 v3.0.0 agents are preserved with unchanged core functionality:

| Agent | v3.0.0 Role | v3.1.0 Status |
|-------|-----------|--------------|
| reader | PDF reader | ✅ Unchanged |
| researcher | Method suggestor | ✅ Enhanced (Phase 0.2 integration) |
| modeler | Math architect | ✅ Unchanged |
| feasibility_checker | Tech assessor | ✅ Unchanged |
| data_engineer | Data expert | ✅ Unchanged |
| code_translator | Math-to-code | ✅ Enhanced (dev_diary.md) |
| model_trainer | Training executor | ✅ Unchanged |
| validator | Quality checker | ✅ Unchanged |
| visualizer | Visual designer | ✅ Enhanced (Mode B: Concept Weaver) |
| writer | Paper author | ✅ Enhanced (style constraint) |
| summarizer | Summary expert | ✅ Unchanged |
| editor | Polisher | ✅ Enhanced (style constraint) |
| advisor | Quality advisor | ✅ Unchanged |
| time_validator | Anti-fraud guardian | ✅ Unchanged |
| **director** | **Team coordinator** | ✅ **Unchanged** |

### v3.1.0 New Agents (4)

| Agent | Role | Integration Point |
|-------|------|-------------------|
| **@metacognition_agent** | Philosopher & Forensic Analyst | Phase 5.8 (NEW) |
| **@narrative_weaver** | Story Director | Phase 7 (before @writer) |
| **@knowledge_librarian** | Academic Curator & Method Guardian | Phase -1, Phase 0.2 (NEW) |
| **@judge_zero** | Red Team Critic & Gatekeeper | Phase 9.1 (NEW) |

---

## 13 Phases Overview

### v3.0.0 Phases (10 - Preserved)

All 10 v3.0.0 phases are preserved:
```
0 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5A → 5B → 5.5 → 6 → 6.5 → 7 → 7.5 → 8 → 9 → 9.5 → 10
```

### v3.1.0 New Phases (3 new phases inserted)

```
-1 → 0 → 0.2 → 0.5 → 1 → 1.5 → 2 → 3 → 4 → 4.5 → 5A → 5B → 5.5 → 5.8 → 6 → 6.5 → 7 → 7.5 → 8 → 9 → 9.1 → 9.5 → 10 → 11
   ^    ^       ^                                                                              ^        ^
   |    |       |                                                                              |        |
  New  New      New                                                                             New      New
```

**Phase Details**:
- **Phase -1** (NEW): Style Guide Generation - Learn from O-Prize papers
- **Phase 0.2** (NEW): Active Knowledge Retrieval - Push advanced methods
- **Phase 5.8** (NEW): Insight Extraction - Metacognitive analysis
- **Phase 6+** (ENHANCED): Dual-mode visualization (data + concept)
- **Phase 9.1** (NEW): Mock Judging - Adversarial review
- **Phase 11** (NEW): Self-Evolution - Post-competition benchmarking

---

## Reading Guide

### For Complete Understanding (Recommended Order)

**Start here**: `README.md` (this file)

**Step 1: Understand Architecture Evolution**
1. `01_version_comparison_v3-0_vs_v3-1.md` - What changed and why
2. `00_architecture.md` - Complete system overview
3. `29_cognitive_narrative_framework.md` - Narrative philosophy

**Step 2: Understand Components**
4. `04_protocols_summary.md` - All 15 protocols
5. `05_agent_specifications.md` - All 18 agents
6. `06_phase_workflow.md` - All 13 phases
7. `07_validation_gates.md` - All validation gates
8. `08_output_structure.md` - Output structure (enhanced)
9. `10_data_authority.md` - Data authority hierarchy

**Step 3: Learn Execution**
10. `09_workspace_configuration.md` - Complete execution guide
11. `31_workspace_v3-1-0_structure.md` - Enhanced workspace structure

**Step 4: Study Protocols (v3.0.0)**
12. `v3-0-0_protocols/10-20_*.md` - All 12 v3.0.0 protocols

**Step 5: Study Protocols (v3.1.0 NEW)**
13. `v3-1-0_protocols/21-28_*.md` - All 6 new v3.1.0 protocols

**Step 6: Deep Dives**
14. `30_hmml_2.0_specification.md` - Dynamic knowledge base

**Step 7: Reference Implementation Design**
15. `m-orientation/` - Design phase documents and Sprint guides

### Quick Reference

**For What Changed**: `01_version_comparison_v3-0_vs_v3-1.md`
**For Protocol Details**: `04_protocols_summary.md` then protocol-specific documents
**For Execution**: `09_workspace_configuration.md`
**For New Features**: `29_cognitive_narrative_framework.md`

---

## Migration from v3.0.0

### Compatibility Guarantee

✅ **100% Backward Compatible**

- All 14 v3.0.0 agents: Preserved (3 enhanced, none removed)
- All 10 v3.0.0 phases: Preserved (3 inserted, none removed)
- All 12 v3.0.0 protocols: Preserved (3 added, none removed)

### What Requires Action

**For existing v3.0.0 users:**

1. **No immediate changes required** - All existing workflows continue to work
2. **Optional adoption** - Can adopt v3.1.0 features incrementally:
   - Sprint 1 (Days 1-3): Set up enhanced workspace
   - Sprint 2 (Days 4-8): Add cognitive narrative agents
   - Sprint 3 (Days 9-14): Add adversarial validation

3. **Migration path**: See `m-orientation/B_IMPLEMENTATION_GUIDES/`

### How to Migrate

**Option A: Full Migration (15 days)**
- Follow Sprint 1-3 guides in `m-orientation/B_IMPLEMENTATION_GUIDES/`
- End state: Full v3.1.0 system operational

**Option B: Incremental Adoption**
- Phase 1: Adopt HMML 2.0 only
- Phase 2: Add @metacognition_agent
- Phase 3: Add @judge_zero
- Phase 4: Enable all features

**Option C: Continue v3.0.0**
- All existing functionality preserved
- No action required
- Upgrade when ready

---

## Document Statistics

| Category | Documents | Total Size | Status |
|----------|-----------|------------|--------|
| Core Architecture | 4 | ~80KB | ✅ Enhanced |
| Overview | 7 | ~200KB | ✅ Enhanced |
| v3.0.0 Protocols | 11 | ~180KB | ✅ Preserved |
| v3.1.0 Protocols | 8 | ~120KB | ✅ New |
| Deep Dives | 3 | ~60KB | ✅ New |
| Reference | 1 | ~10KB | ✅ Enhanced |
| **Total** | **34** | **~650KB** | **✅ Complete** |

---

## Key Innovations in v3.1.0

### 1. Cognitive Narrative Framework
- **Hero's Journey Template**: Transform struggles into research insights
- **Observation-Implication Protocol**: Every data point paired with meaning
- **Metacognitive Agent**: Extracts "Aha!" moments from training logs

### 2. Adversarial Quality System
- **@judge_zero**: Three-persona评审 (Statistician + Domain Expert + Exhausted Editor)
- **DEFCON 1**: Emergency repair mode when paper rejected
- **Mercy Rule**: Prevent infinite loops while maintaining quality

### 3. Dynamic Knowledge Base (HMML 2.0)
- **Structured Methods**: Domain → Subdomain → Method hierarchy
- **Metadata Enrichment**: narrative_value, common_pitfalls, O-Prize examples
- **Active Retrieval**: @knowledge_librarian pushes advanced methods

### 4. Academic Style Alignment
- **Phase -1**: Automatically learn from O-Prize papers
- **style_guide.md**: Generated rules for academic writing
- **Protocol 14**: Mandatory style compliance for all text agents

### 5. Self-Evolution Mechanism
- **Phase 11**: Post-competition automated scoring
- **mmbench_score.py**: Rule-based paper evaluation
- **Trend Analysis**: Track improvement across multiple competitions

---

## System Requirements

### LLM-MM-Agent (Reference System)
- Python 3.10+
- Dependencies in `clean version/LLM-MM-Agent/requirements.txt`
- API key for supported LLM

### MCM-Killer v3.1.0 (Enhanced System)
- Claude Code CLI
- Python 3.10+
- Virtual environment support
- **Additional Requirements**:
  - `pdfplumber` or `PyPDF2` for PDF analysis
  - `spacy` for NLP (optional, for enhanced style analysis)
  - `mermaid-cli` for concept diagram rendering

---

## Support and Documentation

### Architecture Questions
- **System overview**: `00_architecture.md`
- **Version comparison**: `01_version_comparison_v3-0_vs_v3-1.md`
- **Narrative framework**: `29_cognitive_narrative_framework.md`

### Protocol Questions
- **Summary**: `04_protocols_summary.md`
- **v3.0.0 Details**: `v3-0-0_protocols/10-20_*.md`
- **v3.1.0 Details**: `v3-1-0_protocols/21-28_*.md`

### Execution Questions
- **Agents**: `05_agent_specifications.md`
- **Workflow**: `06_phase_workflow.md`
- **Validation**: `07_validation_gates.md`
- **Execution**: `09_workspace_configuration.md`

### Implementation Guidance
- **Design phase**: `m-orientation/README.md`
- **Sprint guides**: `m-orientation/B_IMPLEMENTATION_GUIDES/`

---

## Quick Start

### Using LLM-MM-Agent (Reference)

```bash
cd "clean version/LLM-MM-Agent"
python MMAgent/main.py --key "your_api_key" --task "2024_C" --model_name "gpt-4o"
```

### Using MCM-Killer v3.0.0 (Classic Mode)

**Step 1**: Navigate to workspace
```bash
cd "MCM-Killer/workspace/2025_C"
```

**Step 2**: Run with v3.0.0 workflow
- All 14 agents operational
- All 10 phases functional
- All 12 protocols enforced

### Using MCM-Killer v3.1.0 (Enhanced Mode)

**Step 1**: Navigate to workspace
```bash
cd "MCM-Killer/workspace/2025_C"
```

**Step 2**: Enable v3.1.0 features
1. Review `m-orientation/README.md`
2. Follow Sprint 1-3 implementation guides
3. Enable new agents and phases gradually

---

## Version History

| Version | Date | Type | Key Changes |
|---------|------|------|-------------|
| v2.3.0 | 2025-12-28 | Initial | First architecture documentation |
| v2.4.0 | 2026-01-10 | Enhancement | Modular architecture + agent directory |
| v2.5.7 | 2026-01-19 | Enhancement | 10 critical protocols |
| v2.5.9 | 2026-01-20 | Bugfix | Phase 4.5 re-validation |
| v3.0.0 | 2026-01-24 | Complete | Two-system architecture, 22 documents |
| **v3.1.0** | **2026-01-24** | **🚀 EVOLUTIONARY** | **Cognitive narrative + adversarial validation** |

---

## Contributors

- **Architecture Design**: MCM-Killer Development Team
- **Cognitive Narrative Framework**: Based on Claude + Gemini dialogue series
- **Adversarial System**: Red-blue team confrontation design
- **Documentation**: v3.1.0 Complete Documentation Team

---

## License

Proprietary - For internal competition use only.

---

**Document Version**: v3.1.0
**Last Updated**: 2026-01-24
**Status**: Complete ✅

**Next**: Read `01_version_comparison_v3-0_vs_v3-1.md` for detailed changes
