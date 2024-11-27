def ordena_por_valores(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1]))
dic = {'a': 10, 'b': 5, 'c': 20, 'd': 2}
print(ordena_por_valores(dic))