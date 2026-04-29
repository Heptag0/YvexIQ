# Changelog

## V2.5.0
### Mejoras visuales
- Tema oscuro forzado globalmente con config.toml
- Paleta de colores: gris carbón, violeta semitransparente y blanco hueso
- CSS personalizado en archivo independiente styles.css
- Título con nombre YvexIQ e IQ en color violeta
- Input de texto estilizado con hover y focus
- Botones diferenciados — Rápida oscuro, Profunda violeta semitransparente
- Gráficos Plotly con paleta morada y fondo transparente
- Modo oscuro forzado — experiencia consistente independiente del navegador

### Archivos nuevos
- styles.css
- .streamlit/config.toml

### Archivos modificados
- app.py, graficos.py

## V2.4.0
### Nuevas Features
- Caché de consultas por sesión — consultas repetidas responden instantáneamente
- Archivo cache.py con funciones guardar_cache y cargar_cache
- Solo se cachean resultados exitosos, no errores ni sugerencias

### Archivos nuevos
- cache.py

### Archivos modificados
- main.py

## V2.3.0
### Nuevas Features
- Sugerencias clickeables que ejecutan la consulta automáticamente

### Correcciones
- Sugerencias ahora solo proponen consultas que el sistema puede responder
- Fix session_state para mantener sugerencias entre recargas

### Reorganizacion
- app.py reorganizado por bloques con comentarios
- main.py con función limpiar_respuesta() eliminando código duplicado
- llm.py con constante MODELO — cambiar modelo en una sola línea
- grafico.py con constantes PALABRAS_FECHA y ORDEN_MESES
- Docstrings en todas las funciones principales
- Secciones comentadas con── en todos los archivos

### Archivos modificados
- app.py, main.py, llm.py, grafico.py

## V2.2.0
### Cambios de modelo
- Migración de qwen2.5-coder:7b a deepseek-coder-v2:lite
- Test exhaustivo de 6 modelos: sqlcoder, llama3-sqlcoder, yi-coder, deepseek, prem1b, qwen
- deepseek-coder-v2:lite elegido por mejor balance velocidad/precisión

### Nuevas Features
- Botón "⚡ Respuesta rápida" — tabla y gráfico sin texto explicativo
- Botón "🔍 Respuesta profunda" — texto explicativo + tabla + gráfico
- Respuesta natural activada en modo profundo

### Mejoras de prompt
- Prompt optimizado de 19 a 18 reglas
- Regla 19: fix HAVING vs WHERE para filtros de cantidad acumulada
- Fix alucinación de productos (Peso, Pipad, Ballena Pacifico Amarilla)
- Ejemplo de ventas por departamento agregado

### Arquitectura futura definida
- Perfil 8GB RAM: qwen2.5-coder:7b (4.7GB)
- Perfil 16GB RAM: deepseek-coder-v2:lite (8.9GB)
- Perfil 32GB+: qwen3:8b o superior
- Plan VPS Linux con GPU para versión cloud

### Archivos modificados
- main.py, llm.py, app.py, prompt.py

## V2.1.0
### Correcciones
- None ya no aparece en pantalla cuando respuesta natural está desactivada
- Corregido error index out of bounds en gráficos con una sola columna o fila
- Gráfico de pastel ahora se activa correctamente con is_string_dtype
- Sugerencias ya no se activan en respuestas conversacionales

## V2.0.0
### Nuevas Features
- Reintento automático de consultas SQL con autocorrección de errores
- Gráficos automáticos con Plotly (barras, línea y pastel según el tipo de datos)
- Sugerencias de preguntas alternativas cuando no se puede responder
- Spinner de carga "Analizando tu consulta..." en la interfaz

### Mejoras
- Limpieza automática del bloque thinking con re.sub para compatibilidad con modelos futuros
- Función corregir_sql() con contexto del error para mejor autocorrección
- Detección automática del tipo de gráfico según columnas del DataFrame
- Ordenación correcta de meses en gráficos de línea

### Archivos modificados
- main.py, llm.py, app.py, prompt.py, schema.py
### Archivos nuevos
- grafico.py

## V1.5.2
### Correcciones críticas
- Solucionado error de relación entre venta_articulos_limpia y venta_tickets_limpia (columna ticket_id añadida)

### Mejoras de prompt
- Regla 18: interpretación de fechas ambiguas (primera semana, segunda semana, etc.)
- Regla 19: búsqueda de productos por marca/tipo con LIKE

## V1.5.0
### Mejoras
- Separación del prompt a archivo independiente (prompt.py)
- DAYNAME() y MONTHNAME() para nombres de días y meses
- Fechas relativas: "este mes", "mes pasado", "hoy", "esta semana"
- Formato de fechas DD/MM/YYYY
- Redondeo automático a 2 decimales
- Nombres de columnas en formato legible
- Departamentos definidos en el schema
- Soporte para búsqueda de productos con LIKE
- Cálculo de costo de inventario con JOIN automático

### Correcciones
- GROUP BY estricto compatible con MySQL modo estricto
- Sintaxis MySQL exclusiva, eliminada sintaxis PostgreSQL
- Columna pagado_en correctamente referenciada en venta_articulos_limpia

## V1.0.0
- Conexión a MySQL con SQLAlchemy
- Generación de SQL con LLM local via Ollama
- Interfaz web con Streamlit
- Detección de consultas vs conversación casual
- Manejo de errores amigable
- Credenciales seguras con .env