def lista_invertida(lista):
    invertida =[]
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida
        
lista = [1,2,3,4,5,6,7,8,9,10,11,12]
print(lista_invertida(lista))