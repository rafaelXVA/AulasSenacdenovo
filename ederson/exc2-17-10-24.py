import os
os.system("cls")
while True:
    num=0
    num2=0
    print(" ",23*"_")
    print("  |Selecione a operação |\n  |1-adição             |\n  |2-subtração          |\n  |3-multiplicação      |\n  |4-divisão            |\n ",23*"¯"+"\n\nInsira qualquer coisa que não seja uma opção para sair")
    select=int(input())
    os.system("cls")
    if select==1:
        num=int(input("insira um número: "))
        num2=int(input("insira um número para adicionar: "))
        res=num+num2
        os.system("cls")
        print(f"sua resposta é {res}")
        back=str(input("insira algo para pular\n"))
        os.system("cls")
        if back==0:
            continue
        else:
            continue
    if select==2:
        print(" ",23*"_")
        num=int(input("  |insira um número: "))
        num2=int(input("  |insira um número para diminuir: "))
        res=num-num2
        os.system("cls")
        print(f"sua resposta é {res}")
        back=str(input("insira algo para pular\n"))
        os.system("cls")
        if back==0:
            continue
        else:
            continue
    if select==3:
        num=int(input("insira um número: "))
        num2=int(input("insira um número para multiplicar "))
        res=num*num2
        os.system("cls")
        print(f"sua resposta é {res}")
        back=str(input("insira algo para pular\n"))
        os.system("cls")
        if back==0:
            continue
        else:
            continue
    if select==4:
        num=int(input("insira um número: "))
        num2=int(input("insira um número para dividir"))
        res=num/num2
        os.system("cls")
        print(f"sua resposta é {res}")
        back=str(input("insira algo para pular\n"))
        os.system("cls")
        if back==0:
            continue
        else:
            continue
    else:
        break