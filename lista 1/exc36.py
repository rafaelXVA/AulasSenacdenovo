def eh_perfeito(n):
    lista_de_divisores = []
    for i in range(1, n):
        if(n%i==0):
            lista_de_divisores.append(i)
    
    if(n == sum(lista_de_divisores)):
        return 'é um número perfeito'
    else:
        return 'não é um número perfeito'
    
print(eh_perfeito(496))