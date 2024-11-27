def intercala_listas_ordenadas(lista1, lista2):
    resultado = []
    i, j = 0, 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    if i < len(lista1):
        resultado.extend(lista1[i:])
    if j < len(lista2):
        resultado.extend(lista2[j:])
    return resultado
lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
resultado = intercala_listas_ordenadas(lista1, lista2)
print(resultado)
