#!/usr/bin/env python3
"""
Style Analyzer: Extract academic writing patterns from O-Prize reference papers.

Usage:
    python style_analyzer.py <papers_directory> <output_path>

Example:
    python style_analyzer.py reference_papers/ knowledge_library/academic_writing/style_guide.md

This script analyzes O-Prize winning papers to extract:
1. High-frequency academic verbs and vocabulary
2. Sentence pattern templates (Observation-Implication)
3. Abstract structure rules (quantitative requirements)
4. Figure caption standards
5. Writing constraints and anti-patterns

Requires:
    pip install pdfplumber spacy
    python -m spacy download en_core_web_sm
"""

import os
import re
import sys
import json
from pathlib import Path
from datetime import datetime
from collections import Counter, defaultdict
from typing import Dict, List, Tuple, Optional, Any

# Try to import optional dependencies
try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False
    print("Warning: pdfplumber not installed. PDF parsing will be limited.")

try:
    import spacy
    HAS_SPACY = True
except ImportError:
    HAS_SPACY = False
    print("Warning: spacy not installed. POS tagging will be limited.")


# ============================================================================
# ACADEMIC VOCABULARY LISTS
# ============================================================================

ACADEMIC_VERBS_HIGH = [
    "elucidate", "demonstrate", "quantify", "corroborate", "substantiate",
    "delineate", "postulate", "hypothesize", "validate", "ascertain",
    "underscore", "manifest", "posit", "articulate", "synthesize",
    "interrogate", "illuminate", "exemplify", "characterize", "operationalize",
    "conceptualize", "contextualize", "disambiguate", "extrapolate", "interpolate"
]

ACADEMIC_VERBS_MEDIUM = [
    "investigate", "examine", "analyze", "evaluate", "assess",
    "determine", "establish", "identify", "reveal", "indicate",
    "suggest", "imply", "infer", "conclude", "observe",
    "compare", "contrast", "correlate", "differentiate", "integrate"
]

WEAK_VERBS = [
    "show", "say", "get", "do", "make", "use", "have", "be",
    "go", "see", "look", "find", "give", "take", "come"
]

ACADEMIC_CONNECTORS = [
    "however", "therefore", "furthermore", "moreover", "consequently",
    "nevertheless", "accordingly", "thus", "hence", "thereby",
    "notwithstanding", "conversely", "alternatively", "specifically", "notably"
]

OBSERVATION_MARKERS = [
    "reveals", "shows", "indicates", "demonstrates", "exhibits",
    "displays", "presents", "illustrates", "depicts", "confirms"
]

IMPLICATION_MARKERS = [
    "implying", "suggesting", "indicating", "demonstrating",
    "which implies", "which suggests", "this indicates", "this demonstrates",
    "pointing to", "confirming that", "revealing that"
]


# ============================================================================
# TEXT EXTRACTION
# ============================================================================

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF file."""
    if not HAS_PDFPLUMBER:
        return ""

    text_parts = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
    except Exception as e:
        print(f"  Warning: Could not read {pdf_path}: {e}")
        return ""

    return '\n'.join(text_parts)


def extract_text_from_txt(txt_path: str) -> str:
    """Extract text from a TXT file."""
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"  Warning: Could not read {txt_path}: {e}")
        return ""


def extract_text_from_md(md_path: str) -> str:
    """Extract text from a Markdown file."""
    return extract_text_from_txt(md_path)


def load_papers(directory: str) -> List[Dict[str, str]]:
    """Load all papers from a directory."""
    papers = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            if filename.endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
            elif filename.endswith('.txt'):
                text = extract_text_from_txt(filepath)
            elif filename.endswith('.md'):
                text = extract_text_from_md(filepath)
            else:
                continue

            if text.strip():
                papers.append({
                    "filename": filename,
                    "path": filepath,
                    "text": text
                })
                print(f"    Loaded: {filename} ({len(text)} chars)")

    return papers


# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================

def analyze_vocabulary(texts: List[str]) -> Dict[str, Any]:
    """Analyze vocabulary usage patterns."""

    combined_text = ' '.join(texts).lower()
    words = re.findall(r'\b[a-z]+\b', combined_text)
    word_count = len(words)

    # Count academic verbs
    high_verb_counts = Counter()
    medium_verb_counts = Counter()
    weak_verb_counts = Counter()

    for word in words:
        if word in ACADEMIC_VERBS_HIGH:
            high_verb_counts[word] += 1
        elif word in ACADEMIC_VERBS_MEDIUM:
            medium_verb_counts[word] += 1
        elif word in WEAK_VERBS:
            weak_verb_counts[word] += 1

    # Normalize per 10,000 words
    scale = 10000 / max(word_count, 1)

    return {
        "total_words": word_count,
        "high_value_verbs": {
            word: round(count * scale, 2)
            for word, count in high_verb_counts.most_common(15)
        },
        "medium_value_verbs": {
            word: round(count * scale, 2)
            for word, count in medium_verb_counts.most_common(15)
        },
        "weak_verbs": {
            word: round(count * scale, 2)
            for word, count in weak_verb_counts.most_common(10)
        },
        "academic_connectors": {
            word: round(combined_text.count(word) * scale, 2)
            for word in ACADEMIC_CONNECTORS
            if combined_text.count(word) > 0
        }
    }


def analyze_abstract_patterns(texts: List[str]) -> Dict[str, Any]:
    """Analyze abstract section patterns."""

    abstract_stats = {
        "papers_analyzed": 0,
        "papers_with_numbers": 0,
        "avg_numbers_per_abstract": 0,
        "papers_with_percentages": 0,
        "papers_with_pvalues": 0,
        "common_structures": []
    }

    number_counts = []

    for text in texts:
        # Try to find abstract section
        abstract_match = re.search(
            r'(?:abstract|summary)[\s:]*\n*(.*?)(?:\n\n|introduction|keywords)',
            text,
            re.IGNORECASE | re.DOTALL
        )

        if abstract_match:
            abstract = abstract_match.group(1)[:1500]  # Limit to ~1500 chars
            abstract_stats["papers_analyzed"] += 1

            # Count numbers
            numbers = re.findall(r'\d+\.?\d*', abstract)
            number_counts.append(len(numbers))

            if len(numbers) >= 1:
                abstract_stats["papers_with_numbers"] += 1

            # Check for percentages
            if re.search(r'\d+\.?\d*\s*%', abstract):
                abstract_stats["papers_with_percentages"] += 1

            # Check for p-values
            if re.search(r'p\s*[<>]\s*0\.\d+', abstract, re.IGNORECASE):
                abstract_stats["papers_with_pvalues"] += 1

    if number_counts:
        abstract_stats["avg_numbers_per_abstract"] = round(
            sum(number_counts) / len(number_counts), 1
        )

    # Calculate percentages
    n = abstract_stats["papers_analyzed"]
    if n > 0:
        abstract_stats["pct_with_numbers"] = round(
            100 * abstract_stats["papers_with_numbers"] / n, 1
        )
        abstract_stats["pct_with_percentages"] = round(
            100 * abstract_stats["papers_with_percentages"] / n, 1
        )
        abstract_stats["pct_with_pvalues"] = round(
            100 * abstract_stats["papers_with_pvalues"] / n, 1
        )

    return abstract_stats


def analyze_sentence_patterns(texts: List[str]) -> Dict[str, Any]:
    """Analyze sentence patterns for Observation-Implication structure."""

    patterns = {
        "observation_implication": [],
        "figure_references": [],
        "comparison_patterns": [],
        "methodology_patterns": []
    }

    pattern_counts = Counter()

    for text in texts:
        sentences = re.split(r'[.!?]+', text)

        for sent in sentences:
            sent = sent.strip()
            if len(sent) < 20:
                continue

            # Check for observation-implication pattern
            for obs in OBSERVATION_MARKERS:
                if obs in sent.lower():
                    for imp in IMPLICATION_MARKERS:
                        if imp in sent.lower():
                            # Found pattern - generalize it
                            generalized = generalize_pattern(sent)
                            pattern_counts[generalized] += 1
                            break

            # Check for figure references
            fig_match = re.search(
                r'figure\s+\d+\s+(?:shows?|reveals?|demonstrates?|indicates?)',
                sent,
                re.IGNORECASE
            )
            if fig_match:
                generalized = re.sub(r'\d+', '[N]', sent[:100])
                patterns["figure_references"].append(generalized)

            # Check for comparison patterns
            if re.search(r'compared\s+to|outperforms?|exceeds?|reduces?.*by', sent, re.IGNORECASE):
                generalized = generalize_pattern(sent[:100])
                patterns["comparison_patterns"].append(generalized)

    # Get top patterns
    patterns["observation_implication"] = [
        {"pattern": p, "count": c}
        for p, c in pattern_counts.most_common(10)
    ]

    # Deduplicate figure patterns
    patterns["figure_references"] = list(set(patterns["figure_references"]))[:5]
    patterns["comparison_patterns"] = list(set(patterns["comparison_patterns"]))[:5]

    return patterns


def generalize_pattern(sentence: str) -> str:
    """Generalize a sentence into a reusable pattern."""
    # Replace numbers
    result = re.sub(r'\d+\.?\d*\s*%?', '[X]', sentence)
    # Replace specific nouns with placeholders
    result = re.sub(r'\b(?:model|method|approach|algorithm)\s+[A-Z]\b', '[Model]', result, flags=re.IGNORECASE)
    # Truncate
    if len(result) > 120:
        result = result[:120] + "..."
    return result


def analyze_figure_captions(texts: List[str]) -> Dict[str, Any]:
    """Analyze figure caption patterns."""

    caption_stats = {
        "total_figures": 0,
        "descriptive_only": 0,
        "conclusionary": 0,
        "with_numbers": 0,
        "examples": {
            "good": [],
            "bad": []
        }
    }

    caption_pattern = re.compile(
        r'(?:figure|fig\.?)\s*\d+[:\.\s]+([^.]+\.)',
        re.IGNORECASE
    )

    for text in texts:
        captions = caption_pattern.findall(text)

        for caption in captions:
            caption_stats["total_figures"] += 1
            caption = caption.strip()

            # Check if conclusionary
            is_conclusionary = any(
                marker in caption.lower()
                for marker in IMPLICATION_MARKERS + ["reveals", "demonstrates", "shows that"]
            )

            # Check for numbers
            has_numbers = bool(re.search(r'\d+\.?\d*', caption))

            if is_conclusionary:
                caption_stats["conclusionary"] += 1
                if len(caption_stats["examples"]["good"]) < 3:
                    caption_stats["examples"]["good"].append(caption[:150])
            else:
                caption_stats["descriptive_only"] += 1
                if len(caption_stats["examples"]["bad"]) < 3:
                    caption_stats["examples"]["bad"].append(caption[:150])

            if has_numbers:
                caption_stats["with_numbers"] += 1

    # Calculate percentages
    n = caption_stats["total_figures"]
    if n > 0:
        caption_stats["pct_conclusionary"] = round(
            100 * caption_stats["conclusionary"] / n, 1
        )
        caption_stats["pct_with_numbers"] = round(
            100 * caption_stats["with_numbers"] / n, 1
        )

    return caption_stats


# ============================================================================
# STYLE GUIDE GENERATION
# ============================================================================

def generate_style_guide(
    vocab: Dict,
    abstracts: Dict,
    patterns: Dict,
    captions: Dict,
    paper_count: int
) -> str:
    """Generate the complete style_guide.md content."""

    content = []

    # Header
    content.append("# O-Prize Style Guide (Auto-Generated)")
    content.append("")
    content.append(f"> **Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    content.append(f"> **Source**: {paper_count} reference papers")
    content.append(f"> **Version**: 1.0")
    content.append("")
    content.append("---")
    content.append("")

    # Introduction
    content.append("## Purpose")
    content.append("")
    content.append("This style guide captures the linguistic patterns and structural conventions")
    content.append("observed in O-Prize winning papers. All writing agents (@writer, @editor,")
    content.append("@narrative_weaver) MUST adhere to these guidelines.")
    content.append("")
    content.append("---")
    content.append("")

    # 1. Vocabulary Constraints
    content.append("## 1. Vocabulary Constraints")
    content.append("")
    content.append("### 1.1 High-Value Academic Verbs (RECOMMENDED)")
    content.append("")
    content.append("Use these verbs to elevate academic tone. Frequency per 10,000 words:")
    content.append("")
    content.append("| Verb | Frequency | Usage |")
    content.append("|------|-----------|-------|")
    for verb, freq in list(vocab.get("high_value_verbs", {}).items())[:10]:
        usage = get_verb_usage(verb)
        content.append(f"| **{verb}** | {freq} | {usage} |")
    content.append("")

    content.append("### 1.2 Medium-Value Verbs (ACCEPTABLE)")
    content.append("")
    content.append("| Verb | Frequency |")
    content.append("|------|-----------|")
    for verb, freq in list(vocab.get("medium_value_verbs", {}).items())[:10]:
        content.append(f"| {verb} | {freq} |")
    content.append("")

    content.append("### 1.3 Weak Verbs (AVOID)")
    content.append("")
    content.append("Replace these with stronger alternatives:")
    content.append("")
    content.append("| Weak Verb | Replacement |")
    content.append("|-----------|-------------|")
    replacements = {
        "show": "demonstrate, reveal, illustrate",
        "get": "obtain, acquire, achieve",
        "do": "perform, execute, conduct",
        "make": "construct, generate, produce",
        "use": "employ, utilize, leverage",
        "have": "possess, exhibit, contain",
        "be": "constitute, represent, serve as",
        "find": "identify, discover, determine",
        "look": "examine, inspect, analyze",
        "see": "observe, perceive, note"
    }
    for weak, replace in replacements.items():
        freq = vocab.get("weak_verbs", {}).get(weak, 0)
        if freq > 0:
            content.append(f"| {weak} ({freq}/10k) | {replace} |")
    content.append("")

    content.append("### 1.4 Academic Connectors")
    content.append("")
    content.append("Use these to strengthen logical flow:")
    content.append("")
    connectors = vocab.get("academic_connectors", {})
    if connectors:
        content.append("| Connector | Frequency | Usage |")
        content.append("|-----------|-----------|-------|")
        connector_usage = {
            "however": "Contrast with previous statement",
            "therefore": "Logical consequence",
            "furthermore": "Additional supporting point",
            "moreover": "Emphasize additional evidence",
            "consequently": "Result of prior statement",
            "nevertheless": "Acknowledge limitation, maintain position",
            "thus": "Summarize logical conclusion",
            "hence": "Direct causal relationship",
            "thereby": "Means by which result achieved"
        }
        for conn, freq in sorted(connectors.items(), key=lambda x: -x[1])[:10]:
            usage = connector_usage.get(conn, "Logical transition")
            content.append(f"| {conn} | {freq} | {usage} |")
    content.append("")

    content.append("---")
    content.append("")

    # 2. Abstract Rules
    content.append("## 2. Abstract Requirements")
    content.append("")
    content.append("### 2.1 Quantitative Content (MANDATORY)")
    content.append("")

    pct_numbers = abstracts.get("pct_with_numbers", 0)
    avg_numbers = abstracts.get("avg_numbers_per_abstract", 0)

    content.append(f"- **{pct_numbers}%** of reference abstracts contain numerical results")
    content.append(f"- Average of **{avg_numbers}** numerical values per abstract")
    content.append("")
    content.append("**RULE**: Abstract MUST contain **≥3 quantitative metrics**")
    content.append("")
    content.append("Examples of required metrics:")
    content.append("- Performance: RMSE, R², accuracy, F1-score")
    content.append("- Comparison: \"↓27% from baseline\", \"3x improvement\"")
    content.append("- Significance: p-values, confidence intervals")
    content.append("")

    content.append("### 2.2 Structure Template")
    content.append("")
    content.append("```")
    content.append("[1-2 sentences: Problem importance and gap]")
    content.append("[1 sentence: Our approach and key innovation]")
    content.append("[1-2 sentences: Main results with NUMBERS]")
    content.append("[1 sentence: Broader implication or policy insight]")
    content.append("```")
    content.append("")
    content.append("### 2.3 Examples")
    content.append("")
    content.append("**GOOD** (contains 5 numbers):")
    content.append("> We develop a hierarchical SIR-network model that achieves **RMSE = 4.2**")
    content.append("> (↓27% from baseline), **R² = 0.89** (p < 0.001), and identifies **3 critical")
    content.append("> hub nodes** for targeted intervention, potentially reducing spread by **34%**.")
    content.append("")
    content.append("**BAD** (contains 0 numbers):")
    content.append("> We develop a novel model to predict epidemic spread. Our approach")
    content.append("> incorporates network structure and performs well on test data.")
    content.append("")

    content.append("---")
    content.append("")

    # 3. Sentence Patterns
    content.append("## 3. Sentence Patterns")
    content.append("")
    content.append("### 3.1 Observation-Implication Pattern (Protocol 15)")
    content.append("")
    content.append("Every data statement MUST follow the Observation-Implication structure:")
    content.append("")
    content.append("```")
    content.append("[OBSERVATION: What the data shows]")
    content.append("    +")
    content.append("[IMPLICATION: What this means physically/economically]")
    content.append("```")
    content.append("")
    content.append("**Templates**:")
    content.append("")

    obs_imp_patterns = patterns.get("observation_implication", [])
    for i, p in enumerate(obs_imp_patterns[:5], 1):
        content.append(f"{i}. \"{p['pattern']}\" ({p['count']} occurrences)")
        content.append("")

    if not obs_imp_patterns:
        # Provide default templates
        content.append("1. \"Figure [N] demonstrates [Quantitative Result], which implies [Physical Mechanism].\"")
        content.append("")
        content.append("2. \"The [metric] increased from [X] to [Y] (Observation), indicating that [mechanism] (Implication).\"")
        content.append("")
        content.append("3. \"While initial model [Action], refined model [Action], resulting in [Outcome with numbers].\"")
        content.append("")

    content.append("### 3.2 Figure Reference Patterns")
    content.append("")

    fig_patterns = patterns.get("figure_references", [])
    if fig_patterns:
        for p in fig_patterns[:3]:
            content.append(f"- \"{p}\"")
    else:
        content.append("- \"Figure [N] reveals [trend], implying [mechanism].\"")
        content.append("- \"As shown in Figure [N], [observation] suggests [implication].\"")
        content.append("- \"Figure [N] demonstrates that [finding], which has implications for [domain].\"")
    content.append("")

    content.append("### 3.3 Comparison Patterns")
    content.append("")
    comp_patterns = patterns.get("comparison_patterns", [])
    if comp_patterns:
        for p in comp_patterns[:3]:
            content.append(f"- \"{p}\"")
    else:
        content.append("- \"Model A outperforms Model B by [X]% (95% CI: [Y]-[Z]).\"")
        content.append("- \"Compared to the baseline, our approach reduces [metric] by [X]%.\"")
        content.append("- \"The proposed method achieves [X], exceeding [benchmark] by [Y].\"")
    content.append("")

    content.append("---")
    content.append("")

    # 4. Figure Caption Standards
    content.append("## 4. Figure Caption Standards")
    content.append("")

    pct_conc = captions.get("pct_conclusionary", 0)
    pct_nums = captions.get("pct_with_numbers", 0)

    content.append(f"Reference paper statistics:")
    content.append(f"- **{pct_conc}%** of captions are conclusionary (not just descriptive)")
    content.append(f"- **{pct_nums}%** of captions contain numerical findings")
    content.append("")
    content.append("### 4.1 Caption Requirements")
    content.append("")
    content.append("**MANDATORY**: Every caption must:")
    content.append("1. State a finding (not just label the figure)")
    content.append("2. Include at least one number or quantitative comparison")
    content.append("3. Connect to the physical/domain meaning")
    content.append("")

    content.append("### 4.2 Examples")
    content.append("")
    content.append("**BAD** (descriptive only):")

    bad_examples = captions.get("examples", {}).get("bad", [])
    if bad_examples:
        for ex in bad_examples[:2]:
            content.append(f"> \"{ex}\"")
    else:
        content.append("> \"Figure 1: Model Results\"")
        content.append("> \"Figure 2: Comparison of Models\"")
    content.append("")

    content.append("**GOOD** (conclusionary with numbers):")

    good_examples = captions.get("examples", {}).get("good", [])
    if good_examples:
        for ex in good_examples[:2]:
            content.append(f"> \"{ex}\"")
    else:
        content.append("> \"Figure 1: Hierarchical model converges to region-specific parameters")
        content.append(">  (β ranges 0.45-0.82), revealing cultural heterogeneity in transmission.\"")
        content.append(">")
        content.append("> \"Figure 2: Network centrality predicts outbreak severity (R²=0.89),")
        content.append(">  with hub seeding accelerating spread by 43% compared to random seeding.\"")
    content.append("")

    content.append("---")
    content.append("")

    # 5. Writing Constraints
    content.append("## 5. Writing Constraints")
    content.append("")
    content.append("### 5.1 Banned Phrases")
    content.append("")
    content.append("| Banned | Replacement |")
    content.append("|--------|-------------|")
    content.append("| \"We used X\" | \"We employed X to achieve Y\" |")
    content.append("| \"The results are good\" | \"The results demonstrate [specific improvement]\" |")
    content.append("| \"Our model works\" | \"Our model achieves RMSE=X (↓Y% from baseline)\" |")
    content.append("| \"Clearly shows\" | \"Demonstrates (p<0.05)\" |")
    content.append("| \"Very significant\" | \"Statistically significant (p<0.001)\" |")
    content.append("")

    content.append("### 5.2 Tense Guidelines")
    content.append("")
    content.append("| Section | Tense | Example |")
    content.append("|---------|-------|---------|")
    content.append("| Abstract | Present/Past | \"We develop... achieves...\" |")
    content.append("| Introduction | Present | \"This problem affects...\" |")
    content.append("| Methods | Past | \"We employed... constructed...\" |")
    content.append("| Results | Past | \"The model achieved... Figure 2 showed...\" |")
    content.append("| Discussion | Present | \"These findings suggest... This implies...\" |")
    content.append("")

    content.append("### 5.3 Uncertainty Language")
    content.append("")
    content.append("Always acknowledge uncertainty appropriately:")
    content.append("")
    content.append("| Certainty Level | Language |")
    content.append("|-----------------|----------|")
    content.append("| Strong evidence | \"demonstrates\", \"confirms\", \"establishes\" |")
    content.append("| Moderate evidence | \"suggests\", \"indicates\", \"implies\" |")
    content.append("| Weak evidence | \"may\", \"could\", \"potentially\" |")
    content.append("| Speculation | \"we hypothesize\", \"one possible explanation\" |")
    content.append("")

    content.append("---")
    content.append("")

    # 6. Protocol 14 Compliance
    content.append("## 6. Protocol 14: Academic Style Alignment")
    content.append("")
    content.append("All writing agents MUST load this style guide and comply with:")
    content.append("")
    content.append("1. **Vocabulary**: Use high-value verbs, avoid weak verbs")
    content.append("2. **Abstract**: ≥3 quantitative metrics required")
    content.append("3. **Sentences**: Follow Observation-Implication pattern")
    content.append("4. **Captions**: Conclusionary format with numbers")
    content.append("5. **Tone**: Academic and objective, avoid hyperbole")
    content.append("")
    content.append("**Violation of these rules is equivalent to a syntax error.**")
    content.append("")

    content.append("---")
    content.append("")
    content.append(f"*Generated by style_analyzer.py on {datetime.now().strftime('%Y-%m-%d')}*")

    return '\n'.join(content)


def get_verb_usage(verb: str) -> str:
    """Get usage example for a verb."""
    usage_examples = {
        "elucidate": "\"We elucidate the mechanism by which...\"",
        "demonstrate": "\"Our results demonstrate that...\"",
        "quantify": "\"We quantify the effect of X on Y...\"",
        "corroborate": "\"These findings corroborate previous...\"",
        "substantiate": "\"The evidence substantiates...\"",
        "delineate": "\"We delineate the boundaries of...\"",
        "postulate": "\"We postulate that the mechanism...\"",
        "validate": "\"We validate our model using...\"",
        "underscore": "\"This finding underscores the importance...\"",
        "manifest": "\"The effect manifests as...\""
    }
    return usage_examples.get(verb, f"\"We {verb} that...\"")


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main(papers_dir: str, output_path: str) -> None:
    """Main analysis pipeline."""

    print(f"\nO-Prize Style Analyzer")
    print(f"=" * 40)
    print(f"Source: {papers_dir}")
    print(f"Output: {output_path}\n")

    # Load papers
    print("Loading papers...")
    papers = load_papers(papers_dir)

    if not papers:
        print("\n  No papers found! Creating default style guide...")
        # Generate with empty data but sensible defaults
        texts = []
    else:
        print(f"\n  Loaded {len(papers)} papers")
        texts = [p["text"] for p in papers]

    # Analyze
    print("\nAnalyzing vocabulary...")
    vocab = analyze_vocabulary(texts)

    print("Analyzing abstract patterns...")
    abstracts = analyze_abstract_patterns(texts)

    print("Analyzing sentence patterns...")
    patterns = analyze_sentence_patterns(texts)

    print("Analyzing figure captions...")
    captions = analyze_figure_captions(texts)

    # Generate style guide
    print("\nGenerating style guide...")
    style_guide = generate_style_guide(
        vocab, abstracts, patterns, captions, len(papers)
    )

    # Write output
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(style_guide)

    print(f"\n  Style guide created: {output_path}")

    # Also save raw analysis as JSON
    json_path = output_path.replace('.md', '_analysis.json')
    analysis = {
        "generated": datetime.now().isoformat(),
        "papers_analyzed": len(papers),
        "vocabulary": vocab,
        "abstracts": abstracts,
        "patterns": {
            "observation_implication_count": len(patterns.get("observation_implication", [])),
            "figure_reference_count": len(patterns.get("figure_references", []))
        },
        "captions": captions
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2)

    print(f"  Analysis JSON: {json_path}")
    print(f"\n  Done!")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python style_analyzer.py <papers_directory> <output_path>")
        print("")
        print("Example:")
        print("  python style_analyzer.py reference_papers/ knowledge_library/academic_writing/style_guide.md")
        print("")
        print("Optional dependencies:")
        print("  pip install pdfplumber spacy")
        print("  python -m spacy download en_core_web_sm")
        sys.exit(1)
