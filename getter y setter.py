class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self):
        del self.__nombre
    
    @nombre.deleter 
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
jorge = Persona("jorge",29)
nombre = jorge.nombre
print(nombre)

del jorge.nombre

jorge.nombre = "pepe"
nombre = jorge.nombre
print(nombre)