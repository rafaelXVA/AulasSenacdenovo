def soma(n):
    if(n<2):
        return 1
    else:
        return n + soma(n-1)
n = 13
print(soma(n))