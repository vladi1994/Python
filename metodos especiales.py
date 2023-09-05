#funciones especiales con nombres reservados
class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    ##################metodo str
    #nos devuelve la representacion de un objeto en una cadena de texto
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    #reconstruir el objeto
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'
    
    
    # metodo especial ,: suma de objetos
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
jorge = Persona("jorge",28)
luis = Persona("luis",20)
eddy = Persona("eddy",21)

nueva_persona = jorge + luis + eddy

print(nueva_persona.edad)