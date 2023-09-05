class Animal:
    def comer():
        print("el animal esta comiendo")

class Ave(Animal):
    def volar(self):
        print("el animal esta volando...")
    
class Manifero(Animal):
    def amamantar(self):
        print("el animal esta amamantando...")     
        
class Murcielago(Manifero,Ave):
    pass

murcielago = Murcielago()
murcielago.volar()
murcielago.amamantar()
