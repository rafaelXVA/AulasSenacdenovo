def inverte_dicionario(dic):
    novo_dic = {}
    for chave, valor in dic.items():
        novo_dic[valor] = chave
    return novo_dic
dic = {'a': 1, 'b': 2, 'c': 3}
print(inverte_dicionario(dic))