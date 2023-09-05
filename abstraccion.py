class Auto:
    def __init__(self,):
        self.__estado = "apagado"
    
    def encender(self):
        self.__estado = "encendido"
        print("el auto esta encendido")
        
    def conducir(self):
        if self.__estado == "apagado":
            self.encender()
        print("conduciendo el auto")
        
mi_auto= Auto()
mi_auto.conducir()