
import os
while True:
    nome=input("Insira um nome: ")
    idade=int(input("Insira uma idade: "))
    salario=float(input("Insira um salário: "))
    sexo=input("Insira uma sexo entre\nF-feminino\nM-masculino\nO-outro\n")
    estadoC=input("Insira um estado civil entre\nS-solteiro\nC-casado\nV-viúvo\nD-divorciado\n")
    list={nome,idade,salario,sexo,estadoC}
    back=input("Está tudo correto? S/N\n")
    if back=="S":
        break
    else:
        os.system("cls")
        continue

while len(list[0])<4: 
    print("nome inválido, insira um nome com mais de 3 caracters")
    nome=input("nome: ")
while list[1]<0 or list[1]>150:
    idade=int("idade inválida, insira uma idade menor que 150 e maior que 0\nidade: ")
while list[2]<0:
    salario=float(input("salário inválido, insira um salário maior que 0\nsalário: "))