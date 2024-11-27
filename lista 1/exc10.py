test=int(input("insira um número: "))
for x in range (2,test//2):
    if test%x==0:
        print("número não primo")
    else:
        print("número primo")