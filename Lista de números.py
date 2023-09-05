# Lista de números
numeros = [5, 10, 15, 20, 25]

# Inicializar la suma de los números
suma = 0

# Calcular la suma de los números
for numero in numeros:
    suma += numero

# Calcular el promedio
promedio = suma / len(numeros)

# Imprimir el resultado
print(f"La lista de números es: {numeros}")
print(f"La suma de los números es: {suma}")
print(f"El promedio de los números es: {promedio}")
