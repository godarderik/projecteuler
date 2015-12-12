count = 0
nextNum = 0
for x in range(1,10000000):
    if x % 100000 == 0:
        print x
    startNum = x
    while startNum != 1 and startNum != 89:
        nextNum = 0
        for y in list(str(startNum)):
           nextNum += pow(int(y),2)
        startNum = nextNum
    if startNum == 89:
        count += 1
print count
           
