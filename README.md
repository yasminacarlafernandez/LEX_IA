# ⚖️ LexIA – Agente de IA para Análisis de Contratos Tecnológicos y de Propiedad Intelectual

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

## Descripción

LexIA es una aplicación desarrollada en Python y Streamlit que utiliza Inteligencia Artificial para realizar un análisis preliminar de contratos tecnológicos y de propiedad intelectual.

La herramienta permite cargar documentos, extraer automáticamente su contenido y generar un informe ejecutivo identificando cláusulas relevantes y posibles riesgos jurídicos.

> **Importante:** LexIA es una herramienta de apoyo para profesionales del Derecho y no reemplaza el análisis jurídico realizado por un abogado.

---

## Funcionalidades

- Carga de contratos en formato PDF y DOCX.
- Extracción automática de texto.
- Análisis mediante Google Gemini.
- Identificación de cláusulas contractuales relevantes.
- Evaluación preliminar de riesgos.
- Generación de informe ejecutivo.
- Clasificación de riesgos.
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
LEX_IA/
├── app.py
├── agents/
│   └── contract_agent.py
├── utils/
│   ├── pdf_reader.py
│   └── docx_reader.py
├── screenshots/
│   ├── 01_portada_lexia.png
│   ├── 02_carga_contrato.png
│   ├── 03_informe_generado.png
│   ├── 04_analisis_detalle.png
│   └── LEXIA_Demo.mp4
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
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

## Capturas de pantalla

### Pantalla principal

![Pantalla principal LexIA](./screenshots/01_portada_lexia.png)

### Carga y análisis del contrato

![Carga y análisis del contrato](./screenshots/02_carga_contrato.png)

### Informe generado

![Informe generado](./screenshots/03_informe_generado.png)

### Vista adicional de análisis

![Vista adicional de análisis](./screenshots/04_analisis_detalle.png)

---

## Demo

Video demostrativo del flujo principal de LexIA:

[Ver demo de LexIA](./screenshots/LEXIA_Demo.mp4)

---

## Casos de uso

- Abogados especializados en Tecnología.
- Profesionales de Propiedad Intelectual.
- Startups.
- Empresas SaaS.
- Estudios jurídicos.
- Equipos de Compliance.

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