def diagonais_matriz(matriz):
    n = len(matriz)
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(n):
        diagonal_principal.append(matriz[i][i])  
        diagonal_secundaria.append(matriz[i][n - i - 1]) 
    return diagonal_principal + diagonal_secundaria
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
resultado = diagonais_matriz(matriz)
print(resultado)

