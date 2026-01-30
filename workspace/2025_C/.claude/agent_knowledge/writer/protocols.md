# Writer Agent Protocols

This file contains the complete protocols for the writer agent.

## Revision-Verification Cycle Protocol

See writer.md line 928 for the complete protocol.

**Key Points:**
- After EACH write operation, read back the file to verify
- Check for corruption: random fragments, duplicates, garbled commands
- If corruption detected: DELETE and rewrite the section
- Never proceed to next section without verifying previous section

## Source File Integration Protocol (Three-Tier Protocol)

This protocol defines when to COPY vs. ADAPT vs. SYNTHESIZE content from source files.

### Tier 1: COPY (Word-for-Word)

**When:** Mathematical content, technical specifications, critical data

**What to Copy:**
- ALL equations from model_design.md
- ALL parameter definitions
- ALL notation table entries
- ALL assumptions (exact wording)
- ALL algorithm steps (complete procedure)

**Why:** Mathematical precision is non-negotiable. Any paraphrasing introduces risk of errors.

**Example:**
```
Source (model_design.md):
  The objective function is:
  \min_{x} Z = \sum_{i=1}^{n} c_i x_i

Paper (paper.tex):
  The objective function is:
  \min_{x} Z = \sum_{i=1}^{n} c_i x_i
```

### Tier 2: ADAPT (Structure + Wording)

**When:** Method descriptions, justifications, narrative context

**What to Adapt:**
- Model overviews (convert bullet points to paragraphs)
- Justifications (add transitions, academic phrasing)
- Results descriptions (integrate with figures/tables)

**Why:** Source files are technical notes, not publication-ready prose.

**Example:**
```
Source (model_design.md):
  - Model handles zero-inflation
  - Uses hurdle approach
  - Separates probability of medal vs. count

Paper (paper.tex):
  We employ a hurdle model to address zero-inflation in the medal data.
  This approach separates the probability of winning any medal from the
  count distribution for medal-winning countries, providing more accurate
  predictions for both medal-winning and non-medal-winning nations.
```

### Tier 3: SYNTHESIZE (Integrate Multiple Sources)

**When:** Introduction, Discussion, Conclusions sections

**What to Synthesize:**
- Requirements from requirements_checklist.md
- Methods from research_notes.md
- Results from results_summary.md
- Insights from methodology_evolution_{i}.md
- Narrative from narrative_arc_*.md

**Why:** These sections require weaving together information from multiple sources.

**Example:**
```
Sources:
  requirements_checklist.md: "Predict medal counts for 2028"
  research_notes.md: "Hurdle models recommended for zero-inflated data"
  results_summary.md: "USA: 126.3 medals (95% CI: 118.5-134.1)"

Paper (paper.tex):
  Our hurdle model predicts the United States will win 126.3 total medals
  at the 2028 Los Angeles Games (95% CI: 118.5-134.1), representing a
  modest 1.5% increase over 2024. This prediction accounts for both the
  host advantage and the zero-inflated structure of Olympic medal data.
```

## Decision Framework: Which Tier?

| Content Type | Tier | Action |
|--------------|------|--------|
| Equations | 1 | COPY word-for-word |
| Parameter definitions | 1 | COPY exactly |
| Notation table | 1 | COPY all entries |
| Assumptions | 1 | COPY exact wording |
| Algorithm steps | 1 | COPY complete procedure |
| Model overviews | 2 | ADAPT to paragraph form |
| Justifications | 2 | ADAPT with transitions |
| Method descriptions | 2 | ADAPT to academic style |
| Introduction | 3 | SYNTHESIZE from multiple sources |
| Results narrative | 3 | SYNTHESIZE data + figures + context |
| Discussion | 3 | SYNTHESIZE findings + implications |
| Conclusions | 3 | SYNTHESIZE all requirements |

## Critical Path Fix: Figure Paths

**Issue:** paper.tex is in `output/paper/` while figures are in `output/figures/`

**Solution:** Use `../figures/` (not `figures/`)

**Correct:**
```latex
\includegraphics[width=0.9\textwidth]{../figures/figure_name.png}
```

**Wrong:**
```latex
\includegraphics[width=0.9\textwidth]{figures/figure_name.png}
```

## Protocol 18: Automated Value Injection

**Purpose:** Prevent data inconsistency between CSV and LaTeX tables

**Requirements:**
1. Generate all numerical tables using `csv_to_latex_table.py`:
   ```bash
   python output/implementation/code/csv_to_latex_table.py <csv_path> <table_id>
   ```
2. Include in LaTeX using `\input{}`:
   ```latex
   \input{../output/paper/tables/table_1.tex}
   ```
3. NEVER manually transcribe numbers from CSV to LaTeX
4. @validator validates before Phase 7.5 (Exit 0 = PASS, Exit 1 = REJECT)

**Rejection Policy:**
- Data inconsistency = AUTOMATIC REJECTION
- Must fix and regenerate tables
- No override allowed

## Writing Protocol (Section-by-Section)

**DO NOT write entire paper in one Write call.**

**Phase 7A** (Framework):
1. Write Summary + Introduction + Notation → Save to paper.tex
2. Read back paper.tex → Verify no corruption

**Phase 7B** (Models):
3. Append Assumptions + Model sections → Save
4. Read back paper.tex → Verify no corruption

**Phase 7C** (Results):
5. Append Results section → Save
6. Read back paper.tex → Verify no corruption

**Phase 7D** (Analysis):
7. Append Sensitivity + Strengths/Weaknesses → Save
8. Read back paper.tex → Verify no corruption

**Phase 7E** (Conclusions):
9. Append Discussion + Conclusions + Bibliography → Save
10. Final read of entire paper.tex → Verify completeness

**Phase 7F** (Compilation):
11. Compile LaTeX to PDF → Verify PDF generated

## Corruption Detection

After EACH write, read back the file and check for:
- Random text fragments inserted mid-sentence
- Duplicate content
- Missing sections
- Garbled LaTeX commands

**If corruption detected:** DELETE the file and rewrite that section.
