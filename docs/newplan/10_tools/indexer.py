#!/usr/bin/env python3
"""
External Resource Indexer
Maintains the master index of external resources with SHA-256 hash verification.

Usage:
    python indexer.py add <resource_id> <metadata_path> <quality_score>
    python indexer.py remove <resource_id>
    python indexer.py search <query>
    python indexer.py list [domain|type|consumer]
    python indexer.py stats
    python indexer.py verify              # Protocol 21: Verify all hashes
    python indexer.py verify-one <id>     # Verify single resource hash
    python indexer.py log <id> <agent> <phase> [action]

Example:
    python indexer.py add WEB_20260131_abc123 active/WEB_20260131_abc123/metadata.json 8.5
    python indexer.py search "epidemic network"
    python indexer.py list domain
    python indexer.py verify              # Check all resource integrity
"""

import json
import os
import sys
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# Configuration
BASE_DIR = "output/external_resources"
INDEX_PATH = f"{BASE_DIR}/index.json"
STATS_PATH = f"{BASE_DIR}/statistics.json"


def generate_file_hash(filepath: str) -> str:
    """Generate SHA-256 hash of file content for data integrity."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return ""


def verify_file_hash(filepath: str, expected_hash: str) -> Tuple[bool, str]:
    """
    Verify file integrity by comparing current hash with stored hash.
    Returns (is_valid, message).

    Used by Protocol 21 for data consistency validation.
    """
    if not expected_hash:
        return True, "No hash stored, skipping verification"

    current_hash = generate_file_hash(filepath)
    if not current_hash:
        return False, f"File not found: {filepath}"

    if current_hash == expected_hash:
        return True, "Hash verified OK"
    else:
        return False, f"Hash mismatch! Expected: {expected_hash[:16]}..., Got: {current_hash[:16]}..."


def load_index() -> Dict:
    """Load the master index."""
    if os.path.exists(INDEX_PATH):
        with open(INDEX_PATH) as f:
            return json.load(f)
    return {
        "version": "3.2.0",
        "last_updated": "",
        "total_resources": 0,
        "by_domain": {},
        "by_type": {},
        "by_consumer": {},
        "by_phase": {},
        "resources": {}
    }


def save_index(index: Dict):
    """Save the master index."""
    index["last_updated"] = datetime.now().isoformat()
    index["total_resources"] = len(index.get("resources", {}))

    with open(INDEX_PATH, "w") as f:
        json.dump(index, f, indent=2)

    print(f"Index saved: {index['total_resources']} resources")


def add_resource(resource_id: str, metadata_path: str, quality_score: float) -> Dict:
    """Add a resource to the index with SHA-256 hash for integrity verification."""
    # Load metadata
    with open(metadata_path) as f:
        metadata = json.load(f)

    index = load_index()

    # Determine resource path
    resource_path = os.path.dirname(metadata_path)

    # Find content file and generate hash
    content_file = None
    content_hash = ""
    for ext in [".py", ".m", ".cpp", ".c", ".java", ".r", ".jl", ".md", ".txt", ".csv"]:
        potential_file = os.path.join(resource_path, f"content{ext}")
        if os.path.exists(potential_file):
            content_file = potential_file
            content_hash = generate_file_hash(potential_file)
            break

    # Add to main resources
    index["resources"][resource_id] = {
        "title": metadata.get("title", "Unknown"),
        "path": resource_path,
        "summary_path": os.path.join(resource_path, "summary.md"),
        "quality_score": quality_score,
        "quality_status": "APPROVED" if quality_score >= 7.0 else "CONDITIONAL",
        "domain": metadata.get("domain", "unknown"),
        "type": metadata.get("content_type", "unknown"),
        "tags": metadata.get("keywords", []),
        "keywords": metadata.get("keywords", []),
        "suggested_consumers": metadata.get("suggested_consumers", []),
        "source_url": metadata.get("source_url", ""),
        "added_date": datetime.now().strftime("%Y-%m-%d"),
        "access_count": 0,
        "content_file": content_file,
        "content_hash_sha256": content_hash,  # For Protocol 21 verification
        "hash_verified_at": datetime.now().isoformat()
    }

    # Update by_domain
    domain = metadata.get("domain", "unknown")
    if domain not in index["by_domain"]:
        index["by_domain"][domain] = []
    if resource_id not in index["by_domain"][domain]:
        index["by_domain"][domain].append(resource_id)

    # Update by_type
    content_type = metadata.get("content_type", "unknown")
    if content_type not in index["by_type"]:
        index["by_type"][content_type] = []
    if resource_id not in index["by_type"][content_type]:
        index["by_type"][content_type].append(resource_id)

    # Update by_consumer
    for consumer in metadata.get("suggested_consumers", []):
        if consumer not in index["by_consumer"]:
            index["by_consumer"][consumer] = []
        if resource_id not in index["by_consumer"][consumer]:
            index["by_consumer"][consumer].append(resource_id)

    # Update by_phase (infer from consumers)
    phase_map = {
        "@reader": ["0"],
        "@researcher": ["0", "0.5"],
        "@modeler": ["1"],
        "@data_engineer": ["3"],
        "@code_translator": ["4"],
        "@model_trainer": ["5"],
        "@writer": ["7"],
        "@validator": ["5.5", "9"]
    }

    for consumer in metadata.get("suggested_consumers", []):
        for phase in phase_map.get(consumer, []):
            phase_key = f"phase_{phase}"
            if phase_key not in index["by_phase"]:
                index["by_phase"][phase_key] = []
            if resource_id not in index["by_phase"][phase_key]:
                index["by_phase"][phase_key].append(resource_id)

    save_index(index)
    return index


def remove_resource(resource_id: str):
    """Remove a resource from the index."""
    index = load_index()

    if resource_id not in index.get("resources", {}):
        print(f"Resource not found: {resource_id}")
        return

    # Remove from main resources
    del index["resources"][resource_id]

    # Remove from all category indexes
    for category in ["by_domain", "by_type", "by_consumer", "by_phase"]:
        for key in list(index.get(category, {}).keys()):
            if resource_id in index[category][key]:
                index[category][key].remove(resource_id)
            # Clean up empty lists
            if not index[category][key]:
                del index[category][key]

    save_index(index)
    print(f"Removed: {resource_id}")


def search(query: str) -> List[Dict]:
    """Search for resources by keyword."""
    index = load_index()
    results = []

    query_terms = query.lower().split()

    for resource_id, info in index.get("resources", {}).items():
        score = 0

        # Check title
        title_lower = info.get("title", "").lower()
        for term in query_terms:
            if term in title_lower:
                score += 3

        # Check tags/keywords
        tags = [t.lower() for t in info.get("tags", [])]
        for term in query_terms:
            if any(term in tag for tag in tags):
                score += 2

        # Check domain
        if any(term in info.get("domain", "").lower() for term in query_terms):
            score += 1

        if score > 0:
            results.append({
                "id": resource_id,
                "title": info.get("title"),
                "domain": info.get("domain"),
                "quality_score": info.get("quality_score"),
                "path": info.get("path"),
                "match_score": score
            })

    # Sort by match score, then quality score
    results.sort(key=lambda x: (x["match_score"], x["quality_score"]), reverse=True)
    return results


def list_resources(category: Optional[str] = None):
    """List resources, optionally by category."""
    index = load_index()

    if category is None:
        # List all resources
        print(f"\nTotal Resources: {index['total_resources']}")
        print("-" * 60)
        for resource_id, info in index.get("resources", {}).items():
            print(f"{resource_id}: {info.get('title', 'Unknown')[:40]} ({info.get('quality_score', 0)})")
    elif category == "domain":
        print("\nResources by Domain:")
        print("-" * 40)
        for domain, resources in index.get("by_domain", {}).items():
            print(f"{domain}: {len(resources)} resources")
            for rid in resources:
                print(f"  - {rid}")
    elif category == "type":
        print("\nResources by Type:")
        print("-" * 40)
        for rtype, resources in index.get("by_type", {}).items():
            print(f"{rtype}: {len(resources)} resources")
    elif category == "consumer":
        print("\nResources by Consumer:")
        print("-" * 40)
        for consumer, resources in index.get("by_consumer", {}).items():
            print(f"{consumer}: {len(resources)} resources")


def generate_stats():
    """Generate usage statistics."""
    index = load_index()
    active_dir = f"{BASE_DIR}/active"
    rejected_dir = f"{BASE_DIR}/rejected"
    archived_dir = f"{BASE_DIR}/archived"

    stats = {
        "generated_at": datetime.now().isoformat(),
        "totals": {
            "active": len(index.get("resources", {})),
            "rejected": len(os.listdir(rejected_dir)) if os.path.exists(rejected_dir) else 0,
            "archived": len(os.listdir(archived_dir)) if os.path.exists(archived_dir) else 0
        },
        "by_domain": {},
        "by_type": {},
        "quality_distribution": {
            "excellent_8_10": 0,
            "good_7_8": 0,
            "conditional_5_7": 0
        },
        "most_accessed": []
    }

    # Analyze resources
    resources_by_access = []
    for resource_id, info in index.get("resources", {}).items():
        quality = info.get("quality_score", 0)
        domain = info.get("domain", "unknown")
        rtype = info.get("type", "unknown")

        # Quality distribution
        if quality >= 8:
            stats["quality_distribution"]["excellent_8_10"] += 1
        elif quality >= 7:
            stats["quality_distribution"]["good_7_8"] += 1
        else:
            stats["quality_distribution"]["conditional_5_7"] += 1

        # By domain
        if domain not in stats["by_domain"]:
            stats["by_domain"][domain] = {"count": 0, "total_quality": 0}
        stats["by_domain"][domain]["count"] += 1
        stats["by_domain"][domain]["total_quality"] += quality

        # Track access
        resources_by_access.append({
            "id": resource_id,
            "title": info.get("title", ""),
            "access_count": info.get("access_count", 0),
            "quality": quality
        })

    # Calculate averages
    for domain in stats["by_domain"]:
        count = stats["by_domain"][domain]["count"]
        if count > 0:
            avg = stats["by_domain"][domain]["total_quality"] / count
            stats["by_domain"][domain]["avg_quality"] = round(avg, 1)
            del stats["by_domain"][domain]["total_quality"]

    # Top accessed
    resources_by_access.sort(key=lambda x: x["access_count"], reverse=True)
    stats["most_accessed"] = resources_by_access[:5]

    # Save stats
    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Statistics generated: {STATS_PATH}")
    print(f"Active: {stats['totals']['active']}")
    print(f"Rejected: {stats['totals']['rejected']}")
    print(f"Archived: {stats['totals']['archived']}")

    return stats


def log_access(resource_id: str, agent: str, phase: str, action: str = "read"):
    """Log resource access."""
    index = load_index()

    if resource_id not in index.get("resources", {}):
        print(f"Resource not found: {resource_id}")
        return

    # Increment access count
    index["resources"][resource_id]["access_count"] = \
        index["resources"][resource_id].get("access_count", 0) + 1

    save_index(index)

    # Also update usage_log in resource folder
    resource_path = index["resources"][resource_id].get("path", "")
    usage_log_path = os.path.join(resource_path, "usage_log.json")

    if os.path.exists(usage_log_path):
        with open(usage_log_path) as f:
            usage = json.load(f)
    else:
        usage = {"resource_id": resource_id, "access_log": []}

    usage["access_log"].append({
        "agent": agent,
        "phase": phase,
        "action": action,
        "timestamp": datetime.now().isoformat()
    })

    with open(usage_log_path, "w") as f:
        json.dump(usage, f, indent=2)

    print(f"Logged access: {agent} -> {resource_id} ({action})")


def verify_all_hashes() -> Dict:
    """
    Verify SHA-256 hashes for all indexed resources.
    Used by Protocol 21 for data consistency validation.

    Returns summary of verification results.
    """
    index = load_index()
    results = {
        "verified_at": datetime.now().isoformat(),
        "total": 0,
        "passed": 0,
        "failed": 0,
        "skipped": 0,
        "failures": []
    }

    for resource_id, info in index.get("resources", {}).items():
        results["total"] += 1
        content_file = info.get("content_file", "")
        expected_hash = info.get("content_hash_sha256", "")

        if not content_file or not expected_hash:
            results["skipped"] += 1
            continue

        is_valid, message = verify_file_hash(content_file, expected_hash)

        if is_valid:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["failures"].append({
                "resource_id": resource_id,
                "file": content_file,
                "message": message
            })

    # Print summary
    print(f"\n{'='*50}")
    print("PROTOCOL 21: Hash Verification Report")
    print(f"{'='*50}")
    print(f"Total Resources: {results['total']}")
    print(f"Passed: {results['passed']}")
    print(f"Failed: {results['failed']}")
    print(f"Skipped (no hash): {results['skipped']}")

    if results["failures"]:
        print(f"\n{'!'*50}")
        print("FAILURES DETECTED:")
        for failure in results["failures"]:
            print(f"  - {failure['resource_id']}: {failure['message']}")
        print(f"{'!'*50}")

    return results


def print_help():
    """Print usage help."""
    print(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 5:
        resource_id = sys.argv[2]
        metadata_path = sys.argv[3]
        quality_score = float(sys.argv[4])
        add_resource(resource_id, metadata_path, quality_score)

    elif command == "remove" and len(sys.argv) >= 3:
        remove_resource(sys.argv[2])

    elif command == "search" and len(sys.argv) >= 3:
        query = " ".join(sys.argv[2:])
        results = search(query)
        print(f"\nSearch: '{query}'")
        print(f"Found: {len(results)} results")
        print("-" * 60)
        for r in results[:10]:
            print(f"{r['id']}: {r['title'][:40]} (quality: {r['quality_score']}, match: {r['match_score']})")

    elif command == "list":
        category = sys.argv[2] if len(sys.argv) >= 3 else None
        list_resources(category)

    elif command == "stats":
        generate_stats()

    elif command == "log" and len(sys.argv) >= 5:
        resource_id = sys.argv[2]
        agent = sys.argv[3]
        phase = sys.argv[4]
        action = sys.argv[5] if len(sys.argv) >= 6 else "read"
        log_access(resource_id, agent, phase, action)

    elif command == "verify":
        # Protocol 21: Verify all resource hashes
        verify_all_hashes()

    elif command == "verify-one" and len(sys.argv) >= 3:
        # Verify single resource hash
        resource_id = sys.argv[2]
        index = load_index()
        if resource_id in index.get("resources", {}):
            info = index["resources"][resource_id]
            content_file = info.get("content_file", "")
            expected_hash = info.get("content_hash_sha256", "")
            is_valid, message = verify_file_hash(content_file, expected_hash)
            print(f"{resource_id}: {message}")
        else:
            print(f"Resource not found: {resource_id}")

    else:
        print_help()
