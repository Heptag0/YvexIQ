def obtener_schema():
    return """
Tabla: productos_limpia
Columnas: ID (int), codigo_producto (text), descripcion (text) -- NOMBRE del producto ADVERTENCIA: La columna "producto_nombre" NO EXISTE en esta tabla. 
Usar SIEMPRE "descripcion" para el nombre del producto., precio_costo (double), precio_venta (double), departamento (int) -- ID del departamento hace JOIN con departamentos_limpia.ID, porcentaje_ganancia (double), fecha_editado (text), es_kit (text), eliminado_en (text) -- fecha de registro, ignorar para filtrar productos activos
IMPORTANTE: La tabla tiene 383 productos activos. Para contarlos usar SELECT COUNT(*) FROM productos_limpia SIN WHERE.

Tabla: venta_tickets_limpia
Columnas: ID (int), total (double), ganancia (double), fecha_venta (text) -- formato 'YYYY-MM-DD'. ES LA ÚNICA COLUMNA DE FECHA EN ESTA TABLA., numero_articulos (int)

Tabla: venta_articulos_limpia
Columnas: ID (int), TICKET_ID (int), producto_codigo (varchar), producto_nombre (varchar), cantidad (float), precio_final (decimal) -- precio por unidad, total_articulo (decimal) -- precio_final x cantidad, ganancia (decimal), departamento_ID (int), pagado_en (timestamp) -- fecha y hora de la venta. USAR ESTA COLUMNA para filtrar por fecha en esta tabla

Tabla: inventario_limpia
Columnas: ID (int), producto_id (int), fecha_movimiento (text), cantidad_anterior (double), cantidad_movimiento (double), descripcion (text) -- descripcion del movimiento
-- Para calcular costo de inventario hacer JOIN con productos_limpia usando: inventario_limpia.producto_id = productos_limpia.ID y multiplicar cantidad_movimiento por precio_costo

Tabla: departamentos_limpia
Columnas: ID (int), departamento (text), activo (int)
Departamentos existentes: 1=Sin Departamento, 2=Productos Comunes, 4=LICORES, 5=Licores, 6=Cigarros, 7=Latas/latones, 8=Cuartitos/Medias, 9=Ballena/ballenon, 10=Bebidas, 11=Sabritas, 12=Dulces, 13=Pastillas, 14=Galletas, 15=Otros, 16=Abarrotes, 17=Bimbo

Relaciones:
- venta_articulos_limpia.TICKET_ID = venta_tickets_limpia.ID
- venta_articulos_limpia.producto_codigo = productos_limpia.codigo_producto
- venta_articulos_limpia.departamento_ID = departamentos_limpia.ID
- inventario_limpia.producto_id = productos_limpia.ID
"""