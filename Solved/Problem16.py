number = 2 ** 1000
number = str(number)
x=0
total = 0
while x < len(number):
    total += int(number[x])
    x+=1
print total
