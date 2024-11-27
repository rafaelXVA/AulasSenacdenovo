def diferenca_elementos_lista(lista):
    diferencas = []
    for i in range(len(lista) - 1):
        diferenca = abs(lista[i] - lista[i + 1])
        diferencas.append(diferenca)
    return diferencas

lista = [10, 5, 20, 15, 30]
resultado = diferenca_elementos_lista(lista)
print(resultado)

