def remove_multiplos(lista, n):
    return [x for x in lista if x % n != 0]
lista = [10, 15, 20, 25, 30, 35, 40]
resultado = remove_multiplos(lista, 5)
print(resultado)
