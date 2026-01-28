#!/usr/bin/env python3
"""
O-Prize Quality Checker for MCM Papers

Verifies that papers meet O-Prize quality standards:
- Abstract has ≥3 quantitative metrics
- 3-5 strategic emphasis paragraphs (key findings highlighted)
- Enhanced captions (complete sentences with observation + insight + implication)
- Narrative hooks present (specific numbers, not generic openings)

Usage:
    python o_prize_quality_checker.py /path/to/paper.tex
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple


class OPrizeQualityChecker:
    """Checks LaTeX papers against O-Prize quality standards."""

    def __init__(self, tex_file: str):
        self.tex_file = Path(tex_file)
        self.content = ""
        self.issues = []
        self.warnings = []
        self.passes = []

        # Quality thresholds
        self.MIN_ABSTRACT_METRICS = 3
        self.MIN_EMPHASIZED_PARAGRAPHS = 3
        self.MAX_EMPHASIZED_PARAGRAPHS = 5

    def read_file(self) -> bool:
        """Read LaTeX file content."""
        try:
            with open(self.tex_file, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except Exception as e:
            self.issues.append(f"CRITICAL: Cannot read file: {e}")
            return False

    def check_abstract_metrics(self) -> None:
        """Verify abstract contains ≥3 quantitative metrics."""
        # Extract abstract
        abstract_match = re.search(
            r'\\begin\{abstract\}(.*?)\\end\{abstract\}',
            self.content,
            re.DOTALL
        )

        if not abstract_match:
            self.issues.append("No abstract found")
            return

        abstract = abstract_match.group(1)

        # Count quantitative metrics (numbers with % or intervals)
        # Pattern: digits, possibly with decimals, followed by %, medal(s), or CI intervals
        metric_patterns = [
            r'\d+\.?\d*\s*%',  # percentages
            r'\d+\.?\d*\s*medals?',  # medal counts
            r'\d+\.?\d*\s*--\s*\d+\.?\d*',  # prediction intervals
            r'\d+\.?\d*\s*nations?',  # country counts
            r'\d+\.?\d*\s*years?',  # time periods
            r'r\s*=\s*[-+]?\d+\.?\d*',  # correlation coefficients
            r'RMSE\s*:\s*\d+\.?\d*',  # RMSE values
        ]

        metric_count = 0
        found_metrics = []

        for pattern in metric_patterns:
            matches = re.findall(pattern, abstract, re.IGNORECASE)
            metric_count += len(matches)
            found_metrics.extend(matches)

        if metric_count >= self.MIN_ABSTRACT_METRICS:
            self.passes.append(
                f"✓ Abstract has {metric_count} quantitative metrics "
                f"(≥{self.MIN_ABSTRACT_METRICS} required)"
            )
        else:
            self.issues.append(
                f"✗ Abstract has only {metric_count} quantitative metrics "
                f"(≥{self.MIN_ABSTRACT_METRICS} required). Found: {found_metrics[:3]}"
            )

    def check_emphasized_paragraphs(self) -> None:
        """Verify 3-5 emphasized paragraphs with bold titles."""
        # Look for \textbf{Title}: pattern
        # These indicate strategic emphasis paragraphs

        emphasis_pattern = r'\\textbf\{([^:]+):\}'

        matches = re.findall(emphasis_pattern, self.content)

        # Filter out common LaTeX uses that aren't our emphasis paragraphs
        # (like \textbf{References}, section titles in TOC, etc.)
        excluded_titles = {
            'references', 'bibliography', 'abstract', 'introduction',
            'conclusion', 'conclusions', 'acknowledgments', 'appendix',
            'table of contents', 'figure', 'table', 'problem', 'background',
            'methods', 'results', 'discussion'
        }

        emphasis_paragraphs = [
            title for title in matches
            if title.lower().strip() not in excluded_titles
            and len(title) > 5  # Exclude short labels
        ]

        if len(emphasis_paragraphs) >= self.MIN_EMPHASIZED_PARAGRAPHS:
            if len(emphasis_paragraphs) <= self.MAX_EMPHASIZED_PARAGRAPHS:
                self.passes.append(
                    f"✓ Found {len(emphasis_paragraphs)} strategic emphasis paragraphs "
                    f"(within {self.MIN_EMPHASIZED_PARAGRAPHS}-{self.MAX_EMPHASIZED_PARAGRAPHS} range)"
                )
            else:
                self.warnings.append(
                    f"⚠ Found {len(emphasis_paragraphs)} emphasis paragraphs "
                    f"(>{self.MAX_EMPHASIZED_PARAGRAPHS} may dilute impact)"
                )
        else:
            self.issues.append(
                f"✗ Found only {len(emphasis_paragraphs)} strategic emphasis paragraphs "
                f"(≥{self.MIN_EMPHASIZED_PARAGRAPHS} required). "
                f"Titles found: {emphasis_paragraphs}"
            )

    def check_caption_quality(self) -> None:
        """Verify captions are complete (observation + insight, not just descriptions)."""
        # Extract all captions
        caption_pattern = r'\\caption\{([^}]+(?:\{[^}]*\}[^}]*)*)\}'
        captions = re.findall(caption_pattern, self.content, re.DOTALL)

        if not captions:
            self.issues.append("No captions found")
            return

        poor_captions = []
        good_captions = []

        for caption in captions:
            # Remove LaTeX commands for analysis
            clean_caption = re.sub(r'\\[a-zA-Z]+', '', caption)
            clean_caption = re.sub(r'\{|\}', '', clean_caption)
            clean_caption = clean_caption.strip()

            # Count sentences (rough approximation by periods)
            sentence_count = clean_caption.count('.')

            # Count numbers
            number_count = len(re.findall(r'\d+\.?\d*', clean_caption))

            # Check for descriptive-only captions (too short, few sentences, no numbers)
            if len(clean_caption) < 50 or sentence_count < 2 or number_count == 0:
                poor_captions.append(clean_caption[:60] + "..." if len(clean_caption) > 60 else clean_caption)
            else:
                good_captions.append(clean_caption)

        if len(poor_captions) == 0:
            self.passes.append(
                f"✓ All {len(captions)} captions appear complete (multi-sentence with numbers)"
            )
        elif len(poor_captions) <= len(captions) * 0.2:  # Allow 20% to be simple
            self.warnings.append(
                f"⚠ {len(poor_captions)}/{len(captions)} captions may be incomplete "
                f"(too short or missing numbers)"
            )
        else:
            self.issues.append(
                f"✗ {len(poor_captions)}/{len(captions)} captions appear incomplete "
                f"(likely descriptive-only, missing insight or numbers)"
            )

    def check_narrative_hooks(self) -> None:
        """Verify introduction uses specific numbers, not generic openings."""
        # Extract introduction section
        intro_match = re.search(
            r'\\section\{Introduction\}(.*?)(?=\\section\{|\\end\{document\})',
            self.content,
            re.DOTALL
        )

        if not intro_match:
            self.warnings.append("Cannot find Introduction section for hook check")
            return

        introduction = intro_match.group(1)

        # Remove abstract if present (some docs include it before section)
        introduction = re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}', '', introduction, flags=re.DOTALL)

        # Check for generic openings
        generic_phrases = [
            r'is important',
            r'has become increasingly important',
            r'plays a crucial role',
            r'has garnered significant attention',
            r'is a critical issue',
            r'has been widely studied',
        ]

        # Check first 200 characters for generic phrases
        intro_start = introduction[:200].lower()

        generic_found = False
        for phrase in generic_phrases:
            if phrase in intro_start:
                self.issues.append(
                    f"✗ Introduction may start with generic phrase: '{phrase}'"
                )
                generic_found = True
                break

        if not generic_found:
            # Check for specific numbers in first paragraph
            first_para = introduction.split('\n\n')[0]
            number_count = len(re.findall(r'\d+\.?\d*', first_para))

            if number_count >= 2:
                self.passes.append(
                    f"✓ Introduction appears to use specific numbers "
                    f"({number_count} quantitative facts in first paragraph)"
                )
            else:
                self.warnings.append(
                    f"⚠ Introduction first paragraph has only {number_count} specific numbers "
                    f"(≥2 recommended for compelling hook)"
                )

    def check_section_transitions(self) -> None:
        """Verify sections have transitions (not just "Next we address...")."""
        # Look for section endings
        # Check if sections end with transitions rather than abrupt stops

        section_pattern = r'\\section\{[^}]+\}'
        section_positions = [(m.start(), m.end()) for m in re.finditer(section_pattern, self.content)]

        if len(section_positions) < 2:
            self.warnings.append("Too few sections to check transitions")
            return

        # This is a rough check - look for transition phrases near section boundaries
        transition_phrases = [
            r'having established',
            r'having demonstrated',
            r'these findings',
            r'this motivates',
            r'we now turn to',
            r'while .{0,50} addressed',
            r'building on',
            r'based on',
        ]

        transitions_found = 0
        sections_checked = 0

        for i, (start, end) in enumerate(section_positions[:-1]):
            # Get text from current section to next section
            next_start = section_positions[i + 1][0]
            section_text = self.content[start:next_start]

            # Check last 200 characters for transition phrases
            section_end = section_text[-200:].lower()

            for phrase in transition_phrases:
                if re.search(phrase, section_end):
                    transitions_found += 1
                    break

            sections_checked += 1

        if transitions_found >= sections_checked * 0.5:  # 50% of sections have transitions
            self.passes.append(
                f"✓ Found transitions in {transitions_found}/{sections_checked} section endings"
            )
        else:
            self.warnings.append(
                f"⚠ Only {transitions_found}/{sections_checked} section endings have clear transitions"
            )

    def check_no_emojis(self) -> None:
        """Verify no emojis are used (unprofessional)."""
        # Common emojis
        emoji_pattern = r'[🔍💡🎯📊📈✅❌⚠️⭐🏆]'

        emojis_found = re.findall(emoji_pattern, self.content)

        if emojis_found:
            self.issues.append(
                f"✗ Found {len(emojis_found)} emoji(s) in LaTeX file: {set(emojis_found)}. "
                "Emojis are unprofessional in academic papers."
            )
        else:
            self.passes.append("✓ No emojis found (professional formatting)")

    def check_no_fboxes(self) -> """
        """Verify no fboxes used for emphasis (decorative, not substantive)."""
        fbox_count = self.content.count('\\fbox')

        if fbox_count > 0:
            self.issues.append(
                f"✗ Found {fbox_count} \\fbox{{}} command(s). "
                "Boxed text is decorative and unprofessional. Use strategic bolding instead."
            )
        else:
            self.passes.append("✓ No decorative fboxes found")

    def run_all_checks(self) -> Tuple[List[str], List[str], List[str]]:
        """Run all quality checks and return (issues, warnings, passes)."""
        if not self.read_file():
            return self.issues, self.warnings, self.passes

        print(f"Checking O-Prize quality for: {self.tex_file}\n")

        self.check_abstract_metrics()
        self.check_emphasized_paragraphs()
        self.check_caption_quality()
        self.check_narrative_hooks()
        self.check_section_transitions()
        self.check_no_emojis()
        self.check_no_fboxes()

        return self.issues, self.warnings, self.passes

    def print_report(self) -> None:
        """Print quality check report."""
        issues, warnings, passes = self.run_all_checks()

        print("=" * 70)
        print("O-PRIZE QUALITY CHECK REPORT")
        print("=" * 70)

        if passes:
            print("\n✓ PASSES:")
            for pass_msg in passes:
                print(f"  {pass_msg}")

        if warnings:
            print("\n⚠ WARNINGS:")
            for warn in warnings:
                print(f"  {warn}")

        if issues:
            print("\n✗ ISSUES (Must Fix):")
            for issue in issues:
                print(f"  {issue}")

        print("\n" + "=" * 70)

        # Summary
        total_issues = len(issues)
        total_warnings = len(warnings)
        total_passes = len(passes)

        print(f"Summary: {total_passes} passes, {total_warnings} warnings, {total_issues} issues")
        print("=" * 70)

        if total_issues == 0:
            print("\n✓ Paper meets O-Prize quality standards!")
            return 0
        else:
            print(f"\n✗ Paper has {total_issues} issue(s) that must be addressed.")
            return 1


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python o_prize_quality_checker.py <paper.tex>")
        print("\nExample:")
        print("  python o_prize_quality_checker.py /path/to/paper.tex")
        sys.exit(1)

    tex_file = sys.argv[1]

    if not Path(tex_file).exists():
        print(f"Error: File not found: {tex_file}")
        sys.exit(1)

    checker = OPrizeQualityChecker(tex_file)
    exit_code = checker.print_report()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
