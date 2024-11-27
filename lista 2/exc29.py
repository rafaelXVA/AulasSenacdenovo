def intervalo_entre_elementos(lista):
    if not lista:
        return 0
    maior = max(lista)
    menor = min(lista)
    return maior - menor
lista = [10, 20, 5, 7, 30, 25]
resultado = intervalo_entre_elementos(lista)
print(resultado)
