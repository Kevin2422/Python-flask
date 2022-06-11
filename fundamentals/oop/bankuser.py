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
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self
    
class User:		
    def __init__(self,numberAccounts):
        self.name = 'name'
        self.Checking_account = BankAccount(.02, 0)
        self.Savings_account = BankAccount(.05,0)
        
        

    def make_withdrawal(self,amount, account_type):
        if account_type == 1:
            self.Checking_account.make_withdrawal(amount)
        elif account_type==2:
            self.Savings_account.make_withdrawal(amount)    
        return self

    def display_user_balance(self):
        
        
        print("user:" + self.name + " " + "Checking balance: " + str(self.Checking_account.display_account_balance()) + " " "Savings balance:" + str(self.Savings_account.display_account_balance()))
        
        
        

        return self

    def make_deposit(self, amount, account_type):
        if account_type == 1:
            self.Checking_account.make_deposit(amount)
        else:
            self.Savings_account.make_deposit(amount)    
        
        return self

john = User()
john.name = 'john'
john.make_withdrawal(600,2).make_deposit(800,1).make_withdrawal(100,1).display_user_balance().make_deposit(500,2).display_user_balance()

bobby = User()
bobby.name = 'bobby'
bobby.Savings_account.balance= 900
bobby.Checking_account.balance = 900
bobby.make_withdrawal(600,2).make_deposit(800,1).make_withdrawal(100,1).display_user_balance().make_deposit(500,2).display_user_balance()