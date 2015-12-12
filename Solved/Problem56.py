maxSum = 0
tempSum = 0
for a in range(1,100):
    for b in range(1,100):
        temp = str(a**b)
        for x in temp:
            tempSum += int(x)
        if tempSum > maxSum:
            maxSum = tempSum
        tempSum = 0
print maxSum
