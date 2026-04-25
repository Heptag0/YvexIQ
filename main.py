import re
from llm import generar_sql, corregir_sql, generar_respuesta_natural, sugerencia
from ejecutar_query import ejecutar

def consultar(pregunta):
    generar = generar_sql(pregunta)
    respuesta = generar.message.content
    respuesta = re.sub(r'<think>.*?</think>', '', respuesta, flags=re.DOTALL)
    respuesta = respuesta.strip().replace("```sql","").replace("```","").replace("'", "'").replace("'", "'").replace("%", "%%")
    if "SELECT" not in respuesta.upper():
        sugerencias = sugerencia(pregunta).message.content
        return f"No he podido responder esa consulta. Aquí tienes algunas preguntas similares que sí puedo responder:\n\n{sugerencias}", None
    try: 
        resultado = ejecutar(respuesta)
    except Exception as e:
        print(f"ERROR - Reintentando: {e}")
        correccion = corregir_sql(pregunta, respuesta, str(e))
        respuesta_corregida = correccion.message.content
        respuesta_corregida = re.sub(r'<think>.*?</think>', '', respuesta_corregida, flags=re.DOTALL)
        respuesta_corregida = respuesta_corregida.strip().replace("```sql","").replace("```","").replace("'", "'").replace("'", "'").replace("%", "%%")
        try:
            resultado = ejecutar(respuesta_corregida)
        except Exception as e2:
            sugerencias = sugerencia(pregunta).message.content
            return sugerencias, None
    resultado = resultado.round(2)
    resultado.columns = resultado.columns.str.replace("_", " ").str.title()
    ##respuesta_natural = generar_respuesta_natural(pregunta, resultado).message.content
    ##return respuesta_natural, resultado
    return None, resultado

## try:
   # pregunta_usuario = "Cuanto vendi en total en enero de 2025?"
   # resultado_final = consultar(pregunta_usuario)
   # print(resultado_final)
## except Exception as e:
   #x    print(f"Error al consultar: {e}")
  