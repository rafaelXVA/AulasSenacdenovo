def soma_diagonais(matriz):
    n = len(matriz)
    soma = 0

    for i in range(n):
        soma += matriz[i][i]
        
        soma += matriz[i][n - i - 1]

    
    if n % 2 != 0:
        soma -= matriz[n // 2][n // 2]

    return soma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(soma_diagonais(matriz))  