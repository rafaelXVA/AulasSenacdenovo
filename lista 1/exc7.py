import os
list=[]
os.system("cls")
while True:
    letter=str(input('insira "fechar" para finalizar\ninsira uma letra: '))
    list.append(letter)
    print(list)
    os.system("cls")
    if letter=='fechar':
        vogals=list.count("a")
        vogals2=list.count("e")
        vogals3=list.count("i")
        vogals4=list.count("o")
        vogals5=list.count("u")
        print(f"Você inseriu {vogals+vogals2+vogals3+vogals4+vogals5} vogais")
        break