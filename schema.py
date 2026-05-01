def obtener_schema():
    return """
Tabla: clientes_clean
Columnas: id (int), nombre (varchar) -- nombre del registro, email (varchar) -- correo electrónico, telefono (varchar) -- número de teléfono, ciudad (varchar) -- ciudad del registro, pais (varchar) -- país del registro, fecha_registro (date) -- fecha en que se registró el cliente, fecha_ultima_compra (date) -- fecha de la última compra del cliente, total_gastado (decimal) -- valor monetario total, activo (int) -- indica si el registro está activo, notas_internas (varchar), codigo_legacy (varchar)

Tabla: departamentos_clean
Columnas: id (int), nombre (varchar) -- nombre del registro, activo (int) -- indica si el registro está activo, codigo_interno (varchar), notas_sistema (varchar)

Tabla: descuentos_clean
Columnas: id (int), ticket_id (int), porcentaje (decimal), motivo (varchar) -- razón o motivo del registro

Tabla: devoluciones_clean
Columnas: id (int), ticket_id (int), producto_id (int), cantidad (int) -- cantidad de unidades, fecha (date) -- fecha del registro, motivo (varchar) -- razón o motivo del registro

Tabla: movimientos_clean
Columnas: id (int), producto_id (int), fecha (date) -- fecha del registro, cantidad_anterior (int) -- unidades en inventario antes del movimiento, cantidad_movimiento (int) -- unidades añadidas o retiradas del inventario, descripcion (varchar) -- nombre o descripción del registro, hash_interno (varchar)

Tabla: productos_clean
Columnas: id (int), codigo (varchar), descripcion (varchar) -- nombre o descripción del registro, talla (varchar) -- talla del producto, color (varchar) -- color del producto, temporada (varchar) -- temporada de la colección del producto, precio_costo (decimal) -- precio de compra al proveedor, precio_venta (decimal) -- precio de venta al cliente, stock_actual (int) -- unidades disponibles actualmente en inventario, departamento_id (int), proveedor_id (int), fecha_creado (date) -- fecha de creación del producto, codigo_barras_viejo (varchar), notas (varchar), ultima_modificacion_sistema (date)

Tabla: proveedores_clean
Columnas: id (int), nombre (varchar) -- nombre del registro, pais (varchar) -- país del registro, email (varchar) -- correo electrónico, telefono (varchar) -- número de teléfono

Tabla: ticket_productos_clean
Columnas: id (int), ticket_id (int), producto_id (int), cantidad (int) -- cantidad de unidades, precio_unitario (decimal) -- precio del producto, total (decimal) -- valor monetario total, ganancia (decimal) -- beneficio económico

Tabla: tickets_clean -- tabla principal de ventas, cada fila es una venta
Columnas: id (int), cliente_id (int), total (decimal) -- valor monetario total, ganancia (decimal) -- beneficio económico, fecha (date) -- fecha del registro, numero_articulos (int), metodo_pago (varchar) -- método de pago usado — efectivo, tarjeta o transferencia, canal (varchar) -- canal de venta — tienda física, online o teléfono, operador_codigo (varchar) -- código del operador que realizó la venta

"""
