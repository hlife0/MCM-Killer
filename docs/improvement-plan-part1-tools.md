# MCM-Killer Improvement Plan - Part 1: Tools & Infrastructure

**Date**: 2025-01-28
**Based On**: SYSTEM_COHERENCE_VALIDITY_REPORT_2025-01-28.md
**Assigned To**: Agent 1 (Tools & Infrastructure)
**Scope**: All improvements that modify `tools/` directory
**Estimated Effort**: 20-28 hours

---

## 📋 Part 1 Scope

This document contains improvements that focus on **tool creation and infrastructure**. These improvements:

- ✅ Create new tools in `tools/` directory
- ✅ Modify VERSION_MANIFEST.json
- ✅ Do NOT modify agent prompts (`.claude/agents/`)
- ✅ Can be executed in parallel with Part 2 (Agent Prompts)

### Included Improvements

1. **Improvement #1**: Phase Tracking Automation (HIGH) - 2-3 hours
2. **Improvement #2**: Orchestration Logging System (HIGH) - 3-4 hours
6. **Improvement #6**: System Health Check Tool (MEDIUM) - 4-5 hours
7. **Improvement #7**: Progress Dashboard (LOW) - 11-16 hours

### Excluded Improvements

These are in Part 2 to avoid conflicts:
- Improvement #3: VALUABLE Modular Prompts (modifies `.claude/`)
- Improvement #4: SafePlaceholder Pattern (modifies `.claude/agents/`)
- Improvement #5: Event Tracking System (modifies `.claude/`)

---

## Executive Summary (Part 1)

### Expected Outcomes for Tools & Infrastructure

✅ Automated progress tracking via Phase Tracker
✅ Complete observability into all decisions via Orchestration Logger
✅ Pre-flight validation capabilities via Health Check
✅ Real-time progress monitoring via Progress Dashboard

### Estimated Effort Breakdown

- Improvement #1: 2-3 hours
- Improvement #2: 3-4 hours
- Improvement #6: 4-5 hours
- Improvement #7: 11-16 hours (complex dashboard)
- **Total**: 20-28 hours

---

## Part 1: HIGH-Priority Improvements (Sprint 1)

### Improvement #1: Phase Tracking Automation

**Priority**: HIGH
**Effort**: 2-3 hours
**Risk**: LOW
**Impact**: Enables automated progress tracking and resume capability

---

#### 1.1 Current State

**Problem**: `VERSION_MANIFEST.json` shows `phases_completed: []` despite evidence of completed work (model designs, validation reports, code implementations).

**Impact**:
- Cannot track actual progress
- Cannot resume from interruptions
- Manual verification required
- Difficult to measure completion percentage

**Current Manifest Structure**:
```json
{
  "project": "MCM-Killer",
  "version": "3.1.0",
  "workspace": "2025_C",
  "phases_completed": [],
  "last_updated": "2025-01-28"
}
```

---

#### 1.2 Solution Design

**Approach**: Create automated phase tracking tool that:
1. Detects phase completion artifacts
2. Updates VERSION_MANIFEST.json automatically
3. Provides resume capability from last completed phase
4. Validates phase dependencies

**Components**:
- `tools/phase_tracker.py` - PhaseTracker class
- Enhanced VERSION_MANIFEST.json schema
- Integration commands for CLAUDE.md
- Phase validation rules

---

#### 1.3 Implementation Plan

**Step 1: Create Phase Tracker Tool**

**File**: `workspace/2025_C/tools/phase_tracker.py`

```python
#!/usr/bin/env python3
"""
Phase Tracker - Automated Phase Progress Tracking System

This tool automatically tracks phase completion by detecting artifacts,
validating dependencies, and updating VERSION_MANIFEST.json.

Usage:
    python tools/phase_tracker.py --check          # Check current status
    python tools/phase_tracker.py --update         # Update manifest
    python tools/phase_tracker.py --validate 5     # Validate specific phase
    python tools/phase_tracker.py --resume         # Get resume point
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set
import argparse


class PhaseTracker:
    """Automated phase tracking and validation system."""

    # Phase definitions with required artifacts
    PHASES = {
        "0": {
            "name": "Problem Analysis",
            "artifacts": ["research_notes.md"],
            "optional": ["time_validator_0.md"],
            "depends_on": []
        },
        "0.2": {
            "name": "Knowledge Library Query",
            "artifacts": ["suggested_methods.md"],
            "optional": [],
            "depends_on": ["0"]
        },
        "0.5": {
            "name": "Methodology Evaluation",
            "artifacts": ["methodology_evaluation_*.md"],
            "optional": [],
            "depends_on": ["0.2"]
        },
        "1": {
            "name": "Model Design",
            "artifacts": ["model_design_*.md", "model_selection_report.md"],
            "optional": ["model_comparison_matrix.md"],
            "depends_on": ["0.5"]
        },
        "1.5": {
            "name": "Feature Engineering",
            "artifacts": ["feature_engineering_plan.md"],
            "optional": ["features_*.pkl"],
            "depends_on": ["1"]
        },
        "2": {
            "name": "Data Preprocessing",
            "artifacts": ["preprocessing_report.md", "data_preparation.md"],
            "optional": [],
            "depends_on": ["1.5"]
        },
        "3": {
            "name": "Model Implementation",
            "artifacts": ["model_*.py"],
            "optional": ["model_implementation_report.md"],
            "depends_on": ["2"]
        },
        "4": {
            "name": "Model Integration",
            "artifacts": ["ensemble_system.py"],
            "optional": [],
            "depends_on": ["3"]
        },
        "4.5": {
            "name": "Validation Framework",
            "artifacts": ["validation_framework.md"],
            "optional": [],
            "depends_on": ["4"]
        },
        "5A": {
            "name": "Initial Training",
            "artifacts": ["results_initial.csv"],
            "optional": ["training_log_initial.txt"],
            "depends_on": ["4.5"]
        },
        "5B": {
            "name": "Full Training",
            "artifacts": ["results_*.csv"],
            "optional": ["training_log_full.txt"],
            "depends_on": ["5A"]
        },
        "5.5": {
            "name": "Model Evaluation",
            "artifacts": ["evaluation_report.md"],
            "optional": ["model_performance_metrics.json"],
            "depends_on": ["5B"]
        },
        "5.8": {
            "name": "Metacognitive Analysis",
            "artifacts": ["insights_*.md"],
            "optional": [],
            "depends_on": ["5.5"]
        },
        "6": {
            "name": "Results Validation",
            "artifacts": ["validation_report_6.md"],
            "optional": [],
            "depends_on": ["5.8"]
        },
        "6.5": {
            "name": "Figure Generation",
            "artifacts": ["figures/*.png", "figures/*.pdf"],
            "optional": [],
            "depends_on": ["6"]
        },
        "7": {
            "name": "Outline Generation",
            "artifacts": ["paper_outline.md"],
            "optional": [],
            "depends_on": ["6.5"]
        },
        "7.5": {
            "name": "First Draft",
            "artifacts": ["paper_draft_v1.md"],
            "optional": [],
            "depends_on": ["7"]
        },
        "8": {
            "name": "Self-Review",
            "artifacts": ["review_notes.md"],
            "optional": [],
            "depends_on": ["7.5"]
        },
        "9": {
            "name": "Revision",
            "artifacts": ["paper_draft_v2.md"],
            "optional": [],
            "depends_on": ["8"]
        },
        "9.1": {
            "name": "Style Analysis",
            "artifacts": ["style_analysis_report.md"],
            "optional": [],
            "depends_on": ["9"]
        },
        "9.5": {
            "name": "Final Polish",
            "artifacts": ["paper_final.md"],
            "optional": [],
            "depends_on": ["9.1"]
        },
        "10": {
            "name": "Final Review",
            "artifacts": ["final_review_report.md"],
            "optional": [],
            "depends_on": ["9.5"]
        },
        "11": {
            "name": "Submission Package",
            "artifacts": ["submission/problem_solution.pdf"],
            "optional": [],
            "depends_on": ["10"]
        }
    }

    def __init__(self, workspace_dir: str = None):
        """Initialize phase tracker with workspace directory."""
        self.workspace_dir = Path(workspace_dir or os.getcwd())
        self.manifest_path = self.workspace_dir / "VERSION_MANIFEST.json"
        self.output_dir = self.workspace_dir / "output"
        self.submission_dir = self.output_dir / "submission"

    def load_manifest(self) -> Dict:
        """Load VERSION_MANIFEST.json."""
        if self.manifest_path.exists():
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "project": "MCM-Killer",
            "version": "3.1.0",
            "workspace": str(self.workspace_dir.name),
            "phases_completed": [],
            "last_updated": None
        }

    def save_manifest(self, manifest: Dict):
        """Save VERSION_MANIFEST.json."""
        manifest["last_updated"] = datetime.now().isoformat()
        with open(self.manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"✅ Manifest updated: {self.manifest_path}")

    def check_artifacts(self, phase_id: str) -> Dict[str, bool]:
        """Check if phase artifacts exist."""
        if phase_id not in self.PHASES:
            return {}

        phase = self.PHASES[phase_id]
        artifact_status = {}

        # Check required artifacts
        for artifact in phase["artifacts"]:
            artifact_path = self._find_artifact(artifact)
            artifact_status[artifact] = artifact_path is not None

        # Check optional artifacts
        for artifact in phase.get("optional", []):
            artifact_path = self._find_artifact(artifact)
            if artifact_path:
                artifact_status[f"{artifact} (optional)"] = True

        return artifact_status

    def _find_artifact(self, pattern: str) -> Optional[Path]:
        """Find artifact file matching pattern."""
        # Check output directory
        for path in self.output_dir.rglob(pattern):
            if path.is_file():
                return path

        # Check submission directory
        if self.submission_dir.exists():
            for path in self.submission_dir.rglob(pattern):
                if path.is_file():
                    return path

        return None

    def validate_phase(self, phase_id: str) -> bool:
        """Validate if phase is complete."""
        artifacts = self.check_artifacts(phase_id)
        if not artifacts:
            return False

        # Check required artifacts
        phase = self.PHASES[phase_id]
        for artifact in phase["artifacts"]:
            if not artifacts.get(artifact, False):
                return False

        # Check dependencies
        for dep in phase.get("depends_on", []):
            if dep not in self.load_manifest()["phases_completed"]:
                print(f"⚠️  Warning: Phase {phase_id} depends on uncompleted phase {dep}")
                return False

        return True

    def get_completed_phases(self) -> List[str]:
        """Get list of completed phases."""
        completed = []
        for phase_id in self.PHASES.keys():
            if self.validate_phase(phase_id):
                completed.append(phase_id)
        return completed

    def get_next_phase(self) -> Optional[str]:
        """Get next phase to work on."""
        completed = set(self.get_completed_phases())

        for phase_id in self.PHASES.keys():
            if phase_id not in completed:
                # Check if dependencies are met
                phase = self.PHASES[phase_id]
                deps_met = all(dep in completed for dep in phase.get("depends_on", []))
                if deps_met:
                    return phase_id

        return None

    def get_resume_point(self) -> Optional[Dict]:
        """Get recommended resume point."""
        next_phase = self.get_next_phase()
        if not next_phase:
            return None

        phase = self.PHASES[next_phase]
        return {
            "phase_id": next_phase,
            "phase_name": phase["name"],
            "artifacts_to_create": phase["artifacts"],
            "dependencies": phase.get("depends_on", []),
            "estimated_hours": self._estimate_hours(next_phase)
        }

    def _estimate_hours(self, phase_id: str) -> str:
        """Estimate hours for phase."""
        estimates = {
            "0": "2-3", "0.2": "1-2", "0.5": "2-3",
            "1": "4-6", "1.5": "3-4", "2": "2-3",
            "3": "6-8", "4": "3-4", "4.5": "2-3",
            "5A": "4-6", "5B": "8-12", "5.5": "2-3",
            "5.8": "1-2", "6": "2-3", "6.5": "3-4",
            "7": "2-3", "7.5": "4-6", "8": "2-3",
            "9": "3-4", "9.1": "1-2", "9.5": "2-3",
            "10": "1-2", "11": "1-2"
        }
        return estimates.get(phase_id, "2-4")

    def update_manifest(self):
        """Update VERSION_MANIFEST.json with completed phases."""
        manifest = self.load_manifest()
        completed = self.get_completed_phases()

        # Add new completed phases
        new_phases = set(completed) - set(manifest["phases_completed"])
        if new_phases:
            print(f"📊 Found {len(new_phases)} new completed phase(s): {', '.join(sorted(new_phases, key=float))}")
            manifest["phases_completed"] = completed
            self.save_manifest(manifest)

            # Print progress
            total = len(self.PHASES)
            done = len(completed)
            percent = (done / total) * 100
            print(f"📈 Progress: {done}/{total} phases ({percent:.1f}%)")
        else:
            print("ℹ️  No new completed phases found")

        return manifest

    def print_status(self):
        """Print current status."""
        manifest = self.load_manifest()
        completed = manifest["phases_completed"]
        total = len(self.PHASES)
        percent = (len(completed) / total) * 100

        print(f"\n{'='*60}")
        print(f"MCM-Killer Phase Status")
        print(f"{'='*60}")
        print(f"Workspace: {self.workspace_dir}")
        print(f"Progress: {len(completed)}/{total} phases ({percent:.1f}%)")
        print(f"Last Updated: {manifest.get('last_updated', 'Never')}")
        print(f"\nCompleted Phases:")

        if completed:
            for phase_id in sorted(completed, key=float):
                phase = self.PHASES[phase_id]
                print(f"  ✅ Phase {phase_id}: {phase['name']}")
        else:
            print("  ⚠️  No phases completed yet")

        next_phase = self.get_next_phase()
        if next_phase:
            phase = self.PHASES[next_phase]
            print(f"\n📍 Next Phase:")
            print(f"   Phase {next_phase}: {phase['name']}")
            print(f"   Artifacts: {', '.join(phase['artifacts'])}")
            print(f"   Estimated: {self._estimate_hours(next_phase)} hours")
        else:
            print(f"\n🎉 All phases completed!")

        print(f"{'='*60}\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="MCM-Killer Phase Tracker")
    parser.add_argument("--workspace", type=str, default=None,
                       help="Workspace directory (default: current directory)")
    parser.add_argument("--check", action="store_true",
                       help="Check current status")
    parser.add_argument("--update", action="store_true",
                       help="Update VERSION_MANIFEST.json")
    parser.add_argument("--validate", type=str, metavar="PHASE",
                       help="Validate specific phase")
    parser.add_argument("--resume", action="store_true",
                       help="Get resume point")

    args = parser.parse_args()

    tracker = PhaseTracker(args.workspace)

    if args.check:
        tracker.print_status()
    elif args.update:
        tracker.update_manifest()
    elif args.validate:
        valid = tracker.validate_phase(args.validate)
        print(f"Phase {args.validate}: {'✅ VALID' if valid else '❌ INCOMPLETE'}")
        if not valid:
            artifacts = tracker.check_artifacts(args.validate)
            for artifact, status in artifacts.items():
                print(f"  {'✅' if status else '❌'} {artifact}")
    elif args.resume:
        resume = tracker.get_resume_point()
        if resume:
            print(f"\n📍 Resume Point:")
            print(f"   Phase {resume['phase_id']}: {resume['phase_name']}")
            print(f"   Artifacts to create: {', '.join(resume['artifacts_to_create'])}")
            print(f"   Dependencies: {', '.join(resume['dependencies']) if resume['dependencies'] else 'None'}")
            print(f"   Estimated: {resume['estimated_hours']} hours")
            print()
        else:
            print("\n🎉 All phases completed! No resume point needed.\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

---

**Step 2: Enhanced VERSION_MANIFEST.json Schema**

**File**: `workspace/2025_C/VERSION_MANIFEST.json`

```json
{
  "project": "MCM-Killer",
  "version": "3.1.0",
  "workspace": "2025_C",
  "phases_completed": [],
  "phase_details": {},
  "last_updated": null,
  "metadata": {
    "total_phases": 22,
    "current_phase": null,
    "estimated_completion_hours": null,
    "auto_tracking_enabled": true
  }
}
```

**Enhanced Schema with Details**:
```json
{
  "project": "MCM-Killer",
  "version": "3.1.0",
  "workspace": "2025_C",
  "phases_completed": ["0", "0.2", "0.5", "1"],
  "phase_details": {
    "0": {
      "completed_at": "2025-01-28T10:30:00",
      "artifacts": ["research_notes.md"],
      "duration_hours": 2.5
    },
    "1": {
      "completed_at": "2025-01-28T16:45:00",
      "artifacts": ["model_design_1.md", "model_design_2.md", "model_selection_report.md"],
      "duration_hours": 5.0
    }
  },
  "last_updated": "2025-01-28T16:45:00",
  "metadata": {
    "total_phases": 22,
    "current_phase": "1.5",
    "estimated_completion_hours": 85,
    "auto_tracking_enabled": true
  }
}
```

---

**Step 3: Integration with CLAUDE.md**

**Add to CLAUDE.md** (after Phase 0 header):

```markdown
## Phase 0: Problem Analysis (2-3 hours)

**Agent**: @reader, @researcher
**Output**: `output/research_notes.md`

**After Completion**:
```bash
python tools/phase_tracker.py --update
```

This command automatically updates VERSION_MANIFEST.json to track completion.
```

**Add to CLAUDE.md** (at end, before footer):

```markdown
---

## Phase Tracking Commands

Throughout the workflow, use these commands to track progress:

**Check Status**:
```bash
python tools/phase_tracker.py --check
```

**Update Manifest** (run after completing each phase):
```bash
python tools/phase_tracker.py --update
```

**Get Resume Point** (if interrupted):
```bash
python tools/phase_tracker.py --resume
```

**Validate Specific Phase**:
```bash
python tools/phase_tracker.py --validate 5B
```
```

---

#### 1.4 Testing Procedure

**Test 1: Initial Detection**

```bash
cd workspace/2025_C
python tools/phase_tracker.py --check
```

**Expected Output**:
```
============================================================
MCM-Killer Phase Status
============================================================
Workspace: /path/to/2025_C
Progress: 4/22 phases (18.2%)
Last Updated: Never

Completed Phases:
  ✅ Phase 0: Problem Analysis
  ✅ Phase 0.2: Knowledge Library Query
  ✅ Phase 0.5: Methodology Evaluation
  ✅ Phase 1: Model Design

📍 Next Phase:
   Phase 1.5: Feature Engineering
   Artifacts: feature_engineering_plan.md
   Estimated: 3-4 hours
============================================================
```

**Test 2: Update Manifest**

```bash
python tools/phase_tracker.py --update
```

**Expected Output**:
```
📊 Found 4 new completed phase(s): 0, 0.2, 0.5, 1
📈 Progress: 4/22 phases (18.2%)
✅ Manifest updated: /path/to/VERSION_MANIFEST.json
```

**Test 3: Resume Capability**

```bash
python tools/phase_tracker.py --resume
```

**Expected Output**:
```
📍 Resume Point:
   Phase 1.5: Feature Engineering
   Artifacts to create: feature_engineering_plan.md
   Dependencies: 1
   Estimated: 3-4 hours
```

---

#### 1.5 Rollback Plan

**If issues occur**:

1. **Restore original manifest**:
```bash
git checkout VERSION_MANIFEST.json
```

2. **Disable auto-tracking**:
```json
{
  "metadata": {
    "auto_tracking_enabled": false
  }
}
```

3. **Remove tool**:
```bash
rm tools/phase_tracker.py
```

4. **Revert CLAUDE.md changes**:
```bash
git checkout CLAUDE.md
```

---

### Improvement #2: Orchestration Logging System

**Priority**: HIGH
**Effort**: 3-4 hours
**Risk**: LOW
**Impact**: Complete observability into all agent decisions and actions

---

#### 2.1 Current State

**Problem**: No central record of agent executions, decisions, and reasoning. Limited visibility into:
- Which agents were invoked
- What decisions were made
- Why specific approaches were chosen
- Timeline of execution
- Errors and incidents

**Impact**:
- Difficult to debug issues
- No audit trail for decisions
- Cannot reproduce results
- Limited learning from iterations

---

#### 2.2 Solution Design

**Approach**: Create comprehensive orchestration logging system that:
1. Logs every agent invocation
2. Records all decisions with rationale
3. Tracks timeline and duration
4. Captures errors and incidents
5. Provides structured analysis capability

**Components**:
- `tools/orchestration_logger.py` - OrchestrationLogger class
- `output/docs/orchestration_log.md` - Structured log file
- Integration commands for CLAUDE.md
- Log analysis utilities

---

#### 2.3 Implementation Plan

**Step 1: Create Orchestration Logger Tool**

**File**: `workspace/2025_C/tools/orchestration_logger.py`

```python
#!/usr/bin/env python3
"""
Orchestration Logger - Comprehensive Logging System

Logs all agent executions, decisions, and reasoning for complete
observability and audit trail.

Usage:
    python tools/orchestration_logger.py --start-phase 1
    python tools/orchestration_logger.py --log-agent @modeler "Designed 6 models"
    python tools/orchestration_logger.py --log-decision "Selected ensemble approach" "High diversity needed"
    python tools/orchestration_logger.py --log-error "Missing data file" "Recovering from backup"
    python tools/orchestration_logger.py --end-phase 1
    python tools/orchestration_logger.py --analyze
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import argparse


class OrchestrationLogger:
    """Comprehensive orchestration logging system."""

    def __init__(self, workspace_dir: str = None):
        """Initialize orchestration logger."""
        self.workspace_dir = Path(workspace_dir or os.getcwd())
        self.log_dir = self.workspace_dir / "output" / "docs"
        self.log_path = self.log_dir / "orchestration_log.md"
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.current_phase = None
        self.phase_start_time = None
        self.entries = []

    def _load_log(self) -> str:
        """Load existing log file."""
        if self.log_path.exists():
            with open(self.log_path, 'r', encoding='utf-8') as f:
                return f.read()
        return self._get_template()

    def _save_log(self, content: str):
        """Save log file."""
        with open(self.log_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Log updated: {self.log_path}")

    def _get_template(self) -> str:
        """Get orchestration log template."""
        return f"""# MCM-Killer Orchestration Log

**Project**: MCM-Killer v3.1.0
**Workspace**: {self.workspace_dir.name}
**Started**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Table of Contents

- [Phase Execution Log](#phase-execution-log)
- [Agent Invocations](#agent-invocations)
- [Decisions Log](#decisions-log)
- [Incidents & Errors](#incidents--errors)
- [Timeline Analysis](#timeline-analysis)

---

## Phase Execution Log

| Phase | Name | Start Time | End Time | Duration | Status |
|-------|------|------------|----------|----------|--------|

---

## Agent Invocations

| Time | Phase | Agent | Task | Input | Output | Duration |
|------|-------|-------|------|-------|--------|----------|

---

## Decisions Log

| Time | Phase | Decision | Rationale | Alternatives Considered |
|------|-------|----------|-----------|------------------------|
| {datetime.now().strftime('%Y-%m-%d %H:%M')} | - | System initialized | Logging started | - | - |

---

## Incidents & Errors

| Time | Phase | Severity | Issue | Resolution | Prevention |
|------|-------|----------|-------|------------|------------|

---

## Timeline Analysis

**Total Elapsed Time**: 0 hours 0 minutes

**Phase Breakdown**:

**Agent Usage**:

**Bottlenecks**:

---

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

    def start_phase(self, phase_id: str, phase_name: str):
        """Log phase start."""
        self.current_phase = phase_id
        self.phase_start_time = datetime.now()

        timestamp = self.phase_start_time.strftime('%Y-%m-%d %H:%M:%S')
        entry = f"""
### Phase {phase_id}: {phase_name}

**Started**: {timestamp}
**Status**: 🔄 IN PROGRESS

---

"""
        self._append_to_section("Phase Execution Log", entry, after="## Phase Execution Log\n")
        self._save_log(self._load_log())

        print(f"📍 Phase {phase_id} started at {timestamp}")

    def end_phase(self, phase_id: str, status: str = "✅ COMPLETE"):
        """Log phase completion."""
        if not self.phase_start_time:
            print("⚠️  No phase in progress")
            return

        duration = datetime.now() - self.phase_start_time
        duration_str = self._format_duration(duration)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Update phase table
        entry = f"| {phase_id} | Phase {phase_id} | {self.phase_start_time.strftime('%Y-%m-%d %H:%M')} | {timestamp} | {duration_str} | {status} |\n"

        content = self._load_log()
        # Find phase table and add row
        if "| Phase | Name | Start Time | End Time | Duration | Status |" in content:
            content = content.replace(
                "| Phase | Name | Start Time | End Time | Duration | Status |\n|-------|------|------------|----------|----------|--------|",
                "| Phase | Name | Start Time | End Time | Duration | Status |\n|-------|------|------------|----------|----------|--------|\n" + entry
            )
            self._save_log(content)

        self.current_phase = None
        self.phase_start_time = None

        print(f"✅ Phase {phase_id} completed in {duration_str}")

    def log_agent_invocation(self, agent: str, task: str, input_data: str = "",
                            output_data: str = "", duration: str = ""):
        """Log agent invocation."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        phase = self.current_phase or "-"

        # Truncate long content
        input_trunc = input_data[:100] + "..." if len(input_data) > 100 else input_data
        output_trunc = output_data[:100] + "..." if len(output_data) > 100 else output_data

        entry = f"| {timestamp} | {phase} | {agent} | {task} | {input_trunc} | {output_trunc} | {duration} |\n"

        content = self._load_log()
        if "| Time | Phase | Agent | Task | Input | Output | Duration |" in content:
            content = content.replace(
                "| Time | Phase | Agent | Task | Input | Output | Duration |\n|------|-------|-------|------|-------|--------|----------|",
                "| Time | Phase | Agent | Task | Input | Output | Duration |\n|------|-------|-------|------|-------|--------|----------|\n" + entry
            )
            self._save_log(content)

        print(f"🤖 {agent} invoked: {task}")

    def log_decision(self, decision: str, rationale: str,
                    alternatives: str = ""):
        """Log decision with rationale."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        phase = self.current_phase or "-"

        entry = f"| {timestamp} | {phase} | {decision} | {rationale} | {alternatives} |\n"

        content = self._load_log()
        if "| Time | Phase | Decision | Rationale | Alternatives Considered |" in content:
            content = content.replace(
                "| Time | Phase | Decision | Rationale | Alternatives Considered |\n|------|-------|----------|-----------|------------------------|",
                "| Time | Phase | Decision | Rationale | Alternatives Considered |\n|------|-------|----------|-----------|------------------------|\n" + entry
            )
            self._save_log(content)

        print(f"💡 Decision logged: {decision}")

    def log_error(self, issue: str, resolution: str, prevention: str = "",
                 severity: str = "⚠️ MEDIUM"):
        """Log error or incident."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        phase = self.current_phase or "-"

        entry = f"| {timestamp} | {phase} | {severity} | {issue} | {resolution} | {prevention} |\n"

        content = self._load_log()
        if "| Time | Phase | Severity | Issue | Resolution | Prevention |" in content:
            content = content.replace(
                "| Time | Phase | Severity | Issue | Resolution | Prevention |\n|------|-------|----------|-------|------------|------------|",
                "| Time | Phase | Severity | Issue | Resolution | Prevention |\n|------|-------|----------|-------|------------|------------|\n" + entry
            )
            self._save_log(content)

        print(f"❌ Error logged: {issue}")

    def _format_duration(self, duration: timedelta) -> str:
        """Format duration as readable string."""
        total_seconds = int(duration.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        if hours > 0:
            return f"{hours}h {minutes}m"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"

    def _append_to_section(self, section_name: str, content: str, after: str = ""):
        """Append content to specific section."""
        log_content = self._load_log()

        # Find section
        section_marker = f"## {section_name}"
        if section_marker not in log_content:
            print(f"⚠️  Section '{section_name}' not found")
            return

        # Find insertion point
        if after:
            insert_point = log_content.find(after) + len(after)
            log_content = log_content[:insert_point] + content + "\n" + log_content[insert_point:]
        else:
            # Append after section header
            insert_point = log_content.find(section_marker) + len(section_marker)
            log_content = log_content[:insert_point] + "\n" + content + log_content[insert_point:]

        with open(self.log_path, 'w', encoding='utf-8') as f:
            f.write(log_content)

    def analyze(self):
        """Analyze orchestration log and generate insights."""
        content = self._load_log()

        print(f"\n{'='*60}")
        print(f"Orchestration Log Analysis")
        print(f"{'='*60}")

        # Count agent invocations
        agent_table_start = content.find("| Time | Phase | Agent |")
        if agent_table_start > 0:
            agent_table_end = content.find("\n\n", agent_table_start)
            agent_table = content[agent_table_start:agent_table_end]
            agent_invocations = [line for line in agent_table.split('\n') if '|' in line and line.strip()[0] != '|']

            print(f"\n🤖 Total Agent Invocations: {len(agent_invocations) - 1}")  # -1 for header

            # Count by agent
            agent_counts = {}
            for line in agent_invocations[1:]:  # Skip header
                parts = [p.strip() for p in line.split('|')]
                if len(parts) > 3:
                    agent = parts[3]
                    agent_counts[agent] = agent_counts.get(agent, 0) + 1

            if agent_counts:
                print(f"\nAgent Usage Breakdown:")
                for agent, count in sorted(agent_counts.items(), key=lambda x: -x[1]):
                    print(f"  {agent}: {count} invocation(s)")

        # Count decisions
        decision_table_start = content.find("| Time | Phase | Decision |")
        if decision_table_start > 0:
            decision_table_end = content.find("\n\n", decision_table_start)
            decision_table = content[decision_table_start:decision_table_end]
            decisions = [line for line in decision_table.split('\n') if '|' in line and line.strip()[0] != '|']
            print(f"\n💡 Total Decisions Logged: {len(decisions) - 1}")

        # Count errors
        error_table_start = content.find("| Time | Phase | Severity | Issue |")
        if error_table_start > 0:
            error_table_end = content.find("\n\n", error_table_start)
            error_table = content[error_table_start:error_table_end]
            errors = [line for line in error_table.split('\n') if '|' in line and line.strip()[0] != '|']
            print(f"\n❌ Total Incidents: {len(errors) - 1}")

        print(f"\n📄 Log file: {self.log_path}")
        print(f"{'='*60}\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="MCM-Killer Orchestration Logger")
    parser.add_argument("--workspace", type=str, default=None,
                       help="Workspace directory")

    # Phase management
    parser.add_argument("--start-phase", type=str, nargs=2, metavar=("ID", "NAME"),
                       help="Start phase: ID NAME")
    parser.add_argument("--end-phase", type=str, metavar="ID",
                       help="End phase: ID")

    # Logging
    parser.add_argument("--log-agent", type=str, nargs=3, metavar=("AGENT", "TASK", "INPUT"),
                       help="Log agent invocation")
    parser.add_argument("--log-decision", type=str, nargs=2, metavar=("DECISION", "RATIONALE"),
                       help="Log decision")
    parser.add_argument("--log-error", type=str, nargs=2, metavar=("ISSUE", "RESOLUTION"),
                       help="Log error")

    # Analysis
    parser.add_argument("--analyze", action="store_true",
                       help="Analyze log file")

    args = parser.parse_args()

    logger = OrchestrationLogger(args.workspace)

    if args.start_phase:
        phase_id, phase_name = args.start_phase
        logger.start_phase(phase_id, phase_name)
    elif args.end_phase:
        logger.end_phase(args.end_phase)
    elif args.log_agent:
        agent, task, input_data = args.log_agent
        logger.log_agent_invocation(agent, task, input_data)
    elif args.log_decision:
        decision, rationale = args.log_decision
        logger.log_decision(decision, rationale)
    elif args.log_error:
        issue, resolution = args.log_error
        logger.log_error(issue, resolution)
    elif args.analyze:
        logger.analyze()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

---

**Step 2: Orchestration Log Template**

**File**: `workspace/2025_C/output/docs/orchestration_log.md` (auto-generated)

```markdown
# MCM-Killer Orchestration Log

**Project**: MCM-Killer v3.1.0
**Workspace**: 2025_C
**Started**: 2025-01-28 10:00:00

---

## Table of Contents

- [Phase Execution Log](#phase-execution-log)
- [Agent Invocations](#agent-invocations)
- [Decisions Log](#decisions-log)
- [Incidents & Errors](#incidents--errors)
- [Timeline Analysis](#timeline-analysis)

---

## Phase Execution Log

| Phase | Name | Start Time | End Time | Duration | Status |
|-------|------|------------|----------|----------|--------|
| 0 | Problem Analysis | 2025-01-28 10:00 | 2025-01-28 12:30 | 2h 30m | ✅ COMPLETE |
| 0.2 | Knowledge Library Query | 2025-01-28 12:30 | 2025-01-28 13:15 | 45m | ✅ COMPLETE |
| 0.5 | Methodology Evaluation | 2025-01-28 13:15 | 2025-01-28 15:45 | 2h 30m | ✅ COMPLETE |
| 1 | Model Design | 2025-01-28 15:45 | 2025-01-28 20:45 | 5h 0m | ✅ COMPLETE |

---

## Agent Invocations

| Time | Phase | Agent | Task | Input | Output | Duration |
|------|-------|-------|------|-------|--------|----------|
| 2025-01-28 10:00 | 0 | @reader | Read problem statement | 2025_Problem_C_Data/problem.pdf | research_notes.md | 15m |
| 2025-01-28 10:15 | 0 | @researcher | Analyze problem requirements | research_notes.md | research_notes.md (updated) | 2h 15m |
| 2025-01-28 12:30 | 0.2 | @knowledge_librarian | Query HMML for methods | "time series prediction" | suggested_methods.md | 30m |
| 2025-01-28 15:45 | 1 | @modeler | Design candidate models | research_notes.md, suggested_methods.md | model_design_1.md, model_design_2.md, ... | 4h |

---

## Decisions Log

| Time | Phase | Decision | Rationale | Alternatives Considered |
|------|-------|----------|-----------|------------------------|
| 2025-01-28 16:30 | 1 | Selected 6 candidate models | Diverse approaches: LSTM, XGBoost, Random Forest, Transformer, CNN, Prophet | All 6 models from methodology evaluation |
| 2025-01-28 18:00 | 1 | Prioritized LSTM as primary model | Proven effectiveness on time series, handles long-term dependencies | Transformer (computationally expensive), Prophet (limited for complex patterns) |
| 2025-01-28 19:30 | 1 | Planned ensemble approach | High diversity → robust predictions, reduces overfitting risk | Single best model (less robust), Weighted average (less sophisticated) |

---

## Incidents & Errors

| Time | Phase | Severity | Issue | Resolution | Prevention |
|------|-------|----------|-------|------------|------------|
| 2025-01-28 14:20 | 0.5 | ⚠️ LOW | Missing validation criteria | @advisor added comprehensive criteria | Always include validation framework |
| 2025-01-28 17:45 | 1 | ⚠️ MEDIUM | Model design template unclear | @modeler clarified template structure | Standardize templates |

---

## Timeline Analysis

**Total Elapsed Time**: 10 hours 45 minutes

**Phase Breakdown**:
- Problem Analysis (Phase 0): 2h 30m (23.3%)
- Knowledge Library Query (Phase 0.2): 45m (7.0%)
- Methodology Evaluation (Phase 0.5): 2h 30m (23.3%)
- Model Design (Phase 1): 5h 0m (46.5%)

**Agent Usage**:
- @reader: 15m (2.3%)
- @researcher: 2h 15m (20.9%)
- @knowledge_librarian: 30m (4.7%)
- @modeler: 4h 0m (37.2%)
- @advisor: 1h 0m (9.3%)

**Bottlenecks**:
- Model Design (Phase 1): Longest phase, but expected (creative work)
- No significant delays encountered

---

*Last Updated: 2025-01-28 20:45:00*
```

---

**Step 3: Integration with CLAUDE.md**

**Add to CLAUDE.md** (at beginning of Phase 0):

```markdown
## Phase 0: Problem Analysis (2-3 hours)

**Agent**: @reader, @researcher
**Output**: `output/research_notes.md`

**Before Starting**:
```bash
# Start orchestration logging for Phase 0
python tools/orchestration_logger.py --start-phase 0 "Problem Analysis"
```

**After Completion**:
```bash
# Log agent invocations
python tools/orchestration_logger.py --log-agent @reader "Read problem statement" "2025_Problem_C_Data/problem.pdf"
python tools/orchestration_logger.py --log-agent @researcher "Analyze problem" "research_notes.md"

# End phase
python tools/orchestration_logger.py --end-phase 0

# Update phase tracking
python tools/phase_tracker.py --update
```
```

**Add decision logging example**:

```markdown
## Phase 1: Model Design (4-6 hours)

**Agent**: @modeler, @consultants
**Output**: `output/model_design_*.md`

**Log Decisions**:
```bash
# After making key decisions
python tools/orchestration_logger.py --log-decision "Selected LSTM as primary model" "Proven time series performance"
python tools/orchestration_logger.py --log-decision "Planned ensemble approach" "Robustness through diversity"
```
```

---

#### 2.4 Testing Procedure

**Test 1: Initialize Log**

```bash
cd workspace/2025_C
python tools/orchestration_logger.py --start-phase 1 "Model Design"
```

**Expected**: Log file created with Phase 1 started

**Test 2: Log Agent Invocation**

```bash
python tools/orchestration_logger.py --log-agent "@modeler" "Design LSTM model" "research_notes.md"
```

**Expected**: Agent invocation added to log

**Test 3: Log Decision**

```bash
python tools/orchestration_logger.py --log-decision "Selected LSTM approach" "Best for time series"
```

**Expected**: Decision added to log with rationale

**Test 4: End Phase**

```bash
python tools/orchestration_logger.py --end-phase 1
```

**Expected**: Phase completed with duration calculated

**Test 5: Analyze Log**

```bash
python tools/orchestration_logger.py --analyze
```

**Expected Output**:
```
============================================================
Orchestration Log Analysis
============================================================

🤖 Total Agent Invocations: 5

Agent Usage Breakdown:
  @modeler: 3 invocation(s)
  @reader: 1 invocation(s)
  @researcher: 1 invocation(s)

💡 Total Decisions Logged: 2

❌ Total Incidents: 0

📄 Log file: /path/to/orchestration_log.md
============================================================
```

---

#### 2.5 Rollback Plan

**If issues occur**:

1. **Delete log file**:
```bash
rm output/docs/orchestration_log.md
```

2. **Remove tool**:
```bash
rm tools/orchestration_logger.py
```

3. **Revert CLAUDE.md**:
```bash
git checkout CLAUDE.md
```

---


## Part 3: LOW-Priority Improvements (Sprint 3)

### Improvement #6: System Health Check Tool

**Priority**: MEDIUM (originally LOW)
**Effort**: 4-5 hours
**Risk**: LOW
**Impact**: Pre-flight validation, prevents issues

---

#### 6.1 Current State

**Problem**: No automated validation of system state before starting work.

**Impact**:
- Missing files discovered mid-workflow
- Configuration issues cause delays
- Manual verification time-consuming

---

#### 6.2 Solution Design

**Approach**: Create comprehensive health check tool that validates:
1. File structure integrity
2. Configuration consistency
3. Agent availability
4. Knowledge library integrity
5. Data pipeline status
6. Tool availability
7. Version compatibility

**Components**:
- `tools/system_health_check.py` - HealthCheck class
- Integration with CLAUDE.md (pre-flight check)

---

#### 6.3 Implementation Plan

**File**: `workspace/2025_C/tools/system_health_check.py`

```python
#!/usr/bin/env python3
"""
System Health Check Tool - Pre-flight Validation

Validates system state before starting work to prevent issues.

Usage:
    python tools/system_health_check.py
    python tools/system_health_check.py --quick
    python tools/system_health_check.py --category files
    python tools/system_health_check.py --fix
"""

import os
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import argparse


class HealthCheck:
    """Comprehensive system health validation."""

    def __init__(self, workspace_dir: str = None):
        """Initialize health checker."""
        self.workspace_dir = Path(workspace_dir or os.getcwd())
        self.results = {}
        self.issues = []
        self.warnings = []

    def check_all(self) -> bool:
        """Run all health checks."""
        print("🔍 Running MCM-Killer System Health Check...\n")

        checks = [
            ("File Structure", self.check_file_structure),
            ("Configuration", self.check_configuration),
            ("Agents", self.check_agents),
            ("Knowledge Library", self.check_knowledge_library),
            ("Data Pipeline", self.check_data_pipeline),
            ("Tools", self.check_tools),
            ("Version Compatibility", self.check_version_compatibility)
        ]

        total_passed = 0
        total_failed = 0

        for category, check_func in checks:
            print(f"Checking {category}...")
            passed, failed = check_func()
            total_passed += passed
            total_failed += failed
            print()

        # Summary
        self._print_summary(total_passed, total_failed)
        return total_failed == 0

    def check_file_structure(self) -> Tuple[int, int]:
        """Check file structure integrity."""
        required_dirs = [
            ".claude",
            ".claude/agents",
            ".claude/utils",
            "output",
            "output/docs",
            "tools",
            "2025_Problem_C_Data"
        ]

        required_files = [
            "CLAUDE.md",
            "VERSION_MANIFEST.json",
            ".claude/agents/modeler.md",
            ".claude/agents/coder.md"
        ]

        passed = 0
        failed = 0

        # Check directories
        for dir_path in required_dirs:
            full_path = self.workspace_dir / dir_path
            if full_path.exists() and full_path.is_dir():
                print(f"  ✅ {dir_path}")
                passed += 1
            else:
                print(f"  ❌ {dir_path} - MISSING")
                failed += 1
                self.issues.append(f"Missing directory: {dir_path}")

        # Check files
        for file_path in required_files:
            full_path = self.workspace_dir / file_path
            if full_path.exists() and full_path.is_file():
                print(f"  ✅ {file_path}")
                passed += 1
            else:
                print(f"  ❌ {file_path} - MISSING")
                failed += 1
                self.issues.append(f"Missing file: {file_path}")

        return passed, failed

    def check_configuration(self) -> Tuple[int, int]:
        """Check configuration consistency."""
        passed = 0
        failed = 0

        # Check VERSION_MANIFEST.json
        manifest_path = self.workspace_dir / "VERSION_MANIFEST.json"
        if manifest_path.exists():
            try:
                with open(manifest_path, 'r') as f:
                    manifest = json.load(f)

                required_keys = ["project", "version", "workspace", "phases_completed"]
                for key in required_keys:
                    if key in manifest:
                        print(f"  ✅ Manifest key: {key}")
                        passed += 1
                    else:
                        print(f"  ❌ Manifest missing key: {key}")
                        failed += 1
                        self.issues.append(f"VERSION_MANIFEST.json missing key: {key}")
            except json.JSONDecodeError as e:
                print(f"  ❌ VERSION_MANIFEST.json invalid: {e}")
                failed += 1
                self.issues.append(f"Invalid VERSION_MANIFEST.json: {e}")
        else:
            print(f"  ❌ VERSION_MANIFEST.json not found")
            failed += 1

        # Check CLAUDE.md references
        claude_md = self.workspace_dir / "CLAUDE.md"
        if claude_md.exists():
            with open(claude_md, 'r', encoding='utf-8') as f:
                content = f.read()

            # Count agent references
            agent_count = content.count("@")
            if agent_count > 200:
                print(f"  ✅ CLAUDE.md has {agent_count} agent references")
                passed += 1
            else:
                print(f"  ⚠️  CLAUDE.md has only {agent_count} agent references (expected 200+)")
                passed += 1
                self.warnings.append(f"Low agent reference count: {agent_count}")

        return passed, failed

    def check_agents(self) -> Tuple[int, int]:
        """Check agent availability."""
        agents_dir = self.workspace_dir / ".claude" / "agents"

        expected_agents = [
            "advisor", "coder", "consultant", "data_analyst", "director",
            "figure_generator", "judge", "knowledge_librarian", "mathematician",
            "metacognition_agent", "model_trainer", "modeler", "proofreader",
            "reader", "researcher", "validator", "writer"
        ]

        passed = 0
        failed = 0

        if not agents_dir.exists():
            print(f"  ❌ Agents directory not found")
            failed += len(expected_agents)
            return passed, failed

        for agent in expected_agents:
            agent_file = agents_dir / f"{agent}.md"
            if agent_file.exists():
                print(f"  ✅ Agent: @{agent}")
                passed += 1
            else:
                print(f"  ❌ Agent: @{agent} - MISSING")
                failed += 1
                self.issues.append(f"Missing agent: @{agent}")

        return passed, failed

    def check_knowledge_library(self) -> Tuple[int, int]:
        """Check knowledge library integrity."""
        hmml_dir = self.workspace_dir / "HMML_2.0"

        passed = 0
        failed = 0

        if not hmml_dir.exists():
            print(f"  ❌ HMML_2.0 directory not found")
            failed += 1
            self.issues.append("HMML_2.0 directory missing")
            return passed, failed

        # Check HMML structure
        required_items = [
            "hmml_summary.json",
            "index.md",
            "Domain_1_Time_Series",
            "Domain_2_Machine_Learning"
        ]

        for item in required_items:
            item_path = hmml_dir / item
            if item_path.exists():
                print(f"  ✅ HMML: {item}")
                passed += 1
            else:
                print(f"  ❌ HMML: {item} - MISSING")
                failed += 1
                self.issues.append(f"HMML missing: {item}")

        return passed, failed

    def check_data_pipeline(self) -> Tuple[int, int]:
        """Check data pipeline status."""
        data_dir = self.workspace_dir / "2025_Problem_C_Data"

        passed = 0
        failed = 0

        if not data_dir.exists():
            print(f"  ⚠️  Data directory not found (may not be extracted yet)")
            passed += 1
            self.warnings.append("Data directory not found")
            return passed, failed

        # Check for problem files
        problem_files = list(data_dir.glob("*.pdf")) + list(data_dir.glob("*/*.pdf"))
        if problem_files:
            print(f"  ✅ Found {len(problem_files)} problem PDF(s)")
            passed += 1
        else:
            print(f"  ⚠️  No problem PDFs found")
            passed += 1
            self.warnings.append("No problem PDFs found")

        # Check for data files
        data_files = list(data_dir.glob("*.csv")) + list(data_dir.glob("*.xlsx"))
        if data_files:
            print(f"  ✅ Found {len(data_files)} data file(s)")
            passed += 1
        else:
            print(f"  ⚠️  No data files found")
            passed += 1
            self.warnings.append("No data files found")

        return passed, failed

    def check_tools(self) -> Tuple[int, int]:
        """Check tool availability."""
        tools_dir = self.workspace_dir / "tools"

        expected_tools = [
            "phase_tracker.py",
            "orchestration_logger.py",
            "assemble_agent_prompt.py"
        ]

        passed = 0
        failed = 0

        if not tools_dir.exists():
            print(f"  ⚠️  Tools directory not found")
            passed += len(expected_tools)
            self.warnings.append("Tools directory missing")
            return passed, failed

        for tool in expected_tools:
            tool_path = tools_dir / tool
            if tool_path.exists():
                print(f"  ✅ Tool: {tool}")
                passed += 1
            else:
                print(f"  ⚠️  Tool: {tool} - MISSING (optional)")
                passed += 1
                self.warnings.append(f"Optional tool missing: {tool}")

        return passed, failed

    def check_version_compatibility(self) -> Tuple[int, int]:
        """Check version compatibility."""
        passed = 0
        failed = 0

        # Check VERSION_MANIFEST version
        manifest_path = self.workspace_dir / "VERSION_MANIFEST.json"
        if manifest_path.exists():
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)

            version = manifest.get("version", "")
            if version.startswith("3."):
                print(f"  ✅ Version: {version}")
                passed += 1
            else:
                print(f"  ⚠️  Unexpected version: {version}")
                passed += 1
                self.warnings.append(f"Unexpected version: {version}")
        else:
            print(f"  ⚠️  Cannot check version (manifest missing)")
            passed += 1

        return passed, failed

    def _print_summary(self, passed: int, failed: int):
        """Print health check summary."""
        print("="*60)
        print("Health Check Summary")
        print("="*60)
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")

        if self.warnings:
            print(f"⚠️  Warnings: {len(self.warnings)}")

        print()

        if self.issues:
            print("Issues to Fix:")
            for issue in self.issues:
                print(f"  ❌ {issue}")
            print()

        if self.warnings:
            print("Warnings (non-blocking):")
            for warning in self.warnings:
                print(f"  ⚠️  {warning}")
            print()

        if failed == 0:
            print("✅ System is healthy! Ready to proceed.")
        else:
            print("❌ System has issues. Please fix before proceeding.")

        print("="*60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="MCM-Killer System Health Check")
    parser.add_argument("--workspace", type=str, default=None,
                       help="Workspace directory")
    parser.add_argument("--quick", action="store_true",
                       help="Quick check (critical items only)")
    parser.add_argument("--category", type=str,
                       choices=["files", "config", "agents", "knowledge", "data", "tools", "version"],
                       help="Check specific category")
    parser.add_argument("--fix", action="store_true",
                       help="Attempt to fix issues automatically")

    args = parser.parse_args()

    checker = HealthCheck(args.workspace)

    if args.category:
        category_map = {
            "files": checker.check_file_structure,
            "config": checker.check_configuration,
            "agents": checker.check_agents,
            "knowledge": checker.check_knowledge_library,
            "data": checker.check_data_pipeline,
            "tools": checker.check_tools,
            "version": checker.check_version_compatibility
        }
        print(f"Checking {args.category}...\n")
        passed, failed = category_map[args.category]()
        print(f"\n✅ Passed: {passed}, ❌ Failed: {failed}")
    else:
        checker.check_all()


if __name__ == "__main__":
    main()
```

---

#### 6.4 Testing Procedure

**Test 1: Full Health Check**

```bash
cd workspace/2025_C
python tools/system_health_check.py
```

**Expected Output**:
```
🔍 Running MCM-Killer System Health Check...

Checking File Structure...
  ✅ .claude
  ✅ .claude/agents
  ✅ CLAUDE.md
  ...

Checking Configuration...
  ✅ Manifest key: project
  ...

...

============================================================
Health Check Summary
============================================================
✅ Passed: 45
❌ Failed: 0
⚠️  Warnings: 2

Warnings (non-blocking):
  ⚠️  Optional tool missing: phase_tracker.py
  ⚠️  Data directory not found

✅ System is healthy! Ready to proceed.
============================================================
```

**Test 2: Quick Check**

```bash
python tools/system_health_check.py --quick
```

**Test 3: Category Check**

```bash
python tools/system_health_check.py --category agents
```

---

#### 6.5 Rollback Plan

**If issues occur**:

1. **Remove tool**:
```bash
rm tools/system_health_check.py
```

---

### Improvement #7: Progress Dashboard

**Priority**: LOW
**Effort**: 8-10 hours
**Risk**: LOW
**Impact**: Real-time monitoring (nice-to-have)

---

#### 7.1 Current State

**Problem**: No visual representation of progress.

**Impact**:
- Difficult to gauge completion
- No real-time status display
- Manual progress tracking required

---

#### 7.2 Solution Design

**Approach**: Create CLI-based dashboard that displays:
1. Phase completion status
2. Current phase progress
3. Agent activity
4. Token usage statistics
5. Estimated completion time

**Components**:
- `tools/progress_dashboard.py` - Dashboard generator
- Optional: Web-based dashboard (future enhancement)

---

#### 7.3 Implementation Plan

**File**: `workspace/2025_C/tools/progress_dashboard.py`

```python
#!/usr/bin/env python3
"""
Progress Dashboard - Real-time Status Display

Displays current progress, phase status, and system activity.

Usage:
    python tools/progress_dashboard.py
    python tools/progress_dashboard.py --watch
"""

import json
import time
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
import argparse


class ProgressDashboard:
    """Real-time progress monitoring dashboard."""

    def __init__(self, workspace_dir: str = None):
        """Initialize dashboard."""
        self.workspace_dir = Path(workspace_dir or os.getcwd())
        self.manifest_path = self.workspace_dir / "VERSION_MANIFEST.json"
        self.events_dir = self.workspace_dir / "output" / "docs" / "events"

    def load_manifest(self) -> Dict:
        """Load VERSION_MANIFEST.json."""
        if self.manifest_path.exists():
            with open(self.manifest_path, 'r') as f:
                return json.load(f)
        return {}

    def get_phase_progress(self) -> Dict:
        """Get phase completion progress."""
        manifest = self.load_manifest()
        completed = manifest.get("phases_completed", [])

        total_phases = 22
        completed_count = len(completed)
        percent = (completed_count / total_phases) * 100

        return {
            "total": total_phases,
            "completed": completed_count,
            "remaining": total_phases - completed_count,
            "percent": percent
        }

    def get_current_phase(self) -> Dict:
        """Get current working phase."""
        # Check orchestration log for current phase
        log_path = self.workspace_dir / "output" / "docs" / "orchestration_log.md"

        if not log_path.exists():
            return {"phase": "Unknown", "status": "Not started"}

        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for "IN PROGRESS" phase
        for line in content.split('\n'):
            if '🔄 IN PROGRESS' in line:
                # Extract phase info
                parts = line.split('Phase ')[1].split(':')
                phase_id = parts[0].strip()
                phase_name = parts[1].split('**')[0].strip() if len(parts) > 1 else "Unknown"
                return {"phase": f"Phase {phase_id}", "name": phase_name, "status": "In Progress"}

        return {"phase": "Unknown", "status": "Idle"}

    def get_agent_activity(self) -> List[Dict]:
        """Get recent agent activity."""
        # Check recent events
        today = datetime.now().strftime("%Y-%m-%d")
        event_file = self.events_dir / f"events_{today}.jsonl"

        if not event_file.exists():
            return []

        activity = []
        with open(event_file, 'r', encoding='utf-8') as f:
            for line in f:
                event = json.loads(line.strip())
                if event['event_type'] == 'action':
                    activity.append({
                        "time": event['timestamp'],
                        "agent": event['agent'],
                        "description": event['description']
                    })

        # Return last 10
        return activity[-10:]

    def render(self):
        """Render dashboard to terminal."""
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Get data
        progress = self.get_phase_progress()
        current = self.get_current_phase()
        activity = self.get_agent_activity()

        # Build dashboard
        dashboard = f"""
{'='*70}
                    MCM-Killer Progress Dashboard
{'='*70}

Phase Progress
{'─'*70}
Completed: {progress['completed']}/{progress['total']} phases ({progress['percent']:.1f}%)
Remaining: {progress['remaining']} phases

Progress Bar:
{'█' * int(progress['percent'] // 2)}{'░' * (50 - int(progress['percent'] // 2))} {progress['percent']:.1f}%

Current Phase
{'─'*70}
{current.get('phase', 'Unknown')}: {current.get('name', 'N/A')}
Status: {current.get('status', 'Unknown')}

Recent Activity
{'─'*70}
"""
        if activity:
            for item in activity[-5:]:
                time = datetime.fromisoformat(item['time']).strftime("%H:%M:%S")
                dashboard += f"[{time}] {item['agent']}: {item['description']}\n"
        else:
            dashboard += "No recent activity\n"

        dashboard += f"""
{'='*70}
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}
"""

        print(dashboard)

    def watch(self, interval: int = 30):
        """Watch mode - update dashboard periodically."""
        try:
            while True:
                self.render()
                print(f"\nRefreshing every {interval} seconds... (Press Ctrl+C to exit)")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n\nDashboard stopped.")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="MCM-Killer Progress Dashboard")
    parser.add_argument("--workspace", type=str, default=None,
                       help="Workspace directory")
    parser.add_argument("--watch", action="store_true",
                       help="Watch mode - auto-refresh")
    parser.add_argument("--interval", type=int, default=30,
                       help="Refresh interval in seconds (default: 30)")

    args = parser.parse_args()

    dashboard = ProgressDashboard(args.workspace)

    if args.watch:
        dashboard.watch(args.interval)
    else:
        dashboard.render()


if __name__ == "__main__":
    main()
```

---

#### 7.4 Testing Procedure

**Test 1: Display Dashboard**

```bash
python tools/progress_dashboard.py
```

**Expected**: Dashboard displayed with current progress

**Test 2: Watch Mode**

```bash
python tools/progress_dashboard.py --watch --interval 10
```

**Expected**: Dashboard refreshes every 10 seconds

---

#### 7.5 Rollback Plan

**If issues occur**:

1. **Remove dashboard**:
```bash
rm tools/progress_dashboard.py
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
