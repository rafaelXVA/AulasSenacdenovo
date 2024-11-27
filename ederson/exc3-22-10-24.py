import os
produtos=[]
valores=[]
while True:
    os.system("cls")
    iniciar=int(input("1- inicar operação\n0- finalizar caixa\n"))
    if iniciar==1:
        while True:
            os.system("cls")
            produto=str(input("insira o produto: "))
            valor=float(input("insira o valor do produto: "))
            produtos.append(produto)
            valores.append(valor)
            end=int(input("0- finalizar\n1- outro produto\n"))
            if end==1:
                continue
            else:
                break
        total=sum(valores)
        while len(produtos)>0:
            print(f"{produtos[0]}            {valores[0]}")
            del produtos[0]
            del valores[0]
        print(f"\n          total: {total}")
        recebimento=float(input("\nvalor recebido: "))
        print(f"troco de {recebimento-total}")
        back=str(input("insira qualquer coisa para voltar\n"))
        if back=="1":
            continue
        else:
            continue
    else:
        break