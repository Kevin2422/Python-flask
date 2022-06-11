class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the spec
    

guido = User('guido', 'email')
guido.account_balance = 500

guido.make_deposit(100)
guido.make_deposit(200)

print(guido.account_balance)	# output: 300
	# output: 50

