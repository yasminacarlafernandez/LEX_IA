 ![LexIA AI Agent](https://img.shields.io/badge/LexIA-AI%20Agent-blue)

# LexIA – AI Legal Assistant

LexIA es un asistente jurídico desarrollado con Python, Streamlit y Google Gemini para realizar una revisión preliminar de documentos contractuales mediante Inteligencia Artificial.

## Características

- Análisis preliminar de contratos.
- Identificación de riesgos legales.
- Revisión de obligaciones contractuales.
- Evaluación de cláusulas de confidencialidad.
- Revisión de aspectos de propiedad intelectual.
- Interfaz desarrollada con Streamlit.

## Tecnologías

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-docx

## Estructura del proyecto

```
lexia-ai-agent/
│
├── agents/
├── screenshots/
├── utils/
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

## Configuración

Crear un archivo `.env` con la siguiente variable:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Ejecución

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Aviso

LexIA constituye un prototipo académico de LegalTech destinado a realizar revisiones preliminares de contratos mediante Inteligencia Artificial. No reemplaza el asesoramiento jurídico profesional.