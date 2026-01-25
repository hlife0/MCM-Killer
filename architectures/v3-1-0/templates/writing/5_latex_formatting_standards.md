# LaTeX Formatting Standards for O Award Quality

> **Purpose**: Ensure LaTeX output matches human-authored O Award paper quality
> **Applies to**: @writer, @editor, @judge_zero
> **Reference**: O Award papers in `workspace/2025_C/reference_papers/`

---

## Critical Issues to Avoid

These issues have been observed in current drafts and MUST be fixed:

### 1. Font Size Too Small

**Problem**: Using 10pt or 11pt font makes the paper hard to read and fails to match modern competition trends favoring readability.

**Fix**:
```latex
\documentclass[12pt]{article}  % Standard for modern MCM papers
```

**Standard**: Modern O Award papers use 12pt body text for better readability.

---

### 2. Non-Standard Margins

**Problem**: Default LaTeX margins are too wide, wasting valuable page space.

**Fix**:
```latex
\usepackage[margin=1in]{geometry}
% Or for tighter layout matching O Award papers:
\usepackage[top=1in, bottom=1in, left=0.75in, right=0.75in]{geometry}
```

---

### 3. Blank Pages

**Problem**: Blank pages appear due to improper float handling or page breaks.

**Fix**:
```latex
% Prevent blank pages from floats
\usepackage[section]{placeins}  % Keep floats in section
\renewcommand{\floatpagefraction}{0.8}  % Require 80% float content for float page
\renewcommand{\topfraction}{0.9}
\renewcommand{\bottomfraction}{0.9}
\renewcommand{\textfraction}{0.1}

% Force float placement
\usepackage{float}
\floatplacement{figure}{H}  % Use [H] for exact placement when needed
```

---

### 4. Line Spacing Issues

**Problem**: Double or 1.5 line spacing wastes space and looks unprofessional.

**Fix**:
```latex
\usepackage{setspace}
\singlespacing  % or \setstretch{1.1} for slightly more readable

% For specific sections needing different spacing:
\begin{spacing}{1.0}
  % content
\end{spacing}
```

---

### 5. Section Spacing Inconsistent

**Problem**: Irregular spacing between sections looks sloppy.

**Fix**:
```latex
\usepackage{titlesec}

% Consistent section formatting
\titlespacing*{\section}{0pt}{12pt plus 2pt minus 2pt}{6pt plus 2pt minus 2pt}
\titlespacing*{\subsection}{0pt}{10pt plus 2pt minus 2pt}{4pt plus 2pt minus 2pt}
\titlespacing*{\subsubsection}{0pt}{8pt plus 2pt minus 2pt}{4pt plus 2pt minus 2pt}
```

---

### 6. Figure Placement Problems

**Problem**: Figures float far from their first reference.

**Fix**:
```latex
% Option 1: Place figure immediately after paragraph referencing it
% Option 2: Use [htbp] with preference order
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\textwidth]{figure.pdf}
  \caption{...}
  \label{fig:example}
\end{figure}

% Option 3: Force placement (use sparingly)
\begin{figure}[H]
  ...
\end{figure}
```

---

### 7. Table Formatting Amateur

**Problem**: Tables use default LaTeX style with ugly lines.

**Fix**:
```latex
\usepackage{booktabs}  % Professional table rules

% WRONG:
\begin{tabular}{|c|c|c|}
\hline
A & B & C \\
\hline
1 & 2 & 3 \\
\hline
\end{tabular}

% RIGHT:
\begin{tabular}{ccc}
\toprule
A & B & C \\
\midrule
1 & 2 & 3 \\
\bottomrule
\end{tabular}
```

---

### 8. Equation Numbering Inconsistent

**Problem**: Some equations numbered, some not; inconsistent placement.

**Fix**:
```latex
% Number all displayed equations consistently
\begin{equation}
  E = mc^2
  \label{eq:einstein}
\end{equation}

% For multi-line equations, use align:
\begin{align}
  a &= b + c \label{eq:first} \\
  d &= e + f \label{eq:second}
\end{align}

% Only use equation* for truly auxiliary equations
```

---

### 9. Bibliography Formatting

**Problem**: Inconsistent citation style, missing information.

**Fix**:
```latex
\usepackage[numbers,sort&compress]{natbib}
% or
\usepackage[style=ieee]{biblatex}

% Ensure all references have:
% - Authors (all or et al. consistently)
% - Title
% - Publication venue
% - Year
% - DOI or URL where applicable
```

---

### 10. Header/Footer Issues

**Problem**: Missing team number, page numbers, or unprofessional headers.

**Fix**:
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\rhead{Team \#2512345}
\lhead{Page \thepage\ of \pageref{LastPage}}
\renewcommand{\headrulewidth}{0.4pt}

% For summary sheet:
\thispagestyle{empty}  % No header on first page
```

---

## Complete Professional Template

```latex
\documentclass[12pt]{article}

% ===== GEOMETRY =====
\usepackage[top=1in, bottom=1in, left=1in, right=1in]{geometry}

% ===== FONTS & ENCODING =====
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{times}  % Professional font matching O Award papers

% ===== SPACING =====
\usepackage{setspace}
\setstretch{1.08}  % Slightly more than single for readability

% ===== SECTIONS =====
\usepackage{titlesec}
\titlespacing*{\section}{0pt}{12pt plus 2pt minus 2pt}{6pt plus 2pt minus 2pt}
\titlespacing*{\subsection}{0pt}{10pt plus 2pt minus 2pt}{4pt plus 2pt minus 2pt}

% ===== FIGURES & TABLES =====
\usepackage{graphicx}
\usepackage{float}
\usepackage{booktabs}
\usepackage[section]{placeins}
\renewcommand{\floatpagefraction}{0.8}

% ===== MATH =====
\usepackage{amsmath,amssymb,amsfonts}

% ===== HEADERS =====
\usepackage{fancyhdr}
\usepackage{lastpage}
\pagestyle{fancy}
\fancyhf{}
\rhead{Team \#XXXXXXX}
\lhead{Page \thepage\ of \pageref{LastPage}}
\renewcommand{\headrulewidth}{0.4pt}

% ===== BIBLIOGRAPHY =====
\usepackage[numbers,sort&compress]{natbib}

% ===== HYPERLINKS =====
\usepackage[hidelinks]{hyperref}

\begin{document}

% Summary sheet (no header)
\thispagestyle{empty}
% ... summary content ...

\newpage
\setcounter{page}{1}

% Main content
\section{Introduction}
% ...

\end{document}
```

---

## Visual Quality Checklist

Before submission, compare your PDF against O Award reference papers:

### Page Layout
- [ ] Font size matches (12pt)?
- [ ] Margins appropriate (1 inch)?
- [ ] No blank pages?
- [ ] Page count efficient (no wasted space)?

### Text Formatting
- [ ] Single or 1.1x line spacing?
- [ ] Consistent section spacing?
- [ ] Professional font (Times or similar)?
- [ ] No orphaned lines or widows?

### Figures
- [ ] High resolution (300+ DPI)?
- [ ] Consistent style across all figures?
- [ ] Readable when printed?
- [ ] Placed near first reference?
- [ ] Caption includes interpretation (Protocol 15)?

### Tables
- [ ] Using booktabs style (no vertical lines)?
- [ ] Headers clearly distinguished?
- [ ] Units specified?
- [ ] Aligned appropriately (numbers decimal-aligned)?

### Equations
- [ ] Consistently numbered?
- [ ] Properly aligned (use align environment)?
- [ ] Variables defined when first used?

### Overall Polish
- [ ] Looks like human-authored paper?
- [ ] Would be comfortable in a journal?
- [ ] No amateur formatting tells?

---

## Common Amateur Tells (AVOID)

| Amateur Tell | Professional Fix |
|--------------|-----------------|
| 10-11pt font | Use 12pt |
| Narrow margins | 1 inch |
| Double spacing | Single or 1.1x |
| Vertical table lines | Use booktabs, no vertical lines |
| Figures at end | Place near first reference |
| "Figure 1 shows..." | "Figure 1 reveals..." (interpretation) |
| Inconsistent notation | Define all variables, be consistent |
| Missing page numbers | Always include page X of Y |
| Generic template look | Customize to look professional |

---

## Verification Process

1. **Compile PDF** and open alongside O Award reference paper
2. **Side-by-side comparison** of:
   - Font size (should look similar)
   - Margin width (should look similar)
   - Density of text per page (should look similar)
   - Figure quality and placement
   - Overall professional appearance
3. **Print test** (optional but recommended):
   - Does it look professional when printed?
   - Are figures readable?
   - Is text comfortable to read?

---

**Document Version**: 1.0
**Created**: 2026-01-25
**Status**: Active Template
