# Directory Organization Audit: v3-1-0 Architecture

> **Audit Date**: 2026-01-25
> **Purpose**: Comprehensive check for uniformity, readability, and sequential clarity
> **Status**: Analysis Complete - Recommendations Provided

---

## Current State Analysis

### Directory Structure Overview

```
v3-1-0/
├── [ROOT LEVEL] - 19 documentation files (mixed naming conventions)
├── agents/ - 18 agent prompts + 1 status file
├── templates/ - 3 subdirectories (narrative_arcs, writing, knowledge_base)
└── tools/ - 8 Python files
```

---

## Issue #1: Inconsistent File Naming Conventions

### Root Level Files (19 files)

**THREE Different Naming Patterns Detected**:

#### Pattern A: UPPERCASE_UNDERSCORES (10 files)
```
AGENT_ENHANCEMENT_SUMMARY.md
AGENT_KNOWLEDGE_ACCESS.md
ALL_AGENTS_COMPLETE.md
ARCHITECTURE_COMPLETE.md
ARCHITECTURE_PART2_PHASES.md
ARCHITECTURE_PART3_NARRATIVE.md
COMPLETION_SUMMARY.md
CONSOLIDATION_PLAN.md
CONSOLIDATION_STATUS.md
FINAL_SUMMARY.md
INTEGRATION_SUMMARY.md
MASTER_INDEX.md
O_AWARD_CRITERIA.md
PROTOCOLS_COMPLETE.md
README.md
STRUCTURE.md
```

#### Pattern B: lowercase_underscores (3 files)
```
implementation_guide.md
knowledge_library_specification.md
testing_guide.md
```

#### Pattern C: Numeric prefix (1 file)
```
01_version_comparison.md
```

**❌ ISSUE**: Lack of uniformity makes navigation difficult

---

## Issue #2: Missing Sequential Organization

### Current Root Files Have No Clear Hierarchy

**User Journey NOT Clear**:
- Which file to read first?
- Which files are core vs. supporting?
- Which files are historical vs. current?

**Missing**:
- Clear numbering system for sequential reading
- Categorization (core, reference, historical)
- Entry point identification

---

## Issue #3: Agent Files Lack Standardization

### agents/ Directory (19 files)

**Inconsistent Naming**:
```
✅ Standard pattern (15 files):
   - reader.md
   - researcher.md
   - modeler.md
   - feasibility_checker.md
   - etc.

⚠️ Enhancement suffix (3 files):
   - code_translator_enhancement.md
   - visualizer_enhancement.md
   - writer_enhancement.md

❓ Legacy file (1 file):
   - code_translator.md (duplicate? superseded?)

📄 Status file (1 file):
   - IMPLEMENTATION_STATUS.md
```

**❌ ISSUE**: Confusing to know which is the "official" agent prompt

---

## Issue #4: Template Organization

### templates/ Subdirectories

**Current Structure**:
```
templates/
├── ANTI_PATTERNS.md (top-level, but conceptually fits elsewhere)
├── knowledge_base/
│   ├── method_file_template.md
│   └── suggested_methods_template.md
├── narrative_arcs/
│   ├── comparative_evolution.md
│   ├── hero_journey.md
│   ├── observation_implication.md
│   └── onion_peeling.md
└── writing/
    ├── abstract_template.md
    ├── dev_diary_entry.md
    ├── judgment_report_template.md
    ├── latex_formatting_standards.md
    └── paper_outline_template.md
```

**✅ GOOD**: Logical categorization
**⚠️ MINOR**: ANTI_PATTERNS.md should be in writing/ or have a dedicated category

---

## Issue #5: Tools Directory

### tools/ Python Files (8 files)

**Current Naming**:
```
init_workspace.py
journal_prompts.py
log_analyzer.py
migrate_hmml.py
mmbench_score.py
safe_template.py
style_analyzer.py
system_prompts.py
```

**✅ GOOD**: Consistent lowercase_underscore pattern
**⚠️ MINOR**: No clear priority ordering (which to implement first?)

---

## Recommended Reorganization

### Strategy: Three-Tier Naming System

**Tier 1**: Sequential Core Documents (00-09)
**Tier 2**: Reference Documents (10-19)
**Tier 3**: Supporting/Historical Documents (20-29)

---

### Proposed File Renaming Scheme

#### **TIER 1: Sequential Core (Entry Point → Architecture → Agents → Implementation)**

```
00_start_here.md                        [NEW - Entry point guide]
01_README.md                            [RENAME: README.md]
02_VERSION_COMPARISON.md                [RENAME: 01_version_comparison.md → 02]
03_ARCHITECTURE_COMPLETE.md             [RENAME: ARCHITECTURE_COMPLETE.md]
04_ARCHITECTURE_PHASES.md               [RENAME: ARCHITECTURE_PART2_PHASES.md]
05_ARCHITECTURE_NARRATIVE.md            [RENAME: ARCHITECTURE_PART3_NARRATIVE.md]
06_PROTOCOLS_COMPLETE.md                [RENAME: PROTOCOLS_COMPLETE.md]
07_AGENT_DIRECTORY.md                   [NEW - Index to all 18 agents]
08_IMPLEMENTATION_GUIDE.md              [RENAME: implementation_guide.md]
09_TESTING_GUIDE.md                     [RENAME: testing_guide.md]
```

#### **TIER 2: Reference Documents (Quick Lookup)**

```
10_O_AWARD_CRITERIA.md                  [RENAME: O_AWARD_CRITERIA.md]
11_KNOWLEDGE_LIBRARY_SPEC.md            [RENAME: knowledge_library_specification.md]
12_AGENT_KNOWLEDGE_ACCESS.md            [RENAME: AGENT_KNOWLEDGE_ACCESS.md]
13_STRUCTURE_REFERENCE.md               [RENAME: STRUCTURE.md]
```

#### **TIER 3: Supporting/Historical Documents (Archive)**

```
20_FINAL_SUMMARY.md                     [RENAME: FINAL_SUMMARY.md - completion summary]
21_AGENT_ENHANCEMENT_SUMMARY.md         [RENAME: AGENT_ENHANCEMENT_SUMMARY.md]
22_INTEGRATION_SUMMARY.md               [RENAME: INTEGRATION_SUMMARY.md]
23_ALL_AGENTS_COMPLETE.md               [RENAME: ALL_AGENTS_COMPLETE.md - legacy consolidated]
24_COMPLETION_SUMMARY.md                [RENAME: COMPLETION_SUMMARY.md - historical]
25_CONSOLIDATION_PLAN.md                [RENAME: CONSOLIDATION_PLAN.md - historical]
26_CONSOLIDATION_STATUS.md              [RENAME: CONSOLIDATION_STATUS.md - historical]
27_MASTER_INDEX.md                      [RENAME: MASTER_INDEX.md - needs update]
```

---

### Agent Files Standardization

#### **Proposal**: Remove "_enhancement" suffix, use numbered prefix

```
agents/
├── 00_AGENT_INDEX.md                   [NEW - Quick reference to all agents]
├── 01_reader.md                        [RENAME: reader.md]
├── 02_researcher.md                    [RENAME: researcher.md]
├── 03_modeler.md                       [RENAME: modeler.md]
├── 04_feasibility_checker.md           [RENAME: feasibility_checker.md]
├── 05_data_engineer.md                 [RENAME: data_engineer.md]
├── 06_code_translator.md               [MERGE: code_translator_enhancement.md → code_translator.md]
├── 07_model_trainer.md                 [RENAME: model_trainer.md]
├── 08_validator.md                     [RENAME: validator.md]
├── 09_visualizer.md                    [MERGE: visualizer_enhancement.md]
├── 10_writer.md                        [MERGE: writer_enhancement.md]
├── 11_editor.md                        [RENAME: editor.md]
├── 12_summarizer.md                    [RENAME: summarizer.md]
├── 13_advisor.md                       [RENAME: advisor.md]
├── 14_time_validator.md                [RENAME: time_validator.md]
├── 15_director.md                      [RENAME: director.md]
├── 16_metacognition_agent.md           [RENAME: metacognition_agent.md]
├── 17_narrative_weaver.md              [RENAME: narrative_weaver.md]
├── 18_knowledge_librarian.md           [RENAME: knowledge_librarian.md]
└── 19_judge_zero.md                    [RENAME: judge_zero.md]
```

**Numbering Rationale**: Follows execution order (Phase 0 → Phase 11)

---

### Tools Standardization

#### **Proposal**: Priority-based numbering

```
tools/
├── 0_TOOLS_INDEX.md                    [NEW - Implementation priority guide]
├── 1_system_prompts.py                 [RENAME: system_prompts.py - P0, use first]
├── 2_safe_template.py                  [RENAME: safe_template.py - P0, use first]
├── 3_journal_prompts.py                [RENAME: journal_prompts.py - P1]
├── 4_init_workspace.py                 [RENAME: init_workspace.py - Setup]
├── 5_migrate_hmml.py                   [RENAME: migrate_hmml.py - Setup]
├── 6_style_analyzer.py                 [RENAME: style_analyzer.py - Phase -1]
├── 7_log_analyzer.py                   [RENAME: log_analyzer.py - Phase 5.8]
└── 8_mmbench_score.py                  [RENAME: mmbench_score.py - Phase 11]
```

**Numbering Rationale**: Implementation priority (P0 → Setup → Phase-aligned)

---

### Templates Organization (Keep Current + Minor Fix)

```
templates/
├── narrative_arcs/
│   ├── 1_hero_journey.md               [RENAME: hero_journey.md]
│   ├── 2_onion_peeling.md              [RENAME: onion_peeling.md]
│   ├── 3_comparative_evolution.md      [RENAME: comparative_evolution.md]
│   └── 4_observation_implication.md    [RENAME: observation_implication.md]
├── writing/
│   ├── 1_abstract_template.md          [RENAME: abstract_template.md]
│   ├── 2_paper_outline_template.md     [RENAME: paper_outline_template.md]
│   ├── 3_dev_diary_entry.md            [RENAME: dev_diary_entry.md]
│   ├── 4_judgment_report_template.md   [RENAME: judgment_report_template.md]
│   ├── 5_latex_formatting_standards.md [RENAME: latex_formatting_standards.md]
│   └── 6_anti_patterns.md              [MOVE: ../ANTI_PATTERNS.md]
└── knowledge_base/
    ├── 1_method_file_template.md       [RENAME: method_file_template.md]
    └── 2_suggested_methods_template.md [RENAME: suggested_methods_template.md]
```

---

## New Files to Create

### 1. 00_start_here.md (Entry Point)

**Purpose**: First file users read, provides navigation map

**Contents**:
```markdown
# MCM-Killer v3.1.0: Start Here

## Quick Start (5 Minutes)
1. Read: 01_README.md (overview)
2. Read: 03_ARCHITECTURE_COMPLETE.md (system design)
3. Scan: 07_AGENT_DIRECTORY.md (18 agents index)
4. Execute: 08_IMPLEMENTATION_GUIDE.md (step-by-step)

## Full Documentation Path
**Sequential Reading Order**:
- 00-09: Core documents (read in order)
- 10-13: Reference (lookup as needed)
- 20-27: Historical/completion records (optional)

## Implementation Path
1. Setup: tools/4_init_workspace.py
2. Integrate: tools/1-3 (functional components)
3. Execute: Follow 08_IMPLEMENTATION_GUIDE.md
4. Validate: Follow 09_TESTING_GUIDE.md

## Need Help?
- Architecture questions → 03-05
- Agent details → 07_AGENT_DIRECTORY.md + agents/
- Protocols → 06_PROTOCOLS_COMPLETE.md
- O Award criteria → 10_O_AWARD_CRITERIA.md
```

---

### 2. 07_AGENT_DIRECTORY.md (Agent Index)

**Purpose**: Quick reference to all 18 agents with execution order

**Contents**:
```markdown
# Agent Directory: All 18 Agents

## Execution Order by Phase

### Phase 0: Problem Analysis
- **01_reader.md** - PDF reader (file: agents/01_reader.md)

### Phase 0.2: Knowledge Retrieval
- **18_knowledge_librarian.md** - Method curator (file: agents/18_knowledge_librarian.md)

### Phase 0.5: Method Selection
- **02_researcher.md** - Method retrieval (file: agents/02_researcher.md)
- **04_feasibility_checker.md** - Reality check (file: agents/04_feasibility_checker.md)

[...continues for all phases...]

## By Cluster

### Thinkers (认知与洞察)
1. reader.md
2. researcher.md
3. modeler.md
4. metacognition_agent.md

[...continues...]

## By Role

### Quality Gates
- feasibility_checker.md
- validator.md
- time_validator.md
- judge_zero.md

[...continues...]
```

---

### 3. tools/0_TOOLS_INDEX.md (Tools Guide)

**Purpose**: Implementation priority and integration instructions

**Contents**:
```markdown
# Tools Implementation Guide

## Priority 0: Core Infrastructure (Implement First)
1. **1_system_prompts.py** - Modular prompts (87% token savings)
2. **2_safe_template.py** - Crash-proof formatting

## Priority 1: Enhanced Features
3. **3_journal_prompts.py** - Metacognitive reflection

## Setup Tools (Run Once)
4. **4_init_workspace.py** - Create directory structure
5. **5_migrate_hmml.py** - Convert HMML.md → HMML 2.0

## Phase-Specific Tools
6. **6_style_analyzer.py** - Phase -1 (pre-competition)
7. **7_log_analyzer.py** - Phase 5.8 (insight extraction)
8. **8_mmbench_score.py** - Phase 11 (self-evolution)

## Integration Instructions
[...detailed how-to for each tool...]
```

---

### 4. agents/00_AGENT_INDEX.md (Agent Quick Reference)

**Purpose**: Fast lookup by cluster, role, or phase

---

## Implementation Checklist

### Phase 1: Rename Root Files ✅ (Low Risk)
- [ ] 01_README.md ← README.md
- [ ] 02_VERSION_COMPARISON.md ← 01_version_comparison.md
- [ ] 03_ARCHITECTURE_COMPLETE.md ← ARCHITECTURE_COMPLETE.md
- [ ] 04_ARCHITECTURE_PHASES.md ← ARCHITECTURE_PART2_PHASES.md
- [ ] 05_ARCHITECTURE_NARRATIVE.md ← ARCHITECTURE_PART3_NARRATIVE.md
- [ ] 06_PROTOCOLS_COMPLETE.md ← PROTOCOLS_COMPLETE.md
- [ ] 08_IMPLEMENTATION_GUIDE.md ← implementation_guide.md
- [ ] 09_TESTING_GUIDE.md ← testing_guide.md
- [ ] 10_O_AWARD_CRITERIA.md ← O_AWARD_CRITERIA.md
- [ ] 11_KNOWLEDGE_LIBRARY_SPEC.md ← knowledge_library_specification.md
- [ ] 12_AGENT_KNOWLEDGE_ACCESS.md ← AGENT_KNOWLEDGE_ACCESS.md
- [ ] 13_STRUCTURE_REFERENCE.md ← STRUCTURE.md
- [ ] 20_FINAL_SUMMARY.md ← FINAL_SUMMARY.md
- [ ] 21_AGENT_ENHANCEMENT_SUMMARY.md ← AGENT_ENHANCEMENT_SUMMARY.md
- [ ] 22_INTEGRATION_SUMMARY.md ← INTEGRATION_SUMMARY.md
- [ ] 23_ALL_AGENTS_COMPLETE.md ← ALL_AGENTS_COMPLETE.md
- [ ] 24_COMPLETION_SUMMARY.md ← COMPLETION_SUMMARY.md
- [ ] 25_CONSOLIDATION_PLAN.md ← CONSOLIDATION_PLAN.md
- [ ] 26_CONSOLIDATION_STATUS.md ← CONSOLIDATION_STATUS.md
- [ ] 27_MASTER_INDEX.md ← MASTER_INDEX.md

### Phase 2: Rename Agent Files ✅ (Medium Risk)
- [ ] 01_reader.md ← reader.md
- [ ] 02_researcher.md ← researcher.md
- [ ] 03_modeler.md ← modeler.md
- [ ] 04_feasibility_checker.md ← feasibility_checker.md
- [ ] 05_data_engineer.md ← data_engineer.md
- [ ] 06_code_translator.md ← code_translator_enhancement.md (delete old code_translator.md)
- [ ] 07_model_trainer.md ← model_trainer.md
- [ ] 08_validator.md ← validator.md
- [ ] 09_visualizer.md ← visualizer_enhancement.md
- [ ] 10_writer.md ← writer_enhancement.md
- [ ] 11_editor.md ← editor.md
- [ ] 12_summarizer.md ← summarizer.md
- [ ] 13_advisor.md ← advisor.md
- [ ] 14_time_validator.md ← time_validator.md
- [ ] 15_director.md ← director.md
- [ ] 16_metacognition_agent.md ← metacognition_agent.md
- [ ] 17_narrative_weaver.md ← narrative_weaver.md
- [ ] 18_knowledge_librarian.md ← knowledge_librarian.md
- [ ] 19_judge_zero.md ← judge_zero.md

### Phase 3: Rename Tool Files ✅ (Low Risk)
- [ ] 1_system_prompts.py ← system_prompts.py
- [ ] 2_safe_template.py ← safe_template.py
- [ ] 3_journal_prompts.py ← journal_prompts.py
- [ ] 4_init_workspace.py ← init_workspace.py
- [ ] 5_migrate_hmml.py ← migrate_hmml.py
- [ ] 6_style_analyzer.py ← style_analyzer.py
- [ ] 7_log_analyzer.py ← log_analyzer.py
- [ ] 8_mmbench_score.py ← mmbench_score.py

### Phase 4: Organize Templates ✅ (Low Risk)
- [ ] Rename template files with numeric prefixes (as detailed above)
- [ ] Move ANTI_PATTERNS.md → templates/writing/6_anti_patterns.md

### Phase 5: Create New Index Files ✅ (Low Risk)
- [ ] Create 00_start_here.md
- [ ] Create 07_AGENT_DIRECTORY.md
- [ ] Create tools/0_TOOLS_INDEX.md
- [ ] Create agents/00_AGENT_INDEX.md

### Phase 6: Update Cross-References ⚠️ (High Risk)
- [ ] Update all internal file references in documentation
- [ ] Update import statements in Python files
- [ ] Update README.md navigation links
- [ ] Verify no broken links

---

## Risk Assessment

### Low Risk Changes
- Renaming root .md files (no code dependencies)
- Renaming template files (referenced by agents, not hardcoded)
- Creating new index files (additive, no breaking changes)

### Medium Risk Changes
- Renaming agent files (may be referenced in implementation code)
- Need to verify: Are agent filenames hardcoded anywhere?

### High Risk Changes
- Renaming Python tools (import statements must be updated)
- Moving ANTI_PATTERNS.md (may break references)

---

## Recommended Implementation Order

1. **Create new index files first** (00_start_here.md, etc.) - ADDITIVE, no risk
2. **Rename root .md files** - Update README.md links
3. **Rename template files** - Low impact
4. **Rename agent files** - Verify no hardcoded references first
5. **Rename tool files** - Update imports carefully
6. **Update all cross-references** - Comprehensive search/replace

---

## Alternative: Minimal Disruption Approach

If full reorganization is too risky, **MINIMAL changes**:

1. **Create index files only** (00_start_here.md, 06_agent_directory.md, etc.)
2. **Standardize agent files** (remove _enhancement suffix)
3. **Leave everything else as-is**

This provides 80% of navigation benefit with 20% of risk.

---

**Document Version**: 1.0
**Created**: 2026-01-25
**Status**: AUDIT COMPLETE - Awaiting User Decision on Reorganization
