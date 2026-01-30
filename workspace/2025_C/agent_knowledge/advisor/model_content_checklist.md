# Model Content Completeness Checklist

This checklist ensures that model sections in the paper contain complete mathematical detail as specified in `model_design.md`.

---

## 🚨 CRITICAL: Model Content Completeness Check

> [!IMPORTANT]
> **Compare `model_design.md` with the paper.**
> **O-Prize papers have 2-3 pages of mathematical detail PER MODEL.**
> **If a model section is only 3-4 paragraphs, it's TOO SHORT.**

For EACH model in `model_design.md`:

- [ ] Model name matches exactly
- [ ] ALL assumptions are present (check count matches)
- [ ] Assumptions are NOT summarized (they're copied word-for-word)
- [ ] COMPLETE objective function/expression present
- [ ] ALL constraints present (if optimization)
- [ ] ALL variable definitions present
- [ ] Complete notation table present
- [ ] Solution algorithm described in detail (not "we used X" but HOW)
- [ ] Section length is adequate (2-3 pages, not 3 paragraphs)

---

## Common Issues to Watch For

| Issue | Symptom | Verdict |
|-------|---------|---------|
| Summarized assumptions | "We assumed X, Y, Z" (1 sentence) | REJECT |
| Missing equations | Text describes model but no LaTeX equations | REJECT |
| Incomplete formulation | Only objective function, no constraints | NEEDS REVISION |
| Short sections | Model section < 1 page | NEEDS REVISION |
| Rewritten equations | Equations look different from model_design.md | NEEDS REVISION |
| Missing notation | Variables used but not defined | NEEDS REVISION |

---

## How to Check

1. Read `model_design.md`
2. Read the corresponding model section in `paper.tex` or `paper.pdf`
3. Verify every mathematical element is present
4. Check that equations match (don't just check "something is there")
