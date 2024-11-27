def verificar_ano_bissexto(ano):
    ano = str(ano)
    digito=''
    for i in range(0, len(ano)):
        if(i == len(ano)-1 or i == len(ano)-2):
            digito += ano[i]
    digito = int(digito)
    ano = int(ano)
    
    if(ano %100 ==0 and ano%400 ==0):
        return 'é bissexto'
    else:
        if(digito == 00 ):
            return 'não é bissexto'
        elif(digito%4==0):
            return 'é bissexto'
        else:
            return 'não é bissexto'
print(verificar_ano_bissexto(1600))