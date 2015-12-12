largestNum = 0
tempString = ""
largestX = 0

def isPandigital(num, digits):
    num = list(num)
    for x in range(1,(digits + 1)):
        if num.count(str(x)) == 1:
            continue
        else:
            return False
    return True

for x in range(1,10000):
    for y in range(1,20):
        if (len(tempString + str(x * y)))< 10:
            tempString += str(x * y)
        else:
            if int(tempString) > largestNum and len(tempString) == 9 and isPandigital(tempString, 9) == True:
                largestNum = int(tempString)
                largestX = x
            break
    tempString = ""
print largestX
print largestNum

            
