class Personaje:
    def __init__(self,nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self,otropj):
        nuevo_nombre = self.nombre + "-" + otropj.nombre
        nueva_fuerza = ((self.fuerza + otropj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otropj.velocidad)/2)**2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku = Personaje("Goku",100,150)
vegeta = Personaje("Vegeta",99,100)
    
gogeta = goku + vegeta
print(gogeta)
        