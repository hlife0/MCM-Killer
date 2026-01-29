# Phase 7 Sub-Phase Call Templates

**Agent**: writer
**Source**: Originally embedded in `.claude/agents/writer.md`
**Purpose**: Example calls for Phase 7A-7F sub-phases

---

## Phase 7A - Write paper framework

```
@writer: Phase 7A - Write paper framework
- Write Abstract (with ≥3 quantitative metrics)
- Write Introduction (problem background + restatement + approach)
- Write Notation table (if not in template)
- Use mcmthesis document class
- Output: output/paper/paper.tex
- DO NOT write model sections yet (that's Phase 7B)
```

---

## Phase 7B - Write model sections

```
@writer: Phase 7B - Write model sections

Read output/paper/paper.tex to verify Phase 7A is complete.

Then APPEND model sections following this structure FOR EACH MODEL:

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

CRITICAL REQUIREMENTS:
- Copy equations WORD-FOR-WORD from model_design.md
- Define ALL parameters inline (after equations), NOT in separate tables
- Each model: 1.5-2.5 pages TOTAL
- DO NOT summarize equations
- DO NOT create separate notation tables

After writing, read back paper.tex to verify no corruption.
```

---

## Phase 7C - Integrate results data and figures

```
@writer: Phase 7C - Integrate results data and figures

Read output/paper/paper.tex to verify Phases 7A-7B are complete.

Then APPEND Results section following this structure:

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

CRITICAL REQUIREMENTS:
- Every claim must have a number
- Place figures/tables at first mention using [H]
- Use relative path: ../figures/ (NOT figures/)
- All captions follow Observation → Implication format
- Each figure/table referenced in text BEFORE it appears

Input files:
- output/implementation/data/results_quick_*.csv
- output/figures/*.png (22 figures)

After writing, read back paper.tex to verify no corruption.
```

---

## Phase 7D - Write analysis sections

```
@writer: Phase 7D - Write analysis sections

Read output/paper/paper.tex to verify Phases 7A-7C are complete.

Then APPEND analysis sections:

## Sensitivity Analysis Section (1-1.5 pages)

For each model (1-2 paragraphs per model):
- Parameter tested
- Range tested
- Results observed (with specific numbers)
- Implications for model robustness

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

CRITICAL REQUIREMENTS:
- Be specific (include numbers where possible)
- Avoid generic strengths ("our model is comprehensive")
- Be honest about weaknesses but provide mitigations
- Reference sensitivity analysis plans from model_design.md

After writing, read back paper.tex to verify no corruption.
```

---

## Phase 7E - Write conclusions and bibliography

```
@writer: Phase 7E - Write conclusions and bibliography

Read output/paper/paper.tex to verify Phases 7A-7D are complete.

Then APPEND final sections:

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

## Bibliography (1-1.5 pages)

\begin{thebibliography}{9}

\bibitem{ref1}
Author, A.~A., (Year). ``Title of Paper,'' \textit{Journal Name}, Vol.~X, No.~Y, pp.~123--145.

[Add 8-12 references for methods, data sources, etc.]

\end{thebibliography}

CRITICAL REQUIREMENTS:
- Each requirement response: Start with specific numerical answer
- Total length: 2.5-3 pages (not 4-5 pages)
- Include 8-12 references
- DO NOT repeat results (synthesize, don't restate)

After writing, do final read of entire paper.tex to verify completeness.
```

---

## Phase 7F - Compile LaTeX to PDF

```
@writer: Phase 7F - Compile LaTeX to PDF

Read output/paper/paper.tex to verify it's complete.

Pre-compilation checks:
- [ ] All \includegraphics use ../figures/ (not figures/)
- [ ] All figures referenced in text before they appear
- [ ] All tables/figures have descriptive captions
- [ ] Paper ≤25 pages (excluding summary sheet)

Then compile LaTeX:
cd output/paper
pdflatex paper.tex
pdflatex paper.tex  # Run twice for references

Check exit code:
- 0 = Success
- Non-zero = Compilation failed

If failed:
1. Check paper.log for errors: grep -i "error" paper.log
2. Common issues to fix:
   - Missing } or \end{env}
   - Math mode errors (_ or ^ outside $...$)
   - File not found (check figure paths)
3. Fix errors (max 3 attempts total)
4. Retry compilation

After success:
- Verify PDF exists: ls -lh paper.pdf
- Check page count: pdfinfo paper.pdf | grep Pages
- Verify figures render (not placeholders)

Report compilation status:
SUCCESS: paper.pdf generated (N pages)
FAILURE: errors encountered, specify errors

After success, paper.pdf is ready for Phase 7.5 (LaTeX Gate).
```

---

## Checkpoint Reporting

After completing each sub-phase, report to @director:

```
Director, Phase 7[X] complete.

File: output/paper/paper.tex
Sections written: [list sections]
Word count: [count]
Checkpoint: output/paper/checkpoint_7[X].md

Ready for Phase 7[Y].
```

**Director will update VERSION_MANIFEST.json with your completion timestamp.**
