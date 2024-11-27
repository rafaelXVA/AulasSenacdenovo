num=int(input("número\n"))
cont=0
while True:
    print(num)
    cont=cont+1 #contar quantas vezes entrou no laço
    num=num-1
    if num==0:
        break
print(f"o número foi diminuido {cont} vezes")