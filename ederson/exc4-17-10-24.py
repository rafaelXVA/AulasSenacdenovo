import os
while True:
    nome=input("Nome: ")
    senha=str(input("Senha: "))
    os.system("cls")
    if nome!=senha:
        print("úsuario criado")
        break
    else:
        print("senha não pode ser o mesmo que o úsuario")
        continue