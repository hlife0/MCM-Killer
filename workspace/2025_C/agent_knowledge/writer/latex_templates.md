# LaTeX Templates for Writer Agent

**Agent**: writer
**Source**: Originally embedded in `.claude/agents/writer.md`
**Purpose**: LaTeX section templates for MCM paper writing

---

## Model Section Template (1.5-2.5 pages per model, NOT 2-3 pages)

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

**CRITICAL REQUIREMENTS**:
- Copy equations WORD-FOR-WORD from model_design.md
- Define ALL parameters inline (after equations), NOT in separate tables
- Each model: 1.5-2.5 pages TOTAL
- DO NOT summarize equations
- DO NOT create separate notation tables

---

## Results Section Template (4-5 pages)

### Section 1: Results Overview (1 paragraph)
- Summary of key findings
- Mention 2-3 most important metrics

### Section 2: Requirement-Specific Results (repeat for each requirement)

#### Title
**Context** (1-2 sentences): What this addresses

**Quantitative Findings** (2-3 paragraphs):
- Start with specific numbers
- Integrate tables/figures HERE (at first mention, not at end)
- Reference format: "Figure X shows Y (Observation), indicating Z (Implication)"

**Table/Figure Integration**:
Use [H] placement and relative path ../figures/

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

**Key Insights** (bulleted):
- Item 1: [Specific number] → [Implication]
- Item 2: [Specific number] → [Implication]

### Section 3: Unexpected Findings (1-2 paragraphs)
- What surprised you
- Why it matters

**CRITICAL REQUIREMENTS**:
- Every claim must have a number
- Place figures/tables at first mention using [H]
- Use relative path: ../figures/ (NOT figures/)
- All captions follow Observation → Implication format
- Each figure/table referenced in text BEFORE it appears

---

## Sensitivity Analysis Section (1-1.5 pages)

For each model (1-2 paragraphs per model):
- Parameter tested
- Range tested
- Results observed (with specific numbers)
- Implications for model robustness

---

## Strengths and Weaknesses Section (1-1.5 pages)

### Strengths (3-4 focused items)
\begin{itemize}
  \item \textbf{[Strength 1 Title]}\\
  [Explanation with specific example or number]
  \item \textbf{[Strength 2 Title]}\\
  [Explanation with specific example or number]
\end{itemize}

### Weaknesses (2-3 honest limitations with mitigations)
\begin{itemize}
  \item \textbf{[Weakness 1 Title]}\\
  [Explanation + mitigation strategy]
  \item \textbf{[Weakness 2 Title]}\\
  [Explanation + mitigation strategy]
\end{itemize}

**CRITICAL REQUIREMENTS**:
- Be specific (include numbers where possible)
- Avoid generic strengths ("our model is comprehensive")
- Be honest about weaknesses but provide mitigations
- Reference sensitivity analysis plans from model_design.md

---

## Discussion and Conclusions Section (2.5-3 pages)

### Synthesis and Conclusions (1 paragraph)
- Primary conclusions linked to specific results
- How results validate/challenge expectations

### Response to Each Requirement (1 paragraph each)
\subsubsection{Response to Requirement 1}
[Clear, direct answer with numerical result]

\subsubsection{Response to Requirement 2}
[Clear, direct answer with numerical result]

[Continue for all 6 requirements]

### Evaluation and Bias Analysis (1-1.5 paragraphs)
- Model effectiveness (accuracy, robustness, efficiency)
- Potential biases: Data, Model, Computational
- Mitigation strategies employed

### Implications (1 paragraph)
- Broader implications for the field
- Societal, economic, or environmental relevance
- Unexpected outcomes

### Final Recommendations (1 paragraph)
- Key takeaways
- Contribution to solving the problem
- Next steps for investigation

---

## Bibliography (1-1.5 pages)

\begin{thebibliography}{9}

\bibitem{ref1}
Author, A.~A., (Year). ``Title of Paper,'' \textit{Journal Name}, Vol.~X, No.~Y, pp.~123--145.

[Add 8-12 references for methods, data sources, etc.]

\end{thebibliography}

**CRITICAL REQUIREMENTS**:
- Each requirement response: Start with specific numerical answer
- Total length: 2.5-3 pages (not 4-5 pages)
- Include 8-12 references
- DO NOT repeat results (synthesize, don't restate)

---

## Figure and Table Template

### Figure Template
```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{../figures/figure_name.png}
\caption{[Key finding] (Observation), indicating [meaning/implication] (Implication).
Key metric: [specific number or percentage].}
\label{fig:short-name}
\end{figure}
```

### Table Template
```latex
\begin{table}[H]
\centering
\begin{tabular}{lcc}
\toprule
Column 1 & Column 2 & Column 3 \\
\midrule
Data 1 & 123.4 & 45.6 \\
\bottomrule
\end{tabular}
\caption{[Finding] (Observation), indicating [implication] (Implication).}
\label{tab:name}
\end{table}
```

---

## Critical Path Fix

Use `../figures/` (not `figures/`) because paper.tex is in `output/paper/` while figures are in `output/figures/`
