# Strategic Emphasis Templates for O-Prize Quality Papers

**Purpose**: Highlight key discoveries using professional academic formatting
**Usage**: Apply strategic emphasis to 3-5 major findings throughout the paper
**Goal**: Make key findings memorable through selective formatting, not decoration

**Key Principle**: Reference papers use **strategic bolding and structured paragraphs**, not visual boxes or emojis.

---

## Template 1: Counterintuitive Finding Paragraph

**When to Use**: Results contradict conventional wisdom or expert expectations

### Structure

```latex
\textbf{[Finding Title]}: [Specific number] [measurement] contradicts the expectation
that [common assumption]. This [challenges theory/reveals pattern], suggesting
[implication for understanding]. [Supporting evidence with comparison].
```

### Example (Olympic - from reference paper style)

```latex
\textbf{The 2.0 Medal Floor}: 79 countries (51\% of NOCs) are predicted to win
exactly 2.0 medals with identical 95\% prediction intervals (1.0--3.0). This
clustering reveals an artificial ceiling where the model cannot distinguish between
countries, contradicting the expectation that predictions should vary continuously
across nations. Albania, Botswana, Estonia, Latvia, and Lithuania all receive
identical baseline predictions despite different historical performance and regional
contexts.
```

### Variations

**Variation A: Theory-Challenging Finding**
```latex
\textbf{[Theory] Falls Short}: [Specific number] [outcome] contradicts [established
theory], which predicts [expected outcome]. This reveals [mechanism/limitation],
suggesting [new theoretical direction].
```

**Variation B: Scale Surprising Finding**
```latex
\textbf{[Effect Size] Matters}: [Effect size] of [X] is [Y times larger/smaller]
than conventional wisdom suggests. This [amplifies/reduces] the importance of
[factor], mandating [revised approach].
```

---

## Template 2: Policy Implication Paragraph

**When to Use**: Results have direct implications for decision-makers

### Structure

```latex
\textbf{[Actionable Recommendation]}: Our analysis reveals that [specific finding],
suggesting that [stakeholder] should [action]. This [projected impact with number].
Evidence: [specific quantitative support].
```

### Example (Olympic)

```latex
\textbf{Target Middle-Power Nations for Highest ROI}: Investment efficiency follows
a U-shaped curve where small and middle-power nations achieve 50--150\% medal gains
from \$10--50M investments, whereas superpowers gain <2\% from equivalent funding.
Sixteen middle-power countries (10--40 medals) control 23.1\% of global medals.
Targeted \$10M investments yield 10--15\% medal gains vs. <2\% for superpowers,
indicating that National Olympic Committees should prioritize bronze conversion
strategies and niche sport specialization.
```

---

## Template 3: Methodological Discovery Paragraph

**When to Use**: Technical challenges revealed deeper truths

### Structure

```latex
\textbf{[Technical Discovery Title]}: [Technical challenge] revealed [fundamental
constraint]. This was not a computational nuisance—it exposed [deeper truth],
mandating [methodological approach].
```

### Example (Olympic)

```latex
\textbf{Convergence Revealed Identifiability Constraints}: Severe convergence
issues (1,292 divergences, R-hat > 1.01) exposed fundamental identifiability
challenges in distinguishing country-specific effects from shared regional patterns
with limited Olympic observations. The hierarchical structure created parameter
space "waffle" where the sampler struggled to allocate variance correctly between
country and region levels. This difficulty is not a numerical problem but a
reflection of genuine data limitations—individual country parameters are weakly
identified and rely heavily on regional shrinkage.
```

---

## Template 4: Pattern Discovery Paragraph

**When to Use**: Data reveals surprising regularities

### Structure

```latex
\textbf{[Pattern Name]}: Our analysis uncovered [specific pattern] that [challenges
expectations/defies intuition]. This pattern [implication], suggesting [mechanism].
```

### Example (Olympic)

```latex
\textbf{The Gold Efficiency Gap}: Nations cluster into distinct tiers with
"Gold Specialists" (40--60\% gold ratio) and "Volume Accumulators" (15--25\% gold
ratio). This binary structure contradicts the expectation that gold efficiency
should vary continuously across nations. Twenty-two nations fall into the "Gold
Specialist" tier while 89 are "Volume Accumulators," with minimal middle ground.
This bimodal distribution suggests strategic specialization—small nations target
specific high-probability gold events using niche strategies, while large nations
accumulate volume across many events through diversification.
```

---

## Strategic Placement Guidelines

### Where to Place Emphasized Findings

**Introduction** (0-1 paragraphs):
- Use only if there's a compelling hook that sets up the entire paper
- Place at end of introduction as transition to methods

**Methods Section** (0-1 paragraphs):
- Use only for major methodological insights that changed the approach
- Place after model presentation

**Results Section** (2-3 paragraphs):
- Highlight the most counterintuitive or impactful findings
- Place immediately after the result is first presented
- Use strategic bolding for the key phrase

**Discussion Section** (1-2 paragraphs):
- Synthesize insights across multiple findings
- Policy implications or broader impacts

### When NOT to Use Emphasized Paragraphs

❌ **Avoid overuse**: >5 emphasized paragraphs dilutes impact
❌ **Avoid routine results**: Save for genuinely surprising findings
❌ **Avoid obvious conclusions**: Don't state what readers would expect
❌ **Avoid decoration**: Emphasis must add substantive value

### Design Principles

1. **Scarcity**: 3-5 emphasized paragraphs per paper maximum
2. **Specificity**: Every emphasized paragraph includes specific numbers
3. **Actionability**: Every paragraph answers "so what?"
4. **Strategic Placement**: Emphasized paragraph immediately follows relevant result
5. **Professional Formatting**: Use bold title only, not boxes or borders

---

## Caption Enhancement (4-Element Structure)

**Reference papers use complete caption structures**, not just descriptions.

### Template

```latex
\caption{[What figure shows] with specific numbers. [Key insight or pattern revealed].
[Implication or why this matters]. [Actionable takeaway or "so what?"].}
```

### Example

```latex
\caption{Prediction interval width by country size tier, showing small nations face
99.3\% relative uncertainty compared to 78.4\% for superpowers. This inverse
relationship indicates that prediction error scales with country size, challenging
the intuition that larger datasets should reduce relative uncertainty. Small NOCs
must employ flexible funding models with tiered commitments rather than fixed
medal targets.}
```

---

## Quick Reference: Emphasis Selection Guide

| Finding Type | Use This Template | Bold Title Example |
|--------------|------------------|-------------------|
| Contradicts expectations | Template 1 | \textbf{The 2.0 Medal Floor} |
| Implications for decisions | Template 2 | \textbf{Target Middle-Power Nations} |
| Technical struggle revealed truth | Template 3 | \textbf{Convergence Revealed Constraints} |
| Surprising regularity | Template 4 | \textbf{The Gold Efficiency Gap} |

---

**Phase 2 Corrected**: Template file updated to align with reference papers
**Techniques**: Strategic bolding, structured paragraphs, data-driven storytelling
**Removed**: Emojis, fboxes, decorative elements (unprofessional)

### Example (Olympic Medal Prediction)

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{🔍 Key Insight: The "2.0 Medal Floor" Phenomenon}\\

79 countries (51\% of all NOCs) are predicted to win exactly 2.0 medals with identical
95\% prediction intervals (1.0--3.0). This clustering reveals an artificial ceiling where
the model cannot distinguish between countries, contradicting the expectation that
predictions should vary continuously across nations.

\textbf{The Data}: Albania, Botswana, Estonia, Latvia, Lithuania—all predicted 2.0 medals
(1.0--3.0), despite different historical performance and regional contexts.

\textbf{The Implication}: This ceiling is artificial, not fundamental. Countries at the
2.0-medal floor could realistically win 3--4 medals with targeted investments in bronze
conversion strategies (converting 4th--8th place finishes into medals).
\end{minipage}}
\vspace{0.5em}
```

### Variations

**Variation A: Theory-Challenging Finding**
```latex
\textbf{🔍 Key Insight: [Theory] Falls Short}\\

[Specific number] [outcome] contradicts [established theory], which predicts [expected outcome].
This reveals [mechanism/limitation], suggesting [new theoretical direction].
```

**Variation B: Scale Surprising Finding**
```latex
\textbf{🔍 Key Insight: [Effect Size] Matters}\\

[Effect size] of [X] is [Y times larger/smaller] than conventional wisdom suggests.
This [amplifies/reduces] the importance of [factor], mandating [revised approach].
```

---

## Template 2: Policy Recommendation Box

**When to Use**: Results have direct implications for decision-makers or practitioners

### LaTeX Template

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{💡 Policy Insight: [Actionable Recommendation]}\\

Our analysis reveals that [specific finding]. This suggests that [stakeholder] should
[action], which [projected impact with number].

\textbf{Evidence}: [Specific quantitative support]

\textbf{ROI}: [Cost-benefit comparison if available]
\end{minipage}}
\vspace{0.5em}
```

### Example (Olympic Investment Strategy)

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{💡 Policy Insight: Target Middle-Power Nations for Highest ROI}\\

Investment efficiency follows a U-shaped curve: small and middle-power nations achieve
50--150\% medal gains from \$10--50M investments, whereas superpowers gain <2\% from
equivalent funding. National Olympic Committees should prioritize bronze conversion
strategies and niche sport specialization.

\textbf{Evidence}: 16 middle-power countries (10--40 medals) control 23.1\% of global medals.
Targeted \$10M investments yield 10--15\% medal gains vs. <2\% for superpowers.

\textbf{ROI}: \$10M to middle-power nations → +3--6 medals. \$10M to superpowers → +0--2 medals.
\end{minipage}}
\vspace{0.5em}
```

### Variations

**Variation A: High-Priority Action**
```latex
\textbf{💡 Policy Insight: Priority [Number]}\\

[Stakeholder] should [action] because [quantitative rationale]. Delaying this action
risks [consequence with number], while implementing [approach] yields [benefit with number].
```

**Variation B: Resource Allocation**
```latex
\textbf{💡 Policy Insight: Optimal Resource Strategy}\\

[Resource X] should be allocated to [target Y] rather than [alternative Z]. Our analysis
shows [comparison numbers], indicating [efficiency gain]. This strategy [advantage].
```

---

## Template 3: Methodological Insight Box

**When to Use**: Technical struggles or modeling choices revealed deeper truths

### LaTeX Template

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{🔬 Methodological Insight: [Technical Discovery]}\\

[Technical challenge] revealed [fundamental constraint]. This was not a computational
nuisance—it exposed [deeper truth about system], mandating [methodological approach].

\textbf{The Challenge}: [Brief technical description]

\textbf{The Revelation}: [What this revealed about the domain]

\textbf{The Solution}: [How model evolved to address this]
\end{minipage}}
\vspace{0.5em}
```

### Example (Olympic Modeling)

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{🔬 Methodological Insight: Convergence Struggles Revealed Identifiability Constraints}\\

Severe convergence issues (1,292 divergences, R-hat > 1.01) exposed fundamental
identifiability challenges: distinguishing country-specific effects from shared regional
patterns is inherently difficult with limited Olympic observations.

\textbf{The Challenge}: Hierarchical structure created "waffle" in parameter space—sampler
struggled to allocate variance correctly between country and region levels.

\textbf{The Revelation}: This wasn't a numerical problem—it revealed that country-specific
effects are difficult to distinguish from regional patterns with only ~30 observations per country.

\textbf{The Solution}: Hierarchical shrinkage toward regional means, which balances
country-specific estimates with shared regional patterns.
\end{minipage}}
\vspace{0.5em}
```

### Variations

**Variation A: Data Structure Revelation**
```latex
\textbf{🔬 Methodological Insight: Data Reveals [Structure]}\\

[Modeling challenge] exposed [underlying data structure]. This necessitates [approach],
which [benefit]. Alternative approaches [failed limitation].
```

**Variation B: Algorithm Selection Insight**
```latex
\textbf{🔬 Methodological Insight: Why [Algorithm] Not [Alternative]}\\

Initial [algorithm] attempts [failed outcome]. This revealed [constraint], mandating
switch to [alternative algorithm]. The result: [quantitative improvement].
```

---

## Template 4: Unexpected Pattern Box

**When to Use**: Data reveals surprising regularities, clusters, or anomalies

### LaTeX Template

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{🎯 Pattern Discovery: [Unexpected Regularity]}\\

Our analysis uncovered [specific pattern] that [challenges expectations/defies intuition].
This pattern [implication], suggesting [mechanism/explanation].

\textbf{The Pattern}: [Detailed description with numbers]

\textbf{Why Surprising}: [What conventional wisdom predicts]

\textbf{Potential Explanation}: [Hypothesis for why this occurs]
\end{minipage}}
\vspace{0.5em}
```

### Example (Olympic Medal Distribution)

```latex
\noindent\fbox{\begin{minipage}{\textwidth}
\textbf{🎯 Pattern Discovery: The "Gold Efficiency Gap"}\\

Nations cluster into distinct tiers: "Gold Specialists" (40--60\% gold ratio) vs.
"Volume Accumulators" (15--25\% gold ratio). This binary structure contradicts the
expectation that gold efficiency should vary continuously across nations.

\textbf{The Pattern}: 22 nations fall into "Gold Specialist" tier (gold/total > 0.4),
while 89 nations are "Volume Accumulators" (gold/total < 0.25). Minimal middle ground.

\textbf{Why Surprising}: If medal quality were normally distributed, we'd expect a
continuous gradient of gold ratios, not bimodal clustering.

\textbf{Potential Explanation}: Strategic specialization—small nations target specific
high-probability gold events (niche strategy), while large nations accumulate volume
across many events (diversification strategy).
\end{minipage}}
\vspace{0.5em}
```

### Variations

**Variation A: Threshold Pattern**
```latex
\textbf{🎯 Pattern Discovery: The [Threshold] Effect}\\

[Outcome] remains flat until [variable] exceeds [threshold value], then increases
abruptly. This step-function pattern suggests [mechanism], contradicting [linear assumption].
```

**Variation B: Inverse Relationship**
```latex
\textbf{🎯 Pattern Discovery: The [Paradox]}\\

Conventional wisdom holds that [X] should correlate with [Y]. Our data reveals the opposite:
[negative correlation with numbers]. This paradox suggests [explanation].
```

---

## Strategic Placement Guidelines

### Where to Place Insight Boxes

**Introduction** (0-1 boxes):
- Use only if there's a compelling hook that sets up the entire paper
- Example: "The 2.0 Medal Floor" if it's the central discovery

**Methods Section** (0-1 boxes):
- Use only for major methodological insights that changed the approach
- Example: Convergence struggles revealing identifiability constraints

**Results Section** (2-3 boxes):
- Highlight the most counterintuitive or impactful findings
- Place immediately after the result is first presented
- Example: "Host Advantage Overrated" after presenting host effect quantification

**Discussion Section** (1-2 boxes):
- Synthesize insights across multiple findings
- Policy implications or broader impacts
- Example: "Middle-Power Investment Strategy" synthesizing multiple results

### When NOT to Use Insight Boxes

❌ **Avoid overuse**: >5 insight boxes dilutes impact
❌ **Avoid routine results**: Save for genuinely surprising findings
❌ **Avoid obvious conclusions**: Don't state what readers would expect
❌ **Avoid decoration**: Insight boxes must add substantive value

### Design Principles

1. **Scarcity**: 3-5 boxes per paper maximum
2. **Specificity**: Every box includes specific numbers
3. **Actionability**: Every box answers "so what?"
4. **Strategic Placement**: Box immediately follows relevant result
5. **Visual Distinction**: Use fboxed minipage with emoji or bold title

---

## Quick Reference: Box Selection Guide

| Finding Type | Use This Template | Example |
|--------------|------------------|---------|
| Contradicts expectations | Template 1: Counterintuitive Finding | Host advantage +1.5% not 10-20% |
| Implications for decisions | Template 2: Policy Recommendation | Invest in middle-power nations |
| Technical struggle revealed truth | Template 3: Methodological Insight | Convergence → identifiability |
| Surprising regularity | Template 4: Unexpected Pattern | Bimodal gold efficiency gap |

---

**Phase 2 Complete**: Template file created
**Next**: Create narrative_hook_templates.md
