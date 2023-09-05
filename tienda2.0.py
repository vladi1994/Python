'''''¡Por supuesto! Puedes agregar un sistema de menú para que el usuario pueda elegir entre ver, agregar o eliminar productos. 
Aquí tienes una versión actualizada del código que incluye estas opciones:'''''

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

    def eliminar_producto(self, id_producto):
        cursor = self.conexion.cursor()
        cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
        self.conexion.commit()

# Crear tienda
tienda = Tienda()

while True:
    print("===== MENÚ =====")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        productos_en_tienda = tienda.obtener_productos()
        for producto in productos_en_tienda:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        nuevo_producto = Producto(nombre, precio)
        tienda.agregar_producto(nuevo_producto)
        print("Producto agregado con éxito.")
    elif opcion == "3":
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        tienda.eliminar_producto(id_producto)
        print("Producto eliminado con éxito.")
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
