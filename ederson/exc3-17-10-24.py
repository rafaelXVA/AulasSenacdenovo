import os
while True:
    num=int(input("valor entre 0-10\n"))
    os.system("cls")
    if num>-1 and num<11:
        break
    else:
        print("valor inválido")
        continue