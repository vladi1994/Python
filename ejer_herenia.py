class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostar_datos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def mostar_grado(self):
        print(f"grado: {self.grado}")
        
estudiante = Estudiante("jorge","24","10mo")
estudiante.mostar_datos()