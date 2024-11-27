def diferenca_max_min(lista):
    if not lista:
        return 0
    maior = max(lista)
    menor = min(lista)
    return maior - menor

lista = [3, 6, 8, 10, 1, 2, 1]
resultado = diferenca_max_min(lista)
print(resultado)

