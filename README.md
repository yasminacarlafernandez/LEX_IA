# LexIA – Asistente Jurídico con Inteligencia Artificial

## Descripción del proyecto

LexIA es un prototipo de asistente jurídico basado en inteligencia artificial diseñado para apoyar el análisis preliminar de contratos.

El proyecto busca explorar la aplicación de herramientas de IA en el ámbito legal, facilitando la revisión inicial de documentos contractuales mediante la extracción de información relevante y la generación de informes jurídicos estructurados.

## Objetivo

El objetivo de LexIA es brindar una herramienta de apoyo para abogados y profesionales del derecho, permitiendo identificar aspectos relevantes de un contrato, tales como:

- Partes intervinientes.
- Obligaciones principales.
- Cláusulas relevantes.
- Riesgos legales preliminares.
- Confidencialidad y propiedad intelectual.
- Observaciones generales para una revisión profesional posterior.

## Funcionalidades actuales

- Carga y lectura de documentos contractuales.
- Soporte para archivos PDF y DOCX.
- Extracción del contenido del documento.
- Análisis preliminar mediante inteligencia artificial.
- Generación de una estructura de revisión jurídica.

## Tecnologías utilizadas

- Python.
- Streamlit.
- Google Gemini API.
- Procesamiento de documentos PDF y DOCX.

## Estructura del proyecto
LEX_IA/
│
├── app.py
├── requirements.txt
├── agents/
│ └── contract_agent.py
│
├── utils/
│ ├── pdf_reader.py
│ └── docx_reader.py
│
└── README.md

## Alcance del proyecto

LexIA constituye una herramienta experimental de LegalTech orientada a la asistencia en tareas jurídicas preliminares.

El resultado generado por el sistema no reemplaza el análisis profesional del abogado, sino que funciona como apoyo para optimizar tiempos de revisión y organización de información contractual.

## Próximas mejoras

- Incorporación de exportación de informes jurídicos en formatos profesionales.
- Mejoras en la interfaz de usuario.
- Optimización del modelo de análisis contractual.
- Ampliación de criterios de evaluación jurídica.
