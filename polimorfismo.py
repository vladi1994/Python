#polimorfismo con herencia

class Animal():
    def sonido(self):
        pass
    
class Gato(Animal):
    def sonido(self):
        return("Miau")
        
class Perro(Animal):
    def sonido(self):
        return("Guau")
        
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(perro)