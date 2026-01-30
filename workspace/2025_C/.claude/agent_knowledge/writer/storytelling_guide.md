# O-Prize Visual Storytelling and Narrative Guide

This file contains comprehensive guidance for creating engaging, O-Prize-quality narratives.

## Core Principle

> **"O-Prize papers are flexible but present really eye-catching results."**
> **Balance: 100% math accuracy (technical rigor) + narrative engagement**

## NO Unprofessional Elements

**FORBIDDEN:**
- ❌ Emojis (🔍, 💡, etc.) - never used in academic papers
- ❌ Boxes/fboxes around text - decorative, not substantive
- ❌ Underlining - non-academic formatting
- ❌ ALL CAPS - unprofessional
- ❌ Multiple colors in one sentence - confusing
- ❌ Colored text within paragraphs - hard to read

## 1. Strategic Emphasis Paragraphs (3-5 per paper)

**Purpose:** Highlight counterintuitive findings using professional formatting

**Technique:** Use **bold title** + structured paragraph with specific numbers

**Template:**
```latex
\textbf{[Finding Title]}: [Specific number] [measurement] contradicts [expectation].
This [challenges theory/reveals pattern], suggesting [implication]. [Supporting evidence].
```

**Example** (from reference paper style):
```latex
\textbf{The 2.0 Medal Floor}: 79 countries (51\% of NOCs) are predicted to win exactly
2.0 medals with identical 95\% prediction intervals (1.0--3.0). This clustering reveals
an artificial ceiling where the model cannot distinguish between countries, contradicting
the expectation that predictions should vary continuously across nations.
```

**When to Use:**
- Counterintuitive results (e.g., "Host advantage: +1.5\% not 10-20\%")
- Policy recommendations (e.g., "Target middle-power nations for highest ROI")
- Methodological discoveries (e.g., "Convergence revealed identifiability constraints")
- Unexpected patterns (e.g., "Gold efficiency gap")
- **Avoid:** Routine results, obvious conclusions

## 2. Narrative Hooks (Compelling Openers)

**Purpose:** Grab attention with specific numbers and contrast/comparison

**Technique:** Specific numbers + challenge expectations + progressive revelation

**Template A: Surprising Fact Hook**
```latex
\section{Introduction}

The 2024 Paris Games featured Albania earning its first-ever Olympic medal, while
more than 60 countries remain medalless after decades of participation. This
dichotomy reveals that Olympic success is threshold-governed, not continuous.
```

**Template B: Problem Gap Hook**
```latex
\section{Introduction}

Conventional wisdom holds that [common belief]. However, [specific evidence] reveals
[contradiction], creating a critical gap: [gap description]. Our analysis addresses
this by [approach].
```

**Template C: Counterintuitive Result Hook**
```latex
\subsection{[Section Title]}

\textbf{The Unexpected Discovery}: [Specific number] [measurement units] contradicts the
expectation that [common assumption]. This [reveals pattern/challenges theory].
```

## 3. Strategic Emphasis Guidelines

**Principle:** Use emphasis strategically to guide reader attention, not decorate

**DO** (aligned with reference papers):
- Bold key phrases in emphasized paragraphs: `\textbf{The 2.0 Medal Floor}: ...`
- Emphasize critical metrics: "reduces response time by \textbf{67\%}"
- Use italics for emphasis sparingly: "\textit{contrary to established literature}"
- Color section titles if using colored headers (consistent throughout)

**DON'T** (unprofessional):
- NO emojis
- NO boxes/fboxes around text
- NO underlining
- NO ALL CAPS
- NO multiple colors in one sentence
- NO colored text within paragraphs

## 4. Section Transition Requirements

**Purpose:** Create narrative flow between sections

**Transition Templates:**
```latex
[End of Section 3]
Having established [key finding from Section 3], we now turn to [Section 4 topic].

[Alternative]
The [Section 3 finding] reveals [implication]. This motivates our investigation of
[Section 4 topic].

[Alternative]
While [Section 3] addressed [aspect], [Section 4] examines [related aspect].
```

**Quality Check:**
- [ ] Each section ends with transition sentence
- [ ] Transitions connect findings (not just "Next we address...")
- [ ] Narrative flow is coherent (story arc from problem → solution → insights)

## 5. "What We Discovered" Section Template

**Purpose:** Synthesize key insights at end of Results/Discussion

```latex
\subsection{What We Discovered}

Our analysis revealed six counterintuitive patterns that challenge conventional wisdom:

\begin{enumerate}
  \item \textbf{The "2.0 Medal Floor"}: 79 countries (51\% of NOCs) face identical baseline
  predictions, revealing an artificial ceiling breakable through targeted bronze conversion
  strategies.

  \item \textbf{Host Advantage Overrated}: USA receives only +1.9 medals (+1.5\%) from hosting
  in 2028, contradicting 10--20\% conventional wisdom.

  \item [Continue 4-6 more insights with specific numbers]
\end{enumerate}
```

## 6. Enhanced Caption Structure (4-Element Format)

**MANDATORY for all major figures/tables:**

1. **Observation**: What the data shows (specific numbers)
2. **Implication**: What it means (interpretation)
3. **Story**: How it challenges expectations (narrative element)
4. **Takeaway**: Actionable insight (so what?)

**Example:**
```latex
\caption{Small nations face 99.3\% relative uncertainty compared to 78.4\% for superpowers (Observation),
indicating that prediction error scales inversely with country size (Implication). This contradicts the
intuition that larger datasets should reduce relative uncertainty (Story), mandating flexible budgeting
approaches with tiered funding commitments rather than fixed medal targets (Takeaway). Key number: 99.3\%
CI width for 2.5-medal countries vs. 78.4\% for 38.2-medal countries.}
```

**Quality Check:**
- [ ] All 4 elements present (Observation, Implication, Story, Takeaway)
- [ ] At least one specific number included
- [ ] Caption tells a story (not just describes what's shown)

## 7. Model Section Openers (REQUIRED)

**Purpose:** Each model section opens with problem context, not just name

**Template:**
```latex
\subsection{Model [N]: [Model Name]}

[Specific data characteristic] creates [challenge]. [Standard approach] fails because
[limitation]. We employ [model name], which [key advantage].
```

**Example:**
```latex
\subsection{Model 1: Hurdle Model for Zero-Inflated Medal Counts}

Olympic medal data exhibits severe zero-inflation, with 60+ countries having never won
a medal while established powers win 50+ medals per Olympics. Standard Poisson models
fail because they assume a single stochastic process governs all medal counts. We employ
a hurdle model, which separates the probability of winning any medal from the count
distribution for medal-winning countries.
```

## 8. Methodology Evolution Integration

**When incorporating methodology_evolution_{i}.md insights:**

**Brevity Constraint:**
- Maximum 2 sentences per evolution item
- Focus on the insight, not the journey
- Omit if it doesn't directly support a conclusion

**Academic Framing Examples:**

❌ **Too narrative:**
"We initially struggled with R-hat values exceeding 1.3, but this revealed that parameter correlations were masking convergence. After much deliberation, we..."

✅ **Academic:**
"Sensitivity analysis revealed R-hat > 1.3 for β parameters, indicating parameter correlation. We addressed this through reparameterization (see Section 4.2), improving convergence efficiency by 40%."

**Integration Pattern:**
1. State the technical observation
2. Mention the refinement briefly
3. Report the quantitative improvement
4. Move to next point (no storytelling)

## 9. Academic Writing Style

**From Reference Papers:**

**DO:**
- Use active voice: "We develop..." (not "It was developed...")
- Be precise: "increases by 12.3%" (not "significantly increases")
- Quantify uncertainty: "95\% CI: [X, Y]"
- Use parallel structure in lists
- Vary sentence length (mix of short and long)

**DON'T:**
- Avoid weak verbs: "use", "show", "make" → Replace with "employ", "demonstrate", "construct"
- Avoid hedging: "might", "could possibly" → Use "suggests", "indicates" with evidence
- Avoid wordy phrases: "in order to" → "to"
- Avoid repetition of the same word within 3 sentences

## 10. O-Prize Quality Metrics

**Minimum Standards:**
- ✅ 3+ insight boxes highlighting key discoveries
- ✅ Enhanced captions (4-element) on all major figures/tables
- ✅ Compelling hook in introduction (specific numbers)
- ✅ "What We Discovered" section in Results/Discussion
- ✅ Abstract with ≥3 quantitative metrics
- ✅ 100% math accuracy (equations copied word-for-word)

**O-Prize Excellence Standards:**
- ✅ 5+ insight boxes strategically placed
- ✅ Narrative hooks in multiple sections (not just intro)
- ✅ Counterintuitive findings emphasized throughout
- ✅ Story arc: problem → solution → unexpected insights → implications
- ✅ Every major finding has "so what?" answered
- ✅ Paper would be memorable to judges 6 months later

## 11. Balance Verification (Critical)

**Technical Rigor Check:**
- [ ] All equations copied word-for-word from model_design.md
- [ ] All parameters defined with exact wording
- [ ] Mathematical notation is consistent throughout
- [ ] No summarizing or paraphrasing of math content

**Narrative Engagement Check:**
- [ ] Paper uses compelling hooks (not generic openings)
- [ ] Narrative flow is coherent (story arc present)
- [ ] Key findings emphasized with insight boxes
- [ ] Enhanced captions provide context, not just descriptions

**Brevity Check** (No Soap Opera):
- [ ] Methodology struggles limited to ≤2 sentences each
- [ ] No storytelling about "our journey" or "epiphany"
- [ ] Struggles presented as technical observations, not narratives
- [ ] Focus on insights, not process

**Synthesis Check** (Not Formulaic):
- [ ] Paper doesn't follow rigid predictable structure
- [ ] Narrative connections between sections (not just section headings)
- [ ] Insights synthesized from multiple sources (not rote copying)
- [ ] Paper would be memorable to judges (not blends in)
