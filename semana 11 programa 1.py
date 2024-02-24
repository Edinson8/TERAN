def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == valor:
                return f"El valor {valor} se encontró en la posición ({i}, {j})."
    return f"El valor {valor} no se encontró en la matriz."
# Definir una matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Valor a buscar
valor_a_buscar = 5
# Llamar a la función buscar_valor
resultado_busqueda = buscar_valor(matriz, valor_a_buscar)
# Mostrar el resultado de la búsqueda
print(resultado_busqueda)