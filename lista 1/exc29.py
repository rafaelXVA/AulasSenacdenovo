import os
listX=[]
listY=[]
def intersecao_listas(listX, listY):
    intersecao = []
    for i in range(0,len(listX)):
        for j in range(0,len(listY)):
            if listX[i] == listY[j]:
                intersecao.append(listX[i])
    return intersecao
while True:
    x=int(input("insira número para lista 1: "))
    listX.append(x)
    os.system("cls")
    if x==0:
        break
while True:
    y=int(input("insira números para lista 2: "))
    listY.append(y)
    os.system("cls")
    if y==0:
        break
print(intersecao_listas(listX,listY))