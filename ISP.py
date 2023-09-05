from abc import ABC, abstractclassmethod

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    @abstractclassmethod
    def comer(self):
        pass
    
    
class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass
    
class Humano(Trabajador):
    def comer(self):
        print("el humano esta comiendo")
        
    def trabajar(self):
        print("el humano esta trabajando")
         
    def dormir(self):
        print("el humano esta durmiendo")
        
class Robot(Trabajador):
    def trabajar(self):
        print("el humano esta trabajando")

robot = Robot()
robot.trabajar()