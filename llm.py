import ollama
from schema import obtener_schema
from prompt import obtener_prompt

instrucciones = obtener_prompt() + obtener_schema()

def generar_sql(pregunta):
    modelo = "qwen2.5-coder:7b"
    respuesta = ollama.chat(
        model = modelo,
        messages = [{
            "role": "system",
            "content": instrucciones},
            {"role": "user",
            "content": pregunta
            }
        ]   )
    return respuesta

def corregir_sql(pregunta, sql_fallido, error):
    modelo = "qwen2.5-coder:7b"
    mensaje = f"""La siguiente consulta SQL ha generado un error.
    Pregunta original: {pregunta}
    Error: {error}
    SQL fallido: {sql_fallido}
    IMPORTANTE: En MySQL modo estricto todas las columnas del SELECT que no sean agregaciones deben estar en el GROUP BY.
    IMPORTANTE: La columna producto_nombre NO EXISTE. Usar SIEMPRE descripcion para el nombre del producto.
    Genera un nuevo SQL correcto para responder la pregunta."""
    respuesta = ollama.chat(
        model = modelo,
        messages = [{
            "role": "system",
            "content": instrucciones},
            {"role": "user",
             "content": mensaje}]
         )
    return respuesta

def generar_respuesta_natural(pregunta, resultado):
    modelo = "qwen2.5-coder:7b"
    respuesta = ollama.chat(
        model = modelo,
        messages = [{
            "role": "system",
            "content": "Eres un asistente de negocio. Responde ÚNICAMENTE basándote en los datos proporcionados. NO inventes, asumas ni agregues información que no esté en los resultados. Si los datos no contienen algún campo, no lo menciones. "},
            {"role": "user",
             "content": f"Pregunta: {pregunta} Resultado de la consulta SQL: {resultado.to_string(index=False)} Genera una respuesta natural y profesional basada en el resultado. Responde SOLO con la informacion de los datos anteriores, sin agregar datos externos"}
             ]
         )
    return respuesta

def sugerencia(pregunta):
    modelo = "qwen2.5-coder:7b"
    respuesta = ollama.chat(
        model = modelo,
        messages = [{
            "role": "system",
            "content": "Eres un asistente de negocio. Cuando una consulta no puede responderse, sugiere 2-3 preguntas alternativas similares que sí puedan responderse con datos de ventas, productos y departamentos."
        },
            {"role": "user",
            "content": f"Pregunta original: {pregunta}"}
            ]
    )
    return respuesta

    
#try: 
#  resp = generar_sql("Cuales son los cinco productos mas vendidos?")
#   respuesta_real = resp.message.content
#   print(respuesta_real)
#except Exception as e:
#    print(f"Error al generar la consulta SQL: {e}")