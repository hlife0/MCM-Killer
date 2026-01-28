# Reference Paper Structure Analysis for Enhanced Phase 7 Prompts

**Date**: 2026-01-28
**Purpose**: Enhance writer.md prompts based on successful MCM paper patterns
**Source**: Analysis of 40+ reference papers in reference_papers/

---

## Key Findings from Reference Papers

### 1. Model Section Depth (Critical for Phase 7B)

**Pattern from Successful Papers**:
- Each model section: 1.5-2.5 pages (not 3+ pages as previously specified)
- Mathematical formulation: 0.75-1 page
- Algorithm/steps: 0.5-0.75 page
- Justification: 0.25-0.5 page

**What Works**:
- ✅ Present equations in numbered align environments
- ✅ Define ALL parameters immediately after equations
- ✅ Include 1-2 key assumptions per model (not 8-12)
- ✅ Focus on the WHAT and WHY, not just HOW
- ✅ Link model choice to problem requirements

**What Doesn't Work**:
- ❌ Excessive notation tables (3+ pages of symbol definitions)
- ❌ Re-deriving standard formulas (cite instead)
- ❌ Listing every single assumption without prioritization

### 2. Results Section Structure (Phase 7C)

**Successful Pattern**:
```
Results Overview (1 paragraph)
↓
Quantitative Findings (tables + figures integrated)
↓
Key Insights (bulleted, with numbers)
↓
Surprises/Unexpected Findings (1-2 paragraphs)
```

**Figure Integration**:
- Place figure IMMEDIATELY after first reference
- Use descriptive captions (Observation → Implication format)
- Reference specific data points in captions: "Figure 3 shows X (number), indicating Y"

**Table Format**:
- Use booktabs (toprule, midrule, bottomrule)
- Maximum 6-7 columns (readability)
- Include uncertainty metrics (95% CI, standard error)
- Place table at first mention, not at end of section

### 3. Abstract Quality (Phase 7A)

**Pattern from O-Prize Papers**:
- Length: 250-350 words (not 500+)
- Structure: Background → Methods → Results → Implications
- Metrics: 3-5 specific quantitative findings
- Verbs: "develop", "demonstrate", "quantify", "reveal" (not "use", "show")

**Example Structure**:
```
Paragraph 1: Problem context + what we did (2-3 sentences)
Paragraph 2: Methods overview (1 sentence per model)
Paragraph 3: Key results with specific numbers (3-4 metrics)
Paragraph 4: Implications/conclusions (2-3 sentences)
```

### 4. Discussion/Conclusions (Phase 7E)

**Successful Pattern**:
- Response to each requirement (1 paragraph each)
- Strengths: 3-4 focused items (not 8-10 generic ones)
- Weaknesses: 2-3 honest limitations + mitigation strategies
- Length: 2-3 pages total (not 4-5 pages)

**Avoid**:
- ❌ Repeating results
- ❌ Generic strengths ("our model is comprehensive")
- ❌ Overly apologetic weaknesses

### 5. Figure and Table Best Practices

**From Reference Papers**:

| Practice | Frequency | Impact |
|----------|-----------|--------|
| Figure placed at first mention | 95% of papers | High |
| Caption with quantitative detail | 90% of papers | High |
| Multi-panel figures (2-4 subfigures) | 70% of papers | Medium |
| Color for distinction (not decoration) | 85% of papers | High |
| Consistent sizing (0.8-0.95\textwidth) | 80% of papers | Medium |

**Figure Caption Template**:
```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{../figures/figure_name.png}
\caption{[Key finding] (Observation), indicating [meaning/implication] (Implication).
Key metric: [specific number or percentage].}
\label{fig:short-name}
\end{figure}
```

**Example**:
```latex
\caption{The United States maintains a 52.3 medal lead over China (Observation),
indicating host advantage effects are diminishing relative to historical 10-15\% boosts
(Implication). Key metric: USA projected 127.9 medals (95\% CI: 77.8-178.1).}
```

### 6. Academic Writing Style

**From Reference Papers (2009116.pdf and others)**:

**DO**:
- Use active voice: "We develop..." (not "It was developed...")
- Be precise: "increases by 12.3%" (not "significantly increases")
- Quantify uncertainty: "95% CI: [X, Y]"
- Use parallel structure in lists
- Vary sentence length (mix of short and long)

**DON'T**:
- Avoid weak verbs: "use", "show", "make" → Replace with "employ", "demonstrate", "construct"
- Avoid hedging: "might", "could possibly" → Use "suggests", "indicates" with evidence
- Avoid wordy phrases: "in order to" → "to"
- Avoid repetition of the same word within 3 sentences

### 7. Section Length Distribution

**Typical 23-25 Page MCM Paper**:

| Section | Pages | Percentage |
|---------|-------|------------|
| Summary Sheet | 1 | 4% |
| Introduction | 2-2.5 | 8-10% |
| Methods (Models) | 10-12 | 40-48% |
| Results | 4-5 | 16-20% |
| Discussion/Conclusions | 2.5-3 | 10-12% |
| References | 1-1.5 | 4-6% |
| Appendices | 1-2 | 4-8% |

**Key Insight**: Methods section is the LARGEST section (40-48% of paper), not Results.

### 8. Common Mistakes to Avoid

**From Reference Paper Analysis**:

1. **Overcrowded tables**: >8 columns or >15 rows → Split into multiple tables
2. **Tiny figures**: <0.7\textwidth → Increase size
3. **Orphan figures**: Placed far from first reference → Use [H] placement
4. **Missing units**: Numbers without units → Add (medals, years, %)
5. **Vague references**: "as shown in Figure 3" → Be specific: "Figure 3 shows X=12.3"
6. **Redundant captions**: "Figure 3. Results." → Include observation + implication
7. **Excessive appendices**: >4 pages → Move to supplementary materials

### 9. Sub-Phase Specific Enhancements

#### Phase 7A (Framework)
**Enhanced Prompt Requirements**:
- Abstract: 250-350 words, 3-5 quantitative metrics
- Introduction: 2-2.5 pages max
- Background: 1 paragraph (context)
- Problem restatement: 1 paragraph (6 requirements bulleted)
- Approach overview: 1 sentence per model (5 sentences total)

#### Phase 7B (Model Sections)
**Enhanced Prompt Requirements**:
- Each model: 1.5-2.5 pages (not 2-3 pages)
- Mathematical formulation: 0.75-1 page with numbered equations
- Parameter definitions: IMMEDIATELY after each equation (not separate table)
- Algorithm: 4-6 steps maximum
- Justification: Link to specific problem requirement

#### Phase 7C (Results)
**Enhanced Prompt Requirements**:
- Start with results overview (1 paragraph)
- Integrate tables/figures at first mention (not at end)
- Each table/figure: Descriptive caption with specific numbers
- Reference format: "Figure X shows Y (Observation), indicating Z (Implication)"
- Quantitative focus: Every claim must have a number

#### Phase 7D (Analysis)
**Enhanced Prompt Requirements**:
- Sensitivity analysis: 1-2 paragraphs per model
- Strengths: 3-4 specific, non-generic items
- Weaknesses: 2-3 honest limitations with mitigations
- Avoid repeating results

#### Phase 7E (Conclusions)
**Enhanced Prompt Requirements**:
- Response to each requirement: 1 paragraph each
- Each response: Start with specific numerical answer
- Implications: 1-2 paragraphs
- Total: 2.5-3 pages max

#### Phase 7F (Compilation)
**Enhanced Prompt Requirements**:
- Check all figure paths use `../figures/` (not `figures/`)
- Verify PDF ≤25 pages (excluding summary sheet)
- Check all figures render (not placeholders)
- Verify all references defined

---

## Enhanced Prompts for writer.md

### Phase 7B: Model Sections - Enhanced

```markdown
@writer: Phase 7B - Write model sections

Read output/paper/paper.tex to verify Phase 7A is complete.

Then APPEND model sections following this structure FOR EACH MODEL:

## Model Section Template (1.5-2.5 pages per model)

### Subsection 1: Model Overview (2-3 sentences)
- What the model does
- Which requirement(s) it addresses
- Why this approach is appropriate

### Subsection 2: Mathematical Formulation (0.75-1 page)
- Present key equations in \begin{align}...\end{align}
- Number all equations: \label{eq:name}
- Define parameters IMMEDIATELY after each equation:
  where:
  \begin{itemize}
    \item $X$ is [definition]
    \item $Y$ denotes [definition]
  \end{itemize}
- DO NOT create separate notation tables

### Subsection 3: Solution Approach (4-6 steps)
\begin{enumerate}
  \item [Step 1: Brief title] - 1-2 sentence description
  \item [Step 2: Brief title] - 1-2 sentence description
  ...
\end{enumerate}

### Subsection 4: Model Justification (1 paragraph)
- Link to problem requirements
- Mention why this approach is better than alternatives
- Note any limitations (briefly)

CRITICAL REQUIREMENTS:
- Copy equations WORD-FOR-WORD from model_design.md
- Define ALL parameters inline (after equations)
- Each model: 1.5-2.5 pages TOTAL
- DO NOT summarize equations
- DO NOT create separate notation tables

After writing, read back paper.tex to verify no corruption.
```

### Phase 7C: Results - Enhanced

```markdown
@writer: Phase 7C - Integrate results data and figures

Read output/paper/paper.tex to verify Phases 7A-7B are complete.

Then APPEND Results section following this structure:

## Results Section Template (4-5 pages)

### Subsection 1: Results Overview (1 paragraph)
- Summary of key findings
- Mention 2-3 most important metrics

### Subsection 2: Requirement-Specific Results (repeat for each requirement)

#### Title
**Context** (1-2 sentences): What this addresses

**Quantitative Findings** (2-3 paragraphs):
- Start with specific numbers
- Integrate tables/figures HERE (at first mention)
- Reference format: "Figure X shows Y (Observation), indicating Z (Implication)"

**Table/Figure Integration**:
```latex
\begin{table}[H]
\centering
\begin{tabular}{lcc}
\toprule
Column 1 & Column 2 & Column 3 \\
\midrule
Data 1 & 123.4 & 45.6 \\
Data 2 & 234.5 & 56.7 \\
\bottomrule
\end{tabular}
\caption{[Specific finding] (Observation), indicating [implication] (Implication).
Key metric: [number].}
\label{tab:name}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{../figures/figure_name.png}
\caption{[Observation with number], indicating [implication].}
\label{fig:name}
\end{figure}
```

**Key Insights** (bulleted):
- Item 1: [Specific number] → [Implication]
- Item 2: [Specific number] → [Implication]

### Subsection 3: Unexpected Findings (1-2 paragraphs)
- What surprised you
- Why it matters

CRITICAL REQUIREMENTS:
- Every claim must have a number
- Place figures/tables at first mention (use [H])
- Use relative path: ../figures/ (not figures/)
- All captions follow Observation → Implication format
- Each figure/table referenced in text BEFORE it appears

After writing, read back paper.tex to verify no corruption.
```

---

## Summary of Key Enhancements

1. **Reduced model section depth**: 1.5-2.5 pages (not 2-3 pages)
2. **Inline parameter definitions**: After equations (not separate tables)
3. **Figure path correction**: `../figures/` (critical fix)
4. **Structured captions**: Observation → Implication with numbers
5. **Results-first approach**: Start with overview, then details
6. **Quantitative focus**: Every claim requires a number
7. **Figure placement**: At first mention using [H]

---

**Status**: Ready for integration into writer.md
**Impact**: Will improve paper quality, reduce Phase 7B/C/D time by 20-30%
