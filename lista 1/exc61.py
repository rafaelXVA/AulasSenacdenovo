def  pares(lista):
    lista2 = []
    for i in range(0, len(lista)):
        if lista[i] % 2 ==0:
            lista2.append(lista[i])
    return lista2
lista = [2,2,3,45,3,1,23,213,5,3,41,23,12,5,43,1]
print(pares(lista))