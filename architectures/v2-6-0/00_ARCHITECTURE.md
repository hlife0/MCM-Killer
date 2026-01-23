# MCM-Killer v2.6.0 System Architecture

> **Authoritative Architecture Definition** — All Agent prompts should be derived from this document.
> **Version**: v2.6.0
> **Date**: 2026-01-23
> **Architecture Overview**: Complete integration of v2.5.7-v2.5.9 enhancements into unified system architecture with 12 critical protocols

---

## Document Relationships

| Document | Purpose |
|----------|---------|
| **`00_ARCHITECTURE.md`** (this document) | **Defines architecture and Agent contracts** |
| **`01_SUMMARY.md`** | **Complete summary of all system protocols** |
| **`02_director_file_reading_ban.md`** | **@director file reading prohibition protocol** |
| **`03_time_validator_strict_mode.md`** | **Enhanced @time_validator anti-lazy enforcement** |
| **`04_phase_5_parallel_workflow.md`** | **Phase 5 parallel workflow (5A→paper, 5B background)** |
| **`05_time_validator_enhanced_analysis.md`** | **@time_validator line-by-line code analysis** |
| **`06_code_translator_idealistic_mode.md`** | **@code_translator idealistic/perfectionist mode** |
| **`07_director_time_validator_handoff.md`** | **@director/@time_validator handoff protocol** |
| **`08_model_design_expectations.md`** | **Model design expectations validation protocol** |
| **`09_validator_advisor_brief_format.md`** | **@validator/@advisor concise evaluation format** |
| **`10_phase5b_error_monitoring.md`** | **Phase 5B error monitoring and resolution** |
| **`11_emergency_delegation.md`** | **Emergency delegation for critical convergence failures** |
| **`12_phase45_revalidation.md`** | **Phase 4.5 re-validation for code fixes during training** |

Reading order: **01_SUMMARY.md** → **02-12 (detailed specs)** → **00_ARCHITECTURE.md**

> **CRITICAL SYSTEM PROTOCOLS**: 12 critical protocols ensuring robust execution: (1) @director file reading ban, (2) @time_validator strict mode, (3) Phase 5 parallel workflow, (4) Enhanced time estimation with line-by-line analysis, (5) @code_translator idealistic mode, (6) 48-hour escalation protocol, (7) Director/time_validator handoff logic, (8) Model design expectations validation with scoring tables, (9) @validator/@advisor brief format for efficient decision-making, (10) Phase 5B error monitoring with no-exit guarantee, (11) Emergency convergence protocol for critical failures, (12) Phase 4.5 re-validation protocol for code fixes during training.

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| v2.5.5 | 2026-01-17 | 6 enhancements + @time_validator agent |
| v2.5.6 | 2026-01-18 | 4 fixes: Feedback files, Phase 5.5, Phase 0.5, Image naming |
| v2.5.7 | 2026-01-19 | 10 enhancements: Director file ban, Time validator strict mode, Phase 5 parallel, Enhanced analysis, Idealistic mode, 48h escalation, Handoff protocol, Model design expectations, Brief evaluation format, Phase 5B error monitoring |
| v2.5.8 | 2026-01-19 | 1 enhancement: Emergency delegation protocol for critical convergence failures |
| v2.5.9 | 2026-01-20 | 1 critical fix: Phase 4.5 re-validation protocol for code fixes during training |
| **v2.6.0** | **2026-01-23** | **Integration release: Consolidates all v2.5.7-v2.5.9 protocols into unified architecture** |

---

## Inherited Protocols from v2.5.7-v2.5.9

### Protocol 1: @director File Reading Ban *(v2.5.7)*

**Purpose**: Prevent @director from contaminating agent evaluations by reading files first.

**Key Rules**:
1. **@director CANNOT read files that agents will evaluate**
   - Forbidden: @director reads research_notes.md before calling @advisor
   - Required: @director calls @advisor with explicit file path

2. **@director MUST specify exact file paths for agents to read**
   - Bad: "@advisor: Evaluate the methodology" (no file specified)
   - Good: "@advisor: Read output/docs/research_notes.md and evaluate methodology"

3. **@director MUST verify agents read the correct file**
   - After calling @advisor, ask: "What file did you read?"
   - Check that @advisor's report references the correct file

4. **Agents MUST explicitly state which file they read**
   - @advisor's report MUST include: "I read: output/docs/research_notes.md (843 lines)"
   - If wrong file → Re-call with explicit instruction

**Affected Agents**:
- **@director** (PROHIBITED from reading evaluation targets)
- **@advisor** (MUST read specified file, report file path)
- **@validator** (MUST read specified file, report file path)
- **ALL validation agents** (MUST report which file they evaluated)

**Implementation**:
- See `02_director_file_reading_ban.md` for full specification
- Update @director (CLAUDE.md) with ban rules
- Update @advisor, @validator with file reporting requirements

---

### Protocol 2: @time_validator Strict Mode *(v2.5.7)*

**Purpose**: Ensure @time_validator rejects ALL lazy implementations, especially training duration shortcuts.

**Key Rules**:

1. **@code_translator: Simplification = Academic Fraud**
   - Forbidden: "PyMC didn't work, so I used sklearn instead"
   - Forbidden: "Data structure mismatch, so I used available columns"
   - Required: "encountered error X, I consulted @director for guidance"
   - Required: "I documented the issue and proposed solutions to @director"

2. **@time_validator: Training Duration Red Line**
   - **Red Line**: If actual training time < 30% of expected → **AUTO-REJECT**
   - Expected: 12-18 hours → Actual must be ≥ 3.6 hours
   - 43 minutes is **23× below minimum acceptable threshold**

3. **@time_validator: Algorithm Match Verification**
   - Check: Does code use designed algorithm? (PyMC vs sklearn)
   - Check: Are all features included? (no "use available columns")
   - Check: Are iterations as specified? (10000 samples, not 1000)
   - **Mismatch → LAZY IMPLEMENTATION → REJECT**

4. **@director: Consult Before Simplify Protocol**
   - When @code_translator reports "can't implement X":
     - DO NOT say "just simplify it"
     - DO say: "@modeler, we need to fix this data structure issue"
     - DO say: "@code_translator, wait while we resolve this"
   - **Priority**: Fix implementation problems → Accept lazy shortcuts

**Affected Agents**:
- **@code_translator** (MUST consult before simplifying)
- **@time_validator** (MUST enforce training duration red line)
- **@director** (MUST coordinate fixes, not accept shortcuts)
- **@modeler** (MUST fix design issues, not accept "simpler version")

**Implementation**:
- See `03_time_validator_strict_mode.md` for full specification
- Update @time_validator with strict mode rules
- Update @code_translator with "simplification = fraud" warnings

---

### Protocol 3: Enhanced @time_validator Analysis *(v2.5.7)*

**Purpose**: Improve time estimation accuracy by reading multiple file types and analyzing code line-by-line.

**Key Enhancements**:
1. **@time_validator MUST read 3 file types**:
   - Model design: `output/model/model_design_{i}.md`
   - Dataset: `output/implementation/data/features_{i}.pkl` (check shape/size)
   - Implementation: `output/implementation/code/model_{i}.py` (line-by-line analysis)

2. **@time_validator MUST analyze line-by-line**:
   - Import statements (which library?)
   - Model definition (what algorithm?)
   - Sampling parameters (how many iterations?)
   - Loops (nested = O(n²) or O(n³)?)

3. **@time_validator MUST use empirical table** (not guesses):
   | Algorithm | Dataset | Samples | Expected Time |
   |-----------|---------|---------|---------------|
   | PyMC hierarchical | 5000×50 | 10000×4 | **12-15 hours** |
   | sklearn.LinearRegression | ANY | ANY | **<0.1 hours** |

**Affected Agents**:
- **@time_validator** (MUST read dataset + code, MUST analyze line-by-line)
- **@director** (MUST provide file paths explicitly)

**Implementation**:
- See `05_time_validator_enhanced_analysis.md` for full specification

---

### Protocol 4: Phase 5 Parallel Workflow *(v2.5.7)*

**Purpose**: Enable paper writing to proceed while full training runs in background, saving 6-12 hours.

**Key Changes**:
1. **Phase 5A → Paper writing proceeds immediately**:
   - Phase 5A (30 min): Quick training with `results_quick_*.csv`
   - Phase 6 (30 min): Generate figures from quick results
   - Phase 7 (2-3 hours): Write paper with quick results
   - Phase 5B (6-12 hours): Runs in parallel

2. **When Phase 5B completes**:
   - @visualizer regenerates figures with final results
   - @writer updates Results section with final results

**Per-Model Time Expectations**:
- Minimum: 6 hours
- Typical: 8-12 hours
- Maximum: 48 hours (with @director approval)

**Affected Phases**:
- **Phase 5A** (proceed to paper immediately)
- **Phase 5B** (runs in background)
- **Phase 6** (quick version first, final version later)
- **Phase 7** (draft with quick results, update with final)

**Implementation**:
- See `04_phase_5_parallel_workflow.md` for full specification

---

### Protocol 5: @code_translator Idealistic Mode *(v2.5.7)*

**Purpose**: Enforce perfect implementation by making @code_translator an idealist who never compromises on design.

**Key Changes**:
1. **@code_translator identity**: "I am an idealist, a perfectionist"
2. **Core philosophy**:
   - Token cost is irrelevant
   - Training time is irrelevant
   - **ONLY thing that matters**: Implement design perfectly

3. **Behavioral rules**:
   - ❌ NEVER simplify without @director approval
   - ❌ NEVER "use available columns" when features missing
   - ❌ NEVER switch libraries (PyMC → sklearn)
   - ✅ ALWAYS report errors to @director
   - ✅ ALWAYS wait for guidance before proceeding

**Affected Agents**:
- **@code_translator** (MUST be idealistic, MUST report errors)
- **@director** (MUST coordinate fixes, NOT approve shortcuts)

**Implementation**:
- See `06_code_translator_idealistic_mode.md` for full specification

---

### Protocol 6: 48-Hour Escalation Protocol *(v2.5.7)*

**Purpose**: Provide clear decision framework when training estimates exceed 48 hours.

**Key Framework**:
```python
if total_estimate > 48 hours:
    if competition_remaining >= total_estimate * 1.2:
        return "PROCEED"  # Sufficient buffer
    elif competition_remaining >= total_estimate:
        return "PROCEED_WITH_CAUTION"  # Tight but feasible
    else:
        return "CONSULT_MODELER"  # Need simplification/prioritization
```

**CRITICAL**: **@director NEVER simplifies unilaterally**
- **WRONG**: "@code_translator, simplify the models"
- **RIGHT**: "@modeler, we have a time constraint. How should we prioritize?"

**Affected Agents**:
- **@time_validator** (MUST escalate when >48 hours)
- **@director** (MUST use decision framework)
- **@modeler** (MUST be consulted for any design changes)

**Implementation**:
- See `07_director_time_validator_handoff.md` for full specification

---

### Protocol 7: @director/@time_validator Handoff *(v2.5.7)*

**Purpose**: Standardize communication between @director and @time_validator for consistent decision-making.

**Key Protocol**:
1. **@director's call to @time_validator** (explicit):
   - Specify files to read (model_design, features, code)
   - Request per-model time estimate and total
   - Request algorithm fidelity check and feature completeness
   - Request clear recommendation (APPROVE/REJECT/ESCALATE)

2. **@time_validator's response** (standardized):
   - Files read verification
   - Per-model breakdown with rationale
   - Fidelity checks
   - Clear recommendation with rationale

3. **@director's decision** (systematic):
   - Evaluate @time_validator's recommendation
   - Check competition time remaining
   - Execute decision (PROCEED/CONSULT/etc.)

**Affected Agents**:
- **@director** (MUST call with explicit instructions)
- **@time_validator** (MUST read all files, MUST provide clear recommendation)

**Implementation**:
- See `07_director_time_validator_handoff.md` for full specification

---

### Protocol 8: Model Design Expectations Framework *(v2.5.7)*

**Purpose**: Systematic validation of model designs against implementation with tolerance specifications.

**Key Framework**:
1. **Mandatory Design Expectations Table** (by @modeler):
   | Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
   |-----------|---------------------|-----|-----|------|-------------------|
   | Sampler | NUTS | NUTS | NUTS | - | YES |
   | Chains | 4 | 4 | 4 | chains | YES |
   | Draws | 20000 | 20000 | 20000 | samples | YES |
   | Features | 15 | 15 | 15 | features | YES |

2. **Systematic Comparison Table** (by @time_validator):
   | Parameter | Design | Actual | Diff | Tolerance | Verdict |
   |-----------|--------|--------|------|-----------|---------|
   | Sampler | NUTS | Slice | Changed | Exact | ❌ FAIL |
   | Chains | 4 | 2 | -50% | ±20% | ❌ FAIL |

3. **Scoring System**:
   - CRITICAL parameters: Auto-reject if fail
   - HIGH parameters: ±20% tolerance
   - Overall score: Must be ≥80%
   - **Rule**: One fail = all fail

**Affected Agents**:
- **@modeler** (MUST create design expectations table)
- **@time_validator** (MUST create comparison table, calculate score)
- **@director** (MUST enforce "one fail = all fail" rule)

**Implementation**:
- See `08_model_design_expectations.md` for full specification

---

### Protocol 9: @validator/@advisor Brief Format *(v2.5.7)*

**Purpose**: Enable fast decision-making by requiring concise evaluations in chat, detailed reports to files.

**Key Protocol**:
1. **Brief Format (First 4 lines in chat)**:
   ```
   Grade: 9.0/10 | Verdict: ✅ PASS
   Justification: Mathematically sound with proper specification.
   File verified: output/model/model_design_1.md (324 lines)
   Detailed report written to: output/docs/validation/validator_model_1.md
   ```

2. **Detailed Reports (Written to file, NOT shown in chat)**:
   - Standard template for all reports
   - Can be referenced if revision needed
   - @director does NOT read these reports

3. **@director Decision Logic (Simplified)**:
   - IF @validator PASS AND @advisor PASS → RETURN "APPROVE"
   - ELSE → RETURN "REJECT"

4. **Standardized Report Template**:
   - File Information (path, lines, timestamp)
   - Grade + Verdict
   - Brief Evaluation (1 sentence)
   - Detailed Analysis (for reference)

**Affected Agents**:
- **@validator** (MUST use brief format in chat, detailed report to file)
- **@advisor** (MUST use brief format in chat, detailed report to file)
- **@director** (MUST read only brief format, apply pass/fail rule)

**Implementation**:
- See `09_validator_advisor_brief_format.md` for full specification

---

### Protocol 10: Phase 5B Error Monitoring *(v2.5.7)*

**Purpose**: Prevent errors from being lost by keeping AI session active during training with watch mode.

**Key Protocol**:
1. **AI Session Does NOT Exit**:
   - Training runs in background
   - @model_trainer enters "watch mode"
   - Session stays active, monitoring for errors

2. **Watch Mode Implementation**:
   ```python
   while True:
       check_process_status()
       check_log_file_for_errors()
       if error_detected:
           report_to_director()
           await_guidance()
       if training_complete:
           report_completion()
   ```

3. **Error Resolution Workflow**:
   - @model_trainer detects error → Reports to @director
   - @director delegates fix (@code_translator, @data_engineer, or @modeler)
   - Fix applied → Resume training (no restart from scratch)

4. **Status Reporting**:
   - Regular updates every 30 minutes
   - Immediate error notification
   - Completion report with summary

**Affected Agents**:
- **@model_trainer** (MUST enter watch mode, MUST NOT exit session)
- **@director** (MUST coordinate error resolution)
- **@code_translator** (MUST fix implementation errors)
- **@data_engineer** (MUST fix data errors)

**Implementation**:
- See `10_phase5b_error_monitoring.md` for full specification

---

### Protocol 11: Emergency Convergence Delegation *(v2.5.8)*

**Purpose**: Enable fast response (30-60 min) for critical convergence failures while maintaining @director coordination.

**When to Use** (ALL criteria must be met):
1. Error Category: **Convergence (Category 4)**
2. Severity: **CRITICAL**
   - R-hat > 1.3 (severe non-convergence)
   - OR no convergence after 12 hours of training
   - OR >10% divergent transitions
   - OR complete sampling failure
3. @modeler is **available and responsive**
4. Fix is **well-understood** (parameter adjustment, NOT algorithm change)

**Emergency Flow** (bypasses standard @director delegation):
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
- **Oversight**: @director retroactive approval required

**Response Time**:
- Standard protocol: 4-5 hours
- Emergency protocol: **30-60 minutes** (8x faster)

**Affected Agents**:
- **@model_trainer** (MUST verify criteria before escalating)
- **@modeler** (MUST authorize, delegate to @code_translator)
- **@code_translator** (MUST implement fix, copy @director)
- **@director** (MUST provide retroactive approval within 1 hour)

**Implementation**:
- See `11_emergency_delegation.md` for full specification

---

### Protocol 12: Phase 4.5 Re-Validation *(v2.5.9)*

**Purpose**: Close rework validation gap to prevent academic fraud through unauthorized simplification during training fixes.

**Problem Fixed**: Reworked code during training was NOT re-validated against Design Expectations Table.

**Key Protocol**:
1. **@code_translator MUST provide CHANGES SUMMARY** for all fixes:
   ```markdown
   ## CHANGES SUMMARY
   - File: model_{i}.py
   - Original issue: {description}
   - Fix applied: {description}
   - Parameters changed: {list}
   - Algorithm changed: YES/NO
   - Features changed: YES/NO
   ```

2. **@director analyzes CHANGES SUMMARY**:
   - IF parameter changes detected → Trigger re-validation
   - IF algorithm changed → Full Phase 1 rewind required
   - IF simple bug fix → Resume training

3. **Conditional Re-Validation** (triggered by parameter changes):
   - @director calls @time_validator: "RE-VALIDATION REQUIRED"
   - @time_validator runs Phase 4.5 on reworked code
   - IF ✅ APPROVE → Resume training
   - IF ❌ REJECT → Full rework required

4. **Hidden Modification Detection**:
   - Compare reworked code against Design Expectations Table
   - Check for unauthorized simplifications
   - Verify all parameters within tolerance

**Affected Agents**:
- **@code_translator** (MUST provide changes summary for all fixes)
- **@director** (MUST analyze changes, trigger re-validation)
- **@time_validator** (MUST re-validate when requested)

**Implementation**:
- See `12_phase45_revalidation.md` for full specification

---

## Agent System

### Agent Overview

| Agent | Responsibility | Key Features | Validation Participation |
|-------|---------------|--------------|------------------------|
| `reader` | Read PDF, extract requirements | Mandatory requirement extraction | MODEL, DATA, PAPER |
| `researcher` | Method suggestions | O-Prize alignment | MODEL |
| `modeler` | Design mathematical models | Design expectations table required | DATA, CODE, TRAINING |
| `feasibility_checker` | Feasibility check | Technical feasibility validation | MODEL, CODE |
| `data_engineer` | Data processing | Feature engineering, integrity checks | - |
| `code_translator` | Code translation | Idealistic mode, simplification = fraud | CODE, TRAINING |
| `model_trainer` | Model training | Watch mode, no-exit during Phase 5B | - |
| `validator` | Result validation | Brief format + detailed report to file | DATA, TRAINING, FINAL |
| `visualizer` | Generate figures | Quality verification | - |
| `writer` | Write papers | LaTeX compilation gate | PAPER |
| `summarizer` | Create summary | 1-page summary | - |
| `editor` | Polish documents | Grammar/style/consistency | - |
| `advisor` | Quality assessment | Brief format + detailed report to file | MODEL, PAPER, FINAL |
| `time_validator` | Time validation, anti-lazy | STRICT MODE + comparison tables | Called after MODEL, CODE, TRAINING |
| **`director`** | **Team coordination** | **File reading BAN + simplified decision logic** | **N/A** |

> **Total**: 14 agents with enhanced behavioral constraints

---

## Phase Overview

| Phase | Name | Main Agent | Validation Gate | Key Features |
|-------|------|-----------|-----------------|--------------|
| **0** | Problem Understanding | reader, researcher | - | Initial research |
| **0.5** | **Model Methodology Quality Gate** | **@advisor, @validator** | **✅ METHODOLOGY** | @director file ban enforced |
| 1 | Model Design | modeler | ✅ MODEL (5 agents) | Multi-agent consultation |
| 1.5 | Time Estimate Validation | @time_validator | ✅ TIME_CHECK | Enhanced analysis |
| 2 | Feasibility Check | feasibility_checker | - | Technical validation |
| 3 | Data Processing | data_engineer | ✅ DATA (self) | Feature engineering |
| 4 | Code Translation | code_translator | ✅ CODE (2 agents) | Idealistic mode |
| **4.5** | **Implementation Fidelity** | **@time_validator** | **✅ FIDELITY** | STRICT MODE enforced |
| 5A | Quick Training | model_trainer | ✅ TRAINING | → Proceed to paper |
| 5B | Full Training | model_trainer | ✅ TRAINING | >6h parallel w/ paper, emergency protocol |
| **5.5** | **Data Authenticity** | **@time_validator** | **✅ ANTI_FRAUD** | Red line + analysis |
| 6 | Visualization | visualizer | - | Quick → final |
| 6.5 | Visual Quality Gate | visualizer, Director | ✅ VISUAL | Image corruption check |
| 7 | Paper Writing | writer | ✅ PAPER (4 agents) | Draft w/ quick, update w/ final |
| 7.5 | LaTeX Compilation Gate | writer, Director | ✅ LATEX | Compilation verification |
| 8 | Summary | summarizer | ✅ SUMMARY (2 agents) | 1-page summary |
| 9 | Polish | editor | ✅ FINAL (3 agents) | Grammar/style/consistency |
| 9.5 | Editor Feedback Enforcement | Director, multiple agents | ✅ EDITOR | Multi-agent rework |
| 10 | Final Review | advisor | - | Final quality check |

---

## Core Protocols

### Protocol 1: @director File Reading Ban
**Purpose**: Prevent @director from contaminating agent evaluations by reading files first.

**Scope**: Phases 0.5, 1, 4, 10 (any phase where @director delegates evaluation)

**Rules**:

1. **@director CANNOT read files that agents will evaluate**
   ```
   ❌ FORBIDDEN:
   @director reads research_notes.md → forms understanding → calls @advisor

   ✅ CORRECT:
   @director calls @advisor: "Read output/docs/research_notes.md and evaluate"
   ```

2. **@director MUST specify exact file paths**
   ```
   ❌ VAGUE: "@advisor: Evaluate the methodology quality"
   ✅ EXPLICIT: "@advisor: Read output/docs/research_notes.md and evaluate methodology"
   ```

3. **Agents MUST report which file they read**
   ```
   @advisor's report MUST include:
   - "I read: output/docs/research_notes.md"
   - "File size: 843 lines"
   - "Last modified: [timestamp]"
   ```

4. **@director MUST verify correct file was read**
   ```
   @director's checklist:
   - [ ] Agent specified which file they read
   - [ ] File path matches expected location
   - [ ] File size/timestamp is current
   - [ ] Evaluation content matches file content
   ```

**Implementation**:
- See `02_director_file_reading_ban.md` for full specification
- Update @director (CLAUDE.md) with ban rules
- Update @advisor, @validator with file reporting requirements

---

### Protocol 2: @time_validator Strict Mode
**Purpose**: Ensure @time_validator rejects ALL lazy implementations, especially training duration shortcuts.

**Scope**: Phases 4.5 (Implementation Fidelity), 5.5 (Data Authenticity)

**Rules**:

1. **Training Duration Red Line**
   ```
   Expected: 12-18 hours
   Minimum acceptable: 3.6 hours (30% of minimum expected)

   ❌ REJECT if actual < 3.6 hours:
   - 43 minutes = 0.72 hours → 23× below threshold → AUTO-REJECT
   - 2 hours = 120 minutes → Below threshold → REJECT
   ```

2. **Algorithm Match Verification**
   ```
   Design specifies: PyMC with HMC sampling
   Code uses: sklearn.LinearRegression
   Verdict: ❌ LAZY IMPLEMENTATION → REJECT
   ```

3. **Feature Completeness Check**
   ```
   Design: 15 features including X, Y, Z
   Code: "Use available columns" (only 10 columns)
   Verdict: ❌ INCOMPLETE → REJECT
   ```

4. **Iteration/Parameter Verification**
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

**Implementation**:
- See `03_time_validator_strict_mode.md` for full specification
- Update @time_validator with strict mode rules
- Update @code_translator with "simplification = fraud" warnings

---

## Supporting Protocols

### File Standardization
1. **Feedback File Standardization** - Canonical path + naming enforced
2. **Enhanced Phase 5.5 Anti-Fraud** - Training skip detection, duration verification
3. **Phase 0.5 Model Quality Gate** - Methodology evaluation before implementation
4. **Image Naming Standards** - Fixed wildcards + standardized naming

### Quality Assurance
1. **Strict Re-verification Standards** - 3+ sentences, specific evidence required
2. **All Agents Re-verify** - ALL relevant agents re-verify, not just rejecters
3. **Reader Mandatory Requirements** - Selective requirements are MANDATORY
4. **Modeler Time Pressure Protocol** - Must consult @director before simplifying
5. **Director Systematic Role** - Master checklist, priority hierarchy, decision matrices
6. **@time_validator Agent** - Time validation, lazy detection, anti-fraud

---

## System Features Summary

| Feature | Description | Impact |
|---------|-------------|--------|
| @director file ban | @director BANNED from reading evaluation targets | Agent evaluations accurate |
| @time_validator STRICT MODE | Auto-reject lazy implementations | Academic fraud prevented |
| Phase 5 parallel workflow | Paper proceeds after 5A, 5B runs background | Save 6-12 hours |
| Idealistic code generation | @code_translator perfect implementation | No unauthorized simplification |
| Brief evaluation format | @validator/@advisor concise reports | Faster decision-making |

---

## Testing Checklist

Before deployment, verify:

- [ ] @director file reading ban documented
- [ ] @director protocol specifies exact file paths
- [ ] Agents (@advisor, @validator) required to report file read
- [ ] @time_validator strict mode rules documented
- [ ] Training duration red line (30% threshold) specified
- [ ] Algorithm match verification specified
- [ ] @code_translator "simplification = fraud" warnings added
- [ ] Model design expectations table template documented
- [ ] @time_validator comparison table format specified
- [ ] @modeler design expectations requirements documented
- [ ] @validator/@advisor brief format documented
- [ ] @director simplified decision logic documented
- [ ] Phase 5B watch mode protocol documented
- [ ] Error resolution workflow documented
- [ ] All agent prompts updated
- [ ] Workspace synchronized with architecture
- [ ] Test cases for file reading ban
- [ ] Test cases for training duration rejection
- [ ] Test cases for model design expectations validation
- [ ] Test cases for @validator/@advisor brief format
- [ ] Test cases for Phase 5B error monitoring

---

**Document Version**: v2.6.0
**Last Updated**: 2026-01-23
**Status**: Complete

**For detailed specifications**, see:
- **01_SUMMARY.md** - Complete system summary
- **02_director_file_reading_ban.md** - @director file reading prohibition
- **03_time_validator_strict_mode.md** - @time_validator strict enforcement
- **04_phase_5_parallel_workflow.md** - Phase 5 parallel workflow
- **05_time_validator_enhanced_analysis.md** - @time_validator line-by-line analysis
- **06_code_translator_idealistic_mode.md** - @code_translator idealistic mode
- **07_director_time_validator_handoff.md** - @director/@time_validator handoff
- **08_model_design_expectations.md** - Model design expectations validation
- **09_validator_advisor_brief_format.md** - @validator/@advisor brief format
- **10_phase5b_error_monitoring.md** - Phase 5B error monitoring
- **11_emergency_delegation.md** - Emergency convergence delegation
- **12_phase45_revalidation.md** - Phase 4.5 re-validation
