import os
texto=str(input("Escreva um texto\n"))
os.system("cls")
print(texto+"\nA quantidade de letras no texto é de ", end="")
print(len(texto))