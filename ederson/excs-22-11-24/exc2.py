from Classes import Quadrado
import os

quadrado1=Quadrado(10)

while True:
    test=int(input('1-mostrar area\n2-mudar valor lado\n3-encerrar\n'))
    if test==1:
        Quadrado.mostrar_area(quadrado1)
    elif test==2:
        test=int(input('tamanho do lado? '))
        test=Quadrado.mudar_lado(quadrado1,test)
    else:
        break