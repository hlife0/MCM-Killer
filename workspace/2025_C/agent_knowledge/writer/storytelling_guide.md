# O-Prize Visual Storytelling Guide

**Agent**: writer
**Source**: Originally embedded in `.claude/agents/writer.md`
**Purpose**: O-Prize visual storytelling elements and quality metrics

---

## O-Prize Visual Storytelling Elements

> [!CRITICAL]
> **O-Prize papers are "flexible but present really eye-catching results."**
> **Reference papers use professional techniques: strategic bolding, data-driven storytelling, and complete caption structures.**
>
> **NO EMOJIS, NO BOXES, NO DECORATIVE ELEMENTS** - These are unprofessional.

### 1. Strategic Emphasis Paragraphs (3-5 per paper)

**Purpose**: Highlight counterintuitive findings using professional formatting

**Technique**: Use **bold title** + structured paragraph with specific numbers

**Template**:
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

**When to Use**:
- Counterintuitive results (e.g., "Host advantage: +1.5\% not 10-20\%")
- Policy recommendations (e.g., "Target middle-power nations for highest ROI")
- Methodological discoveries (e.g., "Convergence revealed identifiability constraints")
- Unexpected patterns (e.g., "Gold efficiency gap")
- Avoid: Routine results, obvious conclusions

**Full Templates**: See `knowledge_library/templates/writing/insight_box_templates.md`

---

### 2. Narrative Hooks (Compelling Openers)

**Purpose**: Grab attention with specific numbers and contrast/comparison

**Technique**: Specific numbers + challenge expectations + progressive revelation

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

---

### 3. Strategic Emphasis Guidelines

**Principle**: Use emphasis strategically to guide reader attention, not decorate

**DO** (aligned with reference papers):
- Bold key phrases in emphasized paragraphs: `\textbf{The 2.0 Medal Floor}: ...`
- Emphasize critical metrics: "reduces response time by \textbf{67\%}"
- Use italics for emphasis sparingly: "\textit{contrary to established literature}"
- Color section titles if using colored headers (consistent throughout)

**DON'T** (unprofessional):
- NO emojis (🔍, 💡, etc.) - these are never used in academic papers
- NO boxes/fboxes around text - decorative, not substantive
- NO underlining - non-academic formatting
- NO ALL CAPS - unprofessional
- NO multiple colors in one sentence - confusing
- NO colored text within paragraphs - hard to read

---

### 4. Section Transition Requirements

**Purpose**: Create narrative flow between sections

**Transition Templates**:
```latex
[End of Section 3]
Having established [key finding from Section 3], we now turn to [Section 4 topic]. This [connection/motivation] is critical because [reason].

[Alternative]
The [Section 3 finding] reveals [implication]. This motivates our investigation of
[Section 4 topic].

[Alternative]
While [Section 3] addressed [aspect], [Section 4] examines [related aspect].
```

---

### 5. "What We Discovered" Section Template

**Purpose**: Synthesize key insights at end of Results/Discussion

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

---

## O-Prize Quality Metrics

> [!CRITICAL]
> **Before marking paper as complete, verify these O-Prize quality standards.**
> **O-Prize papers balance technical rigor (100% math accuracy) + narrative engagement.**

### Narrative Engagement Checklist

**Opening Hook**:
- [ ] Introduction starts with specific numbers (not generic statements)
- [ ] First paragraph includes at least 2 quantitative facts
- [ ] Hook challenges conventional wisdom or presents surprising fact
- [ ] Example: "The 2024 Paris Games featured Albania earning its first-ever Olympic medal, while more than 60 countries remain medalless after decades of participation."

**Section Transitions**:
- [ ] Each section ends with transition to next section
- [ ] Transitions connect findings (not just "Next we address...")
- [ ] Narrative flow is coherent (story arc from problem → solution → insights)

**Strategic Emphasis Paragraphs** (3-5 per paper):
- [ ] At least 3 emphasized paragraphs highlight key discoveries
- [ ] Each emphasized paragraph includes specific numbers
- [ ] Emphasized paragraphs use bold titles: `\textbf{The Title}: ...`
- [ ] NO emojis, NO boxes, NO decorative formatting (unprofessional)

**"What We Discovered" Section**:
- [ ] Results or Discussion section includes "What We Discovered" subsection
- [ ] Lists 3-6 key insights with specific numbers
- [ ] Insights are synthesized (not just repeating results)
- [ ] Insights challenge conventional wisdom

---

### Visual Storytelling Checklist

**Enhanced Captions** (4-element format):
- [ ] All figure captions follow: Observation → Implication → Story → Takeaway
- [ ] All table captions follow 4-element format
- [ ] Every caption includes at least one specific number
- [ ] Captions tell a story (not just describe what's shown)

**Color and Emphasis**:
- [ ] Strategic use of bold for key numbers/insights (not overused)
- [ ] Section titles use color sparingly (if using colored headers)
- [ ] No ALL CAPS or underlining (unprofessional)
- [ ] Emphasis supports narrative (doesn't distract)

---

### Eye-Catching Results Checklist

**Counterintuitive Findings**:
- [ ] Abstract mentions at least one counterintuitive finding
- [ ] Introduction highlights what challenges expectations
- [ ] Results section includes "Unexpected Findings" subsection
- [ ] Discussion section explains why findings are surprising

**Specific Numbers**:
- [ ] Every claim has a supporting number
- [ ] Abstract contains ≥3 quantitative metrics
- [ ] Key numbers are repeated in multiple sections (reinforcement)
- [ ] Numbers use appropriate precision (not false precision)

**Actionable Insights**:
- [ ] Results include implications for policy/practice
- [ ] Insights are specific (not vague recommendations)
- [ ] "So what?" is answered for each key finding
- [ ] Takeaways are actionable (not just observations)

---

### Balance Verification (Critical)

**Technical Rigor Check**:
- [ ] All equations copied word-for-word from model_design.md
- [ ] All parameters defined with exact wording
- [ ] Mathematical notation is consistent throughout
- [ ] No summarizing or paraphrasing of math content

**Narrative Engagement Check**:
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

---

### O-Prize Quality Thresholds

**Minimum Standards**:
- ✅ 3+ insight boxes highlighting key discoveries
- ✅ Enhanced captions (4-element) on all major figures/tables
- ✅ Compelling hook in introduction (specific numbers)
- ✅ "What We Discovered" section in Results/Discussion
- ✅ Abstract with ≥3 quantitative metrics
- ✅ 100% math accuracy (equations copied word-for-word)

**O-Prize Excellence Standards**:
- ✅ 5+ insight boxes strategically placed
- ✅ Narrative hooks in multiple sections (not just intro)
- ✅ Counterintuitive findings emphasized throughout
- ✅ Story arc: problem → solution → unexpected insights → implications
- ✅ Every major finding has "so what?" answered
- ✅ Paper would be memorable to judges 6 months later

---

## Prose Density Standards (CRITICAL)

> [!CRITICAL]
> **O-Prize papers read like journal articles, not technical reports.**

### Academic Writing is Prose-Rich

| Technical Report Style | Academic Paper Style |
|------------------------|---------------------|
| Bulleted lists | Flowing paragraphs |
| Assumption tables | Prose explanations |
| Many subheadings | Narrative sections |
| Formula-heavy | Context-rich |
| Sparse interpretation | Deep analysis |

### Minimum Prose Requirements
- **Every equation**: 50+ words of surrounding prose (combined before/after)
- **Every table**: 30+ words of interpretation below caption
- **Every figure**: 40+ words of analysis in text (beyond caption)
- **Every section**: Begins with 3-4 sentence introduction
- **Every section**: Ends with 2-3 sentence transition to next

### Paragraph Templates

**Equation Introduction Template:**
```latex
To address [problem], we formulate [approach]. Following [Author, Year], we define
[key concept] as [brief description]. This formulation captures [key property] while
allowing [flexibility]. The optimization problem can be expressed as:
```

**Equation Interpretation Template:**
```latex
Equation (\ref{eq:name}) captures [key relationship]. The first term represents
[interpretation], while the second term ensures [property]. This formulation is
equivalent to [alternative view], as demonstrated by [Author, Year]. In our context,
this means [practical implication].
```

**Section Transition Template:**
```latex
The preceding analysis demonstrates [key finding]. This result has important
implications for [next topic]. Specifically, [connection between findings]. We now
turn to [next section topic], which [motivation for next section].
```

### Anti-Fragmentation Rules
- **Maximum subheadings per page**: 3 (avoid over-segmentation)
- **Minimum paragraph length**: 4 sentences (avoid bullet-point style)
- **Combine small sections**: If subsection < 1 paragraph, merge with adjacent
- **No orphan paragraphs**: Single sentences between headings are forbidden
