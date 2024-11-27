def multiplica_pares(lista):
    produto = 1
    encontrou_par = False
    for num in lista:
        if num % 2 == 0:
            produto *= num
            encontrou_par = True
    if not encontrou_par:
        return 1
    return produto
lista = [2, 3, 4, 5, 6]
resultado = multiplica_pares(lista)
print(resultado)
