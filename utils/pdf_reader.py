from pypdf import PdfReader


def read_pdf(uploaded_file):
    """
    Lee un archivo PDF y devuelve su contenido como texto.
    """

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text