class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def display_account_balance(self):
        
        return self.balance
        

    def make_deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self
    
class User:		
    def __init__(self,numberAccounts):
        self.name = 'name'
        for x in range(1, numberAccounts+1):
            setattr(self, f'account{x}', BankAccount(0,0)  )
    
    def make_deposit(self, amount, accountnum):
        balance = getattr(self, f'account{accountnum}')
        balance = balance.balance
        print(balance)

        balance = balance+amount
        print(balance)
        setattr(self,f'account{accountnum}', BankAccount(0,balance))
        print(self.account2)
        
        
        
john = User(3)
john.make_deposit(500,3)
print(john.account3.balance)