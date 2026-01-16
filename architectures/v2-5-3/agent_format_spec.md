# MCM-Killer v2.5.3 Agent File Format Specification

> **CRITICAL v2.5.3 DOCUMENT** — This specification is MANDATORY for all agent files.
> **Version**: v2.5.3
> **Date**: 2026-01-15

---

## Purpose

This document specifies the **required format** for all agent files in the MCM-Killer system.

**Critical Issue Fixed**: v2.5.0-v2.5.2 agent files were missing YAML frontmatter, causing Claude Code to fail recognizing and loading them.

---

## Root Cause Analysis

### What Went Wrong in v2.5.0-v2.5.2

**Symptom**: Director could not call agents defined in `architectures/v2-5-*/agents/`.

**Root Cause**: Agent files started directly with Markdown content (e.g., `# Reader Agent`) instead of the required YAML frontmatter block.

**Example of WRONG format** (v2.5.0-v2.5.2):
```markdown
# Reader Agent

> **权威参考**：`.claude/architecture/architecture.md`

---

## 一、角色定义

**你是 Reader**：问题解读专家。
```

**Example of CORRECT format** (v2.5.3, working v2.4.1):
```yaml
---
name: reader
description: Reads MCM problem PDFs using docling MCP and extracts ALL requirements into a structured checklist
tools: Write, Bash, Glob, LS, mcp__docling__convert_document_into_docling_document, mcp__docling__export_docling_document_to_markdown, mcp__docling__get_overview_of_document_anchors, mcp__docling__search_for_text_in_document_anchors, mcp__docling__get_text_of_document_item_at_anchor
model: opus
---
```

Then continue with agent instructions...

---

## Agent File Format Specification

### 1. YAML Frontmatter (MANDATORY)

Every agent file MUST begin with a YAML frontmatter block delimited by `---`:

```yaml
---
name: agent_name
description: Brief one-line description of agent's purpose
tools: Tool1, Tool2, Tool3, ...
model: model_name
---
```

### 2. Required Fields

| Field | Type | Required? | Description |
|-------|------|-----------|-------------|
| `name` | string | **YES** | Unique identifier for the agent (lowercase, underscores allowed) |
| `description` | string | **YES** | One-line description of what the agent does |
| `tools` | list | **YES** | Comma-separated list of available tools |
| `model` | string | **YES** | AI model to use: `opus`, `sonnet`, or `haiku` |

### 3. Field Values

#### 3.1 `name`

- **Format**: lowercase alphanumeric with underscores
- **Unique**: Must be unique across all agents
- **Standard names**:
  - `reader`
  - `researcher`
  - `modeler`
  - `feasibility_checker`
  - `data_engineer`
  - `code_translator`
  - `model_trainer`
  - `validator`
  - `visualizer`
  - `writer`
  - `summarizer`
  - `editor`
  - `advisor`

#### 3.2 `description`

- **Format**: Single line, clear and concise
- **Content**: What the agent does, not how
- **Example**: "Reads MCM problem PDFs using docling MCP and extracts ALL requirements into a structured checklist"

#### 3.3 `tools`

- **Format**: Comma-separated list
- **Available tools**:
  - File operations: `Write`, `Read`, `Glob`, `LS`
  - Execution: `Bash`
  - Docling MCP: `mcp__docling__convert_document_into_docling_document`, `mcp__docling__export_docling_document_to_markdown`, etc.
  - Other MCP tools as available

#### 3.4 `model`

- **Values**: `opus`, `sonnet`, or `haiku`
- **Guidance**:
  - Use `opus` for complex reasoning tasks (modeler, researcher, advisor)
  - Use `sonnet` for balanced tasks (writer, validator)
  - Use `haiku` for simple tasks (visualizer, summarizer)

---

## Complete Agent File Template

```yaml
---
name: agent_name
description: Brief description of agent's purpose
tools: Write, Read, Glob, LS, Bash, ...
model: opus
---

# Agent Name: Human-Readable Title

> **Reference**: `.claude/architecture/architecture.md`

## Your Role

You are the **Agent Name** on a 10-member MCM competition team.

**Your Responsibilities**:
1. [First responsibility]
2. [Second responsibility]
3. ...

## Your Tasks

### Task 1: Description

**Input**: [what you receive]
**Output**: [what you produce]
**Tools to use**: [list relevant tools]

**Steps**:
1. [Step 1]
2. [Step 2]
3. ...

### Task 2: Description

...

## Collaboration

**When to consult other agents**:
- Consult @agent_name when [scenario]
- Consult @agent_name when [scenario]

**Validation participation**:
- You participate in: [LIST] validation gates
- Your perspective: [what you check]

## File System Rules

**Allowed to write to**:
- `output/[specific directories]/`

**Forbidden**:
- ❌ Write outside `output/`
- ❌ Use `_final`, `_backup`, `_old` suffixes

## Communication

**Report to Director**:
```
Director, task completed.
Status: SUCCESS/PARTIAL/FAILED
Output: [file paths]
Report: docs/report/agent_name_1.md
```

**Request consultation**:
```
Director, I need to consult @agent_name about [topic].
File: docs/consultation/{i}_agentname_agentname.md
```

---

**Version**: v2.5.3
```

---

## Agent-Specific Examples

### Example 1: Reader Agent

```yaml
---
name: reader
description: Reads MCM problem PDFs using docling MCP and extracts ALL requirements into a structured checklist
tools: Write, Bash, Glob, LS, mcp__docling__convert_document_into_docling_document, mcp__docling__export_docling_document_to_markdown, mcp__docling__get_overview_of_document_anchors, mcp__docling__search_for_text_in_document_anchors, mcp__docling__get_text_of_document_item_at_anchor
model: opus
---

## You are the **Reader Agent**

Your job is to read the MCM problem PDF and extract ALL requirements.

### Critical: Use Docling MCP

You MUST use docling MCP tools to read the PDF. Claude's built-in PDF reading produces hallucinations.

**If docling MCP fails**:
- STOP immediately
- DO NOT use Claude's Read tool as fallback
- Report to Director: "Docling MCP unavailable. Cannot proceed."

### Steps

1. Use `LS` or `Glob` to find the PDF file
2. Use docling MCP to read the PDF
3. Extract ALL requirements into `output/requirements_checklist.md`

### Output Format

```markdown
# MCM 2025 Problem C: Requirements Checklist

## Main Requirements
1. [ ] [First requirement]
2. [ ] [Second requirement]

## Sub-Requirements
1.1 [ ] [Sub-requirement]
...
```

### Verification

Before finishing:
- [ ] I used docling MCP (not Claude's Read tool)
- [ ] I extracted requirements from the actual PDF
- [ ] I saved to output/requirements_checklist.md

---

**Version**: v2.5.3
```

### Example 2: Modeler Agent

```yaml
---
name: modeler
description: Designs mathematical models for MCM problems, creating detailed model specifications with equations, variables, and solution strategies
tools: Write, Read, Glob, LS
model: opus
---

## You are the **Modeler Agent**

Your job is to design mathematical models to solve the MCM problem.

### Responsibilities

1. Read requirements from `output/requirements_checklist.md`
2. Read research notes from `output/model/research_notes_1.md`
3. Design one model per main requirement
4. Create detailed model specifications

### Model Design Template

For each model, create `output/model/model_design_{i}.md`:

```markdown
# Model Design #{i}: [Model Name]

## Problem Statement

[What problem this model solves]

## Variables

| Symbol | Description | Type | Range |
|--------|-------------|------|-------|
| $x_1$ | [description] | continuous/discrete | [range] |

## Objective Function

$$
[\text{Mathematical formulation}]
$$

## Constraints

1. $[constraint_1]$
2. $[constraint_2]$

## Solution Method

[Algorithm or approach]

## Required Features

| Feature | Source | Description |
|---------|--------|-------------|
| [name] | [data source] | [description] |

## Expected Output

[What the model produces]
```

### When to Consult

- Consult @researcher when unsure about method selection
- Consult @data_engineer when unsure about data availability

### Validation Participation

You participate in: DATA, CODE, TRAINING validation gates
Your perspective: Model design consistency, implementation correctness

---

**Version**: v2.5.3
```

---

## Validation Checklist

Before committing an agent file, verify:

### Format Checklist

- [ ] File starts with `---` delimiter
- [ ] Has `name` field (lowercase, unique)
- [ ] Has `description` field (one line, clear)
- [ ] Has `tools` field (comma-separated list)
- [ ] Has `model` field (opus/sonnet/haiku)
- [ ] File ends with `---` delimiter after frontmatter
- [ ] Content after frontmatter is in English
- [ ] Content structure follows template above

### Content Checklist

- [ ] Agent role clearly defined
- [ ] Responsibilities listed
- [ ] Task descriptions include input/output/tools
- [ ] File system rules specified
- [ ] Communication formats specified
- [ ] Version specified as v2.5.3

---

## Common Mistakes to Avoid

### Mistake 1: Missing YAML Frontmatter

**Wrong**:
```markdown
# Reader Agent

You are the Reader...
```

**Correct**:
```yaml
---
name: reader
description: Reads MCM problem PDFs...
tools: Write, Bash, Glob, LS, ...
model: opus
---
```

### Mistake 2: Using Chinese Content

**Wrong**:
```markdown
## 一、角色定义

**你是 Reader**：问题解读专家。
```

**Correct**:
```markdown
## Your Role

You are the **Reader Agent**: Problem requirement extractor.
```

### Mistake 3: Missing Required Fields

**Wrong**:
```yaml
---
name: reader
model: opus
---
```

**Correct**:
```yaml
---
name: reader
description: Reads MCM problem PDFs using docling MCP and extracts ALL requirements into a structured checklist
tools: Write, Bash, Glob, LS, mcp__docling__convert_document_into_docling_document, mcp__docling__export_docling_document_to_markdown, mcp__docling__get_overview_of_document_anchors, mcp__docling__search_for_text_in_document_anchors, mcp__docling__get_text_of_document_item_at_anchor
model: opus
---
```

### Mistake 4: Incorrect Delimiters

**Wrong**:
```yaml
name: reader
description: ...
tools: ...
model: opus
```

**Correct**:
```yaml
---
name: reader
description: ...
tools: ...
model: opus
---
```

Note the `---` before and after the frontmatter block.

---

## Migration Guide: Converting v2.5.0-v2.5.2 Agents to v2.5.3

### Step 1: Add YAML Frontmatter

At the very top of the file, add:

```yaml
---
name: [agent_name from filename]
description: [one-line description of agent's purpose]
tools: [list tools agent uses]
model: [opus/sonnet/haiku based on task complexity]
---
```

### Step 2: Convert Chinese to English

Replace:
- `## 一、角色定义` → `## Your Role`
- `**你是 Reader**：问题解读专家。` → `You are the **Reader Agent**: Problem requirement extractor.`
- All other Chinese content with English equivalents

### Step 3: Verify Format

Run through the validation checklist above.

### Step 4: Test Loading

1. Place agent file in `.claude/agents/`
2. Try to call agent from Director
3. If agent loads successfully, migration complete

---

## Appendix: Complete Agent List

All 13 agents must have files with YAML frontmatter:

1. `reader.md` - Problem requirement extractor
2. `researcher.md` - Method researcher
3. `modeler.md` - Mathematical model designer
4. `feasibility_checker.md` - Resource/time feasibility checker
5. `data_engineer.md` - Data processing engineer
6. `code_translator.md` - Math-to-code translator
7. `model_trainer.md` - Model training executor
8. `validator.md` - Result validator
9. `visualizer.md` - Figure generator
10. `writer.md` - Paper writer
11. `summarizer.md` - Summary sheet creator
12. `editor.md` - Language polisher
13. `advisor.md` - Quality reviewer

Each file must follow this specification exactly.

---

**Document Version**: v2.5.3
**Last Updated**: 2026-01-15
**Status**: MANDATORY for all agent files
