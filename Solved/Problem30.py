x = 2
total = 0
tempTotal = 0

while x < 1000000:
    for y in str(x):
        tempTotal += int(y) ** 5
    if x == tempTotal:
        total+=tempTotal
        print tempTotal
    tempTotal = 0
    x += 1
print total 
