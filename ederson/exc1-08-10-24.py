import os
num1=int(input("num1: "))
num2=int(input("num2: "))
os.system("cls")
if num1>num2:
    print("num1 maior que num2\n",num1," > ",num2)
elif num2>num1:
    print("num2 maior que num1\n",num2,">",num1)
else:
    print("os números não podem ser iguais")