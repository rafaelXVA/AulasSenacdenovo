def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    return lista

print(selection_sort([2,3,5,3,2,5]))