import os
from Menor import Menor
menor=Menor 
list=[]
os.system("cls")
while True:
    os.system("cls")
    test=int(input("insira uma série de números: "))
    list.append(test)
    if test==0:
        break
print(menor.Menor(list))