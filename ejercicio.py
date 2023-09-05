class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("estudiando...")

nombre = input("ingresa el nombre : ")
edad = input("ingresa su edad: ")
grado = input("ingresa el grado : ")

estudiante = Estudiante(nombre,edad,grado)
print(f"""
        datos del estudiante :\n \n 
        Nombre : {estudiante.nombre}\n
        Edad: {estudiante.edad}\n
        Grado: {estudiante.grado}\n
    """)

while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        