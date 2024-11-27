import os
os.system("cls")
nota1=float(input("insira a primeira nota\n"))
os.system("cls")
nota2=float(input("insira a segunda nota\n"))
os.system("cls")
nota3=float(input("insira a terceira nota\n"))
os.system("cls")
nota4=float(input("insira a quarta nota\n"))
os.system("cls")
media=(nota1+nota2+nota3+nota4)/4

if media<7 and media>-1:   #reprovado
    print(f"O aluno está reprovado\nmédia de {media}")

elif media>7 and media<10: #aprovado
    print(f"O aluno está aprovado\nmédia de {media}")

elif media==10: #aprovado com distinção
    print(f"O aluno está aprovado com distinção\nmédia de {media}")