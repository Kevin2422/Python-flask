num1 = 42 # variable dec number
num2 = 2.3  # variable dec  number
boolean = True #var dec boolean
string = 'Hello World' # var dec string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # var dec list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # var dec dictionary
fruit = ('blueberry', 'strawberry', 'banana') # var dec tuple
print(type(fruit)) # type check
print(pizza_toppings[1]) #access value list
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #acces value John
person['name'] = 'George' # change value
person['eye_color'] = 'blue' # add value
print(fruit[2]) #access value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
    #if statement, prints it's lower

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    # length check of string, prints just right

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)