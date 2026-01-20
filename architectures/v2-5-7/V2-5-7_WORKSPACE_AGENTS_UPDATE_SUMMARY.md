# v2.5.7 Workspace Agents Update Summary

> **Date**: 2026-01-19
> **Purpose**: Summary of all workspace agents updated for v2.5.7

---

## Overview

Successfully updated **4 critical agents** for v2.5.7 with enhanced protocols:
1. **modeler.md** - Design Expectations Table requirements
2. **code_translator.md** - Design expectations compliance + samples protection + "one fail all fail"
3. **advisor.md** - Brief format for efficient evaluation
4. **model_trainer.md** - Watch mode protocol for Phase 5B

---

## Agent 1: modeler.md ✅

### Update: Design Expectations Table (MANDATORY)

**Section Added**: "## Design Expectations Table (v2.5.7 MANDATORY)"

**Key Components**:

1. **Design Expectations Table Template**:
   - Category 1: Sampling Algorithm (Sampler, Tree Depth, etc.)
   - Category 2: MCMC Parameters (Chains, Tune, Draws, Total)
   - Category 3: Neural Network Parameters (Hidden layers, units, epochs)
   - Category 4: Ensemble Parameters (Base models, bootstrap samples)
   - Category 5: Features (Total count, specific features list)
   - Category 6: Computational Requirements (Training time, memory)

2. **Design Rationale (MANDATORY)**:
   - For each CRITICAL parameter, explain WHY it cannot be simplified
   - List alternatives considered and why they were rejected
   - Specify tolerance ranges

3. **Example Provided**: Complete table with NUTS sampler, 4 chains, 20000 draws, 15 features

**Why This Is Critical**:
```
Without Design Expectations Table:
- @code_translator may simplify (20000 → 1000 samples)
- @time_validator has no basis to detect simplification
- Result: Academic fraud through lazy implementation

With Design Expectations Table:
- @time_validator creates comparison table (Design vs Actual vs Tolerance vs Verdict)
- @director enforces "one fail = all fail" rule
- Result: Implementation matches design exactly
```

**Location in file**: After "## 4. Uncertainty Quantification Plan", before "## 5. Computational Requirements"

---

## Agent 2: code_translator.md ✅

### Update: Design Expectations Compliance + Samples Protection

**Section Added**: "## 🎯 Design Expectations Compliance (v2.5.7 MANDATORY)"

**Key Components**:

1. **Step 0: Read Design Expectations Table (MANDATORY)**
   - Must read design expectations BEFORE writing ANY code
   - Extract all parameters with Min/Max/Unit/Must Not Simplify flags

2. **🚨 SAMPLES PROTECTION - ABSOLUTE RED LINE**:
   ```
   ❌ FORBIDDEN (Academic Fraud):
     Draws: 20000 → 1000 (20× reduction)
     Tune: 2000 → 100 (20× reduction)
     Chains: 4 → 2 (50% reduction)

   ✅ REQUIRED (Exact Implementation):
     Draws: 20000 (within ±20%: 16000-24000)
     Tune: 2000 (exact, no tolerance)
     Chains: 4 (exact, no tolerance)
   ```

3. **Why Samples Cannot Be Simplified**:
   - **Posterior Convergence**: 20000 samples required for MCMC convergence
   - **Uncertainty Quantification**: 95% CI requires adequate posterior sampling
   - **Reproducibility**: 4 chains required for convergence verification

4. **Code Implementation Requirements**:
   ```python
   # ✅ CORRECT: Exact implementation
   trace = pm.sample(
       draws=20000,    # ← From design: 20000 (min 16000, max 24000)
       tune=2000,      # ← From design: 2000 (exact)
       chains=4,       # ← From design: 4 (exact)
       cores=4
   )

   # ❌ WRONG: Unauthorized simplification
   trace = pm.sample(
       draws=1000,    # ← 20× below minimum - AUTO-REJECT
       tune=100,      # ← 20× below design - AUTO-REJECT
       chains=2       # ← 50% below design - AUTO-REJECT
   )
   ```

5. **Feature Completeness Check**:
   ```python
   # ✅ CORRECT: Verify ALL designed features present
   missing = set(designed_features) - set(actual_features)
   if missing:
       raise ValueError(
           f"Missing {len(missing)} required features: {missing}\n"
           f"DO NOT use 'available columns' workaround."
       )
   ```

6. **One Fail = All Fail Rule**:
   ```python
   if ANY critical_param_FAIL:
       return "❌ REJECT"
   elif overall_score < 0.8:  # 80%
       return "❌ REJECT"
   else:
       return "✅ APPROVE"
   ```

7. **Summary Table Template**:
   | Parameter | Design | Min | Max | Your Code | Verdict |
   |-----------|--------|-----|-----|-----------|---------|
   | Sampler | NUTS | NUTS | NUTS | [your code] | ⬜ PASS / ❌ FAIL |
   | Chains | 4 | 4 | 4 | [your code] | ⬜ PASS / ❌ FAIL |
   | Tune | 2000 | 2000 | 2000 | [your code] | ⬜ PASS / ❌ FAIL |
   | Draws | 20000 | 16000 | 24000 | [your code] | ⬜ PASS / ❌ FAIL |
   | Features | 15 | 15 | 15 | [your code] | ⬜ PASS / ❌ FAIL |

**Location in file**: After "## 🧠 Self-Awareness & Environment Exploration", before "## 📝 Code Translation Workflow"

---

## Agent 3: advisor.md ✅

### Update: Brief Format for Efficient Evaluation

**Section Added**: "## 📊 Report Format (v2.5.7 BRIEF FORMAT - MANDATORY)"

**Key Components**:

1. **Brief Format for Chat Communication (MANDATORY)**:
   ```
   Grade: X.Y/10 | Verdict: ✅ PASS / ❌ FAIL
   Justification: [One sentence max]
   File verified: {file_path} ({N} lines)
   Detailed report written to: {output_path}
   ```

2. **Examples Provided**:
   - **✅ PASS**: Grade 9.8/10 with excellent methodology
   - **❌ FAIL**: Grade 4.5/10 lacking sophistication

3. **Detailed Report Format (Written to File)**:
   - File Information (path, lines, timestamp)
   - Grade + Verdict
   - Brief Evaluation (for @director)
   - Detailed Analysis (for @researcher reference)
   - Categories with Strengths/Weaknesses
   - O-Prize Comparison
   - Recommendations

4. **Communication Rules**:
   ```
   ❌ FORBIDDEN: Verbose evaluation in chat (10+ sentences)
   ✅ REQUIRED: Brief format (4 lines only)
   ```

5. **Report Quality Standards**:
   - **MUST**: Brief format in chat, detailed report to file, specific evidence, O-Prize comparison
   - **MUST NOT**: Verbose chat, vague feedback, ignore weaknesses, skip comparison

**Why This Matters**:
- @director decision time: **Minutes → Seconds**
- Decision becomes automatic (pass/fail check)
- Verbose analysis preserved in files for @researcher reference

**Location in file**: After "## 🚨 CRITICAL: File Read Verification", before "## 🆔 Phase Jump Capability"

---

## Agent 4: model_trainer.md ✅

### Update: Watch Mode Protocol for Phase 5B

**Section Added**: "## 🔄 Phase 5B Watch Mode Protocol (v2.5.7 MANDATORY)"

**Key Components**:

1. **Watch Mode Implementation**:
   ```python
   def watch_training(process, log_file, check_interval=60):
       """Watch training process for errors.
       CRITICAL: Keeps AI session active.
       DO NOT EXIT until training completes or error detected."""
   ```

2. **Step-by-Step Protocol**:
   - **Step 1**: Start training in background (capture PID)
   - **Step 2**: Enter watch mode (monitor log file every 60 seconds)
   - **Step 3**: Error detected → Report to @director immediately
   - **Step 4**: @director delegates fix → Resume training

3. **Error Patterns Monitored**:
   - Error, Exception, Traceback, Failed
   - AttributeError, KeyError, ValueError, TypeError, RuntimeError, MemoryError

4. **Status Reporting Protocol**:
   - **Regular Updates**: Every 30 minutes
   - **Completion Report**: Total time, samples, chains, convergence, errors resolved

5. **No-Exit Guarantee**:
   ```
   ❌ FORBIDDEN:
   @model_trainer: "Training started. Task complete."
   [AI session exits]

   ✅ REQUIRED:
   @model_trainer: "Training started (PID: 12345). Watch mode active."
   [AI session stays active, monitoring]
   ```

6. **Error Categories**:
   - **Category 1**: Implementation Errors → @code_translator fixes
   - **Category 2**: Data Errors → @data_engineer fixes
   - **Category 3**: Resource Errors → @code_translator optimizes
   - **Category 4**: Convergence Errors → @modeler consulted

7. **Timeout Protection**:
   - If >24 hours (above maximum), report to @director
   - Options: Continue monitoring, Investigate, Terminate and restart

**Why This Matters**:
- **Old behavior**: AI exits → Error occurs → Discovered hours later → Restart from scratch
- **New behavior**: AI monitors → Error detected → Fixed immediately → Resume from checkpoint

**Location in file**: After "## 🏆 Your Team Identity", before "## 🆔 Phase Jump Capability"

---

## Summary Table

| Agent | Update | Key Enhancement | Files Referenced |
|-------|--------|----------------|------------------|
| **modeler** | Design Expectations Table | Mandatory table for every model with parameters, tolerances, rationale | model_design.md |
| **code_translator** | Compliance + Samples Protection | Read design expectations, implement exactly, samples red line, one fail all fail | model_design.md, model_{i}.py |
| **advisor** | Brief Format | 4-line chat format + detailed file reports, O-Prize comparison | All files evaluated |
| **model_trainer** | Watch Mode | AI session stays active, monitor errors, report immediately, resume training | training_{i}.log |

---

## Critical Rules Summary

### Design Expectations (modeler + code_translator)

1. **@modeler MUST create** design expectations table for every model
2. **@code_translator MUST read** design expectations before coding
3. **@time_validator MUST create** comparison table (Design vs Actual vs Tolerance vs Verdict)
4. **@director MUST enforce** "one fail = all fail" rule

### Samples Protection (code_translator)

1. **Sampler**: NUTS (cannot simplify to Slice/Metropolis)
2. **Chains**: 4 (exact, no tolerance)
3. **Tune**: 2000 (exact, no tolerance)
4. **Draws**: 20000 (±20% tolerance: 16000-24000)
5. **Total**: 88000 (±20% tolerance: 70400-105600)

### Brief Format (advisor + validator)

1. **Chat format**: Grade + Verdict + Justification (1 sentence) + File verified + Detailed report path
2. **File reports**: Comprehensive analysis with evidence
3. **@director decision**: Automatic (both pass → approve, otherwise reject)

### Watch Mode (model_trainer)

1. **AI session**: MUST NOT exit during Phase 5B
2. **Monitoring**: Check log file every 60 seconds for errors
3. **Reporting**: Status every 30 minutes, errors immediately
4. **Error handling**: Report → Delegate fix → Resume training

---

## Verification Checklist

Before deploying v2.5.7, verify:

**Architecture Files**:
- [x] 08_model_design_expectations.md created
- [x] 09_validator_advisor_brief_format.md created
- [x] 10_phase5b_error_monitoring.md created
- [x] 00_ARCHITECTURE.md updated (Problem 8-10, Agent Overview, Testing)
- [x] V2-5-7_ENHANCEMENTS_SUMMARY.md created

**Workspace Agents**:
- [x] modeler.md updated (Design Expectations Table)
- [x] code_translator.md updated (Compliance + Samples Protection)
- [x] advisor.md updated (Brief Format)
- [x] model_trainer.md updated (Watch Mode)
- [x] validator.md updated (Brief Format) - previously done
- [x] time_validator.md updated (Strict Mode) - previously done

**Integration**:
- [x] CLAUDE.md references new enhancements
- [x] All agents consistent with v2.5.7 architecture
- [x] Protocol dependencies documented

---

## Testing Scenarios

### Scenario 1: Samples Simplification Detection

**Setup**:
- @modeler creates design: Draws=20000, Tune=2000, Chains=4
- @code_translator implements: Draws=1000, Tune=100, Chains=2

**Expected**:
```
@time_validator comparison table:
| Parameter | Design | Actual | Diff | Tolerance | Verdict |
| Draws | 20000 | 1000 | -95% | ±20% | ❌ FAIL |
| Tune | 2000 | 100 | -95% | Exact | ❌ FAIL |
| Chains | 4 | 2 | -50% | Exact | ❌ FAIL |

Overall Score: 0/3 (0%)
Final Verdict: ❌ AUTO-REJECT (All parameters simplified beyond tolerance)

@director: ❌ REJECT (Draws failed - one fail rule engaged)
```

### Scenario 2: Brief Format Evaluation

**Setup**:
- @director calls @advisor: "Evaluate output/docs/research_notes.md"

**Expected**:
```
@advisor (BRIEF FORMAT in chat):
Grade: 9.8/10 | Verdict: ✅ PASS
Justification: Excellent methodology with comprehensive approach.
File verified: output/docs/research_notes.md (843 lines)
Detailed report: output/docs/consultations/advisor_methodology.md

@dector (AUTOMATIC DECISION):
Both @validator (9.0/10 ✅ PASS) and @advisor (9.8/10 ✅ PASS) passed.
Average: 9.4/10 = EXCELLENT
Decision: ✅ APPROVE (proceed to next phase)

Time elapsed: ~5 seconds (vs 2+ minutes with verbose reports)
```

### Scenario 3: Watch Mode Error Detection

**Setup**:
- Phase 5B training starts
- After 2 hours, error occurs: `AttributeError: 'TensorVariable' object has no attribute 'logp'`

**Expected**:
```
@model_trainer (Watch Mode, 2 hours into training):
⚠️ ERROR DETECTED during Phase 5B training
Model: 2
PID: 12345
Error: AttributeError: 'TensorVariable' object has no attribute 'logp'
Line: 45
Timestamp: 2026-01-19 16:42:13

Awaiting @director guidance.

[AI session does NOT exit, awaiting @director response]

@director:
@code_translator: PyMC API error at line 45. Investigate and fix.

@code_translator:
Issue: PyMC v5 changed API from .logp to pm.logp()
Fix: log_prob = pm.logp(latent_var, observed)
Ready to apply.

@director:
@model_trainer: Fix applied. Resume training.

@model_trainer:
Restarting training with fixed code...
Old process killed: PID 12345
New process started: PID 12346
Entering watch mode...

[Training continues from checkpoint, not from scratch]
```

---

## Key Benefits

| Benefit | Before (v2.5.6) | After (v2.5.7) |
|---------|-----------------|----------------|
| **Samples protection** | Could simplify 20× without approval | Red line enforcement, auto-reject |
| **Design expectations** | No systematic validation | Comparison table + scoring |
| **Director decision time** | Minutes of deliberation | Automatic (seconds) |
| **Phase 5B errors** | Discovered hours later → Restart | Real-time detection → Resume |
| **Implementation fidelity** | Hit-or-miss verification | "One fail = all fail" enforcement |

---

## Files Modified

**Architecture**:
```
/home/jcheniu/MCM-Killer/architectures/v2-5-7/
├── 00_ARCHITECTURE.md (updated)
├── 08_model_design_expectations.md (new)
├── 09_validator_advisor_brief_format.md (new)
├── 10_phase5b_error_monitoring.md (new)
└── V2-5-7_ENHANCEMENTS_SUMMARY.md (new)
```

**Workspace Agents**:
```
/home/jcheniu/MCM-Killer/workspace/2025_C/.claude/agents/
├── modeler.md (updated: Design Expectations Table)
├── code_translator.md (updated: Compliance + Samples Protection)
├── advisor.md (updated: Brief Format)
├── model_trainer.md (updated: Watch Mode)
└── validator.md (updated: Brief Format - previously done)
```

---

**Document Version**: v2.5.7
**Last Updated**: 2026-01-19
**Status**: Complete
