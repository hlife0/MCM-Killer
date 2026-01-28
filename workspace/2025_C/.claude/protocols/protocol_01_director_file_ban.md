# Protocol 1: @director File Reading Ban

> **Purpose**: Prevent @director from contaminating agent evaluations by reading files first
> **Owner**: @director
> **Scope**: Phases 0.5, 1, 4, 10 (any phase where @director delegates evaluation)

## Problem Statement

When @director reads files before delegating to agents, it contaminates the evaluation process:

```
@director reads research_notes.md → forms understanding → calls @advisor
@advisor evaluates from @director's context (NOT the actual file)
Result: Contaminated evaluation, wrong file read
```

## Rules

### Rule 1: @director CANNOT Read Files That Agents Will Evaluate

**FORBIDDEN**:
```
@director reads research_notes.md → forms understanding → calls @advisor
```

**CORRECT**:
```
@director calls @advisor: "Read output/docs/research_notes.md and evaluate"
```

### Rule 2: @director MUST Specify Exact File Paths

**VAGUE** (FORBIDDEN):
```
"@advisor: Evaluate the methodology quality"
```

**EXPLICIT** (REQUIRED):
```
"@advisor: Read output/docs/research_notes.md and evaluate methodology"
```

### Rule 3: Agents MUST Report Which File They Read

**@advisor's report MUST include**:
- "I read: output/docs/research_notes.md"
- "File size: 843 lines"
- "Last modified: [timestamp]"

### Rule 4: @director MUST Verify Correct File Was Read

**@director's checklist**:
- [ ] Agent specified which file they read
- [ ] File path matches expected location
- [ ] File size/timestamp is current
- [ ] Evaluation content matches file content

## Affected Agents

- **@director** (PROHIBITED from reading evaluation targets)
- **@advisor** (MUST read specified file, report file path)
- **@validator** (MUST read specified file, report file path)
- **ALL validation agents** (MUST report which file they evaluated)

## Verification Example

**Correct delegation**:
```
@director: "@advisor: Read output/docs/research_notes.md and evaluate methodology sophistication (1-10 grade). Report which file you read at the start of your response."

@advisor: "File: output/docs/research_notes.md, Size: 843 lines, Last modified: 2026-01-28 10:30 AM. Evaluation: Grade 9/10..."
```

**Incorrect delegation** (Protocol violation):
```
@director: "@advisor: Evaluate the methodology quality"

@advisor: "Grade 8/10" (What file? What methodology?)
```

## Consequences of Violation

- **Contaminated evaluations**: Agents evaluate @director's understanding, not actual file
- **Wrong file read**: Agent reads wrong/old version
- **Quality gate failures**: Invalid evaluations compromise decision-making

## Version History

- **v1.0** (2026-01-25): Extracted from V3.1.0 architecture
