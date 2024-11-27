def conta_intervalo(lista, inicio, fim):
    contagem = 0
    for num in lista:
        if inicio <= num <= fim:
            contagem += 1
    return contagem
lista = [1, 3, 5, 7, 9, 11, 13, 15]
inicio = 5
fim = 10
resultado = conta_intervalo(lista, inicio, fim)
print(resultado)
