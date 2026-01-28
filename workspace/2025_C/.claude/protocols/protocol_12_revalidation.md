# Protocol 12: Phase 4.5 Re-Validation

> **Purpose**: Close rework validation gap to prevent academic fraud through unauthorized simplifications during training fixes
> **Owner**: @director (trigger) + @time_validator (re-validation)
> **Scope**: Phase 4.5 (Implementation Fidelity) - triggered after code fixes

## Problem Statement

Code fixes during training can introduce unauthorized simplifications:

```
Training error → @code_translator fixes "on the fly"
No validation → Simplifications slip through
Result: Academic fraud through hidden parameter changes
```

**Example scenario**:
```
@code_translator: "KeyError: 'Gold' → I'll use available columns"
[Training resumes with 5 features instead of 15]
@time_validator (Phase 5.5): "Training completed in 2 hours"
Expected: 12-18 hours → Actual: 2 hours → Fraud detected (too late)
```

## Steps

### Step 1: @code_translator MUST Provide CHANGES SUMMARY

**When @code_translator modifies code during training, MUST provide**:

```markdown
## CHANGES SUMMARY

- **File**: model_{i}.py
- **Original issue**: {description}
- **Fix applied**: {description}
- **Parameters changed**: {list}
- **Algorithm changed**: YES/NO
- **Features changed**: YES/NO
```

**Example** (Simple bug fix):
```markdown
## CHANGES SUMMARY

- **File**: model_1.py
- **Original issue**: TypeError: Feature name 'Gold' vs 'gold'
- **Fix applied**: Added feature name normalization
- **Parameters changed**: NONE
- **Algorithm changed**: NO
- **Features changed**: NO
```

**Example** (Parameter change - TRIGGERS RE-VALIDATION):
```markdown
## CHANGES SUMMARY

- **File**: model_1.py
- **Original issue**: Divergent transitions (15%)
- **Fix applied**: Increased target_accept from 0.80 to 0.95
- **Parameters changed**: target_accept (0.80→0.95), max_treedepth (10→15)
- **Algorithm changed**: NO
- **Features changed**: NO
```

**Example** (Feature change - TRIGGERS RE-VALIDATION):
```markdown
## CHANGES SUMMARY

- **File**: model_1.py
- **Original issue**: KeyError: 'Gold' not in data
- **Fix applied**: Used available columns instead
- **Parameters changed**: NONE
- **Algorithm changed**: NO
- **Features changed**: YES (15→5 features)
```

### Step 2: @director Analyzes CHANGES SUMMARY

**@director decision logic**:
```
IF parameter changes detected:
    Trigger re-validation
ELIF algorithm changed:
    Full Phase 1 rewind required
ELIF features changed:
    Trigger re-validation
ELIF simple bug fix (syntax, import):
    Resume training without re-validation
```

**Decision matrix**:

| Change Type | Action | Rationale |
|-------------|--------|-----------|
| Syntax error | Resume training | No logic change |
| Import error | Resume training | No logic change |
| Parameter change | Re-validation | May affect fidelity |
| Feature change | Re-validation | MAJOR - affects model |
| Algorithm change | **REWIND Phase 1** | FUNDAMENTAL - different model |

### Step 3: Conditional Re-Validation

**@director calls @time_validator** (when triggered):
```
"@time_validator: RE-VALIDATION REQUIRED

@code_translator has modified model_{i}.py during training:
Changes: {from CHANGES SUMMARY}

Please run Phase 4.5 validation on reworked code:
- Read CHANGES SUMMARY
- Compare to Design Expectations Table
- Check for unauthorized simplifications
- Verify parameters within tolerance
- Check features (all 15 present?)

Return: APPROVE/REJECT decision

DO NOT allow training to resume until validation complete."
```

**@time_validator re-validation process**:
```markdown
## Re-Validation Report: Model 1 (After Fix)

**Original issue**: Divergent transitions (15%)
**Fix applied**: Increased target_accept (0.80→0.95), max_treedepth (10→15)

### Parameter Check

| Parameter | Design | Pre-Fix | Post-Fix | Tolerance | Verdict |
|-----------|---------|---------|----------|-----------|---------|
| target_accept | 0.80 | 0.80 | 0.95 | ±0.15 | ✅ Within tolerance |
| max_treedepth | 10 | 10 | 15 | ±20% | ✅ Within tolerance |
| Algorithm | PyMC | PyMC | PyMC | Exact | ✅ No change |
| Features | 15 | 15 | 15 | Exact | ✅ All present |

### Simplification Check
- Algorithm changed: NO
- Features reduced: NO
- Iterations reduced: NO
- Library switched: NO

**Verdict**: APPROVED
**Training**: Authorized to resume
```

**Re-validation with FAIL**:
```markdown
## Re-Validation Report: Model 1 (After Fix)

**Original issue**: KeyError: 'Gold' not found
**Fix applied**: Used available columns instead

### Feature Check

| Parameter | Design | Pre-Fix | Post-Fix | Tolerance | Verdict |
|-----------|---------|---------|----------|-----------|---------|
| Features | 15 | 15 | 5 | Exact | ❌ FAIL |
| Algorithm | PyMC | PyMC | PyMC | Exact | ✅ No change |

### Simplification Check
- Algorithm changed: NO
- Features reduced: YES (15→5) ❌
- Iterations reduced: NO
- Library switched: NO

**Verdict**: REJECTED
**Reason**: Unauthorized feature reduction (Protocol 2 violation)
**Action**: Restore all 15 features or consult @modeler for design revision
**Training**: BLOCKED - Do NOT resume
```

## When Re-Validation Is NOT Required

**Simple bug fixes only**:
- Syntax errors (missing colon, wrong indentation)
- Import errors (typo in library name)
- Variable name typos
- File path corrections

**Criteria**:
```
IF (no parameter changes AND
    no algorithm changes AND
    no feature changes):
    RETURN "Resume training without re-validation"
```

**Example**:
```markdown
## CHANGES SUMMARY

- **File**: model_1.py
- **Original issue**: ImportError: 'pmc' instead of 'pymc'
- **Fix applied**: Corrected import statement
- **Parameters changed**: NONE
- **Algorithm changed**: NO
- **Features changed**: NO

@director: "Simple typo fix - re-validation not required
Training may resume immediately"
```

## Impact

**Without Protocol 12**:
- Fraud risk: 40% (simplifications slip through)
- Detection: Phase 5.5 (too late)
- Recovery: Full rework required

**With Protocol 12**:
- Fraud risk: <5% (all changes validated)
- Detection: Immediately after fix
- Recovery: Block before training resumes

**8× reduction in academic fraud risk**

## Enforcement

**@director checklist after every code fix**:
- [ ] CHANGES SUMMARY received from @code_translator?
- [ ] Changes analyzed for type (parameter/feature/algorithm)?
- [ ] Re-validation triggered if needed?
- [ ] @time_validator approval received before training resumed?

**@time_validator re-validation checklist**:
- [ ] Read CHANGES SUMMARY?
- [ ] Compared to Design Expectations Table?
- [ ] Checked all parameters?
- [ ] Verified all features present?
- [ ] No unauthorized simplifications?
- [ ] Provided clear APPROVE/REJECT verdict?

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
