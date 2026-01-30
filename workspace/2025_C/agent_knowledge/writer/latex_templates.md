# LaTeX Templates for Writer Agent

**Agent**: writer
**Source**: Originally embedded in `.claude/agents/writer.md`
**Purpose**: LaTeX section templates for MCM paper writing

---

## Model Section Template (REVISED - 2-3 pages per model)

### Structure Rules
- **Maximum 3 subheadings per model** (not 4-5)
- Use paragraphs instead of \subsubsection for minor divisions
- Combine "Model Overview" and "Model Justification" into introductory prose

### Template Structure

```latex
\subsection{Model [N]: [Name]}

% Opening paragraph: 4-6 sentences introducing what the model does, which requirement
% it addresses, why this approach is appropriate, and how it relates to prior work.
% Include 1-2 citations to foundational papers.

[Opening paragraph: Model [N] addresses [Requirement X] by [approach]. Following
\cite{Author1Year} and \cite{Author2Year}, we employ [method] because [justification].
This approach is particularly suited to [problem characteristic] while maintaining
[desirable property]. Unlike [alternative approach], our method [key advantage].]

% Mathematical formulation paragraph: Present key equations with inline context.
% Each equation should have 2-3 sentences before and 1-2 sentences after explaining
% the intuition. Define parameters inline, not in separate tables.

\subsubsection{Mathematical Formulation}

To capture [phenomenon], we define [key concept] as follows. The [relationship]
between [variables] can be expressed as:

\begin{align}
[Equation] \label{eq:name}
\end{align}
where $X$ represents [definition] and $Y$ denotes [definition]. This formulation
captures [key insight] while maintaining [property].

% Solution approach paragraph: Describe the solution approach as flowing prose,
% not as enumerated steps. Use "First,... Then,... Finally,..." transitions.

\subsubsection{Solution Approach}

We solve [problem] through a [N]-stage process. First, we [step 1], which establishes
[foundation]. Then, we apply [step 2] to obtain [intermediate result]. This is followed
by [step 3], where [key computation occurs]. Finally, we [step 4] to produce [final output].

% Closing paragraph: Discuss assumptions (as prose, not tables), limitations,
% and how this model connects to the next section.

We make several simplifying assumptions in this formulation. First, we assume [assumption 1]
because [justification]. This is reasonable given [evidence]. Second, [assumption 2], which
[rationale]. These assumptions allow [benefit] while accepting [limitation]. Having established
the [model name] framework, we now turn to [next model/section topic].
```

**CRITICAL**: NO ASSUMPTION TABLES. Write assumptions as prose paragraphs.

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

> [!CRITICAL]
> **Academic rigor requires 20-30 references, not 8-12.**

### Required Reference Categories

```latex
\begin{thebibliography}{30}  % Note: 30 not 9

% === METHODOLOGY REFERENCES (8-10) ===
% Include foundational papers for each method used
\bibitem{mcmc1}
Hoffman, M.~D., and Gelman, A., (2014). ``The No-U-Turn Sampler: Adaptively Setting Path Lengths in Hamiltonian Monte Carlo,'' \textit{Journal of Machine Learning Research}, Vol.~15, pp.~1593--1623.

\bibitem{pymc}
Salvatier, J., Wiecki, T.~V., and Fonnesbeck, C., (2016). ``Probabilistic Programming in Python using PyMC3,'' \textit{PeerJ Computer Science}, Vol.~2, e55.

\bibitem{bayes1}
Gelman, A., Carlin, J.~B., Stern, H.~S., et al., (2013). \textit{Bayesian Data Analysis}, 3rd ed., Chapman \& Hall/CRC.

\bibitem{rf1}
Breiman, L., (2001). ``Random Forests,'' \textit{Machine Learning}, Vol.~45, No.~1, pp.~5--32.

\bibitem{shap1}
Lundberg, S.~M., and Lee, S.~I., (2017). ``A Unified Approach to Interpreting Model Predictions,'' \textit{Advances in Neural Information Processing Systems}, Vol.~30, pp.~4765--4774.

% [Add 3-5 more methodology refs as needed]

% === DOMAIN-SPECIFIC REFERENCES (5-7) ===
% Prior work in the problem domain
\bibitem{domain1}
[Author], ([Year]). ``[Title],'' \textit{[Journal]}, [Volume], pp.~[pages].

% [Add comparable studies, prior analyses]

% === THEORETICAL FOUNDATIONS (3-5) ===
% Foundational theory papers
\bibitem{theory1}
[Foundational theory paper - Arrow, social choice, optimization theory, etc.]

% === DATA SOURCES (3-5) ===
% Primary and secondary data sources
\bibitem{data1}
[Primary data source documentation]

\bibitem{data2}
[Secondary data source]

\end{thebibliography}
```

### Citation Style Guide
- **Journal articles**: Author, A.~A., (Year). ``Title,'' \textit{Journal}, Vol.~X, No.~Y, pp.~XX--YY.
- **Books**: Author, A.~A., (Year). \textit{Title}, Edition, Publisher.
- **Conference papers**: Author, A.~A., (Year). ``Title,'' \textit{Proceedings of Conference}, pp.~XX--YY.
- **Websites/Reports**: Author/Organization, (Year). \textit{Title}. Retrieved from [URL].

### Citation Integration in Text
- Every method must cite foundational paper: "Following Gelman et al. \cite{bayes1}, we employ..."
- Every comparison must cite prior work: "Consistent with \cite{domain1} who found..."
- Every data source must be cited: "Data obtained from \cite{data1}..."

**CRITICAL REQUIREMENTS**:
- Minimum 20 references, target 25-30
- Each category must be represented
- All methods must cite foundational papers
- Inline citations integrated into prose (not just bibliography)
- Each requirement response: Start with specific numerical answer
- Total length: 2.5-3 pages (not 4-5 pages)
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
