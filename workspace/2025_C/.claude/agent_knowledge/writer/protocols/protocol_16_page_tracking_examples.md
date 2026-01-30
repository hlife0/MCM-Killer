# Protocol 16: Page Count Tracking Examples

This file provides detailed examples and scenarios for Protocol 16 (Page Count Tracking Compliance).

## Reporting Format

After EACH Phase 7 sub-phase (7A-7F), report to Director using this format:

```
Director, Phase 7[X] complete.

File: output/paper/paper.tex
Sections written: [list sections]
Current page count: [X.X] pages
Budget status: [GREEN/YELLOW/RED]
Checkpoint: output/paper/checkpoint_7[X].md

Ready for Phase 7[Y].
```

## Budget Status Thresholds

| Status | Page Count | Action Required |
|--------|-----------|-----------------|
| **GREEN** | < 20.0 pages | Continue normally |
| **YELLOW** | 20.0 - 22.9 pages | Warning - optimize remaining sections |
| **RED** | 23.0 - 24.9 pages | Critical - trigger emergency consolidation |
| **LIMIT** | ≥ 25.0 pages | REJECT - must reduce before proceeding |

## Example Scenarios

### Scenario 1: GREEN Status (Phase 7B)

```
Director, Phase 7B complete.

File: output/paper/paper.tex
Sections written: Abstract, Introduction, Notation, Models 1-5
Current page count: 15.3 pages
Budget status: GREEN (15.3/25.0, 61% used)
Checkpoint: output/paper/checkpoint_7B.md

Remaining budget: 9.7 pages for Results, Analysis, Conclusions
Ready for Phase 7C.
```

**Analysis:** On track, no action needed.

### Scenario 2: YELLOW Status (Phase 7C)

```
Director, Phase 7C complete.

File: output/paper/paper.tex
Sections written: Abstract through Results
Current page count: 21.4 pages
Budget status: YELLOW (21.4/25.0, 86% used)
Checkpoint: output/paper/checkpoint_7C.md

WARNING: Only 3.6 pages remaining for:
- Sensitivity Analysis (est. 1.5 pages)
- Strengths/Weaknesses (est. 1.0 page)
- Discussion/Conclusions (est. 2.0 pages)
Total needed: 4.5 pages

ACTION: Will consolidate sensitivity analysis and streamline discussion to fit budget.
Ready for Phase 7D.
```

**Analysis:** Yellow warning triggered. Writer will optimize remaining sections.

### Scenario 3: RED Status (Emergency Consolidation)

```
Director, Phase 7D complete.

File: output/paper/paper.tex
Sections written: Abstract through Strengths/Weaknesses
Current page count: 23.8 pages
Budget status: RED (23.8/25.0, 95% used)
Checkpoint: output/paper/checkpoint_7D.md

CRITICAL: Only 1.2 pages remaining for Discussion/Conclusions (needs 2.0 pages minimum)

EMERGENCY CONSOLIDATION TRIGGERED:
1. Reducing model section lengths by 0.5 pages total (remove redundant explanations)
2. Condensing sensitivity analysis by 0.3 pages (remove minor parameter tests)
3. Streamlining strengths/weaknesses by 0.2 pages (merge similar points)
Target: Recover 1.0 page → allows 2.2 pages for conclusions

Implementing consolidation now...
```

**Analysis:** Red critical status. Writer initiates emergency consolidation protocol.

### Scenario 4: LIMIT Exceeded (REJECT)

```
Director, Phase 7E complete.

File: output/paper/paper.tex
Sections written: Complete paper
Current page count: 25.3 pages
Budget status: LIMIT EXCEEDED (25.3/25.0)
Checkpoint: output/paper/checkpoint_7E.md

REJECT: Paper exceeds 25-page limit by 0.3 pages.

REQUIRED REDUCTIONS:
1. Remove appendix examples (0.2 pages)
2. Consolidate two similar figures (0.15 pages)
Total reduction: 0.35 pages → brings to 24.95 pages

Implementing reductions now...
```

**Analysis:** Limit exceeded. Writer must reduce before Phase 7F.

## Page Allocation Guidelines (23-25 page paper)

| Section | Typical Pages | Percentage |
|---------|--------------|------------|
| Summary Sheet | 1 | 4% |
| Introduction | 2-2.5 | 8-10% |
| Methods (Models) | 10-12 | 40-48% |
| Results | 4-5 | 16-20% |
| Discussion/Conclusions | 2.5-3 | 10-12% |
| References | 1-1.5 | 4-6% |
| Appendices | 1-2 | 4-8% |

**Key Insight:** Methods section is the LARGEST (40-48%), not Results.

## Emergency Consolidation Strategies

When RED or LIMIT exceeded, apply these strategies in order:

1. **Remove redundancy** (first choice):
   - Eliminate repeated explanations
   - Merge similar paragraphs
   - Remove obvious statements

2. **Consolidate figures/tables**:
   - Combine related plots into subplots
   - Use multi-column tables
   - Move minor figures to appendix

3. **Streamline sections**:
   - Reduce sensitivity analysis to key parameters only
   - Condense strengths/weaknesses (3-4 items each, not 5-6)
   - Shorten literature review

4. **Format optimization** (last resort):
   - Reduce figure sizes slightly (0.9 → 0.8 textwidth)
   - Tighten spacing (but stay within MCM standards)
   - Use more efficient table layouts

**Do NOT:**
- ❌ Remove entire sections (violates requirements)
- ❌ Delete critical equations or results
- ❌ Use tiny fonts or abnormal margins
- ❌ Remove required content to meet page limit

## Checkpoint File Format

Each checkpoint file should document:

```markdown
# Phase 7[X] Checkpoint

**Timestamp:** 2026-01-28T15:30:00Z
**Sections Written:** [list]
**Page Count:** X.X pages
**Budget Status:** GREEN/YELLOW/RED

## Page Breakdown
- Section 1: X.X pages
- Section 2: X.X pages
- Total: X.X pages

## Quality Checks
- [ ] All equations copied word-for-word
- [ ] All figures have 4-element captions
- [ ] Tables generated from CSV (Protocol 18)
- [ ] No corruption detected

## Next Phase
- Phase 7[Y]: [section names]
- Estimated pages: X.X
- Projected total: X.X pages
```

## Version Control Integration

Update VERSION_MANIFEST.json after each phase:

```json
{
  "phase_7a": {
    "status": "completed",
    "timestamp": "2026-01-28T14:30:00Z",
    "page_count": 4.2,
    "budget_status": "GREEN"
  },
  "phase_7b": {
    "status": "completed",
    "timestamp": "2026-01-28T15:15:00Z",
    "page_count": 15.3,
    "budget_status": "GREEN"
  },
  "phase_7c": {
    "status": "completed",
    "timestamp": "2026-01-28T15:45:00Z",
    "page_count": 21.4,
    "budget_status": "YELLOW"
  }
}
```
