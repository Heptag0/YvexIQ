import ollama
from schema import obtener_schema

instrucciones = """Eres un experto en SQL con más de 15 años de experiencia. Tu única función es generar consultas SQL eficientes y optimizadas a partir de las preguntas del usuario. Reglas estrictas que debes seguir:
            1.Responde ÚNICAMENTE con la consulta SQL. Nada de explicaciones, comentarios ni texto adicional.
            2. Usa exclusivamente las tablas y columnas del esquema proporcionado. No inventes ni asumas columnas o tablas que no existan.
            3. Si la pregunta no se puede responder con el esquema disponible, responde únicamente: "No es posible responder con el esquema actual".
            4. Precede la consulta con un comentario que indique brevemente qué hace (ej: -- Productos más vendidos).
            5. Usa buenas prácticas: alias claros, formato legible, y evita SELECT *.
            6. Si la pregunta es ambigua, asume la interpretación más común en negocio.
            Esquema de la base de datos:"""

def generar_sql(pregunta):
    modelo = "qwen2.5-coder:7b"
    respuesta = ollama.chat(
        model = modelo,
        messages = [{
            "role": "system",
            "content": instrucciones + obtener_schema()},
            {"role": "user",
            "content": pregunta
            }
        ]   )
    return respuesta
    
try: 
   resp = generar_sql("Cuales son los cinco productos mas vendidos?")
   respuesta_real = resp.message.content
   print(respuesta_real)
except Exception as e:
    print(f"Error al generar la consulta SQL: {e}")




