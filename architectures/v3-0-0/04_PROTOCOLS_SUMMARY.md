# 12 Critical Protocols Summary (MCM-Killer)

> **Version**: v3.0.0
> **Date**: 2026-01-23
> **Purpose**: Complete summary of all 12 critical protocols inherited from v2.5.7-v2.5.9

---

## Protocol Overview

| # | Protocol Name | Version | Purpose | Impact |
|---|---------------|---------|---------|--------|
| 1 | @director File Reading Ban | v2.5.7 | Prevent evaluation contamination | Agent evaluations accurate |
| 2 | @time_validator Strict Mode | v2.5.7 | Reject lazy implementations | Academic fraud prevented |
| 3 | Enhanced Time Estimation | v2.5.7 | Improve time prediction accuracy | ±50% accuracy target |
| 4 | Phase 5 Parallel Workflow | v2.5.7 | Enable parallel paper writing | Save 6-12 hours |
| 5 | @code_translator Idealistic Mode | v2.5.7 | Enforce perfect implementation | No unauthorized simplification |
| 6 | 48-Hour Escalation Protocol | v2.5.7 | Decision framework for long training | Clear escalation criteria |
| 7 | @director/@time_validator Handoff | v2.5.7 | Standardized communication | Consistent decision-making |
| 8 | Model Design Expectations | v2.5.7 | Systematic validation framework | Tolerance-based scoring |
| 9 | @validator/@advisor Brief Format | v2.5.7 | Fast decision-making | Reduced @director load |
| 10 | Phase 5B Error Monitoring | v2.5.7 | Prevent lost errors | Real-time error resolution |
| 11 | Emergency Convergence Delegation | v2.5.8 | Fast critical error response | 8× faster (30-60 min) |
| 12 | Phase 4.5 Re-Validation | v2.5.9 | Close rework validation gap | 8× fraud reduction |

---

## Protocol 1: @director File Reading Ban

**Purpose**: Prevent @director from contaminating agent evaluations by reading files first.

**Problem Solved**:
```
@director reads research_notes.md → forms understanding → calls @advisor
@advisor evaluates from @director's context (NOT the actual file)
Result: Contaminated evaluation, wrong file read
```

**Solution**:

**Rule 1**: @director CANNOT read files that agents will evaluate
```
❌ FORBIDDEN:
@director reads research_notes.md → forms understanding → calls @advisor

✅ CORRECT:
@director calls @advisor: "Read output/docs/research_notes.md and evaluate"
```

**Rule 2**: @director MUST specify exact file paths
```
❌ VAGUE: "@advisor: Evaluate the methodology quality"
✅ EXPLICIT: "@advisor: Read output/docs/research_notes.md and evaluate methodology"
```

**Rule 3**: Agents MUST report which file they read
```
@advisor's report MUST include:
- "I read: output/docs/research_notes.md"
- "File size: 843 lines"
- "Last modified: [timestamp]"
```

**Rule 4**: @director MUST verify correct file was read
```
@director's checklist:
- [ ] Agent specified which file they read
- [ ] File path matches expected location
- [ ] File size/timestamp is current
- [ ] Evaluation content matches file content
```

**Affected Agents**:
- **@director** (PROHIBITED from reading evaluation targets)
- **@advisor** (MUST read specified file, report file path)
- **@validator** (MUST read specified file, report file path)
- **ALL validation agents** (MUST report which file they evaluated)

**Scope**: Phases 0.5, 1, 4, 10 (any phase where @director delegates evaluation)

**Implementation Reference**: `v2-6-0/02_director_file_reading_ban.md`

---

## Protocol 2: @time_validator Strict Mode

**Purpose**: Ensure @time_validator rejects ALL lazy implementations, especially training duration shortcuts.

**Problem Solved**:
```
Expected training: 12-18 hours
Actual training: 43 minutes
@time_validator: "Looks good"
Result: Academic fraud through simplification
```

**Solution**:

**Rule 1**: Training Duration Red Line
```
Expected: 12-18 hours
Minimum acceptable: 3.6 hours (30% of minimum expected)

❌ REJECT if actual < 3.6 hours:
- 43 minutes = 0.72 hours → 23× below threshold → AUTO-REJECT
- 2 hours = 120 minutes → Below threshold → REJECT
```

**Rule 2**: Algorithm Match Verification
```
Design specifies: PyMC with HMC sampling
Code uses: sklearn.LinearRegression
Verdict: ❌ LAZY IMPLEMENTATION → REJECT
```

**Rule 3**: Feature Completeness Check
```
Design: 15 features including X, Y, Z
Code: "Use available columns" (only 10 columns)
Verdict: ❌ INCOMPLETE → REJECT
```

**Rule 4**: Iteration/Parameter Verification
```
Design: 10,000 MCMC samples
Code: pm.sample(1000)
Verdict: ❌ REDUCED BY 10× → LAZY → REJECT
```

**Decision Matrix**:

| Check | Pass Threshold | Fail Action |
|-------|---------------|-------------|
| Training duration | ≥ 30% of expected | Auto-reject |
| Algorithm match | Exact match | Reject |
| Features | All present | Reject |
| Iterations | ≥ 80% of specified | Reject |

**Consequences of Lazy Implementation**:
1. **First offense**: @code_translator must rework completely
2. **Second offense**: @director issues formal warning
3. **Third offense**: Consider agent replacement (reinitialize agent)

**Affected Agents**:
- **@time_validator** (MUST enforce strict mode)
- **@code_translator** (MUST not simplify)
- **@director** (MUST coordinate fixes, not accept shortcuts)
- **@modeler** (MUST fix design issues, not accept "simpler version")

**Scope**: Phases 4.5 (Implementation Fidelity), 5.5 (Data Authenticity)

**Implementation Reference**: `v2-6-0/03_time_validator_strict_mode.md`

---

## Protocol 3: Enhanced @time_validator Analysis

**Purpose**: Fix inaccurate time predictions through comprehensive file reading and line-by-line code analysis.

**Problem Solved**:
```
@time_validator prediction: 16 hours
Actual training time: 43 minutes
Error: 22× underestimate
```

**Solution**:

**Enhancement 1**: @time_validator MUST read 3 file types
```
1. Model design: output/model/model_design_{i}.md
2. Dataset: output/implementation/data/features_{i}.pkl (check shape/size)
3. Implementation: output/implementation/code/model_{i}.py (line-by-line)
```

**Enhancement 2**: @time_validator MUST analyze line-by-line
```
Check:
- Import statements (which library?)
- Model definition (what algorithm?)
- Sampling parameters (how many iterations?)
- Loops (nested = O(n²) or O(n³)?)
```

**Enhancement 3**: @time_validator MUST use empirical table
```
| Algorithm | Dataset | Samples | Expected Time |
|-----------|---------|---------|---------------|
| PyMC hierarchical | 5000×50 | 10000×4 | 12-15 hours |
| sklearn.LinearRegression | ANY | ANY | <0.1 hours |
| Random Forest | 5000×50 | 100 trees | 0.5-1 hours |
| Neural Network | 5000×50 | 1000 epochs | 2-4 hours |
```

**Accuracy Target**: ±50% of actual time

**Affected Agents**:
- **@time_validator** (MUST read 3 files, analyze line-by-line)
- **@director** (MUST provide file paths explicitly)

**Scope**: Phases 1.5 (Time Estimate), 4.5 (Fidelity Check), 5.5 (Anti-Fraud)

**Implementation Reference**: `v2-6-0/05_time_validator_enhanced_analysis.md`

---

## Protocol 4: Phase 5 Parallel Workflow

**Purpose**: Enable paper writing to proceed while full training runs in background, saving 6-12 hours.

**Problem Solved**:
```
Phase 5A (30 min) → Phase 5B (6-12 hours) → Phase 6 → Phase 7
@writer idle for 6-12 hours waiting for Phase 5B
```

**Solution**:

**Key Change 1**: Phase 5A → Paper writing proceeds immediately
```
Phase 5A (30 min): Quick training with results_quick_*.csv
    ↓
Phase 6 (30 min): Generate figures from quick results
    ↓
Phase 7 (2-3 hours): Write paper with quick results
    ↓
Phase 5B (6-12 hours): Runs in parallel
```

**Key Change 2**: When Phase 5B completes
```
- @visualizer regenerates figures with final results
- @writer updates Results section with final results
```

**Per-Model Time Expectations**:
- **Minimum**: 6 hours
- **Typical**: 8-12 hours
- **Maximum**: 48 hours (with @director approval)

**Impact**: Save 6-12 hours per competition through parallelization

**Affected Phases**:
- **Phase 5A** (proceed to paper immediately)
- **Phase 5B** (runs in background)
- **Phase 6** (quick version first, final version later)
- **Phase 7** (draft with quick results, update with final)

**Implementation Reference**: `v2-6-0/04_phase_5_parallel_workflow.md`

---

## Protocol 5: @code_translator Idealistic Mode

**Purpose**: Enforce perfect implementation by making @code_translator an idealist who never compromises on design.

**Problem Solved**:
```
@code_translator: "KeyError: 'Gold' → I'll use available columns"
@code_translator: "PyMC doesn't work → I'll use sklearn"
Result: Academic fraud through simplification
```

**Solution**:

**Identity Statement**:
```
@code_translator: "I am an idealist, a perfectionist"
```

**Core Philosophy**:
- Token cost is irrelevant
- Training time is irrelevant
- **ONLY thing that matters**: Implement design perfectly

**Behavioral Rules**:
```
❌ NEVER simplify without @director approval
❌ NEVER "use available columns" when features missing
❌ NEVER switch libraries (PyMC → sklearn)
❌ NEVER reduce iterations to save time
✅ ALWAYS report errors to @director
✅ ALWAYS wait for guidance before proceeding
✅ ALWAYS document issues and propose solutions
```

**Error Handling Protocol**:
```
When @code_translator encounters error:
1. DO NOT: "I'll use a simpler version"
2. DO: "I encountered error X: [description]"
3. DO: "The design requires [feature] but [issue]"
4. DO: "@director, please advise on how to proceed"
```

**Affected Agents**:
- **@code_translator** (MUST be idealistic, MUST report errors)
- **@director** (MUST coordinate fixes, NOT approve shortcuts)

**Scope**: Phase 4 (Code Translation), all code modifications

**Implementation Reference**: `v2-6-0/06_code_translator_idealistic_mode.md`

---

## Protocol 6: 48-Hour Escalation Protocol

**Purpose**: Provide clear decision framework when training estimates exceed 48 hours.

**Problem Solved**:
```
@time_validator: "Training estimate: 78 hours (>48 hours threshold)"
@director: "Should I approve? Should I ask @modeler to simplify? What are the criteria?"
```

**Solution**:

**Decision Framework**:
```python
if total_estimate > 48 hours:
    if competition_remaining >= total_estimate * 1.2:
        return "PROCEED"  # Sufficient buffer (20%)
    elif competition_remaining >= total_estimate:
        return "PROCEED_WITH_CAUTION"  # Tight but feasible
    else:
        return "CONSULT_MODELER"  # Need simplification/prioritization
```

**CRITICAL Rule**:
```
❌ FORBIDDEN: "@code_translator, simplify the models"
✅ CORRECT: "@modeler, we have a time constraint. How should we prioritize?"
```

**Priority Order**:
1. Fix implementation problems (time-efficient solutions)
2. Reduce model complexity (last resort, requires @modeler approval)
3. Prioritize models (focus on most important ones)

**Affected Agents**:
- **@time_validator** (MUST escalate when >48 hours)
- **@director** (MUST use decision framework)
- **@modeler** (MUST be consulted for any design changes)

**Scope**: Phase 1.5 (Time Estimate Validation)

**Implementation Reference**: `v2-6-0/07_director_time_validator_handoff.md`

---

## Protocol 7: @director/@time_validator Handoff

**Purpose**: Standardize communication between @director and @time_validator for consistent decision-making.

**Problem Solved**:
```
@director calls @time_validator: "Check if this is OK"
@time_validator: "Looks good"
@director: "But what did you check? What are the criteria?"
```

**Solution**:

**Step 1**: @director's call to @time_validator (explicit)
```
"@time_validator: Validate time estimates for Phase 5B.

Read:
- output/model/model_design_*.md
- output/implementation/data/features_*.pkl
- output/implementation/code/model_*.py

Provide:
1. Per-model time estimate
2. Total time estimate
3. Algorithm fidelity check
4. Feature completeness check
5. Recommendation: APPROVE/REJECT/ESCALATE"
```

**Step 2**: @time_validator's response (standardized)
```
Files Read Verification:
- Read: model_design_1.md (324 lines)
- Read: features_1.pkl (shape: (5000, 50))
- Read: model_1.py (215 lines)

Per-Model Breakdown:
- Model 1: PyMC hierarchical, 5000×50, 10000×4 chains
  - Estimated: 12-15 hours
  - Algorithm: ✅ Exact match (PyMC)
  - Features: ✅ All 15 present
  - Verdict: ✅ VALID

Total Estimate: 48 hours (range: 36-72 hours)

Fidelity Checks:
- Algorithm match: ✅ All models use designed algorithms
- Feature completeness: ✅ All features present
- Iteration/Parameter: ✅ Within tolerance

Recommendation: ✅ APPROVE (total < 48h threshold)
```

**Step 3**: @director's decision (systematic)
```
@director's checklist:
- [ ] @time_validator read all 3 file types
- [ ] Line-by-line analysis performed
- [ ] Empirical time estimation used
- [ ] Fidelity checks passed
- [ ] Competition time remaining: XX hours
- [ ] Decision: PROCEED (based on recommendation + time check)
```

**Affected Agents**:
- **@director** (MUST call with explicit instructions)
- **@time_validator** (MUST read all files, MUST provide clear recommendation)

**Scope**: Phases 1.5, 4.5, 5.5

**Implementation Reference**: `v2-6-0/07_director_time_validator_handoff.md`

---

## Protocol 8: Model Design Expectations Framework

**Purpose**: Systematic validation of model designs against implementation with tolerance specifications.

**Problem Solved**:
```
Model design says: "NUTS sampler with 10000 draws"
Implementation: "Slice sampler with 1000 draws"

Current state:
- No explicit design expectations documented
- No tolerance specifications
- No scoring tables for validation
```

**Solution**:

**Step 1**: Mandatory Design Expectations Table (by @modeler)
```markdown
## Design Expectations Table

| Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
|-----------|---------------------|-----|-----|------|-------------------|
| Sampler | NUTS | NUTS | NUTS | - | YES |
| Chains | 4 | 4 | 4 | chains | YES |
| Draws | 20000 | 20000 | 20000 | samples | YES |
| Tune | 2000 | 2000 | 2000 | iterations | YES |
| Features | 15 | 15 | 15 | features | YES |
| Algorithm | PyMC | PyMC | PyMC | - | YES |
```

**Step 2**: Systematic Comparison Table (by @time_validator)
```markdown
## Implementation Fidelity Check

| Parameter | Design | Actual | Diff | Tolerance | Verdict |
|-----------|--------|--------|------|-----------|---------|
| Sampler | NUTS | NUTS | 0% | Exact | ✅ PASS |
| Chains | 4 | 4 | 0% | ±0 | ✅ PASS |
| Draws | 20000 | 20000 | 0% | ±0 | ✅ PASS |
| Features | 15 | 15 | 0% | ±0 | ✅ PASS |
```

**Step 3**: Scoring System
```
CRITICAL parameters: Auto-reject if fail
  - Sampler, Algorithm, Core features

HIGH parameters: ±20% tolerance
  - Draws, Tune, Iterations

Overall score: Must be ≥80%

Rule: One fail = all fail
```

**Step 4**: @director Enforcement
```python
if ANY critical_param FAIL:
    return "REJECT"  # No exceptions
elif overall_score < 0.8:
    return "REJECT"
else:
    return "APPROVE"
```

**Affected Agents**:
- **@modeler** (MUST create design expectations table)
- **@time_validator** (MUST create comparison table, calculate score)
- **@director** (MUST enforce "one fail = all fail" rule)

**Scope**: Phase 1 (Model Design), Phase 4.5 (Implementation Fidelity)

**Implementation Reference**: `v2-6-0/08_model_design_expectations.md`

---

## Protocol 9: @validator/@advisor Brief Format

**Purpose**: Enable fast decision-making by requiring concise evaluations in chat, detailed reports to files.

**Problem Solved**:
```
@validator: "I've reviewed the methodology document in detail.
           The document contains sophisticated Bayesian hierarchical models... (10+ sentences)"

@director: [Spends 5 minutes analyzing verbose reports]
```

**Solution**:

**Brief Format** (First 4 lines only in chat):
```
Grade: 9.0/10 | Verdict: ✅ PASS
Justification: Mathematically sound with proper specification.
File verified: output/model/model_design_1.md (324 lines)
Detailed report written to: output/docs/validation/validator_model_1.md
```

**Detailed Reports** (Written to file, NOT shown in chat):
```markdown
# Validation Report: Model Design 1

## File Information
- Path: output/model/model_design_1.md
- Lines: 324
- Last Modified: 2026-01-23 14:32:15

## Grade: 9.0/10

## Verdict: ✅ PASS

## Brief Evaluation
Mathematically sound with proper specification.

## Detailed Analysis
[Full analysis here for @researcher reference if revision needed]
```

**@director Decision Logic** (Simplified):
```
IF @validator PASS AND @advisor PASS:
    RETURN "APPROVE"
ELSE:
    RETURN "REJECT"
```

**Standardized Report Template**:
1. File Information (path, lines, timestamp)
2. Grade + Verdict
3. Brief Evaluation (1 sentence)
4. Detailed Analysis (for @researcher reference)

**Impact**: Faster decision-making, less @director cognitive load

**Affected Agents**:
- **@validator** (MUST use brief format in chat, detailed report to file)
- **@advisor** (MUST use brief format in chat, detailed report to file)
- **@director** (MUST read only brief format, apply pass/fail rule)
- **@researcher** (CAN read detailed reports when revision needed)

**Scope**: Phases 0.5, 1, 4, 5.5, 10 (all validation phases)

**Implementation Reference**: `v2-6-0/09_validator_advisor_brief_format.md`

---

## Protocol 10: Phase 5B Error Monitoring

**Purpose**: Prevent errors from being lost by keeping AI session active during training with watch mode.

**Problem Solved**:
```
Model 2 Failed: 'TensorVariable' object has no attribute 'logp'
Error occurs at 3 AM → AI session has exited → Error discovered hours later
```

**Solution**:

**Rule 1**: AI Session Does NOT Exit
```
Training runs in background
@model_trainer enters "watch mode"
Session stays active, monitoring for errors
```

**Rule 2**: Watch Mode Implementation
```python
while True:
    check_process_status()
    check_log_file_for_errors()

    if error_detected:
        report_to_director()
        await_guidance()

    if training_complete:
        report_completion()
        break

    sleep(60)  # Check every 60 seconds
```

**Rule 3**: Error Resolution Workflow
```
1. @model_trainer detects error → Reports to @director
2. @director delegates fix:
   - Implementation error → @code_translator
   - Data error → @data_engineer
   - Design issue → @modeler
3. Fix applied → Resume training (no restart from scratch)
```

**Rule 4**: Status Reporting
```
Regular updates: Every 30 minutes
Immediate notification: Error detected
Completion report: Summary of training results
```

**Affected Agents**:
- **@model_trainer** (MUST enter watch mode, MUST NOT exit session)
- **@director** (MUST coordinate error resolution)
- **@code_translator** (MUST fix implementation errors)
- **@data_engineer** (MUST fix data errors)

**Scope**: Phase 5B (Full Training)

**Implementation Reference**: `v2-6-0/10_phase5b_error_monitoring.md`

---

## Protocol 11: Emergency Convergence Delegation ⭐ v2.5.8

**Purpose**: Enable fast response (30-60 min) for critical convergence failures while maintaining @director coordination.

**Problem Solved**:
```
Critical convergence error occurs at 3 AM during competition:
R-hat: 1.42 (threshold: 1.3)
Standard protocol response time: 4-5 hours
Problem: Competition deadline is approaching fast
```

**Solution**:

**When to Use** (ALL criteria must be met):
```
1. Error Category: Convergence (Category 4)
2. Severity: CRITICAL
   - R-hat > 1.3 (severe non-convergence)
   - OR no convergence after 12 hours of training
   - OR >10% divergent transitions
   - OR complete sampling failure
3. @modeler is available and responsive
4. Fix is well-understood (parameter adjustment, NOT algorithm change)
```

**Emergency Flow** (bypasses @director):
```
@model_trainer → @modeler (direct escalation)
@modeler → @code_translator (direct delegation)
@code_translator → implements fix (copies @director)
@director → retroactive approval (within 1 hour)
@model_trainer → resumes training
```

**Safeguards**:
- **Single-use limit**: Once per model only
- **Time limit**: Fix must be implemented within 30 minutes
- **Severity threshold**: R-hat > 1.3 (not just >1.1)
- **Documentation**: All emergency fixes logged in VERSION_MANIFEST.json
- **Oversight**: @director retroactive approval required within 1 hour

**Response Time**:
- Standard protocol: 4-5 hours
- Emergency protocol: 30-60 minutes (**8× faster**)

**Affected Agents**:
- **@model_trainer** (MUST recognize emergency conditions)
- **@modeler** (MUST be available during training phase)
- **@code_translator** (MUST implement emergency fixes within 10 min)
- **@director** (MUST provide retroactive oversight)

**Scope**: Phase 5B (Full Training) - critical convergence errors only

**Implementation Reference**: `v2-6-0/11_emergency_delegation.md`

---

## Protocol 12: Phase 4.5 Re-Validation ⭐ v2.5.9

**Purpose**: Close rework validation gap to prevent academic fraud through unauthorized simplification during training fixes.

**Problem Solved**:
```
@code_translator fixes bug during training:
Original code: "tune: 2000" (from design)
Fixed code: "tune: 4000" (parameter changed)

Problem: Fixed code is NOT re-validated against Design Expectations Table
Risk: 40% chance of unauthorized simplification or algorithm change
```

**Solution**:

**Step 1**: @code_translator MUST provide CHANGES SUMMARY
```markdown
## CHANGES SUMMARY
- File: model_{i}.py
- Original issue: {description}
- Fix applied: {description}
- Parameters changed: {list}
- Algorithm changed: YES/NO
- Features changed: YES/NO
```

**Step 2**: @director analyzes CHANGES SUMMARY
```
IF parameter changes detected → Trigger re-validation
IF algorithm changed → Full Phase 1 rewind required
IF simple bug fix (syntax, import) → Resume training
```

**Step 3**: Conditional Re-Validation (triggered by parameter changes)
```
@director calls @time_validator: "RE-VALIDATION REQUIRED"

@time_validator runs Phase 4.5 on reworked code:
- Read CHANGES SUMMARY
- Compare to Design Expectations Table
- Check for unauthorized simplifications
- Verify parameters within tolerance

IF ✅ APPROVE → Resume training
IF ❌ REJECT → Full rework required
```

**Step 4**: Hidden Modification Detection
```
- Compare reworked code against Design Expectations Table
- Check for unauthorized simplifications
- Verify all parameters within tolerance
- Detect algorithm changes
```

**Impact**: 8× reduction in academic fraud risk (40% → <5%)

**Affected Agents**:
- **@code_translator** (MUST provide changes summary)
- **@director** (MUST analyze changes, trigger re-validation)
- **@time_validator** (MUST re-validate when requested)

**Scope**: Phase 4.5 (Implementation Fidelity) - triggered after code fixes

**Implementation Reference**: `v2-6-0/12_phase45_revalidation.md`

---

## Protocol Interdependencies

```
Protocol 1 (File Ban)
    ↓
Protocol 2 (Strict Mode)
    ↓
Protocol 3 (Enhanced Analysis)
    ↓
Protocol 7 (Handoff)
    ↓
Protocol 8 (Design Expectations) ←→ Protocol 5 (Idealistic Mode)
    ↓
Protocol 9 (Brief Format)
    ↓
Protocol 4 (Parallel Workflow)
    ↓
Protocol 10 (Error Monitoring)
    ↓
Protocol 11 (Emergency Delegation)
    ↓
Protocol 12 (Re-Validation)
```

**Key Relationships**:
- Protocol 1 enables accurate evaluation for all other protocols
- Protocol 2 depends on Protocol 3 for accurate analysis
- Protocol 5 feeds into Protocol 8 for validation
- Protocol 10 enables Protocol 11 (error detection → emergency delegation)
- Protocol 12 closes loop from Protocol 10 (error fix → re-validation)

---

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

**Total Impact**:
- **Time Savings**: 9-18 hours per competition
- **Quality Improvement**: 100% accurate evaluations, perfect implementations
- **Risk Reduction**: 8× reduction in academic fraud risk

---

## Testing Checklist

Before deployment, verify all 12 protocols:

**Protocol 1**:
- [ ] @director file reading ban documented
- [ ] @director protocol specifies exact file paths
- [ ] Agents (@advisor, @validator) required to report file read

**Protocol 2**:
- [ ] @time_validator strict mode rules documented
- [ ] Training duration red line (30% threshold) specified
- [ ] Algorithm match verification specified

**Protocol 3**:
- [ ] 3 file types requirement specified
- [ ] Line-by-line analysis requirement specified
- [ ] Empirical table provided

**Protocol 4**:
- [ ] Phase 5 parallel workflow documented
- [ ] Time expectations updated (>6h, typical 8-12h)
- [ ] Two-pass workflow specified

**Protocol 5**:
- [ ] @code_translator idealistic mode specified
- [ ] "Simplification = fraud" warnings added
- [ ] Error reporting protocol specified

**Protocol 6**:
- [ ] 48-hour escalation framework documented
- [ ] Decision matrix provided
- [ ] "@director NEVER simplifies" rule specified

**Protocol 7**:
- [ ] @director/@time_validator handoff protocol specified
- [ ] @director's call template provided
- [ ] @time_validator's response template provided

**Protocol 8**:
- [ ] Design expectations table template documented
- [ ] Comparison table format specified
- [ ] Scoring system documented

**Protocol 9**:
- [ ] Brief format template specified
- [ ] Detailed report template specified
- [ ] @director decision logic simplified

**Protocol 10**:
- [ ] Watch mode protocol documented
- [ ] Error resolution workflow documented
- [ ] Status reporting intervals specified

**Protocol 11** ⭐:
- [ ] Emergency criteria documented (R-hat > 1.3, 12h elapsed)
- [ ] Emergency flow documented (@model_trainer → @modeler → @code_translator)
- [ ] Safeguards specified (single-use, severity threshold, time limit)
- [ ] @modeler training phase responsibilities documented

**Protocol 12** ⭐:
- [ ] CHANGES SUMMARY template documented
- [ ] Re-validation trigger logic documented
- [ ] @time_validator re-validation mode specified
- [ ] Comparison table format for re-validation defined

---

**Document Version**: v3.0.0
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**Next**: See `05_AGENT_SPECIFICATIONS.md` for complete agent specifications
