import os
list=[]
def conta_ocorrencia(lista, elemento):
    cont = 0
    for i in range (0, len(lista)):
        if(lista[i] == elemento):
            cont = cont+1
        
    return cont
while True:
    x=int(input("insira 0 para finalizar\ninsira números:"))
    os.system("cls")
    list.append(x)
    if x==0:
        break
res=int(input("insira um número para saber quantas vezes ele se repitiu: "))
print(conta_ocorrencia(list,res))
