# Changelog

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