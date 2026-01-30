# -*- coding: utf-8 -*-
"""
PDF to Markdown converter using docling.
Fallback when docling MCP times out.

Usage:
    python pdf_to_markdown.py <input_pdf> <output_md>
"""

import sys
import os

def convert_pdf_to_markdown(pdf_path: str, output_path: str):
    """Convert PDF to Markdown using docling."""
    try:
        from docling.document_converter import DocumentConverter

        print(f"Converting: {pdf_path}")

        converter = DocumentConverter()
        result = converter.convert(pdf_path)

        # Export to markdown
        markdown_content = result.document.export_to_markdown()

        # Write output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"Output saved to: {output_path}")
        return True

    except ImportError:
        print("docling not installed. Installing...")
        os.system(f"{sys.executable} -m pip install docling")
        # Retry after install
        return convert_pdf_to_markdown(pdf_path, output_path)
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
