 # LexIA – Asistente Jurídico con Inteligencia Artificial

## Descripción del proyecto

LexIA es un asistente jurídico desarrollado en Python que utiliza Inteligencia Artificial Generativa (Google Gemini) para analizar documentos legales y responder preguntas en lenguaje natural basándose exclusivamente en el contenido del documento proporcionado.

La aplicación permite cargar contratos en formato PDF o DOCX, extraer automáticamente su contenido y generar respuestas jurídicas preliminares que facilitan la revisión documental, optimizando el tiempo de análisis de abogados, estudiantes y profesionales del derecho.

---

# Objetivo

El objetivo de LexIA es brindar una herramienta de apoyo para el análisis preliminar de documentos jurídicos mediante Inteligencia Artificial, permitiendo identificar de forma rápida información relevante contenida en un contrato.

Entre otros aspectos, el agente puede asistir en la identificación de:

- Partes intervinientes.
- Objeto del contrato.
- Obligaciones de las partes.
- Derechos y responsabilidades.
- Cláusulas de confidencialidad.
- Propiedad intelectual.
- Plazos de vigencia.
- Causales de rescisión.
- Riesgos jurídicos preliminares.
- Observaciones generales para una revisión profesional posterior.

---

# Arquitectura de la solución

```text
                   Usuario
                      │
                      ▼
          Interfaz Web (Streamlit)
                      │
                      ▼
      Carga de documento PDF o DOCX
                      │
                      ▼
     Extracción y procesamiento del texto
                      │
                      ▼
       Google Gemini Generative AI API
                      │
                      ▼
     Generación de respuesta jurídica
                      │
                      ▼
          Respuesta mostrada al usuario
```

---

# Tecnologías utilizadas

- Python 3
- Streamlit
- Google Gemini API
- python-dotenv
- PyPDF2
- python-docx
- Git
- GitHub
- Oracle Cloud Infrastructure (OCI)

---

# Estructura del proyecto

```text
LEX_IA/

│── app.py
│── requirements.txt
│── README.md
│── .env.example
│
├── agents/
│     └── contract_agent.py
│
├── utils/
│     ├── pdf_reader.py
│     └── docx_reader.py
│
├── screenshots/
│     └── deploy.png
│
└── data/
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone TU_URL_DEL_REPOSITORIO
```

## 2. Ingresar al proyecto

```bash
cd LEX_IA
```

## 3. Crear un entorno virtual

```bash
python -m venv venv
```

## 4. Activar el entorno virtual

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 6. Configurar las variables de entorno

Crear un archivo `.env`

```env
GOOGLE_API_KEY=TU_API_KEY
```

## 7. Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# Funcionamiento

1. El usuario carga un documento jurídico en formato PDF o DOCX.
2. La aplicación extrae automáticamente el contenido textual.
3. El texto es enviado al modelo Google Gemini.
4. El usuario realiza consultas en lenguaje natural.
5. El agente genera respuestas basadas exclusivamente en el contenido del documento.

---

# Ejemplos de preguntas

- ¿Cuál es el objeto del contrato?
- ¿Quiénes son las partes intervinientes?
- ¿Cuál es el plazo de vigencia?
- ¿Qué obligaciones tiene cada parte?
- ¿Existe una cláusula de confidencialidad?
- ¿Cómo se regula la propiedad intelectual?
- ¿Existen penalidades por incumplimiento?
- ¿Cuáles son las causales de rescisión?
- ¿Qué riesgos jurídicos presenta el contrato?
- Realiza un resumen del documento.

---

# Ejemplos de respuestas

### Pregunta

> ¿Cuál es el objeto del contrato?

**Respuesta**

El contrato tiene por objeto la prestación de servicios profesionales conforme a las condiciones establecidas entre las partes.

---

### Pregunta

> ¿Existe cláusula de confidencialidad?

**Respuesta**

Sí. El contrato incorpora una cláusula de confidencialidad que obliga a las partes a resguardar la información intercambiada durante la vigencia de la relación contractual.

---

### Pregunta

> ¿Cuál es el plazo de vigencia?

**Respuesta**

El documento establece una vigencia de doce meses contados desde la fecha de suscripción.

---

# Alcance del proyecto

LexIA constituye una herramienta de apoyo para la revisión preliminar de documentación jurídica.

Las respuestas generadas por Inteligencia Artificial tienen carácter orientativo y no sustituyen el criterio profesional de un abogado ni constituyen asesoramiento jurídico.

---

# Deploy en Oracle Cloud Infrastructure (OCI)

La aplicación fue desplegada en Oracle Cloud Infrastructure (OCI).

**URL pública de la aplicación**

TU_URL_DEL_DEPLOY

---

# Evidencia del despliegue

La carpeta `screenshots/` contiene una captura de pantalla de la aplicación ejecutándose correctamente en la nube.

```
screenshots/
└── deploy.png
```

---

# Repositorio

Repositorio GitHub:

TU_URL_DEL_REPOSITORIO

---

# Próximas mejoras

- Soporte para nuevos formatos documentales.
- Exportación de informes en PDF.
- Historial de consultas.
- Mejoras en la interfaz de usuario.
- Optimización del análisis jurídico mediante IA.
- Integración con bases documentales.

---

# Autor

**Yasmina Carla Fernández**

Abogada

Agente de Propiedad Intelectual (INPI)

Proyecto desarrollado como Challenge de Inteligencia Artificial aplicado al ámbito LegalTech.