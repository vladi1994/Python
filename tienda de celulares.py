import sqlite3

class Celular:
    def __init__(self, marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.ram = ram
        self.procesador = procesador
        self.almacenamiento = almacenamiento
        self.camara_frontal = camara_frontal
        self.camara_trasera = camara_trasera
        self.es_5G = es_5G
        self.calidad_pantalla = calidad_pantalla

class TiendaCelulares:
    def __init__(self, db_name="tienda_celulares.db"):
        self.conexion = sqlite3.connect(db_name)
        self.crear_tabla()
    
    def crear_tabla(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS celulares (
                id INTEGER PRIMARY KEY,
                marca TEXT,
                modelo TEXT,
                precio REAL,
                ram INTEGER,
                procesador TEXT,
                almacenamiento TEXT,
                camara_frontal TEXT,
                camara_trasera TEXT,
                es_5G BOOLEAN,
                calidad_pantalla TEXT
            )
        ''')
        self.conexion.commit()

    def agregar_celular(self, celular):
        cursor = self.conexion.cursor()
        cursor.execute('INSERT INTO celulares (marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (celular.marca, celular.modelo, celular.precio, celular.ram, celular.procesador, celular.almacenamiento, celular.camara_frontal, celular.camara_trasera, celular.es_5G, celular.calidad_pantalla))
        self.conexion.commit()

    def obtener_celulares(self):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM celulares')
        return cursor.fetchall()

    def eliminar_celular(self, id_celular):
        cursor = self.conexion.cursor()
        cursor.execute('DELETE FROM celulares WHERE id = ?', (id_celular,))
        self.conexion.commit()

# Crear tienda de celulares
tienda_celulares = TiendaCelulares()

while True:
    print("===== MENÚ =====")
    print("1. Ver celulares")
    print("2. Agregar celular")
    print("3. Eliminar celular")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        celulares_en_tienda = tienda_celulares.obtener_celulares()
        for celular in celulares_en_tienda:
            print(f"ID: {celular[0]}, Marca: {celular[1]}, Modelo: {celular[2]}, Precio: {celular[3]}")
            print(f"RAM: {celular[4]} GB, Procesador: {celular[5]}, Almacenamiento: {celular[6]}, Cámara frontal: {celular[7]}, Cámara trasera: {celular[8]}, 5G: {celular[9]}, Calidad de pantalla: {celular[10]}")
    elif opcion == "2":
        marca = input("Ingrese la marca del celular: ")
        modelo = input("Ingrese el modelo del celular: ")
        precio = float(input("Ingrese el precio del celular: "))
        ram = int(input("Ingrese la capacidad de RAM (en GB): "))
        procesador = input("Ingrese el modelo del procesador: ")
        almacenamiento = input("Ingrese la capacidad de almacenamiento: ")
        camara_frontal = input("Ingrese la capacidad de la cámara frontal: ")
        camara_trasera = input("Ingrese la capacidad de la cámara trasera: ")
        es_5G = input("¿Es compatible con 5G? (Sí/No): ").lower() == "sí"
        calidad_pantalla = input("Ingrese la calidad de pantalla: ")
        nuevo_celular = Celular(marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla)
        tienda_celulares.agregar_celular(nuevo_celular)
        print("Celular agregado con éxito.")
    elif opcion == "3":
        id_celular = int(input("Ingrese el ID del celular a eliminar: "))
        tienda_celulares.eliminar_celular(id_celular)
        print("Celular eliminado con éxito.")
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
