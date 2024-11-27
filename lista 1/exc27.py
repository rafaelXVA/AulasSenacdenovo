import os
list=[]
def n_solo(list):
    solo = []
    for n in list:
        if list.count(n) == 1:
            solo.append(n)
    return solo

while True:
    x=int(input("insira números: "))
    list.append(x)
    os.system("cls")
    if x==0:
        break
print(n_solo(list))