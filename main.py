from llm import generar_sql
from ejecutar_query import ejecutar

def consultar(pregunta):
    generar = generar_sql(pregunta)
    respuesta = generar.message.content
    respuesta = respuesta.strip().replace("```sql","").replace("```","").replace("'", "'").replace("'", "'").replace("%", "%%")
    if "SELECT" not in respuesta.upper():
        return respuesta
    resultado = ejecutar(respuesta)
    return resultado

## try:
    pregunta_usuario = "Cuanto vendi en total en enero de 2025?"
    resultado_final = consultar(pregunta_usuario)
    print(resultado_final)
## except Exception as e:
    print(f"Error al consultar: {e}")
