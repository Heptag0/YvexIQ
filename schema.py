def obtener_schema():
    return """
Tabla: productos_limpia
Columnas: ID (int),
codigo_producto (text),
descripcion (text) -- este es el nombre del producto, NUNCA USAR PRODUCTO NOMBRE COMO COLUMNA PARA CONSULTAS, SIEMPRE USAR DESCRIPCION YA QUE ES LA CORRECTA.
precio_costo (double),
precio_venta (double),
departamento (int), -- este es el ID del departamento,
porcentaje_ganancia (double),
fecha_editado (text),
es_kit (text),
eliminado_en (text) -- si el producto fue eliminado

Tabla: venta_tickets_limpia
Columnas: ID (int),
total (double),
ganancia (double),
fecha_venta (text),
numero_articulos (int)

Tabla: venta_articulos_limpia
Columnas: ID (int),
producto_codigo (varchar), -- codigo del producto
producto_nombre (varchar),
cantidad (float),
precio_final (decimal), -- precio final por una unidad.
total_articulo (decimal), -- precio_final * cantidad
ganancia (decimal), -- ganancia por un articulo
departamento_ID (int),
pagado_en (timestamp) -- fecha y hora de la venta

Tabla: inventario_limpia
Columnas: ID (int),
producto_id (int),
fecha_movimiento (text),
cantidad_anterior (double),
cantidad_movimiento (double),
descripcion (text) -- descripcion del movimiento

Tabla: departamentos_limpia
Columnas: ID (int),
departamento (text), --nombre del departamento
activo (int)

Relaciones:
- venta_articulos_limpia.ID = venta_tickets_limpia.ID
- venta_articulos_limpia.producto_codigo = productos_limpia.codigo_producto
- venta_articulos_limpia.departamento_ID = departamentos_limpia.ID
- inventario_limpia.producto_id = productos_limpia.ID

IMPORTANTE: En productos_limpia el nombre del producto es "descripcion", NO "producto_nombre"
"""