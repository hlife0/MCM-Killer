# Method Scoring System

## Overview

Automated method selection using 5-dimensional evaluation framework adapted from MM_Assets_Export.

## Components

### 1. Scoring Rubric
**Location**: `knowledge_library/method_scoring/scoring_rubric.md`

Five-dimensional evaluation framework:
1. **Applicability** (适用性) - Problem fit
2. **Feasibility** (可行性) - Implementation practicality
3. **Cost/Efficiency** (成本/效率) - Resource requirements
4. **Risk** (风险) - Failure likelihood (inverted: higher = lower risk)
5. **Clarity** (清晰度) - Implementation clarity

Each dimension scored 0-10, total = average of all 5 dimensions.

### 2. Reference Implementation
**Location**: `tools/method_scorer.py`

Original implementation from MM_Assets_Export/retrieve_method/retrieve_method.py

**Key Features**:
- Hierarchical method tree processing
- Embedding-based semantic similarity scoring
- LLM-based 5-dimensional evaluation
- Parent-child weight propagation (default: 50/50)
- Top-k method selection

**Status**: Adapted for MCM-Killer architecture (dependencies removed)

### 3. Integration with HMML 2.0
**Location**: `knowledge_base/HMML_2.0/`

Method scorer queries HMML 2.0 index to retrieve candidate methods for evaluation.

## Usage

### For @knowledge_librarian

1. **Problem Analysis**: Parse problem description from @reader
2. **Method Retrieval**: Query HMML 2.0 for candidate methods
3. **Scoring**: Apply 5-dimensional rubric to each candidate
4. **Ranking**: Sort by total score, return top-k

### Manual Scoring Process

When evaluating methods manually:

1. **Problem**: "Predict Olympic medal counts based on GDP, population, and past performance"

2. **Candidates**:
   - Multiple Regression
   - Random Forest
   - Neural Network
   - Poisson Regression

3. **Scoring** (example for Multiple Regression):
   - Applicability: 9/10 (excellent for continuous prediction)
   - Feasibility: 8/10 (standard, widely available)
   - Cost/Efficiency: 9/10 (fast, simple)
   - Risk: 7/10 (well-established but assumptions)
   - Clarity: 9/10 (well-documented)
   - **Total: 8.4/10**

4. **Output**: Rank all methods by total score

## Scoring Guidelines

### Conservative Approach
When uncertain, use conservative scores:
- Risk: Default to 5-7 (moderate uncertainty)
- Feasibility: Assume 6-8 unless clearly proven
- Cost: Account for competition time pressure

### Context Matters
Adjust scoring based on competition constraints:
- **Time-limited** (72 hours): Penalize complex methods (Cost/Efficiency)
- **Data-poor**: Penalize data-intensive methods (Feasibility)
- **Team expertise**: Adjust Clarity based on team familiarity

### Red Flags
Auto-reject methods with:
- Applicability < 5: Wrong problem type
- Feasibility < 4: Impossible to implement
- Risk < 3: Experimental/unproven for competition

## Integration with Existing Workflow

### Phase 0.2: Knowledge Retrieval
```
@knowledge_librarian receives problem_description
  ↓
Query HMML 2.0 for relevant methods
  ↓
Score candidates using 5-dim rubric
  ↓
Return top-k methods (k=6-10) with scores
  ↓
@researcher uses scored list for method selection
```

### Handoff Format

**Input** (from @reader):
```
Problem: "Predict Olympic medal counts..."
Requirements: [list of requirements]
Constraints: [time, data, resources]
```

**Output** (to @researcher):
```markdown
# Top 6 Methods for Medal Count Prediction

## 1. Multiple Regression Analysis (Total: 8.4/10)
**Scores**: Applicability: 9.0, Feasibility: 8.0, Cost: 9.0, Risk: 7.0, Clarity: 9.0
**Rationale**: Excellent fit for prediction with continuous variables. Well-established method with low implementation complexity.

## 2. Random Forest (Total: 8.1/10)
**Scores**: Applicability: 8.5, Feasibility: 8.5, Cost: 7.5, Risk: 8.0, Clarity: 8.0
**Rationale**: Handles non-linear relationships well. Requires more tuning but robust.

[... 4 more methods ...]
```

## Dependencies

### Required
- HMML 2.0 index files: `knowledge_base/HMML_2.0/hmml_index.json`
- Scoring rubric: `knowledge_library/method_scoring/scoring_rubric.md`

### Optional (for automated scoring)
- Embedding model: sentence-transformers (for semantic similarity)
- LLM access: For automated 5-dimensional evaluation

## Migration Notes

### From MM_Assets_Export
**Source**: `retrieve_method/retrieve_method.py` (6.8KB)
**Changes**:
- Removed dependencies on MM_Assets codebase structure
- Updated HMML path references
- Extracted scoring rubric to separate markdown file
- Added CLI interface (optional)

### Preserved Features
- Hierarchical scoring with parent-child weights
- 5-dimensional evaluation framework
- Top-k selection logic
- Method ranking and formatting

## Troubleshooting

### Issue: Low scores for all methods
**Cause**: Rubric applied too strictly
**Fix**: Adjust thresholds, focus on relative ranking not absolute scores

### Issue: High-risk methods scoring well
**Cause**: Risk dimension underweighted
**Fix**: Increase risk weighting in total calculation, or apply risk veto

### Issue: Too many methods tied
**Cause**: Insufficient granularity in 0-10 scale
**Fix**: Use decimal scores (7.3, 7.5, 7.7) or add tie-breaker criteria

## Future Enhancements

- [ ] Add automated embedding-based scoring (requires sentence-transformers)
- [ ] Implement LLM-based evaluation (requires API access)
- [ ] Create CLI tool: `python tools/method_scorer.py --problem "..." --top_k 10`
- [ ] Add domain-specific weighting (e.g., risk more important for medical problems)
- [ ] Track scoring accuracy via feedback from competition results
