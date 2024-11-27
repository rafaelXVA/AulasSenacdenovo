from BussinerAccount import *
from MotherClass import *
import os

account=BussinerAccount(5624,'rafael',10,2,1000)

while True:
    try:
        test=int(input('1-withdraw\n2-deposit\n3-balance\n4-loan\n0-exit\n'))
        os.system('cls')
    except ValueError:
        os.system('cls')
        print('only numbers')
        continue
    if test==1:
        while True:
            try:
                amount=float(input('amount to withdraw: '))
                os.system('cls')
                Account.withdraw(account,amount)
                print(f'your new balance is {account.balance}')
                os.system('pause')
                os.system('cls')
                break
            except ValueError:
                print('only numbers')
                os.system('pause')
                os.system('cls')
                continue
    elif test==2:
        while True:
            try:
                amount=float(input('amount to deposit: '))
                os.system('cls')
                Account.deposit(account,amount)
                print(f'your new balance is {account.balance}')
                os.system('pause')
                os.system('cls')
                break
            except ValueError:
                print('only numbers')
                os.system('pause')
                os.system('cls')
                continue
    elif test==3:
        Account.balance(account)
        os.system('pause')
        os.system('cls')
    elif test==4:
        while True:   
            if account.code==2:
                try:
                    amount=float(input('amount of the loan: '))
                    os.system('cls')
                    BussinerAccount.loan(account,amount)
                    print(f'yout new balance is {account.balance}')
                    os.system('pause')
                    os.system('cls')
                    break
                except ValueError:
                    print('only numbers')
            else:
                print("you are not a bussiner account")
                os.system('pause')
                os.system('cls')
                break
    else:
        print('end')
        break