# LaTeX Section Templates for Writer Agent

This file contains detailed LaTeX templates for each major section of the MCM paper.

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

## Results Section Template (4-5 pages)

```latex
\section{Results}
\label{sec:results}

\subsection{Implementation Details}
[Programming language, software, computational resources]

\subsection{Model 1 Results}

[Present numerical results from results_summary.md]
[Use tables and figures]

\begin{table}[H]
\centering
\begin{tabular}{lcc}
\toprule
Scenario & Metric 1 & Metric 2 \\
\midrule
Case A   & 123.45  & 67.89   \\
Case B   & 234.56  & 78.90   \\
\bottomrule
\end{tabular}
\caption{[Observation with at least one number], indicating [implication/meaning].}
\label{tab:results1}
\end{table}

\begin{figure}[H]
\centering
\includegraphics[width=0.8\textwidth]{../figures/result1.png}
\caption{[Observation with at least one number], indicating [implication/meaning].}
\label{fig:result1}
\end{figure}

[Continue for all models]
```

## Sensitivity Analysis Template

```latex
\section{Sensitivity Analysis}
\label{sec:sensitivity}

\subsection{Model 1 Sensitivity}
[Parameter tested, range tested, results observed]

[Include figures showing sensitivity curves]

\subsection{Model 2 Sensitivity}
[Continue for each model]
```

## Strengths/Weaknesses Template

```latex
\section{Strengths and Weaknesses}
\label{sec:strengths}

\subsection{Strengths}
\begin{itemize}
  \item \textbf{[Strength 1 Title]}\\
  [Explanation]
  \item \textbf{[Strength 2 Title]}\\
  [Explanation]
\end{itemize}

\subsection{Weaknesses}
\begin{itemize}
  \item \textbf{[Weakness 1 Title]}\\
  [Explanation and potential improvements]
  \item \textbf{[Weakness 2 Title]}\\
  [Explanation and potential improvements]
\end{itemize}
```

## Discussion and Conclusions Template

```latex
\section{Discussion and Conclusions}
\label{sec:discussion}

\subsection{Synthesis and Conclusions}
[Begin by clearly stating primary conclusions linked to specific results. Discuss how these validate/challenge expectations.]

\subsubsection{Response to Requirement 1}
[Clear, direct answer with numerical result.]

\subsubsection{Response to Requirement 2}
[Clear, direct answer with numerical result.]

\subsection{Evaluation and Bias Analysis}
[Evaluate effectiveness and reliability of models (accuracy, robustness, efficiency). Address limitations.]

\paragraph{Bias Analysis}
[Analyze potential biases: Data (representation), Model (assumptions), Computational. Discuss strategies to mitigate identified biases.]

\subsection{Implications}
[Explore broader implications for the field. Discuss societal, economic, or environmental relevance. Identify unexpected outcomes.]

\subsection{Final Recommendations}
[Summarize key takeaways. Emphasize contribution to solving the problem. Outline next steps for investigation.]
```

## Bibliography Template (ENHANCED - 20-30 references)

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

## Figure and Table Templates

### Figure Template (MANDATORY 4-element caption)

```latex
\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{../figures/figure_name.png}
\caption{[Key finding] (Observation), indicating [meaning/implication] (Implication).
This [challenges expectations/reveals pattern] (Story), suggesting [actionable insight] (Takeaway).
Key metric: [specific number or percentage].}
\label{fig:short-name}
\end{figure}
```

### Table Template (booktabs style)

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

## Complete Paper Template Structure

See writer.md lines 1184-1537 for the full template starting with:
```latex
\documentclass{mcmthesis}
```
