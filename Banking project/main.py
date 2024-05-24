import random
class Account:
    def __init__(self, balance = 0, accountNumber = -1):# this a constructor
        self.balance = balance
        
        if accountNumber == -1:
            accountNumber = random.randint(10000000,99999999)
        self.accountNumber = accountNumber
        self.transLog = []
        self.balance = balance
    def getAccountNumber(self):
        return self.accountNumber
    def getBalance(self):
        return self.balance
    def getTransactions(self):
        return self.transaction
    def Deposit(self,deposit_amount):
        self.balance = self.balance +deposit_amount
        print('Deposite is made and amount is ' + str(self.balance))
    def Withdraw(self,withdraw_amount):
        if self.balance < withdraw_amount:
            raise ValueError('sorry not enough balance')
        else:
            self.balance = self.balance - withdraw_amount
        print('withdraw is made and amount is ' + str(self.balance) )
    def addTransaction(self):
        return self.transaction

class User(Account):
    def __init__(self,name,balance,accountNumber):#this is constructor
        super().__init__(balance,accountNumber)
        self.name = name
        self.createPin()
        
    def createPin(self):
        self.pin = random.randint(1000,9999)
    def getName(self):
        return self.name
    def getPin(self):
        return self.pin
    
class ATM():
    def __init__(self):
        self.accounts = []
        f = open("accounts.txt", "r")
        x = 1
        for each in f.readlines():
            print(each.strip())
            self.accounts.append(User(each.strip(),100,x))
            x = x + 1

a = ATM()
print(a.accounts)

