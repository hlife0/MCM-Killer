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
│   └── storytelling_guide.md
├── code_translator/     # Code workflow and structure
│   ├── workflow.md
│   └── code_structure_template.md
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
└── data_engineer/       # Data protocols
    ├── protocols.md
    └── validation_templates.md
```

---

## Path Conventions

**Critical**: All agent files are located in `.claude/agents/`
**Knowledge files are in**: `agent_knowledge/`

**Relative path from agents to knowledge**: `../agent_knowledge/`

Example:
- Agent file: `.claude/agents/writer.md`
- Knowledge file: `agent_knowledge/writer/latex_templates.md`
- Reference in agent: `../agent_knowledge/writer/latex_templates.md`

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

   - **[Topic]**: `../agent_knowledge/[agent]/[file].md`
   ```

---

## Verification

After extraction, verify:
- [ ] Agent file size reduced
- [ ] All references use correct relative path (`../agent_knowledge/`)
- [ ] No content lost during extraction
- [ ] Headers and formatting preserved
- [ ] Code blocks intact
