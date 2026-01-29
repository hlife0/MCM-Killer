# Protocols Knowledge Base

**Version**: v3.2.0
**Total Protocols**: 18
**Last Updated**: 2026-01-29

---

## Overview

This knowledge base contains all protocols for the MCM-Killer multi-agent competition system. Protocols are organized by category and include detailed implementation guidelines, examples, and agent responsibilities.

---

## Protocol Categories

### 1. Quality & Fidelity (Protocols 1-3, 7-9, 12)
- **Protocol 1**: @director File Reading Ban
- **Protocol 2**: @time_validator Strict Mode
- **Protocol 3**: Enhanced @time_validator Analysis
- **Protocol 7**: @director/@time_validator Handoff
- **Protocol 8**: Model Design Expectations Framework
- **Protocol 9**: @validator/@advisor Brief Format
- **Protocol 12**: Phase 4.5 Re-Validation

### 2. Time & Workflow (Protocols 4, 6, 10)
- **Protocol 4**: Phase 5 Parallel Workflow
- **Protocol 6**: 48-Hour Escalation Protocol
- **Protocol 10**: Phase 5B Error Monitoring

### 3. Agent Behavior (Protocol 5)
- **Protocol 5**: @code_translator Idealistic Mode

### 4. Emergency Response (Protocol 11)
- **Protocol 11**: Emergency Convergence Delegation

### 5. Paper Quality (Protocols 13-15)
- **Protocol 13**: Mock Court Rewind (DEFCON 1)
- **Protocol 14**: Academic Style Alignment
- **Protocol 15**: Observation-Implication Patterns

### 6. Execution Quality (Protocols 16-18) 🆕
- **Protocol 16**: Page Count Tracking
- **Protocol 17**: Model Component Testing
- **Protocol 18**: Automated Value Injection

---

## Quick Reference

### Protocol 16: Page Count Tracking
**Purpose**: Prevent page count overrun violations
**Owner**: @director (enforcement), @writer (compliance)
**Scope**: Phase 7A-7F
**Key Feature**: 5 checkpoint system with alert thresholds
**Examples**: `agent_knowledge/writer/protocols/protocol_16_page_tracking_examples.md`

### Protocol 17: Model Component Testing
**Purpose**: Catch bugs before 14-hour training runs
**Owner**: @code_translator (create tests), @model_trainer (run tests)
**Scope**: Phase 4-5
**Key Feature**: Unit tests, dimension verification, reduced dataset validation
**Template**: `agent_knowledge/code_translator/protocols/protocol_17_unit_test_template.py`

### Protocol 18: Automated Value Injection
**Purpose**: Ensure 100% data consistency OR automatic rejection
**Owner**: @data_engineer (create scripts), @writer (use scripts), @validator (enforce rejection)
**Scope**: Phase 7
**Key Feature**: Automatic rejection for data inconsistencies
**Examples**: `agent_knowledge/data_engineer/protocols/protocol_18_script_examples.md`

---

## Protocol Locations

### Main Protocol Files
**Location**: `.claude/protocols/`

- `protocol_01_director_file_ban.md`
- `protocol_02_time_validator_strict_mode.md`
- `protocol_03_enhanced_time_analysis.md`
- `protocol_04_parallel_workflow.md`
- `protocol_05_idealistic_mode.md`
- `protocol_06_48hour_escalation.md`
- `protocol_07_director_timevalidator_handoff.md`
- `protocol_08_design_expectations.md`
- `protocol_09_brief_format.md`
- `protocol_10_error_monitoring.md`
- `protocol_11_emergency_delegation.md`
- `protocol_12_revalidation.md`
- `protocol_13_defcon1.md`
- `protocol_14_academic_style.md`
- `protocol_15_observation_implication.md`
- `protocol_16_page_count_tracking.md` 🆕
- `protocol_17_model_component_testing.md` 🆕
- `protocol_18_automated_value_injection.md` 🆕

---

## Agent-Specific Protocol Knowledge

### @writer
**Location**: `agent_knowledge/writer/protocols/`

- `protocol_16_page_tracking_examples.md` - Page count reporting examples, consolidation scenarios
- `csv_to_latex_table.py` - Script reference (created by @data_engineer)

**Key Responsibilities**:
- Report page count after each Phase 7 sub-phase
- Stay within allocated budget OR trigger emergency consolidation
- Use csv_to_latex_table.py for ALL numerical tables
- Never manually transcribe values from CSV to LaTeX

---

### @code_translator
**Location**: `agent_knowledge/code_translator/protocols/`

- `protocol_17_unit_test_template.py` - Unit test template for all model files

**Key Responsibilities**:
- Include unit tests in every model_{i}.py file
- Include dimension verification function
- Include synthetic data generation function
- Test before delivery to @model_trainer

---

### @data_engineer
**Location**: `agent_knowledge/data_engineer/protocols/`

- `protocol_18_script_examples.md` - Complete script examples and usage
- `csv_to_latex_table.py` - Automated LaTeX table generation script
- `validate_consistency.py` - Automated consistency validation script

**Key Responsibilities**:
- Create csv_to_latex_table.py before Phase 7A
- Create validate_consistency.py before Phase 7A
- Test scripts on sample CSV files
- Document usage in script docstrings

---

### @validator
**Location**: `agent_knowledge/validator/protocols/`

- `validate_consistency.py` - Script reference (created by @data_engineer)

**Key Responsibilities**:
- Run validate_consistency.py before Phase 7.5
- Check exit code (0 = APPROVE, 1 = REJECT)
- Enforce rejection (NO OVERRIDE allowed)
- Re-verify after table regeneration

---

### @director
**Location**: `CLAUDE.md` (Automatic Decision Rules)

**Key Responsibilities**:

**Protocol 16**:
- Verify page count after each Phase 7 sub-phase
- Enforce alert thresholds (Yellow, Red, Critical)
- Block Phase 7F if page count ≥25.0

**Protocol 17**:
- Verify all model files have test blocks before Phase 5
- Confirm all tests passed before approving Phase 5B
- Block Phase 5B launch if pre-training checklist incomplete

**Protocol 18**:
- Verify scripts exist before Phase 7A
- Enforce rejection if @validator detects inconsistency
- NO OVERRIDE allowed for @validator's rejection

---

## Python Scripts Reference

### Script 1: csv_to_latex_table.py
**Purpose**: Generate LaTeX table code from CSV files
**Location**: `output/implementation/code/csv_to_latex_table.py`
**Usage**: `python csv_to_latex_table.py <csv_path> <table_id> [output_dir]`
**Owner**: @data_engineer (create), @writer (use)

**Key Features**:
- Reads CSV file (results_{i}.csv)
- Rounds all values to 2 decimal places (ENSURES CONSISTENCY)
- Generates LaTeX table code
- Writes to `output/paper/tables/table_{i}.tex`

---

### Script 2: validate_consistency.py
**Purpose**: Verify CSV values match LaTeX values exactly
**Location**: `output/implementation/code/validate_consistency.py`
**Usage**: `python validate_consistency.py <csv_path> <latex_path>`
**Owner**: @data_engineer (create), @validator (use)

**Key Features**:
- Reads CSV and LaTeX files
- Extracts numerical values from both
- Compares values (tolerance: 0.0 for EXACT match)
- Exit code 0: All values consistent → APPROVE submission
- Exit code 1: Mismatch detected → REJECT submission

---

## Protocol Interdependencies

```
Protocol 1 (File Ban)
    |
Protocol 2 (Strict Mode)
    |
Protocol 3 (Enhanced Analysis)
    |
Protocol 7 (Handoff)
    |
Protocol 8 (Design Expectations) <-> Protocol 5 (Idealistic Mode)
    |
Protocol 9 (Brief Format)
    |
Protocol 4 (Parallel Workflow)
    |
Protocol 10 (Error Monitoring)
    |
Protocol 11 (Emergency Delegation)
    |
Protocol 12 (Re-Validation)
    |
Phase 5.8 (Insight Extraction) -> Protocol 15 (Interpretation)
    |
Protocol 14 (Style Alignment) + Protocol 15 (Interpretation)
    |
Phase 9.1 (Mock Judging)
    |
Protocol 13 (DEFCON 1) <-> [Loop back to fix issues]
    |
Protocol 16 (Page Count Tracking) -> Phase 7 Checkpoints
    |
Protocol 17 (Model Component Testing) -> Phase 4-5 Validation
    |
Protocol 18 (Automated Value Injection) -> Phase 7 Data Consistency
    |
Phase 11 (Self-Evolution)
```

---

## Protocol Enforcement Summary

### Automatic Rejection (Protocol 18)
- **Trigger**: @validator detects paper.tex values ≠ CSV values
- **Action**: Mark submission as REJECTED
- **Override**: NOT ALLOWED (must fix inconsistency first)
- **Resolution**: @writer regenerates all tables from CSV
- **Loop**: Until exit code = 0 (100% consistent)

---

### Page Count Enforcement (Protocol 16)
- **Yellow Warning**: ≥20.0 pages → Tighten remaining sections
- **Red Critical**: ≥23.0 pages → Stop writing, consolidate
- **Submission Limit**: ≥25.0 pages → Block submission, mandatory consolidation

---

### Model Testing Enforcement (Protocol 17)
- **Pre-Phase 5B**: All 4 validation steps must pass
- **Failed Test**: Do not launch Phase 5B
- **Resolution**: Fix bug, re-run tests, re-verify

---

## Impact Summary

| Protocol | Time Savings | Risk Reduction | Quality Improvement |
|----------|--------------|----------------|---------------------|
| 16. Page Count | 4-6 hours | Zero page violations | Systematic tracking |
| 17. Model Testing | 14-30 hours per bug | Zero failed training | Perfect implementation |
| 18. Value Injection | 2-4 hours | Zero inconsistencies | 100% consistency |

**Total Impact**: 15-28 hours time savings, eliminates 3 highest-risk issues

---

## Related Documentation

- **Protocols README**: `.claude/protocols/README.md` - Complete protocol list and descriptions
- **Phase Details**: `knowledge_base/phase_details.md` - Detailed phase procedures
- **Agent Details**: `.claude/agents/README.md` - Agent responsibilities and capabilities
- **Operations Index**: `knowledge_base/operations.md` - Operational procedures

---

## Version History

- **v3.2.0** (2026-01-29): Protocols 16-18 added for execution quality
- **v3.1.0** (2026-01-28): Protocols 13-15 added for DEFCON 1, style, and interpretation
- **v3.0.0** (2026-01-25): Original 12 protocols defined

---

**END OF PROTOCOLS KNOWLEDGE BASE**
