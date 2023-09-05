altura = 5

for i in range(1, altura + 1):
    espacios = altura - i
    asteriscos = 2 * i - 1
    linea = ' ' * espacios + '*' * asteriscos
    print(linea)
    
    
# Este código utiliza un bucle for para iterar a través de cada nivel de la pirámide. 
# En cada nivel, calcula la cantidad de espacios en blanco y la cantidad de asteriscos necesarios para esa línea, y 
# luego imprime la línea con los espacios y los asteriscos correspondientes. 
# La salida será una pirámide de asteriscos con 5 niveles:

print("\n\n ")
print("priamide invertida")
print("\n\n ")
print("\n\n ")


for i in range(altura, 0, -1):
    espacios = altura - i
    asteriscos = 2 * i - 1
    linea = ' ' * espacios + '*' * asteriscos
    print(linea)


# En este código, utilizamos un bucle for para imprimir las capas del árbol, 
# y luego imprimimos el tronco del árbol después de completar el bucle. 
# El resultado será algo como esto:

for i in range(1, altura + 1):
    espacios = altura - i
    asteriscos = 2 * i - 1
    linea = ' ' * espacios + '*' * asteriscos
    print(linea)

tronco = ' ' * (altura - 1) + '|'
print(tronco)
