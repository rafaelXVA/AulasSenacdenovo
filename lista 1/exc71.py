def conta_elementos(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1 
        else:
            contador[elemento] = 1
    return contador
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(conta_elementos(lista))