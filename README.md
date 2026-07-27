# LexIA

**Agente de IA para revisión de contratos de Tecnología y Propiedad Intelectual**

LexIA es un asistente basado en Inteligencia Artificial diseñado para apoyar la revisión preliminar de contratos tecnológicos y de propiedad intelectual. Permite identificar cláusulas relevantes, detectar riesgos potenciales y generar informes ejecutivos estructurados para equipos legales, startups y organizaciones orientadas a la innovación.

El proyecto explora la aplicación de Inteligencia Artificial en flujos de trabajo legales, combinando análisis contractual, procesamiento documental y generación automatizada de reportes.

[![IA](https://img.shields.io/badge/IA-Revisi%C3%B3n%20de%20Contratos-7B61FF)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB)](#)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green)](#)
[![Estado](https://img.shields.io/badge/Estado-Prototipo-orange)](#)

---

## Descripción general

LexIA está orientado a la revisión inicial de contratos de tecnología y propiedad intelectual.

El agente analiza contratos relacionados con:

- Acuerdos de software.
- Contratos SaaS.
- Licencias de software.
- Acuerdos de confidencialidad (NDA).
- Cláusulas de propiedad intelectual.
- Protección de datos.
- Servicios tecnológicos.

El objetivo no es reemplazar el criterio profesional legal, sino reducir tareas repetitivas y brindar una capa estructurada de análisis que facilite la toma de decisiones.

---

## Problema que resuelve

Los contratos tecnológicos suelen contener cláusulas complejas que requieren una revisión detallada, especialmente en:

- Titularidad de propiedad intelectual.
- Obligaciones de confidencialidad.
- Limitaciones de responsabilidad.
- Condiciones de terminación.
- Protección de datos.
- Cesión de derechos.

LexIA ayuda mediante:

- Extracción de cláusulas relevantes.
- Identificación de posibles riesgos.
- Organización de hallazgos.
- Generación de informes ejecutivos.

---

## Funcionalidades principales

- Carga de contratos en formato PDF, DOCX o TXT.
- Extracción automática de texto.
- Identificación de cláusulas contractuales relevantes.
- Análisis preliminar de riesgos.
- Detección de aspectos relacionados con tecnología y propiedad intelectual.
- Generación de informes ejecutivos.
- Clasificación de riesgos.
- Selección de idioma del informe.
- Interfaz desarrollada con Streamlit.

---

## Cómo funciona

LexIA sigue el siguiente flujo:

1. La persona usuaria carga un contrato.
2. El sistema extrae el contenido del documento.
3. El agente de IA analiza las cláusulas relevantes.
4. Se identifican riesgos y observaciones.
5. Se genera un informe estructurado.

Ejemplo:

**Entrada:**

Contrato SaaS con cláusulas de propiedad intelectual y responsabilidad.

**Salida:**

Informe estructurado con:

- Resumen del contrato.
- Cláusulas detectadas.
- Observaciones de riesgo.
- Recomendaciones de revisión.

---

## Arquitectura

```mermaid
flowchart TD
    A[Usuario carga contrato] --> B[Lector de documentos]
    B --> C[Extracción de cláusulas]
    C --> D[Agente de análisis contractual IA]
    D --> E[Evaluación de riesgos]
    E --> F[Generación de informe ejecutivo]
    F --> G[Interfaz Streamlit]

    D --> H[(Gemini API)]
    B --> I[(Documento procesado)]
    LEX_IA/
├── agents/
│   └── contract_agent.py
├── utils/
│   ├── pdf_reader.py
│   └── docx_reader.py
├── screenshots/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
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