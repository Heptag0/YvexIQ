[English](#yvexiq---english) | [Español](#espanol)

[Español](#yvexiq----español)
[Español](#yvexiq--español)

[Español](#yvexiq)

---

# YvexIQ — English

### Intelligent business queries powered by AI

YvexIQ is a Text-to-SQL system that lets small business owners query their sales data using natural language — no SQL knowledge required. Just ask a question and get instant answers, tables, and charts.

---

## What problem does it solve?

Small business owners have valuable data in their point-of-sale systems but no easy way to analyze it. YvexIQ bridges that gap — connecting directly to their database and translating plain questions into SQL queries, executed locally and privately.

---

## Tech stack

- **Language:** Python
- **LLM:** Ollama + DeepSeek Coder V2 Lite (100% local)
- **Database:** MySQL via SQLAlchemy + PyMySQL
- **Interface:** Streamlit with custom CSS
- **Charts:** Plotly
- **Data:** Pandas

## Project architecture

| File | Description |
|------|-------------|
| `app.py` | Streamlit interface — buttons, suggestions, and results display |
| `main.py` | Main orchestrator — query flow, cache, and error handling |
| `llm.py` | Ollama connection — SQL generation, correction, and natural language response |
| `prompt.py` | LLM instructions — 19 optimized rules for accurate SQL generation |
| `schema.py` | Database schema — tables, columns, and relationships |
| `graficos.py` | Automatic chart detection and generation with Plotly |
| `cache.py` | Session query cache — instant responses for repeated queries |
| `db_connector.py` | MySQL connection via SQLAlchemy and .env credentials |
| `ejecutar_query.py` | SQL query execution and results as DataFrame |

---

## Installation

### Requirements
- Python 3.10+
- Anaconda or Miniconda
- Ollama installed and running
- MySQL database with your business data

> **Note:** Since YvexIQ runs a local AI model, performance depends on your hardware. 
> Response times may vary — a machine with 16GB RAM will respond significantly 
> faster than one with 8GB. For optimal performance, 16GB RAM or more is recommended.

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/Heptag0/YvexIQ.git

# 2. Install dependencies
pip install streamlit sqlalchemy pymysql pandas plotly python-dotenv ollama

# 3. Pull the model
ollama pull deepseek-coder-v2:lite

# 4. Configure your database
# Create a .env file with your credentials
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_database

# 5. Run the app
streamlit run app.py

| Version | Status | Description |
|---------|--------|-------------|
| V1.0.0 | ✅ Done | MySQL connection, local LLM, Streamlit interface |
| V2.0.0 | ✅ Done | Auto SQL correction, Plotly charts, query suggestions |
| V2.1.0 | ✅ Done | Bug fixes — graphs, None display, suggestions |
| V2.2.0 | ✅ Done | Model migration to DeepSeek, fast/deep response modes |
| V2.3.0 | ✅ Done | Clickable suggestions, session state improvements |
| V2.4.0 | ✅ Done | Session query cache for instant repeated responses |
| V2.5.0 | ✅ Done | Custom dark UI — CSS, Plotly theme, YvexIQ branding |
| V2.6.0 | 🔄 In progress | Spanish experience — months, tone, welcome message, input placeholder |
| V2.7.0 | 📅 Planned | Visual feedback — response time, no results message, mode indicator |
| V2.8.0 | 📅 Planned | Installation script for new clients |
| V3.0.0 | 📅 Planned | Cloud API, persistent history, voice input, and much more |


---

# YvexIQ — Español

### Consultas inteligentes para tu negocio impulsadas por IA

YvexIQ es un sistema Text-to-SQL que permite a dueños de pequeños negocios consultar sus datos de ventas usando lenguaje natural — sin necesidad de saber SQL. Solo haz una pregunta y obtén respuestas, tablas y gráficas al instante.

---

## ¿Qué problema resuelve?

Los dueños de negocios tienen datos valiosos en sus sistemas de punto de venta pero sin una forma sencilla de analizarlos. YvexIQ cierra esa brecha — conectándose directamente a su base de datos y traduciendo preguntas en lenguaje natural a consultas SQL, ejecutadas de forma local y privada.

---

## Tecnologías

- **Lenguaje:** Python
- **LLM:** Ollama + DeepSeek Coder V2 Lite (100% local)
- **Base de datos:** MySQL con SQLAlchemy + PyMySQL
- **Interfaz:** Streamlit con CSS personalizado
- **Gráficas:** Pl

## Arquitectura del proyecto

| Archivo | Descripción |
|---------|-------------|
| `app.py` | Interfaz Streamlit — botones, sugerencias y visualización de resultados |
| `main.py` | Orquestador principal — flujo de consultas, caché y manejo de errores |
| `llm.py` | Conexión con Ollama — generación de SQL, corrección y respuesta natural |
| `prompt.py` | Instrucciones del LLM — 19 reglas optimizadas para generación precisa de SQL |
| `schema.py` | Esquema de la base de datos — tablas, columnas y relaciones |
| `graficos.py` | Detección y generación automática de gráficas con Plotly |
| `cache.py` | Caché de consultas por sesión — respuestas instantáneas para preguntas repetidas |
| `db_connector.py` | Conexión MySQL con SQLAlchemy y credenciales via .env |
| `ejecutar_query.py` | Ejecución de consultas SQL y resultados como DataFrame |

---

## Instalación

### Requisitos
- Python 3.10+
- Anaconda o Miniconda
- Ollama instalado y en ejecución
- Base de datos MySQL con los datos de tu negocio

 **Nota:** YvexIQ ejecuta un modelo de IA de forma local, por lo que el rendimiento depende del hardware del usuario. Los tiempos de respuesta pueden variar — una máquina con 16GB de RAM responderá significativamente más rápido que una con 8GB. Para un rendimiento óptimo se recomiendan minimo 16GB de RAM.

### Pasos
```bash
# 1. Clona el repositorio
git clone https://github.com/Heptag0/YvexIQ.git

# 2. Instala las dependencias
pip install streamlit sqlalchemy pymysql pandas plotly python-dotenv ollama

# 3. Descarga el modelo
ollama pull deepseek-coder-v2:lite

# 4. Configura tu base de datos
# Crea un archivo .env con tus credenciales
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tu_base_de_datos

# 5. Ejecuta la app
streamlit run app.py
```
## Hoja de ruta

| Versión | Estado | Descripción |
|---------|--------|-------------|
| V1.0.0 | ✅ Completada | Conexión MySQL, LLM local, interfaz Streamlit |
| V2.0.0 | ✅ Completada | Corrección automática de SQL, gráficas Plotly, sugerencias |
| V2.1.0 | ✅ Completada | Correcciones — gráficas, visualización de None, sugerencias |
| V2.2.0 | ✅ Completada | Migración a DeepSeek, modos de respuesta rápida y profunda |
| V2.3.0 | ✅ Completada | Sugerencias clickeables, mejoras de sesión |
| V2.4.0 | ✅ Completada | Caché de consultas por sesión para respuestas instantáneas |
| V2.5.0 | ✅ Completada | Interfaz oscura personalizada — CSS, tema Plotly, branding YvexIQ |
| V2.6.0 | 🔄 En progreso | Experiencia en español — meses, tono, mensaje de bienvenida, placeholder |
| V2.7.0 | 📅 Planificada | Feedback visual — tiempo de respuesta, mensaje sin resultados, indicador de modo |
| V2.8.0 | 📅 Planificada | Script de instalación para nuevos clientes |
| V3.0.0 | 📅 Planificada | API cloud, historial persistente, entrada por voz, y mucho más |