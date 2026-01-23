# MCM-Killer v2.6.0 System Architecture

> **Authoritative Architecture Definition** — All Agent prompts should be derived from this document.
> **Version**: v2.6.0 (Integration Release)
> **Date**: 2026-01-23
> **Architecture Overview**: Complete integration of all v2.5.7-v2.5.9 protocols into unified system architecture with 12 critical protocols

---

## 📚 Document Navigation

| Document | Purpose |
|----------|---------|
| **`00_ARCHITECTURE.md`** (this document) | **Complete architecture definition** |
| **`v2-6-0_new.md`** | **Future changes and TODO** |
| **`01_SUMMARY.md`** | **Summary of all 12 protocols** |
| **`02-12_*.md`** | **Detailed protocol specifications** |

**Reading Order**:
1. This document (00_ARCHITECTURE.md) - Complete system overview
2. 01_SUMMARY.md - Protocol summaries
3. 02-12_*.md - Detailed specifications

---

## System Overview

**MCM-Killer** is a multi-agent autonomous system for MCM (Mathematical Contest in Modeling) competition participation. The system coordinates 14 specialized agents through a structured 10-phase workflow to produce complete research papers from problem statements.

### Core Principles

1. **Agent Specialization**: Each agent has a single, well-defined responsibility
2. **Quality Gates**: Multiple validation gates ensure output quality at each phase
3. **Anti-Fraud**: Strict protocols prevent lazy implementation and academic fraud
4. **Parallel Workflow**: Paper writing proceeds while full training runs in background
5. **Emergency Response**: Fast response (30-60 min) for critical convergence errors

### System Goals

- **O-Prize Competitive**: Produce papers competitive for the $1.5M O-Prize
- **Autonomous Operation**: Minimal human intervention during competition
- **Quality Assurance**: Multiple validation layers prevent errors
- **Time Efficiency**: Parallel workflows save 6-12 hours
- **Academic Integrity**: Zero tolerance for fraud or simplification

---

## Version Evolution

| Version | Date | Type | Key Changes |
|---------|------|------|-------------|
| v2.5.5 | 2026-01-17 | Enhancement | 6 enhancements + @time_validator agent |
| v2.5.6 | 2026-01-18 | Bugfix | 4 fixes: Feedback files, Phase 5.5, Phase 0.5, Image naming |
| v2.5.7 | 2026-01-19 | Enhancement | 10 protocols: File ban, Strict mode, Parallel workflow, Enhanced analysis, Idealistic mode, 48h escalation, Handoff, Design expectations, Brief format, Error monitoring |
| v2.5.8 | 2026-01-19 | Enhancement | Protocol 11: Emergency delegation (8× faster convergence fixes) |
| v2.5.9 | 2026-01-20 | Critical Fix | Protocol 12: Phase 4.5 re-validation (8× fraud reduction) |
| **v2.6.0** | **2026-01-23** | **🎯 INTEGRATION** | **Complete integration of all 12 protocols from v2.5.7-v2.5.9** |

---

## Critical Problems and Solutions

### Problem 1: @director Reads Files → Agent Evaluations Contaminated

**Symptom**:
```
CRITICAL DISCREPANCY DETECTED

  @validator: 9/10 (APPROVED) - sees sophisticated methods
  @advisor: 1/10 (CRITICAL FAILURE) - sees NO methodological content

  research_notes.md file contains 843 lines of sophisticated mathematical methods.

  - @validator: 9/10 (CORRECT) - sees detailed equations and methods
  - @advisor: 1/10 (ERROR) - claims "ZERO methodological content"
```

**Root Cause**:
- **@director read research_notes.md independently**
- **@director called @advisor with implicit context from memory**
- **@advisor evaluated a DIFFERENT file or worked from contaminated context**
- **@advisor did NOT read the actual research_notes.md file**

**Why This Happens**:
1. @director wants to "verify" work before delegating
2. @director reads file, forms own understanding
3. @director calls @advisor with: "Evaluate methodology quality"
4. @advisor works from @director's summary, not the actual file
5. OR @advisor reads a stale/different file

**Solution**: **Protocol 1: @director File Reading Ban**

**Key Rules**:
1. **@director CANNOT read files that agents will evaluate**
   - Forbidden: @director reads research_notes.md before calling @advisor
   - Required: @director calls @advisor with explicit file path

2. **@director MUST specify exact file paths**
   - Bad: "@advisor: Evaluate the methodology" (no file specified)
   - Good: "@advisor: Read output/docs/research_notes.md and evaluate methodology"

3. **@director MUST verify agents read the correct file**
   - After calling @advisor, ask: "What file did you read?"
   - Check that @advisor's report references the correct file

4. **Agents MUST explicitly state which file they read**
   - @advisor's report MUST include: "I read: output/docs/research_notes.md (843 lines)"
   - If wrong file → Re-call with explicit instruction

**Implementation**: See `02_director_file_reading_ban.md`

---

### Problem 2: @code_translator Simplifies → Training Time 12-18h → 43min

**Symptom**:
```
Phase 5B 代码Bug (4个模型的实现问题)

  | 模型    | Bug                                            | 影响                 |
  |---------|------------------------------------------------|----------------------|
  | Model 3 | PyMC API 兼容性：TensorVariable 没有 logp 属性 | 使用简化逻辑回归替代 |
  | Model 4 | 函数名错误：prepare_factor_model 未定义        | 使用 PCA 替代        |
  | Model 5 | 数据结构不匹配：KeyError: 'years'              | 简化的变点检测       |
  | Model 6 | 列名错误：KeyError: 'Gold'                     | 使用可用列           |

  原因：@code_translator 写的代码与数据结构不匹配

  影响：训练时间从预期的 12-18 小时降至 43 分钟（低于 O-Prize 标准）
```

**Root Cause**:
1. **@code_translator encounters implementation error** (e.g., KeyError, API incompatibility)
2. **@code_translator chooses "simplified alternative" instead of fixing**
3. **@code_translator does NOT consult @director before simplifying**
4. **@time_validator does NOT reject 43-minute training** (should be 12-18 hours)
5. **Result: Academic fraud through simplification**

**Why This Happens**:
- @code_translator thinks: "This won't work, I'll use simpler version"
- @code_translator doesn't realize: **Simplification = Academic Fraud**
- @time_validator checks: "Did training complete?" not "Is this the designed method?"

**Solution**: **Protocol 2: @time_validator Strict Mode**

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
   - **Priority**: Fix implementation problems > Accept lazy shortcuts

**Implementation**: See `03_time_validator_strict_mode.md`

**Consequences of Lazy Implementation**:
1. **First offense**: @code_translator must rework completely
2. **Second offense**: @director issues formal warning
3. **Third offense**: Consider agent replacement (reinitialize agent)

---

### Problem 3: @time_validator Time Predictions Inaccurate (Orders of Magnitude)

**Symptom**:
```
@time_validator prediction: 16 hours
Actual training time: 43 minutes
Error: 22× underestimate

@time_validator prediction: 12 hours
Actual training time: 2 hours
Error: 6× underestimate
```

**Root Cause**:
- **@time_validator only reads model_design.md** (not actual code)
- **@time_validator doesn't check dataset size** (assumes generic)
- **@time_validator doesn't analyze algorithmic complexity** (uses generic estimates)
- **@time_validator misses simplifications** (sklearn vs PyMC not detected)

**Solution**: **Protocol 3: Enhanced @time_validator Analysis**

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

**Implementation**: See `05_time_validator_enhanced_analysis.md`

---

### Problem 4: Phase 5B Blocks Paper Writing (6-12 hours wait)

**Symptom**:
```
Phase 5A (30 min) → Phase 5B (6-12 hours) → Phase 6 → Phase 7

@writer idle for 6-12 hours waiting for Phase 5B
```

**Root Cause**:
- **Sequential workflow**: Paper must wait for training
- **No parallelization**: @writer could work with quick results
- **Time wasted**: 6-12 hours of dead time

**Solution**: **Protocol 4: Phase 5 Parallel Workflow**

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
- **Old spec (v2.5.6)**: "4-6 hours" → **WRONG** (too optimistic)
- **New spec (v2.5.7)**: ">6 hours" → **CORRECT** (realistic)
  - Minimum: 6 hours
  - Typical: 8-12 hours
  - Maximum: 48 hours (with @director approval)

**Impact**: Save 6-12 hours per competition through parallelization

**Implementation**: See `04_phase_5_parallel_workflow.md`

---

### Problem 5: @code_translator "Pragmatic" → Simplifies Implementation

**Symptom**:
```
@code_translator: "KeyError: 'Gold' → I'll use available columns"
@code_translator: "PyMC doesn't work → I'll use sklearn"
@code_translator: "Training too slow → I'll reduce iterations"
```

**Root Cause**:
- **@code_translator thinks pragmatically** ("make it work")
- **@code_translator doesn't realize simplification = fraud**
- **No idealistic mindset** enforced

**Solution**: **Protocol 5: @code_translator Idealistic Mode**

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

**Implementation**: See `06_code_translator_idealistic_mode.md`

---

### Problem 6: 48-Hour Training → Unclear Decision Process

**Symptom**:
```
@time_validator: "Training estimate: 78 hours (>48 hours threshold)"
@director: "Should I approve? Should I ask @modeler to simplify? What are the criteria?"
```

**Root Cause**:
- **Unclear escalation threshold**
- **No decision framework**
- **@director might simplify unilaterally**

**Solution**: **Protocol 6: 48-Hour Escalation Protocol**

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

**Implementation**: See `07_director_time_validator_handoff.md`

---

### Problem 7: @director/@time_validator Handoff Unclear

**Symptom**:
```
@director calls @time_validator: "Check if this is OK"
@time_validator: "Looks good"
@director: "But what did you check? What are the criteria?"
```

**Root Cause**:
- **Unclear handoff protocol**
- **Ambiguous responsibilities**
- **No standardized communication**

**Solution**: **Protocol 7: @director/@time_validator Handoff**

**Key Protocol**:
1. **@director's call to @time_validator** (explicit):
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

2. **@time_validator's response** (standardized):
   - Files read verification
   - Per-model breakdown (with rationale)
   - Fidelity checks
   - Clear recommendation with rationale

3. **@director's decision** (systematic):
   - Evaluate @time_validator's recommendation
   - Check competition time remaining
   - Execute decision (PROCEED/CONSULT/etc.)

**Implementation**: See `07_director_time_validator_handoff.md`

---

### Problem 8: No Model Design Expectations Listed → No Systematic Validation

**Symptom**:
```
Model design says: "NUTS sampler with 10000 draws"
Implementation: "Slice sampler with 1000 draws"

Current state:
- No explicit design expectations documented
- No parameter tolerance specifications
- No scoring tables for validation
- No systematic comparison (Design vs Actual)
- No "one fail = all fail" enforcement
```

**Root Cause**:
- **Model designs lack explicit expectations tables**
- **No tolerance specifications** (What's acceptable deviation?)
- **No scoring system** (How to grade compliance?)
- **No systematic comparison format** (Design vs Actual vs Tolerance vs Verdict)

**Solution**: **Protocol 8: Model Design Expectations Framework**

**Key Framework**:
1. **Mandatory Design Expectations Table**:
   ```markdown
   | Parameter | Design Specification | Min | Max | Unit | Must Not Simplify |
   |-----------|---------------------|-----|-----|------|-------------------|
   | Sampler | NUTS | NUTS | NUTS | - | YES |
   | Chains | 4 | 4 | 4 | chains | YES |
   | Draws | 20000 | 20000 | 20000 | samples | YES |
   | Features | 15 | 15 | 15 | features | YES |
   ```

2. **Systematic Comparison Table** (by @time_validator):
   ```markdown
   | Parameter | Design | Actual | Diff | Tolerance | Verdict |
   |-----------|--------|--------|------|-----------|---------|
   | Sampler | NUTS | Slice | Changed | Exact | ❌ FAIL |
   | Chains | 4 | 2 | -50% | ±20% | ❌ FAIL |
   ```

3. **Scoring System**:
   - CRITICAL parameters: Auto-reject if fail
   - HIGH parameters: ±20% tolerance
   - Overall score: Must be ≥80%
   - **Rule**: One fail = all fail

4. **@director Enforcement**:
   ```python
   if ANY critical_param FAIL:
       return "REJECT"  # No exceptions
   elif overall_score < 0.8:
       return "REJECT"
   else:
       return "APPROVE"
   ```

**Implementation**: See `08_model_design_expectations.md`

---

### Problem 9: @validator/@advisor Verbose → @director Thinking Too Long

**Symptom**:
```
@validator: "I've reviewed the methodology document in detail.
           The document contains sophisticated Bayesian hierarchical models
           with NUTS sampling, 4 chains, 20000 samples. The approach is
           mathematically sound with proper priors. The convergence
           diagnostics are appropriate. I find this to be excellent work.
           Grade: 9/10"

@advisor: "After careful analysis of the methodological framework,
          I have concerns about the lack of sensitivity analysis.
          The document would benefit from additional robustness checks.
          However, the core approach is solid. Grade: 7/10"

@director: [Spends 5 minutes analyzing both verbose reports]
           "Let me think about this. @validator gave 9/10, @advisor gave 7/10.
           @validator says sophisticated Bayesian approach, @advisor says
           lacks sensitivity analysis. Should I approve or request revision?"
```

**Root Cause**:
- **@validator and @advisor write verbose reports** (10+ sentences)
- **@director must read and analyze verbose reports**
- **No standardized brief format**
- **@director makes decision based on deliberation** (should be automatic)

**Solution**: **Protocol 9: @validator/@advisor Brief Format**

**Key Protocol**:
1. **Brief Format (First 4 lines only)**:
   ```
   Grade: 9.0/10 | Verdict: ✅ PASS
   Justification: Mathematically sound with proper specification.
   File verified: output/model/model_design_1.md (324 lines)
   Detailed report written to: output/docs/validation/validator_model_1.md
   ```

2. **Detailed Reports (Written to file, NOT shown in chat)**:
   - Standard template for all reports
   - Can be referenced by @researcher if revision needed
   - @director does NOT read these reports

3. **@director Decision Logic (Simplified)**:
   ```
   IF @validator PASS AND @advisor PASS:
       RETURN "APPROVE"
   ELSE:
       RETURN "REJECT"
   ```

4. **Standardized Report Template**:
   - File Information (path, lines, timestamp)
   - Grade + Verdict
   - Brief Evaluation (1 sentence)
   - Detailed Analysis (for @researcher reference)

**Impact**: Faster decision-making, less @director cognitive load

**Implementation**: See `09_validator_advisor_brief_format.md`

---

### Problem 10: Phase 5B Errors → AI Session Exits → Errors Lost

**Symptom**:
```
Model 2 Failed: 'TensorVariable' object has no attribute 'logp'
Error: Custom Zero-Truncated Poisson likelihood implementation error

Current behavior:
1. @model_trainer starts training
2. Training runs for hours
3. Error occurs
4. AI session has already exited
5. Error discovered too late (hours or days later)
6. Must restart from scratch
```

**Root Cause**:
- **AI session exits after starting training**
- **No monitoring during execution**
- **Errors not caught in real-time**
- **No error recovery protocol**

**Solution**: **Protocol 10: Phase 5B Error Monitoring**

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

**Implementation**: See `10_phase5b_error_monitoring.md`

---

### Problem 11: Critical Convergence Errors → 4-5 Hour Resolution Time

**Symptom**:
```
Critical convergence error occurs at 3 AM during competition:
R-hat: 1.42 (threshold: 1.3)
Elapsed: 14 hours

Standard protocol response time: 4-5 hours
Problem: Competition deadline is approaching fast
Impact: Wasted time, potential competition failure
```

**Root Cause**:
- **Standard protocol is too slow**: @model_trainer → @director → @modeler → @director → @code_translator
- **@director may not be available**: Delays escalation
- **Time wasted waiting**: 4-5 hours is unacceptable for critical errors

**Solution**: **Protocol 11: Emergency Convergence Delegation** ⭐ v2.5.8

**Key Protocol**:
- **Direct escalation**: @model_trainer → @modeler → @code_translator (bypasses @director)
- **Retroactive approval**: @director reviews within 1 hour after fix
- **Safeguards**: Single-use limit, severity threshold, time limit, documentation

**When to Use** (ALL criteria must be met):
1. Error Category: Convergence (Category 4)
2. Severity: CRITICAL
   - R-hat > 1.3 (severe non-convergence)
   - OR no convergence after 12 hours of training
   - OR >10% divergent transitions
   - OR complete sampling failure
3. @modeler is available and responsive
4. Fix is well-understood (parameter adjustment, NOT algorithm change)

**Emergency Flow**:
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

**Impact**: 8× faster response (30-60 minutes vs 4-5 hours)

**Implementation**: See `11_emergency_delegation.md`

---

### Problem 12: Code Fixes During Training → No Re-validation → Academic Fraud Risk

**Symptom**:
```
@code_translator fixes bug during training:
Original code: "tune: 2000" (from design)
Fixed code: "tune: 4000" (parameter changed)

Problem: Fixed code is NOT re-validated against Design Expectations Table
Risk: 40% chance of unauthorized simplification or algorithm change
```

**Root Cause**:
- **Reworked code during training was NOT re-validated**
- **No CHANGES SUMMARY requirement**
- **@director doesn't analyze parameter changes**
- **Hidden modifications go undetected**

**Solution**: **Protocol 12: Phase 4.5 Re-Validation** ⭐ v2.5.9

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

**Impact**: 8× reduction in academic fraud risk (40% → <5%)

**Implementation**: See `12_phase45_revalidation.md`

---

## Agent System

### Complete Agent Overview

| Agent | Responsibility | Key Features | Validation Participation |
|-------|---------------|--------------|------------------------|
| `reader` | Read PDF, extract requirements | Mandatory requirement extraction | MODEL, DATA, PAPER |
| `researcher` | Method suggestions | O-Prize alignment + Phase 0.5 evaluation | MODEL |
| `modeler` | Design mathematical models | Design expectations table + training phase availability | DATA, CODE, TRAINING |
| `feasibility_checker` | Feasibility check | Technical feasibility validation | MODEL, CODE |
| `data_engineer` | Data processing | Feature engineering, integrity checks | - |
| `code_translator` | Code translation | Idealistic mode + changes summary requirement + emergency protocol compliance | CODE, TRAINING |
| `model_trainer` | Model training | Watch mode + emergency delegation support | - |
| `validator` | Result validation | Brief format + detailed report to file | DATA, TRAINING, FINAL |
| `visualizer` | Generate figures | Quality verification + image naming standards | - |
| `writer` | Write papers | LaTeX compilation gate | PAPER |
| `summarizer` | Create summary | 1-page summary | - |
| `editor` | Polish documents | Grammar/style/consistency | - |
| `advisor` | Quality assessment | Brief format + detailed report to file | MODEL, PAPER, FINAL |
| `time_validator` | Time validation, anti-lazy | STRICT MODE + re-validation mode | Called after MODEL, CODE, TRAINING |
| **`director`** | **Team coordination** | **File reading BAN + emergency delegation oversight + re-validation trigger** | **N/A** |

> **Total**: 14 agents with enhanced behavioral constraints

> **v2.6.0 Updates**: 4 agents with new Protocol 11/12 responsibilities (marked in **bold** above)

### Agent Detailed Responsibilities

#### @director (Team Coordinator)
- **Primary Role**: Coordinate all agents, manage workflow, make decisions
- **Critical Constraints**:
  - **CANNOT read files that agents will evaluate** (Protocol 1)
  - **MUST specify exact file paths** when delegating
  - **MUST verify agents read correct files**
  - **NEVER simplifies unilaterally** (Protocol 6)
  - **MUST provide retroactive approval** for emergency fixes (Protocol 11)
  - **MUST analyze CHANGES SUMMARY** and trigger re-validation (Protocol 12)
- **Decision Logic**: Simplified pass/fail based on @validator and @advisor brief reports

#### @modeler (Model Designer)
- **Primary Role**: Design mathematical models based on @researcher's methods
- **Critical Constraints**:
  - **MUST create Design Expectations Table** (Protocol 8)
  - **MUST be available during training phase** (Protocol 11)
  - **MUST fix design issues** (not accept "simpler version")
- **Training Phase Responsibilities** (Protocol 11):
  - Be available for consultation (30-min response target)
  - Monitor training logs (optional but recommended)
  - Analyze convergence failures (when consulted)
  - Document design issues (if found)

#### @code_translator (Code Translator)
- **Primary Role**: Translate model designs into Python code
- **Critical Constraints**:
  - **Idealistic mode**: "I am an idealist, a perfectionist" (Protocol 5)
  - **Simplification = Academic Fraud** (Protocol 2)
  - **MUST provide CHANGES SUMMARY** for all fixes (Protocol 12)
  - **MUST implement emergency fixes within 10 minutes** (Protocol 11)
- **Behavioral Rules**:
  - NEVER simplify without @director approval
  - NEVER "use available columns" when features missing
  - NEVER switch libraries (PyMC → sklearn)
  - ALWAYS report errors to @director
  - ALWAYS wait for guidance before proceeding

#### @model_trainer (Model Trainer)
- **Primary Role**: Execute model training and monitor for errors
- **Critical Constraints**:
  - **Watch mode**: AI session MUST NOT exit during Phase 5B (Protocol 10)
  - **Emergency escalation**: Direct to @modeler for critical errors (Protocol 11)
  - **Status reporting**: Every 30 minutes + immediate error notification
- **Error Resolution**:
  - Detect error → Report to @director
  - Await guidance (no session exit)
  - Apply fix → Resume training (no restart from scratch)

#### @time_validator (Time Validator)
- **Primary Role**: Validate time estimates, detect lazy implementation, prevent fraud
- **Critical Constraints**:
  - **STRICT MODE**: Auto-reject if training < 30% of expected (Protocol 2)
  - **MUST read 3 file types**: Model design, dataset, implementation (Protocol 3)
  - **MUST analyze line-by-line**: Imports, model definition, parameters, loops (Protocol 3)
  - **MUST provide clear recommendation**: APPROVE/REJECT/ESCALATE (Protocol 7)
  - **Re-validation mode**: Run Phase 4.5 on reworked code (Protocol 12)
- **Decision Matrix**:
  | Check | Pass Threshold | Fail Action |
  |-------|---------------|-------------|
  | Training duration | ≥ 30% of expected | Auto-reject |
  | Algorithm match | Exact match | Reject |
  | Features | All present | Reject |
  | Iterations | ≥ 80% of specified | Reject |

#### @validator (Result Validator)
- **Primary Role**: Validate data, training results, and final outputs
- **Critical Constraints**:
  - **Brief format**: First 4 lines in chat only (Protocol 9)
  - **Detailed report**: Written to file, NOT shown in chat (Protocol 9)
  - **MUST report which file was read**: "I read: output/docs/research_notes.md (843 lines)"
- **Brief Format Template**:
  ```
  Grade: 9.0/10 | Verdict: ✅ PASS
  Justification: Mathematically sound with proper specification.
  File verified: {file_path} ({line_count} lines)
  Detailed report written to: {report_path}
  ```

#### @advisor (Quality Advisor)
- **Primary Role**: Assess quality of models, papers, and final outputs
- **Critical Constraints**:
  - **Brief format**: First 4 lines in chat only (Protocol 9)
  - **Detailed report**: Written to file, NOT shown in chat (Protocol 9)
  - **Phase 0.5 evaluation**: Evaluate methodology quality before implementation
  - **MUST report which file was read**: Same as @validator
- **Brief Format**: Same as @validator

#### @researcher (Method Researcher)
- **Primary Role**: Suggest modeling methods based on problem requirements
- **Critical Constraints**:
  - **Phase 0.5 evaluation**: Methods evaluated before implementation
  - **O-Prize alignment**: Methods must be competitive for O-Prize
  - **Consultation feedback**: MUST provide feedback on model drafts

#### @data_engineer (Data Engineer)
- **Primary Role**: Process data, create features, ensure data integrity
- **Critical Constraints**:
  - **Feature engineering**: Create all features specified by @modeler
  - **Integrity checks**: Verify data quality
  - **Consultation feedback**: MUST provide feedback on model drafts

#### @feasibility_checker (Feasibility Checker)
- **Primary Role**: Assess technical feasibility of proposed models
- **Critical Constraints**:
  - **Technical validation**: Can this be implemented?
  - **Consultation feedback**: MUST provide feedback on model drafts

#### @visualizer (Figure Generator)
- **Primary Role**: Generate figures from model results
- **Critical Constraints**:
  - **Image naming standards**: `{model_number}_{figure_type}_{description}.png`
  - **Quality verification**: Check for corrupted images
  - **Two-pass generation**: Quick results first, final results later

#### @writer (Paper Writer)
- **Primary Role**: Write LaTeX paper from results
- **Critical Constraints**:
  - **LaTeX compilation gate**: Must compile successfully
  - **Two-pass writing**: Draft with quick results, update with final results

#### @editor (Document Editor)
- **Primary Role**: Polish paper for grammar, style, and consistency
- **Critical Constraints**:
  - **Multi-agent rework**: Coordinate rework based on feedback

#### @summarizer (Summary Creator)
- **Primary Role**: Create 1-page summary of paper
- **Critical Constraints**:
  - **Conciseness**: 1-page maximum

#### @reader (PDF Reader)
- **Primary Role**: Read problem PDF, extract requirements
- **Critical Constraints**:
  - **Mandatory requirements**: All requirements are MANDATORY (not optional)

---

## Phase Workflow

### Complete Phase Overview

| Phase | Name | Main Agent | Validation Gate | Key Features |
|-------|------|-----------|-----------------|--------------|
| **0** | Problem Understanding | reader, researcher | - | Initial research |
| **0.5** | **Model Methodology Quality Gate** | **@advisor, @validator** | **✅ METHODOLOGY** | @director file ban enforced |
| 1 | Model Design | modeler | ✅ MODEL (5 agents) | Multi-agent consultation |
| 1.5 | Time Estimate Validation | @time_validator | ✅ TIME_CHECK | Enhanced analysis |
| 2 | Feasibility Check | feasibility_checker | - | Technical validation |
| 3 | Data Processing | data_engineer | ✅ DATA (self) | Feature engineering |
| 4 | Code Translation | code_translator | ✅ CODE (2 agents) | Idealistic mode |
| **4.5** | **Implementation Fidelity** | **@time_validator** | **✅ FIDELITY** | STRICT MODE + re-validation |
| 5A | Quick Training | model_trainer | ✅ TRAINING | → Proceed to paper |
| 5B | Full Training | model_trainer | ✅ TRAINING | >6h parallel w/ paper + emergency protocol |
| **5.5** | **Data Authenticity** | **@time_validator** | **✅ ANTI_FRAUD** | Red line + analysis |
| 6 | Visualization | visualizer | - | Quick → final |
| 6.5 | Visual Quality Gate | visualizer, Director | ✅ VISUAL | Image corruption check |
| 7 | Paper Writing | writer | ✅ PAPER (4 agents) | Draft w/ quick, update w/ final |
| 7.5 | LaTeX Compilation Gate | writer, Director | ✅ LATEX | Compilation verification |
| 8 | Summary | summarizer | ✅ SUMMARY (2 agents) | 1-page summary |
| 9 | Polish | editor | ✅ FINAL (3 agents) | Grammar/style/consistency |
| 9.5 | Editor Feedback Enforcement | Director, multiple agents | ✅ EDITOR | Multi-agent rework |
| 10 | Final Review | advisor | - | Final quality check |

### Phase 0: Problem Understanding

**Participants**: @reader, @researcher

**Tasks**:
1. @reader reads problem PDF
2. @reader extracts all requirements (MANDATORY, not optional)
3. @researcher suggests modeling methods
4. @researcher writes research_notes.md

**Output**: `output/docs/research_notes.md`

**Next**: Phase 0.5 (Model Methodology Quality Gate)

---

### Phase 0.5: Model Methodology Quality Gate ⭐ v2.5.6

**Purpose**: Evaluate the quality of @researcher's proposed methods BEFORE @modeler starts implementation

**Participants**: @advisor, @validator

**Tasks**:
1. Read `output/docs/research_notes.md`
2. Evaluate each proposed method:
   - Sophistication level (basic / moderate / advanced)
   - Computational intensity (expected training time)
   - O-Prize competitiveness (weak / moderate / strong)
3. Assign grade (1-10) for each method
4. Provide feedback on weak methods

**Decision Criteria**:
- **Average grade >= 9/10**: ✅ PROCEED to Phase 1 (@modeler starts design)
- **Average grade 7-8/10**: ⚠️ ADVISE @researcher to enhance methods (optional)
- **Average grade < 7/10**: ❌ REWIND to Phase 0.5 (@researcher MUST brainstorm better methods)

**Output**: `output/docs/consultations/methodology_evaluation_1.md`

**Key Protocol**: @director CANNOT read research_notes.md (Protocol 1)

---

### Phase 1: Model Design

**Participants**: @modeler (primary), @researcher, @feasibility_checker, @data_engineer, @code_translator, @advisor

**Tasks**:
1. @modeler reads research_notes.md
2. @modeler writes draft model proposals (one per model)
3. @director sends drafts to 5 agents in PARALLEL for consultation
4. Each consultant provides feedback
5. @modeler reads all feedback
6. @modeler writes final model designs

**Output**:
- Draft proposals: `output/model/model_proposals/model_X_draft.md`
- Final designs: `output/model/model_design_X.md`

**Key Protocol**: Feedback File Standardization (v2.5.6)

**Canonical Path**: `output/docs/consultations/`
**Naming Convention**: `feedback_model_{model_number}_{agent_name}.md`

**Examples**:
- `feedback_model_1_researcher.md`
- `feedback_model_1_feasibility_checker.md`
- `feedback_model_1_data_engineer.md`
- `feedback_model_1_code_translator.md`
- `feedback_model_1_advisor.md`

**Validation Gate**: ✅ MODEL (5 agents provide feedback)

---

### Phase 1.5: Time Estimate Validation

**Participants**: @time_validator

**Tasks**:
1. Read 3 file types for each model:
   - Model design: `output/model/model_design_{i}.md`
   - Dataset: `output/implementation/data/features_{i}.pkl` (check shape/size)
   - Implementation: `output/implementation/code/model_{i}.py` (line-by-line analysis)
2. Analyze code line-by-line:
   - Import statements (which library?)
   - Model definition (what algorithm?)
   - Sampling parameters (how many iterations?)
   - Loops (nested = O(n²) or O(n³)?)
3. Use empirical table (not guesses):
   | Algorithm | Dataset | Samples | Expected Time |
   |-----------|---------|---------|---------------|
   | PyMC hierarchical | 5000×50 | 10000×4 | **12-15 hours** |
   | sklearn.LinearRegression | ANY | ANY | **<0.1 hours** |
4. Provide per-model and total time estimates
5. Algorithm fidelity check
6. Feature completeness check
7. Clear recommendation: APPROVE/REJECT/ESCALATE

**Output**: `output/docs/validation/time_validator_model_1.md`

**Validation Gate**: ✅ TIME_CHECK

---

### Phase 2: Feasibility Check

**Participants**: @feasibility_checker

**Tasks**:
1. Assess technical feasibility of each model
2. Identify potential implementation challenges
3. Provide feasibility assessment

**Output**: `output/model/feasibility_{i}.md`

**Validation Participation**: MODEL, CODE

---

### Phase 3: Data Processing

**Participants**: @data_engineer

**Tasks**:
1. Read problem data
2. Create features as specified in model designs
3. Perform feature engineering
4. Ensure data integrity
5. Save features to disk

**Output**: `output/implementation/data/features_{i}.pkl`

**Validation Gate**: ✅ DATA (self-validation)

**Key Protocol**: All features from design MUST be present (no "use available columns")

---

### Phase 4: Code Translation

**Participants**: @code_translator (primary), @modeler, @validator

**Tasks**:
1. @code_translator reads model design
2. @code_translator writes Python code
3. @code_translator reports completion
4. @validator validates code correctness
5. If validation fails → Rewind to Phase 4

**Output**: `output/implementation/code/model_{i}.py`

**Validation Gate**: ✅ CODE (2 agents: @modeler + @validator)

**Key Protocol**: @code_translator Idealistic Mode (Protocol 5)
- Identity: "I am an idealist, a perfectionist"
- Simplification = Academic Fraud
- ALWAYS report errors to @director
- NEVER simplify without approval

---

### Phase 4.5: Implementation Fidelity Check

**Participants**: @time_validator

**Tasks**:
1. Read model design expectations table (from Phase 1)
2. Read implementation code
3. Create comparison table:
   | Parameter | Design | Actual | Diff | Tolerance | Verdict |
   |-----------|--------|--------|------|-----------|---------|
   | Sampler | NUTS | Slice | Changed | Exact | ❌ FAIL |
   | Chains | 4 | 2 | -50% | ±20% | ❌ FAIL |
4. Calculate overall score
5. Apply "one fail = all fail" rule
6. Provide recommendation: APPROVE/REJECT

**Output**: `output/docs/validation/time_validator_code_{i}.md`

**Validation Gate**: ✅ FIDELITY

**Key Protocol**: STRICT MODE (Protocol 2)

**Re-Validation** (Protocol 12):
- If @code_translator fixes bug during training
- @director analyzes CHANGES SUMMARY
- IF parameter changes → Trigger Phase 4.5 re-validation
- @time_validator runs Phase 4.5 on reworked code
- IF ✅ APPROVE → Resume training
- IF ❌ REJECT → Full rework required

---

### Phase 5A: Quick Training

**Participants**: @model_trainer

**Tasks**:
1. Start quick training (reduced iterations)
2. Generate quick results: `results_quick_{i}.csv`
3. Report completion

**Output**: `output/results/results_quick_{i}.csv`

**Validation Gate**: ✅ TRAINING

**Time Expectation**: ~30 minutes

**Key Protocol**: Proceed immediately to Phase 6 (don't wait for Phase 5B)

---

### Phase 5B: Full Training (Parallel with Paper)

**Participants**: @model_trainer (primary), @director, @modeler, @code_translator

**Tasks**:
1. Start full training in background
2. Enter "watch mode" (AI session does NOT exit)
3. Monitor for errors:
   - Check process status every 60 seconds
   - Check log file for error patterns
   - Report errors immediately to @director
4. Report status every 30 minutes
5. When complete, report training summary

**Output**:
- Trained model: `output/implementation/models/model_{i}_full.pkl`
- Training log: `output/implementation/logs/training_{i}_full.log`
- Results: `output/results/results_{i}.csv`

**Validation Gate**: ✅ TRAINING

**Time Expectation**:
- Minimum: 6 hours
- Typical: 8-12 hours
- Maximum: 48 hours (with @director approval)

**Key Protocols**:
- **Watch mode** (Protocol 10): AI session does NOT exit
- **Emergency delegation** (Protocol 11): Direct @model_trainer → @modeler → @code_translator for critical convergence errors

**Error Resolution**:
- Detect error → Report to @director
- @director delegates fix
- Fix applied → Resume training (no restart from scratch)

**Emergency Delegation** (Protocol 11):
- **When to use**: R-hat > 1.3 OR 12h elapsed
- **Flow**: @model_trainer → @modeler → @code_translator → @director (retroactive)
- **Safeguards**: Single-use, 30-min limit, severity threshold, documentation

---

### Phase 5.5: Data Authenticity Gate

**Participants**: @time_validator (primary), @director

**Tasks**:
1. **Training Skip Detection** (v2.5.6):
   - Verify training log contains actual iteration progress
   - Check if epochs/iterations were actually executed
   - Look for "faked" logs (copied output without real training)

2. **Training Duration Verification** (v2.5.6):
   - Calculate expected duration based on method complexity
   - Compare to actual training duration
   - Flag if training was suspiciously fast (< 30% of expected)

3. **Result Authenticity** (v2.5.6):
   - Verify results match model type (Bayesian should have uncertainty, not point estimates)
   - Check if convergence criteria were actually met
   - Validate intermediate results (checkpoints if available)

4. **Code-Result Consistency** (v2.5.6):
   - Spot-check: Run code on subset, compare to CSV
   - Verify randomness (if random seed set, results should be reproducible)

**Decision Criteria**:
- **All checks pass**: ✅ AUTHENTIC → Proceed to Phase 6
- **1-2 checks fail**: ⚠️ SUSPICIOUS → Investigate, may request re-run
- **3+ checks fail**: ❌ FABRICATED → Re-run with verification

**Output**: `output/docs/validation/time_validator_data_{i}.md`

**Validation Gate**: ✅ ANTI_FRAUD

**Key Protocol**: STRICT MODE (Protocol 2) - Red line: Auto-reject if < 30% of expected

---

### Phase 6: Visualization

**Participants**: @visualizer

**Tasks**:
1. **First pass** (with quick results from Phase 5A):
   - Generate figures from `results_quick_{i}.csv`
   - Save with standard naming: `{model_number}_{figure_type}_{description}.png`
   - Verify image quality (check for corruption)

2. **Second pass** (when Phase 5B completes):
   - Regenerate figures with final results
   - Update all figures

**Output**: `output/figures/*.png`

**Key Protocol**: Image Naming Standards (v2.5.6)
- Naming: `{model_number}_{figure_type}_{description}.png`
- Examples:
  - `model_1_scatter_predictions_vs_actual.png`
  - `model_1_histogram_residuals.png`
  - `model_2_bar_feature_importance.png`

**Figure Types**:
- `scatter` - Scatter plots
- `line` - Line plots
- `bar` - Bar charts
- `histogram` - Histograms
- `heatmap` - Heatmaps
- `boxplot` - Box plots
- `violin` - Violin plots
- `diagram` - Flowcharts/diagrams

---

### Phase 6.5: Visual Quality Gate

**Participants**: @visualizer, @director

**Tasks**:
1. Verify all images exist
2. Check for corrupted images
3. Count images: `ls -1 output/figures/*.png | wc -l`
4. Verify image quality with PIL

**Decision**:
- ✅ PASS: All images present and valid
- ❌ FAIL: Corrupted images detected → Regenerate

**Validation Gate**: ✅ VISUAL

---

### Phase 7: Paper Writing

**Participants**: @writer (primary), @visualizer, @summarizer, @editor

**Tasks**:
1. **First pass** (with quick results from Phase 5A):
   - Write complete paper with quick results
   - Include all sections: Abstract, Introduction, Methods, Results, Discussion, Conclusion
   - Compile LaTeX
   - Generate PDF

2. **Second pass** (when Phase 5B completes):
   - Update Results section with final results
   - Update figures
   - Recompile LaTeX
   - Regenerate PDF

**Output**: `output/paper/paper.pdf`

**Validation Gate**: ✅ PAPER (4 agents: @writer + @visualizer + @summarizer + @editor)

**Key Protocol**: LaTeX Compilation Gate (Phase 7.5)

---

### Phase 7.5: LaTeX Compilation Gate

**Participants**: @writer, @director

**Tasks**:
1. Compile LaTeX document
2. Check for compilation errors
3. Verify PDF generated successfully

**Decision**:
- ✅ PASS: LaTeX compiles without errors
- ❌ FAIL: Compilation errors → Fix and recompile

**Validation Gate**: ✅ LATEX

---

### Phase 8: Summary

**Participants**: @summarizer (primary), @editor

**Tasks**:
1. Read paper
2. Create 1-page summary
3. Include key findings, methods, results

**Output**: `output/paper/summary.pdf`

**Validation Gate**: ✅ SUMMARY (2 agents: @summarizer + @editor)

**Constraint**: 1-page maximum

---

### Phase 9: Polish

**Participants**: @editor (primary), @writer, @summarizer

**Tasks**:
1. Review paper for grammar
2. Review for style consistency
3. Review for clarity
4. Make corrections
5. Finalize paper

**Output**: Polished `output/paper/paper.pdf`

**Validation Gate**: ✅ FINAL (3 agents: @editor + @writer + @summarizer)

---

### Phase 9.5: Editor Feedback Enforcement

**Participants**: @director, multiple agents

**Tasks**:
1. @editor provides feedback
2. @director coordinates rework
3. Multiple agents revise as needed
4. Re-verify changes

**Validation Gate**: ✅ EDITOR

**Key Protocol**: Multi-agent rework (all relevant agents participate)

---

### Phase 10: Final Review

**Participants**: @advisor

**Tasks**:
1. Read final paper
2. Assess overall quality
3. Provide final grade and feedback

**Output**: Final assessment report

**Key Protocol**: @advisor MUST report which file was read (Protocol 1)

---

## 12 Critical Protocols Summary

### Protocol 1: @director File Reading Ban
**Purpose**: Prevent @director from contaminating agent evaluations
**Implementation**: `02_director_file_reading_ban.md`
**Key Rules**:
- @director CANNOT read files that agents will evaluate
- @director MUST specify exact file paths
- Agents MUST explicitly state which file they read
- @director MUST verify agents read the correct file

---

### Protocol 2: @time_validator Strict Mode
**Purpose**: Reject ALL lazy implementations
**Implementation**: `03_time_validator_strict_mode.md`
**Key Rules**:
- Training Duration Red Line: Auto-reject if < 30% of expected
- Algorithm Match Verification: Must use designed algorithm exactly
- Feature Completeness Check: All features must be present
- Iteration/Parameter Verification: Must meet specifications

---

### Protocol 3: Enhanced @time_validator Analysis
**Purpose**: Improve time estimation accuracy
**Implementation**: `05_time_validator_enhanced_analysis.md`
**Key Enhancements**:
- MUST read 3 file types: Model design, Dataset, Implementation
- MUST analyze code line-by-line
- MUST use empirical table (not guesses)

---

### Protocol 4: Phase 5 Parallel Workflow
**Purpose**: Enable paper writing while training runs in background
**Implementation**: `04_phase_5_parallel_workflow.md`
**Key Changes**:
- Phase 5A (30 min) → Proceed to paper immediately
- Phase 5B (6-12 hours) → Runs in parallel
- Save 6-12 hours through parallelization

---

### Protocol 5: @code_translator Idealistic Mode
**Purpose**: Enforce perfect implementation
**Implementation**: `06_code_translator_idealistic_mode.md`
**Key Changes**:
- @code_translator identity: "I am an idealist, a perfectionist"
- Core philosophy: ONLY thing that matters = implement design perfectly
- Behavioral rules: NEVER simplify, ALWAYS report errors

---

### Protocol 6: 48-Hour Escalation Protocol
**Purpose**: Clear decision framework for long training estimates
**Implementation**: `07_director_time_validator_handoff.md`
**Key Framework**:
- If >48h AND buffer ≥20% → PROCEED
- If >48h AND buffer ≥0% → PROCEED_WITH_CAUTION
- If >48h AND buffer <0% → CONSULT_MODELER
- **CRITICAL**: @director NEVER simplifies unilaterally

---

### Protocol 7: @director/@time_validator Handoff
**Purpose**: Standardize communication
**Implementation**: `07_director_time_validator_handoff.md`
**Key Protocol**:
- @director's call: Specify files, request estimates + checks + recommendation
- @time_validator's response: Files read verification, breakdown, checks, recommendation
- @director's decision: Evaluate, check time, execute

---

### Protocol 8: Model Design Expectations Framework
**Purpose**: Systematic validation with tolerance specifications
**Implementation**: `08_model_design_expectations.md`
**Key Framework**:
- Mandatory Design Expectations Table (by @modeler)
- Systematic Comparison Table (by @time_validator)
- Scoring System: CRITICAL = auto-reject, HIGH = ±20%, overall ≥80%
- Rule: One fail = all fail

---

### Protocol 9: @validator/@advisor Brief Format
**Purpose**: Fast decision-making
**Implementation**: `09_validator_advisor_brief_format.md`
**Key Protocol**:
- Brief Format (First 4 lines in chat): Grade | Verdict | Justification | File verified | Report path
- Detailed Reports: Written to file, NOT shown in chat
- @director Decision Logic: IF both PASS → APPROVE, ELSE → REJECT

---

### Protocol 10: Phase 5B Error Monitoring
**Purpose**: Prevent errors from being lost
**Implementation**: `10_phase5b_error_monitoring.md`
**Key Protocol**:
- AI Session Does NOT Exit: Training runs in background, @model_trainer enters "watch mode"
- Watch Mode: While loop checking process + log file
- Error Resolution: Detect → Report → Delegate → Fix → Resume
- Status Reporting: Every 30 min + immediate error notification

---

### Protocol 11: Emergency Convergence Delegation ⭐ v2.5.8
**Purpose**: 30-60 min response for critical convergence errors
**Implementation**: `11_emergency_delegation.md`
**When to Use** (ALL criteria):
1. Error Category: Convergence (Category 4)
2. Severity: CRITICAL (R-hat > 1.3 OR 12h elapsed OR >10% divergent OR sampling failure)
3. @modeler available and responsive
4. Fix well-understood (parameter adjustment, NOT algorithm change)

**Emergency Flow**: @model_trainer → @modeler → @code_translator → @director (retroactive)

**Safeguards**: Single-use, 30-min limit, severity threshold, documentation, oversight

**Impact**: 8× faster (30-60 min vs 4-5 hours)

---

### Protocol 12: Phase 4.5 Re-Validation ⭐ v2.5.9
**Purpose**: Close rework validation gap to prevent academic fraud
**Implementation**: `12_phase45_revalidation.md`
**Key Protocol**:
- @code_translator MUST provide CHANGES SUMMARY for all fixes
- @director analyzes: IF parameter changes → Trigger re-validation
- @time_validator runs Phase 4.5 on reworked code
- IF ✅ APPROVE → Resume, IF ❌ REJECT → Full rework
- Hidden Modification Detection: Compare to Design Expectations Table

**Impact**: 8× fraud reduction (40% → <5%)

---

## Directory Structure

```
MCM-Killer/
├── architectures/              # Architecture documentation library (development reference)
│   ├── v2-3-0.md              # Legacy documentation
│   ├── v2-4-0/                # v2.4.0 modular architecture
│   ├── v2-4-1/                # v2.4.1 architecture and backup
│   ├── v2-4-2/                # v2.4.2 enhancements
│   ├── v2-5-0/                # v2.5.0 agent directory structure fix
│   ├── v2-5-1/                # v2.5.1 improvements
│   ├── v2-5-2/                # v2.5.2 enhancements
│   ├── v2-5-3/                # v2.5.3 YAML enforcement
│   ├── v2-5-4/                # v2.5.4 bug fixes
│   ├── v2-5-5/                # v2.5.5 enhancements + @time_validator
│   ├── v2-5-6/                # v2.5.6 critical fixes
│   ├── v2-5-7/                # v2.5.7 10 critical protocols
│   ├── v2-5-8/                # v2.5.8 emergency delegation
│   ├── v2-5-9/                # v2.5.9 Phase 4.5 re-validation
│   └── v2-6-0/                # v2.6.0 integration release (current)
│       ├── 00_ARCHITECTURE.md # This file
│       ├── v2-6-0_new.md     # Future changes and TODO
│       ├── 01_SUMMARY.md      # Protocol summary
│       └── 02-12_*.md         # Protocol specifications
│
└── workspace/
    └── 2025_C/
        └── .claude/
            ├── agents/        # Agent files (flat structure, runtime use)
            │   ├── director.md
            │   ├── model_trainer.md
            │   └── ... (14 agents total)
            └── CLAUDE.md      # Main configuration file
```

---

## Output Directory Structure

```
output/
├── VERSION_MANIFEST.json          # Version control metadata
│
├── docs/                          # ALL documentation goes here (MANDATORY)
│   ├── research_notes.md          # Research methodology and notes
│   ├── model/                     # Model design documents
│   │   ├── model_design_1.md
│   │   ├── model_design_2.md
│   │   ├── model_design_3.md
│   │   └── model_proposals/       # Draft proposals for consultation
│   │       ├── model_1_draft.md
│   │       ├── model_2_draft.md
│   │       └── model_3_draft.md
│   ├── consultations/             # Inter-agent consultation feedback
│   │   ├── feedback_model_1_researcher.md
│   │   ├── feedback_model_1_feasibility_checker.md
│   │   ├── feedback_model_1_data_engineer.md
│   │   ├── feedback_model_1_code_translator.md
│   │   ├── feedback_model_1_advisor.md
│   │   ├── feedback_model_2_researcher.md
│   │   └── ... (one file per agent per model)
│   ├── validations/               # Validation reports
│   │   ├── methodology_evaluation_1.md  # Phase 0.5 evaluation
│   │   ├── validator_model_1.md
│   │   ├── validator_data_1.md
│   │   ├── advisor_model_1.md
│   │   ├── time_validator_model_1.md
│   │   ├── time_validator_code_1.md
│   │   ├── time_validator_data_1.md
│   │   └── ... (one per validation per model)
│   └── feedback/                  # Re-verification feedback
│       ├── feedback_model_1.md
│       └── ... (one per model)
│
├── data/                          # Feature files (stage 3)
│   ├── features_1.pkl
│   ├── features_2.pkl
│   ├── features_3.pkl
│   ├── features_1.csv
│   ├── features_2.csv
│   └── features_3.csv
│
├── implementation/                # Implementation files (stage 4)
│   ├── .venv/                   # Python virtual environment
│   ├── code/                      # Python model code
│   │   ├── model_1.py
│   │   ├── model_2.py
│   │   ├── model_3.py
│   │   ├── test_1.py
│   │   ├── test_2.py
│   │   └── test_3.py
│   ├── data/                      # Processed datasets
│   │   ├── features_1.pkl
│   │   ├── features_2.pkl
│   │   └── features_3.pkl
│   ├── models/                    # Trained model objects
│   │   ├── model_1_full.pkl
│   │   ├── model_2_full.pkl
│   │   └── model_3_full.pkl
│   └── logs/                      # Training logs
│       ├── training_1_full.log
│       ├── training_2_full.log
│       └── training_3_full.log
│
├── results/                       # Results files (stage 5)
│   ├── results_1.csv
│   ├── results_2.csv
│   ├── results_3.csv
│   ├── results_quick_1.csv
│   ├── results_quick_2.csv
│   └── results_quick_3.csv
│
├── figures/                       # Figures (stage 6)
│   ├── model_1_scatter_predictions_vs_actual.png
│   ├── model_1_histogram_residuals.png
│   ├── model_1_trace_plot.png
│   ├── model_1_posterior_predictive.png
│   ├── model_2_bar_feature_importance.png
│   ├── model_2_line_convergence.png
│   └── ... (standardized naming: {model_number}_{figure_type}_{description}.png)
│
└── paper/                         # Paper outputs (stages 7-9)
    ├── paper.tex                  # LaTeX source
    ├── paper.pdf                  # Compiled PDF
    ├── paper.bib                  # Bibliography
    ├── summary.pdf                # 1-page summary
    └── figures/                   # Figures for paper
        ├── figure_1.png
        ├── figure_2.png
        └── ... (paper figures, copied from output/figures/)
```

---

## System Features Summary

| Feature | Description | Impact | Protocol |
|---------|-------------|--------|----------|
| @director file ban | @director BANNED from reading evaluation targets | Agent evaluations accurate | 1 |
| @time_validator STRICT MODE | Auto-reject lazy implementations | Academic fraud prevented | 2 |
| Phase 5 parallel workflow | Paper proceeds after 5A, 5B runs background | Save 6-12 hours | 4 |
| Idealistic code generation | @code_translator perfect implementation | No unauthorized simplification | 5 |
| Brief evaluation format | @validator/@advisor concise reports | Faster decision-making | 9 |
| Phase 5B error monitoring | Watch mode prevents lost errors | Real-time error resolution | 10 |
| **Emergency delegation** | **30-60 min critical error response** | **8× faster convergence fixes** | **11** ⭐ |
| **Re-validation trigger** | **Automatic validation of code fixes** | **8× fraud reduction** | **12** ⭐ |

---

## Testing Checklist

Before deployment, verify:

**Protocols 1-10 (v2.5.7 Inherited)**:
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
- [ ] Phase 5B watch mode protocol documented
- [ ] Error resolution workflow documented

**Protocol 11 (Emergency Delegation - v2.5.8)** ⭐:
- [ ] Emergency criteria documented (R-hat > 1.3, 12h elapsed)
- [ ] Emergency flow documented (@model_trainer → @modeler → @code_translator)
- [ ] Safeguards specified (single-use, severity threshold, time limit)
- [ ] @modeler training phase responsibilities documented
- [ ] @director retroactive approval process documented

**Protocol 12 (Re-Validation - v2.5.9)** ⭐:
- [ ] CHANGES SUMMARY template documented
- [ ] Re-validation trigger logic documented
- [ ] @time_validator re-validation mode specified
- [ ] Comparison table format for re-validation defined
- [ ] Decision rules (APPROVE/REJECT/ESCALATE) specified

**Integration**:
- [ ] All agent prompts updated with v2.6.0 protocols
- [ ] Workspace synchronized with architecture
- [ ] All 12 protocol documents updated to v2.6.0 format

---

## Conclusion

**v2.6.0** is a complete integration release that consolidates all protocols from v2.5.7-v2.5.9 into a unified system architecture with 12 critical protocols. This architecture ensures:

1. **Academic Integrity**: Zero tolerance for fraud or simplification
2. **Quality Assurance**: Multiple validation layers at each phase
3. **Time Efficiency**: Parallel workflows save 6-12 hours
4. **Error Recovery**: Real-time error monitoring and resolution
5. **Emergency Response**: 8× faster response for critical errors (30-60 min vs 4-5 hours)
6. **Fraud Prevention**: 8× reduction in academic fraud risk (40% → <5%)

All agents are strictly constrained by behavioral protocols that prevent common failure modes and ensure O-Prize competitive outputs.

---

**Document Version**: v2.6.0 (Integration Release)
**Last Updated**: 2026-01-23
**Status**: Complete ✅

**📚 Documentation Suite**:
- **00_ARCHITECTURE.md** - This file (complete architecture)
- **v2-6-0_new.md** - Future changes and TODO
- **01_SUMMARY.md** - Complete protocol summary
- **02-12_*.md** - Detailed protocol specifications (12 protocols)
