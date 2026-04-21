from sqlalchemy import create_engine
url = 'mysql+pymysql://root:1234@localhost:3306/eleventa'
def conectar():
    engine = create_engine(url)
    return engine

try:
    engine = conectar()
    engine.connect()
    print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    