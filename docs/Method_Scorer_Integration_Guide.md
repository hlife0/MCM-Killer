# Method Scorer Integration Guide

## Overview

The Method Scorer provides a quantitative framework for evaluating and ranking mathematical modeling methods using a 5-dimensional evaluation rubric. This guide explains how to integrate and use the scoring system in MCM-Killer.

**Source**: MM_Assets_Export/retrieve_method/ (清华大学数学建模团队)
**Integration Status**: ✅ Complete - Rubric and guidelines integrated

---

## Components

### 1. Scoring Rubric
**Location**: `knowledge_library/method_scoring/scoring_rubric.md`

**Five Dimensions** (each scored 0-10):
1. **Applicability** (适用性) - How well method fits problem type
2. **Feasibility** (可行性) - Implementation practicality under constraints
3. **Cost/Efficiency** (成本/效率) - Time, resources, complexity requirements
4. **Risk** (风险) - Failure likelihood (higher = lower risk)
5. **Clarity** (清晰度) - Implementation clarity and documentation quality

**Total Score**: Average of all 5 dimensions (0-10 scale)

### 2. Reference Implementation
**Location**: `tools/method_scorer.py`

**Features**:
- Hierarchical method tree processing
- Parent-child weight propagation (default 50/50)
- Top-k method selection
- Embedding-based semantic similarity (optional)
- LLM-based evaluation (optional)

**Status**: Adapted from MM_Assets_Export, dependencies removed for MCM-Killer architecture

### 3. Usage Documentation
**Location**: `knowledge_library/method_scoring/README.md`

**Contents**:
- Detailed scoring guidelines
- Conservative scoring approach
- Red flag detection (auto-reject criteria)
- Integration with agents workflow
- Usage examples

---

## Installation

### Prerequisites

**Required**:
- Python 3.10+
- HMML 2.0 index files: `knowledge_library/hmml_summary.json`
- Scoring rubric: `knowledge_library/method_scoring/scoring_rubric.md`

**Optional** (for automated scoring):
- `sentence-transformers` (for embedding-based scoring)
- OpenAI API or similar (for LLM-based evaluation)

### Setup

1. **Verify files exist**:
```bash
ls -l knowledge_library/method_scoring/scoring_rubric.md
ls -l knowledge_library/hmml_summary.json
```

2. **Test reference implementation** (optional):
```bash
cd tools/
python method_scorer.py --help
```

3. **Review scoring rubric**:
```bash
cat knowledge_library/method_scoring/scoring_rubric.md
```

---

## Usage

### For @knowledge_librarian: Manual Scoring

When invoked for method consultation:

1. **Understand the problem**:
   - Read requirements from @reader's checklist
   - Identify problem type (optimization, prediction, etc.)
   - Note constraints (time, data, resources)

2. **Retrieve candidate methods**:
   - Query HMML 2.0 index for relevant methods
   - Filter by domain applicability
   - Select 10-15 candidates for evaluation

3. **Apply scoring rubric**:
   For each candidate method, score 0-10 on:
   - **Applicability**: Does this method solve the core problem?
   - **Feasibility**: Can we implement this in 72 hours?
   - **Cost/Efficiency**: What are computational/time requirements?
   - **Risk**: How likely is this to fail? (Higher = less risky)
   - **Clarity**: Is this method well-documented?

4. **Calculate total scores**:
   ```
   Total = (Applicability + Feasibility + Cost/Efficiency + Risk + Clarity) / 5
   ```

5. **Rank and select**:
   - Sort methods by total score (descending)
   - Select top-k methods (k=6-10)
   - Prepare justifications for each

6. **Output to @researcher**:
   ```markdown
   # Top 6 Methods for [Problem Name]

   ## 1. [Method Name] (Total: 8.4/10)
   **Scores**: Applicability: 9.0, Feasibility: 8.0, Cost/Efficiency: 9.0, Risk: 7.0, Clarity: 9.0
   **Rationale**: Excellent fit for prediction with continuous variables. Well-established method with low implementation complexity. Main assumptions compatible with problem structure. Minor risk: assumes linear relationships.

   ## 2. [Method Name] (Total: 8.1/10)
   [... continue for top 6-10 methods ...]
   ```

### Example Scoring Session

**Problem**: "Predict Olympic medal counts based on GDP, population, and past performance"

**Candidate Method**: Multiple Regression Analysis

**Scoring Process**:

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| **Applicability** | 9.0 | Perfect for continuous prediction problems. Designed exactly for this type of "predict Y given X1, X2, X3" problem. |
| **Feasibility** | 8.0 | Standard method, widely implemented. Python (sklearn), R, Excel all support it. High probability of successful implementation. |
| **Cost/Efficiency** | 9.0 | Very fast to implement (minutes to hours). Low computational requirements. Can iterate quickly. |
| **Risk** | 7.0 | Well-established, low risk of failure. BUT: Assumes linear relationships, which may not hold. Assumes independence of predictors, which may be violated (GDP correlated with population). |
| **Clarity** | 9.0 | Extremely well-documented. Tons of examples. Interpretation is straightforward (coefficients = effect size). |
| **Total** | **8.4/10** | **Strongly recommended** |

**Comparison with other methods**:
- Random Forest: 8.1/10 (better nonlinear capture, but less interpretable)
- Neural Network: 6.5/10 (overkill for small data, black box)
- Poisson Regression: 7.8/10 (good for counts, but less flexible)

**Result**: Multiple Regression ranked #1, recommended as baseline

---

## Scoring Guidelines

### Conservative Approach

When uncertain, use conservative scores:

**Default Range**: 5-7 (moderate)
- Don't give 9-10 unless clearly exceptional
- Don't give 1-2 unless clearly terrible
- Most methods fall in the middle range

**Risk Dimension Special Handling**:
- Default to 6-7 (moderate uncertainty)
- Unless method is clearly proven (9-10) or clearly experimental (1-3)
- Remember: Higher score = LOWER risk (inverted scale)

**Context Matters**:
- **Time-limited competition** (72 hours): Penalize complex methods (Cost/Efficiency)
- **Data-poor problems**: Penalize data-intensive methods (Feasibility < 6)
- **Team expertise**: Adjust Clarity based on team familiarity

### Red Flags (Auto-Reject)

If ANY dimension scores below threshold, **AUTO-REJECT** the method:

| Dimension | Threshold | Rationale |
|-----------|-----------|-----------|
| Applicability | < 5 | Wrong problem type - don't use |
| Feasibility | < 4 | Impossible to implement - don't attempt |
| Risk | < 3 | Experimental/unproven - too risky for competition |
| Cost/Efficiency | < 3 | Prohibitively expensive - will exceed timeline |
| Clarity | < 3 | Too vague - can't implement reliably |

**Example**: "Deep learning with custom architecture"
- Applicability: 7/10 (could work)
- Feasibility: 3/10 (need 1000+ samples, probably only have 100)
- **Result**: AUTO-REJECT due to Feasibility < 4

### Scoring Rubric Reference

For detailed criteria, see `knowledge_library/method_scoring/scoring_rubric.md`:

**Applicability Criteria**:
- 9-10: Perfect fit
- 7-8: Good fit with minor adjustments
- 5-6: Moderate fit, some aspects not aligned
- 3-4: Poor fit, major aspects incompatible
- 1-2: Fundamentally unsuitable

**Feasibility Criteria**:
- 9-10: Highly feasible with standard tools
- 7-8: Feasible with reasonable effort
- 5-6: Moderately feasible, requires significant effort
- 3-4: Challenging, may require specialized resources
- 1-2: Impractical or impossible

**Cost/Efficiency Criteria**:
- 9-10: Very efficient, minimal resources
- 7-8: Good efficiency, reasonable requirements
- 5-6: Moderate efficiency, acceptable usage
- 3-4: Low efficiency, high requirements
- 1-2: Prohibitively expensive

**Risk Criteria** (higher = lower risk):
- 9-10: Very low risk, well-established
- 7-8: Low risk, minor uncertainties
- 5-6: Moderate risk, some uncertainties
- 3-4: High risk, major uncertainties
- 1-2: Very high risk, experimental

**Clarity Criteria**:
- 9-10: Very clear, well-documented, step-by-step
- 7-8: Clear, good documentation available
- 5-6: Moderately clear, some ambiguity
- 3-4: Unclear, limited guidance
- 1-2: Very vague or poorly defined

---

## Integration with Workflow

### Phase 0.2: Knowledge Retrieval

```
@reader completes problem analysis
  ↓
@researcher requests method consultation
  ↓
@knowledge_librarian invoked
  ↓
1. Query HMML 2.0 for candidates
2. Score candidates using 5-dim rubric
3. Rank by total score
4. Return top-k with justifications
  ↓
@researcher uses scored list for method selection
```

### Handoff Format

**Input** (from @researcher):
```
Problem: "Design food distribution network during epidemic"
Domain: Optimization + Network Science
Constraints: 72 hours, limited computational resources
Data: City locations, demand points, supply capacities
```

**Output** (from @knowledge_librarian):
```markdown
# Top 6 Methods for Epidemic Food Distribution Optimization

## 1. Minimum Cost Flow (Total: 8.7/10)
**Scores**: Applicability: 9.0, Feasibility: 9.0, Cost/Efficiency: 9.0, Risk: 8.0, Clarity: 9.0
**Rationale**: Perfect fit for network flow problem. Standard algorithm (Network Simplex), well-tested, fast computation. Very low risk - extensively used in logistics. Excellent documentation available.

## 2. Vehicle Routing Problem (VRP) (Total: 8.2/10)
**Scores**: Applicability: 9.0, Feasibility: 7.0, Cost/Efficiency: 7.0, Risk: 8.0, Clarity: 9.0
**Rationale**: Captures routing aspect well. More complex than MCF, requires heuristics for large instances. Still feasible within 72 hours using Google OR-Tools.

[... 4 more methods ...]
```

### Downstream Usage

**@researcher**:
- Reviews top-k methods
- Selects methods based on scores and justifications
- Considers problem-specific factors
- Makes final recommendation to @modeler

**@modeler**:
- Reviews scored recommendations
- Checks risk and feasibility before finalizing
- Uses `modeling_basic.txt` or `modeling_advanced.txt` based on complexity
- Designs mathematical model

---

## Troubleshooting

### Issue: All methods scoring low (6-7 range)

**Cause**: Rubric applied too strictly

**Fix**:
- Remember scores are relative, not absolute
- Focus on ranking methods, not absolute perfection
- Adjust thresholds based on problem difficulty
- Use 7-8 as "good" for hard problems

### Issue: High-risk methods scoring well

**Cause**: Risk dimension underweighted

**Fix**:
- Increase weight of risk dimension in total calculation
- Apply risk veto: if risk < 5, auto-reject regardless of total score
- For competitions, prioritize proven methods over novel ones

### Issue: Too many methods tied at same score

**Cause**: Insufficient granularity in 0-10 scale

**Fix**:
- Use decimal scores: 7.3, 7.5, 7.7 (not just 7, 8, 9)
- Add tie-breaker criteria:
  1. Prefer lower risk
  2. Prefer higher clarity
  3. Prefer simpler methods (Occam's razor)

### Issue: Disagreement with @researcher

**Cause**: Different evaluation criteria

**Fix**:
- @knowledge_librarian provides scored list (objective)
- @researcher provides domain expertise (subjective)
- Both inputs considered by @director for final decision
- Document rationale for disagreements

---

## Advanced Usage

### Automated Scoring (Future)

**Option 1: Embedding-based Scoring**
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
problem_embedding = model.encode(problem_description)
method_embeddings = model.encode([method['description'] for method in methods])

# Calculate cosine similarity
scores = cosine_similarity(problem_embedding, method_embeddings)
```

**Option 2: LLM-based Evaluation**
```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{
        "role": "system",
        "content": "You are a method scoring expert. Rate this method on 5 dimensions (0-10)."
    }, {
        "role": "user",
        "content": f"Problem: {problem}\nMethod: {method}\nProvide scores in JSON format."
    }]
)
```

**Status**: Not yet implemented. Requires API access and testing.

### Domain-Specific Weighting

For certain problem types, adjust dimension weights:

**Medical/Health Problems** (risk-averse):
```
Total = (Applicability + 2*Risk + Feasibility + Cost + Clarity) / 6
```
(Risk weighted 2× because lives at stake)

**Exploratory Research** (risk-tolerant):
```
Total = (Applicability + 0.5*Risk + Feasibility + Cost + Clarity) / 5
```
(Risk weighted 0.5× because novelty valued)

**Time-Critical** (efficiency-focused):
```
Total = (Applicability + Feasibility + 2*Cost + Risk + Clarity) / 6
```
(Cost weighted 2× because timeline tight)

---

## Best Practices

### DO ✅

1. **Score consistently**: Use same rubric for all methods
2. **Document rationale**: Explain WHY you gave each score
3. **Be conservative**: Default to moderate scores (5-7)
4. **Context matters**: Adjust for competition constraints
5. **Auto-reject red flags**: Don't waste time on infeasible methods
6. **Provide top-k**: Return 6-10 methods for selection
7. **Include justifications**: Help @researcher understand rankings

### DON'T ❌

1. **Don't be random**: Scores must have rationale
2. **Don't ignore constraints**: 72 hours is real limit
3. **Don't overcomplicate**: Simple often beats complex
4. **Don't skip risk**: High-risk methods fail in competitions
5. **Don't be extreme**: 9-10 and 1-2 should be rare
6. **Don't play favorites**: Score objectively, not by preference
7. **Don't work alone**: Consult with @researcher if uncertain

---

## Metrics & Feedback

### Track Success

After each competition, evaluate:

**Method Selection Quality**:
- Did top-scoring methods work well?
- Were any high-scoring methods rejected? Why?
- Did any low-scoring methods succeed? Why?

**Time Savings**:
- How long did method selection take?
- Compared to manual search (baseline: 2-4 hours)?
- Was scoring rubric helpful?

**Agent Satisfaction**:
- Was @researcher satisfied with recommendations?
- Did @modeler find selected methods feasible?
- Any suggestions for improvement?

### Continuous Improvement

**Update rubric** based on feedback:
- Are dimensions appropriate?
- Are scoring criteria clear?
- Any missing dimensions?

**Track scoring accuracy**:
- Compare predicted scores vs. actual performance
- Identify systematic biases
- Adjust criteria accordingly

---

## References

- **Scoring Rubric**: `knowledge_library/method_scoring/scoring_rubric.md`
- **Usage Guide**: `knowledge_library/method_scoring/README.md`
- **Reference Implementation**: `tools/method_scorer.py`
- **Original Source**: MM_Assets_Export/retrieve_method/ (清华大学数学建模团队)

---

**Document Version**: 1.0
**Last Updated**: 2026-01-29
**Status**: Active
