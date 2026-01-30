# Re-verification Strict Standards

This document defines the mandatory standards for re-verification after revisions are made.

---

## 🔄 CRITICAL: Re-verification Strict Standards

> [!CRITICAL]
> **When you participate in re-verification, you MUST provide detailed evidence**
>
> Lazy approvals like "Looks good, approved" are FORBIDDEN.
> You must provide specific evidence of checking.

---

## When You Re-verify Your Review

**Scenario**: You found issues, @modeler/@writer made revisions, now you re-verify.

---

## ❌ FORBIDDEN: Lazy Re-verification Approvals

```
❌ "Looks good, approved."
❌ "Fixed the issues, good to go."
❌ "All set, no problems found."
```

---

## ✅ REQUIRED: Evidence-Based Re-verification

**Template**:
```markdown
## Re-verification Verdict: ✅ APPROVED

### Issues Raised (Original)
1. [Issue 1 from previous review]
2. [Issue 2 from previous review]

### Verification Process
I re-verified the revisions:

**Issue 1**: [Describe issue]
- Checked: [Specific file, line numbers, or section]
- Evidence: [What I found]
- Status: ✅ RESOLVED / ❌ NEEDS MORE WORK

**Issue 2**: [Describe issue]
- Checked: [Specific file, line numbers, or section]
- Evidence: [What I found]
- Status: ✅ RESOLVED / ❌ NEEDS MORE WORK

### Regression Check
I also verified that:
- [ ] No new issues introduced
- [ ] Previously acceptable parts still meet standards
- [ ] No side effects from changes

### Conclusion
All issues resolved, no regressions detected. **APPROVED**.
```

---

## Minimum Requirements

Your re-verification verdict MUST:
- Contain at least **3 sentences**
- Cite **specific file locations** (file:line or section)
- Provide **specific evidence** (what you checked, what you found)
- Include a **regression check**
- State clearly **APPROVED** or **NEEDS_REVISION**
