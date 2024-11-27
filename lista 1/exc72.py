def merge_dicionarios(d1, d2):
    resultado = d1.copy() 
    for chave, valor in d2.items():
        if chave in resultado:
            resultado[chave] += valor  
        else:
            resultado[chave] = valor  
    return resultado
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicionarios(d1, d2))