def soma(base, expoente):
    if(expoente == 0 ):
        return 1
    else:
        return base * soma(base, expoente-1)
print(soma(7,5))