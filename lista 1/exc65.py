def dec2bin(n):
    if n == 0:
        return "0" 
    binario = ""
    while n > 0:
        resto = n % 2 
        binario = str(resto) + binario  
        n = n // 2  
    return binario

# Exemplo de uso
numero = 2
print(dec2bin(numero))