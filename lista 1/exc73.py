def filtro_dicionario(dic, valor):
    novo_dic = {}
    for chave, val in dic.items():
        if val > valor:  
            novo_dic[chave] = val  
    return novo_dic

dic = {'a': 10, 'b': 5, 'c': 20, 'd': 2}
valor = 6
print(filtro_dicionario(dic, valor))