import ollama
from schema import obtener_schema
from prompt import obtener_prompt

# CONFIGURACIÓN 
MODELO = "deepseek-coder-v2:lite"
instrucciones = obtener_prompt() + obtener_schema()

# GENERACIÓN DE SQL 
def generar_sql(pregunta):
    """Genera una consulta SQL a partir de una pregunta en lenguaje natural"""
    return ollama.chat(
        model=MODELO,
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": pregunta}
        ]
    )

# CORRECCIÓN DE SQL 
def corregir_sql(pregunta, sql_fallido, error):
    """Reintenta generar SQL correcto usando el error como contexto"""
    mensaje = f"""La siguiente consulta SQL ha generado un error.
Pregunta original: {pregunta}
Error: {error}
SQL fallido: {sql_fallido}
IMPORTANTE: En MySQL modo estricto todas las columnas del SELECT que no sean agregaciones deben estar en el GROUP BY.
IMPORTANTE: La columna producto_nombre NO EXISTE. Usar SIEMPRE descripcion para el nombre del producto.
Genera un nuevo SQL correcto para responder la pregunta."""

    return ollama.chat(
        model=MODELO,
        messages=[
            {"role": "system", "content": instrucciones},
            {"role": "user", "content": mensaje}
        ]
    )

# RESPUESTA EN LENGUAJE NATURAL
def generar_respuesta_natural(pregunta, resultado):
    """Genera una respuesta en español basada en los resultados del SQL"""
    return ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente de negocio moderno y cercano. Responde ÚNICAMENTE basándote en los datos proporcionados, de forma clara y directa. Usa un tono amigable y natural, como si le explicaras los resultados a un amigo que tiene un negocio. No uses lenguaje técnico innecesario. NO inventes, asumas ni agregues información que no esté en los resultados."
            },
            {
                "role": "user",
                "content": f"Pregunta: {pregunta}\nDatos:\n{resultado.to_string(index=False)}\nResponde SOLO con la información de los datos anteriores, sin agregar datos externos."
            }
        ]
    )

# SUGERENCIAS
def sugerencia(pregunta):
    """Genera preguntas alternativas cuando una consulta no puede responderse"""
    return ollama.chat(
        model=MODELO,
        messages=[
            {
                "role": "system",
                "content": "Eres un asistente de negocio. Cuando una consulta no puede responderse, sugiere 2-3 preguntas alternativas que SÍ puedan responderse. El sistema SOLO tiene datos de: ventas totales, tickets de venta, productos vendidos, ganancias, cantidades, departamentos y fechas. NO sugieras nada sobre clientes, empleados, proveedores, inventario de entrada o cualquier dato que no sea de ventas. Devuelve ÚNICAMENTE las preguntas separadas por |, sin numeración ni texto adicional. Ejemplo: ¿Cuánto vendí este mes?|¿Cuál es el producto más vendido?|¿Qué departamento genera más ganancia?"
            },
            {
                "role": "user",
                "content": f"Pregunta original: {pregunta}"
            }
        ]
    )