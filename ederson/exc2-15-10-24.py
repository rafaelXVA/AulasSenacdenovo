import os
os.system("cls")
salario=float(input("insira o salário\n"))
os.system("cls")
if salario>0 and salario<=280:
    porcentagem=salario*20/100
    salarioNew=salario+porcentagem
    print("salário antigo: ",salario,"\nquantidade aumentada: ",porcentagem,"\nnovo salário: ",salarioNew,"\naumento de 20%")
elif salario>280 and salario<700:
    porcentagem=salario*15/100
    salarioNew=salario+porcentagem
    print("salário antigo: ",salario,"\nquantidade aumentada: ",porcentagem,"\nnovo salário: ",salarioNew,"\naumento de 15%")
elif salario>=700 and salario<1500:
    porcentagem=salario*10/100
    salarioNew=salario+porcentagem
    print("salário antigo: ",salario,"\nquantidade aumentada: ",porcentagem,"\nnovo salário: ",salarioNew,"\naumento de 10%")
elif salario>=1500:
    porcentagem=salario*5/100
    salarioNew=salario+porcentagem
    print("salário antigo: ",salario,"\nquantidade aumentada: ",porcentagem,"\nnovo salário: ",salarioNew,"\naumento de 5%")