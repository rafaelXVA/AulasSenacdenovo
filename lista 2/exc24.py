import math

def numeros_primos(n):
    primos = []
    def is_primo(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    for i in range(2, n + 1):
        if is_primo(i):
            primos.append(i)
    return primos
n = 30
resultado = numeros_primos(n)
print(resultado)
