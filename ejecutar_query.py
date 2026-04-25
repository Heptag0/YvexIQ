import pandas as pd
from  db_connector import conectar

def ejecutar(sql_query):
    engine = conectar()
    sql_query = pd.read_sql_query(sql_query, engine)
    return sql_query

##try:
    resultado = ejecutar("""SELECT p.descripcion, SUM(va.cantidad) AS total_cantidad_vendida 
FROM venta_articulos_limpia va 
JOIN productos_limpia p ON va.producto_codigo = p.codigo_producto 
GROUP BY p.descripcion 
ORDER BY total_cantidad_vendida DESC 
LIMIT 5;""")
    print(resultado)
##except Exception as e:
    print(f"Error al ejecutar la consulta SQL: {e}")

