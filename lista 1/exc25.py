import os
list=[]
def remove_duplicados(list):
    listR = []
    for x in list:
        if x not in listR:
            listR.append(x)
    return listR
        
while True:
    x=int(input("insira números: "))
    os.system("cls")
    list.append(x)
    if x==0:
        break
print(remove_duplicados(list))