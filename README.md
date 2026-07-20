![LexIA AI Agent](https://img.shields.io/badge/LexIA-AI%20Agent-blue)

# LexIA

## AI Agent for Technology & Intellectual Property Contract Review

LexIA is a bilingual AI assistant designed to support the preliminary review of technology and intellectual property contracts.

The system identifies key contractual clauses, assesses legal risks, and generates executive summaries using Artificial Intelligence.

---

# Español

LexIA es un asistente de IA bilingüe diseñado para la revisión preliminar de contratos tecnológicos y de propiedad intelectual.

El sistema identifica cláusulas relevantes, evalúa riesgos contractuales y genera informes ejecutivos mediante Inteligencia Artificial.

---

## Features / Características

- 📄 Contract preliminary review / Revisión preliminar de contratos.
- ⚖️ Contract risk identification / Identificación de riesgos legales.
- 🔍 Clause analysis / Análisis de cláusulas relevantes.
- 🔒 Confidentiality and IP review / Revisión de confidencialidad y propiedad intelectual.
- 🌐 Bilingual support English-Spanish / Soporte bilingüe inglés-español.
- 🖥️ Streamlit interactive interface / Interfaz interactiva con Streamlit.

---

## Technologies / Tecnologías

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-docx

---

## Project Structure / Estructura del proyecto
lexia-ai-agent/
│
├── agents/
├── screenshots/
├── utils/
├── app.py
├── requirements.txt
├── .env.example
└── README.md

---

## Configuration / Configuración

Create a `.env` file with:

Crear un archivo `.env` con:

```env
GEMINI_API_KEY=YOUR_API_KEY
pip install -r requirements.txt
streamlit run app.py
Disclaimer / Aviso

LexIA is an academic LegalTech prototype designed to assist with preliminary contract review using Artificial Intelligence.

LexIA es un prototipo académico de LegalTech destinado a asistir en la revisión preliminar de contratos mediante Inteligencia Artificial.

It does not replace professional legal advice.

No reemplaza el asesoramiento jurídico profesional.
