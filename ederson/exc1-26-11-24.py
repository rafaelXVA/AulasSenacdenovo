import os
class Conta():
    def __init__(self,saldo,cpf: str,nome,senha: str):
        self.__saldo=saldo
        self.__cpf=cpf
        self.nome=nome
        self.__senha=senha
    def extrato(self):
        senha=input('insira sua senha\n')
        if senha==self.__senha:
            print(f'nome: {self.nome}\ncpf: {self.__cpf}\nsaldo em conta: {self.__saldo}')
        else:
            print('senha inválida')
    def depositar(self,valor):
        self.__saldo +=valor
        return self.__saldo
    def sacar(self,valor):
        self.__saldo-=valor
        return self.__saldo
    def entrar(self):
        while True:
            senha=input('insira sua senha\n')
            if senha==self.__senha:
                os.system('cls')
                break
            else:
                print('senha inválida')
                os.system('pause')
                os.system('cls')
                continue
            
conta=Conta(0,87228294828,'Rafael','5')

Conta.entrar(conta)

while True:
    try:
        test=int(input('1-Extrato\n2-Deposito\n3-Saque\n0-Sair\n'))
        os.system('cls')
    except:
        print('apenas números')
        os.system('pause')
        os.system('cls')
        continue
    if test==1:
        Conta.extrato(conta)
        os.system('pause')
        os.system('cls')
    elif test==2:
        while True:
            try:    
                x=int(input('valor do deposito: '))
            except ValueError:
                print('apenas números')
                os.system('pause')
                os.system('cls')
                continue
            Conta.depositar(conta,x)
            print('deposito feito com sucesso!')
            os.system('pause')
            os.system('cls')
            break
    elif test==3:
       while True:
            try:    
                x=int(input('valor do saque: '))
            except ValueError:
                print('apenas números')
                os.system('pause')
                os.system('cls')
                continue
            Conta.sacar(conta,x)
            print('saque feito com sucesso!')
            os.system('pause')
            os.system('cls')
            break
    elif test==0:
        print('encerrado')
        break