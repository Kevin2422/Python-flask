local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__) #can use conditionals like these to prevent code from running unless the file is being run directly

if __name__ == "__main__":
    product = Product([args])
    print(product)
    print(product.add_tax(0.18))
# this tests out/prints out code if running directly from the doc. If you are importing this file and don't need to see this code, then this is a use case