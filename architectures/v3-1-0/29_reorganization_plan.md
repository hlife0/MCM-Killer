# File Reorganization Plan: v3-1-0

> **Issue**: Inconsistent file naming (UPPERCASE vs lowercase, no serial numbers)
> **Goal**: Clean, numbered, intuitive structure with clear sequential flow
> **Approach**: Systematic renaming with zero data loss

---

## Current Problems Identified

1. **Mixed case**: UPPERCASE_UNDERSCORES vs lowercase_underscores
2. **No numbering**: Can't tell reading order
3. **Confusing duplicates**: code_translator.md vs code_translator_enhancement.md
4. **Poor navigation**: Which file is core vs reference vs historical?

---

## Proposed Solution: Three-Tier Numbered System

### Tier 0: Entry Point (00-09)
- **00-09**: Core sequential documents
- **Format**: `0X_descriptive_name.md`
- **Purpose**: Read in order for complete understanding

### Tier 1: Reference (10-19)
- **10-19**: Lookup references
- **Format**: `1X_descriptive_name.md`
- **Purpose**: Quick reference, not sequential

### Tier 2: Supporting (20-29)
- **20-29**: Historical/completion records
- **Format**: `2X_descriptive_name.md`
- **Purpose**: Archive, optional reading

---

## Execution Plan

### Phase 1: Root Directory Reorganization ✅

**Execute these renames:**

```bash
# Tier 0: Core Sequential (00-09)
mv README.md                            00_readme.md
mv 01_version_comparison.md             01_version_comparison.md  # Already correct
mv ARCHITECTURE_COMPLETE.md             02_architecture_overview.md
mv ARCHITECTURE_PART2_PHASES.md         03_architecture_phases.md
mv ARCHITECTURE_PART3_NARRATIVE.md      04_architecture_narrative.md
mv PROTOCOLS_COMPLETE.md                05_protocols_complete.md
# 06 reserved for agent directory (to create)
mv implementation_guide.md              07_implementation_guide.md
mv testing_guide.md                     08_testing_guide.md

# Tier 1: Reference (10-19)
mv O_AWARD_CRITERIA.md                  10_o_award_criteria.md
mv knowledge_library_specification.md   11_knowledge_library_spec.md
mv AGENT_KNOWLEDGE_ACCESS.md            12_agent_knowledge_access.md
mv STRUCTURE.md                         13_structure_reference.md

# Tier 2: Supporting/Historical (20-29)
mv FINAL_SUMMARY.md                     20_final_summary.md
mv AGENT_ENHANCEMENT_SUMMARY.md         21_agent_enhancement_summary.md
mv INTEGRATION_SUMMARY.md               22_integration_summary.md
mv ALL_AGENTS_COMPLETE.md               23_all_agents_legacy.md
mv COMPLETION_SUMMARY.md                24_completion_summary.md
mv CONSOLIDATION_PLAN.md                25_consolidation_plan.md
mv CONSOLIDATION_STATUS.md              26_consolidation_status.md
mv MASTER_INDEX.md                      27_master_index_legacy.md
mv ORGANIZATION_AUDIT.md                28_organization_audit.md

# New files
# 00_start_here.md - already exists
# 06_agent_directory.md - need to create from AGENT_DIRECTORY.md
mv AGENT_DIRECTORY.md                   06_agent_directory.md
```

---

### Phase 2: Agents Directory Standardization ✅

**Remove duplicates and add numbers:**

```bash
cd agents/

# Remove old duplicate
rm code_translator.md  # Superseded by code_translator_enhancement.md

# Rename all with execution order numbering (01-19)
mv reader.md                            01_reader.md
mv researcher.md                        02_researcher.md
mv modeler.md                           03_modeler.md
mv feasibility_checker.md               04_feasibility_checker.md
mv data_engineer.md                     05_data_engineer.md
mv code_translator_enhancement.md       06_code_translator.md  # Remove _enhancement
mv model_trainer.md                     07_model_trainer.md
mv validator.md                         08_validator.md
mv visualizer_enhancement.md            09_visualizer.md  # Remove _enhancement
mv writer_enhancement.md                10_writer.md  # Remove _enhancement
mv editor.md                            11_editor.md
mv summarizer.md                        12_summarizer.md
mv advisor.md                           13_advisor.md
mv time_validator.md                    14_time_validator.md
mv director.md                          15_director.md
mv metacognition_agent.md               16_metacognition_agent.md
mv narrative_weaver.md                  17_narrative_weaver.md
mv knowledge_librarian.md               18_knowledge_librarian.md
mv judge_zero.md                        19_judge_zero.md

# Keep status file with clear name
mv IMPLEMENTATION_STATUS.md             00_implementation_status.md
```

---

### Phase 3: Tools Directory Standardization ✅

**Add priority-based numbers:**

```bash
cd tools/

# P0: Core infrastructure (must implement first)
mv system_prompts.py                    1_system_prompts.py
mv safe_template.py                     2_safe_template.py

# P1: Enhanced features
mv journal_prompts.py                   3_journal_prompts.py

# Setup tools
mv init_workspace.py                    4_init_workspace.py
mv migrate_hmml.py                      5_migrate_hmml.py

# Phase-specific tools
mv style_analyzer.py                    6_style_analyzer.py
mv log_analyzer.py                      7_log_analyzer.py
mv mmbench_score.py                     8_mmbench_score.py
```

---

### Phase 4: Templates Standardization ✅

**Add numbers within each subdirectory:**

```bash
# narrative_arcs/
cd templates/narrative_arcs/
mv hero_journey.md                      1_hero_journey.md
mv onion_peeling.md                     2_onion_peeling.md
mv comparative_evolution.md             3_comparative_evolution.md
mv observation_implication.md           4_observation_implication.md

# writing/
cd ../writing/
mv abstract_template.md                 1_abstract_template.md
mv paper_outline_template.md            2_paper_outline_template.md
mv dev_diary_entry.md                   3_dev_diary_entry.md
mv judgment_report_template.md          4_judgment_report_template.md
mv latex_formatting_standards.md        5_latex_formatting_standards.md

# Move ANTI_PATTERNS to writing/
mv ../../ANTI_PATTERNS.md               6_anti_patterns.md

# knowledge_base/
cd ../knowledge_base/
mv method_file_template.md              1_method_file_template.md
mv suggested_methods_template.md        2_suggested_methods_template.md
```

---

## Final Directory Structure

```
v3-1-0/
│
├── 00_start_here.md                    ← ENTRY POINT
├── 00_readme.md                        ← System overview
├── 01_version_comparison.md            ← v3.0.0 vs v3.1.0
├── 02_architecture_overview.md         ← System design Part 1
├── 03_architecture_phases.md           ← All 13 phases
├── 04_architecture_narrative.md        ← Cognitive narrative framework
├── 05_protocols_complete.md            ← All 15 protocols
├── 06_agent_directory.md               ← 18 agents index
├── 07_implementation_guide.md          ← 3-sprint roadmap
├── 08_testing_guide.md                 ← Testing strategy
│
├── 10_o_award_criteria.md              ← 10 characteristics
├── 11_knowledge_library_spec.md        ← HMML 2.0
├── 12_agent_knowledge_access.md        ← Agent→knowledge mapping
├── 13_structure_reference.md           ← Navigation guide
│
├── 20_final_summary.md                 ← Completion summary
├── 21_agent_enhancement_summary.md     ← Enhancement details
├── 22_integration_summary.md           ← Functional components
├── 23_all_agents_legacy.md             ← Legacy consolidated
├── 24_completion_summary.md            ← Historical
├── 25_consolidation_plan.md            ← Historical
├── 26_consolidation_status.md          ← Historical
├── 27_master_index_legacy.md           ← Needs update
├── 28_organization_audit.md            ← This audit
│
├── agents/
│   ├── 00_implementation_status.md
│   ├── 01_reader.md
│   ├── 02_researcher.md
│   ├── 03_modeler.md
│   ├── 04_feasibility_checker.md
│   ├── 05_data_engineer.md
│   ├── 06_code_translator.md
│   ├── 07_model_trainer.md
│   ├── 08_validator.md
│   ├── 09_visualizer.md
│   ├── 10_writer.md
│   ├── 11_editor.md
│   ├── 12_summarizer.md
│   ├── 13_advisor.md
│   ├── 14_time_validator.md
│   ├── 15_director.md
│   ├── 16_metacognition_agent.md
│   ├── 17_narrative_weaver.md
│   ├── 18_knowledge_librarian.md
│   └── 19_judge_zero.md
│
├── tools/
│   ├── 1_system_prompts.py
│   ├── 2_safe_template.py
│   ├── 3_journal_prompts.py
│   ├── 4_init_workspace.py
│   ├── 5_migrate_hmml.py
│   ├── 6_style_analyzer.py
│   ├── 7_log_analyzer.py
│   └── 8_mmbench_score.py
│
└── templates/
    ├── narrative_arcs/
    │   ├── 1_hero_journey.md
    │   ├── 2_onion_peeling.md
    │   ├── 3_comparative_evolution.md
    │   └── 4_observation_implication.md
    ├── writing/
    │   ├── 1_abstract_template.md
    │   ├── 2_paper_outline_template.md
    │   ├── 3_dev_diary_entry.md
    │   ├── 4_judgment_report_template.md
    │   ├── 5_latex_formatting_standards.md
    │   └── 6_anti_patterns.md
    └── knowledge_base/
        ├── 1_method_file_template.md
        └── 2_suggested_methods_template.md
```

---

## Benefits of New Structure

### ✅ Clear Reading Order
- 00-09: Read sequentially
- 10-19: Reference as needed
- 20-29: Archive (optional)

### ✅ Consistent Naming
- All lowercase with underscores
- Numbers indicate priority/order
- Descriptive names

### ✅ Intuitive Navigation
- Numbers tell you what to read first
- Similar numbers = similar importance
- No duplicates or confusion

### ✅ Easy Sorting
- Files naturally sort in reading order
- Tools sort by implementation priority
- Agents sort by execution order

---

## Verification Checklist

After execution:

- [ ] All root files lowercase with numbers
- [ ] All agent files numbered 01-19
- [ ] All tool files numbered 1-8
- [ ] All template files numbered within subdirectories
- [ ] No UPPERCASE files except intentional (README if needed)
- [ ] No duplicates (code_translator_enhancement removed)
- [ ] No orphaned files
- [ ] 00_start_here.md points to correct new filenames

---

**Status**: PLAN COMPLETE - Ready for execution
**Risk Level**: LOW (file renames only, no content changes)
**Estimated Time**: 5-10 minutes
