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
        print('Balance: $' + str(self.balance))
        return self

    def make_deposit(self, amount):
        self.balance += amount
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts: #can also be BankAccount.all_accounts                                 
            print( str(account.balance) + ' ' + str(account.int_rate))

    
        


account1 = BankAccount(.05, 500)
account2 = BankAccount(.04, 1000)

account1.make_deposit(200).make_deposit(400).make_deposit(500).make_withdrawal(1000).yield_interest().display_account_balance()
account2.make_deposit(1).make_deposit(55).make_withdrawal(5).make_withdrawal(5).make_withdrawal(40).make_withdrawal(40).yield_interest().display_account_balance()
print(BankAccount.all_accounts)

BankAccount.all_instances()