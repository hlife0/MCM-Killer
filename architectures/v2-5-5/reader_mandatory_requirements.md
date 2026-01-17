# Reader Mandatory Requirements Protocol (v2.5.5)

> **Critical Enhancement**: v2.5.5
> **Purpose**: Ensure selective/optional requirements are treated as MANDATORY for quality
> **Status**: MANDATORY for @reader

---

## Problem Statement

**Issue Discovered**:
```
Problem statement includes:
"Coach Effect Attribution: Without explicit coaching data, we cannot
definitively attribute systemic shifts to coaching alone. Funding,
infrastructure, and demographic changes may contribute."

Current (v2.5.4) @reader behavior:
- Marks as "选择性/加分项/附加项"
- Treats as optional
- Skips looking for coaching data
- Result: Critical analysis missing from paper

Problems:
1. Problem says "we cannot definitively attribute" → This is a HINT
   that you SHOULD try to find coaching data, not skip it!
2. Reader treats unclear/extra requirements as optional
3. Missing data sources = incomplete analysis
4. Judges notice missing analysis → score suffers
```

**Root Cause**:
- @reader interprets "optional" literally
- No mechanism to mark selective requirements as MANDATORY for quality
- No protocol for finding missing data from reliable sources
- Assumes "data unclear" = "can skip"

**Impact**:
- Critical requirements missed
- Paper lacks depth
- Analysis incomplete
- Competition score reduced

---

## Solution: All Requirements Are MANDATORY

### Core Principle

**ALL Requirements Mentioned in Problem Statement Are MANDATORY**

**Rationale**:
- MCM problems don't include "filler" requirements
- If it's mentioned, it's important for quality
- "Optional" often means "extra credit for better papers"
- "Data unclear" means "you need to research", not "skip it"

---

## Reader Requirements Classification

### Classification System

**Category 1: Explicit Requirements** (MANDATORY)
- Clearly stated main tasks
- Direct questions to answer
- Specific deliverables

**Category 2: Contextual Requirements** (MANDATORY for quality)
- Hinted requirements ("we cannot X without Y")
- Suggestions ("consider including...")
- Notes about data limitations
- Implicit requirements for complete analysis

**Category 3: Data Requirements** (FIND or FLAG)
- If data unclear → Must search reliable sources
- If impossible → Document and flag for @advisor
- Never mark as "skip"

### Decision Tree

```
Reader encounters requirement
  ↓
Is it mentioned in problem statement?
  ↓ YES
Is it clearly marked as "optional" or "extra credit"?
  ↓ NO
Treat as MANDATORY for quality
  ↓
Is data available?
  ↓ YES                        ↓ NO
Mark as: CONFIDENT            Mark as: NEEDS RESEARCH
  ↓                              ↓
List data needed              Must search reliable sources
List data source              Cannot mark as "skip"
  ↓                              ↓
                              After searching:
                                ↓ Found              ↓ Not found
                              Mark as: CONFIDENT    Mark as: IMPOSSIBLE
                                                         ↓
                                                     Flag for @advisor
```

---

## New Output Format

### Requirements Checklist Template (v2.5.5)

```markdown
# MCM 2025 Problem C: Requirements Analysis

## Category 1: Explicit Requirements (MANDATORY)

### Main Tasks
1. [ ] Build a model to predict medal counts for 2028 LA Olympics
   - **Source**: Problem statement, page 2, paragraph 1
   - **Deliverable**: Predictions for all NOCs, uncertainty intervals
   - **Data needed**: Historical medal counts, economic indicators, host data
   - **Feasibility**: ✅ CONFIDENT
     - Data sources: medal_counts.csv, world_bank.csv, hosts.csv
     - All data available in provided dataset

2. [ ] Identify and explain the key factors influencing Olympic success
   - **Source**: Problem statement, page 2, paragraph 2
   - **Deliverable**: Factor analysis with explanations
   - **Data needed**: Various predictors (GDP, population, host, etc.)
   - **Feasibility**: ✅ CONFIDENT

### Sub-Requirements
1.1 [ ] Provide predictions for at least 15 NOCs
   - **Source**: Problem statement, page 3
   - **Feasibility**: ✅ CONFIDENT

1.2 [ ] Include uncertainty quantification
   - **Source**: Problem statement, page 4
   - **Feasibility**: ✅ CONFIDENT

## Category 2: Contextual Requirements (MANDATORY for Quality)

### Hinted Requirements
2. [ ] Coach Effect Attribution Analysis
   - **Source**: Problem statement, page 7
   - **Statement**: "Coach Effect Attribution: Without explicit coaching data,
                   we cannot definitively attribute systemic shifts to coaching
                   alone. Funding, infrastructure, and demographic changes may
                   contribute."
   - **Interpretation**: This is a HINT that coaching analysis is important
   - **Data needed**:
     - Coaching data (hiring, tenure, effectiveness)
     - Funding data (sports budgets, investment)
     - Infrastructure data (facilities, training centers)
     - Demographic data (population trends, age distributions)
   - **Feasibility**: ⚠️ NEEDS RESEARCH
     - Coaching data: Not in provided dataset, must search
     - Funding data: May be in World Bank indicators
     - Infrastructure: Need to search reliable sources
     - Demographics: Available in World Bank data
   - **Priority**: 🔴 HIGH (affects analysis quality, judges will notice if missing)
   - **Action**: Request @researcher to search for these data sources

3. [ ] Near-Miss Feature Analysis
   - **Source**: Problem statement, page 6, footnote
   - **Statement**: "Note: Near-miss data is often incomplete and may require
                   creative problem-solving."
   - **Interpretation**: Problem expects us to include near-miss analysis
   - **Data needed**: Near-miss events (4th place, near-qualifications)
   - **Feasibility**: ⚠️ NEEDS RESEARCH
     - Not in provided dataset
     - May need to approximate or use proxy measures
   - **Priority**: 🟡 MEDIUM (enhances analysis but may be challenging)

### Implicit Requirements
4. [ ] Temporal Dynamics
   - **Source**: Problem asks about "changes over time"
   - **Interpretation**: Should analyze trends, not just snapshots
   - **Data needed**: Time-series data for all predictors
   - **Feasibility**: ✅ CONFIDENT

5. [ ] Host Country Effect
   - **Source**: Problem mentions "home advantage"
   - **Interpretation**: Should quantify host effect
   - **Data needed**: Host history, host dummy variable
   - **Feasibility**: ✅ CONFIDENT

## Category 3: Data Requirements Status

### Available in Provided Dataset
- ✅ Medal counts (1924-2024)
- ✅ Economic indicators (GDP, population)
- ✅ Host data
- ✅ NOC mappings

### Need to Search (Reliable Sources)
- ⚠️ Coaching effectiveness data
  - Potential sources: IOC reports, academic papers, sports analytics
  - Action: Request @researcher to search
- ⚠️ Sports funding data
  - Potential sources: World Bank, national Olympic committee reports
  - Action: Request @researcher to search
- ⚠️ Infrastructure data
  - Potential sources: Olympic bid documents, IOC evaluations
  - Action: Request @researcher to search
- ⚠️ Near-miss data
  - Potential sources: Sports reference databases, Olympic archives
  - Action: Request @researcher to search or propose proxy

### Impossible to Find (Flag for @advisor)
- None currently identified

## Summary

**Total Requirements**: 8
- Category 1 (Explicit): 3
- Category 2 (Contextual): 5
- Category 3 (Data): 4 need research, 0 impossible

**Priority Actions**:
1. Request @researcher to search for coaching data (HIGH priority)
2. Request @researcher to search for funding data (HIGH priority)
3. Request @researcher to search for infrastructure data (MEDIUM priority)
4. Request @researcher to search for near-miss data or propose proxy (MEDIUM priority)

**Quality Impact**:
- Missing Category 2 requirements → Paper grade: B (good but not excellent)
- Including Category 2 requirements → Paper grade: A (comprehensive analysis)
```

---

## Protocol for Data Missing Requirements

### Step 1: Identify Missing Data

When @reader encounters requirement with unclear/missing data:

**DO NOT**:
- ❌ Mark as "optional" and skip
- ❌ Assume it's not important
- ❌ Leave for later (may be forgotten)

**DO**:
- ✅ Mark as "NEEDS RESEARCH"
- ✅ Add to priority list
- ✅ Specify what data is needed
- ✅ Suggest potential sources

### Step 2: Categorize by Priority

**HIGH Priority** (Must find or have good reason):
- Directly mentioned in problem
- Affects core analysis
- Judges will notice if missing

**MEDIUM Priority** (Should find):
- Enhances analysis
- Shows thoroughness
- May differentiate paper quality

**LOW Priority** (Nice to have):
- Minor enhancements
- Decorative elements

### Step 3: Request Research

For each "NEEDS RESEARCH" item, @reader creates consultation request:

```markdown
# Consultation: @reader → @researcher

## Requirement: Coach Effect Attribution

**Problem Statement Reference**:
Page 7: "Coach Effect Attribution: Without explicit coaching data,
we cannot definitively attribute systemic shifts to coaching alone."

**Data Needed**:
1. Coaching effectiveness metrics
   - Coach hiring patterns
   - Coach tenure
   - Coach background (former athletes?)
   - Coach turnover

2. Alternative explanations (as problem suggests):
   - Sports funding (budgets, investment)
   - Infrastructure (facilities, training centers)
   - Demographics (population age distribution, participation)

**Priority**: HIGH
This is directly mentioned in problem statement. Judges will expect
this analysis or at least discussion of why it's not possible.

**Potential Sources**:
- IOC reports and publications
- Academic papers on Olympic success factors
- Sports analytics databases
- National Olympic committee reports
- World Bank indicators (for funding, demographics)

**Question**: Can you find reliable data sources for these?
If impossible, please document why so we can explain to judges.
```

### Step 4: Handle Research Results

**Case 1: Data Found** ✅
```
@researcher finds coaching data
  ↓
@reader updates requirement:
  - From: NEEDS RESEARCH
  - To: CONFIDENT
  - Add: Data source citation
```

**Case 2: Data Not Found, Proxy Available** ⚠️
```
@researcher cannot find direct coaching data
  ↓
@researcher proposes proxy: "Use medal trajectory change after major
                            coaching changes as proxy"
  ↓
@reader updates requirement:
  - From: NEEDS RESEARCH
  - To: CONFIDENT (with proxy)
  - Add: Proxy method explanation
```

**Case 3: Truly Impossible** ❌
```
@researcher searches extensively, no data or proxy available
  ↓
@researcher documents: "Coaching data not available for 80% of NOCs.
                        Reliable proxies also not feasible due to [reasons]."
  ↓
@reader updates requirement:
  - From: NEEDS RESEARCH
  - To: IMPOSSIBLE (documented)
  - Add: Explanation for judges
  - Flag: For @advisor to include in paper's limitations section
```

---

## Quality Standards

### What Judges Expect

**Excellent Paper (A-grade)**:
- Addresses all explicit requirements (Category 1)
- Addresses most contextual requirements (Category 2)
- Shows extra research for missing data
- Discusses limitations honestly
- Comprehensive analysis

**Good Paper (B-grade)**:
- Addresses all explicit requirements (Category 1)
- Addresses some contextual requirements (Category 2)
- Missing some data but acknowledges
- Good analysis but not comprehensive

**Acceptable Paper (C-grade)**:
- Addresses explicit requirements (Category 1)
- Misses most contextual requirements (Category 2)
- Minimal effort on missing data
- Basic analysis

**Unacceptable Paper (D/F)**:
- Misses explicit requirements
- No effort beyond provided dataset
- Incomplete analysis

### Reader's Target

@reader should aim for **A-grade paper** by:
- ✅ Treating Category 2 as MANDATORY for quality
- ✅ Actively searching for missing data (via @researcher)
- ✅ Not accepting "data unclear" as final answer
- ✅ Documenting all attempts and findings

---

## Integration with Workflow

### Phase 0: Problem Understanding

```
@reader reads PDF
  ↓
Extracts ALL requirements
  ↓
Categorizes: Explicit / Contextual / Data
  ↓
For each "NEEDS RESEARCH":
  Create consultation request to @researcher
  ↓
Wait for @researcher responses
  ↓
Update requirements checklist
  ↓
Flag IMPOSSIBLE items for @advisor
  ↓
Finalize requirements checklist
  ↓
Proceed to @researcher (method brainstorming)
```

---

## Anti-Patterns to Avoid

❌ **WRONG**: Mark contextual requirements as optional
```
"Coach Effect Attribution: Optional, skip if data unavailable."
```
✅ **CORRECT**: Mark as MANDATORY, request research
```
"Coach Effect Attribution: MANDATORY for quality.
 Data unavailable → MUST search or explain why impossible."
```

❌ **WRONG**: Skip unclear requirements
```
"Near-miss data unclear, marking as optional enhancement."
```
✅ **CORRECT**: Flag for research, find proxy or explain
```
"Near-miss data not in dataset.
 Priority: MEDIUM
 Action: Request @researcher to find data or propose proxy."
```

❌ **WRONG**: Accept missing data without trying
```
"Funding data not provided, will skip this analysis."
```
✅ **CORRECT**: Search for data, document attempts
```
"Funding data not in provided dataset.
 Priority: HIGH
 Action: Consult @researcher to search World Bank indicators,
         national Olympic committee reports."
```

---

## Testing Checklist

Before implementing, verify:

- [ ] Classification system defined (Explicit/Contextual/Data)
- [ ] Decision tree created
- [ ] New output format template created
- [ ] Data missing protocol specified
- [ ] Priority categorization defined
- [ ] Consultation request template created
- [ ] Research result handling protocol specified
- [ ] Quality standards defined (A/B/C grade papers)
- [ ] Workflow integration specified
- [ ] Anti-patterns documented

---

**Document Version**: v2.5.5
**Created**: 2026-01-17
**Status**: MANDATORY for @reader
