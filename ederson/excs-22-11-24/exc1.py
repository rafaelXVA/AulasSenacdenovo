from Classes import Bola
import os


bola1=Bola('preta',10,'plastico')
while True:
    test=int(input('1-mostrar cor\n2-trocar cor\n3-encerrar\n'))
    if test==1:
        os.system('cls')
        Bola.mostra_cor(bola1)
        continue
    elif test==2:
        test=input('nova cor: ')
        test=Bola.troca_cor(bola1,test)
    else:
        break