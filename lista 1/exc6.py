import os
list=[]
os.system("cls")
while True:
    test=int(input("0 para finalizar o programa\ninsira um números:"))
    list.append(test)
    os.system("cls")
    if test==0:
        print(f"a soma total foi de {sum(list)}")
        break