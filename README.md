# MCM-Killer Agent 🤖

> **Project Goal**: Building an Autonomous AI Agent to conquer the Mathematical Contest in Modeling (MCM/ICM).

**MCM-Killer** is an active research project aiming to demonstrate that with the right structured knowledge and reasoning capability, an AI agent can fully automate the MCM competition process—from reading the problem to producing an O-Prize quality paper.

---

## 🧪 Data Strategy: Training vs Testing

The repository is strictly divided to prevent data leakage:

| Dataset | Years | Purpose |
|---------|-------|---------|
| **Training** | 2020 - 2024 | Knowledge Base, Few-Shot Examples, Chain-of-Thought templates |
| **Blind Test** | 2025 | Hold-out set for final Agent evaluation |

---

## 📂 Directory Structure

All directories follow a **strict, machine-readable format**.

```
MCM-killer/
│
├── student paper/                  # [Few-Shot Corpus] O-Prize Papers
│   ├── 2020/
│   │   ├── A/                     # Problem Type A (Continuous)
│   │   │   ├── 2001334.pdf
│   │   │   └── ...
│   │   ├── B/                     # Problem Type B (Discrete)
│   │   ├── C/                     # Problem Type C (Data Insights)
│   │   ├── D/                     # Problem Type D (Operations)
│   │   ├── E/                     # Problem Type E (Environment)
│   │   └── F/                     # Problem Type F (Policy)
│   ├── 2021/
│   │   └── ... (same structure)
│   ├── 2022/
│   ├── 2023/
│   └── 2024/
│
├── problems and results/           # [Benchmark Set] Inputs & Ground Truth
│   ├── 2020/
│   │   ├── 2020_MCM_Problem_A.pdf
│   │   ├── 2020_MCM_Problem_A_Results.pdf
│   │   └── ...
│   ├── 2021/
│   ├── 2022/
│   ├── 2023/
│   ├── 2024/
│   └── 2025/                      # [BLIND TEST - DO NOT TRAIN ON THIS]
│
├── problem analysis/               # [CoT Templates] Reasoning Schemas
│   ├── A/
│   │   ├── question.md            # Problem type analysis
│   │   ├── solution.md            # Standard solution strategies
│   │   └── result.md              # Expected output format
│   ├── B/
│   └── C/
│
└── README.md
```

---

## ✅ Data Integrity Checklist

- [x] `student paper/` contains **ONLY** PDF files
- [x] All papers follow `YYYY/Category/ID.pdf` format
- [x] No orphan files (CSV, LICENSE, README) in data directories
- [x] No nested junk folders (`problem/`, `student paper/`)
- [x] 2025 data isolated as blind test set

---

## 🚀 Roadmap

- [x] **Phase 1**: Data Collection & Standardization
- [ ] **Phase 2**: Knowledge Ingestion (Vector DB from papers)
- [ ] **Phase 3**: Agent Construction (Director-Modeler-Solver-Writer)
- [ ] **Phase 4**: Evaluation on 2025 Problems

---

## 📄 License

This project is for research and educational purposes.