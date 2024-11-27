def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 3, 7, 2, 8]
print(esta_ordenada(lista1))
print(esta_ordenada(lista2))
