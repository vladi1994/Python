from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    def presentarse(self):
        print("********************************************")
        print(f"Hola, me llamo : {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad,grado):
        super().__init__(nombre, edad, sexo, actividad)
        self.grado = grado
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")   
        print(f"Y estoy en el grado : {self.grado}")
        print("********************************************\n\n")   
        
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad,salario):
        super().__init__(nombre, edad, sexo, actividad)
        self.salario = salario
        
    def hacer_actividad(self):
        print(f"Actualmente estoy en el rubro de : {self.actividad}")
        print(f"Y mi sueldo es : {self.salario}")
        print("********************************************\n\n")   

# Solicitar datos para un estudiante
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
edad_estudiante = int(input("Ingrese la edad del estudiante: "))
sexo_estudiante = input("Ingrese el sexo del estudiante: ")
actividad_estudiante = input("Ingrese la actividad del estudiante: ")
grado_estudiante = input("Ingrese el grado que cursa:")

# Crear una instancia de Estudiante con los datos ingresados

nuevo_estudiante = Estudiante(nombre_estudiante, edad_estudiante, sexo_estudiante, actividad_estudiante,grado_estudiante)

# Solicitar datos para un trabajador
nombre_trabajador = input("Ingrese el nombre del trabajador: ")
edad_trabajador = int(input("Ingrese la edad del trabajador: "))
sexo_trabajador = input("Ingrese el sexo del trabajador: ")
actividad_trabajador = input("Ingrese la actividad del trabajador: ")
salario = float(input("Ingrese el salario :"))

# Crear una instancia de Trabajador con los datos ingresados
nuevo_trabajador = Trabajador(nombre_trabajador, edad_trabajador, sexo_trabajador, actividad_trabajador,salario)

# Mostrar la información de las instancias creadas
print("\nInformación del estudiante:")
nuevo_estudiante.presentarse()
nuevo_estudiante.hacer_actividad()

print("\nInformación del trabajador:")
nuevo_trabajador.presentarse()
nuevo_trabajador.hacer_actividad()
