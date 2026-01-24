# Protocol 25: Phase 11 - Self-Evolution

> **Version**: v3.1.0
> **Date**: 2026-01-24
> **Phase**: Phase 11 (New - Post-Submission)
> **Agent**: @director + @knowledge_librarian
> **Trigger**: After competition submission complete
> **Purpose**: Continuous improvement through automated scoring and feedback analysis

---

## Purpose

Implement **self-improving system** that learns from every competition to:
1. Automatically score papers using `mmbench_score.py`
2. Track protocol violations over time
3. Identify systematic weaknesses
4. Update ANTI_PATTERNS.md with new flaws
5. Refine agent prompts based on judgment data

**Core Philosophy**: "Every competition is training data for the system."

---

## When to Execute

**Trigger**: Competition submission complete (after Phase 10)

**Frequency**: Once per competition

**Timing**: Post-competition (after MCM/ICM results available)

---

## Process

### Step 1: Automated Paper Scoring

**Tool**: `tools/mmbench_score.py`

**Input**: `output/paper/paper.pdf`

**Process**:
1. Parse PDF text
2. Score against O-Prize criteria (0-100)
3. Generate detailed report
4. Extract common violations

**Output**: `output/docs/validation/automated_score.json`

**Scoring Categories**:
```json
{
  "abstract": {
    "score": 15,
    "max": 20,
    "issues": [
      "Only 2 quantitative metrics (require ≥3)",
      "No uncertainty quantification"
    ]
  },
  "figures": {
    "score": 8,
    "max": 15,
    "issues": [
      "Figure 1 caption non-descriptive",
      "Figure 3 missing error bars"
    ]
  },
  "methods": {
    "score": 18,
    "max": 20,
    "issues": []
  },
  "style": {
    "score": 12,
    "max": 20,
    "issues": [
      "Banned vocabulary: 'show' (3 times)",
      "Banned vocabulary: 'get' (1 time)"
    ]
  },
  "total_score": 53,
  "max_total": 100
}
```

---

### Step 2: Violation Tracking

**Agent**: @knowledge_librarian

**Task**: Aggregate violations across competitions

**Database**: `knowledge_library/evolution/violation_history.json`

**Structure**:
```json
{
  "competitions": [
    {
      "competition": "2025_C",
      "date": "2025-02-04",
      "automated_score": 53,
      "official_score": null,
      "violations": {
        "abstract_空洞": true,
        "banned_vocabulary": {
          "show": 3,
          "get": 1
        },
        "missing_uncertainty": true,
        "non_descriptive_captions": 2
      },
      "defcon_1_triggered": true,
      "defcon_1_duration": "2 hours 15 minutes"
    }
  ]
}
```

---

### Step 3: Pattern Identification

**Task**: Identify systematic weaknesses

**Analysis**:
1. **Recurring Violations**: Which flaws appear most often?
2. **Agent Attribution**: Which agents consistently cause issues?
3. **Protocol Effectiveness**: Which protocols prevent flaws?

**Output**: `knowledge_library/evolution/weakness_analysis.md`

**Template**:
```markdown
# Weakness Analysis: [Competition Year_Problem]

## Recurring Violations (Top 5)

### 1. Abstract空洞 (Frequency: 80%)
- **Responsible Agent**: @writer
- **Root Cause**: Not enforcing Protocol 14 strictly
- **Protocol Gap**: @validator doesn't check abstract numbers
- **Fix**: Add abstract validation to @validator checklist

### 2. Banned Vocabulary (Frequency: 60%)
- **Responsible Agent**: @writer, @editor
- **Root Cause**: style_guide.md not loaded as System Context
- **Protocol Gap**: No LINT ERROR for violations
- **Fix**: Implement automatic vocabulary checker in Phase 7.5

### 3. Missing Uncertainty (Frequency: 45%)
- **Responsible Agent**: @writer
- **Root Cause**: Not part of standard paper template
- **Protocol Gap**: No mandatory uncertainty section
- **Fix**: Add uncertainty to paper template

---

## Agent Performance

### @writer
- **Responsibility**: Paper generation
- **Violation Rate**: 35% (highest)
- **Common Issues**: Abstract空洞, banned vocabulary
- **Prompt Review Needed**: Yes (Phase 7)

### @visualizer
- **Responsibility**: Figure generation
- **Violation Rate**: 20%
- **Common Issues**: Non-descriptive captions
- **Prompt Review Needed**: Yes (Phase 6)

### @validator
- **Responsibility**: Result validation
- **Violation Rate**: 5% (lowest)
- **Common Issues**: None
- **Prompt Review Needed**: No

---

## Protocol Effectiveness

### Most Effective Protocols
1. **Protocol 1 (File Reporting)**: 0 violations related to file confusion
2. **Protocol 8 (Model Design Expectations)**: Clear model designs
3. **Protocol 11 (Emergency Delegation)**: No pipeline stalls

### Least Effective Protocols
1. **Protocol 14 (Style Alignment)**: 60% banned vocabulary violations
   - **Issue**: No automatic enforcement
   - **Fix**: Implement LINT ERROR system

2. **Protocol 15 (Interpretation)**: 40% non-descriptive captions
   - **Issue**: No automatic checking
   - **Fix**: Add caption validator

---

## Priority Actions

### High Priority (Fix Before Next Competition)
1. ✅ Add abstract validation to @validator (Protocol 14 enforcement)
2. ✅ Implement automatic vocabulary checker
3. ✅ Add uncertainty section to paper template

### Medium Priority (Improvements)
1. Enhance @visualizer caption template
2. Add caption validator to Phase 7.5
3. Improve @writer prompt for style compliance

### Low Priority (Nice to Have)
1. Create style checking tool
2. Add more banned vocabulary
3. Expand ANTI_PATTERNS.md
```

---

### Step 4: Update Knowledge Bases

**Agent**: @knowledge_librarian

**Task**: Update system knowledge based on learnings

#### 4.1 Update ANTI_PATTERNS.md

**Add**: New flaws discovered in this competition

**Example**:
```markdown
## New Flaws (Added 2025-02-04)

### Flaw #N: [Flaw Name]
- **Severity**: Fatal / Level 2 / Level 3
- **First Seen**: 2025_C
- **Frequency**: [N] times
- **Persona**: [A/B/C]
- **Description**: [What went wrong]
- **Example**: [Bad example]
- **Fix**: [How to prevent]
```

#### 4.2 Update style_guide.md

**Add**: New banned words based on violation data

**Example**:
```markdown
### Banned Words (Updated 2025-02-04)
- show → Use "demonstrate" (1200% more academic)
- get → Use "obtain" or "achieve"
- say → Use "state" or "posit"
- try → Use "attempt" or "endeavor" [NEW]
- basically → Remove filler word [NEW]
```

#### 4.3 Update Agent Prompts

**Task**: Revise agent prompts based on performance

**Example for @writer**:
```markdown
# Agent: @writer (Updated v3.1.1)

## System Context (CRITICAL - DO NOT MODIFY)
You MUST read and follow: knowledge_library/academic_writing/style_guide.md

**NEW IN v3.1.1**:
- Abstract MUST contain ≥3 numbers (auto-checked)
- All figure captions MUST be conclusionary (auto-checked)
- Banned vocabulary auto-detected → LINT ERROR

## Performance History (2025_C)
- Violations: 12 (abstract空洞, banned vocabulary)
- DEFCON 1 Triggered: Yes (2h 15m)
- Lesson Learned: Always include numbers in abstract
```

---

### Step 5: Meta-Learning Analysis

**Task**: Correlate automated scores with official MCM/ICM results

**Analysis**:
1. Compare `mmbench_score.py` output with official scores
2. Identify scoring biases (over/under-predicting)
3. Calibrate scoring formula

**Output**: `knowledge_library/evolution/scoring_calibration.md`

**Example**:
```markdown
# Scoring Calibration Analysis

## Competition: 2025_C

### Automated Score
- **mmbench_score.py**: 53/100
- **Components**:
  - Abstract: 15/20 (-5 for 2 metrics only)
  - Figures: 8/15 (-7 for captions)
  - Methods: 18/20 (-2 for no sensitivity)
  - Style: 12/20 (-8 for vocabulary)

### Official Result
- **MCM Score**: [Pending]
- **Rank**: [Pending]

### Correlation Analysis
[After official results released]

### Bias Detection
[Compare automated vs official scores]

### Calibration Updates
[Adjust scoring weights if needed]
```

---

## mmbench_score.py Implementation

### Complete Code

```python
#!/usr/bin/env python3
"""
MCM-Bench Automated Paper Scorer
Automatically scores MCM/ICM papers against O-Prize criteria
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

class MMBenchScorer:
    """Automated MCM/ICM paper scorer"""

    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)
        self.text = self._extract_text()
        self.score = 0
        self.max_score = 100
        self.issues = []

    def _extract_text(self) -> str:
        """Extract text from PDF"""
        try:
            import PyPDF2
            with open(self.pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error extracting PDF: {e}")
            return ""

    def score_abstract(self) -> Tuple[int, int, List[str]]:
        """Score abstract (20 points max)"""
        score = 0
        max_score = 20
        issues = []

        # Extract abstract
        abstract_match = re.search(
            r'Abstract\s*(.*?)(?=\n\s*\n|\n\s*Keywords?|\n\s*1\.|\n\s*Introduction)',
            self.text,
            re.DOTALL | re.IGNORECASE
        )

        if not abstract_match:
            return 0, max_score, ["Abstract not found"]

        abstract = abstract_match.group(1)

        # Check 1: Number of quantitative metrics
        numbers = re.findall(r'\d+\.?\d*', abstract)
        if len(numbers) >= 3:
            score += 10
        else:
            issues.append(f"Only {len(numbers)} quantitative metrics (require ≥3)")

        # Check 2: Uncertainty quantification
        uncertainty_patterns = [
            r'p\s*[<≤]\s*0\.05',
            r'95%\s*CIs?',
            r'confidence\s*interval',
            r'standard\s*error',
            r'±',
            r'\[\d+\.?\d*,\s*\d+\.?\d*\]'
        ]
        has_uncertainty = any(re.search(p, abstract, re.IGNORECASE) for p in uncertainty_patterns)
        if has_uncertainty:
            score += 5
        else:
            issues.append("No uncertainty quantification")

        # Check 3: Specific metrics (RMSE, R², AIC, BIC)
        metric_patterns = [
            r'RMSE\s*=\s*\d+\.?\d*',
            r'R²\s*=\s*\d+\.?\d*',
            r'AIC\s*=\s*\d+',
            r'BIC\s*=\s*\d+'
        ]
        has_metrics = any(re.search(p, abstract, re.IGNORECASE) for p in metric_patterns)
        if has_metrics:
            score += 5
        else:
            issues.append("No specific performance metrics (RMSE, R², etc.)")

        return score, max_score, issues

    def score_figures(self) -> Tuple[int, int, List[str]]:
        """Score figures (15 points max)"""
        score = 0
        max_score = 15
        issues = []

        # Extract figure captions
        figure_captions = re.findall(
            r'Figure\s+\d+[:\.]\s*(.*?)(?=Figure\s+\d+|\.|$)',
            self.text,
            re.DOTALL | re.IGNORECASE
        )

        if not figure_captions:
            return 0, max_score, ["No figures found"]

        for i, caption in enumerate(figure_captions, 1):
            caption_score = 0
            caption_issues = []

            # Check 1: Quantitative content
            if re.search(r'\d+', caption):
                caption_score += 2
            else:
                caption_issues.append(f"Figure {i}: No numbers")

            # Check 2: Conclusionary words
            conclusionary_words = [
                'indicates', 'suggests', 'demonstrates', 'shows',
                'reveals', 'implies', 'illustrates', 'exacerbates'
            ]
            has_conclusionary = any(word in caption.lower() for word in conclusionary_words)
            if has_conclusionary:
                caption_score += 3
            else:
                caption_issues.append(f"Figure {i}: Non-descriptive caption")

            # Check 3: Physical implication
            implication_words = [
                'due to', 'because', 'caused by', 'result of',
                'mechanism', 'effect', 'impact'
            ]
            has_implication = any(word in caption.lower() for word in implication_words)
            if has_implication:
                caption_score += 1

            score += caption_score
            issues.extend(caption_issues)

        # Cap at max_score
        score = min(score, max_score)

        return score, max_score, issues

    def score_methods(self) -> Tuple[int, int, List[str]]:
        """Score methods section (20 points max)"""
        score = 0
        max_score = 20
        issues = []

        # Check 1: Mathematical formulation
        math_patterns = [
            r'\\\\[\s\S]*?\\\\',  # LaTeX equations
            r'd\w+\s*/\s*dt\s*=',  # Differential equations
            r'∑',  # Summation
            r'∫'   # Integral
        ]
        has_math = any(re.search(p, self.text) for p in math_patterns)
        if has_math:
            score += 5

        # Check 2: Model assumptions
        assumptions = re.findall(
            r'(?:assumption|assume|assuming)\s*:?\s*.*',
            self.text,
            re.IGNORECASE
        )
        if len(assumptions) >= 3:
            score += 5
        else:
            issues.append(f"Only {len(assumptions)} explicit assumptions (recommend ≥3)")

        # Check 3: Justification
        justification_patterns = [
            r'we\s+(?:use|adopt|employ)\s+\w+\s+because',
            r'rationale',
            r'justif',
            r'motivat'
        ]
        has_justification = any(re.search(p, self.text, re.IGNORECASE) for p in justification_patterns)
        if has_justification:
            score += 5
        else:
            issues.append("No methodological justification")

        # Check 4: Sensitivity analysis
        sensitivity = re.search(
            r'sensitivity\s+analysis',
            self.text,
            re.IGNORECASE
        )
        if sensitivity:
            score += 5
        else:
            issues.append("No sensitivity analysis")

        return score, max_score, issues

    def score_style(self) -> Tuple[int, int, List[str]]:
        """Score writing style (20 points max)"""
        score = 0
        max_score = 20
        issues = []

        # Load style_guide.md for banned words
        style_guide_path = Path("knowledge_library/academic_writing/style_guide.md")
        banned_words = {
            'show': 3,
            'get': 2,
            'say': 2,
            'look at': 1,
            'put': 1
        }

        if style_guide_path.exists():
            # Parse banned words from style_guide.md
            with open(style_guide_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract banned words list
                banned_section = re.search(
                    r'###?\s*Banned\s+Words.*?(?=###|$)',
                    content,
                    re.DOTALL | re.IGNORECASE
                )
                if banned_section:
                    # Parse banned words
                    for line in banned_section.group(0).split('\n'):
                        match = re.match(r'-\s*(\w+)\s*→', line)
                        if match:
                            banned_words[match.group(1).lower()] = 3

        # Check for banned words
        violations = {}
        text_lower = self.text.lower()
        for word, penalty in banned_words.items():
            count = len(re.findall(rf'\b{re.escape(word)}\b', text_lower))
            if count > 0:
                violations[word] = count * penalty

        if violations:
            for word, points in violations.items():
                issues.append(f"Banned vocabulary: '{word}' (-{points} points)")
            score = max(0, 20 - sum(violations.values()))
        else:
            score = 20

        # Check for consistent notation
        # (Simplified check - in reality would be more complex)
        notation_patterns = [
            (r'\bS\b', 'Susceptible'),
            (r'\bI\b', 'Infected'),
            (r'\bR\b', 'Recovered')
        ]
        # This would require more sophisticated analysis

        return score, max_score, issues

    def score_completeness(self) -> Tuple[int, int, List[str]]:
        """Score paper completeness (25 points max)"""
        score = 0
        max_score = 25
        issues = []

        # Required sections
        required_sections = {
            'abstract': r'Abstract',
            'introduction': r'Introduction|1\.',
            'methods': r'(?:Methods?|Model|Methodology)',
            'results': r'(?:Results?|Analysis)',
            'discussion': r'(?:Discussion|Conclusions?)',
            'references': r'References?'
        }

        for section, pattern in required_sections.items():
            if re.search(pattern, self.text, re.IGNORECASE):
                score += 4
            else:
                issues.append(f"Missing section: {section.capitalize()}")

        # Check for references (≥10)
        references = re.findall(r'\[\d+\]', self.text)
        if len(references) >= 10:
            score += 1
        else:
            issues.append(f"Only {len(references)} references (recommend ≥10)")

        return min(score, max_score), max_score, issues

    def run_full_scoring(self) -> Dict:
        """Run complete scoring and return detailed report"""
        results = {
            'abstract': self._score_to_dict(*self.score_abstract()),
            'figures': self._score_to_dict(*self.score_figures()),
            'methods': self._score_to_dict(*self.score_methods()),
            'style': self._score_to_dict(*self.score_style()),
            'completeness': self._score_to_dict(*self.score_completeness())
        }

        total_score = sum(r['score'] for r in results.values())
        max_total = sum(r['max_score'] for r in results.values())

        results['total_score'] = total_score
        results['max_total'] = max_total
        results['percentage'] = (total_score / max_total) * 100 if max_total > 0 else 0

        # Flatten all issues
        all_issues = []
        for category, data in results.items():
            if category in ['total_score', 'max_total', 'percentage']:
                continue
            for issue in data.get('issues', []):
                all_issues.append(f"{category}: {issue}")

        results['all_issues'] = all_issues

        return results

    def _score_to_dict(self, score: int, max_score: int, issues: List[str]) -> Dict:
        """Convert score tuple to dictionary"""
        return {
            'score': score,
            'max_score': max_score,
            'issues': issues
        }

    def save_report(self, output_path: str):
        """Save scoring report to JSON file"""
        results = self.run_full_scoring()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)

        print(f"\n{'='*60}")
        print(f"MCM-BENCH AUTOMATED SCORING REPORT")
        print(f"{'='*60}")
        print(f"\nTotal Score: {results['total_score']}/{results['max_total']} ({results['percentage']:.1f}%)")
        print(f"\nBreakdown:")
        for category, data in results.items():
            if category in ['total_score', 'max_total', 'percentage', 'all_issues']:
                continue
            status = "✓" if data['score'] >= data['max_score'] * 0.7 else "✗"
            print(f"  {status} {category.capitalize()}: {data['score']}/{data['max_score']}")

        if results['all_issues']:
            print(f"\nIssues Found ({len(results['all_issues'])}):")
            for issue in results['all_issues']:
                print(f"  - {issue}")

        print(f"\n{'='*60}")
        print(f"Report saved to: {output_path}")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description='MCM-Bench Automated Paper Scorer')
    parser.add_argument('pdf_path', help='Path to paper PDF')
    parser.add_argument('-o', '--output', default='output/docs/validation/automated_score.json',
                       help='Output JSON path')
    args = parser.parse_args()

    scorer = MMBenchScorer(args.pdf_path)
    scorer.save_report(args.output)


if __name__ == '__main__':
    main()
```

---

## Quality Assurance

### Verification Checklist

After Phase 11 completion, verify:

- [ ] `mmbench_score.py` executed successfully
- [ ] `automated_score.json` generated
- [ ] Score breakdown calculated (all 5 categories)
- [ ] `violation_history.json` updated
- [ ] `weakness_analysis.md` generated
- [ ] ANTI_PATTERNS.md updated (if new flaws found)
- [ ] Agent prompts revised (if needed)
- [ ] `scoring_calibration.md` updated (if official results available)

---

## Dependencies

**Input**:
- `output/paper/paper.pdf`
- `knowledge_library/academic_writing/style_guide.md`
- `ANTI_PATTERNS.md`

**Tools**:
- `tools/mmbench_score.py`

**Output**:
- `output/docs/validation/automated_score.json`
- `knowledge_library/evolution/violation_history.json`
- `knowledge_library/evolution/weakness_analysis.md`
- `knowledge_library/evolution/scoring_calibration.md`

**Agents**: @director, @knowledge_librarian

---

## Impact

**Without Phase 11**:
- Same mistakes repeated every competition
- No systematic improvement
- Agent prompts never refined
- Weaknesses never addressed

**With Phase 11**:
- Every competition improves the system
- Agent prompts evolve based on performance
- System learns from mistakes
- Continuous quality improvement

**Value**: **Transforms one-time system into continuously improving AI.**

---

**Document Version**: v3.1.0
**Related Phases**: Phase 9.1 (Mock Judging), Phase 10 (Final Package)
**Related Protocols**: Protocol 13 (DEFCON 1), Protocol 14 (Style)
**Status**: Ready for Implementation
