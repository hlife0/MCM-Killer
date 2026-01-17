# LaTeX Compilation Gate Specification (v2.5.4)

> **Critical Addition**: v2.5.4
> **Purpose**: Prevent LaTeX compilation deadlocks in Phase 7
> **Status**: MANDATORY

---

## Problem Statement

**Issue Discovered**:
- @writer generates LaTeX source that fails to compile
- Director cannot detect compilation failure
- Workflow enters infinite loop trying to proceed
- No self-correction mechanism exists

**Impact**:
- Paper generation completely blocked
- Cannot proceed to @editor or @summarizer
- Entire competition workflow fails

---

## Solution: Phase 7.5 LaTeX Compilation Gate

### Gate Location

```
Phase 7 (@writer) → Phase 7.5 (LaTeX Compilation Gate) → Phase 8 (@summarizer)
                                          ↓ FAIL
                                    Rewind to Phase 7
```

### Gate Rules

**MANDATORY**: Every paper submission MUST pass this gate before proceeding.

**Exit Conditions**:
- ✅ **PASS**: LaTeX compiles successfully → Proceed to Phase 8
- ❌ **FAIL**: LaTeX fails to compile → Rewind to Phase 7

---

## Implementation Protocol

### Step 1: @writer Self-Verification

After @writer completes `paper_{i}.tex`:

**MANDATORY**: @writer MUST attempt compilation before submission.

```python
# @writer's self-verification steps
1. cd output/paper/
2. pdflatex paper_{i}.tex
3. Check exit code:
   - 0 → Success, proceed to submission
   - Non-zero → Compilation failed, fix errors
4. If failed, examine .log file for errors
5. Fix errors in .tex source
6. Retry compilation (max 3 attempts total)
```

**Error Types**:

| Error Type | Who Fixes | Example |
|-----------|-----------|---------|
| **Syntax errors** | @writer | Missing `}`, unclosed environment |
| **Table errors** | @writer | Misaligned `&` or `\\` |
| **Math errors** | @writer | Unescaped `_` or `^` in math mode |
| **File not found** | @writer | Missing image file, wrong path |
| **Package errors** | @feasibility_checker | Missing package, needs installation |
| **Font errors** | @feasibility_checker | Missing font, environment issue |

### Step 2: Director Verification

After @writer claims "paper complete":

```
Director MUST:
1. Check for compilation evidence
2. Verify .pdf file exists
3. If no .pdf → Request @writer to compile
4. If compilation fails → Initiate rewind or fix
```

**Verification Commands**:
```bash
# Check if PDF exists
ls -lh output/paper/paper_{i}.pdf

# Check if PDF is valid (non-zero size)
file output/paper/paper_{i}.pdf

# Check .log for errors
grep -i "error" output/paper/paper_{i}.log
```

### Step 3: Error Handling

**Scenario 1: Fixable Errors (@writer can fix)**

```
@writer attempts compilation
    ↓ FAIL
Director examines .log file
    ↓ Errors are syntax/table/math errors
Director sends back to @writer:
  "Compilation failed with errors:
   - Line 234: Missing }
   - Line 456: Misaligned table
   Please fix and recompile. Attempt X/3"
    ↓
@writer fixes errors
    ↓
Recompile
    ↓
Loop until PASS or 3 failures
```

**Scenario 2: Environment Errors (requires @feasibility_checker)**

```
@writer attempts compilation
    ↓ FAIL
Director examines .log file
    ↓ Errors are missing packages/fonts
Director sends to @feasibility_checker:
  "LaTeX compilation failed due to missing environment:
   - Package 'xcircle' not found
   - Font 'Times New Roman' not available
   Please resolve environment issues."
    ↓
@feasibility_checker installs/configures
    ↓
Send back to @writer to retry compilation
```

**Scenario 3: 3 Compilation Failures**

```
@writer fails 3 compilation attempts
    ↓
Director initiates REWIND to Phase 7:
  "LaTeX compilation failed 3 times.
   Rewinding to Phase 7.
   Please:
   1. Simplify complex LaTeX constructs
   2. Use standard packages only
   3. Verify all syntax before compilation attempt
   4. Consider breaking into smaller sections"
```

---

## Error Detection Checklist

@writer MUST check for these common errors before submission:

### Syntax Errors
- [ ] All `\begin{env}` have matching `\end{env}`
- [ ] All `{` have matching `}`
- [ ] All `[` have matching `]`
- [ ] No unclosed math modes (`$` or `\[`)

### Table Errors
- [ ] Correct number of `&` in each row
- [ ] `\\` at end of each row (except last)
- [ ] `\hline` correctly placed
- [ ] No `\multicolumn` syntax errors

### Math Errors
- [ ] All `_` and `^` in math mode only
- [ ] All `\frac{a}{b}` have both arguments
- [ ] No unescaped special characters in math

### File Errors
- [ ] All `\includegraphics` files exist
- [ ] All file paths correct (relative to .tex file)
- [ ] All image formats supported (.pdf, .png, .jpg)

### Package Errors
- [ ] All used packages are standard or available
- [ ] Package names spelled correctly
- [ ] No conflicting packages

---

## Compilation Output Format

@writer MUST report compilation status:

**SUCCESS**:
```
Director, LaTeX compilation SUCCESSFUL.

File: output/paper/paper_{i}.tex
PDF: output/paper/paper_{i}.pdf (pages: 27)
Log: output/paper/paper_{i}.log (no errors)

Compilation time: 45 seconds
Paper is ready for Phase 8.
```

**FAILURE** (with fixable errors):
```
Director, LaTeX compilation FAILED.

File: output/paper/paper_{i}.tex
Errors found:
  Line 234: Missing } (detected by pdflatex)
  Line 456: Misaligned table (detected by pdflatex)

Attempt: 1/3
Action: Fixing errors now...
```

**FAILURE** (after 3 attempts):
```
Director, LaTeX compilation FAILED after 3 attempts.

File: output/paper/paper_{i}.tex
Errors persist:
  - Complex table alignment (lines 400-450)
  - Nested environment issues (Section 5)

Recommendation: REWIND to Phase 7
Reason: Cannot resolve with simple fixes
Action required: Simplify LaTeX structure
```

---

## Director Decision Flow

```
@writer submits "paper complete"
    ↓
Director checks for PDF evidence
    ↓
  PDF exists and valid?
    ↓ YES                              ↓ NO
  Check .log for errors          Request @writer to compile
    ↓                                    ↓
  Errors in .log?                      Compilation succeeds?
    ↓ YES    ↓ NO                         ↓ YES       ↓ NO
Fixable?  Proceed to Phase 8         Proceed    Fixable?
  ↓ YES    ↓ NO                                    ↓ YES    ↓ NO
@writer   Rewind to                     @writer   Send to
fixes     Phase 7                      fixes     @feasibility_checker
```

---

## Timeout Handling

**Compilation Timeout**: 5 minutes

If compilation exceeds 5 minutes:
1. Kill pdflatex process
2. Examine .log for stuck point
3. Likely cause: Infinite loop in TikZ or complex table
4. Send back to @writer: "Compilation timeout. Simplify [stuck element]."

---

## Version Management

Each compilation attempt should be logged:

```markdown
# Compilation Log: paper_{i}.tex

| Attempt | Time | Exit Code | Errors | Status |
|---------|------|-----------|--------|--------|
| 1 | 14:23:10 | 1 | 3 syntax errors | FAILED |
| 2 | 14:25:30 | 0 | 0 | SUCCESS |
```

Save to: `output/paper/compilation_log_{i}.md`

---

## Integration with Workflow

### Update Phase 7 Description

**OLD (v2.5.3)**:
```
Phase 7: Paper Writing
  @writer writes paper.tex
  Output: paper.tex
  Next: Phase 8
```

**NEW (v2.5.4)**:
```
Phase 7: Paper Writing
  @writer writes paper.tex
  Output: paper.tex (draft)

Phase 7.5: LaTeX Compilation Gate (MANDATORY)
  @writer compiles paper.tex → paper.pdf
  Verification: PDF exists and valid
  Exit conditions:
    - PASS → Phase 8
    - FAIL (3x) → Rewind to Phase 7
  Output: paper.pdf
  Next: Phase 8
```

---

## Testing Checklist

Before implementing in real competition, test with:

- [ ] Paper with no errors (should pass)
- [ ] Paper with syntax errors (should detect and fix)
- [ ] Paper with missing images (should detect and fix)
- [ ] Paper with missing packages (should detect and escalate)
- [ ] Paper with complex tables (should handle or simplify)

---

## Anti-Patterns to Avoid

❌ **WRONG**: @writer submits .tex without compiling
✅ **CORRECT**: @writer MUST compile before submission

❌ **WRONG**: Director proceeds to Phase 8 without checking PDF
✅ **CORRECT**: Director MUST verify PDF exists

❌ **WRONG**: @writer gives up after 1 compilation failure
✅ **CORRECT**: @writer must attempt 3 times before requesting rewind

❌ **WRONG**: Director ignores compilation errors
✅ **CORRECT**: Director must enforce compilation gate

---

**Document Version**: v2.5.4
**Created**: 2026-01-16
**Status**: MANDATORY for Phase 7 → Phase 8 transition
