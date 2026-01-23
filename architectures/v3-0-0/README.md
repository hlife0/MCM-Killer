# MCM-Killer Architecture v3.0.0

> **Version**: v3.0.0 (Major Reorganization Release)
> **Date**: 2026-01-23
> **Type**: Complete Reorganization
> **Status**: Complete ✅

---

## Version Summary

**v3.0.0** is a major reorganization release that:

1. **Clarifies Two-System Architecture**: Clear separation between LLM-MM-Agent (reference/stable) and MCM-Killer (competition system)
2. **Improves Documentation Hierarchy**: Each system has its own complete documentation
3. **Enables Reproduction**: Complete architecture specification for downstream work
4. **Maintains Compatibility**: All v2.6.0 protocols preserved and integrated

---

## Document Structure

```
v3-0-0/
├── README.md                      # This file - Version overview
│
├── 00_ARCHITECTURE.md             # Complete architecture definition
├── 01_SYSTEM_COMPARISON.md        # System comparison (LLM-MM-Agent vs MCM-Killer)
│
├── 02_LLM_MM_AGENT_ARCHITECTURE.md # LLM-MM-Agent detailed architecture
├── 03_MCM_KILLER_ARCHITECTURE.md  # MCM-Killer detailed architecture
│
├── 04_PROTOCOLS_SUMMARY.md        # All 12 protocols summary
├── 05_AGENT_SPECIFICATIONS.md     # Complete agent specifications (14 agents)
├── 06_PHASE_WORKFLOW.md           # Detailed phase workflow (10 phases)
├── 07_VALIDATION_GATES.md         # Validation gate specifications (7 gates)
├── 08_OUTPUT_STRUCTURE.md         # Output directory structure
│
└── draft/                         # Preserved drafts - DO NOT MODIFY
    ├── LLM-MM-Agent/              # LLM-MM-Agent architecture drafts
    └── MCM-Killer/                # MCM-Killer architecture drafts
```

---

## Key Changes from v2.6.0

### New Documents

1. **01_SYSTEM_COMPARISON.md**: Detailed comparison between LLM-MM-Agent and MCM-Killer
2. **02_LLM_MM_AGENT_ARCHITECTURE.md**: Complete LLM-MM-Agent architecture
3. **03_MCM_KILLER_ARCHITECTURE.md**: Complete MCM-Killer architecture
4. **05_AGENT_SPECIFICATIONS.md**: Detailed specifications for all 14 agents
5. **06_PHASE_WORKFLOW.md**: Complete workflow for all 10 phases
7. **07_VALIDATION_GATES.md**: Complete specification of 7 validation gates
8. **08_OUTPUT_STRUCTURE.md**: Output directory structure and file organization

### Reorganized Documents

- **00_ARCHITECTURE.md**: Now serves as complete system overview with two-system architecture
- **04_PROTOCOLS_SUMMARY.md**: Comprehensive summary of all 12 protocols

### Preserved

- **draft/**: All draft documents preserved unchanged

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

**Use Cases**:
- Study reference implementation from academic papers
- Understand 4-stage pipeline architecture
- Retrieve modeling methods via HMML
- Test different LLM models
- Research and experimentation

**Documentation**: See `02_LLM_MM_AGENT_ARCHITECTURE.md`

### System 2: MCM-Killer (Competition)

**Location**: `MCM-Killer/workspace/2025_C/`

**Purpose**: Competition-optimized system for MCM/ICM participation

**Key Features**:
- Multi-agent architecture with 14 specialized agents
- 10-phase workflow with 7 validation gates
- 12 critical protocols for quality control
- Parallel workflow (save 6-12 hours)
- O-Prize competitive ($1.5M target)

**Use Cases**:
- Participate in actual MCM/ICM competitions
- Generate O-Prize competitive papers
- Multi-agent collaboration
- Strict quality control
- Win competitions

**Documentation**: See `03_MCM_KILLER_ARCHITECTURE.md`

---

## 12 Critical Protocols (MCM-Killer)

All 12 protocols from v2.5.7-v2.5.9 are preserved in v3.0.0:

1. **@director File Reading Ban** (v2.5.7) - Prevent evaluation contamination
2. **@time_validator Strict Mode** (v2.5.7) - Reject lazy implementations
3. **Enhanced Time Estimation** (v2.5.7) - Improve prediction accuracy
4. **Phase 5 Parallel Workflow** (v2.5.7) - Save 6-12 hours
5. **@code_translator Idealistic Mode** (v2.5.7) - Enforce perfect implementation
6. **48-Hour Escalation Protocol** (v2.5.7) - Decision framework
7. **@director/@time_validator Handoff** (v2.5.7) - Standardized communication
8. **Model Design Expectations** (v2.5.7) - Systematic validation
9. **@validator/@advisor Brief Format** (v2.5.7) - Fast decision-making
10. **Phase 5B Error Monitoring** (v2.5.7) - Prevent lost errors
11. **Emergency Convergence Delegation** (v2.5.8) - 8× faster response
12. **Phase 4.5 Re-Validation** (v2.5.9) - 8× fraud reduction

**Complete Details**: See `04_PROTOCOLS_SUMMARY.md`

---

## Reading Order

### For New Users

1. **Start here**: `README.md` (this file)
2. **System overview**: `00_ARCHITECTURE.md`
3. **Choose your system**:
   - For research: Read `02_LLM_MM_AGENT_ARCHITECTURE.md`
   - For competition: Read `03_MCM_KILLER_ARCHITECTURE.md`

### For MCM-Killer Users

1. **System comparison**: `01_SYSTEM_COMPARISON.md`
2. **MCM-Killer architecture**: `03_MCM_KILLER_ARCHITECTURE.md`
3. **Protocols**: `04_PROTOCOLS_SUMMARY.md`
4. **Agents**: `05_AGENT_SPECIFICATIONS.md`
5. **Workflow**: `06_PHASE_WORKFLOW.md`
6. **Validation**: `07_VALIDATION_GATES.md`
7. **Output**: `08_OUTPUT_STRUCTURE.md`

### For LLM-MM-Agent Users

1. **System comparison**: `01_SYSTEM_COMPARISON.md`
2. **LLM-MM-Agent architecture**: `02_LLM_MM_AGENT_ARCHITECTURE.md`

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
| **v3.0.0** | **2026-01-23** | **🎯 MAJOR REORGANIZATION** | **Two-system architecture + complete documentation** |

---

## Migration from v2.6.0

### What Changed

1. **Document Reorganization**: Documents reorganized for clarity
2. **New Documents**: 7 new detailed documents added
3. **Two-System Separation**: Clear separation between LLM-MM-Agent and MCM-Killer
4. **Preserved Content**: All v2.6.0 protocols preserved

### What Stayed the Same

1. **12 Protocols**: All protocols unchanged
2. **14 Agents**: All agents unchanged
3. **10 Phases**: All phases unchanged
4. **7 Validation Gates**: All gates unchanged

### How to Migrate

**For MCM-Killer users**:
- All your workflows remain the same
- Refer to new document structure for detailed specifications
- `03_MCM_KILLER_ARCHITECTURE.md` replaces v2-6-0/00_ARCHITECTURE.md for MCM-Killer specific details
- `04_PROTOCOLS_SUMMARY.md` replaces v2-6-0/01_SUMMARY.md
- Protocol documents (02-12) remain valid

**For LLM-MM-Agent users**:
- Refer to `02_LLM_MM_AGENT_ARCHITECTURE.md` for complete details
- `clean version/LLM-MM-Agent/` structure unchanged

---

## Quick Start

### Using LLM-MM-Agent

```bash
cd "clean version/LLM-MM-Agent"
python MMAgent/main.py --key "your_api_key" --task "2024_C" --model_name "gpt-4o"
```

### Using MCM-Killer

```bash
cd "MCM-Killer/workspace/2025_C"
# Run Claude Code CLI and instruct to solve MCM problem
```

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
- **System comparison**: `01_SYSTEM_COMPARISON.md`
- **LLM-MM-Agent details**: `02_LLM_MM_AGENT_ARCHITECTURE.md`
- **MCM-Killer details**: `03_MCM_KILLER_ARCHITECTURE.md`

### Protocol Questions
- **All protocols**: `04_PROTOCOLS_SUMMARY.md`
- **Specific protocols**: See v2-6-0/02-12_*.md

### Implementation Questions
- **Agents**: `05_AGENT_SPECIFICATIONS.md`
- **Workflow**: `06_PHASE_WORKFLOW.md`
- **Validation**: `07_VALIDATION_GATES.md`
- **Output**: `08_OUTPUT_STRUCTURE.md`

---

## Testing and Verification

### Before Using v3.0.0

**Verify Document Structure**:
- [ ] All 9 documents present
- [ ] draft/ folder preserved
- [ ] All documents readable

**Verify Content**:
- [ ] 00_ARCHITECTURE.md provides complete overview
- [ ] 01_SYSTEM_COMPARISON.md compares two systems
- [ ] 02-03 provide detailed architectures
- [ ] 04-08 provide complete specifications

**Verify Compatibility**:
- [ ] All 12 protocols documented
- [ ] All 14 agents specified
- [ ] All 10 phases documented
- [ ] All 7 validation gates specified

---

## Known Issues

None. v3.0.0 is a reorganization release with no functional changes.

---

## Future Versions

**v3.1.0**: Planned enhancements
- [ ] Additional validation protocols
- [ ] Enhanced error handling
- [ ] Improved parallel workflow
- [ ] Additional agent specializations

**v4.0.0**: Next major release (TBD)
- [ ] Potential architectural changes
- [ ] New protocols based on competition experience
- [ ] Enhanced automation

---

## Contributors

- **Architecture Design**: MCM-Killer Development Team
- **Documentation**: v3.0.0 Reorganization Team
- **Protocol Design**: v2.5.7-v2.5.9 Enhancement Teams

---

## License

Proprietary - For internal competition use only.

---

## Contact

For questions about v3.0.0 architecture:
- Review relevant documentation files
- Consult `00_ARCHITECTURE.md` for system overview
- Refer to system-specific architecture documents

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: Read `00_ARCHITECTURE.md` for complete system overview
