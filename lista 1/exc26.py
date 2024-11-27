import os
list=[]
def soma_pares(list):
    listR = []
    listR2 = []
    for x in list:
        if x not in listR:
            listR.append(x)
        else:
            listR2.append(x)
    return sum(listR2)
while True:
    x=int(input("insira números: "))
    list.append(x)
    os.system("cls")
    if x==0:
        break
print(soma_pares(list))