from CalculadoraClass import Calculadora as C
c=C
x=input("somar ou subtrair?\n")
if x=='somar':
    n1=int(input("numero 1: "))
    n2=int(input("numero 2: "))
    res=c.somar(n1,n2)
    print(res)
else:
    n1=int(input("numero 1: "))
    n2=int(input("numero 2: "))
    res=c.subtrair(n1,n2)
    print(res)