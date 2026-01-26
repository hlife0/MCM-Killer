# Testing Guide: v3.1.0 (m-orientation)

> **Target**: MCM-Killer v3.1.0
> **Testing Strategy**: Unit → Integration → End-to-End
> **Coverage Goal**: ≥80% for Python tools

---

## Testing Philosophy

### Principles

1. **Test Tools First**: Python tools are critical infrastructure
2. **Agent Tests are Manual**: LLM behavior tested via scenarios
3. **Integration Over Unit**: Ensure components work together
4. **Real Data Preferred**: Use actual O-Prize papers when possible

---

## Unit Tests (Python Tools)

### Test Framework

```bash
# Install testing dependencies
pip install pytest pytest-cov pytest-mock

# Run all unit tests
pytest tests/unit/ -v

# Run with coverage
pytest tests/unit/ --cov=tools/ --cov-report=html
```

---

### Tool 1: init_workspace.py

**Test File**: `tests/unit/test_init_workspace.py`

```python
import pytest
import os
from tools.init_workspace import create_workspace, generate_version_manifest

def test_create_workspace(tmp_path):
    """Test workspace creation."""
    workspace_path = tmp_path / "test_workspace"
    create_workspace(str(workspace_path))

    # Verify directories exist
    assert (workspace_path / "output" / "docs" / "insights").exists()
    assert (workspace_path / "knowledge_library" / "methods").exists()
    assert (workspace_path / "agents").exists()

def test_version_manifest(tmp_path):
    """Test VERSION_MANIFEST.json generation."""
    output = tmp_path / "VERSION_MANIFEST.json"
    generate_version_manifest(str(output))

    import json
    with open(output) as f:
        manifest = json.load(f)

    assert manifest['version'] == '3.1.0'
    assert 'phases' in manifest
    assert len(manifest['phases']) >= 15  # Should have all phases
```

**Run**:
```bash
pytest tests/unit/test_init_workspace.py -v
```

---

### Tool 2: migrate_hmml.py

**Test File**: `tests/unit/test_migrate_hmml.py`

```python
import pytest
from tools.migrate_hmml import classify_domain, estimate_complexity, parse_method

def test_classify_domain():
    """Test domain classification."""
    text = "This method solves epidemic spread on networks using SIR dynamics"
    domain, category = classify_domain(text)

    assert domain == 'differential_equations'
    assert category == 'epidemic'

def test_estimate_complexity():
    """Test complexity estimation."""
    # Long method with many equations
    long_method = "\\n".join(["$$equation$$"] * 20) + "\\n" * 200
    complexity = estimate_complexity(long_method)

    assert complexity in ['Very High', 'High']

    # Short method
    short_method = "Simple method\\n" * 10
    complexity = estimate_complexity(short_method)

    assert complexity in ['Medium', 'Low']

def test_parse_method():
    """Test method parsing."""
    sample_md = """
    # SIR Model

    The basic SIR model is...

    ## Equations
    $$dS/dt = -\\beta SI$$
    """

    method = parse_method(sample_md)

    assert method['name'] == 'SIR Model'
    assert 'equations' in method['content'].lower()
```

**Run**:
```bash
pytest tests/unit/test_migrate_hmml.py -v
```

---

### Tool 3: style_analyzer.py

**Test File**: `tests/unit/test_style_analyzer.py`

```python
import pytest
from tools.style_analyzer import extract_verbs, count_numbers_in_abstract, analyze_sentences

def test_extract_verbs():
    """Test verb extraction."""
    text = "We demonstrate that the model reveals significant patterns."
    verbs = extract_verbs(text)

    assert 'demonstrate' in verbs
    assert 'reveals' in verbs

def test_count_numbers():
    """Test abstract number counting."""
    abstract = "Our model achieves RMSE=4.2, R²=0.89 (p<0.001), with 95% CI."
    count = count_numbers_in_abstract(abstract)

    assert count >= 3  # Should detect 4.2, 0.89, 0.001, 95

def test_sentence_patterns():
    """Test Observation-Implication detection."""
    sentence = "RMSE=4.2 (Observation), indicating model accuracy (Implication)."
    pattern = analyze_sentences([sentence])

    assert pattern['has_observation']
    assert pattern['has_implication']
```

**Run**:
```bash
pytest tests/unit/test_style_analyzer.py -v
```

---

### Tool 4: log_analyzer.py

**Test File**: `tests/unit/test_log_analyzer.py`

```python
import pytest
from tools.log_analyzer import parse_log, calculate_oscillation_score, detect_struggles

def test_parse_log():
    """Test log parsing."""
    sample_log = """
    Epoch 1/100 - Loss: 0.5
    Epoch 2/100 - Loss: 0.45
    Epoch 50/100 - Loss: 0.35
    Epoch 51/100 - Loss: 0.50
    Epoch 52/100 - Loss: 0.33
    """

    data = parse_log(sample_log)

    assert 'epochs' in data
    assert 'losses' in data
    assert len(data['epochs']) == 5

def test_oscillation_score():
    """Test oscillation detection."""
    # Oscillating loss
    losses = [0.5, 0.3, 0.6, 0.2, 0.7, 0.1, 0.8]
    score = calculate_oscillation_score(losses)

    assert score > 0.1  # High oscillation

    # Smooth loss
    smooth_losses = [0.5, 0.48, 0.46, 0.44, 0.42]
    smooth_score = calculate_oscillation_score(smooth_losses)

    assert smooth_score < 0.05  # Low oscillation

def test_detect_struggles():
    """Test struggle detection."""
    log_data = {
        'losses': [0.5, 0.3, float('inf'), 0.2],
        'gradients': [0.1, 0.2, 1e6, 0.15]
    }

    struggles = detect_struggles(log_data)

    assert len(struggles) > 0
    assert any('gradient explosion' in s.lower() for s in struggles)
```

**Run**:
```bash
pytest tests/unit/test_log_analyzer.py -v
```

---

### Tool 5: mmbench_score.py

**Test File**: `tests/unit/test_mmbench_score.py`

```python
import pytest
from tools.mmbench_score import check_memo, check_sensitivity, check_abstract, calculate_score

def test_check_memo():
    """Test memo existence check."""
    paper_with_memo = "...Summary for Policymakers: We recommend..."
    assert check_memo(paper_with_memo) == True

    paper_without = "Introduction\\nResults\\n"
    assert check_memo(paper_without) == False

def test_check_abstract():
    """Test abstract number counting."""
    good_abstract = "RMSE=4.2, R²=0.89, p<0.001, 95% CI"
    assert check_abstract(good_abstract)['passed'] == True

    bad_abstract = "Our model performs well"
    assert check_abstract(bad_abstract)['passed'] == False

def test_calculate_score():
    """Test final score calculation."""
    checks = {
        'memo': True,
        'sensitivity': True,
        'abstract': True,
        'code': False,
        'uncertainty': True,
        'captions': True,
        'diagrams': True,
        'narrative': True,
        'docs': True
    }

    score = calculate_score(checks)

    assert 80 <= score <= 95  # Should lose points for missing code
```

**Run**:
```bash
pytest tests/unit/test_mmbench_score.py -v
```

---

## Integration Tests

### Test 1: HMML 2.0 Migration Pipeline

**Test File**: `tests/integration/test_hmml_pipeline.py`

```python
def test_full_hmml_migration(tmp_path):
    """Test complete HMML migration."""
    # 1. Create sample HMML.md
    input_file = tmp_path / "HMML.md"
    input_file.write_text("""
    # SIR Model
    Basic compartmental model...

    # Genetic Algorithm
    Optimization heuristic...
    """)

    # 2. Run migration
    output_dir = tmp_path / "methods"
    from tools.migrate_hmml import migrate_hmml
    migrate_hmml(str(input_file), str(output_dir))

    # 3. Verify structure
    assert (output_dir / "differential_equations" / "epidemic" / "sir_basic.md").exists()
    assert (output_dir / "optimization" / "heuristics" / "genetic_algorithm.md").exists()

    # 4. Verify index
    index_file = tmp_path / "index.md"
    assert index_file.exists()

    # 5. Verify JSON
    json_file = tmp_path / "hmml_summary.json"
    import json
    with open(json_file) as f:
        summary = json.load(f)

    assert summary['total_methods'] >= 2
```

**Run**:
```bash
pytest tests/integration/test_hmml_pipeline.py -v
```

---

### Test 2: Narrative Arc Generation

**Test File**: `tests/integration/test_narrative_pipeline.py`

```python
def test_narrative_arc_generation(tmp_path):
    """Test Phase 5.8 narrative arc generation."""
    # 1. Create sample training log
    log_file = tmp_path / "training.log"
    log_file.write_text("""
    Epoch 1: Loss=0.5
    Epoch 50: Loss=inf - Gradient explosion!
    Epoch 51: Loss=0.3 - Fixed with gradient clipping
    """)

    # 2. Run log analyzer
    from tools.log_analyzer import analyze_log
    summary = analyze_log(str(log_file))

    # 3. Create dev diary
    diary_file = tmp_path / "dev_diary_1.md"
    diary_file.write_text("""
    ## Struggle: Gradient Explosion
    Symptom: Loss became inf at epoch 50
    Fix: Added gradient clipping
    Why: Variables interact multiplicatively
    """)

    # 4. Verify summary has struggles
    assert len(summary['struggles']) > 0
    assert 'gradient explosion' in str(summary['struggles']).lower()

    # Manual step: Run @metacognition_agent with inputs
    # Expected output: narrative_arc_1.md with insight about multiplicative interaction
```

**Run**:
```bash
pytest tests/integration/test_narrative_pipeline.py -v
```

---

### Test 3: Mock Judging Pipeline

**Test File**: `tests/integration/test_judging_pipeline.py`

```python
def test_mock_judging_flow(tmp_path):
    """Test Phase 9.1 → Protocol 13 flow."""
    # 1. Create bad paper (abstract空洞)
    paper_file = tmp_path / "paper.tex"
    paper_file.write_text("""
    \\begin{document}
    \\begin{abstract}
    Our model performs well and provides insights.
    \\end{abstract}
    \\end{document}
    """)

    # 2. Run automated scoring
    from tools.mmbench_score import score_paper
    result = score_paper(str(paper_file))

    # 3. Verify REJECT
    assert result['score'] < 70
    assert not result['checks']['abstract']

    # 4. Verify Kill List generation
    assert len(result['issues']) > 0
    assert any('abstract' in issue.lower() for issue in result['issues'])

    # Manual step: @judge_zero should issue REJECT
    # Manual step: Protocol 13 should activate
```

**Run**:
```bash
pytest tests/integration/test_judging_pipeline.py -v
```

---

## End-to-End Tests

### E2E Test: Complete Competition Simulation

**Test Scenario**: 2024 Problem C (Epidemic Spread)

**Test File**: `tests/e2e/test_problem_c_2024.py`

```python
def test_problem_c_full_pipeline(tmp_path):
    """Simulate complete pipeline for 2024 Problem C."""

    # Pre-Competition: Style Generation (skip - use pre-generated)

    # Phase 0: Problem Reading
    problem_file = "tests/fixtures/2024_problem_c.pdf"
    # Manual: @reader extracts requirements

    # Phase 0.2: Method Recommendation
    # Manual: @knowledge_librarian recommends SIR-Network
    # Expected: SIR-Network rated ⭐⭐⭐⭐⭐

    # Phase 2-4: Research & Modeling (skip)

    # Phase 5: Training
    training_log = tmp_path / "training.log"
    # Simulate training with struggles

    # Phase 5.8: Insight Extraction
    from tools.log_analyzer import analyze_log
    summary = analyze_log(str(training_log))
    # Expected: narrative_arc.md generated

    # Phase 7: Paper Writing
    # Manual: @narrative_weaver → @writer
    # Expected: paper.tex with Hero's Journey structure

    # Phase 9.1: Mock Judging
    from tools.mmbench_score import score_paper
    # Expected: Score ≥ 95 (PASS)

    # Phase 9.5: Submission
    # Success criteria met
```

**Run**:
```bash
pytest tests/e2e/test_problem_c_2024.py -v --slow
```

---

## Agent Testing (Manual Scenarios)

Since agents are LLM-based, testing uses scenario validation.

### Scenario 1: @metacognition_agent

**Input**:
- `logs/summary.json` with gradient explosion
- `dev_diary.md` with multiplicative interaction hypothesis

**Expected Output**:
- `narrative_arc.md` contains:
  - Observation: Gradient explosion at epoch 50
  - Mechanism: Multiplicative variable interaction
  - Implication: Need log-transform
  - No "bug fixing" language

**Validation**:
```bash
# Check for required elements
grep "gradient explosion" output/docs/insights/narrative_arc_1.md
grep "multiplicative" output/docs/insights/narrative_arc_1.md
! grep -i "bug" output/docs/insights/narrative_arc_1.md  # Should NOT contain "bug"
```

---

### Scenario 2: @narrative_weaver

**Input**:
- `narrative_arc_1.md` with Hero's Journey structure

**Expected Output**:
- `paper_outline.md` with:
  - Red thread sentence
  - Section 3.3 matches "The Revelation" from narrative arc
  - All figure captions use Observation-Implication

**Validation**:
```bash
# Check structure
grep "Red Thread" output/docs/requirements/paper_outline.md
grep "Section 3.3" output/docs/requirements/paper_outline.md

# Check Protocol 15 compliance
grep "indicating\\|demonstrating\\|revealing" output/docs/requirements/paper_outline.md | wc -l
# Should be > 5 (multiple O-I patterns)
```

---

### Scenario 3: @judge_zero

**Input**:
- Paper with abstract空洞 (0 numbers)

**Expected Output**:
- `judgment_report.md` with:
  - Verdict: REJECT
  - Score < 70
  - Persona C flags abstract issue
  - Kill List contains specific fix

**Validation**:
```bash
# Check verdict
grep "REJECT" output/docs/validation/judgment_report.md

# Check score
SCORE=$(grep "Score:" output/docs/validation/judgment_report.md | grep -oP '\\d+')
test $SCORE -lt 70

# Check Kill List
grep "Abstract空洞" output/docs/validation/judgment_report.md
```

---

## Performance Tests

### Benchmark Suite

```bash
# Run performance benchmarks
pytest tests/performance/ -v --benchmark-only
```

**Test File**: `tests/performance/test_tool_performance.py`

```python
import pytest

def test_log_analyzer_performance(benchmark, tmp_path):
    """Benchmark log analyzer on 1GB log."""
    # Generate large log file
    log_file = tmp_path / "large.log"
    # ... generate 1GB of log data

    from tools.log_analyzer import analyze_log
    result = benchmark(analyze_log, str(log_file))

    # Should complete in < 60 seconds
    assert benchmark.stats['mean'] < 60

def test_hmml_search_performance(benchmark):
    """Benchmark HMML keyword search."""
    from tools.hmml_search import search_methods
    result = benchmark(search_methods, keywords=['bayesian', 'epidemic'])

    # Should complete in < 2 seconds
    assert benchmark.stats['mean'] < 2
```

---

## Continuous Integration

### GitHub Actions Workflow

Create `.github/workflows/test.yml`:

```yaml
name: v3.1.0 Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov pytest-benchmark

    - name: Run unit tests
      run: pytest tests/unit/ -v --cov=tools/

    - name: Run integration tests
      run: pytest tests/integration/ -v

    - name: Upload coverage
      uses: codecov/codecov-action@v2
```

---

## Test Coverage Goals

| Component | Target Coverage | Acceptance |
|-----------|----------------|------------|
| Python Tools | 90% | ≥80% |
| Agents (manual scenarios) | 100% scenarios | ≥80% |
| Integration Tests | All critical paths | All pass |
| E2E Tests | 1 complete scenario | Passes |

---

## Version History

- **v1.0** (2026-01-25): Initial testing guide from plan
