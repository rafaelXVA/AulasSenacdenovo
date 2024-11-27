def cont(x):
    vogais = "aeiouAEIOU"
    contador = 0
    for i in x:
        if i not in vogais:
            contador += 1
    return contador
test=input("insira um texto: ")
print(cont(test))