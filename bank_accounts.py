class balanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName) -> None:
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(f"\nDeposit complite.\nAccount '{self.name}' balance = ${self.balance:.2f}")
        print(f"\nDeposit complite.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except balanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            
    def transfor(self, amount, account):
        try:
            print('\n***********\n\nBeginning Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!!\n\n**********")
        except balanceException as error:
            print(f"\nTransfer interrupted. X {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print(f"\nWitdraw completed.")
        except balanceException as erorr:
            print(f"\nWithdraw interrupted: {erorr}")