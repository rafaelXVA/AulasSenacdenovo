def soma_recursiva(n):
    if(n<2):
        return 1
    else:
        return n + soma_recursiva(n-1)
n = 10
print(soma_recursiva(n))