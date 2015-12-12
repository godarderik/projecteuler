num = "1"
addNum = 2
timesNum = 1
total = 1
while addNum <= 1000000:
    num += str(addNum)
    addNum += 1
print num
while timesNum <= 1000000:
    print num[timesNum  - 1]
    total *= int(num[timesNum - 1])
    timesNum *= 10
print total 
