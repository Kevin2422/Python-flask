# declare a class and give it name User
class User:		
    def __init__(self):
        self.name = 'Bob'
        self.account_balance = 0
        

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name + ', Balance: $' + str(self.account_balance))
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self


guido = User()
monty = User()
john = User()

guido.name = "Guido"
guido.account_balance = 500
monty.name = "Monty"
monty.account_balance = 1500
john.name = "John"
john.account_balance = 2200


john.make_deposit(200).make_withdrawal(600).display_user_balance()




