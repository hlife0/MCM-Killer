# -*- coding: utf-8 -*-
"""
PDF to Markdown converter using docling CLI (preferred).
Fallback when docling MCP times out.

Usage:
    python pdf_to_markdown.py <input_pdf> <output_md>
"""

import sys
import os
import subprocess


def convert_pdf_to_markdown(pdf_path: str, output_path: str):
    """Convert PDF to Markdown using docling CLI (preferred)."""
    try:
        # Get output directory from output_path
        output_dir = os.path.dirname(output_path) or "."
        os.makedirs(output_dir, exist_ok=True)

        print(f"Converting via docling CLI: {pdf_path}")

        result = subprocess.run(
            ["docling", "--to", "md", "--output", output_dir, pdf_path],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            # docling outputs to output_dir with same basename as input
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            generated_file = os.path.join(output_dir, f"{base_name}.md")

            # Rename to expected output_path if different
            if generated_file != output_path and os.path.exists(generated_file):
                os.rename(generated_file, output_path)

            print(f"Output saved to: {output_path}")
            return True
        else:
            print(f"docling CLI error: {result.stderr}")
            return False

    except FileNotFoundError:
        print("docling CLI not found, falling back to PyMuPDF...")
        return False
    except subprocess.TimeoutExpired:
        print("docling CLI timeout, falling back to PyMuPDF...")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def convert_with_pymupdf_fallback(pdf_path: str, output_path: str):
    """Fallback using PyMuPDF if docling fails."""
    try:
        import fitz  # PyMuPDF

        print(f"Using PyMuPDF fallback for: {pdf_path}")

        doc = fitz.open(pdf_path)
        markdown_lines = []

        for page_num, page in enumerate(doc):
            text = page.get_text()
            markdown_lines.append(f"\n## Page {page_num + 1}\n")
            markdown_lines.append(text)

        doc.close()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_lines))

        print(f"Output saved to: {output_path}")
        return True

    except ImportError:
        print("PyMuPDF not installed. Installing...")
        os.system(f"{sys.executable} -m pip install PyMuPDF")
        return convert_with_pymupdf_fallback(pdf_path, output_path)
    except Exception as e:
        print(f"PyMuPDF fallback error: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_markdown.py <input_pdf> <output_md>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)

    # Try docling first, fall back to PyMuPDF
    success = convert_pdf_to_markdown(pdf_path, output_path)
    if not success:
        print("Docling failed, trying PyMuPDF fallback...")
        success = convert_with_pymupdf_fallback(pdf_path, output_path)

    sys.exit(0 if success else 1)
