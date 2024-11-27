def conta_ocorrencias_recursiva(lista, elem):
    if not lista:
        return 0
    if lista[0] == elem:
        return 1 + conta_ocorrencias_recursiva(lista[1:], elem)
    else:
        return conta_ocorrencias_recursiva(lista[1:], elem)
lista = [1, 2, 3, 4, 2, 2, 10]
print(conta_ocorrencias_recursiva(lista, 2))