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


def start_phase(phase: str, agent: str, is_rerun: bool = False) -> Dict[str, Any]:
    """
    Record the start of a phase or a rerun attempt.

    Args:
        phase: Phase identifier (e.g., "1", "4.5", "7A")
        agent: Agent name (e.g., "modeler", "code_translator")
        is_rerun: If True, this is a rerun (accumulate time from previous attempts)

    Returns:
        Dictionary with phase start info
    """
    log_path = get_log_path(phase)

    # Check if this is a rerun (file exists and we want to accumulate)
    existing_data = None
    if is_rerun and log_path.exists():
        with open(log_path, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)

    current_time = datetime.now().isoformat()

    if existing_data and is_rerun:
        # RERUN MODE: Accumulate time from previous attempts
        attempts = existing_data.get('attempts', [])

        # If previous attempt was completed, archive it
        if existing_data.get('status') == 'completed' or existing_data.get('end_time'):
            previous_attempt = {
                "attempt_number": len(attempts) + 1,
                "start_time": existing_data.get('current_attempt_start', existing_data.get('start_time')),
                "end_time": existing_data.get('end_time'),
                "duration_minutes": existing_data.get('current_attempt_duration', existing_data.get('duration_minutes', 0)),
                "status": existing_data.get('status', 'completed'),
                "verdict": existing_data.get('time_verdict', 'UNKNOWN')
            }
            attempts.append(previous_attempt)

        # Calculate cumulative duration from all previous attempts
        cumulative_duration = sum(a.get('duration_minutes', 0) or 0 for a in attempts)

        data = {
            "phase": phase,
            "phase_name": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("name", "Unknown"),
            "agent": agent,
            "start_time": existing_data.get('start_time'),  # Original first start
            "current_attempt_start": current_time,  # This attempt's start
            "end_time": None,
            "duration_minutes": None,
            "current_attempt_duration": None,
            "cumulative_duration": cumulative_duration,
            "attempt_count": len(attempts) + 1,
            "attempts": attempts,
            "status": "in_progress",
            "expected_min": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("min_min", 0),
            "expected_max": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("max_min", 0),
            "threshold_pct": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("threshold_pct", 1.0),
            "previous_output_path": existing_data.get('output_path', None),
        }
    else:
        # FRESH START: First attempt
        data = {
            "phase": phase,
            "phase_name": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("name", "Unknown"),
            "agent": agent,
            "start_time": current_time,
            "current_attempt_start": current_time,
            "end_time": None,
            "duration_minutes": None,
            "current_attempt_duration": None,
            "cumulative_duration": 0,
            "attempt_count": 1,
            "attempts": [],
            "status": "in_progress",
            "expected_min": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("min_min", 0),
            "expected_max": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("max_min", 0),
            "threshold_pct": PHASE_TIME_REQUIREMENTS.get(phase, {}).get("threshold_pct", 1.0),
            "previous_output_path": None,
        }

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    attempt_msg = f" (Attempt #{data['attempt_count']})" if data['attempt_count'] > 1 else ""
    print(f"[TIME_TRACKER] Phase {phase} started by @{agent} at {current_time}{attempt_msg}")
    if data['cumulative_duration'] > 0:
        print(f"[TIME_TRACKER] Cumulative time from previous attempts: {data['cumulative_duration']:.1f} min")
    if data.get('previous_output_path'):
        print(f"[TIME_TRACKER] Previous output to reference: {data['previous_output_path']}")

    return data


def end_phase(phase: str, agent: str, status: str = "completed", output_path: str = None) -> Dict[str, Any]:
    """
    Record the end of a phase and calculate duration (including cumulative).

    Args:
        phase: Phase identifier
        agent: Agent name
        status: Status (completed, partial, failed)
        output_path: Path to the output file/directory for this phase (for rerun reference)

    Returns:
        Dictionary with phase timing info including validation result
    """
    log_path = get_log_path(phase)

    if not log_path.exists():
        raise ValueError(f"Phase {phase} was never started. Call start_phase first.")

    with open(log_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    end_time = datetime.now()
    # Use current_attempt_start if available (for reruns), otherwise use start_time
    attempt_start = datetime.fromisoformat(data.get('current_attempt_start', data['start_time']))
    current_attempt_duration = (end_time - attempt_start).total_seconds() / 60

    # Calculate cumulative duration
    previous_cumulative = data.get('cumulative_duration', 0) or 0
    total_cumulative = previous_cumulative + current_attempt_duration

    data['end_time'] = end_time.isoformat()
    data['current_attempt_duration'] = round(current_attempt_duration, 2)
    data['duration_minutes'] = round(current_attempt_duration, 2)  # Keep for backward compatibility
    data['cumulative_duration'] = round(total_cumulative, 2)
    data['status'] = status
    if output_path:
        data['output_path'] = output_path

    # Use CUMULATIVE duration for validation, not single attempt
    min_threshold = data['expected_min']
    data['min_threshold'] = min_threshold

    # Validation uses cumulative_duration
    if total_cumulative < min_threshold:
        data['time_verdict'] = "INSUFFICIENT"
        data['time_message'] = f"Cumulative {total_cumulative:.1f} min < MINIMUM {min_threshold:.1f} min - REJECT"
    elif total_cumulative > data['expected_max'] * 2:
        data['time_verdict'] = "EXCESSIVE"
        data['time_message'] = f"Cumulative {total_cumulative:.1f} min > 2x max {data['expected_max']} min"
    else:
        data['time_verdict'] = "ACCEPTABLE"
        data['time_message'] = f"Cumulative {total_cumulative:.1f} min within acceptable range"

    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    attempt_count = data.get('attempt_count', 1)
    print(f"[TIME_TRACKER] Phase {phase} ended (Attempt #{attempt_count}). This attempt: {current_attempt_duration:.1f} min. Cumulative: {total_cumulative:.1f} min. Verdict: {data['time_verdict']}")
    return data


def validate_phase(phase: str) -> Dict[str, Any]:
    """
    Validate phase timing using CUMULATIVE duration across all attempts.

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

    # Use CUMULATIVE duration for validation
    cumulative_duration = data.get('cumulative_duration', data.get('duration_minutes', 0)) or 0
    current_attempt_duration = data.get('current_attempt_duration', data.get('duration_minutes', 0)) or 0
    expected_min = data.get('expected_min', 0)
    expected_max = data.get('expected_max', 0)
    attempt_count = data.get('attempt_count', 1)
    attempts = data.get('attempts', [])

    result = {
        "phase": phase,
        "phase_name": data.get('phase_name', 'Unknown'),
        "agent": data.get('agent', 'Unknown'),
        "current_attempt_duration": current_attempt_duration,
        "cumulative_duration": cumulative_duration,
        "attempt_count": attempt_count,
        "attempt_history": attempts,
        "expected_range": f"{expected_min}-{expected_max} min",
        "minimum": f"{expected_min} min (HARD FLOOR)",
        "start_time": data.get('start_time'),
        "end_time": data.get('end_time'),
        "previous_output_path": data.get('previous_output_path'),
        "output_path": data.get('output_path'),
    }

    # Validation uses CUMULATIVE duration
    if cumulative_duration < expected_min:
        result['verdict'] = "REJECT_INSUFFICIENT_TIME"
        result['action'] = "RERUN_REQUIRED"
        result['message'] = f"Cumulative {cumulative_duration:.1f} min across {attempt_count} attempt(s) < MINIMUM {expected_min} min. FORCE RERUN."
        result['additional_time_needed'] = round(expected_min - cumulative_duration, 1)
    elif cumulative_duration > expected_max * 2:
        result['verdict'] = "WARN_SLOW"
        result['action'] = "NOTE"
        result['message'] = f"Cumulative {cumulative_duration:.1f} min much longer than max {expected_max} min."
    else:
        result['verdict'] = "APPROVE"
        result['action'] = "PROCEED"
        result['message'] = f"Cumulative {cumulative_duration:.1f} min across {attempt_count} attempt(s) meets MINIMUM."

    return result


def list_phases() -> None:
    """List all phase timing logs with cumulative duration tracking."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logs = sorted(LOG_DIR.glob("phase_*_timing.json"))

    print("\n=== Phase Timing Logs (Cumulative Time Tracking) ===\n")
    for log in logs:
        with open(log, 'r', encoding='utf-8') as f:
            data = json.load(f)

        phase = data.get('phase', '?')
        name = data.get('phase_name', 'Unknown')
        status = data.get('status', 'unknown')
        current_duration = data.get('current_attempt_duration') or data.get('duration_minutes')
        cumulative_duration = data.get('cumulative_duration', current_duration)
        attempt_count = data.get('attempt_count', 1)
        verdict = data.get('time_verdict', 'N/A')

        # Handle None duration for in-progress phases
        current_str = f"{current_duration:.1f}" if current_duration is not None else "N/A"
        cumulative_str = f"{cumulative_duration:.1f}" if cumulative_duration is not None else "N/A"
        print(f"Phase {phase:5s} ({name:25s}): {status:12s} | Attempt #{attempt_count} | This: {current_str:>6} min | Cumulative: {cumulative_str:>6} min | {verdict}")

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
    start_parser.add_argument('--rerun', '-r', action='store_true',
                              help='This is a rerun (accumulate time from previous attempts)')

    # end command
    end_parser = subparsers.add_parser('end', help='End timing a phase')
    end_parser.add_argument('--phase', '-p', required=True, help='Phase ID')
    end_parser.add_argument('--agent', '-a', required=True, help='Agent name')
    end_parser.add_argument('--status', '-s', default='completed',
                           choices=['completed', 'partial', 'failed'])
    end_parser.add_argument('--output-path', '-o', default=None,
                           help='Path to the output file/directory for this phase (for rerun reference)')

    # validate command
    validate_parser = subparsers.add_parser('validate', help='Validate phase timing')
    validate_parser.add_argument('--phase', '-p', required=True, help='Phase ID')

    # list command
    list_parser = subparsers.add_parser('list', help='List all phase timing logs')

    args = parser.parse_args()

    if args.command == 'start':
        result = start_phase(args.phase, args.agent, is_rerun=args.rerun)
        print(json.dumps(result, indent=2))
    elif args.command == 'end':
        result = end_phase(args.phase, args.agent, args.status, output_path=args.output_path)
        print(json.dumps(result, indent=2))
    elif args.command == 'validate':
        result = validate_phase(args.phase)
        print(json.dumps(result, indent=2))
    elif args.command == 'list':
        list_phases()
