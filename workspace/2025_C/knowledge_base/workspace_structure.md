# Workspace Structure

> **Source**: Extracted from CLAUDE.md v3.1.0
> **Purpose**: Directory layout and file organization reference

## File Structure

All files in CURRENT directory:

```
./ (workspace/2025_C/)
├── 2025_MCM_Problem_C.pdf     # Problem statement (READ FIRST)
├── 2025_Problem_C_Data.zip    # Data files
├── reference_papers/          # 44 O-Prize papers
├── latex_template/            # LaTeX template files
├── CLAUDE.md                  # Main operational documentation
├── .claude/agents/            # Agent configurations
└── output/                    # All outputs
    ├── implementation/        # Code, data, logs, models
    ├── docs/                  # Consultations, rewind, validation reports
    ├── model/                 # Model design documents
    ├── model_proposals/       # Draft proposals
    ├── figures/               # Generated figures
    ├── paper/                 # LaTeX files
    └── results/               # Training results
```

## HMML 2.0 Knowledge Library

The canonical modeling-method library lives under `knowledge_library/`:

- **Methods**: `knowledge_library/methods/**` (HMML 2.0 per-method Markdown)
- **Catalog JSON**: `knowledge_library/hmml_summary.json`
- **Human index**: `knowledge_library/index.md`

## Regeneration Pipeline

JSON-driven pipeline (HMML.json is source of truth):

```bash
python tools/8_migrate_hmml_json.py      # regenerate knowledge_library/methods from HMML.json
python tools/6_build_hmml_index.py       # rebuild hmml_summary.json and index.md
python tools/7_verify_hmml_coverage.py   # sanity-check coverage vs HMML.json
```

**Usage Note**: Subagents that consult methods (especially `@knowledge_librarian` and `@researcher`) MUST use `knowledge_library/hmml_summary.json` and `knowledge_library/methods/**` for method lookup and citations.

---

*Reference: CLAUDE.md - Main operational documentation*
