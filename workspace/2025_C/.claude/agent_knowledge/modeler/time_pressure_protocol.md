# Time Pressure Protocol: Consult @director Before Simplifying

> [!CRITICAL] **You are NOT allowed to unilaterally simplify models due to time pressure.**
>
> **Old behavior**: Work 20 minutes, feel time pressure, unilaterally "simplify to Tier 2"
> **New behavior**: Feel time pressure → STOP → Create proposal → Consult @director → Wait for approval

## When You Feel Time Pressure

**Trigger Events** (any of these):
- Worked 2+ hours but < 30% progress on model design
- Realize initial time estimate was too optimistic
- Encounter unexpected complexity
- Competition deadline approaching faster than expected
- Token usage higher than anticipated

**What NOT to do**:
- ❌ Unilaterally simplify model (Tier 1 → Tier 2/3)
- ❌ Skip model components to save time
- ❌ Reduce complexity without asking
- ❌ Say "time pressure" and continue working

**What TO do** (protocol):

## Step 1: STOP Working
**DO NOT continue modeling. STOP immediately.**

## Step 2: Assess Situation Honestly
Evaluate:
- Time worked: [X hours]
- Progress: [X% complete]
- Original estimate: [X hours]
- New estimate at current pace: [X hours]
- Issue: [describe what's causing delay]

## Step 3: Create Proposal for @director
Create consultation request:

```markdown
# Time Pressure Consultation Request

## Current Situation
**Time Worked**: [X hours]
**Progress**: Model 1 partially designed ([X]%), Models 2-3 not started
**Original Estimate**: [X-Y hours total for all models]
**Concern**: At this pace, will need [Z] hours, exceeding available time

## Time Pressure Analysis
**Issue**: [Describe specific issue]
- Model 1 more complex than anticipated
- Unexpected [specific complexity]
- [Other reason]

## Proposal Options

### Option A: Continue with Tier 1 (Full Models)
- **Models**: [number] full-complexity models as designed
- **Time Required**: [X-Y hours]
- **Quality**: Highest
- **Risk**: May not finish in time

### Option B: Simplify to Tier 2 (Lightweight)
- **Models**: [number] models with reduced complexity
-   - [Specific changes]
- **Time Required**: [X-Y hours]
- **Quality**: Good
- **Risk**: Some depth lost

### Option C: Rewind to Phase 0
- **Action**: Request @researcher to suggest simpler but still advanced methods
- **Time Required**: [X hours]
- **Quality**: High (with better-suited methods)

### Option D: Reduce Scope
- **Models**: [number] models instead of [number]
- **Time Required**: [X-Y hours]
- **Quality**: Good (fewer but thorough models)

## Request for Decision
Director, please advise which option to pursue.
I will wait for your decision before proceeding.
```

## Step 4: Send to @director and WAIT
```
Director, I'm encountering time pressure on model design.

Consultation file: output/docs/consultation/{i}_modeler_director.md

I have assessed the situation and prepared [X] options.
I'm waiting for your decision before simplifying or proceeding.
```

**DO NOT proceed with ANY modeling until @director responds.**

## Step 5: Follow @director's Decision

**If @director approves Option A (Tier 1)**:
- Continue with full models
- Update feasibility report if needed

**If @director approves Option B (Tier 2)**:
- Simplify as specified in approval
- **MUST document in feasibility report**:
  ```markdown
  **Note**: Per @director approval (Option B), this is a Tier 2
  lightweight model. All required components included.
  Downgraded from [Tier 1 method] to [Tier 2 method] due to
  time constraints, maintaining rigor while reducing complexity.
  ```

**If @director approves Option C (Rewind)**:
- Stop current work
- Wait for rewind to Phase 0

**If @director approves Option D (Reduce Scope)**:
- Drop specified models
- Focus on remaining models with full Tier 1 quality

## Tier System (Updated)

**Tier 1: Full Model** (default, no approval needed)
- Standard parameter settings
- Full sampling/iterations
- Expected time: Depends on problem

**Tier 2: Lightweight Model** (requires @director approval)
- Reduce sampling to 50%
- Lower convergence standards
- Expected time: 1-2 hours
- **MUST**: Still have all 6 required components
- **MUST**: Document approval

**Tier 3: Minimal Model** (requires @director approval + @time_validator analysis)
- Quick prototype algorithms
- Minimum necessary iterations
- Expected time: 10-30 minutes
- **MUST**: Still have all 6 required components
- **MUST**: Document approval and limitations

## Forbidden vs Allowed

**❌ FORBIDDEN**:
- Unilateral simplification without consultation
- Saying "time pressure" and continuing to simplify
- Reducing quality to save time without asking

**✅ ALLOWED**:
- Consulting @director when feeling time pressure
- Proposing specific options with trade-offs
- Waiting for @director decision
- Following @director's approved plan

## Quality Impact

**With consultation + approval**:
- Tier 2 with approval → Score: 7-8/10 (justified simplification)
- Tier 3 with approval → Score: 6-7/10 (documented constraints)

**Without consultation (unilateral)**:
- Tier 2 → Score: 5-6/10 (looks lazy)
- Tier 3 → Score: 3-4/10 (unjustified oversimplification)

**Lesson**: Consultation + Documentation = Higher score even with simplification
