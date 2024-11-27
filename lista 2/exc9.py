def quick_sort(lista):
    pilha = []
    pilha.append((0, len(lista) - 1))
    while pilha:
        inicio, fim = pilha.pop()
        if inicio < fim:
            p = particionar(lista, inicio, fim)
            pilha.append((inicio, p - 1))
            pilha.append((p + 1, fim))
def particionar(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1 
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1
lista = [10, 7, 8, 9, 1, 5]
quick_sort(lista)
print(lista)
