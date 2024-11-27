from MotherClass import *

class BussinerAccount(Account):
    def __init__(self, number:int, holder:str, balance:float,code:int,loanLimit:float):
        super().__init__(number, holder, balance, code)
        self.loanLimit=loanLimit
    def loan(self,amount):
        if self.loanLimit>=amount and amount>0:
            self.balance=self.balance+amount
            self.loanLimit=self.loanLimit-amount
            return self.balance,self.loanLimit
        else:
            if self.loanLimit>=amount:
                print("you don't have such limit fot that loan")
            else:
                print("you can't loan negative numbers")