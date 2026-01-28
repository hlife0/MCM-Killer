# MCM-Killer Improvement Plan - Part 2: Agent Prompts & Configuration

**Date**: 2025-01-28
**Based On**: SYSTEM_COHERENCE_VALIDITY_REPORT_2025-01-28.md
**Assigned To**: Agent 2 (Agent Prompts & Config)
**Scope**: All improvements that modify `.claude/` directory
**Estimated Effort**: 18-22 hours

---

## 📋 Part 2 Scope

This document contains improvements that focus on **agent prompt refactoring and system configuration**. These improvements:

- ✅ Create new configs in `.claude/` directory
- ✅ Modify agent prompts in `.claude/agents/`
- ✅ Do NOT modify tools/ directory
- ✅ Can be executed in parallel with Part 1 (Tools & Infrastructure)

### Included Improvements

3. **Improvement #3**: VALUABLE Modular Prompts (MEDIUM) - 6-8 hours
4. **Improvement #4**: SafePlaceholder Pattern (MEDIUM) - 2-3 hours
5. **Improvement #5**: Event Tracking System (MEDIUM) - 10-11 hours

### Excluded Improvements

These are in Part 1 to avoid conflicts:
- Improvement #1: Phase Tracking (modifies tools/)
- Improvement #2: Orchestration Logging (modifies tools/)
- Improvement #6: Health Check (modifies tools/)
- Improvement #7: Progress Dashboard (modifies tools/)

---

## Executive Summary (Part 2)

### Expected Outcomes for Agent Prompts & Config

✅ 30-40% token reduction via Modular Prompts
✅ Robust error handling via SafePlaceholder Pattern
✅ Complete observability via Event Tracking System

### Estimated Effort Breakdown

- Improvement #3: 6-8 hours (modular prompt system)
- Improvement #4: 2-3 hours (SafePlaceholder pattern)
- Improvement #5: 10-11 hours (event tracking system)
- **Total**: 18-22 hours

---

## Part 2: MEDIUM-Priority Improvements (Sprint 2)

### Improvement #3: VALUABLE Modular Prompts

**Priority**: MEDIUM
**Effort**: 6-8 hours
**Risk**: LOW
**Impact**: 30-40% token reduction, improved maintainability

---

#### 3.1 Current State

**Problem**: Agent prompts use monolithic structure with duplicated context. From VALUABLE analysis:

**Current Issues**:
- Each agent prompt contains full system context (~2000-3000 tokens)
- Common sections duplicated across 17 agents
- Protocol explanations repeated everywhere
- Role definitions verbose and redundant

**Impact**:
- 3-5x higher token usage than necessary
- Slower agent initialization
- Higher API costs
- Difficult to maintain consistency

---

#### 3.2 Solution Design

**Approach**: Implement modular prompt system from VALUABLE framework:
1. Base system prompt (shared context)
2. Agent-specific modules (role, expertise, instructions)
3. Protocol modules (on-demand loading)
4. Prompt assembly tool
5. Migration strategy for existing agents

**Components**:
- `.claude/base_system_prompt.txt` - Shared foundation
- `.claude/agents/*_modular.txt` - Agent-specific modules (17 files)
- `tools/assemble_agent_prompt.py` - Assembly tool
- Migration script for existing agents

---

#### 3.3 Implementation Plan

**Step 1: Create Base System Prompt**

**File**: `workspace/2025_C/.claude/base_system_prompt.txt`

```
# MCM-Killer Base System Prompt

## System Identity

You are part of the MCM-Killer system, an autonomous AI-powered framework for solving mathematical modeling competitions (MCM/ICM).

**Project**: MCM-Killer v3.1.0
**Goal**: Win the O Prize (Outstanding Winner) in the 2025 MCM Competition

## Cognitive Narrative Framework

This system operates under the **v3.1.0 Cognitive Narrative Framework**, which structures problem-solving as a journey of discovery and refinement.

### Core Narrative Principles

1. **Iterative Discovery**: Progress through cycles of exploration, modeling, validation, and refinement
2. **Diverse Perspectives**: Consult multiple approaches before converging on solutions
3. **Evidence-Based Decisions**: Ground all decisions in data, literature, and validation
4. **Metacognitive Awareness**: Reflect on process, identify biases, and adapt strategies
5. **Quality Over Speed**: Prioritize thoroughness and correctness over rapid completion

### The Journey Phases

The workflow consists of 22 phases across 5 stages:

**Stage 1: Foundation** (Phases 0-2)
- Understanding the problem
- Researching methods
- Designing models

**Stage 2: Implementation** (Phases 3-5B)
- Building models
- Training systems
- Generating results

**Stage 3: Validation** (Phases 5.5-6)
- Evaluating performance
- Validating results
- Ensuring robustness

**Stage 4: Synthesis** (Phases 6.5-8)
- Creating visualizations
- Writing paper
- Self-reviewing

**Stage 5: Refinement** (Phases 9-11)
- Iterating on paper
- Polishing prose
- Finalizing submission

## Knowledge Library: HMML 2.0

This system has access to the **Hierarchical Mathematical Modeling Library (HMML) v2.0**, a comprehensive knowledge base containing:

- **Method Domain 1**: Time Series Analysis & Forecasting
- **Method Domain 2**: Machine Learning & Statistical Models
- **Method Domain 3**: Optimization & Operations Research
- **Method Domain 4**: Simulation & Monte Carlo Methods
- **Method Domain 5**: Network Analysis & Graph Theory
- **Method Domain 6**: Data Visualization & Communication

Query the knowledge library via @knowledge_librarian for relevant methods, examples, and best practices.

## Quality Standards: O Award Criteria

All work must meet **Outstanding Winner** standards:

1. **Clarity**: Executives must understand your paper after one reading
2. **Spelling & Grammar**: Perfect English, no errors
3. **Visualizations**: Professional, informative figures
4. **Mathematical Model**: Clearly explained, well-justified
5. **Results**: Validated, sensitivity analysis performed
6. **Strengths & Weaknesses**: Honest self-assessment

## Collaboration Protocol

You work alongside 17 other specialized agents. Coordinate via:

- **@director**: Orchestrates the overall workflow
- **@advisor**: Provides strategic guidance
- **@validator**: Ensures quality standards

When handing off work:
1. Clearly state what you've completed
2. Provide file paths to outputs
3. Highlight any issues or concerns
4. Suggest next steps

## Operating Principles

1. **Read Before Acting**: Always read existing files before creating new ones
2. **Think Before Writing**: Plan your approach before generating content
3. **Validate Before Submitting**: Check your work before marking complete
4. **Document Everything**: Explain your reasoning, assumptions, and decisions
5. **Ask For Help**: Consult @advisor or @validator when uncertain

## Error Handling

If you encounter issues:
1. Log the error via orchestration logger
2. Attempt to resolve or work around
3. Escalate to @advisor if blocking
4. Document the incident and resolution

---

*Base prompt loaded. Agent-specific instructions follow.*
```

---

**Step 2: Create Agent-Specific Modules**

**Example: @modeler Module**

**File**: `workspace/2025_C/.claude/agents/modeler_modular.txt`

```
# Agent: @modeler

## Role Identity

You are the **Model Design Specialist**, responsible for conceptualizing, designing, and specifying mathematical models for the competition problem.

## Expertise

- **Mathematical Modeling**: Translate real-world problems into mathematical formulations
- **Algorithm Selection**: Choose appropriate algorithms and techniques
- **Model Architecture**: Design model structures and component interactions
- **Trade-off Analysis**: Balance complexity, accuracy, and interpretability
- **Documentation**: Create clear model specifications for implementation

## Responsibilities

1. **Analyze Problem Requirements**: Extract key modeling objectives and constraints
2. **Research Methods**: Consult HMML 2.0 for relevant modeling approaches
3. **Design Candidates**: Create 3-6 candidate models with different approaches
4. **Specify Models**: Provide detailed specifications for each model (equations, algorithms, data flows)
5. **Compare Models**: Evaluate trade-offs and recommend primary/backup approaches
6. **Document Designs**: Create model_design_*.md files with complete specifications

## Input Sources

- Problem statement (from @reader)
- Research notes (from @researcher)
- Suggested methods (from @knowledge_librarian)
- Methodology evaluation (from @advisor/@validator)

## Output Artifacts

- `output/model_design_*.md` - Individual model specifications
- `output/model_selection_report.md` - Comparison and recommendation
- `output/model_comparison_matrix.md` - Trade-off analysis

## Key Protocols

Follow **PROTOCOL-1: Iterative Modeling**:
1. Start simple: Create baseline model
2. Add complexity incrementally
3. Validate at each step
4. Document rationale for design choices

Follow **PROTOCOL-5: Model Documentation**:
1. State assumptions clearly
2. Provide equations and algorithms
3. Explain data requirements
4. Define evaluation metrics
5. Discuss limitations and alternatives

## Decision Framework

When designing models, consider:

1. **Problem Fit**: Does the model address the core problem?
2. **Data Availability**: Do we have sufficient data for this approach?
3. **Complexity vs. Accuracy**: Is added complexity justified?
4. **Computational Feasibility**: Can we train/run this model in time?
5. **Interpretability**: Can we explain how the model works?
6. **Robustness**: Will the model generalize to new data?

## Common Tasks

**Task: Design Candidate Models**
1. Read problem statement and research notes
2. Query @knowledge_librarian for relevant methods
3. Design 3-6 models with diverse approaches
4. Specify each model completely
5. Compare and recommend
6. Output: model_design_1.md, model_design_2.md, ..., model_selection_report.md

**Task: Refine Model Architecture**
1. Review existing model designs
2. Identify weaknesses or limitations
3. Propose architectural improvements
4. Update specifications
5. Document changes and rationale

## Quality Checks

Before submitting model designs, verify:

- [ ] All models address the problem statement
- [ ] Models are mathematically sound
- [ ] Assumptions are clearly stated
- [ ] Equations/algorithms are specified
- [ ] Data requirements are defined
- [ ] Evaluation metrics are proposed
- [ ] Trade-offs are analyzed
- [ ] Recommendation is justified

## Collaboration Handoffs

**To @coder**: Provide model specifications with:
- Mathematical formulations
- Algorithm pseudocode
- Data structure requirements
- Expected inputs/outputs
- Performance targets

**From @researcher**: Expect:
- Problem understanding
- Key variables and constraints
- Domain-specific insights

**From @knowledge_librarian**: Expect:
- Relevant method suggestions
- Literature examples
- Best practices

---

*Agent module: @modeler*
*Ready for prompt assembly*
```

---

**Step 3: Create Prompt Assembly Tool**

**File**: `workspace/2025_C/tools/assemble_agent_prompt.py`

```python
#!/usr/bin/env python3
"""
Prompt Assembly Tool - Modular Prompt System

Assembles agent prompts from modular components to reduce token usage
and improve maintainability.

Usage:
    python tools/assemble_agent_prompt.py --agent modeler
    python tools/assemble_agent_prompt.py --all
    python tools/assemble_agent_prompt.py --migrate
"""

import os
from pathlib import Path
from typing import Dict, List, Optional
import argparse


class PromptAssembler:
    """Assemble modular prompts for agents."""

    def __init__(self, workspace_dir: str = None):
        """Initialize prompt assembler."""
        self.workspace_dir = Path(workspace_dir or os.getcwd())
        self.claude_dir = self.workspace_dir / ".claude"
        self.agents_dir = self.claude_dir / "agents"
        self.utils_dir = self.claude_dir / "utils"

        self.base_prompt_path = self.claude_dir / "base_system_prompt.txt"

    def load_base_prompt(self) -> str:
        """Load base system prompt."""
        if not self.base_prompt_path.exists():
            raise FileNotFoundError(f"Base prompt not found: {self.base_prompt_path}")

        with open(self.base_prompt_path, 'r', encoding='utf-8') as f:
            return f.read()

    def load_agent_module(self, agent_name: str) -> str:
        """Load agent-specific module."""
        module_path = self.agents_dir / f"{agent_name}_modular.txt"

        if not module_path.exists():
            raise FileNotFoundError(f"Agent module not found: {module_path}")

        with open(module_path, 'r', encoding='utf-8') as f:
            return f.read()

    def load_protocol_module(self, protocol_name: str) -> str:
        """Load protocol module."""
        protocol_path = self.utils_dir / "protocols" / f"{protocol_name}.txt"

        if not protocol_path.exists():
            return f"# Protocol: {protocol_name}\n# (Not yet implemented)\n"

        with open(protocol_path, 'r', encoding='utf-8') as f:
            return f.read()

    def assemble_prompt(self, agent_name: str,
                       include_protocols: List[str] = None) -> str:
        """Assemble complete prompt for agent."""
        # Load base prompt
        base_prompt = self.load_base_prompt()

        # Load agent module
        agent_module = self.load_agent_module(agent_name)

        # Load protocol modules (if specified)
        protocol_modules = []
        if include_protocols:
            for protocol in include_protocols:
                protocol_modules.append(self.load_protocol_module(protocol))

        # Assemble
        prompt_parts = [
            base_prompt,
            "\n" + "="*80 + "\n",
            agent_module
        ]

        if protocol_modules:
            prompt_parts.append("\n" + "="*80 + "\n")
            prompt_parts.append("# Relevant Protocols\n")
            prompt_parts.extend(protocol_modules)

        return "\n".join(prompt_parts)

    def save_prompt(self, agent_name: str, prompt: str):
        """Save assembled prompt to file."""
        output_path = self.agents_dir / f"{agent_name}.md"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(prompt)

        print(f"✅ Saved: {output_path}")

    def get_all_agents(self) -> List[str]:
        """Get list of all agents with modular modules."""
        if not self.agents_dir.exists():
            return []

        agents = []
        for file in self.agents_dir.glob("*_modular.txt"):
            agent_name = file.stem.replace("_modular", "")
            agents.append(agent_name)

        return sorted(agents)

    def count_tokens(self, text: str) -> int:
        """Estimate token count (rough approximation: 1 token ≈ 4 characters)."""
        return len(text) // 4

    def migrate_all_agents(self):
        """Migrate all agents to modular system."""
        agents = self.get_all_agents()

        if not agents:
            print("⚠️  No agent modules found")
            return

        print(f"🔄 Migrating {len(agents)} agents to modular prompt system...")

        total_old_tokens = 0
        total_new_tokens = 0

        for agent in agents:
            # Load existing monolithic prompt (if exists)
            old_prompt_path = self.agents_dir / f"{agent}.md"
            old_tokens = 0

            if old_prompt_path.exists():
                with open(old_prompt_path, 'r', encoding='utf-8') as f:
                    old_prompt = f.read()
                old_tokens = self.count_tokens(old_prompt)

            # Assemble new modular prompt
            new_prompt = self.assemble_prompt(agent)
            new_tokens = self.count_tokens(new_prompt)

            # Save new prompt
            self.save_prompt(agent, new_prompt)

            total_old_tokens += old_tokens
            total_new_tokens += new_tokens

            # Calculate savings
            if old_tokens > 0:
                savings = old_tokens - new_tokens
                percent = (savings / old_tokens) * 100
                print(f"  📉 {agent}: {old_tokens} → {new_tokens} tokens ({percent:.1f}% reduction)")

        # Summary
        if total_old_tokens > 0:
            total_savings = total_old_tokens - total_new_tokens
            total_percent = (total_savings / total_old_tokens) * 100
            print(f"\n📊 Summary:")
            print(f"  Total tokens: {total_old_tokens} → {total_new_tokens}")
            print(f"  Total savings: {total_savings} tokens ({total_percent:.1f}% reduction)")
            print(f"  Cost savings: ~${total_savings * 0.000003:.2f} per 1M calls")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="MCM-Killer Prompt Assembler")
    parser.add_argument("--workspace", type=str, default=None,
                       help="Workspace directory")
    parser.add_argument("--agent", type=str, metavar="NAME",
                       help="Assemble prompt for specific agent")
    parser.add_argument("--all", action="store_true",
                       help="Assemble prompts for all agents")
    parser.add_argument("--migrate", action="store_true",
                       help="Migrate all agents to modular system")

    args = parser.parse_args()

    assembler = PromptAssembler(args.workspace)

    if args.agent:
        prompt = assembler.assemble_prompt(args.agent)
        assembler.save_prompt(args.agent, prompt)
        print(f"\n📊 Token count: {assembler.count_tokens(prompt)}")
    elif args.all or args.migrate:
        assembler.migrate_all_agents()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

---

**Step 4: Migration Strategy**

**Create migration modules for all 17 agents**:

```bash
# Create agent modules
cd workspace/2025_C/.claude/agents

# For each agent, create *_modular.txt:
# - advisor_modular.txt
# - coder_modular.txt
# - consultant_modular.txt
# - data_analyst_modular.txt
# - director_modular.txt
# - figure_generator_modular.txt
# - judge_modular.txt
# - knowledge_librarian_modular.txt
# - mathematician_modular.txt
# - metacognition_agent_modular.txt
# - model_trainer_modular.txt
# - modeler_modular.txt
# - proofreader_modular.txt
# - reader_modular.txt
# - researcher_modular.txt
# - validator_modular.txt
# - writer_modular.txt
```

**Run migration**:

```bash
# Migrate all agents
python tools/assemble_agent_prompt.py --migrate
```

**Expected Output**:
```
🔄 Migrating 17 agents to modular prompt system...
  📉 advisor: 2800 → 1200 tokens (57.1% reduction)
  📉 coder: 2500 → 1100 tokens (56.0% reduction)
  📉 consultant: 2600 → 1150 tokens (55.8% reduction)
  ...
  📉 writer: 2700 → 1250 tokens (53.7% reduction)

📊 Summary:
  Total tokens: 44200 → 20400
  Total savings: 23800 tokens (53.8% reduction)
  Cost savings: ~$0.07 per 1M calls
```

---

#### 3.4 Testing Procedure

**Test 1: Assemble Single Agent**

```bash
python tools/assemble_agent_prompt.py --agent modeler
```

**Expected**: modeler.md created with assembled prompt

**Test 2: Verify Token Reduction**

```bash
# Before: Check existing agent prompt
wc -c .claude/agents/modeler.md

# After: Check modular prompt
wc -c .claude/agents/modeler.md

# Should be 50-60% smaller
```

**Test 3: Migrate All Agents**

```bash
python tools/assemble_agent_prompt.py --migrate
```

**Expected**: All 17 agents migrated with token savings reported

**Test 4: Validate Functionality**

```bash
# Test that agent still works
# In Claude Code context, invoke @modeler and verify it responds correctly
```

---

#### 3.5 Rollback Plan

**If issues occur**:

1. **Restore original prompts**:
```bash
git checkout .claude/agents/*.md
```

2. **Remove modular files**:
```bash
rm .claude/agents/*_modular.txt
rm .claude/base_system_prompt.txt
```

3. **Remove assembly tool**:
```bash
rm tools/assemble_agent_prompt.py
```

---

### Improvement #4: SafePlaceholder Pattern

**Priority**: MEDIUM
**Effort**: 2-3 hours
**Risk**: LOW
**Impact**: Prevents agent crashes from missing context

---

#### 4.1 Current State

**Problem**: Prompts use direct variable references that fail if context is missing.

**Example**:
```
Read the {{research_notes}} file and design models based on {{problem_constraints}}.
```

If `research_notes` or `problem_constraints` are not provided, agent may:
- Fail to understand instructions
- Generate incorrect outputs
- Crash or error out

---

#### 4.2 Solution Design

**Approach**: Implement SafePlaceholder pattern that:
1. Uses placeholder syntax for variables
2. Provides default values when context missing
3. Gracefully degrades functionality
4. Logs missing context for debugging

**Components**:
- `.claude/utils/safe_placeholder.py` - SafePlaceholder utility
- Integration with prompt assembly
- Placeholder naming conventions

---

#### 4.3 Implementation Plan

**Step 1: Create SafePlaceholder Utility**

**File**: `workspace/2025_C/.claude/utils/safe_placeholder.py`

```python
#!/usr/bin/env python3
"""
SafePlaceholder Pattern - Graceful Handling of Missing Context

Provides safe variable substitution with defaults and graceful degradation.

Usage:
    from safe_placeholder import SafePlaceholder

    template = "Read {{file:research_notes.md}} and design models for {{problem_type:prediction}}."
    context = {"file": "actual_notes.md"}  # problem_type missing
    result = SafePlaceholder.substitute(template, context)
    # Result: "Read actual_notes.md and design models for [prediction: DEFAULT - unknown problem type]."
"""


class SafePlaceholder:
    """Safe variable substitution with defaults."""

    # Default values for common placeholders
    DEFAULTS = {
        "research_notes": "[DEFAULT: Use problem statement directly]",
        "problem_constraints": "[DEFAULT: Extract constraints from problem statement]",
        "suggested_methods": "[DEFAULT: Research appropriate methods independently]",
        "model_designs": "[DEFAULT: Design models from scratch]",
        "features": "[DEFAULT: Perform feature engineering]",
        "training_data": "[DEFAULT: Use all available data]",
        "validation_results": "[DEFAULT: Perform validation]",
        "figures": "[DEFAULT: Create appropriate visualizations]",
        "paper_outline": "[DEFAULT: Follow standard structure]",
        "previous_draft": "[DEFAULT: Start fresh]"
    }

    @staticmethod
    def substitute(template: str, context: dict, strict: bool = False) -> str:
        """
        Substitute placeholders in template with context values.

        Args:
            template: String with {{placeholder}} or {{placeholder:default}} syntax
            context: Dictionary of variable names to values
            strict: If True, raise error on missing variables (default: False)

        Returns:
            String with placeholders substituted
        """
        import re

        # Find all placeholders
        pattern = r'\{\{(\w+)(?::([^}]+))?\}\}'
        matches = re.findall(pattern, template)

        result = template

        for var_name, default in matches:
            placeholder = f"{{{{{var_name}" + (f":{default}" if default else "") + "}}}}"

            if var_name in context and context[var_name]:
                # Use provided value
                result = result.replace(placeholder, str(context[var_name]))
            elif default:
                # Use template default
                result = result.replace(placeholder, default)
            elif var_name in SafePlaceholder.DEFAULTS:
                # Use global default
                result = result.replace(placeholder, SafePlaceholder.DEFAULTS[var_name])
            elif strict:
                raise ValueError(f"Missing required variable: {var_name}")
            else:
                # Graceful degradation
                result = result.replace(placeholder, f"[MISSING: {var_name}]")

        return result

    @staticmethod
    def validate_context(template: str, context: dict) -> dict:
        """
        Validate context against template requirements.

        Returns:
            Dictionary with 'valid', 'missing', 'optional' keys
        """
        import re

        pattern = r'\{\{(\w+)(?::([^}]+))?\}\}'
        matches = re.findall(pattern, template)

        required = set()
        optional = set()

        for var_name, default in matches:
            if default or var_name in SafePlaceholder.DEFAULTS:
                optional.add(var_name)
            else:
                required.add(var_name)

        missing = required - set(context.keys())

        return {
            "valid": len(missing) == 0,
            "missing": sorted(missing),
            "optional": sorted(optional),
            "total_required": len(required),
            "total_provided": len(set(context.keys()) & required)
        }

    @staticmethod
    def extract_placeholders(template: str) -> list:
        """Extract all placeholder names from template."""
        import re

        pattern = r'\{\{(\w+)(?::([^}]+))?\}\}'
        matches = re.findall(pattern, template)

        return [(var_name, bool(default) or var_name in SafePlaceholder.DEFAULTS)
                for var_name, default in matches]


def demo():
    """Demonstrate SafePlaceholder usage."""
    template = """
    Task: Design models for the problem

    Context:
    - Problem: {{problem_type:unknown}}
    - Research: {{research_notes}}
    - Methods: {{suggested_methods}}

    Deliverable: {{output_file:model_design.md}}
    """

    # Test 1: Complete context
    print("Test 1: Complete context")
    context = {
        "problem_type": "time series prediction",
        "research_notes": "notes.md",
        "suggested_methods": "LSTM, XGBoost",
        "output_file": "design.md"
    }
    result = SafePlaceholder.substitute(template, context)
    print(result)
    print()

    # Test 2: Missing context
    print("Test 2: Missing context (graceful degradation)")
    context = {
        "problem_type": "time series prediction",
        "output_file": "design.md"
        # research_notes and suggested_methods missing
    }
    result = SafePlaceholder.substitute(template, context)
    print(result)
    print()

    # Test 3: Validate
    print("Test 3: Validation")
    validation = SafePlaceholder.validate_context(template, context)
    print(f"Valid: {validation['valid']}")
    print(f"Missing: {validation['missing']}")
    print(f"Optional: {validation['optional']}")
    print()


if __name__ == "__main__":
    demo()
```

---

**Step 2: Integration with Agent Prompts**

**Update agent modules to use SafePlaceholder syntax**:

**Example: @modeler module**:

```
## Common Tasks

**Task: Design Candidate Models**
1. Read {{research_notes:problem statement}} for understanding
2. Query @knowledge_librarian for {{suggested_methods:relevant methods}}
3. Design models based on {{problem_constraints:extracted from problem}}
4. Output: {{output_files:model_design_*.md}}
```

**Step 3: Update CLAUDE.md with Context Injection**

**Add to CLAUDE.md** (before Phase sections):

```markdown
## Context Injection Protocol

When invoking agents, provide context using this format:

```python
context = {
    "research_notes": "output/research_notes.md",
    "problem_constraints": "Extract from 2025_Problem_C_Data/problem.pdf",
    "suggested_methods": "output/suggested_methods.md",
    "model_designs": "output/model_design_*.md",
    # ... other context variables
}
```

SafePlaceholder will:
- ✅ Use provided values when available
- ⚠️ Use defaults when missing (graceful degradation)
- ❌ Log missing variables for debugging
```

---

#### 4.4 Testing Procedure

**Test 1: Basic Substitution**

```bash
python .claude/utils/safe_placeholder.py
```

**Expected**: Demo output showing substitution with complete and missing context

**Test 2: Validation**

```python
from safe_placeholder import SafePlaceholder

template = "Read {{file}} and create {{output:default.md}}"
context = {"file": "input.txt"}

validation = SafePlaceholder.validate_context(template, context)
print(validation)
# Expected: {'valid': True, 'missing': [], 'optional': ['output'], ...}
```

**Test 3: Agent Prompt with Placeholders**

```bash
# Invoke agent with missing context
# Agent should use defaults instead of crashing
```

---

#### 4.5 Rollback Plan

**If issues occur**:

1. **Remove SafePlaceholder**:
```bash
rm .claude/utils/safe_placeholder.py
```

2. **Revert prompt changes**:
```bash
git checkout .claude/agents/*_modular.txt
```

---

### Improvement #5: Event Tracking System

**Priority**: MEDIUM
**Effort**: 4-5 hours
**Risk**: LOW
**Impact**: Structured logging for analysis and debugging

---

#### 5.1 Current State

**Problem**: No structured event logging for:
- Agent actions
- Decision rationale
- Error occurrences
- Output generation

**Impact**:
- Difficult to analyze workflow
- Cannot debug issues effectively
- No historical record for learning

---

#### 5.2 Solution Design

**Approach**: Implement event tracking system with:
1. Structured event logging (JSONL format)
2. Event types: action, decision, error, output
3. Event analysis tool
4. Timeline reconstruction

**Components**:
- `.claude/utils/event_tracker.py` - EventTracker class
- `tools/analyze_events.py` - Event analysis tool
- `output/docs/events/*.jsonl` - Event logs

---

#### 5.3 Implementation Plan

**Step 1: Create Event Tracker**

**File**: `workspace/2025_C/.claude/utils/event_tracker.py`

```python
#!/usr/bin/env python3
"""
Event Tracking System - Structured Logging

Logs all system events in structured JSONL format for analysis and debugging.

Usage:
    from event_tracker import EventTracker

    tracker = EventTracker()
    tracker.log_action("@modeler", "Designed LSTM model", {"model_type": "LSTM"})
    tracker.log_decision("Selected ensemble approach", "High diversity needed")
    tracker.log_error("Missing file", "data.csv", {"recovery": "Used backup"})
    tracker.log_output("@modeler", "model_design_1.md", {"size": "2.5KB"})
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class Event:
    """Structured event data."""
    timestamp: str
    event_type: str  # action, decision, error, output
    phase: Optional[str]
    agent: Optional[str]
    description: str
    details: Dict[str, Any]

    def to_json(self) -> str:
        """Convert to JSON string."""
        return json.dumps(asdict(self), ensure_ascii=False)


class EventTracker:
    """Structured event tracking system."""

    def __init__(self, workspace_dir: str = None):
        """Initialize event tracker."""
        self.workspace_dir = Path(workspace_dir or os.getcwd())
        self.events_dir = self.workspace_dir / "output" / "docs" / "events"
        self.events_dir.mkdir(parents=True, exist_ok=True)

        # Use date-based log files
        today = datetime.now().strftime("%Y-%m-%d")
        self.log_file = self.events_dir / f"events_{today}.jsonl"

        self.current_phase = None

    def set_phase(self, phase_id: str):
        """Set current phase context."""
        self.current_phase = phase_id

    def log_action(self, agent: str, description: str, details: Dict = None):
        """Log agent action."""
        event = Event(
            timestamp=datetime.now().isoformat(),
            event_type="action",
            phase=self.current_phase,
            agent=agent,
            description=description,
            details=details or {}
        )
        self._write_event(event)

    def log_decision(self, description: str, rationale: str,
                    alternatives: List[str] = None, details: Dict = None):
        """Log decision."""
        event_details = {
            "rationale": rationale,
            "alternatives": alternatives or [],
            **(details or {})
        }
        event = Event(
            timestamp=datetime.now().isoformat(),
            event_type="decision",
            phase=self.current_phase,
            agent=None,
            description=description,
            details=event_details
        )
        self._write_event(event)

    def log_error(self, error_type: str, message: str,
                 resolution: str = None, details: Dict = None):
        """Log error."""
        event_details = {
            "error_type": error_type,
            "message": message,
            "resolution": resolution,
            **(details or {})
        }
        event = Event(
            timestamp=datetime.now().isoformat(),
            event_type="error",
            phase=self.current_phase,
            agent=None,
            description=f"Error: {error_type}",
            details=event_details
        )
        self._write_event(event)

    def log_output(self, agent: str, output_path: str, details: Dict = None):
        """Log output generation."""
        event_details = {
            "output_path": output_path,
            **(details or {})
        }
        event = Event(
            timestamp=datetime.now().isoformat(),
            event_type="output",
            phase=self.current_phase,
            agent=agent,
            description=f"Generated {output_path}",
            details=event_details
        )
        self._write_event(event)

    def _write_event(self, event: Event):
        """Write event to log file."""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(event.to_json() + '\n')

    def get_events(self, event_type: str = None, phase: str = None,
                   agent: str = None) -> List[Event]:
        """Retrieve filtered events."""
        events = []

        if not self.log_file.exists():
            return events

        with open(self.log_file, 'r', encoding='utf-8') as f:
            for line in f:
                data = json.loads(line.strip())

                # Apply filters
                if event_type and data['event_type'] != event_type:
                    continue
                if phase and data['phase'] != phase:
                    continue
                if agent and data['agent'] != agent:
                    continue

                events.append(Event(**data))

        return events

    def get_timeline(self) -> List[Dict]:
        """Get chronological timeline of events."""
        events = self.get_events()
        timeline = []

        for event in events:
            timeline.append({
                "time": event.timestamp,
                "type": event.event_type,
                "phase": event.phase,
                "agent": event.agent,
                "description": event.description,
                "details": event.details
            })

        return sorted(timeline, key=lambda x: x['time'])

    def get_summary(self) -> Dict:
        """Get event summary statistics."""
        events = self.get_events()

        summary = {
            "total_events": len(events),
            "by_type": {},
            "by_phase": {},
            "by_agent": {},
            "errors": len([e for e in events if e.event_type == "error"]),
            "decisions": len([e for e in events if e.event_type == "decision"])
        }

        for event in events:
            # Count by type
            summary["by_type"][event.event_type] = summary["by_type"].get(event.event_type, 0) + 1

            # Count by phase
            if event.phase:
                summary["by_phase"][event.phase] = summary["by_phase"].get(event.phase, 0) + 1

            # Count by agent
            if event.agent:
                summary["by_agent"][event.agent] = summary["by_agent"].get(event.agent, 0) + 1

        return summary


def demo():
    """Demonstrate event tracker usage."""
    tracker = EventTracker()

    # Set phase
    tracker.set_phase("1")

    # Log action
    tracker.log_action("@modeler", "Designed LSTM model", {
        "model_type": "LSTM",
        "layers": 3,
        "units": 128
    })

    # Log decision
    tracker.log_decision(
        "Selected LSTM as primary model",
        "Proven effectiveness on time series",
        ["Transformer", "Prophet"]
    )

    # Log output
    tracker.log_output("@modeler", "output/model_design_1.md", {
        "size": "2.5KB",
        "models": 6
    })

    # Log error
    tracker.log_error(
        "Missing template",
        "model_template.md not found",
        "Used custom template"
    )

    # Get summary
    summary = tracker.get_summary()
    print("Event Summary:")
    print(json.dumps(summary, indent=2))

    # Get timeline
    timeline = tracker.get_timeline()
    print("\nTimeline:")
    for event in timeline:
        print(f"  {event['time']}: {event['description']}")


if __name__ == "__main__":
    demo()
```

---

**Step 2: Create Event Analysis Tool**

**File**: `workspace/2025_C/tools/analyze_events.py`

```python
#!/usr/bin/env python3
"""
Event Analysis Tool - Analyze Event Logs

Analyzes event logs to generate insights and reports.

Usage:
    python tools/analyze_events.py --summary
    python tools/analyze_events.py --timeline
    python tools/analyze_events.py --actions
    python tools/analyze_events.py --decisions
    python tools/analyze_events.py --errors
    python tools/analyze_events.py --agent @modeler
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
import sys

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent.parent / ".claude" / "utils"))
from event_tracker import EventTracker


def print_summary(tracker: EventTracker):
    """Print event summary."""
    summary = tracker.get_summary()

    print("\n" + "="*60)
    print("Event Summary")
    print("="*60)
    print(f"Total Events: {summary['total_events']}")
    print(f"Decisions: {summary['decisions']}")
    print(f"Errors: {summary['errors']}")

    print("\nBy Type:")
    for event_type, count in sorted(summary['by_type'].items(), key=lambda x: -x[1]):
        print(f"  {event_type}: {count}")

    print("\nBy Phase:")
    for phase, count in sorted(summary['by_phase'].items(), key=lambda x: float(x[0]) if x[0] != 'None' else 0):
        print(f"  Phase {phase}: {count}")

    print("\nBy Agent:")
    for agent, count in sorted(summary['by_agent'].items(), key=lambda x: -x[1]):
        print(f"  {agent}: {count}")

    print("="*60 + "\n")


def print_timeline(tracker: EventTracker):
    """Print chronological timeline."""
    timeline = tracker.get_timeline()

    print("\n" + "="*60)
    print("Event Timeline")
    print("="*60)

    for event in timeline:
        time = datetime.fromisoformat(event['time']).strftime("%H:%M:%S")
        phase = f"Phase {event['phase']}" if event['phase'] else "No Phase"
        agent = f"@{event['agent']}" if event['agent'] else "System"
        desc = event['description']

        print(f"{time} [{phase}] {agent}: {desc}")

    print("="*60 + "\n")


def print_actions(tracker: EventTracker):
    """Print all actions."""
    actions = tracker.get_events(event_type="action")

    print("\n" + "="*60)
    print(f"Agent Actions ({len(actions)} total)")
    print("="*60)

    for action in actions:
        time = datetime.fromisoformat(action.timestamp).strftime("%H:%M:%S")
        print(f"\n[{time}] {action.agent}: {action.description}")
        if action.details:
            for key, value in action.details.items():
                print(f"  - {key}: {value}")

    print("="*60 + "\n")


def print_decisions(tracker: EventTracker):
    """Print all decisions."""
    decisions = tracker.get_events(event_type="decision")

    print("\n" + "="*60)
    print(f"Decisions ({len(decisions)} total)")
    print("="*60)

    for decision in decisions:
        time = datetime.fromisoformat(decision.timestamp).strftime("%H:%M:%S")
        print(f"\n[{time}] Phase {decision.phase}: {decision.description}")
        print(f"  Rationale: {decision.details.get('rationale', 'N/A')}")

        alternatives = decision.details.get('alternatives', [])
        if alternatives:
            print(f"  Alternatives: {', '.join(alternatives)}")

    print("="*60 + "\n")


def print_errors(tracker: EventTracker):
    """Print all errors."""
    errors = tracker.get_events(event_type="error")

    print("\n" + "="*60)
    print(f"Errors ({len(errors)} total)")
    print("="*60)

    for error in errors:
        time = datetime.fromisoformat(error.timestamp).strftime("%H:%M:%S")
        print(f"\n[{time}] Phase {error.phase}: {error.description}")
        print(f"  Error Type: {error.details.get('error_type', 'N/A')}")
        print(f"  Message: {error.details.get('message', 'N/A')}")
        print(f"  Resolution: {error.details.get('resolution', 'None')}")

    print("="*60 + "\n")


def print_agent_activity(tracker: EventTracker, agent: str):
    """Print activity for specific agent."""
    events = tracker.get_events(agent=agent)

    print("\n" + "="*60)
    print(f"Activity for {agent} ({len(events)} events)")
    print("="*60)

    # Group by event type
    by_type = defaultdict(list)
    for event in events:
        by_type[event.event_type].append(event)

    for event_type, type_events in sorted(by_type.items()):
        print(f"\n{event_type.upper()} ({len(type_events)})")
        for event in type_events:
            time = datetime.fromisoformat(event.timestamp).strftime("%H:%M:%S")
            print(f"  [{time}] {event.description}")

    print("="*60 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="MCM-Killer Event Analyzer")
    parser.add_argument("--workspace", type=str, default=None,
                       help="Workspace directory")
    parser.add_argument("--summary", action="store_true",
                       help="Show event summary")
    parser.add_argument("--timeline", action="store_true",
                       help="Show chronological timeline")
    parser.add_argument("--actions", action="store_true",
                       help="Show all actions")
    parser.add_argument("--decisions", action="store_true",
                       help="Show all decisions")
    parser.add_argument("--errors", action="store_true",
                       help="Show all errors")
    parser.add_argument("--agent", type=str, metavar="NAME",
                       help="Show activity for specific agent")

    args = parser.parse_args()

    tracker = EventTracker(args.workspace)

    if args.summary:
        print_summary(tracker)
    elif args.timeline:
        print_timeline(tracker)
    elif args.actions:
        print_actions(tracker)
    elif args.decisions:
        print_decisions(tracker)
    elif args.errors:
        print_errors(tracker)
    elif args.agent:
        print_agent_activity(tracker, args.agent)
    else:
        # Default: show summary
        print_summary(tracker)


if __name__ == "__main__":
    main()
```

---

**Step 3: Integration with Agents**

**Add to agent modules**:

```
## Event Tracking

When performing significant actions, log events:

```python
from event_tracker import EventTracker

tracker = EventTracker()
tracker.set_phase("1")
tracker.log_action("@modeler", "Designed LSTM model", {"model_type": "LSTM"})
tracker.log_decision("Selected LSTM", "Best for time series", ["Transformer", "XGBoost"])
tracker.log_output("@modeler", "output/model_design_1.md", {"models": 6})
```
```

---

#### 5.4 Testing Procedure

**Test 1: Log Events**

```bash
python .claude/utils/event_tracker.py
```

**Expected**: Demo events logged to JSONL file

**Test 2: Analyze Events**

```bash
python tools/analyze_events.py --summary
python tools/analyze_events.py --timeline
python tools/analyze_events.py --decisions
```

**Expected**: Structured output of events

**Test 3: Filter by Agent**

```bash
python tools/analyze_events.py --agent @modeler
```

**Expected**: Only @modeler events shown

---

#### 5.5 Rollback Plan

**If issues occur**:

1. **Remove event tracking**:
```bash
rm .claude/utils/event_tracker.py
rm tools/analyze_events.py
rm -rf output/docs/events/
```

2. **Remove from agent modules**:
```bash
git checkout .claude/agents/*_modular.txt
```

---


## Part 4: Implementation Roadmap

### Sprint 1: Foundation (Week 1) - 8-10 hours

**Goal**: Establish observability and tracking infrastructure

**Tasks**:
1. ✅ Create `tools/phase_tracker.py` (2-3 hours)
2. ✅ Enhance `VERSION_MANIFEST.json` schema (0.5 hours)
3. ✅ Update `CLAUDE.md` with tracking commands (0.5 hours)
4. ✅ Create `tools/orchestration_logger.py` (3-4 hours)
5. ✅ Initialize `output/docs/orchestration_log.md` (0.5 hours)
6. ✅ Test tracking and logging (1 hour)

**Deliverables**:
- Automated phase tracking
- Complete orchestration logging
- Decision audit trail
- Timeline analysis capability

**Success Criteria**:
- ✅ Phase tracker detects completed phases
- ✅ VERSION_MANIFEST.json auto-updates
- ✅ Orchestration log records all agent executions
- ✅ All decisions logged with rationale
- ✅ No breaking changes to existing workflow

---

### Sprint 2: Optimization (Week 2-3) - 18-22 hours

**Goal**: Reduce token usage and improve robustness

**Tasks**:
1. ✅ Create `.claude/base_system_prompt.txt` (1-2 hours)
2. ✅ Create agent modules for 17 agents (6-8 hours)
3. ✅ Create `tools/assemble_agent_prompt.py` (2-3 hours)
4. ✅ Migrate all agents to modular system (2-3 hours)
5. ✅ Create `.claude/utils/safe_placeholder.py` (2-3 hours)
6. ✅ Create `.claude/utils/event_tracker.py` (2-3 hours)
7. ✅ Create `tools/analyze_events.py` (1-2 hours)
8. ✅ Test modular prompts and event tracking (2 hours)

**Deliverables**:
- 30-40% token reduction
- SafePlaceholder pattern implemented
- Event tracking system operational
- All agents migrated to modular prompts

**Success Criteria**:
- ✅ Token usage reduced by 30-40%
- ✅ No agent crashes from missing context
- ✅ All events logged and analyzable
- ✅ All agents functional with modular prompts
- ✅ SafePlaceholder working correctly

---

### Sprint 3: Enhancement (Week 4+) - 27-35 hours

**Goal**: Add health checks and monitoring capabilities

**Tasks**:
1. ✅ Create `tools/system_health_check.py` (4-5 hours)
2. ✅ Create `tools/progress_dashboard.py` (8-10 hours)
3. ✅ Write unit tests for critical components (10-15 hours)
4. ✅ Integration testing (5 hours)
5. ✅ Documentation updates (2-3 hours)
6. ✅ Final validation (2-3 hours)

**Deliverables**:
- Automated health validation
- Real-time progress monitoring
- Comprehensive test coverage
- Complete documentation

**Success Criteria**:
- ✅ Health check passes all validations
- ✅ Dashboard displays correct status
- ✅ Unit tests cover critical components
- ✅ System fully operational
- ✅ Documentation updated

---

## Part 5: Risk Management

### Risk Matrix

| Improvement | Risk Level | Probability | Impact | Mitigation |
|-------------|------------|-------------|--------|------------|
| **Phase Tracking** | LOW | Low | Low | Reversible, manual fallback |
| **Orchestration Logging** | LOW | Low | Low | Optional, can disable |
| **Modular Prompts** | LOW | Medium | Medium | Test on 1 agent first, rollback plan |
| **SafePlaceholder** | LOW | Low | Low | Backward compatible |
| **Event Tracking** | LOW | Low | Low | Optional, no impact if disabled |
| **Health Check** | LOW | Low | Low | Informational only |
| **Progress Dashboard** | LOW | Low | Low | Nice-to-have, optional |

**Overall Risk**: **LOW**

All improvements are:
- **Non-breaking**: Can be disabled without affecting core functionality
- **Reversible**: Can rollback to previous state
- **Optional**: Enhancements, not fixes
- **Tested**: Validation procedures included

### Risk Mitigation Strategies

1. **Incremental Implementation**
   - Start with Sprint 1 (lowest risk)
   - Test thoroughly before proceeding
   - Monitor for issues

2. **Backup Plans**
   - Git version control for rollback
   - Documented rollback procedures
   - Keep original files until migration complete

3. **Validation Gates**
   - Test after each improvement
   - Verify functionality before proceeding
   - Stop if critical issues found

4. **Monitoring**
   - Watch for agent errors
   - Monitor token usage
   - Check performance metrics

---

## Part 6: Success Metrics

### Sprint 1 Metrics

**Phase Tracking**:
- ✅ VERSION_MANIFEST.json auto-updates after each phase
- ✅ Progress percentage accurate
- ✅ Resume capability functional
- ✅ No manual intervention required

**Orchestration Logging**:
- ✅ All agent executions logged
- ✅ All decisions recorded with rationale
- ✅ Timeline analysis functional
- ✅ Error logging operational

**Overall**:
- ✅ Zero breaking changes
- ✅ Existing workflow unchanged
- ✅ New capabilities available

---

### Sprint 2 Metrics

**Modular Prompts**:
- ✅ Token usage reduced by 30-40%
- ✅ All agents functional
- ✅ Prompt assembly fast (< 1 second)
- ✅ Maintenance easier

**SafePlaceholder**:
- ✅ No agent crashes from missing context
- ✅ Defaults appropriate
- ✅ Missing variables logged
- ✅ Graceful degradation working

**Event Tracking**:
- ✅ All events logged to JSONL
- ✅ Analysis tool functional
- ✅ Timeline reconstruction works
- ✅ Filtering by agent/phase/type works

**Overall**:
- ✅ Cost reduction achieved
- ✅ Robustness improved
- ✅ Observability enhanced

---

### Sprint 3 Metrics

**Health Check**:
- ✅ All 7 categories validated
- ✅ Execution time < 30 seconds
- ✅ Issues correctly identified
- ✅ Fix suggestions helpful

**Progress Dashboard**:
- ✅ Real-time updates working
- ✅ Progress bar accurate
- ✅ Agent activity displayed
- ✅ Watch mode functional

**Testing**:
- ✅ Unit tests pass
- ✅ Integration tests pass
- ✅ Coverage > 80% for critical code
- ✅ No regressions

**Overall**:
- ✅ System fully validated
- ✅ Monitoring operational
- ✅ Documentation complete

---

## Part 7: Conclusion

### Summary

This improvement plan provides **comprehensive, step-by-step implementation guidance** for all recommended improvements from the System Coherence & Validity Report.

**Key Points**:

1. **Sprint 1** (8-10 hours): Phase tracking + Orchestration logging
   - Highest impact, lowest risk
   - Enables all future improvements
   - Foundation for observability

2. **Sprint 2** (18-22 hours): Modular prompts + Robustness
   - 30-40% token cost reduction
   - Prevents agent crashes
   - Enhanced event tracking

3. **Sprint 3** (27-35 hours): Health checks + Monitoring
   - Nice-to-have features
   - Comprehensive testing
   - Production hardening

### Expected Benefits

**Immediate (Sprint 1)**:
- Automated progress tracking
- Complete decision audit trail
- Timeline analysis capability
- Enhanced debugging support

**Short-term (Sprint 2)**:
- 30-40% reduction in token costs
- Improved agent robustness
- Better error handling
- Enhanced observability

**Long-term (Sprint 3)**:
- Pre-flight validation
- Real-time monitoring
- Comprehensive testing
- Production readiness

### Recommendation

**Start with Sprint 1 before next competition**

**Reasoning**:
- **Highest Impact**: Enables observability and tracking
- **Lowest Risk**: Simple tools, easy to test
- **Fastest Implementation**: 8-10 hours total
- **Foundation**: Enables all other improvements

**Expected Benefits**:
- Automated progress tracking
- Complete decision audit trail
- Timeline analysis capability
- Debugging support

### Next Steps

1. ✅ **Review this plan** - Understand all improvements
2. ✅ **Approve Sprint 1** - Get stakeholder buy-in
3. ✅ **Begin Implementation** - Start with Phase Tracking Automation
4. ✅ **Test Thoroughly** - Validate each improvement
5. ✅ **Proceed to Sprint 2** - After Sprint 1 validated
6. ✅ **Consider Sprint 3** - Based on available time

---

**Plan Created**: 2025-01-28
**Based On**: SYSTEM_COHERENCE_VALIDITY_REPORT_2025-01-28.md
**Confidence Level**: HIGH
**Risk Assessment**: LOW
**Recommendation**: **APPROVED for implementation**

---

## Appendix A: File Structure

### New Files (Sprint 1)

```
workspace/2025_C/
├── tools/
│   ├── phase_tracker.py              # Phase tracking automation
│   └── orchestration_logger.py       # Orchestration logging
├── output/
│   └── docs/
│       └── orchestration_log.md      # Orchestration log
└── VERSION_MANIFEST.json             # Enhanced schema
```

### New Files (Sprint 2)

```
workspace/2025_C/
├── .claude/
│   ├── base_system_prompt.txt        # Shared system prompt
│   ├── agents/
│   │   ├── advisor_modular.txt       # Agent modules (17 files)
│   │   ├── coder_modular.txt
│   │   ├── ...
│   │   └── writer_modular.txt
│   └── utils/
│       ├── safe_placeholder.py       # SafePlaceholder utility
│       └── event_tracker.py          # Event tracking
├── tools/
│   ├── assemble_agent_prompt.py      # Prompt assembly
│   └── analyze_events.py             # Event analysis
└── output/
    └── docs/
        └── events/
            └── events_YYYY-MM-DD.jsonl  # Event logs
```

### New Files (Sprint 3)

```
workspace/2025_C/
├── tools/
│   ├── system_health_check.py        # Health validation
│   └── progress_dashboard.py         # Progress monitoring
└── tests/
    ├── test_phase_tracker.py         # Unit tests
    ├── test_orchestration_logger.py
    ├── test_event_tracker.py
    └── ...
```

---

## Appendix B: Command Reference

### Phase Tracking Commands

```bash
# Check status
python tools/phase_tracker.py --check

# Update manifest
python tools/phase_tracker.py --update

# Validate phase
python tools/phase_tracker.py --validate 5B

# Get resume point
python tools/phase_tracker.py --resume
```

### Orchestration Logging Commands

```bash
# Start phase
python tools/orchestration_logger.py --start-phase 1 "Model Design"

# Log agent
python tools/orchestration_logger.py --log-agent "@modeler" "Design model" "input.md"

# Log decision
python tools/orchestration_logger.py --log-decision "Selected LSTM" "Best for time series"

# Log error
python tools/orchestration_logger.py --log-error "Missing file" "Recovered from backup"

# End phase
python tools/orchestration_logger.py --end-phase 1

# Analyze log
python tools/orchestration_logger.py --analyze
```

### Prompt Assembly Commands

```bash
# Assemble single agent
python tools/assemble_agent_prompt.py --agent modeler

# Assemble all agents
python tools/assemble_agent_prompt.py --all

# Migrate to modular system
python tools/assemble_agent_prompt.py --migrate
```

### Event Analysis Commands

```bash
# Show summary
python tools/analyze_events.py --summary

# Show timeline
python tools/analyze_events.py --timeline

# Show actions
python tools/analyze_events.py --actions

# Show decisions
python tools/analyze_events.py --decisions

# Show errors
python tools/analyze_events.py --errors

# Filter by agent
python tools/analyze_events.py --agent @modeler
```

### Health Check Commands

```bash
# Full health check
python tools/system_health_check.py

# Quick check
python tools/system_health_check.py --quick

# Check specific category
python tools/system_health_check.py --category agents
```

### Dashboard Commands

```bash
# Display dashboard once
python tools/progress_dashboard.py

# Watch mode (auto-refresh)
python tools/progress_dashboard.py --watch

# Custom refresh interval
python tools/progress_dashboard.py --watch --interval 60
```

---

## Appendix C: Testing Checklist

### Sprint 1 Testing

- [ ] Phase tracker detects completed phases
- [ ] VERSION_MANIFEST.json updates correctly
- [ ] Resume point accurate
- [ ] Orchestration log initializes
- [ ] Agent invocations logged
- [ ] Decisions recorded with rationale
- [ ] Errors logged with resolution
- [ ] Timeline analysis works
- [ ] No breaking changes to workflow

### Sprint 2 Testing

- [ ] Base system prompt loads
- [ ] All 17 agent modules created
- [ ] Prompt assembly functional
- [ ] Token reduction achieved (30-40%)
- [ ] All agents work with modular prompts
- [ ] SafePlaceholder substitutes correctly
- [ ] Missing variables handled gracefully
- [ ] Event tracker logs all events
- [ ] Event analysis tool functional
- [ ] Timeline reconstruction works

### Sprint 3 Testing

- [ ] Health check validates all categories
- [ ] Execution time < 30 seconds
- [ ] Issues correctly identified
- [ ] Dashboard displays correctly
- [ ] Watch mode updates
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] No regressions
- [ ] Documentation accurate

---

**END OF DETAILED IMPROVEMENT PLAN**
