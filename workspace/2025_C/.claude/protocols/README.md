# MCM-Killer Protocol Documentation

**Total Protocols**: 15 (complete set from v3.1.0 architecture)
**Last Updated**: 2026-01-28
**Status**: ✅ COMPLETE

## Protocol List

### v3.0.0 Protocols (1-12)

| # | Protocol Name | Purpose | Owner | Scope |
|---|---------------|---------|-------|-------|
| 1 | [@director File Reading Ban](protocol_01_director_file_ban.md) | Prevent @director from contaminating agent evaluations | @director | Phases 0.5, 1, 4, 10 |
| 2 | [@time_validator Strict Mode](protocol_02_time_validator_strict_mode.md) | Reject ALL lazy implementations | @time_validator | Phases 4.5, 5.5 |
| 3 | [Enhanced @time_validator Analysis](protocol_03_enhanced_time_analysis.md) | Fix inaccurate time predictions | @time_validator | Phases 1.5, 4.5, 5.5 |
| 4 | [Phase 5 Parallel Workflow](protocol_04_parallel_workflow.md) | Enable paper writing during training | @director | Phase 5 |
| 5 | [@code_translator Idealistic Mode](protocol_05_idealistic_mode.md) | Enforce perfect implementation | @code_translator | Phase 4 |
| 6 | [48-Hour Escalation Protocol](protocol_06_48hour_escalation.md) | Framework for >48h estimates | @time_validator + @director | Phase 1.5 |
| 7 | [@director/@time_validator Handoff](protocol_07_director_timevalidator_handoff.md) | Standardize communication | @director + @time_validator | Phases 1.5, 4.5, 5.5 |
| 8 | [Model Design Expectations Framework](protocol_08_design_expectations.md) | Systematic validation with tolerances | @modeler + @time_validator | Phases 1, 4.5 |
| 9 | [@validator/@advisor Brief Format](protocol_09_brief_format.md) | Fast decision-making | @validator, @advisor | All validation phases |
| 10 | [Phase 5B Error Monitoring](protocol_10_error_monitoring.md) | Watch mode for training errors | @model_trainer | Phase 5B |
| 11 | [Emergency Convergence Delegation](protocol_11_emergency_delegation.md) | 8× faster critical error response | @model_trainer + @modeler + @code_translator | Phase 5B |
| 12 | [Phase 4.5 Re-Validation](protocol_12_revalidation.md) | Prevent fraud during code fixes | @director + @time_validator | Phase 4.5 |

### v3.1.0 New Protocols (13-15)

| # | Protocol Name | Purpose | Owner | Scope |
|---|---------------|---------|-------|-------|
| 13 | [Mock Court Rewind (DEFCON 1)](protocol_13_defcon1.md) | Emergency recovery from judge rejection | @director | Phase 9.1 |
| 14 | [Academic Style Alignment](protocol_14_academic_style.md) | Enforce O-Prize writing standards | @writer, @editor | Phases 7-9 |
| 15 | [Observation-Implication Patterns](protocol_15_observation_implication.md) | Transform descriptive to insightful | All text agents | All paper content |

## Protocol Categories

### Quality & Fidelity (Protocols 1-3, 7-9, 12)
- Prevent evaluation contamination
- Reject lazy implementations
- Validate design-to-code fidelity
- Ensure consistent communication
- Close validation gaps

### Time & Workflow (Protocols 4, 6, 10)
- Parallel workflow for efficiency
- 48-hour escalation framework
- Error monitoring during training
- Save 9-18 hours per competition

### Agent Behavior (Protocol 5)
- Idealistic mode for @code_translator
- Perfect implementation requirement

### Emergency Response (Protocol 11)
- 8× faster convergence error response
- Direct delegation bypass
- Retroactive approval

### Paper Quality (Protocols 13-15)
- DEFCON 1 recovery mechanism
- Academic style enforcement
- Observation-Implication structure

## Impact Summary

| Protocol | Quality Impact | Time Impact | Risk Reduction |
|----------|----------------|-------------|----------------|
| 1. File Ban | 100% accurate evaluations | - | Prevents evaluation errors |
| 2. Strict Mode | Eliminates lazy implementations | - | Academic fraud prevented |
| 3. Enhanced Analysis | ±50% time accuracy | - | Better planning |
| 4. Parallel Workflow | - | **Save 6-12 hours** | - |
| 5. Idealistic Mode | Perfect implementation | - | No simplification |
| 6. 48h Escalation | Clear decisions | Better time management | - |
| 7. Handoff | Consistent decisions | - | - |
| 8. Design Expectations | Systematic validation | - | Fidelity assured |
| 9. Brief Format | Faster decisions | Save 1-2 hours | - |
| 10. Error Monitoring | Real-time fixes | Save 2-4 hours | Errors not lost |
| 11. Emergency | - | **8× faster (30-60 min)** | - |
| 12. Re-Validation | - | - | **8× fraud reduction** |
| 13. DEFCON 1 | **Only perfect papers survive** | - | **Prevents submission failure** |
| 14. Style Alignment | **O-Prize-level writing** | - | **Consistent quality** |
| 15. Interpretation | **Insightful vs descriptive** | - | **Physical understanding** |

**Total Impact**:
- **Time Savings**: 9-18 hours per competition
- **Quality Improvement**: 100% accurate evaluations, O-Prize-level papers
- **Risk Reduction**: 8× reduction in academic fraud, prevents submission failure

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
Phase 11 (Self-Evolution)
```

## Usage Guidelines

### For @director
- **Read protocols before delegating** to agents
- **Enforce protocols consistently** - zero tolerance for violations
- **Reference protocols when making decisions**
- **Log protocol violations** in VERSION_MANIFEST.json

### For All Agents
- **Read applicable protocols** before starting tasks
- **Follow protocol requirements** strictly
- **Report protocol violations** to @director
- **Suggest protocol improvements** in Phase 11

## Version History

- **v3.1.0** (2026-01-28): Complete protocol set (1-15) implemented
- **v3.0.0** (2026-01-25): Original 12 protocols defined
- **v3.1.0 new**: Protocols 13-15 added for DEFCON 1, style, and interpretation

## Reference Documentation

All protocol content derived from:
- `architectures/v3-1-0/05_protocols_complete.md` (complete reference)
- `architectures/v3-0-0/04_protocols_summary.md` (summary reference)

---

**END OF PROTOCOL DOCUMENTATION**
