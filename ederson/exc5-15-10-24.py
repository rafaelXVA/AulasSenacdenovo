import os
gas=2.5
alc=1.9
os.system("cls")
pergunta=input("digite G para gasolina ou A para álcool\n")
os.system("cls")
if pergunta.upper()=="G":
    quant=float(input("quantidade de gasolina?\n"))
    os.system("cls")
    if quant>20:
        price=(quant*gas)
        porcentagem=price*6/100
        valor=price-porcentagem
        print(f"você abasteceu um total de {quant} dando o valor total de {valor}")
    else:
        price=(quant*gas)/(4/100)
        print(f"você abasteceu um total de {quant} dando o valor total de {price}")
if pergunta.upper=="A":
    quant=float(input("quantidade de álcool?\n"))
    os.system("cls")
    if quant>20:
        price=(quant*alc)/(5/100)
        print(f"você abasteceu um total de {quant} dando o valor total de {price}")
    else:
        price=(quant*alc)/(3/100)
        print(f"você abasteceu um total de {quant} dando o valor total de {price}")