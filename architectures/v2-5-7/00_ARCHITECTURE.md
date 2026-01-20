# MCM-Killer v2.5.7 System Architecture

> **Authoritative Architecture Definition** — All Agent prompts should be derived from this document.
> **Version**: v2.5.7
> **Date**: 2026-01-19
> **Critical Enhancements**: **[v2.5.7] 7 Critical Enhancements - Phase 5 parallel workflow, enhanced time estimation, idealistic code generation, and director/time_validator handoff**

---

## Document Relationships

| Document | Purpose |
|----------|---------|
| **`00_ARCHITECTURE.md`** (this document) | **Defines architecture and Agent contracts** |
| **`01_SUMMARY.md`** | **[v2.5.7] Complete summary of all v2.5.7 changes** |
| **`02_director_file_reading_ban.md`** | **[v2.5.7 NEW] @director file reading prohibition protocol** |
| **`03_time_validator_strict_mode.md`** | **[v2.5.7 NEW] Enhanced @time_validator anti-lazy enforcement** |
| **`04_phase_5_parallel_workflow.md`** | **[v2.5.7 NEW] Phase 5 parallel workflow (5A→paper, 5B background)** |
| **`05_time_validator_enhanced_analysis.md`** | **[v2.5.7 NEW] @time_validator line-by-line code analysis** |
| **`06_code_translator_idealistic_mode.md`** | **[v2.5.7 NEW] @code_translator idealistic/perfectionist mode** |
| **`07_director_time_validator_handoff.md`** | **[v2.5.7 NEW] @director/@time_validator handoff protocol** |
| **`08_model_design_expectations.md`** | **[v2.5.7 NEW] Model design expectations validation protocol** |
| **`09_validator_advisor_brief_format.md`** | **[v2.5.7 NEW] @validator/@advisor concise evaluation format** |
| **`10_phase5b_error_monitoring.md`** | **[v2.5.7 NEW] Phase 5B error monitoring and resolution** |

Reading order: **01_SUMMARY.md** → **02-10 (detailed specs)** → **00_ARCHITECTURE.md**

> **CRITICAL v2.5.7 ENHANCEMENTS**: 10 critical enhancements including (1) @director file reading ban, (2) @time_validator strict mode, (3) Phase 5 parallel workflow, (4) Enhanced time estimation with line-by-line analysis, (5) @code_translator idealistic mode, (6) 48-hour escalation protocol, (7) Director/time_validator handoff logic, (8) Model design expectations validation with scoring tables, (9) @validator/@advisor brief format for efficient decision-making, (10) Phase 5B error monitoring with no-exit guarantee.

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| v2.5.5 | 2026-01-17 | 6 enhancements + @time_validator agent |
| v2.5.6 | 2026-01-18 | 4 fixes: Feedback files, Phase 5.5, Phase 0.5, Image naming |
| v2.5.7 | 2026-01-19 | 10 enhancements: Director file ban + Time validator strict mode + Phase 5 parallel + Enhanced analysis + Idealistic mode + 48h escalation + Handoff protocol + Model design expectations + Brief evaluation format + Phase 5B error monitoring |
| **v2.5.8** | **2026-01-19** | **1 enhancement: Emergency delegation protocol for critical convergence failures (fast response while maintaining @director coordination)** |
| **v2.5.9** | **2026-01-20** | **1 critical fix: Phase 4.5 re-validation protocol for code fixes during training (closes rework validation gap, prevents academic fraud through unauthorized simplification)** |

---

## v2.5.7 Critical Fixes

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

**Root Cause Identified**:
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

**Solution**: **@director File Reading Ban Protocol** (see `02_director_file_reading_ban.md`)

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

**Solution**: **@time_validator Strict Mode** (see `03_time_validator_strict_mode.md`)

**Key Rules**:

1. **@code_translator: Simplification = Academic Fraud**
   - Forbidden: "PyMC didn't work, so I used sklearn instead"
   - Forbidden: "Data structure mismatch, so I used available columns"
   - Required: " encountered error X, I consulted @director for guidance"
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

**Solution**: **Enhanced @time_validator Analysis Protocol** (see `05_time_validator_enhanced_analysis.md`)

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

**Solution**: **Phase 5 Parallel Workflow** (see `04_phase_5_parallel_workflow.md`)

**Key Changes**:
1. **Phase 5A → Paper writing proceeds immediately**:
   - Phase 5A (30 min): Quick training with `results_quick_*.csv`
   - Phase 6 (30 min): Generate figures from quick results
   - Phase 7 (2-3 hours): Write paper with quick results
   - Phase 5B (6-12 hours): Runs in parallel

2. **When Phase 5B completes**:
   - @visualizer regenerates figures with final results
   - @writer updates Results section with final results

**Per-Model Time Expectations (v2.5.7 UPDATED)**:
- **Old spec (v2.5.6)**: "4-6 hours" → **WRONG** (too optimistic)
- **New spec (v2.5.7)**: ">6 hours" → **CORRECT** (realistic)
  - Minimum: 6 hours
  - Typical: 8-12 hours
  - Maximum: 48 hours (with @director approval)

**Affected Phases**:
- **Phase 5A** (proceed to paper immediately)
- **Phase 5B** (runs in background)
- **Phase 6** (quick version first, final version later)
- **Phase 7** (draft with quick results, update with final)

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

**Solution**: **@code_translator Idealistic Mode** (see `06_code_translator_idealistic_mode.md`)

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

**Solution**: **48-Hour Escalation Protocol** (see `07_director_time_validator_handoff.md`)

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

**Solution**: **@director/@time_validator Handoff Protocol** (see `07_director_time_validator_handoff.md`)

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

**Affected Agents**:
- **@director** (MUST call with explicit instructions)
- **@time_validator** (MUST read all files, MUST provide clear recommendation)

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

**Solution**: **Model Design Expectations Framework** (see `08_model_design_expectations.md`)

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

**Affected Agents**:
- **@modeler** (MUST create design expectations table)
- **@time_validator** (MUST create comparison table, calculate score)
- **@director** (MUST enforce "one fail = all fail" rule)

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

**Solution**: **@validator/@advisor Brief Format Protocol** (see `09_validator_advisor_brief_format.md`)

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

**Affected Agents**:
- **@validator** (MUST use brief format in chat, detailed report to file)
- **@advisor** (MUST use brief format in chat, detailed report to file)
- **@director** (MUST read only brief format, apply pass/fail rule)
- **@researcher** (CAN read detailed reports when revision needed)

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

**Solution**: **Phase 5B Error Monitoring Protocol** (see `10_phase5b_error_monitoring.md`)

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

---

## Agent System (v2.5.7)

### Agent Overview (Updated v2.5.7)

| Agent | Responsibility | v2.5.7 Changes | Validation Participation |
|-------|---------------|----------------|------------------------|
| `reader` | Read PDF, extract requirements | (inherited v2.5.6) | MODEL, DATA, PAPER |
| `researcher` | Method suggestions | (inherited v2.5.6) | MODEL |
| `modeler` | Design mathematical models | **[v2.5.7] Must create design expectations table** | DATA, CODE, TRAINING |
| `feasibility_checker` | Feasibility check | (inherited v2.5.6) | MODEL, CODE |
| `data_engineer` | Data processing | (inherited v2.5.6) | - |
| `code_translator` | Code translation | **[v2.5.7] Simplification = Fraud, idealistic mode** | CODE, TRAINING |
| `model_trainer` | Model training | **[v2.5.7] Watch mode, no-exit during Phase 5B** | - |
| `validator` | Result validation | **[v2.5.7] Brief format + detailed report to file** | DATA, TRAINING, FINAL |
| `visualizer` | Generate figures | (inherited v2.5.6) | - |
| `writer` | Write papers | (inherited v2.5.6) | PAPER |
| `summarizer` | Create summary | - | - |
| `editor` | Polish documents | (inherited v2.5.6) | - |
| `advisor` | Quality assessment | **[v2.5.7] Brief format + detailed report to file** | MODEL, PAPER, FINAL |
| `time_validator` | Time validation, anti-lazy | **[v2.5.7] STRICT MODE + comparison tables** | Called after MODEL, CODE, TRAINING |
| **`director`** | **Team coordination** | **[v2.5.7] File reading BAN + simplified decision logic** | **N/A** |

> **Total**: 14 agents (same as v2.5.6, with enhanced behavioral constraints)

---

## Phase Overview (Updated v2.5.7)

| Phase | Name | Main Agent | Validation Gate | v2.5.7 Changes |
|-------|------|-----------|-----------------|----------------|
| **0** | Problem Understanding | reader, researcher | - | (inherited) |
| **0.5** | **Model Methodology Quality Gate** | **@advisor, @validator** | **✅ METHODOLOGY** | **[v2.5.7] @director file ban** |
| 1 | Model Design | modeler | ✅ MODEL (5 agents) | (inherited v2.5.6) |
| 1.5 | Time Estimate Validation | @time_validator | ✅ TIME_CHECK | **[v2.5.7] Enhanced analysis** |
| 2 | Feasibility Check | feasibility_checker | - | - |
| 3 | Data Processing | data_engineer | ✅ DATA (self) | - |
| 4 | Code Translation | code_translator | ✅ CODE (2 agents) | **[v2.5.7] Idealistic mode** |
| **4.5** | **Implementation Fidelity** | **@time_validator** | **✅ FIDELITY** | **[v2.5.7] STRICT MODE** |
| 5A | Quick Training | model_trainer | ✅ TRAINING | **[v2.5.7] → Paper immediately** |
| 5B | Full Training | model_trainer | ✅ TRAINING | **[v2.5.7] >6h, parallel w/ paper | [v2.5.8] Emergency protocol for critical convergence** |
| **5.5** | **Data Authenticity** | **@time_validator** | **✅ ANTI_FRAUD** | **[v2.5.7] Red line + analysis** |
| 6 | Visualization | visualizer | - | **[v2.5.7] Quick → final** |
| 6.5 | Visual Quality Gate | visualizer, Director | ✅ VISUAL | (inherited v2.5.6) |
| 7 | Paper Writing | writer | ✅ PAPER (4 agents) | **[v2.5.7] Draft w/ quick, update w/ final** |
| 7.5 | LaTeX Compilation Gate | writer, Director | ✅ LATEX | (inherited v2.5.6) |
| 8 | Summary | summarizer | ✅ SUMMARY (2 agents) | - |
| 9 | Polish | editor | ✅ FINAL (3 agents) | - |
| 9.5 | Editor Feedback Enforcement | Director, multiple agents | ✅ EDITOR | (inherited v2.5.6) |
| 10 | Final Review | advisor | - | **[v2.5.7] Must report file** |

---

## New v2.5.7 Protocols

### Protocol 1: @director File Reading Ban (NEW)

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

### Protocol 2: @time_validator Strict Mode (NEW)

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

## Inherited v2.5.6 Components

All v2.5.6 enhancements are fully inherited in v2.5.7:

### v2.5.6 Enhancements (Still Active)
1. **Feedback File Standardization** - Canonical path + naming enforced
2. **Enhanced Phase 5.5 Anti-Fraud** - Training skip detection, duration verification
3. **Phase 0.5 Model Quality Gate** - Methodology evaluation before implementation
4. **Image Naming Standards** - Fixed wildcards + standardized naming

### v2.5.5 Enhancements (Still Active)
1. **Strict Re-verification Standards** - 3+ sentences, specific evidence required
2. **All Agents Re-verify** - ALL relevant agents re-verify, not just rejecters
3. **Reader Mandatory Requirements** - Selective requirements are MANDATORY
4. **Modeler Time Pressure Protocol** - Must consult @director before simplifying
5. **Director Systematic Role** - Master checklist, priority hierarchy, decision matrices
6. **@time_validator Agent** - Time validation, lazy detection, anti-fraud

---

## Key Improvements Summary (v2.5.6 → v2.5.7)

| Issue | v2.5.6 | v2.5.7 | Impact |
|-------|--------|--------|--------|
| @director reads files → @advisor evaluates wrong | @director can read | @director BANNED from reading | Agent evaluations accurate |
| @code_translator simplifies → training 43min | @time_validator may miss | @time_validator STRICT MODE | Lazy implementation rejected |

---

## Testing Checklist (v2.5.7)

Before deploying v2.5.7, verify:

- [ ] @director file reading ban documented
- [ ] @director protocol specifies exact file paths
- [ ] Agents (@advisor, @validator) required to report file read
- [ ] @time_validator strict mode rules documented
- [ ] Training duration red line (30% threshold) specified
- [ ] Algorithm match verification specified
- [ ] @code_translator "simplification = fraud" warnings added
- [ ] **[v2.5.7] Model design expectations table template documented**
- [ ] **[v2.5.7] @time_validator comparison table format specified**
- [ ] **[v2.5.7] @modeler design expectations requirements documented**
- [ ] **[v2.5.7] @validator/@advisor brief format documented**
- [ ] **[v2.5.7] @director simplified decision logic documented**
- [ ] **[v2.5.7] Phase 5B watch mode protocol documented**
- [ ] **[v2.5.7] Error resolution workflow documented**
- [ ] All agent prompts updated with v2.5.7 changes
- [ ] Workspace synchronized with architecture
- [ ] Test cases for file reading ban
- [ ] Test cases for training duration rejection
- [ ] **[v2.5.7] Test cases for model design expectations validation**
- [ ] **[v2.5.7] Test cases for @validator/@advisor brief format**
- [ ] **[v2.5.7] Test cases for Phase 5B error monitoring**

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Complete

**For detailed specifications**, see:
- **01_SUMMARY.md** - Complete v2.5.7 summary
- **02_director_file_reading_ban.md** - @director file reading prohibition
- **03_time_validator_strict_mode.md** - @time_validator strict enforcement
- **04_phase_5_parallel_workflow.md** - Phase 5 parallel workflow
- **05_time_validator_enhanced_analysis.md** - @time_validator line-by-line analysis
- **06_code_translator_idealistic_mode.md** - @code_translator idealistic mode
- **07_director_time_validator_handoff.md** - @director/@time_validator handoff
- **08_model_design_expectations.md** - Model design expectations validation
- **09_validator_advisor_brief_format.md** - @validator/@advisor brief format
- **10_phase5b_error_monitoring.md** - Phase 5B error monitoring
