'''import salario

print(salario.SalarioAumento(2000,3))
print(salario.SalarioDesconto(2000,3))'''

import math
import datetime
import os
import time

#x=2.6    //arredondar para o próximo número 1.2=>2//
#print(math.ceil(x))

#x=-54   //transformar em positivo//
#print(math.fabs(x))

#x=5   //fatoriar//
#print(math.factorial(x))

#x=5.9   //arredondar para o número anterior//
#print(math.floor(x))

#x=2
#y=10    //elevar o número(x=exponenciado//y=expoente)//
#print(math.pow(x,y))

#               //data atual e mudança de ordem//
#print(datetime.date.today().strftime('%d/%m/%y'))

#while True:      //tempo atual com milesegundos
#    print(datetime.datetime.now())
#    os.system("cls")

#while True:
#    print(datetime.datetime.now().strftime('%d/%m/%y %H:%M %S'))
#    os.system("cls")

a=0
time.perf_counter()
while a<10000:
    print(a)
    a+=1
y=time.perf_counter()
print(y-a)