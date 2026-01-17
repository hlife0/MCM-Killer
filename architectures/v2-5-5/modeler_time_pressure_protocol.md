# Modeler Time Pressure Protocol (v2.5.5)

> **Critical Enhancement**: v2.5.5
> **Purpose**: Prevent @modeler from unilaterally simplifying models due to time pressure
> **Status**: MANDATORY for @modeler and @director

---

## Problem Statement

**Issue Discovered**:
```
@modeler's workflow (v2.5.4):
1. Designs 3 models (Tier 1: Full complexity)
2. Estimates time: 2-6 hours
3. Starts implementing, works 20 minutes
4. Realizes: "This is taking too long"
5. Unilaterally decides: "I'll use Tier 2 (lightweight) instead"
6. Submits simplified models without consulting @director
7. Result: Models 50% simpler than designed
8. @director unaware until validation gate

Problems:
- @modeler abuses "degrade don't skip" principle
- No consultation before simplifying
- @director can't make informed decisions
- Token budget wasted
- Quality suffers
```

**Root Cause**:
- v2.5.0 introduced "Tier 2 lightweight" and "Tier 3 minimal" as options
- @modeler interprets this as permission to simplify when "feeling time pressure"
- No protocol for "ask @director before simplifying"
- @director unaware of time vs. quality trade-off until too late

**Impact**:
- Models simpler than necessary
- Wasted token budget (could have done better models)
- @director discovers quality issue too late
- Competition score reduced

---

## Solution: Consult @director Before Simplifying

### Core Principle

**@modeler Is NOT Allowed To Unilaterally Simplify Due To Time Pressure**

**When @modeler feels time pressure**:
1. STOP working
2. ASSESS situation honestly
3. CONSULT @director with specific proposal
4. WAIT for @director decision
5. PROCEED per @director's decision

---

## Protocol

### Step 1: Initial Time Estimation (Unchanged)

@modeler designs models and estimates time:

```markdown
## Model Design #1: Hierarchical Bayesian Model

### Complexity Analysis
**Time Complexity**: O(n × p × iterations)
- n = 1000 observations
- p = 15 parameters
- iterations = 10000 (HMC sampling)

**Estimated Runtime**:
- Model design: 1-2 hours
- Implementation: 2-3 hours
- Training: 4-6 hours
- **Total: 7-11 hours**

**Feasibility**: ✅ CONFIDENT (within 4-day competition timeframe)
```

### Step 2: @modeler Works on Design (Unchanged)

@modeler continues work, making progress.

### Step 3: Time Pressure Detection (NEW)

**When @modeler encounters time pressure**:

**Trigger Events** (any of these):
- Worked 2+ hours but < 30% progress on model design
- Realizes initial estimate was too optimistic
- Encounters unexpected complexity
- Competition deadline approaching faster than expected
- Token usage higher than anticipated

**@modeler's Internal Check**:
```
Am I feeling time pressure?
  ↓ YES
Do I want to simplify the model?
  ↓ YES
STOP! Do NOT simplify unilaterally.
  ↓
Follow Consultation Protocol →
```

### Step 4: Consultation Protocol (NEW)

**@modeler Creates Proposal**:

```markdown
# Time Pressure Consultation Request

## Current Situation
**Time Worked**: 2.5 hours
**Progress**: Model 1 partially designed (40%), Models 2-3 not started
**Original Estimate**: 7-11 hours total for all 3 models
**Concern**: At this pace, will need 15+ hours, exceeding available time

## Time Pressure Analysis
**Issue**: Model 1 more complex than anticipated
- HMC sampling requires careful prior specification
- Hierarchical structure needs validation
- Posterior predictive checks add time

**Root Cause**: Initial estimate didn't account for:
- Convergence diagnostics time
- Model comparison time
- Sensitivity analysis time

## Proposal Options

### Option A: Continue with Tier 1 (Full Models)
- **Models**: 3 full-complexity models as designed
- **Time Required**: 15-18 hours
- **Quality**: Highest
- **Risk**: May not finish in time

### Option B: Simplify to Tier 2 (Lightweight)
- **Models**: 3 models with reduced complexity
  - Model 1: Use frequentist instead of Bayesian
  - Model 2: Reduce ensemble from 5 to 3 models
  - Model 3: Skip cross-validation, use simple validation
- **Time Required**: 8-10 hours
- **Quality**: Good
- **Risk**: Some depth lost

### Option C: Rewind to Phase 0
- **Action**: Request @researcher to suggest simpler but still advanced methods
- **Time Required**: 1 hour consultation + 8-10 hours redesign = 9-11 hours total
- **Quality**: High (with better-suited methods)
- **Risk**: Delays progress but may find better approach

### Option D: Reduce Scope
- **Models**: 2 models instead of 3 (keep Models 1 and 2, drop Model 3)
- **Time Required**: 10-12 hours
- **Quality**: Good (fewer but thorough models)
- **Risk**: May miss some aspects of problem

## Request for Decision
Director, please advise which option to pursue.
I will wait for your decision before proceeding.
```

**@modeler Sends to @director**:
```
Director, I'm encountering time pressure on model design.

Consultation file: docs/consultation/{i}_modeler_director.md

I have assessed the situation and prepared 4 options.
I'm waiting for your decision before simplifying or proceeding.
```

### Step 5: @director's Decision Process (NEW)

**@director Calls @time_validator** (NEW in v2.5.5):
```
@time_validator:

Please review @modeler's time estimates.

Files:
- output/model/feasibility_{i}.md
- output/model/model_design_{i}.md

Assess:
1. Are original time estimates realistic?
2. Is @modeler's concern about time pressure valid?
3. Which option would you recommend?

Provide analysis to help me decide.
```

**@time_validator Returns Analysis**:
```markdown
## Time Validation Report

### Original Estimates Review
**Model 1 (Bayesian)**: Estimated 7-11 hours
  - My analysis: 8-12 hours ✅ Realistic
**Model 2 (Ensemble)**: Estimated 4-6 hours
  - My analysis: 5-7 hours ✅ Realistic
**Model 3 (Timeseries)**: Estimated 3-5 hours
  - My analysis: 3-5 hours ✅ Realistic

**Total**: 14-21 hours (original) vs 16-24 hours (my analysis)
**Conclusion**: Estimates were reasonable but slightly optimistic

### Time Pressure Assessment
@modeler's concern is VALID:
- Worked 2.5 hours, only 40% progress on Model 1
- At this pace: 2.5 / 0.4 = 6.25 hours per model
- Total: 6.25 × 3 = 18.75 hours
- This is within my estimate range (16-24 hours)

### Recommendation
**Option B (Tier 2 Lightweight)** is best:
- Reduces time to 8-10 hours ✅ Manageable
- Maintains quality: Frequentist still rigorous ✅
- Ensemble of 3 still shows sophistication ✅
- No rewind needed (saves time) ✅

**Option C (Rewind)** is second choice:
- May find better methods
- But costs 1 hour for consultation
- Risk: New methods also time-consuming

**Not Recommended**:
- Option A: Too risky (15-18 hours)
- Option D: Reduces scope too much
```

**@director Makes Decision**:
```
@modeler:

I've consulted @time_validator and reviewed your proposal.

**Decision**: Option B - Simplify to Tier 2 (Lightweight)

**Rationale**:
- @time_validator confirms your time pressure is valid
- Option B balances time and quality best
- Specific changes approved:
  ✅ Model 1: Frequentist instead of Bayesian (still rigorous)
  ✅ Model 2: Ensemble of 3 models (still sophisticated)
  ✅ Model 3: Simple validation (acceptable)

**Requirements**:
- You MUST still include all 6 required components
  (Mathematical Formulation, Variables, Assumptions, etc.)
- You MUST document in feasibility report:
  "Downgraded from Tier 1 to Tier 2 per @director approval
   due to time pressure. Maintained all required components."
- No further simplification without new consultation.

**Approved to proceed with Option B.**
```

### Step 6: @modeler Proceeds (With Approval)

```markdown
## Model Design #1: Zero-Inflated Negative Binomial Model

### Mathematical Formulation
[Frequentist ZINB formulation - still rigorous]

### Variables Table
[Complete table with all variables]

### Assumptions
[5-7 assumptions with justifications]

### Solution Method
[Maximum likelihood estimation - specific algorithm]

### Complexity Analysis
**Time**: O(n × p) per iteration, converges in 50-100 iterations
**Estimated runtime**: 2-3 hours ✅ (was 7-11 hours)

### Validation Approach
[Cross-validation, residual diagnostics, etc.]

**Note**: Per @director approval (Option B), this is a Tier 2
lightweight model. All required components included.
Downgraded from Bayesian HMC to frequentist MLE due to time
constraints, maintaining rigor while reducing complexity.
```

---

## Forbidden vs. Allowed Actions

### ❌ FORBIDDEN: Unilateral Simplification

```
@modeler: "I've worked 20 minutes, this is taking too long.
           I'll use simple linear regression instead."

Problems:
  - No consultation
  - No @director approval
  - Oversimplified (linear regression too simple)
  - No documentation
```

### ✅ ALLOWED: Consultation-Based Decision

```
@modeler: "I've worked 2 hours, progress slower than expected.
           I need to consult @director about options."
  → [Creates detailed proposal]
  → [Waits for @director decision]
  → [Proceeds with approved option]
  → [Documents approval]

Proper:
  - Consulted @director
  - Provided specific options
  - Waited for approval
  - Documented decision
```

---

## Tier System Clarification

### v2.5.5 Updated Tier System

**Tier Usage Protocol**:

**Tier 1: Full Model** (default)
- Use when: Normal circumstances
- **Requires**: No approval (this is standard)
- Complexity: Full methods with all extensions

**Tier 2: Lightweight Model** (degrade)
- Use when: Time pressure, **with @director approval**
- **Requires**: @director consultation and approval
- Complexity: Core method, reduced extensions
- **Documentation**: Must note "per @director approval"

**Tier 3: Minimal Model** (last resort)
- Use when: Extreme time pressure, **with @director approval**
- **Requires**: @director consultation + @time_validator analysis
- Complexity: Basic method with essential components only
- **Documentation**: Must note "per @director approval, extreme time pressure"

**Key Change**:
- v2.5.4: @modeler can choose Tier 2/3 unilaterally
- v2.5.5: @modeler MUST consult @director for Tier 2/3

---

## Quality Standards

### What Judges Expect

**Tier 1 (Full)**:
- "This team used advanced methods appropriate for the problem"
- Score potential: 9-10/10 for methodology

**Tier 2 (Lightweight, with approval)**:
- "This team used appropriate methods, some simplifications but justified"
- Score potential: 7-8/10 for methodology

**Tier 2 (Lightweight, WITHOUT approval)**:
- "This team oversimplified their models"
- Score potential: 5-6/10 for methodology
- **Problem**: No justification = looks lazy

**Tier 3 (Minimal, with approval + documentation)**:
- "This team faced time constraints but maintained rigor"
- Score potential: 6-7/10 for methodology

**Tier 3 (Minimal, WITHOUT approval)**:
- "This team's models are too simple"
- Score potential: 3-4/10 for methodology
- **Problem**: Unjustified simplification = poor quality

**Lesson**:
- Consultation + Documentation = Higher score even with simplification
- No consultation = Lower score, looks like lazy work

---

## Integration with @time_validator

### New Checkpoint (v2.5.5)

**After MODEL Validation Gate**:

```
Director calls @time_validator:
  "Validate @modeler's time estimates in feasibility_{i}.md"

@time_validator reviews:
  - Are estimates realistic?
  - Any discrepancies?

If @time_validator flags > 2x discrepancy:
  Director asks @modeler:
    "Your estimate was 2-6h, but @time_validator says 8-12h.
     Please explain."

@modeler either:
  - Revises estimate (if error)
  - Justifies difference (if has valid reason)
```

**Purpose**: Catch estimation errors early, not during implementation.

---

## Anti-Patterns to Avoid

❌ **WRONG**: Unilateral simplification
```
@modeler: "Time running out, using simple method instead."
```
✅ **CORRECT**: Consultation-based decision
```
@modeler: "Time pressure detected. Creating proposal for @director.
           Waiting for decision."
```

❌ **WRONG**: Vague time pressure
```
@modeler: "This is taking too long." (no specifics)
```
✅ **CORRECT**: Quantified assessment
```
@modeler: "Worked 2.5 hours, 40% progress.
           At this pace: 18.75 hours total (exceeds estimate)."
```

❌ **WRONG**: No documentation
```
@modeler: [Simplifies to Tier 2, doesn't mention why]
```
✅ **CORRECT**: Clear documentation
```
@modeler: "Downgraded to Tier 2 per @director approval (Option B).
           Reason: Time pressure, as documented in consultation {i}."
```

---

## Testing Checklist

Before implementing, verify:

- [ ] Consultation protocol specified
- [ ] Proposal template created
- [ ] @director decision process defined
- [ ] @time_validator integration specified
- [ ] Tier system updated (approval required)
- [ ] Quality standards defined
- [ ] Forbidden vs. allowed actions documented
- [ ] Anti-patterns documented

---

## Integration with v2.5.4 Protocols

### Updates to Modeler Anti-Simplification

**v2.5.4**:
```
@modeler may degrade to Tier 2/3 if time pressure
```

**v2.5.5**:
```
@modeler MUST consult @director before degrading to Tier 2/3
@director calls @time_validator for analysis
@modeler documents approval in feasibility report
```

### Updates to Director Oversight

**v2.5.4**:
```
Director checks token usage after @modeler submission
If suspiciously low → Query for completeness
```

**v2.5.5**:
```
Director calls @time_validator after MODEL validation gate
@time_validator validates time estimates
If discrepancy > 2x → Query @modeler

Additionally:
If @modeler requests consultation → Decision protocol
```

---

**Document Version**: v2.5.5
**Created**: 2026-01-17
**Status**: MANDATORY for @modeler and @director
