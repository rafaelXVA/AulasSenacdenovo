def armstrongN(n):
    list = []
    size = len(str(n))
    case = str(n)
    for i in range(0, size):
        list.append(int(case[i])**size) 
    if sum(list) == n:
        return 'é um número de armstrong'
    else:
        return 'não é um número de armstrong'
print(armstrongN(1634))