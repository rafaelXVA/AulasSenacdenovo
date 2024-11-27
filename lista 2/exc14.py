import math

def desvio_padrao(lista):
    media = sum(lista) / len(lista)
    soma_dos_quadrados = sum((x - media) ** 2 for x in lista)
    desvio = math.sqrt(soma_dos_quadrados / len(lista))
    return desvio
lista = [10, 20, 30, 40, 50]
resultado = desvio_padrao(lista)
print(resultado)
