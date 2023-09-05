class Persona:
    def __init__(self):
        pass
    
    def correr(self):
        print("L persona esta corriendo")
        
    def trabajar(self):
        print("La persona esta Trabajando")
        
class Estudiante(Persona):
    def __init__(self,nombre, apellido,edad,grado):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad= edad
        self.grado= grado

jorge = Estudiante("jorge","lopez",29,"5t0")

print(f"{jorge.nombre}")
jorge.correr()