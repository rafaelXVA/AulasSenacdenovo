test=str(input("insira uma palavra: "))
inverse=test[::-1]
if inverse==test:
    print("é um palindromo")
else:
    print("não é um palindromo")