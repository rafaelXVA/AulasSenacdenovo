def separa_pares_impares(lista):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separa_pares_impares(lista)
print("Pares:", pares)
print("Ímpares:", impares)
