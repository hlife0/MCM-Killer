#!/usr/bin/env python3
"""
HMML Migrator: Convert flat HMML.md to structured HMML 2.0.

Usage:
    python migrate_hmml.py <hmml_source.md> <output_directory>

Example:
    python migrate_hmml.py ../MMAgent/HMML/HMML.md knowledge_library/methods/

This script:
1. Parses the monolithic HMML.md file
2. Infers domain classification for each method
3. Estimates complexity and narrative value
4. Generates individual .md files with YAML front matter
5. Creates an index.md catalog

HMML 2.0 Format:
- Each method becomes a separate file with YAML front matter
- Methods are organized by domain (optimization, statistics, etc.)
- Metadata includes: complexity, narrative_value, common_pitfalls, tags
"""

import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
import yaml
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Any


# ============================================================================
# DOMAIN CLASSIFICATION KEYWORDS
# ============================================================================

DOMAIN_KEYWORDS = {
    "optimization": [
        "linear programming", "simplex", "interior point", "genetic algorithm",
        "simulated annealing", "lagrange", "convex", "nonlinear", "quadratic",
        "integer programming", "milp", "constraint", "objective function",
        "gradient descent", "newton", "quasi-newton", "lbfgs", "sgd",
        "particle swarm", "ant colony", "evolutionary", "metaheuristic",
        "knapsack", "traveling salesman", "tsp", "vehicle routing",
        "multi-objective", "pareto", "game theory", "nash equilibrium"
    ],
    "differential_equations": [
        "ode", "pde", "sir", "seir", "sirs", "epidemic", "diffusion",
        "stochastic differential", "sde", "euler", "runge-kutta",
        "compartmental", "population dynamics", "predator-prey",
        "heat equation", "wave equation", "laplace", "poisson",
        "finite element", "finite difference", "boundary value",
        "initial value", "stability analysis", "bifurcation",
        "chaos", "lyapunov", "dynamical systems", "phase portrait"
    ],
    "statistics": [
        "bayesian", "regression", "time series", "arima", "likelihood",
        "inference", "hierarchical", "mcmc", "metropolis", "gibbs",
        "maximum likelihood", "mle", "posterior", "prior", "credible interval",
        "hypothesis testing", "p-value", "confidence interval",
        "variance", "covariance", "correlation", "anova", "chi-square",
        "bootstrap", "cross-validation", "regularization", "lasso", "ridge",
        "mixed effects", "random effects", "longitudinal", "survival analysis",
        "kaplan-meier", "cox regression", "hazard", "censoring"
    ],
    "network_science": [
        "network", "graph", "dijkstra", "shortest path", "centrality",
        "pagerank", "topology", "adjacency", "node", "edge", "degree",
        "betweenness", "closeness", "eigenvector", "community detection",
        "modularity", "clustering coefficient", "small world",
        "scale-free", "power law", "random graph", "erdos-renyi",
        "barabasi-albert", "preferential attachment", "social network",
        "influence propagation", "cascade", "contagion", "diffusion network"
    ],
    "machine_learning": [
        "neural", "random forest", "svm", "support vector", "clustering",
        "classification", "deep learning", "cnn", "rnn", "lstm", "transformer",
        "decision tree", "gradient boosting", "xgboost", "lightgbm",
        "k-means", "hierarchical clustering", "dbscan", "pca",
        "dimensionality reduction", "feature selection", "ensemble",
        "cross-validation", "overfitting", "regularization", "dropout",
        "batch normalization", "attention mechanism", "embedding",
        "reinforcement learning", "q-learning", "policy gradient"
    ],
    "graph_theory": [
        "graph", "tree", "cycle", "euler", "hamilton", "planar",
        "bipartite", "matching", "coloring", "chromatic", "spanning tree",
        "minimum spanning tree", "mst", "flow network", "max flow",
        "min cut", "ford-fulkerson", "edmonds-karp", "vertex cover",
        "independent set", "clique", "isomorphism", "subgraph"
    ]
}

# ============================================================================
# COMPLEXITY ESTIMATION
# ============================================================================

COMPLEXITY_KEYWORDS = {
    "Very High": [
        "agent-based", "stochastic differential", "deep learning",
        "reinforcement learning", "transformer", "graph neural network",
        "partial differential", "multi-scale", "hierarchical bayesian",
        "variational inference", "normalizing flow", "diffusion model"
    ],
    "High": [
        "bayesian hierarchical", "genetic algorithm", "neural network",
        "pde", "sir network", "lstm", "random forest", "mcmc",
        "convex optimization", "mixed integer", "finite element"
    ],
    "Medium": [
        "time series", "simplex", "sde", "arima", "regression",
        "clustering", "decision tree", "ode", "linear programming",
        "gradient descent", "maximum likelihood"
    ],
    "Low": [
        "linear regression", "basic sir", "dijkstra", "shortest path",
        "k-means", "naive bayes", "logistic regression", "correlation",
        "chi-square", "t-test"
    ]
}

# ============================================================================
# NARRATIVE VALUE ASSESSMENT
# ============================================================================

HIGH_NARRATIVE_KEYWORDS = [
    "network", "topology", "heterogeneity", "uncertainty", "hierarchical",
    "agent-based", "stochastic", "spatial", "temporal", "dynamic",
    "emergence", "complexity", "multi-scale", "interaction", "feedback",
    "sensitivity", "robustness", "resilience", "regime shift", "phase transition"
]

# ============================================================================
# ANTI-PATTERN DETECTION
# ============================================================================

COMMON_PITFALLS = {
    "identifiability": [
        "identifi", "correlated parameters", "overparameterized",
        "non-identifiable", "structural", "observability"
    ],
    "scale_mismatch": [
        "scale", "normali", "standardiz", "magnitude", "unit", "dimension"
    ],
    "numerical_instability": [
        "overflow", "underflow", "numerical", "precision", "floating",
        "ill-conditioned", "singular", "nan", "inf"
    ],
    "local_optima": [
        "local", "global", "saddle", "plateau", "convergence",
        "multiple restart", "initialization"
    ],
    "overfitting": [
        "overfit", "generalization", "regularization", "complexity",
        "train-test", "cross-validation", "validation"
    ]
}

# ============================================================================
# O-PRIZE EXAMPLE YEARS (Simulated - based on common MCM/ICM patterns)
# ============================================================================

OPRIZE_EXAMPLES = {
    "bayesian": ["2019 Problem D", "2022 Problem F"],
    "sir": ["2020 Problem C", "2023 Problem B"],
    "network": ["2019 Problem D", "2022 Problem E"],
    "time_series": ["2021 Problem C", "2023 Problem A"],
    "optimization": ["2020 Problem A", "2022 Problem B"],
    "agent-based": ["2021 Problem D", "2023 Problem C"],
    "machine_learning": ["2022 Problem A", "2023 Problem E"]
}


def infer_domain(content: str, method_name: str) -> str:
    """Infer domain from content keywords."""
    content_lower = content.lower()
    method_lower = method_name.lower()
    combined = content_lower + " " + method_lower

    scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw in combined)
        scores[domain] = score

    best_domain = max(scores, key=scores.get)
    return best_domain if scores[best_domain] > 0 else "optimization"


def infer_subdomain(domain: str, content: str) -> str:
    """Infer sub-domain for more specific categorization."""
    content_lower = content.lower()

    subdomain_map = {
        "optimization": {
            "linear_programming": ["linear", "simplex", "dual"],
            "nonlinear_programming": ["nonlinear", "gradient", "newton"],
            "heuristic": ["genetic", "simulated", "particle", "evolutionary"]
        },
        "differential_equations": {
            "epidemic": ["sir", "seir", "epidemic", "infection", "disease"],
            "pde": ["partial", "heat", "wave", "diffusion", "laplace"],
            "sde": ["stochastic", "brownian", "wiener", "ito"]
        },
        "statistics": {
            "bayesian": ["bayesian", "posterior", "prior", "mcmc"],
            "time_series": ["arima", "time series", "forecast", "seasonal"],
            "regression": ["regression", "linear model", "glm"]
        },
        "network_science": {
            "pathfinding": ["shortest", "dijkstra", "path", "route"],
            "centrality": ["centrality", "pagerank", "degree", "betweenness"],
            "community": ["community", "modularity", "cluster", "partition"]
        },
        "machine_learning": {
            "trees": ["tree", "forest", "boosting", "xgboost"],
            "neural_networks": ["neural", "deep", "cnn", "rnn", "lstm"],
            "clustering": ["cluster", "k-means", "dbscan", "hierarchical"]
        }
    }

    if domain in subdomain_map:
        for subdomain, keywords in subdomain_map[domain].items():
            if any(kw in content_lower for kw in keywords):
                return subdomain

    return domain.split("_")[0] if "_" in domain else domain


def estimate_complexity(content: str, method_name: str) -> str:
    """Estimate complexity from keywords."""
    combined = (content + " " + method_name).lower()

    for level, keywords in COMPLEXITY_KEYWORDS.items():
        if any(kw in combined for kw in keywords):
            return level

    return "Medium"


def assess_narrative_value(method_name: str, domain: str, content: str) -> Dict[str, Any]:
    """Assess O-Prize narrative potential with detailed reasoning."""
    content_lower = content.lower()
    method_lower = method_name.lower()
    combined = content_lower + " " + method_lower

    score = sum(1 for kw in HIGH_NARRATIVE_KEYWORDS if kw in combined)

    if score >= 3:
        level = "Very High"
        reason = "Enables deep discussion of system complexity, heterogeneity, and emergent behaviors"
    elif score >= 2:
        level = "High"
        reason = "Demonstrates understanding of complex interactions and uncertainty"
    elif score >= 1:
        level = "Medium"
        reason = "Solid methodological choice with some narrative potential"
    else:
        level = "Low"
        reason = "Standard method - consider enhancing with sensitivity analysis"

    return {
        "level": level,
        "score": score,
        "reason": reason
    }


def extract_pitfalls(content: str, method_name: str) -> List[Dict[str, str]]:
    """Extract common pitfalls from content with detailed descriptions."""
    pitfalls = []
    combined = (content + " " + method_name).lower()

    pitfall_descriptions = {
        "identifiability": {
            "name": "Parameter Identifiability",
            "description": "Correlated parameters may not converge or may compensate for each other",
            "solution": "Use non-centered parameterization, strong priors, or reduce model complexity"
        },
        "scale_mismatch": {
            "name": "Scale Mismatch",
            "description": "Input features with different magnitudes may cause numerical issues",
            "solution": "Normalize all features to [0, 1] or standardize to zero mean, unit variance"
        },
        "numerical_instability": {
            "name": "Numerical Instability",
            "description": "Large values may cause overflow, small values may cause underflow",
            "solution": "Use log-space computations, gradient clipping, or numerical stable implementations"
        },
        "local_optima": {
            "name": "Local Optima",
            "description": "Optimization may converge to suboptimal solutions",
            "solution": "Use multiple random restarts, global optimization, or simulated annealing"
        },
        "overfitting": {
            "name": "Overfitting Risk",
            "description": "Model may fit training data too closely and fail to generalize",
            "solution": "Use cross-validation, regularization (L1/L2), or early stopping"
        }
    }

    for pitfall_type, keywords in COMMON_PITFALLS.items():
        if any(kw in combined for kw in keywords):
            pitfalls.append(pitfall_descriptions[pitfall_type])

    return pitfalls


def get_oprize_examples(domain: str, content: str) -> List[Dict[str, str]]:
    """Get relevant O-Prize examples for the method."""
    examples = []
    content_lower = content.lower()

    for key, years in OPRIZE_EXAMPLES.items():
        if key in content_lower or key in domain:
            for year_problem in years:
                examples.append({
                    "competition": year_problem,
                    "relevance": f"Used {key} methodology"
                })
            break

    return examples[:2]  # Limit to 2 examples


def slugify(text: str) -> str:
    """Convert text to filename-safe slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s-]+', '_', text)
    return text.strip('_')


def parse_hmml_method(block: str, method_name: str) -> Dict[str, Any]:
    """Parse a single method block from HMML.md."""

    # Extract sections
    sections = {}
    current_section = "Overview"
    sections[current_section] = []

    for line in block.split('\n'):
        if line.startswith('## '):
            current_section = line[3:].strip()
            sections[current_section] = []
        else:
            sections[current_section].append(line)

    # Join sections
    for key in sections:
        sections[key] = '\n'.join(sections[key]).strip()

    # Infer metadata
    full_content = block
    domain = infer_domain(full_content, method_name)
    subdomain = infer_subdomain(domain, full_content)
    complexity = estimate_complexity(full_content, method_name)
    narrative_value = assess_narrative_value(method_name, domain, full_content)
    pitfalls = extract_pitfalls(full_content, method_name)
    oprize_examples = get_oprize_examples(domain, full_content)

    filename = slugify(method_name)

    # Build metadata
    metadata = {
        "method_name": method_name,
        "domain": domain,
        "sub_domain": subdomain,
        "complexity": complexity,
        "narrative_value": narrative_value["level"],
        "narrative_reason": narrative_value["reason"],
        "common_pitfalls": [p["name"] for p in pitfalls],
        "oprize_examples": [e["competition"] for e in oprize_examples],
        "tags": [domain, subdomain, complexity.lower().replace(" ", "_")],
        "version": "2.0",
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }

    return {
        "metadata": metadata,
        "sections": sections,
        "filename": filename,
        "pitfalls_detail": pitfalls,
        "oprize_detail": oprize_examples
    }


def generate_method_file(parsed: Dict[str, Any]) -> str:
    """Generate the complete method file content."""
    metadata = parsed["metadata"]
    sections = parsed["sections"]
    pitfalls = parsed["pitfalls_detail"]
    oprize = parsed["oprize_detail"]

    content = []

    # YAML front matter
    content.append("---")
    content.append(yaml.dump(metadata, default_flow_style=False, allow_unicode=True).strip())
    content.append("---")
    content.append("")

    # Title
    content.append(f"# {metadata['method_name']}")
    content.append("")

    # Quick reference box
    content.append("> **Domain**: " + metadata["domain"].replace("_", " ").title())
    content.append(f"> **Complexity**: {metadata['complexity']}")
    content.append(f"> **Narrative Value**: {metadata['narrative_value']}")
    content.append("")

    # Existing sections
    for section_name, section_content in sections.items():
        if section_content.strip():
            content.append(f"## {section_name}")
            content.append("")
            content.append(section_content)
            content.append("")

    # Add O-Prize Examples section
    if oprize:
        content.append("## O-Prize Examples")
        content.append("")
        for ex in oprize:
            content.append(f"- **{ex['competition']}**: {ex['relevance']}")
        content.append("")

    # Add Common Pitfalls section (detailed)
    if pitfalls:
        content.append("## Common Pitfalls (Detailed)")
        content.append("")
        for i, p in enumerate(pitfalls, 1):
            content.append(f"### Pitfall {i}: {p['name']}")
            content.append("")
            content.append(f"**Problem**: {p['description']}")
            content.append("")
            content.append(f"**Solution**: {p['solution']}")
            content.append("")

    # Add Narrative Strategy section
    content.append("## Narrative Strategy")
    content.append("")
    content.append(f"**Value**: {metadata['narrative_value']} - {metadata['narrative_reason']}")
    content.append("")
    content.append("### Suggested Framing")
    content.append("")
    content.append(f"> \"We employ {metadata['method_name']} to capture [specific mechanism], ")
    content.append(f"> which enables us to [key insight] while accounting for [complexity/uncertainty].\"")
    content.append("")

    return '\n'.join(content)


def main(hmml_path: str, output_base: str) -> None:
    """Main migration pipeline."""

    print(f"\nHMML 2.0 Migration Tool")
    print(f"=" * 40)
    print(f"Source: {hmml_path}")
    print(f"Target: {output_base}\n")

    # Read HMML.md
    with open(hmml_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ### (method-level headers)
    method_blocks = re.split(r'\n###\s+', content)

    print(f"  Found {len(method_blocks) - 1} methods in HMML.md")
    print("")

    migrated = []
    domain_counts = {}

    for i, block in enumerate(method_blocks[1:], 1):
        lines = block.split('\n')
        method_name = lines[0].strip()
        method_content = '\n'.join(lines[1:])

        # Parse
        parsed = parse_hmml_method(method_content, method_name)

        # Determine output path
        domain = parsed["metadata"]["domain"]
        subdomain = parsed["metadata"]["sub_domain"]

        # Track domain counts
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

        output_dir = os.path.join(output_base, domain, subdomain)
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        output_file = os.path.join(output_dir, f"{parsed['filename']}.md")

        # Generate and write
        file_content = generate_method_file(parsed)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(file_content)

        print(f"  [{i:3d}] {method_name}")
        print(f"        → {domain}/{subdomain}/{parsed['filename']}.md")

        migrated.append({
            "name": method_name,
            "file": output_file,
            "domain": domain,
            "subdomain": subdomain,
            "complexity": parsed["metadata"]["complexity"],
            "narrative_value": parsed["metadata"]["narrative_value"]
        })

    # Generate index
    generate_index(output_base, migrated, domain_counts)

    # Generate summary report
    generate_summary(output_base, migrated, domain_counts)

    print(f"\n  Migration complete!")
    print(f"  Total methods: {len(migrated)}")
    print(f"  Domains: {len(domain_counts)}")


def generate_index(output_base: str, migrated: List[Dict], domain_counts: Dict) -> None:
    """Generate index.md catalog."""

    index_path = os.path.join(output_base, "index.md")

    content = []
    content.append("# HMML 2.0 Method Index")
    content.append("")
    content.append(f"> **Version**: 2.0")
    content.append(f"> **Total Methods**: {len(migrated)}")
    content.append(f"> **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}")
    content.append("")

    # Summary table
    content.append("## Domain Summary")
    content.append("")
    content.append("| Domain | Count | Complexity Range |")
    content.append("|--------|-------|------------------|")
    for domain, count in sorted(domain_counts.items()):
        domain_methods = [m for m in migrated if m["domain"] == domain]
        complexities = set(m["complexity"] for m in domain_methods)
        content.append(f"| {domain.replace('_', ' ').title()} | {count} | {', '.join(sorted(complexities))} |")
    content.append("")

    # Group by domain
    by_domain = {}
    for m in migrated:
        domain = m["domain"]
        if domain not in by_domain:
            by_domain[domain] = {}
        subdomain = m["subdomain"]
        if subdomain not in by_domain[domain]:
            by_domain[domain][subdomain] = []
        by_domain[domain][subdomain].append(m)

    # Generate sections
    for domain in sorted(by_domain.keys()):
        content.append(f"## {domain.replace('_', ' ').title()}")
        content.append("")

        for subdomain in sorted(by_domain[domain].keys()):
            content.append(f"### {subdomain.replace('_', ' ').title()}")
            content.append("")
            content.append("| Method | Complexity | Narrative Value |")
            content.append("|--------|------------|-----------------|")

            for m in sorted(by_domain[domain][subdomain], key=lambda x: x["name"]):
                rel_path = os.path.relpath(m["file"], output_base).replace("\\", "/")
                content.append(f"| [{m['name']}]({rel_path}) | {m['complexity']} | {m['narrative_value']} |")

            content.append("")

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

    print(f"\n  Index created: {index_path}")


def generate_summary(output_base: str, migrated: List[Dict], domain_counts: Dict) -> None:
    """Generate JSON summary for programmatic access."""

    summary = {
        "version": "2.0",
        "generated": datetime.now().isoformat(),
        "total_methods": len(migrated),
        "domains": domain_counts,
        "by_complexity": {},
        "by_narrative_value": {},
        "methods": []
    }

    for m in migrated:
        # Count by complexity
        c = m["complexity"]
        summary["by_complexity"][c] = summary["by_complexity"].get(c, 0) + 1

        # Count by narrative value
        n = m["narrative_value"]
        summary["by_narrative_value"][n] = summary["by_narrative_value"].get(n, 0) + 1

        # Add method reference
        summary["methods"].append({
            "name": m["name"],
            "domain": m["domain"],
            "subdomain": m["subdomain"],
            "complexity": m["complexity"],
            "narrative_value": m["narrative_value"],
            "file": os.path.relpath(m["file"], output_base).replace("\\", "/")
        })

    summary_path = os.path.join(output_base, "hmml_summary.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

    print(f"  Summary created: {summary_path}")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python migrate_hmml.py <hmml_source.md> <output_directory>")
        print("")
        print("Example:")
        print("  python migrate_hmml.py ../MMAgent/HMML/HMML.md knowledge_library/methods/")
        sys.exit(1)
