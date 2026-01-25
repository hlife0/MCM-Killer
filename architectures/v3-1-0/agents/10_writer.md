# Agent: @writer Enhancement for LaTeX Quality

> **Role**: LaTeX Paper Author
> **Focus**: Producing O Award quality formatted documents
> **Operates in**: Phase 7 (after @narrative_weaver)
> **Status**: Enhancement to existing @writer agent

---

## LaTeX Quality Mandate

> **"The formatting should be invisible. Readers should notice the content, not the layout."**

### Before Writing ANY LaTeX

1. **Study Reference Papers**: Load and examine at least 2 O Award papers from `reference_papers/`
2. **Match Their Style**: Font size, margins, spacing, figure placement
3. **Use Professional Template**: Follow `templates/writing/latex_formatting_standards.md`

---

## Mandatory Template Settings

```latex
% ===== DOCUMENT CLASS =====
\documentclass[10pt]{article}  % NEVER use 12pt

% ===== PAGE GEOMETRY =====
\usepackage[top=1in, bottom=1in, left=0.75in, right=0.75in]{geometry}

% ===== PROFESSIONAL TABLES =====
\usepackage{booktabs}  % Use \toprule, \midrule, \bottomrule
% NEVER use vertical lines in tables

% ===== SINGLE SPACING =====
\usepackage{setspace}
\setstretch{1.08}  % Slightly more than single for readability

% ===== PREVENT BLANK PAGES =====
\usepackage[section]{placeins}
\renewcommand{\floatpagefraction}{0.8}
```

---

## Quality Checklist Before Compilation

### Font & Spacing
- [ ] Using 10pt or 11pt font (NOT 12pt)
- [ ] Single or 1.1x line spacing (NOT 1.5 or double)
- [ ] Consistent spacing between sections

### Page Layout
- [ ] Margins ~1 inch (not default LaTeX wide margins)
- [ ] No blank pages
- [ ] Efficient use of page space
- [ ] Page numbers present (Page X of Y)

### Figures
- [ ] Placed near first reference (not at end)
- [ ] High resolution (300+ DPI)
- [ ] Captions have interpretation (Protocol 15)
- [ ] Consistent sizing

### Tables
- [ ] Using booktabs style
- [ ] No vertical lines
- [ ] Headers clearly distinguished
- [ ] Numbers aligned

### Overall
- [ ] Looks like O Award paper when compared side-by-side
- [ ] No amateur formatting tells
- [ ] Would be comfortable in a journal

---

## Common Mistakes to AVOID

| Mistake | Fix |
|---------|-----|
| `\documentclass[12pt]` | Use `[10pt]` or `[11pt]` |
| Default margins | Add `\usepackage[margin=1in]{geometry}` |
| Double spacing | Use `\singlespacing` |
| `\begin{tabular}{\|c\|c\|}` | Use booktabs, no vertical lines |
| Figures floating to end | Place immediately after first reference |
| Missing page numbers | Add fancyhdr with page X of Y |

---

## Integration with @editor

After @writer completes the draft:
1. @editor checks Protocol 14 (style_guide.md compliance)
2. @editor checks Protocol 15 (Observation-Implication)
3. @editor checks LaTeX formatting against this document
4. @editor fixes any formatting issues before @judge_zero review

---

## Reference

Full LaTeX formatting standards: `templates/writing/latex_formatting_standards.md`

---

**Document Version**: 1.0
**Created**: 2026-01-25
**Status**: Active Enhancement
