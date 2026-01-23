# MCM-Killer Architecture v3.0.0

> **Version**: v3.0.0
> **Date**: 2026-01-24
> **Purpose**: Complete detailed architecture for reproduction
> **Status**: Complete ✅

---

## Version Summary

**v3.0.0** is a complete detailed architecture release that:

1. **Clarifies Two-System Architecture**: Clear separation between LLM-MM-Agent (reference/stable) and MCM-Killer (competition system)
2. **Provides Complete Documentation**: All protocols, agents, workflows, and configurations documented
3. **Enables Complete Reproduction**: Sufficient detail to reproduce the entire project
4. **Maintains Compatibility**: All v2.6.0 protocols preserved and integrated

---

## Document Structure

```
v3-0-0/
├── README.md                               # This file - Version overview and index
│
├── 00_architecture.md                      # Complete system overview
├── 01_system_comparison.md                 # LLM-MM-Agent vs MCM-Killer comparison
│
├── 02_llm_mm_agent_architecture.md         # LLM-MM-Agent detailed architecture
├── 03_mcm_killer_architecture.md          # MCM-Killer detailed architecture
│
├── 04_protocols_summary.md                 # All 12 protocols summary
├── 05_agent_specifications.md              # Agent specifications (overview)
├── 06_phase_workflow.md                    # Phase workflow (overview)
├── 07_validation_gates.md                  # Validation gates (overview)
├── 08_output_structure.md                  # Output directory structure
├── 09_workspace_configuration.md           # Workspace execution guide (detailed)
│
├── 10_director_file_reading_ban.md         # Protocol 1: Director file ban (detailed)
├── 11_time_validator_strict_mode.md        # Protocol 2: Strict mode (detailed)
├── 12_phase_5_parallel_workflow.md         # Protocol 4: Parallel workflow (detailed)
├── 13_time_validator_enhanced_analysis.md   # Protocol 3: Enhanced analysis (detailed)
├── 14_code_translator_idealistic_mode.md   # Protocol 5: Idealistic mode (detailed)
├── 15_director_time_validator_handoff.md    # Protocol 7: Handoff protocol (detailed)
├── 16_model_design_expectations.md         # Protocol 8: Design expectations (detailed)
├── 17_validator_advisor_brief_format.md     # Protocol 9: Brief format (detailed)
├── 18_phase5b_error_monitoring.md          # Protocol 10: Error monitoring (detailed)
├── 19_emergency_delegation.md              # Protocol 11: Emergency delegation (detailed)
├── 20_phase45_revalidation.md              # Protocol 12: Re-validation (detailed)
│
├── 21_agent_detailed_configurations.md     # Reference to actual agent files
│
└── draft/                                   # Preserved drafts - DO NOT MODIFY
    ├── LLM-MM-Agent/                        # LLM-MM-Agent architecture drafts
    └── MCM-Killer/                          # MCM-Killer architecture drafts
```

---

## Key Features

### Complete Documentation (22 Documents)

**Core Architecture (00-03)**:
- System overview and two-system architecture
- Detailed comparison between LLM-MM-Agent and MCM-Killer
- Complete architecture for both systems

**Overview Documents (04-08)**:
- Protocols, agents, workflow, validation gates, output structure

**Execution Guide (09)**:
- Complete workspace execution guide with all commands and procedures

**Detailed Protocols (10-20)**:
- All 12 protocols with complete implementation details

**Agent Reference (21)**:
- Reference to actual agent configuration files in workspace

---

## Two-System Architecture

### System 1: LLM-MM-Agent (Reference/Stable)

**Location**: `clean version/LLM-MM-Agent/`

**Purpose**: Research prototype published at NeurIPS 2025 and ICML 2025

**Key Features**:
- Single-agent architecture with actor-critic refinement
- 4-stage pipeline: Problem Analysis → Mathematical Modeling → Computational Solving → Solution Reporting
- HMML (Hierarchical Mathematical Modeling Library) with 98+ schemas
- DAG-based task scheduling
- Command-line interface

**Documentation**: `02_llm_mm_agent_architecture.md`

### System 2: MCM-Killer (Competition)

**Location**: `MCM-Killer/workspace/2025_C/`

**Purpose**: Competition-optimized system for MCM/ICM participation

**Key Features**:
- Multi-agent architecture with 14 specialized agents
- 10-phase workflow with 7 validation gates
- 12 critical protocols for quality control
- Parallel workflow (save 6-12 hours)
- O-Prize competitive ($1.5M target)

**Documentation**: `03_mcm_killer_architecture.md`

---

## 12 Critical Protocols (MCM-Killer)

All 12 protocols from v2.5.7-v2.5.9 with complete details:

1. **@director File Reading Ban** (v2.5.7) - Prevent evaluation contamination
   - Details: `10_director_file_reading_ban.md`
2. **@time_validator Strict Mode** (v2.5.7) - Reject lazy implementations
   - Details: `11_time_validator_strict_mode.md`
3. **Enhanced Time Estimation** (v2.5.7) - Improve prediction accuracy
   - Details: `13_time_validator_enhanced_analysis.md`
4. **Phase 5 Parallel Workflow** (v2.5.7) - Save 6-12 hours
   - Details: `12_phase_5_parallel_workflow.md`
5. **@code_translator Idealistic Mode** (v2.5.7) - Enforce perfect implementation
   - Details: `14_code_translator_idealistic_mode.md`
6. **48-Hour Escalation Protocol** (v2.5.7) - Decision framework
   - Details: `15_director_time_validator_handoff.md`
7. **@director/@time_validator Handoff** (v2.5.7) - Standardized communication
   - Details: `15_director_time_validator_handoff.md`
8. **Model Design Expectations** (v2.5.7) - Systematic validation
   - Details: `16_model_design_expectations.md`
9. **@validator/@advisor Brief Format** (v2.5.7) - Fast decision-making
   - Details: `17_validator_advisor_brief_format.md`
10. **Phase 5B Error Monitoring** (v2.5.7) - Prevent lost errors
    - Details: `18_phase5b_error_monitoring.md`
11. **Emergency Convergence Delegation** (v2.5.8) - 8× faster response
    - Details: `19_emergency_delegation.md`
12. **Phase 4.5 Re-Validation** (v2.5.9) - 8× fraud reduction
    - Details: `20_phase45_revalidation.md`

**Summary**: `04_protocols_summary.md`

---

## Reading Guide

### For Complete Understanding (Recommended Order)

**Start here**: `README.md` (this file)

**Step 1: Understand Architecture**
1. `00_architecture.md` - Complete system overview
2. `01_system_comparison.md` - Compare two systems
3. `02_llm_mm_agent_architecture.md` - LLM-MM-Agent details
4. `03_mcm_killer_architecture.md` - MCM-Killer details

**Step 2: Understand Components**
5. `04_protocols_summary.md` - All 12 protocols
6. `05_agent_specifications.md` - 14 agents overview
7. `06_phase_workflow.md` - 10-phase workflow
8. `07_validation_gates.md` - 7 validation gates
9. `08_output_structure.md` - Output structure

**Step 3: Learn Execution**
10. `09_workspace_configuration.md` - Complete execution guide

**Step 4: Study Protocols (Detailed)**
11. `10-20_*.md` - All 12 protocols with complete details

**Step 5: Reference**
12. `21_agent_detailed_configurations.md` - Agent file references

### Quick Reference

**For Architecture Overview**: `00_architecture.md`

**For Protocol Details**: `04_protocols_summary.md` then `10-20_*.md`

**For Execution**: `09_workspace_configuration.md`

**For Agents**: `05_agent_specifications.md` and `21_agent_detailed_configurations.md`

---

## Document Descriptions

### Core Documents (00-03)

**00_architecture.md** (20KB)
- Complete system overview
- Two-system architecture
- Version history
- Critical problems and solutions
- Agent overview
- Phase overview
- 12 protocols summary

**01_system_comparison.md** (21KB)
- Detailed comparison table
- Architecture comparison
- Agent composition comparison
- Knowledge base comparison
- Validation strategy comparison
- Time efficiency comparison
- Quality control comparison
- When to use which system
- Decision flowchart

**02_llm_mm_agent_architecture.md** (15KB)
- 4-stage pipeline details
- HMML structure and retrieval
- DAG-based scheduling
- Actor-critic pattern
- Context pruning strategy
- Output structure
- Unique innovations
- Configuration details
- Usage guide

**03_mcm_killer_architecture.md** (16KB)
- 14 specialized agents
- 10-phase workflow
- 7 validation gates
- 12 critical protocols
- Output structure
- Unique innovations
- Usage guide

### Overview Documents (04-08)

**04_protocols_summary.md** (28KB)
- All 12 protocols summary
- Problem statement and solution
- Implementation details
- Impact summary
- Complete protocol list

**05_agent_specifications.md** (28KB)
- Complete agent overview table
- Detailed responsibilities for each agent
- Validation participation
- Key protocols per agent
- Phase participation
- Agent communication protocols

**06_phase_workflow.md** (28KB)
- Complete phase overview table
- Entry/exit conditions
- Tasks for each phase
- Output specifications
- Validation criteria
- Time estimates
- Key protocols
- Phase completion checklist

**07_validation_gates.md** (22KB)
- 14 validation gates specifications
- Evaluation criteria
- Decision criteria
- Output formats
- Key protocols
- Failure handling
- Gate relationships

**08_output_structure.md** (16KB)
- Complete output directory structure
- VERSION_MANIFEST.json specification
- Data authority hierarchy
- File creation order
- File size guidelines
- Backup strategy

### Execution Guide (09)

**09_workspace_configuration.md** (102KB)
- **Complete execution manual** with 17,000+ lines
- System overview and director role
- File structure and team composition
- Critical rules and protocols
- 18-phase workflow with full details
- Phase jump mechanism
- Workspace initialization
- Director master checklist
- Validation gates with protocols
- Phase-specific procedures
- Python environment setup
- File write integrity rules
- Inter-agent communication
- Task management
- Parallel work patterns
- Emergency protocols
- All bash commands and verification scripts
- Decision trees and checklists

### Detailed Protocols (10-20)

**10_director_file_reading_ban.md** (13KB)
- Complete protocol specification
- Implementation details
- Examples and scenarios
- Affected agents
- Phase scope

**11_time_validator_strict_mode.md** (19KB)
- STRICT MODE rules
- Decision matrix
- Training duration red line
- Algorithm match verification
- Feature completeness check
- Consequences of violations

**12_phase_5_parallel_workflow.md** (12KB)
- Key changes
- Two-pass workflow
- Time expectations (updated)
- Impact analysis

**13_time_validator_enhanced_analysis.md** (19KB)
- Enhanced check procedures
- File reading requirements
- Line-by-line analysis
- Empirical time estimation table

**14_code_translator_idealistic_mode.md** (19KB)
- Identity statement
- Core philosophy
- Behavioral rules
- Error handling protocol

**15_director_time_validator_handoff.md** (19KB)
- Handoff protocol
- @director's call template
- @time_validator's response template
- @director's decision logic

**16_model_design_expectations.md** (17KB)
- Mandatory design expectations table
- Systematic comparison table
- Scoring system
- @director enforcement

**17_validator_advisor_brief_format.md** (17KB)
- Brief format template
- Detailed report template
- @director decision logic

**18_phase5b_error_monitoring.md** (15KB)
- Watch mode implementation
- Error resolution workflow
- Status reporting

**19_emergency_delegation.md** (9KB)
- When to use (all criteria)
- Emergency flow
- Safeguards
- Response time

**20_phase45_revalidation.md** (25KB)
- Re-validation trigger
- @director's analysis protocol
- Conditional re-validation
- Hidden modification detection

### Agent Reference (21)

**21_agent_detailed_configurations.md** (13KB)
- Reference to actual agent files
- Agent configuration file locations
- Tool configurations
- Key excerpts from each agent

---

## Version History

| Version | Date | Type | Key Changes |
|---------|------|------|-------------|
| v2.3.0 | 2025-12-28 | Initial | First architecture documentation |
| v2.4.0 | 2026-01-10 | Enhancement | Modular architecture + agent directory |
| v2.5.0 | 2026-01-13 | Fix | Agent directory structure fix |
| v2.5.5 | 2026-01-17 | Enhancement | 6 enhancements + @time_validator |
| v2.5.6 | 2026-01-18 | Bugfix | 4 fixes: Feedback, Phase 5.5, Phase 0.5, Images |
| v2.5.7 | 2026-01-19 | Enhancement | 10 protocols: File ban, Strict mode, Parallel, etc. |
| v2.5.8 | 2026-01-19 | Enhancement | Protocol 11: Emergency delegation |
| v2.5.9 | 2026-01-20 | Fix | Protocol 12: Phase 4.5 re-validation |
| v2.6.0 | 2026-01-23 | Integration | Complete integration of all 12 protocols |
| **v3.0.0** | **2026-01-24** | **🎯 COMPLETE DETAILED** | **All details for complete reproduction** |

---

## Migration from v2.6.0

### What Changed

1. **Document Reorganization**: Documents reorganized for clarity
2. **New Documents**: 13 new detailed documents added
3. **Two-System Separation**: Clear separation between LLM-MM-Agent and MCM-Killer
4. **Complete Details**: All execution details, protocols, and configurations documented

### What Stayed the Same

1. **12 Protocols**: All protocols unchanged with complete details
2. **14 Agents**: All agents unchanged
3. **10 Phases**: All phases unchanged
4. **7 Validation Gates**: All gates unchanged

### How to Migrate

**For MCM-Killer users**:
- All your workflows remain the same
- Refer to new document structure for detailed specifications
- `03_mcm_killer_architecture.md` for MCM-Killer details
- `09_workspace_configuration.md` for execution guide
- `10-20_*.md` for protocol details

**For LLM-MM-Agent users**:
- `02_llm_mm_agent_architecture.md` for complete details
- `clean version/LLM-MM-Agent/` structure unchanged

---

## Quick Start

### Using LLM-MM-Agent

```bash
cd "clean version/LLM-MM-Agent"
python MMAgent/main.py --key "your_api_key" --task "2024_C" --model_name "gpt-4o"
```

### Using MCM-Killer

**Step 1**: Read execution guide
```bash
cd "MCM-Killer/workspace/2025_C"
```

**Step 2**: Review architecture
- Read `03_mcm_killer_architecture.md`
- Read `09_workspace_configuration.md`

**Step 3**: Run Claude Code CLI and follow the 18-phase workflow

---

## Document Statistics

| Category | Documents | Total Size |
|----------|-----------|------------|
| Core Architecture | 4 (00-03) | ~72KB |
| Overview | 6 (04-09) | ~140KB |
| Detailed Protocols | 11 (10-20) | ~180KB |
| Reference | 1 (21) | ~13KB |
| README | 1 | ~11KB |
| **Total** | **23** | **~416KB** |

---

## System Requirements

### LLM-MM-Agent
- Python 3.10+
- Dependencies in `clean version/LLM-MM-Agent/requirements.txt`
- API key for supported LLM (OpenAI, DeepSeek, Zhipu AI, or Qwen)

### MCM-Killer
- Claude Code CLI
- Python 3.10+
- Virtual environment support
- Dependencies per model requirements

---

## Support and Documentation

### Architecture Questions
- **System overview**: `00_architecture.md`
- **System comparison**: `01_system_comparison.md`
- **LLM-MM-Agent**: `02_llm_mm_agent_architecture.md`
- **MCM-Killer**: `03_mcm_killer_architecture.md`

### Protocol Questions
- **Summary**: `04_protocols_summary.md`
- **Details**: `10-20_*.md` (all 12 protocols with complete details)

### Execution Questions
- **Agents**: `05_agent_specifications.md` and `21_agent_detailed_configurations.md`
- **Workflow**: `06_phase_workflow.md`
- **Validation**: `07_validation_gates.md`
- **Output**: `08_output_structure.md`
- **Execution**: `09_workspace_configuration.md`

---

## Reproduction Capability

**v3.0.0 enables complete reproduction of the MCM-Killer system**:

✅ **All protocols documented** with complete implementation details
✅ **All agents specified** with responsibilities and configurations
✅ **All phases defined** with entry/exit conditions and tasks
✅ **All validation gates specified** with criteria and decision logic
✅ **Execution guide included** with all commands and procedures
✅ **Agent configuration files** referenced for detailed setups
✅ **Workspace configuration** documented with bash scripts and verification

**To reproduce**:
1. Read `09_workspace_configuration.md` for complete execution guide
2. Read protocol details in `10-20_*.md`
3. Reference agent files in `workspace/2025_C/.claude/agents/`
4. Follow the 18-phase workflow step by step

---

## Contributors

- **Architecture Design**: MCM-Killer Development Team
- **Documentation**: v3.0.0 Complete Documentation Team
- **Protocol Design**: v2.5.7-v2.5.9 Enhancement Teams

---

## License

Proprietary - For internal competition use only.

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-24
**Status**: Complete ✅

**Next**: Read `00_architecture.md` for complete system overview
