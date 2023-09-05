#class Celular():
 #   marca = "Samsung"
  #  modelo = "S23"
   # camara = "48MP"
    
#Celular1 = Celular()
#print(Celular1.camara)

################################################################$
class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
            #se define los metodos
    def llamar(self):
        print(f'estas haciendo una llamda desde un : {self.modelo}')
        
    def cortar(self):
        print(f'cortaste la llamada desde un : {self.modelo}')
            
Celular1 = Celular("Samsung", "S23","48MP")
Celular2 = Celular("Iphone", "Iphone 15 pro","96MP")
print(Celular1.marca)
print(Celular2 .marca)
Celular1.cortar()
        
####################################################################