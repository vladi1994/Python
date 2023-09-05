def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for num in arr[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)

numeros = [7, 2, 1, 6, 8, 5, 3, 4]
numeros_ordenados = quicksort(numeros)
print(numeros_ordenados)



# QuickSort es un algoritmo de ordenación eficiente que utiliza una estrategia de divide y
# vencerás para ordenar una lista de elementos. Aquí tienes una implementación paso a paso:

# Supongamos que tenemos una lista desordenada de números:
#numeros = [7, 2, 1, 6, 8, 5, 3, 4]
