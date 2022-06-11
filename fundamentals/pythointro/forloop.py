for x in range(0, 151):
    print(x)

for y in range(0, 1005, 5):
    print(y)

for a in range(1, 101):
    if a % 10 == 0:
        print("Coding Dojo")
    elif a % 5 == 0:
        print("Coding")
    else:
        print(a)

sum = 0
for b in range(1, 500000, 2):
    sum = sum + b

print(sum)

for c in range(2018, 0, -4):
    print(c)

lowNum = 2
highNum = 9
mult = 3

for d in range(lowNum, highNum+1):
    if d%mult == 0:
        print(d)
