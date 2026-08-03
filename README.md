# ⚖️ LexIA – AI Legal, IP & Compliance Risk Analyzer

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

## 🌟 Overview

LexIA es una herramienta LegalTech impulsada por Inteligencia Artificial diseñada para realizar revisiones preliminares de contratos tecnológicos y documentos vinculados a Propiedad Intelectual.

La aplicación permite identificar cláusulas relevantes, riesgos potenciales, obligaciones críticas y oportunidades de mejora, generando informes ejecutivos para apoyar la toma de decisiones de abogados, startups, equipos de compliance y organizaciones tecnológicas.

Además del análisis contractual tradicional, LexIA incorpora una perspectiva orientada a:

- Propiedad Intelectual
- Inteligencia Artificial
- Protección de Datos
- Compliance Digital
- Transformación Digital

🌎 Español | English

📄 PDF y DOCX

🤖 Google Gemini

⚖️ LegalTech

---

## 📖 Descripción

LexIA es una aplicación desarrollada en Python y Streamlit que utiliza Inteligencia Artificial Generativa para realizar un análisis preliminar de contratos tecnológicos y de propiedad intelectual.

La herramienta permite cargar documentos, extraer automáticamente su contenido y generar un informe ejecutivo identificando cláusulas relevantes, posibles riesgos jurídicos y aspectos críticos para la toma de decisiones.

> **Importante:** LexIA es una herramienta de apoyo para profesionales del Derecho y no reemplaza el análisis jurídico realizado por un abogado.

---

## 🎥 Demo

Video demostrativo del flujo principal de LexIA:

[▶ Ver Demo](screenshots/LEXIA_Demo.mp4)

---

## 📊 Características Principales

✅ Contratos PDF y DOCX

✅ Informes bilingües (Español / English)

✅ Integración con Google Gemini

✅ Análisis mediante IA Generativa

✅ Identificación de cláusulas relevantes

✅ Evaluación preliminar de riesgos

✅ Generación de informes ejecutivos

✅ Interfaz web intuitiva desarrollada con Streamlit

---

## 🚀 Funcionalidades

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

## 🎯 Diferencial de LexIA

A diferencia de herramientas genéricas de análisis documental, LexIA incorpora una revisión enfocada en:

- Contratos tecnológicos
- Licenciamiento de software
- Propiedad Intelectual
- Protección de Datos
- Compliance Digital
- Riesgos emergentes asociados a Inteligencia Artificial

Esto permite una evaluación más alineada con las necesidades actuales de empresas tecnológicas, startups y profesionales jurídicos especializados.

---

## 🔍 Cláusulas Analizadas

- Confidencialidad (NDA)
- Propiedad Intelectual
- Protección de Datos
- Limitación de Responsabilidad
- Terminación
- Ley Aplicable
- Indemnidad

---

## 📸 Capturas de Pantalla

### Pantalla Principal

![Pantalla principal LexIA](screenshots/01_portada_lexia.png)

### Carga y Análisis del Contrato

![Carga y análisis del contrato](screenshots/02_carga_contrato.png)

### Informe Generado

![Informe generado](screenshots/03_informe_generado.png)

### Vista Adicional de Análisis

![Vista adicional de análisis](screenshots/04_analisis_detalle.png)

---

## 💼 Casos de Uso

### Startups

- Revisión preliminar de contratos tecnológicos.
- Identificación de riesgos contractuales.
- Validación inicial de acuerdos SaaS.

### Estudios Jurídicos

- Apoyo en revisiones documentales.
- Identificación rápida de cláusulas relevantes.
- Optimización de tiempos de análisis.

### Equipos de Compliance

- Detección de cláusulas sensibles.
- Revisión de aspectos vinculados a protección de datos.
- Identificación de riesgos regulatorios.

### Profesionales de Propiedad Intelectual

- Revisión de cláusulas de titularidad.
- Licenciamiento de activos intangibles.
- Protección de derechos sobre desarrollos tecnológicos.

---

## ⚙️ Tecnologías Utilizadas

- Python
- Streamlit
- Google Gemini API
- PyPDF
- python-docx
- python-dotenv

---

## 🏗️ Estructura del Proyecto

```text
LEX_IA/
├── app.py
├── agents/
│   └── contract_agent.py
├── utils/
│   ├── pdf_reader.py
│   └── docx_reader.py
├── screenshots/
│   ├── 01_portada_lexia.jpeg
│   ├── 02_carga_contrato.jpeg
│   ├── 03_análisis_del_documento.jpeg
│   ├── 04_informe_generado.jpeg
│   └── LEXIA_Demo.mp4
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🔄 Flujo de Trabajo

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

## 🛠️ Instalación

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

## 🛣️ Roadmap

### Versión Actual

- [x] Análisis de contratos PDF
- [x] Análisis de contratos DOCX
- [x] Integración con Google Gemini
- [x] Informes ejecutivos
- [x] Soporte Español / Inglés

### Próximas Versiones

- [ ] Exportación PDF
- [ ] Dashboard de riesgos
- [ ] Comparación de contratos
- [ ] Historial de análisis
- [ ] Matriz visual de riesgos
- [ ] Módulo de Compliance
- [ ] Evaluación específica de riesgos de IA
- [ ] Análisis avanzado de Propiedad Intelectual

---

## ⚠️ Aviso Legal

Los resultados generados por LexIA tienen fines exclusivamente educativos e informativos.

La herramienta proporciona una revisión preliminar automatizada y no constituye asesoramiento jurídico profesional.

Toda conclusión debe ser revisada y validada por un abogado matriculado antes de su utilización.

---

## 👩‍💼 Autora

**Yasmina Carla Fernández**

- Lawyer (Universidad de Morón)
- Intellectual Property Agent (INPI)
- LegalTech & AI Enthusiast
- Compliance and Technology Law

GitHub:

https://github.com/yasminacarlafernandez

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT.