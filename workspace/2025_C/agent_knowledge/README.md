# Agent Knowledge Base

**Purpose**: External knowledge files for MCM agents, extracted to reduce agent file sizes and improve maintainability.

---

## Folder Structure

```
agent_knowledge/
├── writer/              # LaTeX templates and protocols
│   ├── latex_templates.md
│   ├── phase_7_templates.md
│   ├── protocols.md
│   ├── protocols/              # 🆕 Protocol 16-18 knowledge
│   │   ├── protocol_16_page_tracking_examples.md
│   │   └── csv_to_latex_table.py
│   └── storytelling_guide.md
├── code_translator/     # Code workflow and structure
│   ├── workflow.md
│   ├── code_structure_template.md
│   └── protocols/              # 🆕 Protocol 17 knowledge
│       └── protocol_17_unit_test_template.py
├── modeler/             # Math protocols and iterations
│   ├── math_protocol.md
│   └── iteration_protocol.md
├── model_trainer/       # Training templates and checks
│   ├── training_templates.md
│   ├── sanity_checks.md
│   └── report_templates.md
├── time_validator/      # Validation protocols
│   ├── validation_protocols.md
│   ├── scoring_tables.md
│   └── verdict_templates.md
├── data_engineer/       # Data protocols
│   ├── protocols.md
│   ├── validation_templates.md
│   └── protocols/              # 🆕 Protocol 18 knowledge
│       ├── protocol_18_script_examples.md
│       ├── csv_to_latex_table.py
│       └── validate_consistency.py
└── validator/           # 🆕 Validation protocols
    └── protocols/              # 🆕 Protocol 18 knowledge
        └── validate_consistency.py
```

---

## Path Conventions

**Critical**: All agent files are located in `.claude/agents/`
**Knowledge files are in**: `agent_knowledge/`

**Relative path from agents to knowledge**: `../../agent_knowledge/`

Example:
- Agent file: `.claude/agents/writer.md`
- Knowledge file: `agent_knowledge/writer/latex_templates.md`
- Reference in agent: `../../agent_knowledge/writer/latex_templates.md`

---

## Why External Knowledge Files?

1. **Smaller agent files**: Reduced context window usage
2. **Reusable knowledge**: Templates can be shared across agents
3. **Easier maintenance**: Update templates in one place
4. **Better organization**: Knowledge categorized by topic
5. **Version control friendly**: Smaller diffs when changing core logic

---

## File Size Reduction Summary

| Agent | Before | After | Reduction |
|-------|--------|-------|-----------|
| writer.md | 67,922 B | 54,869 B | 19% |
| code_translator.md | 56,386 B | 50,479 B | 11% |
| modeler.md | 53,311 B | TBD | TBD |
| model_trainer.md | 48,786 B | TBD | TBD |
| time_validator.md | 42,814 B | TBD | TBD |
| data_engineer.md | 40,036 B | TBD | TBD |

---

## Adding New Knowledge Files

When extracting content from agent files:

1. Create folder in `agent_knowledge/[agent_name]/`
2. Create `.md` file with descriptive name
3. Add header:
   ```markdown
   # [Title]

   **Agent**: [agent_name]
   **Source**: Originally embedded in `.claude/agents/[agent_name].md`
   **Purpose**: [description]
   ---
   ```
4. Update agent file with reference:
   ```markdown
   ## 📖 External Knowledge Reference

   - **[Topic]**: `../../agent_knowledge/[agent]/[file].md`
   ```

---

## Verification

After extraction, verify:
- [ ] Agent file size reduced
- [ ] All references use correct relative path (`../../agent_knowledge/`)
- [ ] No content lost during extraction
- [ ] Headers and formatting preserved
- [ ] Code blocks intact

---

## Protocol 16-18 Knowledge Files (v3.2.0)

### @writer Protocol Knowledge
- **File**: `writer/protocols/protocol_16_page_tracking_examples.md`
- **Purpose**: Page count reporting examples, consolidation scenarios, budget reference
- **Usage**: Reference when writing Phase 7 sections, reporting page counts

### @code_translator Protocol Knowledge
- **File**: `code_translator/protocols/protocol_17_unit_test_template.py`
- **Purpose**: Unit test template for all model_{i}.py files
- **Usage**: Copy and customize for each model implementation

### @data_engineer Protocol Knowledge
- **File**: `data_engineer/protocols/protocol_18_script_examples.md`
- **Purpose**: Complete script examples and usage for csv_to_latex_table.py and validate_consistency.py
- **Usage**: Reference when creating and testing Protocol 18 scripts

- **File**: `data_engineer/protocols/csv_to_latex_table.py`
- **Purpose**: Automated LaTeX table generation script
- **Usage**: @writer uses this script to generate LaTeX tables from CSV

- **File**: `data_engineer/protocols/validate_consistency.py`
- **Purpose**: Automated consistency validation script
- **Usage**: @validator uses this script to verify CSV vs LaTeX consistency

### @validator Protocol Knowledge
- **File**: `validator/protocols/validate_consistency.py`
- **Purpose**: Script reference for consistency validation
- **Usage**: Run before Phase 7.5 to enforce data consistency

---

## Protocol 16-18 Quick Reference

### Protocol 16: Page Count Tracking
**Agent**: @writer
**Knowledge**: `writer/protocols/protocol_16_page_tracking_examples.md`
**Key Feature**: 5 checkpoint system with alert thresholds

### Protocol 17: Model Component Testing
**Agent**: @code_translator
**Knowledge**: `code_translator/protocols/protocol_17_unit_test_template.py`
**Key Feature**: Unit tests, dimension verification, reduced dataset validation

### Protocol 18: Automated Value Injection
**Agents**: @data_engineer, @writer, @validator
**Knowledge**:
- `data_engineer/protocols/protocol_18_script_examples.md`
- `data_engineer/protocols/csv_to_latex_table.py`
- `data_engineer/protocols/validate_consistency.py`
**Key Feature**: Automatic rejection for data inconsistencies

---
