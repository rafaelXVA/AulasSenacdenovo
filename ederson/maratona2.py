list2=[]
cont=0
import os
list=[]
while True:
    os.system("cls")
    n=int(input("0 para finalizar\ninsira um número: "))
    if n==0:
        break
    list.append(n)
    cont=cont+1
media=sum(list)/cont
print(media)
for i in list:
    n=(i-media)**2
    list2.append(n)
dp=(sum(list2)/cont)**0.5
print(f"dp={dp:.4f}")