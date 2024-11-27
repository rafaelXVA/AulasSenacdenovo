import os
os.system("cls")
sele=0
try:
    sele=int(input('1- adição\n2- subtração\n3- multiplicação\n4- divisão\n\nselecione a operação digitando\nseu número: '))
    os.system("cls")
except ValueError:
    print("digite apenas números\nfim do programa")
except:
    print("erro desconhecido\nfim do programa")
if sele==1:
    try:
        n1=int(input("número para ser somado: "))
        n2=int(input("número para somar: "))
        res=n1+n2
        print("resposta: ",res)
    except ValueError:
        print("digite apenas números\nfim do programa")
    except:
        print("erro desconhecido\nfim do programa")
elif sele==2:
    try:
        n1=int(input("número para ser subtraído: "))
        n2=int(input("número para subtrair: "))
        res=n1-n2
        print("resposta: ",res)
    except ValueError:
        print("digite apenas números\nfim do programa")
    except:
        print("erro desconhecido\nfim do programa")
if sele==3:
    try:
        n1=int(input("número para ser multiplicado: "))
        n2=int(input("multiplicar número por: "))
        res=n1*n2
        print("resposta: ",res)
    except ValueError:
        print("digite apenas números\nfim do programa")
    except:
        print("erro desconhecido\nfim do programa")
if sele==4:
    try:
        n1=int(input("número para ser dividido: "))
        n2=int(input("dividir número por: "))
        res=n1/n2
        print("resposta: ",res)
    except ValueError:
        print("digite apenas números\nfim do programa")
    except ZeroDivisionError:
        print("não divida o números por zero\nfim do programa")
    except:
        print("erro desconhecido\nfim do programa")
        