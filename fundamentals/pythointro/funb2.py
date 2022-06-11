
def countdown(number):
    newList = []
    for x in range(number, -1,-1):
        newList.append(x)
    return newList

cd = countdown(5)
print(cd)

def print_and_return(num1, num2):
    print(num1)
    return(num2)

print_and_return(1,2)
x = print_and_return(1,2)
print(x)

def first_plus_length(numlist):
    sum = numlist[0] + len(numlist)
    print(sum)
    return sum

first_plus_length([1,2,3,4,5])


def values_greater_than_second(numlist):
    count = 0
    secList = []
    for x in range(0, len(numlist)):
        if numlist[x] > numlist[1]:
            count = count + 1
            
            secList.append(numlist[x])
            print(secList)
    print(count)
    return secList
            
        

values_greater_than_second([5,2,3,2,1,4])

def length_and_value(size, value):
    sizeV = []
    for x in range(0, size):
        sizeV.append(value)
        print(sizeV)
    

length_and_value(6,2)

