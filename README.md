# ⚖️ LexIA – Agente de IA para Análisis de Contratos Tecnológicos y de Propiedad Intelectual

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

## Descripción

LexIA es una aplicación desarrollada en Python y Streamlit que utiliza Inteligencia Artificial para realizar un análisis preliminar de contratos vinculados con Tecnología y Propiedad Intelectual.

La herramienta permite cargar documentos, extraer automáticamente su contenido y generar un informe ejecutivo identificando cláusulas relevantes y posibles riesgos jurídicos.

> **Importante:** LexIA es una herramienta de apoyo para profesionales del Derecho y no reemplaza el análisis jurídico realizado por un abogado.

---

## Funcionalidades

- Carga de contratos en formato PDF.
- Carga de contratos en formato DOCX.
- Extracción automática de texto.
- Análisis mediante Google Gemini.
- Identificación de cláusulas relevantes.
- Evaluación preliminar de riesgos.
- Generación de informe ejecutivo.
- Selección de idioma del informe (Español / Inglés).
- Interfaz web desarrollada con Streamlit.

---

## Cláusulas analizadas

LexIA identifica, entre otras, las siguientes cláusulas:

- Confidencialidad.
- Propiedad Intelectual.
- Protección de Datos.
- Limitación de Responsabilidad.
- Terminación.
- Ley Aplicable.
- Indemnidad.

---

## Tecnologías utilizadas

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-docx
- python-dotenv

---

## Estructura del proyecto

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

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/yasminacarlafernandez/LEX_IA.git
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la API de Gemini

Crear un archivo `.env`

```env
GEMINI_API_KEY=TU_API_KEY
```

### 4. Ejecutar la aplicación

```bash
streamlit run app.py
```

---

## Flujo de trabajo

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

## 1. Pantalla principal

![Pantalla principal](screenshots/01_portada_lexia.png)

---

## 2. Carga del contrato

![Carga del contrato](screenshots/02_carga_contrato.png)

---

## 3. Análisis del documento

![Análisis del documento](screenshots/03_análisis_del_documento.png)

---

## 4. Informe generado

![Informe generado](screenshots/04_informe_generado.png)

---

## 5. Resultado final

![Resultado final](screenshots/05_informe_generado.png)

---

# Demo

Se incluye una demostración en video del funcionamiento de la aplicación.

**Archivo:** `LEXIA_Demo.mp4`

El video muestra:

- Carga de un contrato.
- Procesamiento mediante IA.
- Identificación de cláusulas relevantes.
- Evaluación preliminar de riesgos.
- Generación automática del informe ejecutivo.

---

## Posibles mejoras futuras

- Exportación de informes en PDF.
- Comparación entre contratos.
- Dashboard de riesgos.
- Historial de análisis.
- Nuevos tipos de cláusulas.
- Soporte para formatos adicionales.
- Recomendaciones automáticas de mejora contractual.

---

## Aviso

Los resultados generados por LexIA tienen fines exclusivamente educativos y de apoyo al análisis preliminar de documentos jurídicos.

Toda conclusión debe ser revisada y validada por un profesional del Derecho antes de su utilización.

---

## Autora

**Yasmina Carla Fernández**

- Abogada
- Agente de la Propiedad Intelectual (INPI)
- Especialización en Tecnología, Inteligencia Artificial y Compliance

GitHub:

https://github.com/yasminacarlafernandez

---

## Licencia

Este proyecto se distribuye bajo licencia MIT.