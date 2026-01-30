import pdfplumber
import sys

pdf_path = "2026_MCM_Problem_C.pdf"

try:
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n\n"
        print(full_text)
except Exception as e:
    print(f"Error reading PDF: {e}", file=sys.stderr)
