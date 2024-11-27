def  filtra_pares(lista):
    lista2 = []
    for i in range(0, len(lista)):
        if lista[i] % 2 ==0:
            lista2.append(lista[i])
    return lista2
lista = [0, 1,2,3,4,5,6,7,8,9,10]
print(filtra_pares(lista))