 import streamlit as st
from agents.contract_agent import analyze_contract
from pypdf import PdfReader
from docx import Document

st.set_page_config(
    page_title="LexIA | AI Legal Assistant",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LexIA - Analizador Jurídico de Contratos")

st.subheader(
    "Asistente jurídico basado en Inteligencia Artificial para el análisis preliminar de contratos"
)

st.markdown("""
LexIA utiliza Inteligencia Artificial para realizar una revisión preliminar de contratos, identificando obligaciones, riesgos legales, cláusulas de confidencialidad y aspectos relacionados con la propiedad intelectual.
""")

st.divider()


def extraer_texto(archivo):

    extension = archivo.name.split(".")[-1].lower()

    if extension == "txt":
        return archivo.read().decode("utf-8")

    elif extension == "pdf":
        pdf = PdfReader(archivo)
        texto = ""

        for pagina in pdf.pages:
            texto += pagina.extract_text() or ""

        return texto

    elif extension == "docx":
        documento = Document(archivo)
        texto = ""

        for parrafo in documento.paragraphs:
            texto += parrafo.text + "\n"

        return texto

    return ""


archivo = st.file_uploader(
    "📄 Subir contrato",
    type=["pdf", "docx", "txt"]
)


if archivo is not None:

    texto = extraer_texto(archivo)

    if texto:

        st.success("✅ Documento cargado correctamente.")

        with st.expander("Vista previa del documento"):
            st.text_area(
                "Contenido extraído:",
                texto,
                height=300
            )

        if st.button("⚖️ Analizar Contrato"):

            try:
                with st.spinner("Analizando contrato..."):

                    resultado = analyze_contract(texto)

                st.divider()
                st.subheader("📋 Informe LexIA")

                st.markdown(resultado)

            except Exception as e:

                st.error(f"Ocurrió un error durante el análisis: {e}")

    else:

        st.error("No se pudo extraer texto del documento.")

else:

    st.info("📄 Suba un contrato en formato PDF, DOCX o TXT para comenzar.")


st.divider()

st.caption(
    "LexIA • Proyecto desarrollado con Streamlit y Google Gemini | Challenge Alura LATAM + Oracle Next Education"
)