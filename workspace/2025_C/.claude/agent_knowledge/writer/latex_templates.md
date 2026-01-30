# LaTeX Section Templates for Writer Agent

This file contains detailed LaTeX templates for each major section of the MCM paper.

## Model Section Template (1.5-2.5 pages)

```latex
\subsection{Model X: [Name]}

\subsubsection{Model Overview}
[2-3 sentences: What it does, which requirement, why appropriate]

\subsubsection{Mathematical Formulation}
[Key equations in \begin{align}...\end{align}]
[Define parameters IMMEDIATELY after each equation:]
where:
\begin{itemize}
  \item $X$ is [definition]
  \item $Y$ denotes [definition]
\end{itemize}

\subsubsection{Solution Approach}
[4-6 steps maximum]
\begin{enumerate}
  \item [Step 1] - 1-2 sentence description
  \item [Step 2] - 1-2 sentence description
\end{enumerate}

\subsubsection{Model Justification}
[1 paragraph: Link to requirements, why better than alternatives, note limitations]
```

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

## Bibliography Template

```latex
\begin{thebibliography}{9}

\bibitem{ref1}
Author, A.~A., (Year). ``Title of Paper,'' \textit{Journal Name}, Vol.~X, No.~Y, pp.~123--145.

\bibitem{ref2}
Author, B.~B., and Author, C.~C., (Year). ``Title of Book,'' Publisher, City.

[Add references for methods, data sources, etc.]

\end{thebibliography}
```

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
