class Account:
    def __init__(self,number:int,holder:str,balance:float,code: int):
        self.number=number 
        self.holder=holder
        self.balance=balance
        self.code=code
    def withdraw(self,amount: float):
        if self.balance>=amount and amount>0:
            self.balance=self.balance-amount
            return self.balance
        else:
            if amount>self.balance:
                print("can't withdraw more than you have")
            else:
                print("you can't withdraw negative numbers")
    def deposit(self,amount:float):
        if amount>0:
            self.balance=self.balance+amount
            return self.balance
        else:
            print("you can't deposit negative numbers")
    def balanceVerify(self):
        print(f'your balance is {self.balance}')