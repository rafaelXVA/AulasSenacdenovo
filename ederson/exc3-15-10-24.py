import os
conceitoList=["A","B","C","D","E"]
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
if media>9 and media<=10:
    estado="APROVADO"
    conceito=conceitoList[0]
elif media<=9 and media>7.5:
    estado="APROVADO"
    conceito=conceitoList[1]
elif media>=6 and media<=7.5:
    estado="APROVADO"
    conceito=conceitoList[2]
elif media>4 and media<6:
    estado="REPROVADO"
    conceito=conceitoList[3]
elif media<=4 and media>=0:
    estado="REPROVADO"
    conceito=conceitoList[4]
print(f"O aluno está {estado} com as notas de conceito {conceito} com média {media}\nnota 1: {nota1}\nnota 2: {nota2}\nnota 3: {nota3}\nnota 4: {nota4}")