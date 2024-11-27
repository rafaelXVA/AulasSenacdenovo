def busca_binaria(lista, elemento):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
resultado = busca_binaria(lista, 7)
print(resultado)
resultado_inexistente = busca_binaria(lista, 8)
print(resultado_inexistente)
