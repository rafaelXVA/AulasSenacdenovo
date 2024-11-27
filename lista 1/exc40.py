def mediana(lista):
    for i in range(0, len(lista)):
        for j in range(i, len(lista)):
            if(lista[i]> lista[j]):
                memoria = lista[j]
                lista[j] = lista[i]
                lista[i] = memoria
    size = len(lista)
    medialista = round(size/2)-1
    media = (lista[medialista]+lista[medialista+1])/2
    return media
lista = [10,9,8,7,6,5,4,3,2,1]
print(mediana(lista))