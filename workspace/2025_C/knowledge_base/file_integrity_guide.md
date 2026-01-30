# File Integrity and PDF Reading Guide

> **Source**: CLAUDE.md v3.2.0 File Write Integrity Rules, PDF Reading
> **Purpose**: Detailed reference for file handling and PDF processing

---

## File Write Integrity Rules

### Overview

File corruption can destroy hours of work. ALL agents must follow these rules to prevent corruption.

---

### Rule 1: No Parallel Writes to Same File

**Principle**: One agent finishes writing → next agent starts

**Why**:
- Multiple writers cause race conditions
- Partial writes overwrite each other
- Result: garbled, incomplete, or lost content

**Implementation**:
```
✅ CORRECT:
@modeler writes model_design.md → completes → @feasibility_checker reads

❌ WRONG:
@modeler writing model_design.md
    WHILE @feasibility_checker also writing model_design.md
```

**Director Coordination**:
- Track which agent is working on which file
- Never assign same file to multiple agents
- Use clear handoff signals ("@modeler: Please write to model_design.md. Signal when complete.")

---

### Rule 2: Write-Then-Verify

**Principle**: Write → Read back → Verify content → If corrupted → delete and rewrite

**Implementation**:
```python
# Agent workflow
1. Write file content
2. Read file back
3. Compare: Does content match expected?
   - If YES: Continue
   - If NO: Delete file, rewrite from scratch
```

**Verification Check**:
- File size reasonable (not 0 bytes, not truncated)
- Key sections present (check for headers)
- No garbage characters
- Encoding correct (UTF-8)

---

### Rule 3: Large File Handling

**Principle**: Write in sections → Verify each → Append next

**For files > 50KB**:
```
1. Write Section 1 → Verify → Confirm
2. Append Section 2 → Verify → Confirm
3. Append Section 3 → Verify → Confirm
...
N. Final verification of complete file
```

**Why**:
- Reduces risk of losing entire file
- Easier to identify where corruption occurred
- Recovery: Only rewrite corrupted section

**Example (paper.tex)**:
```
Phase 7A: Write Abstract + Introduction → Verify
Phase 7B: Append Model sections → Verify
Phase 7C: Append Results → Verify
...
```

---

### Rule 4: Corruption Detection

**Signs of Corruption**:
1. **Random fragments**: Text from unrelated commands mixed in
2. **Duplicates**: Same section appears multiple times
3. **Garbled commands**: Shell/tool output mixed with content
4. **Missing sections**: Entire sections disappeared
5. **Encoding issues**: Mojibake (garbled Unicode)
6. **Truncation**: File ends abruptly mid-sentence

**Example Corrupted Content**:
```latex
\section{Model Description}
The model uses...
[tool_use: read_file]     ← Garbled command
"result": "success"       ← JSON leaked
...where β represents the transmission rate.
```

**Action When Detected**:
1. Stop writing immediately
2. Delete corrupted file
3. Rewrite from scratch using source data
4. Do NOT attempt to "fix" corruption

---

### Rule 5: Backup Critical Files

**Files to protect**:
- `model_design.md` (Phase 1 output)
- `features_{i}.pkl` (Phase 3 output)
- `model_{i}.py` (Phase 4 output)
- `results_{i}.csv` (Phase 5 output)
- `paper.tex` (Phase 7 output)

**Backup strategy**:
```bash
# After each major phase, create checkpoint
cp output/implementation/model_1.py output/implementation/checkpoints/model_1_phase4.py
```

**Recovery**:
```bash
# If file corrupted, restore from checkpoint
cp output/implementation/checkpoints/model_1_phase4.py output/implementation/model_1.py
```

---

## PDF Reading: Use Docling MCP

### Why Not Built-in PDF Reading?

Claude's built-in PDF reading produces hallucinations:
- Misreads numbers (especially tables)
- Invents requirements not in the PDF
- Misses sections entirely
- Conflates similar-sounding text

### Docling MCP Solution

**Tool**: `mcp__docling__convert_document_into_docling_document`

**Usage**:
```json
{
  "source": "file:///D:/MCM-Killer/MCM-Killer/workspace/2025_C/output/problem/problem_c.pdf"
}
```

**Returns**: Markdown text with accurate extraction

### ⚠️ Windows File URI Format (CRITICAL)

> [!CAUTION] **Windows paths MUST use forward slashes in file:// URIs.**
>
> The docling MCP will crash with `[Errno 22] Invalid argument` if you use backslashes.

**Correct Format (Windows)**:
```
file:///D:/MCM-Killer/MCM-Killer/workspace/2025_C/problem.pdf
       ↑↑↑ ↑                    ↑
       ||| |                    └── Forward slashes (/)
       ||| └── Drive letter with colon
       ||└── Third slash after file:
       |└── Second slash
       └── First slash (total: 3 slashes after "file:")
```

**Wrong Format (Will Crash)**:
```
file:\D:\MCM-Killer\MCM-Killer\workspace\2025_C\problem.pdf
     ↑  ↑          ↑
     └──┴──────────┴── Backslashes cause [Errno 22] Invalid argument
```

**Conversion Rule**:
```python
# Convert Windows path to file URI
windows_path = r"D:\MCM-Killer\MCM-Killer\workspace\2025_C\problem.pdf"
file_uri = "file:///" + windows_path.replace("\\", "/")
# Result: file:///D:/MCM-Killer/MCM-Killer/workspace/2025_C/problem.pdf
```

**Recommendation**: Prefer docling CLI over MCP to avoid URI format issues:
```bash
docling --to md --output output/problem problem.pdf
```

### Critical: Sequential Reading Only

**Docling MCP will crash if you read multiple PDFs concurrently.**

**Correct Pattern**:
```
✅ Read PDF 1 → Wait for response → Read PDF 2 → Wait for response
```

**Wrong Pattern**:
```
❌ Read PDF 1 AND Read PDF 2 simultaneously
```

**Implementation**:
```
@reader: Read problem_c.pdf
[Wait for completion]
@reader: Read supplementary.pdf
[Wait for completion]
@reader: Read data_description.pdf
```

### PDF Reading Workflow

1. **Identify PDFs to read**:
   ```bash
   ls output/problem/*.pdf
   ```

2. **Read sequentially**:
   - Problem statement first
   - Supplementary materials second
   - Data descriptions last

3. **Extract to Markdown**:
   - Save Docling output to `output/docs/problem_text.md`
   - @reader processes Markdown (not original PDF)

4. **Verify extraction**:
   - Spot-check numbers match PDF
   - Verify section headings present
   - Check tables converted correctly

---

## Reference Papers

### Location

Reference papers are in: `reference_papers/`

### Reading Protocol

Same rules apply:
1. Use Docling MCP (not built-in reading)
2. Read sequentially (one at a time)
3. Extract to Markdown for processing

### O-Prize Paper Analysis

When analyzing O-Prize winning papers:
```
@knowledge_librarian: Analyze reference paper structure
File: reference_papers/2022_O_Prize.pdf
Focus: Section structure, mathematical notation style, figure quality
```

---

## Troubleshooting

### File Won't Write

**Symptoms**: Write command fails, file not created

**Solutions**:
1. Check directory exists: `mkdir -p output/docs/`
2. Check permissions: File not locked by another process
3. Check disk space: Unlikely but possible
4. Check path: Windows vs Unix separators

### File Corrupted After Write

**Symptoms**: Content garbled, sections missing

**Solutions**:
1. Delete file: `rm output/docs/corrupted.md`
2. Rewrite from scratch
3. Check for parallel writes (were two agents working?)
4. Reduce write size (break into sections)

### PDF Not Reading Correctly

**Symptoms**: Docling returns partial/garbled content

**Solutions**:
1. Verify PDF exists and is valid
2. Use absolute path with file:/// prefix
3. Check PDF isn't encrypted/protected
4. Try reading smaller PDF first (verify tool works)

### Encoding Issues

**Symptoms**: Mojibake (中文 becomes æä¸­æ)

**Solutions**:
1. Ensure UTF-8 encoding in all writes
2. Verify source data encoding
3. Convert if necessary: `iconv -f LATIN1 -t UTF-8`

---

*Reference: CLAUDE.md - File Write Integrity Rules, PDF Reading*
