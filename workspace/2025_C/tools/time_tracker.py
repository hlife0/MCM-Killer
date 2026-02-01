#!/usr/bin/env python3
"""
Phase Time Tracker for MCM-Killer Agent Coordination.

This script provides functions for agents to record phase timing
and for time_validator to validate phase durations.

Usage by agents:
    python time_tracker.py start --phase 1 --agent modeler
    python time_tracker.py end --phase 1 --agent modeler
    python time_tracker.py validate --phase 1

Usage in Python:
    from time_tracker import start_phase, end_phase, validate_phase
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

# Phase time requirements - MINIMUM values aligned with CLAUDE.md (v3.3.0)
# threshold_pct is kept for legacy compatibility but NOT used for enforcement
# min_min IS the hard floor - no threshold reduction applied
PHASE_TIME_REQUIREMENTS = {
    "0":   {"name": "Problem Understanding",   "min_min": 35,  "max_min": 60,   "threshold_pct": 1.0},
    "0.1": {"name": "External Resources",      "min_min": 15,  "max_min": 30,   "threshold_pct": 1.0},
    "0.2": {"name": "Knowledge Retrieval",     "min_min": 20,  "max_min": 30,   "threshold_pct": 1.0},
    "0.5": {"name": "Methodology Gate",        "min_min": 25,  "max_min": 40,   "threshold_pct": 1.0},
    "1":   {"name": "Model Design",            "min_min": 120, "max_min": 360,  "threshold_pct": 1.0},
    "1.5": {"name": "Time Validation",         "min_min": 10,  "max_min": 20,   "threshold_pct": 1.0},
    "2":   {"name": "Feasibility Check",       "min_min": 35,  "max_min": 60,   "threshold_pct": 1.0},
    "3":   {"name": "Data Processing",         "min_min": 75,  "max_min": 120,  "threshold_pct": 1.0},
    "4":   {"name": "Code Translation",        "min_min": 75,  "max_min": 120,  "threshold_pct": 1.0},
    "4.5": {"name": "Fidelity Check",          "min_min": 10,  "max_min": 20,   "threshold_pct": 1.0},
    "5":   {"name": "Model Training",          "min_min": 180, "max_min": 2880, "threshold_pct": 1.0},  # 3 hours MINIMUM per CLAUDE.md
    "5.5": {"name": "Data Authenticity",       "min_min": 10,  "max_min": 20,   "threshold_pct": 1.0},
    "5.8": {"name": "Insight Extraction",      "min_min": 25,  "max_min": 40,   "threshold_pct": 1.0},
    "6":   {"name": "Visualization",           "min_min": 35,  "max_min": 60,   "threshold_pct": 1.0},
    "6.5": {"name": "Visual Gate",             "min_min": 10,  "max_min": 20,   "threshold_pct": 1.0},
    "7A":  {"name": "Paper Framework",         "min_min": 25,  "max_min": 40,   "threshold_pct": 1.0},
    "7B":  {"name": "Model Sections",          "min_min": 60,  "max_min": 90,   "threshold_pct": 1.0},
    "7C":  {"name": "Results Integration",     "min_min": 45,  "max_min": 60,   "threshold_pct": 1.0},
    "7D":  {"name": "Analysis Sections",       "min_min": 25,  "max_min": 40,   "threshold_pct": 1.0},
    "7E":  {"name": "Conclusions",             "min_min": 32,  "max_min": 45,   "threshold_pct": 1.0},
    "7F":  {"name": "LaTeX Compilation",       "min_min": 15,  "max_min": 30,   "threshold_pct": 1.0},
    "7.5": {"name": "LaTeX Gate",              "min_min": 10,  "max_min": 20,   "threshold_pct": 1.0},
    "8":   {"name": "Summary",                 "min_min": 35,  "max_min": 60,   "threshold_pct": 1.0},
    "9":   {"name": "Polish",                  "min_min": 35,  "max_min": 60,   "threshold_pct": 1.0},
    "9.1": {"name": "Mock Judging",            "min_min": 20,  "max_min": 45,   "threshold_pct": 1.0},
    "9.5": {"name": "Editor Feedback",         "min_min": 20,  "max_min": 60,   "threshold_pct": 1.0},
    "10":  {"name": "Final Review",            "min_min": 35,  "max_min": 60,   "threshold_pct": 1.0},
    "11":  {"name": "Self-Evolution",          "min_min": 10,  "max_min": 20,   "threshold_pct": 1.0},
}

LOG_DIR = Path("output/implementation/logs")


def get_log_path(phase: str) -> Path:
    """Get the log file path for a phase."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    return LOG_DIR / f"phase_{phase}_timing.json"


def start_phase(phase: str, agent: str) -> Dict[str, Any]:
    """
    Record the start of a phase.

    Args:
        phase: Phase identifier (e.g., "1", "4.5", "7A")
        agent: Agent name (e.g., "modeler", "code_translator")

    Returns:
        Dictionary with phase start info
    """
    log_path = get_log_path(phase)

    data = {
        "phase": phase,
        "phase_name": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("name", "Unknown"),
        "agent": agent,
        "start_time": datetime.now().isoformat(),
        "end_time": None,
        "duration_minutes": None,
        "status": "in_progress",
        "expected_min": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("min_min", 0),
        "expected_max": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("max_min", 0),
        "threshold_pct": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("threshold_pct", 0.70),
    }

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"[TIME_TRACKER] Phase {phase} started by @{agent} at {data['start_time']}")
    return data


def end_phase(phase: str, agent: str, status: str = "completed") -> Dict[str, Any]:
    """
    Record the end of a phase and calculate duration.

    Args:
        phase: Phase identifier
        agent: Agent name
        status: Status (completed, partial, failed)

    Returns:
        Dictionary with phase timing info including validation result
    """
    log_path = get_log_path(phase)

    if not log_path.exists():
        raise ValueError(f"Phase {phase} was never started. Call start_phase first.")

    with open(log_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    end_time = datetime.now()
    start_time = datetime.fromisoformat(data['start_time'])
    duration = (end_time - start_time).total_seconds() / 60

    data['end_time'] = end_time.isoformat()
    data['duration_minutes'] = round(duration, 2)
    data['status'] = status

    # Calculate threshold - min_min IS the hard floor, no reduction (v3.3.0)
    # threshold_pct is now always 1.0, so min_threshold == expected_min
    min_threshold = data['expected_min']  # Use MINIMUM directly, no threshold reduction
    data['min_threshold'] = min_threshold

    # Preliminary validation - MINIMUM is the hard floor
    if duration < min_threshold:
        data['time_verdict'] = "INSUFFICIENT"
        data['time_message'] = f"Duration {duration:.1f} min < MINIMUM {min_threshold:.1f} min - REJECT"
    elif duration > data['expected_max'] * 2:
        data['time_verdict'] = "EXCESSIVE"
        data['time_message'] = f"Duration {duration:.1f} min > 2x max {data['expected_max']} min"
    else:
        data['time_verdict'] = "ACCEPTABLE"
        data['time_message'] = f"Duration {duration:.1f} min within acceptable range"

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"[TIME_TRACKER] Phase {phase} ended. Duration: {duration:.1f} min. Verdict: {data['time_verdict']}")
    return data


def validate_phase(phase: str) -> Dict[str, Any]:
    """
    Validate phase timing (called by time_validator).

    Args:
        phase: Phase identifier

    Returns:
        Validation result with verdict and recommendation
    """
    log_path = get_log_path(phase)

    if not log_path.exists():
        return {
            "phase": phase,
            "verdict": "NO_DATA",
            "message": f"No timing log found for phase {phase}"
        }

    with open(log_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data.get('status') == 'in_progress':
        return {
            "phase": phase,
            "verdict": "IN_PROGRESS",
            "message": f"Phase {phase} is still in progress"
        }

    duration = data.get('duration_minutes', 0)
    min_threshold = data.get('min_threshold', 0)
    expected_min = data.get('expected_min', 0)
    expected_max = data.get('expected_max', 0)

    result = {
        "phase": phase,
        "phase_name": data.get('phase_name', 'Unknown'),
        "agent": data.get('agent', 'Unknown'),
        "duration_minutes": duration,
        "expected_range": f"{expected_min}-{expected_max} min",
        "minimum": f"{expected_min} min (HARD FLOOR - no threshold reduction)",
        "start_time": data.get('start_time'),
        "end_time": data.get('end_time'),
    }

    # MINIMUM is the hard floor - duration < min_min = REJECT (v3.3.0)
    if duration < expected_min:
        result['verdict'] = "REJECT_INSUFFICIENT_TIME"
        result['action'] = "RERUN_REQUIRED"
        result['message'] = f"Phase completed in {duration:.1f} min, below MINIMUM of {expected_min} min. FORCE RERUN."
    elif duration > expected_max * 2:
        result['verdict'] = "WARN_SLOW"
        result['action'] = "NOTE"
        result['message'] = f"Phase took {duration:.1f} min, much longer than max {expected_max} min. Check for issues."
    else:
        result['verdict'] = "APPROVE"
        result['action'] = "PROCEED"
        result['message'] = f"Phase completed in {duration:.1f} min, within acceptable range."

    return result


def list_phases() -> None:
    """List all phase timing logs."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logs = sorted(LOG_DIR.glob("phase_*_timing.json"))

    print("\n=== Phase Timing Logs ===\n")
    for log in logs:
        with open(log, 'r', encoding='utf-8') as f:
            data = json.load(f)

        phase = data.get('phase', '?')
        name = data.get('phase_name', 'Unknown')
        status = data.get('status', 'unknown')
        duration = data.get('duration_minutes')
        verdict = data.get('time_verdict', 'N/A')

        # Handle None duration for in-progress phases
        duration_str = f"{duration:.2f}" if duration is not None else "N/A"
        print(f"Phase {phase:5s} ({name:25s}): {status:12s} | {duration_str:>6} min | {verdict}")

    if not logs:
        print("No timing logs found.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Phase Time Tracker for MCM-Killer")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # start command
    start_parser = subparsers.add_parser('start', help='Start timing a phase')
    start_parser.add_argument('--phase', '-p', required=True, help='Phase ID (e.g., 1, 4.5, 7A)')
    start_parser.add_argument('--agent', '-a', required=True, help='Agent name')

    # end command
    end_parser = subparsers.add_parser('end', help='End timing a phase')
    end_parser.add_argument('--phase', '-p', required=True, help='Phase ID')
    end_parser.add_argument('--agent', '-a', required=True, help='Agent name')
    end_parser.add_argument('--status', '-s', default='completed',
                           choices=['completed', 'partial', 'failed'])

    # validate command
    validate_parser = subparsers.add_parser('validate', help='Validate phase timing')
    validate_parser.add_argument('--phase', '-p', required=True, help='Phase ID')

    # list command
    list_parser = subparsers.add_parser('list', help='List all phase timing logs')

    args = parser.parse_args()

    if args.command == 'start':
        result = start_phase(args.phase, args.agent)
        print(json.dumps(result, indent=2))
    elif args.command == 'end':
        result = end_phase(args.phase, args.agent, args.status)
        print(json.dumps(result, indent=2))
    elif args.command == 'validate':
        result = validate_phase(args.phase)
        print(json.dumps(result, indent=2))
    elif args.command == 'list':
        list_phases()
