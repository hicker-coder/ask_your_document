from PyPDF2 import PdfReader


def load_pdf_text(pdf_file):
    """
    Load the text content from a PDF file.
    """
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
