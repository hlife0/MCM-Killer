#!/usr/bin/env python3
"""
Log Analyzer: Compress training logs and extract insights for @metacognition_agent.

Usage:
    python log_analyzer.py <training_log> <output_json>

Example:
    python log_analyzer.py output/implementation/logs/training_full.log logs/summary.json

This script:
1. Parses training logs (potentially GBs of text)
2. Extracts key metrics (loss, accuracy, warnings, errors)
3. Calculates oscillation score and convergence characteristics
4. Identifies critical events (NaN, gradient explosion, etc.)
5. Produces a compact JSON summary (<10KB) for @metacognition_agent

The output summary is the primary INPUT for Phase 5.8 (Insight Extraction).
"""

import os
import re
import sys
import json
import math
import statistics
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from collections import defaultdict


# ============================================================================
# LOG PARSING PATTERNS
# ============================================================================

# Common patterns for training log parsing
PATTERNS = {
    # Epoch markers
    "epoch": re.compile(
        r'epoch[:\s]+(\d+)',
        re.IGNORECASE
    ),

    # Loss values
    "loss": re.compile(
        r'(?:loss|train_loss|training_loss)[:\s=]+([0-9.e+-]+)',
        re.IGNORECASE
    ),

    # Validation loss
    "val_loss": re.compile(
        r'(?:val_loss|validation_loss|test_loss)[:\s=]+([0-9.e+-]+)',
        re.IGNORECASE
    ),

    # Accuracy
    "accuracy": re.compile(
        r'(?:accuracy|acc|train_acc)[:\s=]+([0-9.]+)',
        re.IGNORECASE
    ),

    # Learning rate
    "learning_rate": re.compile(
        r'(?:lr|learning_rate)[:\s=]+([0-9.e+-]+)',
        re.IGNORECASE
    ),

    # Gradient norm
    "gradient_norm": re.compile(
        r'(?:gradient_norm|grad_norm|norm)[:\s=]+([0-9.e+-]+)',
        re.IGNORECASE
    ),

    # R-hat (for MCMC)
    "rhat": re.compile(
        r'(?:r_hat|rhat|r-hat)[:\s=]+([0-9.]+)',
        re.IGNORECASE
    ),

    # RMSE
    "rmse": re.compile(
        r'(?:rmse)[:\s=]+([0-9.]+)',
        re.IGNORECASE
    ),

    # Warnings
    "warning": re.compile(
        r'(?:warning|warn)[:\s]+(.+)',
        re.IGNORECASE
    ),

    # Errors
    "error": re.compile(
        r'(?:error|exception|traceback)[:\s]+(.+)',
        re.IGNORECASE
    ),

    # NaN/Inf detection
    "nan_inf": re.compile(
        r'(nan|inf|-inf|infinity)',
        re.IGNORECASE
    ),

    # Convergence messages
    "convergence": re.compile(
        r'(converged|convergence|not converging|failed to converge)',
        re.IGNORECASE
    ),

    # Time per epoch
    "time": re.compile(
        r'(?:time|duration|elapsed)[:\s=]+([0-9.]+)\s*(?:s|sec|seconds)?',
        re.IGNORECASE
    )
}


# ============================================================================
# CRITICAL EVENT PATTERNS
# ============================================================================

CRITICAL_PATTERNS = {
    "gradient_explosion": [
        r'gradient.*explo',
        r'grad.*norm.*(?:1e[5-9]|1e[1-9]\d)',
        r'exploding.*gradient',
        r'overflow'
    ],
    "gradient_vanishing": [
        r'gradient.*vanish',
        r'grad.*norm.*(?:1e-[5-9]|1e-[1-9]\d)',
        r'vanishing.*gradient'
    ],
    "nan_loss": [
        r'loss.*nan',
        r'nan.*loss',
        r'loss.*inf'
    ],
    "divergence": [
        r'diverge',
        r'not.*converg',
        r'failed.*converg',
        r'r[-_]?hat.*(?:1\.[1-9]|[2-9])'
    ],
    "memory_issue": [
        r'out.*of.*memory',
        r'oom',
        r'cuda.*memory',
        r'memory.*error'
    ],
    "numerical_instability": [
        r'numerical.*instab',
        r'underflow',
        r'overflow',
        r'ill.*condition'
    ]
}


# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================

def parse_log_file(log_path: str) -> Dict[str, Any]:
    """Parse a training log file and extract all relevant information."""

    data = {
        "epochs": [],
        "loss_values": [],
        "val_loss_values": [],
        "accuracy_values": [],
        "gradient_norms": [],
        "learning_rates": [],
        "rhat_values": [],
        "rmse_values": [],
        "warnings": [],
        "errors": [],
        "times": [],
        "raw_lines": 0,
        "critical_events": defaultdict(list)
    }

    current_epoch = 0

    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            data["raw_lines"] += 1

            # Extract epoch
            epoch_match = PATTERNS["epoch"].search(line)
            if epoch_match:
                current_epoch = int(epoch_match.group(1))
                if current_epoch not in data["epochs"]:
                    data["epochs"].append(current_epoch)

            # Extract loss
            loss_match = PATTERNS["loss"].search(line)
            if loss_match:
                try:
                    loss = float(loss_match.group(1))
                    if not math.isnan(loss) and not math.isinf(loss):
                        data["loss_values"].append({
                            "epoch": current_epoch,
                            "value": loss,
                            "line": line_num
                        })
                except ValueError:
                    pass

            # Extract validation loss
            val_loss_match = PATTERNS["val_loss"].search(line)
            if val_loss_match:
                try:
                    val_loss = float(val_loss_match.group(1))
                    if not math.isnan(val_loss) and not math.isinf(val_loss):
                        data["val_loss_values"].append({
                            "epoch": current_epoch,
                            "value": val_loss,
                            "line": line_num
                        })
                except ValueError:
                    pass

            # Extract accuracy
            acc_match = PATTERNS["accuracy"].search(line)
            if acc_match:
                try:
                    acc = float(acc_match.group(1))
                    data["accuracy_values"].append({
                        "epoch": current_epoch,
                        "value": acc,
                        "line": line_num
                    })
                except ValueError:
                    pass

            # Extract gradient norm
            grad_match = PATTERNS["gradient_norm"].search(line)
            if grad_match:
                try:
                    grad = float(grad_match.group(1))
                    data["gradient_norms"].append({
                        "epoch": current_epoch,
                        "value": grad,
                        "line": line_num
                    })
                except ValueError:
                    pass

            # Extract R-hat
            rhat_match = PATTERNS["rhat"].search(line)
            if rhat_match:
                try:
                    rhat = float(rhat_match.group(1))
                    data["rhat_values"].append({
                        "epoch": current_epoch,
                        "value": rhat,
                        "line": line_num
                    })
                except ValueError:
                    pass

            # Extract warnings
            warn_match = PATTERNS["warning"].search(line)
            if warn_match:
                data["warnings"].append({
                    "epoch": current_epoch,
                    "message": warn_match.group(1)[:200],  # Truncate
                    "line": line_num
                })

            # Extract errors
            error_match = PATTERNS["error"].search(line)
            if error_match:
                data["errors"].append({
                    "epoch": current_epoch,
                    "message": error_match.group(1)[:200],
                    "line": line_num
                })

            # Check for critical events
            line_lower = line.lower()
            for event_type, patterns in CRITICAL_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, line_lower):
                        data["critical_events"][event_type].append({
                            "epoch": current_epoch,
                            "line": line_num,
                            "context": line[:200].strip()
                        })
                        break

            # Check for NaN/Inf
            if PATTERNS["nan_inf"].search(line):
                data["critical_events"]["nan_inf"].append({
                    "epoch": current_epoch,
                    "line": line_num,
                    "context": line[:200].strip()
                })

    return data


def calculate_oscillation(values: List[Dict]) -> Dict[str, Any]:
    """Calculate oscillation score from a series of values."""

    if len(values) < 3:
        return {
            "score": 0,
            "severity": "Insufficient data",
            "trend": "unknown"
        }

    raw_values = [v["value"] for v in values]

    # Calculate first derivative (changes between consecutive values)
    derivatives = []
    for i in range(1, len(raw_values)):
        derivatives.append(raw_values[i] - raw_values[i-1])

    if not derivatives:
        return {
            "score": 0,
            "severity": "Insufficient data",
            "trend": "unknown"
        }

    # Oscillation score = std of derivatives / mean of absolute values
    # Higher score = more oscillation
    try:
        mean_abs = sum(abs(v) for v in raw_values) / len(raw_values)
        if mean_abs == 0:
            mean_abs = 1e-10

        std_deriv = statistics.stdev(derivatives) if len(derivatives) > 1 else 0
        oscillation_score = std_deriv / mean_abs

        # Determine severity
        if oscillation_score > 0.5:
            severity = "Very High"
        elif oscillation_score > 0.2:
            severity = "High"
        elif oscillation_score > 0.1:
            severity = "Medium"
        else:
            severity = "Low"

        # Determine trend
        if len(raw_values) >= 2:
            first_half = sum(raw_values[:len(raw_values)//2]) / (len(raw_values)//2)
            second_half = sum(raw_values[len(raw_values)//2:]) / (len(raw_values) - len(raw_values)//2)

            if second_half < first_half * 0.9:
                trend = "decreasing"
            elif second_half > first_half * 1.1:
                trend = "increasing"
            else:
                trend = "stable"
        else:
            trend = "unknown"

        return {
            "score": round(oscillation_score, 4),
            "severity": severity,
            "trend": trend,
            "std_derivative": round(std_deriv, 6)
        }

    except Exception as e:
        return {
            "score": 0,
            "severity": "Error",
            "error": str(e)
        }


def calculate_convergence(values: List[Dict]) -> Dict[str, Any]:
    """Analyze convergence characteristics."""

    if len(values) < 5:
        return {
            "converged": "unknown",
            "speed": "unknown",
            "final_value": None
        }

    raw_values = [v["value"] for v in values]

    # Check if converged (last 10% of values have low variance)
    tail_size = max(len(raw_values) // 10, 3)
    tail = raw_values[-tail_size:]

    try:
        tail_std = statistics.stdev(tail) if len(tail) > 1 else 0
        tail_mean = sum(tail) / len(tail)

        # Coefficient of variation
        if tail_mean != 0:
            cv = abs(tail_std / tail_mean)
        else:
            cv = 0

        # Converged if CV < 5%
        converged = cv < 0.05

        # Convergence speed (epochs to reach 90% of improvement)
        if len(raw_values) >= 2:
            initial = raw_values[0]
            final = raw_values[-1]
            improvement = initial - final  # For loss, lower is better

            target_90 = initial - (0.9 * improvement)

            speed_epoch = None
            for i, v in enumerate(raw_values):
                if v <= target_90:
                    speed_epoch = i
                    break

            if speed_epoch is not None:
                speed = "fast" if speed_epoch < len(raw_values) * 0.3 else "slow"
            else:
                speed = "did not reach 90%"
        else:
            speed = "unknown"

        return {
            "converged": converged,
            "speed": speed,
            "final_value": round(raw_values[-1], 6),
            "initial_value": round(raw_values[0], 6),
            "improvement_pct": round(
                100 * (raw_values[0] - raw_values[-1]) / max(abs(raw_values[0]), 1e-10), 2
            ),
            "tail_cv": round(cv, 4)
        }

    except Exception as e:
        return {
            "converged": "error",
            "error": str(e)
        }


def identify_struggle_points(data: Dict) -> List[Dict]:
    """Identify significant struggle points in training."""

    struggles = []

    # Check for gradient issues
    for norm in data["gradient_norms"]:
        if norm["value"] > 1e5:
            struggles.append({
                "type": "gradient_explosion",
                "epoch": norm["epoch"],
                "line": norm["line"],
                "value": norm["value"],
                "severity": "critical",
                "physical_meaning": "Scale mismatch or wrong functional form (additive vs multiplicative)"
            })
        elif norm["value"] < 1e-7:
            struggles.append({
                "type": "gradient_vanishing",
                "epoch": norm["epoch"],
                "line": norm["line"],
                "value": norm["value"],
                "severity": "critical",
                "physical_meaning": "Deep network saturation or dying neurons"
            })

    # Check for R-hat divergence
    for rhat in data["rhat_values"]:
        if rhat["value"] > 1.1:
            struggles.append({
                "type": "rhat_divergence",
                "epoch": rhat["epoch"],
                "line": rhat["line"],
                "value": rhat["value"],
                "severity": "critical" if rhat["value"] > 1.3 else "warning",
                "physical_meaning": "Hidden subgroups or violated pooling assumption"
            })

    # Check loss oscillation
    if data["loss_values"]:
        osc = calculate_oscillation(data["loss_values"])
        if osc["severity"] in ["High", "Very High"]:
            struggles.append({
                "type": "loss_oscillation",
                "score": osc["score"],
                "severity": "warning" if osc["severity"] == "High" else "critical",
                "physical_meaning": "Data non-stationarity, regime shift, or learning rate issues"
            })

    # Add critical events
    for event_type, events in data["critical_events"].items():
        if events:
            struggles.append({
                "type": event_type,
                "count": len(events),
                "first_occurrence": events[0],
                "severity": "critical"
            })

    return struggles


def generate_summary(data: Dict, log_path: str) -> Dict[str, Any]:
    """Generate the final summary JSON for @metacognition_agent."""

    # Basic info
    summary = {
        "meta": {
            "source_file": os.path.basename(log_path),
            "generated": datetime.now().isoformat(),
            "raw_lines": data["raw_lines"],
            "version": "1.0"
        },
        "training": {
            "total_epochs": len(data["epochs"]),
            "epochs_range": [min(data["epochs"]), max(data["epochs"])] if data["epochs"] else [0, 0]
        },
        "loss": {},
        "validation": {},
        "convergence": {},
        "oscillation": {},
        "gradients": {},
        "mcmc": {},
        "events": {},
        "struggles": [],
        "recommendations": []
    }

    # Loss analysis
    if data["loss_values"]:
        values = [v["value"] for v in data["loss_values"]]
        summary["loss"] = {
            "initial": round(values[0], 6),
            "final": round(values[-1], 6),
            "min": round(min(values), 6),
            "max": round(max(values), 6),
            "improvement_pct": round(100 * (values[0] - values[-1]) / max(abs(values[0]), 1e-10), 2)
        }
        summary["oscillation"]["loss"] = calculate_oscillation(data["loss_values"])
        summary["convergence"]["loss"] = calculate_convergence(data["loss_values"])

    # Validation loss
    if data["val_loss_values"]:
        values = [v["value"] for v in data["val_loss_values"]]
        summary["validation"] = {
            "final_val_loss": round(values[-1], 6),
            "best_val_loss": round(min(values), 6),
            "best_epoch": data["val_loss_values"][values.index(min(values))]["epoch"]
        }

        # Check for overfitting
        if data["loss_values"]:
            train_final = data["loss_values"][-1]["value"]
            val_final = values[-1]
            if val_final > train_final * 1.5:
                summary["events"]["overfitting_suspected"] = True

    # Gradient analysis
    if data["gradient_norms"]:
        norms = [v["value"] for v in data["gradient_norms"]]
        summary["gradients"] = {
            "max_norm": max(norms),
            "mean_norm": round(sum(norms) / len(norms), 6),
            "explosion_detected": any(n > 1e5 for n in norms),
            "vanishing_detected": any(n < 1e-7 for n in norms)
        }

    # MCMC analysis
    if data["rhat_values"]:
        rhats = [v["value"] for v in data["rhat_values"]]
        summary["mcmc"] = {
            "max_rhat": round(max(rhats), 4),
            "mean_rhat": round(sum(rhats) / len(rhats), 4),
            "converged": all(r < 1.05 for r in rhats[-5:]) if len(rhats) >= 5 else "unknown"
        }

    # Event counts
    summary["events"]["warning_count"] = len(data["warnings"])
    summary["events"]["error_count"] = len(data["errors"])
    summary["events"]["top_warnings"] = [
        w["message"][:100] for w in data["warnings"][:5]
    ]
    summary["events"]["top_errors"] = [
        e["message"][:100] for e in data["errors"][:5]
    ]

    # Critical events
    for event_type, events in data["critical_events"].items():
        if events:
            summary["events"][event_type] = {
                "count": len(events),
                "first_epoch": events[0]["epoch"],
                "first_line": events[0]["line"]
            }

    # Struggles
    summary["struggles"] = identify_struggle_points(data)

    # Generate recommendations
    recommendations = []

    if summary.get("gradients", {}).get("explosion_detected"):
        recommendations.append({
            "issue": "Gradient explosion detected",
            "action": "Apply gradient clipping or reduce learning rate",
            "physical_insight": "Data scale mismatch - consider log-transform for multiplicative variables"
        })

    if summary.get("mcmc", {}).get("max_rhat", 0) > 1.1:
        recommendations.append({
            "issue": "R-hat divergence detected",
            "action": "Use non-centered parameterization or stronger priors",
            "physical_insight": "Hidden subgroups in data - consider hierarchical structure"
        })

    osc = summary.get("oscillation", {}).get("loss", {})
    if osc.get("severity") in ["High", "Very High"]:
        recommendations.append({
            "issue": "High loss oscillation",
            "action": "Reduce learning rate or use learning rate scheduler",
            "physical_insight": "Possible regime shift or non-stationarity in data"
        })

    if summary.get("events", {}).get("overfitting_suspected"):
        recommendations.append({
            "issue": "Overfitting suspected",
            "action": "Add regularization (L1/L2), dropout, or early stopping",
            "physical_insight": "Model complexity exceeds data information content"
        })

    summary["recommendations"] = recommendations

    return summary


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main(log_path: str, output_path: str) -> None:
    """Main analysis pipeline."""

    print(f"\nLog Analyzer for Phase 5.8")
    print(f"=" * 40)
    print(f"Source: {log_path}")
    print(f"Output: {output_path}\n")

    # Check file exists
    if not os.path.exists(log_path):
        print(f"  Error: Log file not found: {log_path}")
        sys.exit(1)

    # Parse log
    print("Parsing log file...")
    data = parse_log_file(log_path)

    print(f"  Lines parsed: {data['raw_lines']:,}")
    print(f"  Epochs found: {len(data['epochs'])}")
    print(f"  Loss values: {len(data['loss_values'])}")
    print(f"  Warnings: {len(data['warnings'])}")
    print(f"  Errors: {len(data['errors'])}")

    # Generate summary
    print("\nGenerating summary...")
    summary = generate_summary(data, log_path)

    # Write output
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    output_size = os.path.getsize(output_path)
    print(f"\n  Summary created: {output_path}")
    print(f"  Size: {output_size:,} bytes")

    # Print key findings
    print("\n  Key Findings:")
    print(f"    Struggles identified: {len(summary['struggles'])}")
    print(f"    Recommendations: {len(summary['recommendations'])}")

    if summary.get("oscillation", {}).get("loss", {}).get("severity"):
        print(f"    Loss oscillation: {summary['oscillation']['loss']['severity']}")

    if summary.get("convergence", {}).get("loss", {}).get("converged") is not None:
        converged = summary['convergence']['loss']['converged']
        print(f"    Converged: {converged}")

    print(f"\n  Done!")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python log_analyzer.py <training_log> <output_json>")
        print("")
        print("Example:")
        print("  python log_analyzer.py output/implementation/logs/training_full.log logs/summary.json")
        print("")
        print("Output JSON structure:")
        print("  - meta: Source file info")
        print("  - training: Epoch counts")
        print("  - loss: Initial/final/min/max loss")
        print("  - oscillation: Oscillation score and severity")
        print("  - convergence: Convergence analysis")
        print("  - struggles: Identified struggle points with physical meaning")
        print("  - recommendations: Suggested actions")
        sys.exit(1)
