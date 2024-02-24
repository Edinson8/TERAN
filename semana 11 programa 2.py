def ordenar_fila(matriz, fila):
    fila_ordenada = sorted(matriz[fila])
    matriz[fila] = fila_ordenada
# Definir una matriz de ejemplo
matriz = [
    [9, 2, 3],
    [4, 5, 1],
    [7, 8, 6]
]
# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)
# Fila a ordenar (se asume que la fila es válida)
fila_a_ordenar = 1
# Llamar a la función para ordenar la fila especificada
ordenar_fila(matriz, fila_a_ordenar)
# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)