import sqlite3

class Celular:
    def __init__(self, marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla, anio_salida):
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
        self.anio_salida = anio_salida

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
                calidad_pantalla TEXT,
                anio_salida INTEGER
            )
        ''')
        self.conexion.commit()

    def agregar_celular(self, celular):
        cursor = self.conexion.cursor()
        cursor.execute('INSERT INTO celulares (marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla, anio_salida) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (celular.marca, celular.modelo, celular.precio, celular.ram, celular.procesador, celular.almacenamiento, celular.camara_frontal, celular.camara_trasera, celular.es_5G, celular.calidad_pantalla, celular.anio_salida))
        self.conexion.commit()

    def obtener_celulares(self, ordenar_por="precio"):
        cursor = self.conexion.cursor()
        cursor.execute(f'SELECT * FROM celulares ORDER BY {ordenar_por}')
        return cursor.fetchall()

    def obtener_celular_por_id(self, id_celular):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT * FROM celulares WHERE id = ?', (id_celular,))
        return cursor.fetchone()

    def editar_celular(self, id_celular, celular):
        cursor = self.conexion.cursor()
        cursor.execute('UPDATE celulares SET marca=?, modelo=?, precio=?, ram=?, procesador=?, almacenamiento=?, camara_frontal=?, camara_trasera=?, es_5G=?, calidad_pantalla=?, anio_salida=? WHERE id=?',
                       (celular.marca, celular.modelo, celular.precio, celular.ram, celular.procesador, celular.almacenamiento, celular.camara_frontal, celular.camara_trasera, celular.es_5G, celular.calidad_pantalla, celular.anio_salida, id_celular))
        self.conexion.commit()

    def eliminar_celular(self, id_celular):
        cursor = self.conexion.cursor()
        cursor.execute('DELETE FROM celulares WHERE id = ?', (id_celular,))
        self.conexion.commit()

# Crear tienda de celulares
tienda_celulares = TiendaCelulares()

while True:
    print("===== MENÚ =====")
    print("1. Ver celulares (ordenados por precio)")
    print("2. Ver celulares (ordenados por año)")
    print("3. Agregar celular")
    print("4. Editar celular")
    print("5. Eliminar celular")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        celulares_en_tienda = tienda_celulares.obtener_celulares(ordenar_por="precio")
        for celular in celulares_en_tienda:
            print(f"ID: {celular[0]}, Marca: {celular[1]}, Modelo: {celular[2]}, Precio: {celular[3]}")
            print(f"RAM: {celular[4]} GB, Procesador: {celular[5]}, Almacenamiento: {celular[6]}, Cámara frontal: {celular[7]}, Cámara trasera: {celular[8]}, 5G: {celular[9]}, Calidad de pantalla: {celular[10]}, Año de salida: {celular[11]}")
    elif opcion == "2":
        celulares_en_tienda = tienda_celulares.obtener_celulares(ordenar_por="anio_salida")
        for celular in celulares_en_tienda:
            print(f"ID: {celular[0]}, Marca: {celular[1]}, Modelo: {celular[2]}, Precio: {celular[3]}")
            print(f"RAM: {celular[4]} GB, Procesador: {celular[5]}, Almacenamiento: {celular[6]}, Cámara frontal: {celular[7]}, Cámara trasera: {celular[8]}, 5G: {celular[9]}, Calidad de pantalla: {celular[10]}, Año de salida: {celular[11]}")
    elif opcion == "3":
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
        anio_salida = int(input("Ingrese el año de salida: "))
        nuevo_celular = Celular(marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla, anio_salida)
        tienda_celulares.agregar_celular(nuevo_celular)
        print("Celular agregado con éxito.")
    elif opcion == "4":
        id_celular = int(input("Ingrese el ID del celular a editar: "))
        celular_actual = tienda_celulares.obtener_celular_por_id(id_celular)
        if celular_actual:
            marca = input(f"Marca actual: {celular_actual[1]}. Ingrese la nueva marca del celular: ")
            modelo = input(f"Modelo actual: {celular_actual[2]}. Ingrese el nuevo modelo del celular: ")
            precio = float(input(f"Precio actual: {celular_actual[3]}. Ingrese el nuevo precio del celular: "))
            ram = int(input(f"RAM actual: {celular_actual[4]} GB. Ingrese la nueva capacidad de RAM (en GB): "))
            procesador = input(f"Procesador actual: {celular_actual[5]}. Ingrese el nuevo modelo del procesador: ")
            almacenamiento = input(f"Almacenamiento actual: {celular_actual[6]}. Ingrese la nueva capacidad de almacenamiento: ")
            camara_frontal = input(f"Cámara frontal actual: {celular_actual[7]}. Ingrese la nueva capacidad de la cámara frontal: ")
            camara_trasera = input(f"Cámara trasera actual: {celular_actual[8]}. Ingrese la nueva capacidad de la cámara trasera: ")
            es_5G = input(f"¿Es compatible con 5G? (Sí/No) Actual: {'Sí' if celular_actual[9] else 'No'}. ").lower() == "sí"
            calidad_pantalla = input(f"Calidad de pantalla actual: {celular_actual[10]}. Ingrese la nueva calidad de pantalla: ")
            anio_salida = int(input(f"Año de salida actual: {celular_actual[11]}. Ingrese el nuevo año de salida: "))
            celular_editado = Celular(marca, modelo, precio, ram, procesador, almacenamiento, camara_frontal, camara_trasera, es_5G, calidad_pantalla, anio_salida)
            tienda_celulares.editar_celular(id_celular, celular_editado)
            print("Celular editado con éxito.")
        else:
            print("ID de celular no encontrado.")
    elif opcion == "5":
        id_celular = int(input("Ingrese el ID del celular a eliminar: "))
        tienda_celulares.eliminar_celular(id_celular)
        print("Celular eliminado con éxito.")
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
