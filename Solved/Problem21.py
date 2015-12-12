from math import sqrt

total = 0
a = 1
b = 0

def getDivisors(num):
    x = 1
    divisorSum = 0
    while x <= num/2:
        if (num % x) == 0:
            divisorSum+=x
        x += 1
    return divisorSum
while a < 10000:
    b = getDivisors(a)
    if a == getDivisors(b) and a<>b:
        total += a
    a +=1
    
    if (a % 100) == 0:
        print a
print total
