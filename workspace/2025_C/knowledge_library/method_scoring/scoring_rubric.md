# Method Scoring Rubric (5-Dimensional Evaluation)

## Translation from MM_Assets_Export/retrieve_method/中文自然语言.txt

## Overview

This rubric provides a structured framework for evaluating mathematical modeling methods against specific problem requirements. Each method is scored across 5 dimensions, with scores ranging from 0-10.

## Dimension 1: Applicability (适用性)

**Score 0-10**: How well does the method fit the problem type?

### Evaluation Criteria
- **9-10**: Perfect fit for problem domain and requirements
- **7-8**: Good fit with minor adjustments needed
- **5-6**: Moderate fit, some aspects not well-aligned
- **3-4**: Poor fit, major aspects incompatible
- **1-2**: Fundamentally unsuitable for this problem type

### Questions to Ask
- Does this method address the core problem?
- Are the problem assumptions compatible with method assumptions?
- Has this method been used successfully for similar problems?

## Dimension 2: Feasibility (可行性)

**Score 0-10**: Can this method be implemented under realistic constraints?

### Evaluation Criteria
- **9-10**: Highly feasible with standard tools and resources
- **7-8**: Feasible with reasonable effort and resources
- **5-6**: Moderately feasible, requires significant effort
- **3-4**: Challenging, may require specialized expertise or resources
- **1-2**: Impractical or impossible with available resources

### Questions to Ask
- Do we have the required data?
- Do we have the computational resources?
- Do we have the required expertise?
- Can it be implemented within the competition timeframe?

## Dimension 3: Cost/Efficiency (成本/效率)

**Score 0-10**: Is the method cost-effective in terms of time, resources, and complexity?

### Evaluation Criteria
- **9-10**: Very efficient, minimal resources, fast implementation
- **7-8**: Good efficiency, reasonable resource requirements
- **5-6**: Moderate efficiency, acceptable resource usage
- **3-4**: Low efficiency, high resource requirements
- **1-2**: Prohibitively expensive in time or resources

### Questions to Ask
- How long will implementation take?
- What computational resources are needed?
- How complex is the implementation?
- Are there simpler alternatives that achieve similar results?

## Dimension 4: Risk (风险)

**Score 0-10**: What is the likelihood of failure or adverse outcomes?
**Note**: Higher score = LOWER risk (less risky is better)

### Evaluation Criteria
- **9-10**: Very low risk, well-established method
- **7-8**: Low risk, minor uncertainties
- **5-6**: Moderate risk, some uncertainties
- **3-4**: High risk, major uncertainties or potential failures
- **1-2**: Very high risk, experimental or unproven approach

### Questions to Ask
- Is this method well-established or experimental?
- What are the common failure modes?
- How sensitive is the method to assumptions?
- What happens if the method fails?

## Dimension 5: Clarity (清晰度)

**Score 0-10**: Is the method well-defined with clear implementation steps?

### Evaluation Criteria
- **9-10**: Very clear, well-documented, step-by-step procedure available
- **7-8**: Clear, good documentation available
- **5-6**: Moderately clear, some ambiguity in implementation
- **3-4**: Unclear, limited guidance on implementation
- **1-2**: Very vague or poorly defined

### Questions to Ask
- Are the method steps clearly defined?
- Is there good documentation and examples?
- Are the parameters and settings well-specified?
- Is it clear how to validate results?

## Total Score Calculation

```
Total Score = (Applicability + Feasibility + Cost/Efficiency + Risk + Clarity) / 5
```

**Range**: 0-10, where higher scores indicate better methods

## Usage Instructions

### Step 1: Problem Analysis
Read the problem description carefully and identify:
- Problem type (optimization, prediction, evaluation, etc.)
- Data availability and quality
- Computational constraints
- Time constraints

### Step 2: Method Evaluation
For each candidate method:
1. Assess applicability to the problem
2. Evaluate feasibility under constraints
3. Consider cost/efficiency implications
4. Analyze potential risks
5. Judge clarity of implementation

### Step 3: Scoring
Assign scores (0-10) for each dimension based on the criteria above.

### Step 4: Ranking
Rank methods by total score and select top-k for detailed analysis.

## Example Scoring

**Problem**: Predict Olympic medal counts based on GDP, population, and past performance.

**Method**: Multiple Regression Analysis

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Applicability | 9.0 | Excellent for prediction with continuous variables |
| Feasibility | 8.0 | Standard statistical method, widely available |
| Cost/Efficiency | 9.0 | Fast to implement, low computational cost |
| Risk | 7.0 | Well-established, but assumptions may be violated |
| Clarity | 9.0 | Very clear, extensive documentation available |
| **Total** | **8.4** | **Recommended** |

## Integration with Agents

- **@knowledge_librarian**: Use this rubric when scoring methods
- **@researcher**: Reference scores when selecting methods
- **@modeler**: Consider risk and clarity when designing models
- **@advisor**: Review scoring rationale for quality assurance

## Notes

- Scores should be based on objective criteria, not personal preference
- Consider the specific competition context (time limits, available resources)
- When in doubt, be conservative with risk scores
- Document scoring rationale for transparency
