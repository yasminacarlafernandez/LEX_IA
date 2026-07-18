from docx import Document


def read_docx(uploaded_file):
    """
    Lee un archivo DOCX y devuelve su contenido como texto.
    """

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text