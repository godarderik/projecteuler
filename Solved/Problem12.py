from math import sqrt

currentNum = 0
currentTri = 1
divs = 0

def getDivisors(num):
    divisors = 1
    copyNum = num
    currentNumberOfFactors = 1
    currentDividingNumber = 2
    factors = []
    while currentDividingNumber <= sqrt(num):
        if (num % currentDividingNumber == 0):
            factors.append(currentDividingNumber)
            num = num/currentDividingNumber
            currentDividingNumber = 2
        else:
            if (currentDividingNumber == 2):
                currentDividingNumber += 1
            else:
                currentDividingNumber += 2
    while currentDividingNumber <= num:
         if (num % currentDividingNumber == 0):
            factors.append(currentDividingNumber)
            num = num/currentDividingNumber
            currentDividingNumber = num + 1
         else:
            currentDividingNumber += 1
    if len(factors) == 2:
        return 2
    x = 0
    while x < len(factors):
        if x == 0:
         x+=0
        elif factors[x] == factors[x-1]:
            currentNumberOfFactors += 1
        else:
            currentNumberOfFactors  += 1
            divisors *= currentNumberOfFactors 
            currentNumberOfFactors = 1
        x += 1
    currentNumberOfFactors  += 1
    divisors *= currentNumberOfFactors 
    return divisors
            
while divs <= 500:
    currentNum= (1.0/2.0) * (currentTri * (currentTri + 1))
    currentTri += 1
    tempDivs = getDivisors(currentNum)
    if tempDivs>divs:
        divs = tempDivs
        print divs
        print currentNum
print currentNum 



    
