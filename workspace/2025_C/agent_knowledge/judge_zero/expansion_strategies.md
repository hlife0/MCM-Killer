# Expansion Strategies for Under-Length Papers

**Agent**: @judge_zero (routing), @writer (execution), @visualizer (support)
**Purpose**: Quick reference for expanding papers that fall below the 24-page minimum
**Last Updated**: 2026-02-01

---

## Quick Reference by Page Deficit

| Current Pages | Deficit | Primary Strategy | Secondary Strategy | Est. Time |
|---------------|---------|------------------|-------------------|-----------|
| 22-24 | 0-2 pages | Expand discussions | Add sensitivity details | 30-60 min |
| 20-22 | 2-4 pages | Add conceptual figures | Expand model descriptions | 1-2 hours |
| 18-20 | 4-6 pages | Multiple strategies | Restructure entirely | 2-3 hours |
| <18 | 6+ pages | Full content review | Consider adding appendix | 3+ hours |

---

## 6 Expansion Strategies (Priority Order)

### Priority 1: Add Conceptual Figures (+1-2 pages)

**Agent**: @visualizer
**Phase to Revisit**: Phase 6 or Phase 7

**What to Add**:
- Model architecture diagrams
- Flowcharts showing methodology workflow
- DAG (Directed Acyclic Graph) for causal relationships
- Decision tree visualizations
- Timeline diagrams (if applicable)

**Request Format**:
```
@visualizer: REQUEST_CONCEPTUAL_DIAGRAM

Type: [Flowchart / Architecture / DAG / Hierarchy / Timeline]
Description: [What the diagram should show]
Context: [Which section/model this is for]
Key Elements: [List of nodes/steps to include]
Suggested Filename: model_X_diagram_[description].png
```

**Page Gain**: +0.5 to +1.0 pages per diagram (with caption and explanation)

---

### Priority 2: Expand Model Descriptions (+1-2 pages)

**Agent**: @writer
**Phase to Revisit**: Phase 7B

**What to Expand**:
- Mathematical derivations (move from appendix to main text)
- Parameter justifications
- Model assumptions with detailed rationale
- Comparison with alternative approaches (and why chosen)
- Step-by-step algorithmic explanations

**Source Material**:
- `output/model_design.md` - full mathematical formulations
- `output/docs/consultations/` - expert feedback on methodology
- `knowledge_library/` - theoretical foundations

**Page Gain**: +0.3 to +0.5 pages per model section

---

### Priority 3: Add Sensitivity Analysis Details (+0.5-1 page)

**Agent**: @writer, @validator
**Phase to Revisit**: Phase 7D

**What to Expand**:
- Additional parameter variations
- Robustness checks not previously included
- Extended discussion of sensitivity results
- Tornado diagrams or additional sensitivity plots
- Comparison across different scenarios

**Page Gain**: +0.5 to +1.0 page

---

### Priority 4: Expand Results Interpretation (+0.5-1 page)

**Agent**: @writer
**Phase to Revisit**: Phase 7C

**What to Expand**:
- Deeper interpretation of each table/figure
- "What We Discovered" section with synthesized insights
- Unexpected findings subsection
- Comparison with domain expectations
- Policy/practical implications

**Page Gain**: +0.5 to +1.0 page

---

### Priority 5: Add Appendix Content (+1-2 pages)

**Agent**: @writer
**Phase to Revisit**: Phase 7E

**What to Add**:
- Detailed data description (sources, preprocessing)
- Extended model derivations
- Additional results tables
- Convergence diagnostics
- Code and reproducibility notes

**Page Gain**: +1.0 to +2.0 pages

---

### Priority 6: Expand Discussion Section (+0.5 page)

**Agent**: @writer
**Phase to Revisit**: Phase 7E

**What to Expand**:
- Limitations discussion
- Comparison with prior work
- Future research directions
- Broader implications
- Methodology evolution insights

**Source Material**:
- `output/docs/methodology_evolution_{i}.md` (from @metacognition_agent)

**Page Gain**: +0.3 to +0.5 page

---

## Expansion Anti-Patterns to AVOID

### DO NOT:

1. **Pad with Fluff**
   - ❌ Adding redundant sentences that repeat the same information
   - ❌ Excessive use of transitional phrases
   - ❌ Verbose restatements of results

2. **Over-Explain Basics**
   - ❌ Multi-page explanations of standard methods (cite instead)
   - ❌ Defining well-known terms extensively
   - ❌ Lengthy literature reviews beyond scope

3. **Add Low-Value Content**
   - ❌ Including results that don't support conclusions
   - ❌ Adding figures without meaningful interpretation
   - ❌ Appendix content that duplicates main text

4. **Sacrifice Readability**
   - ❌ Increasing font size or margins
   - ❌ Excessive whitespace between sections
   - ❌ Stretching tables or figures unnecessarily

5. **Break Content Flow**
   - ❌ Inserting tangential discussions
   - ❌ Adding content that disrupts narrative arc
   - ❌ Including sections that don't connect to main argument

---

## Strategy Selection Matrix

| Situation | Best Strategy | Avoid |
|-----------|---------------|-------|
| Strong results, weak methodology explanation | Priority 2 (Expand Models) | Priority 4 |
| Good text, few visuals | Priority 1 (Add Figures) | Priority 6 |
| Shallow analysis | Priority 3 (Sensitivity) | Priority 5 |
| Results lack interpretation | Priority 4 (Expand Results) | Priority 2 |
| Missing supplementary material | Priority 5 (Appendix) | Priority 1 |
| Thin discussion | Priority 6 (Discussion) | Priority 3 |

---

## Expansion Routing Table

| Issue Type | Primary Agent | Supporting Agent | Phase |
|------------|--------------|------------------|-------|
| Missing conceptual diagrams | @visualizer | @writer | 6/7 |
| Thin model sections | @writer | @modeler | 7B |
| Insufficient sensitivity | @validator | @writer | 7D |
| Shallow results | @writer | @visualizer | 7C |
| Missing appendix | @writer | @data_engineer | 7E |
| Weak discussion | @writer | @metacognition_agent | 7E |

---

## Expansion Verification Checklist

After expansion, verify:

- [ ] Total page count >= 24 pages
- [ ] Added content is substantive (not padding)
- [ ] Narrative flow maintained
- [ ] All new figures have 4-element captions
- [ ] Content balance still appropriate (~44% models)
- [ ] No new blank space issues created
- [ ] LaTeX compiles without errors

---

**END OF EXPANSION STRATEGIES**
