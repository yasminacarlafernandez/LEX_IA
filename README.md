# LexIA

## Agente de Inteligencia Artificial para revisión de contratos de Tecnología y Propiedad Intelectual

[![IA](https://img.shields.io/badge/IA-Revisi%C3%B3n%20Contractual-7B61FF)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB)](#)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](#)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green)](#)

---

## Descripción

**LexIA** es un agente basado en Inteligencia Artificial diseñado para asistir en la revisión preliminar de contratos tecnológicos y de Propiedad Intelectual.

La aplicación permite analizar documentos contractuales, identificar cláusulas relevantes, detectar posibles riesgos y generar informes ejecutivos estructurados.

El proyecto explora la aplicación de Inteligencia Artificial en procesos legales, combinando:

- Análisis contractual.
- Procesamiento documental.
- Automatización de reportes.
- Tecnología aplicada al Derecho.

LexIA funciona como herramienta de apoyo y no reemplaza el análisis profesional jurídico.

---

# Objetivo del proyecto

Los contratos tecnológicos contienen información crítica relacionada con derechos, obligaciones y riesgos.

LexIA busca facilitar una primera revisión organizada sobre aspectos como:

- Propiedad Intelectual.
- Confidencialidad.
- Protección de datos.
- Limitaciones de responsabilidad.
- Terminación contractual.
- Licencias de software.
- Servicios tecnológicos.

---

# Funcionalidades principales

✅ Carga de contratos en formatos PDF, DOCX y TXT.

✅ Extracción automática del contenido documental.

✅ Identificación de cláusulas contractuales relevantes.

✅ Análisis preliminar de riesgos.

✅ Generación de informes ejecutivos.

✅ Clasificación de hallazgos.

✅ Selector de idioma del reporte.

✅ Interfaz web desarrollada con Streamlit.

---

# Flujo de funcionamiento

```text
Usuario
  |
  v
Carga del contrato
  |
  v
Extracción documental
(PDF / DOCX / TXT)
  |
  v
Análisis mediante agente IA
  |
  v
Identificación de cláusulas y riesgos
  |
  v
Generación de informe ejecutivo
```

---
## Arquitectura

LexIA está compuesto por los siguientes módulos:

```text
Usuario
  |
  v
Carga del contrato
  |
  v
Extracción documental
(PDF / DOCX / TXT)
  |
  v
Agente de análisis contractual IA
  |
  v
Identificación de cláusulas y riesgos
  |
  v
Generación de informe ejecutivo
  |
  v
Interfaz Streamlit
```

### Estructura del proyecto

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

# Capturas de pantalla

### Pantalla principal

![Pantalla principal LexIA](./screenshots/01_portada_lexia.png)

### Carga y análisis del contrato

![Carga y análisis del contrato](./screenshots/02_carga_contrato.png)

### Informe generado

![Informe generado](./screenshots/03_informe_generado.png)

### Vista adicional de análisis

![Vista adicional de análisis](./screenshots/04_analisis_detalle.png)

---

# Demo

Video demostrativo del flujo principal de LexIA:

[Ver demo de LexIA](./screenshots/LEXIA_Demo.mp4)