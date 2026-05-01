import mysql.connector
import random
from faker import Faker
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# CONFIGURACIÓN
load_dotenv()
fake = Faker(['es_ES', 'en_US', 'fr_FR', 'de_DE', 'it_IT'])
Faker.seed(0)

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT"))
}

DB_NAME = "yvexiq_demo"

def conectar(database=None):
    config = DB_CONFIG.copy()
    if database:
        config["database"] = database
    return mysql.connector.connect(**config)

def crear_base_datos():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")
    
    # DEPARTAMENTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departamentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            activo TINYINT DEFAULT 1,
            codigo_interno VARCHAR(20),
            notas_sistema TEXT
        )
    """)
    
    # CLIENTES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            email VARCHAR(100),
            telefono VARCHAR(50),
            ciudad VARCHAR(100),
            pais VARCHAR(100),
            fecha_registro DATE,
            fecha_ultima_compra DATE,
            total_gastado DECIMAL(10,2),
            activo TINYINT DEFAULT 1,
            notas_internas TEXT,
            codigo_legacy VARCHAR(50)
        )
    """)

    # PROVEEDORES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proveedores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            pais VARCHAR(100),
            email VARCHAR(100),
            telefono VARCHAR(50)
        )
    """)

    # PRODUCTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            codigo VARCHAR(50),
            descripcion VARCHAR(200),
            talla VARCHAR(10),
            color VARCHAR(50),
            temporada VARCHAR(20),
            precio_costo DECIMAL(10,2),
            precio_venta DECIMAL(10,2),
            stock_actual INT,
            departamento_id INT,
            proveedor_id INT,
            fecha_creado DATE,
            codigo_barras_viejo VARCHAR(50),
            notas TEXT,
            ultima_modificacion_sistema TIMESTAMP
        )
    """)

    # TICKETS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            cliente_id INT,
            total DECIMAL(10,2),
            ganancia DECIMAL(10,2),
            fecha DATE,
            numero_articulos INT,
            metodo_pago VARCHAR(20),
            canal VARCHAR(20),
            terminal_id VARCHAR(20),
            operador_codigo VARCHAR(20)
        )
    """)

    # TICKET_PRODUCTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ticket_productos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ticket_id INT,
            producto_id INT,
            cantidad INT,
            precio_unitario DECIMAL(10,2),
            total DECIMAL(10,2),
            ganancia DECIMAL(10,2)
        )
    """)

    # MOVIMIENTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimientos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            producto_id INT,
            fecha DATE,
            cantidad_anterior INT,
            cantidad_movimiento INT,
            descripcion TEXT,
            sistema_origen VARCHAR(50),
            hash_interno VARCHAR(100)
        )
    """)

    # DESCUENTOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS descuentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ticket_id INT,
            porcentaje DECIMAL(5,2),
            motivo VARCHAR(100)
        )
    """)

    # DEVOLUCIONES
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devoluciones (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ticket_id INT,
            producto_id INT,
            cantidad INT,
            fecha DATE,
            motivo VARCHAR(100)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Base de datos y tablas creadas correctamente")

def generar_departamentos(cursor):
    departamentos = [
        "Ropa Mujer", "Ropa Hombre", "Ropa Niños", 
        "Calzado", "Accesorios", "Deportivo", 
        "Temporada", "Outlet", "Premium", "Básicos"
    ]
    for nombre in departamentos:
        cursor.execute("""
            INSERT INTO departamentos (nombre, activo, codigo_interno, notas_sistema)
            VALUES (%s, %s, %s, %s)
        """, (
            nombre,
            random.choice([1, 1, 1, 0]), 
            fake.bothify(text="DEP-###") if random.random() > 0.2 else None,
            fake.text(50) if random.random() > 0.7 else None 
        ))
    print("✅ Departamentos generados")


def generar_proveedores(cursor):
    paises = ["España", "Francia", "Italia", "USA", "China", "Portugal", "Alemania"]
    for _ in range(20):
        cursor.execute("""
            INSERT INTO proveedores (nombre, pais, email, telefono)
            VALUES (%s, %s, %s, %s)
        """, (
            fake.company(),
            random.choice(paises),
            fake.email() if random.random() > 0.15 else None,
            fake.phone_number() if random.random() > 0.2 else None
        ))
    print("✅ Proveedores generados")


def generar_clientes(cursor, n=200):
    for _ in range(n):
        fecha_registro = fake.date_between(start_date="-3y", end_date="today")
        cursor.execute("""
            INSERT INTO clientes (nombre, email, telefono, ciudad, pais, 
                                fecha_registro, fecha_ultima_compra, total_gastado,
                                activo, notas_internas, codigo_legacy)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.name(),
            fake.email() if random.random() > 0.1 else None,
            fake.phone_number() if random.random() > 0.2 else None,
            fake.city() if random.random() > 0.15 else None,
            fake.country(),
            fecha_registro,
            fake.date_between(start_date=fecha_registro, end_date="today") if random.random() > 0.1 else None,
            round(random.uniform(50, 5000), 2) if random.random() > 0.1 else None,
            random.choice([1, 1, 1, 0]),
            fake.text(100) if random.random() > 0.8 else None, 
            fake.bothify(text="LEG-####") if random.random() > 0.6 else None 
        ))
    print(f"✅ {n} clientes generados")

def generar_productos(cursor, n=400):
    tallas = ["XS", "S", "M", "L", "XL", "XXL", "36", "37", "38", "39", "40", "41", "42"]
    colores = ["Negro", "Blanco", "Rojo", "Azul", "Verde", "Gris", "Beige", "Rosa", "Amarillo", "Naranja"]
    temporadas = ["Primavera", "Verano", "Otoño", "Invierno", "Todo el año"]
    
    tipos_ropa = [
        "Camiseta", "Pantalón", "Vestido", "Falda", "Chaqueta", "Abrigo",
        "Sudadera", "Jersey", "Camisa", "Shorts", "Leggings", "Blazer",
        "Zapatillas", "Botas", "Sandalias", "Zapatos", "Deportivas",
        "Cinturón", "Bolso", "Bufanda", "Gorro", "Guantes"
    ]
    marcas = ["Urban", "Classic", "Sport", "Elegant", "Casual", "Basic", "Premium", "Trend"]

    for i in range(n):
        precio_costo = round(random.uniform(5, 150), 2)
        precio_venta = round(precio_costo * random.uniform(1.3, 2.5), 2)
        
        cursor.execute("""
            INSERT INTO productos (codigo, descripcion, talla, color, temporada,
                                precio_costo, precio_venta, stock_actual,
                                departamento_id, proveedor_id, fecha_creado,
                                codigo_barras_viejo, notas, ultima_modificacion_sistema)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            fake.bothify(text="PROD-####-??").upper(),
            f"{random.choice(marcas)} {random.choice(tipos_ropa)}",
            random.choice(tallas) if random.random() > 0.1 else None,
            random.choice(colores) if random.random() > 0.1 else None,
            random.choice(temporadas),
            precio_costo if random.random() > 0.05 else None,
            precio_venta,
            random.randint(0, 200),
            random.randint(1, 10),
            random.randint(1, 20),
            fake.date_between(start_date="-3y", end_date="today"),
            fake.bothify(text="BAR-########") if random.random() > 0.6 else None,
            fake.text(50) if random.random() > 0.8 else None,
            fake.date_time_between(start_date="-3y", end_date="now") if random.random() > 0.3 else None
        ))
    print(f"✅ {n} productos generados")


def generar_tickets(cursor, n=30000):
    metodos_pago = ["efectivo", "tarjeta", "transferencia", "bizum"]
    canales = ["tienda_fisica", "tienda_fisica", "tienda_fisica", "online", "telefono"]
    
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2025, 12, 31)
    rango_dias = (fecha_fin - fecha_inicio).days

    ticket_ids = []

    for _ in range(n):
        fecha = fecha_inicio + timedelta(days=random.randint(0, rango_dias))
        num_articulos = random.randint(1, 5)
        total = round(random.uniform(10, 500), 2)
        ganancia = round(total * random.uniform(0.2, 0.5), 2)

        cursor.execute("""
            INSERT INTO tickets (cliente_id, total, ganancia, fecha, 
                               numero_articulos, metodo_pago, canal,
                               terminal_id, operador_codigo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            random.randint(1, 200) if random.random() > 0.2 else None,
            total,
            ganancia,
            fecha,
            num_articulos,
            random.choice(metodos_pago),
            random.choice(canales),
            "TERMINAL_01",  
            fake.bothify(text="OP-###")  
        ))
        ticket_ids.append(cursor.lastrowid)

    print(f"✅ {n} tickets generados")
    return ticket_ids

def generar_ticket_productos(cursor, ticket_ids):
    for ticket_id in ticket_ids:
        num_productos = random.randint(1, 5)
        for _ in range(num_productos):
            precio_unitario = round(random.uniform(10, 200), 2)
            cantidad = random.randint(1, 3)
            total = round(precio_unitario * cantidad, 2)
            ganancia = round(total * random.uniform(0.2, 0.5), 2)
            
            cursor.execute("""
                INSERT INTO ticket_productos (ticket_id, producto_id, cantidad,
                                           precio_unitario, total, ganancia)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                ticket_id,
                random.randint(1, 400),
                cantidad,
                precio_unitario,
                total,
                ganancia
            ))
    print("✅ Ticket productos generados")


def generar_descuentos(cursor, ticket_ids):
    motivos = ["Promoción", "Cliente frecuente", "Temporada", "Cupón", "Error de precio"]
    tickets_con_descuento = random.sample(ticket_ids, int(len(ticket_ids) * 0.2))
    
    for ticket_id in tickets_con_descuento:
        cursor.execute("""
            INSERT INTO descuentos (ticket_id, porcentaje, motivo)
            VALUES (%s, %s, %s)
        """, (
            ticket_id,
            round(random.uniform(5, 50), 2),
            random.choice(motivos) if random.random() > 0.1 else None
        ))
    print(f"✅ {len(tickets_con_descuento)} descuentos generados")


def generar_devoluciones(cursor, ticket_ids):
    motivos = ["Talla incorrecta", "Defecto", "No convence", "Color diferente", "Regalo duplicado"]
    tickets_con_devolucion = random.sample(ticket_ids, int(len(ticket_ids) * 0.05))
    
    for ticket_id in tickets_con_devolucion:
        cursor.execute("""
            INSERT INTO devoluciones (ticket_id, producto_id, cantidad, fecha, motivo)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            ticket_id,
            random.randint(1, 400),
            random.randint(1, 3),
            fake.date_between(start_date="-3y", end_date="today"),
            random.choice(motivos) if random.random() > 0.1 else None
        ))
    print(f"✅ {len(tickets_con_devolucion)} devoluciones generadas")


def generar_movimientos(cursor, n=1000):
    descripciones = ["Entrada de stock", "Ajuste inventario", "Devolución proveedor", 
                    "Merma", "Transferencia entre tiendas"]
    
    for _ in range(n):
        cantidad_anterior = random.randint(0, 200)
        cantidad_movimiento = random.randint(-50, 100)
        
        cursor.execute("""
            INSERT INTO movimientos (producto_id, fecha, cantidad_anterior,
                                   cantidad_movimiento, descripcion,
                                   sistema_origen, hash_interno)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            random.randint(1, 400),
            fake.date_between(start_date="-3y", end_date="today"),
            cantidad_anterior,
            cantidad_movimiento,
            random.choice(descripciones) if random.random() > 0.15 else None,
            "POS_V1",  
            fake.sha256() if random.random() > 0.3 else None  
        ))
    print(f"✅ {n} movimientos generados")

def main():
    print("Iniciando generación de base de datos demo...")
    
    # CREAR BASE DE DATOS Y TABLAS
    crear_base_datos()
    
    # CONECTAR A LA BASE DE DATOS
    conn = conectar(DB_NAME)
    cursor = conn.cursor()
    
    try:
        # GENERAR DATOS EN ORDEN
        print("\n Generando datos...")
        generar_departamentos(cursor)
        conn.commit()
        
        generar_proveedores(cursor)
        conn.commit()
        
        generar_clientes(cursor)
        conn.commit()
        
        generar_productos(cursor)
        conn.commit()
        
        ticket_ids = generar_tickets(cursor)
        conn.commit()
        
        generar_ticket_productos(cursor, ticket_ids)
        conn.commit()
        
        generar_descuentos(cursor, ticket_ids)
        conn.commit()
        
        generar_devoluciones(cursor, ticket_ids)
        conn.commit()
        
        generar_movimientos(cursor)
        conn.commit()
        
        print("\n✅ Base de datos demo generada correctamente")
        print(f" Base de datos: {DB_NAME}")
        print(" Actualiza tu .env con DB_NAME=yvexiq_demo para usar la demo")

    except Exception as e:
        print(f" Error generando datos: {e}")
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()