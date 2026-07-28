# ⚖️ LexIA – Agente de IA para el análisis preliminar de contratos tecnológicos y de Propiedad Intelectual

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

## Descripción

LexIA es una aplicación desarrollada en Python y Streamlit que utiliza Inteligencia Artificial para realizar un análisis preliminar de contratos vinculados con Tecnología y Propiedad Intelectual.

La herramienta permite cargar documentos, extraer automáticamente su contenido y generar un informe ejecutivo identificando cláusulas relevantes y posibles riesgos jurídicos.

> **Importante:** LexIA constituye una herramienta de apoyo para profesionales del Derecho y no reemplaza el análisis ni el criterio jurídico de un abogado.

---

# Funcionalidades

- Carga de contratos en formato PDF y DOCX.
- Extracción automática del texto.
- Análisis mediante Google Gemini.
- Identificación de cláusulas relevantes.
- Evaluación preliminar de riesgos.
- Generación de informe ejecutivo.
- Selección del idioma del informe (Español / Inglés).
- Interfaz web desarrollada con Streamlit.

---

# Cláusulas analizadas

LexIA busca identificar, entre otras, las siguientes cláusulas:

- Confidencialidad
- Propiedad Intelectual
- Protección de Datos
- Limitación de Responsabilidad
- Terminación
- Ley Aplicable
- Indemnidad

---

# Tecnologías utilizadas

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-docx
- python-dotenv

---

# Estructura del proyecto

```text
LEXIA
│
├── agents
│   └── contract_agent.py
│
├── utils
│   ├── pdf_reader.py
│   └── docx_reader.py
│
├── screenshots
│
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/yasminacarlafernandez/LEX_IA.git
```

## 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 3. Configurar la API de Gemini

Crear un archivo `.env`

```env
GEMINI_API_KEY=TU_API_KEY
```

## 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# Flujo de trabajo

```text
Carga del contrato
        │
        ▼
Extracción del texto
        │
        ▼
Análisis mediante IA
        │
        ▼
Identificación de cláusulas
        │
        ▼
Evaluación de riesgos
        │
        ▼
Generación del informe
```

---

# Capturas de pantalla

## Pantalla principal

![Pantalla principal](screenshots/home.png)

---

## Carga del contrato

![Carga](screenshots/upload.png)

---

## Resultado del análisis

![Resultado](screenshots/analysis.png)

---

## Informe generado

![Informe](screenshots/report.png)

---

# Demostración

A continuación se muestra una demostración del funcionamiento de la aplicación mediante un GIF.

![Demo](screenshots/demo.gif)

---

# Posibles mejoras

- Exportación del informe en PDF.
- Comparación entre versiones de contratos.
- Panel de métricas y riesgos.
- Incorporación de nuevos tipos de cláusulas.
- Soporte para más formatos de documentos.
- Historial de análisis.
- Mayor personalización del reporte.

---

# Aviso

Los resultados generados por LexIA poseen fines exclusivamente educativos y de apoyo al análisis preliminar de documentos jurídicos.

Toda conclusión debe ser revisada y validada por un profesional del Derecho antes de su utilización.

---

# Autora

**Yasmina Carla Fernández**

Abogada

Agente de la Propiedad Intelectual (INPI)

Especialización en Tecnología, Inteligencia Artificial y Compliance.

GitHub:
https://github.com/yasminacarlafernandez

---

# Licencia

Este proyecto se distribuye bajo la licencia MIT.