from BancoClass import *
saldo=0

while True:
    test=input("sacar ou depositar?\n")
    if test=='sacar':
        sacado=int(input('valor do saque\n'))
        saldo=Banco.sacar(saldo,sacado)
        print(f'seu saldo é {saldo}')
        continue
    if test=='depositar':
        deposito=int(input('valor do deposito\n'))
        saldo=Banco.deposito(saldo,deposito)
        print(f'seu saldo é {saldo}')
        continue