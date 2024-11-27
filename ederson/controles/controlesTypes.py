from controleclass import *
import os

ControleQuarto=ControleRemoto('preto',30,3,6)
ControleSala=ControleRemoto('cinza',40,3,5)
ControleBanheiro=ControleRemoto('azul-claro',10,3,10)
ControleTelhado=ControleRemoto('branco',25,3,5)
ControlePorao=ControleRemoto('marrom',35,3,7)

while True:
    os.system('cls')
    inicio=input('ligar tv? (Y/N)')
    if inicio=='Y':
        os.system('cls')
        slc=int(input('qual controle?\n1-Quarto\n2-Sala\n3-Banheiro\n4-Telhado\n5-Porão'))
        if slc==1:
            os.system('cls')
            crtl=int(input('1-desligar\n2-volume'))
            if crtl==1:
                os.system('cls')
                ControleRemoto.ligar_tv('desligar')
                break
            else:
                os.system('cls')
                volume=input('+/-')
    elif inicio=='N':
        break
    else:
        print('valor invalido')
        continue