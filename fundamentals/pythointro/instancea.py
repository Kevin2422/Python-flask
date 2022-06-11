class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self , name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python



User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty



guido = User()
monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union 
print(monty.bank_name) # output: First National Dojo

