currentNum = 100
tempTotal = 100;
total = 0
x = 0
while currentNum > 1 :
    tempTotal *= currentNum - 1
    currentNum -= 1
    print currentNum

tempTotal = str(tempTotal)
while x < len(tempTotal):
    total += int(tempTotal[x])
    x+=1

print total
