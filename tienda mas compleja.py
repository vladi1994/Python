import sqlite3

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self, db_name="tienda.db"):
        self.conexion = sqlite3.connect(db_name)
        self.crear_tabla()
    
    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY,
                nombre TEXT,
                precio REAL
            )
        ''')
        self.conexion.commit()

    def agregar_producto(self, producto):
        cursor = self.conexion.cursor()
        cursor.execute('INSERT INTO productos (nombre, precio) VALUES (?, ?)', (producto.nombre, producto.precio))
        self.conexion.commit()

    def obtener_productos(self):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM productos')
        return cursor.fetchall()

# Crear productos
producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 30)
producto3 = Producto("Zapatos", 50)

# Crear tienda
tienda = Tienda()

# Agregar productos al inventario y a la base de datos
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Obtener productos de la base de datos y mostrarlos
productos_en_tienda = tienda.obtener_productos()
for producto in productos_en_tienda:
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
