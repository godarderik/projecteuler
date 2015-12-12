import algorithms
from math import *
primesCounter = 0
testPrime = 2
rotation = ""


def rotate(string):
    tempLetter = string[0]
    returnString = ""
    for x in range(0, len(string) - 1):
        returnString += string[x + 1]
    returnString += tempLetter
    return returnString         


while testPrime < 2000000:
    if algorithms.isPrime(testPrime) == True:
        rotation = str(testPrime)
        for y in range(1, len(rotation) + 1):
            rotation = rotate(rotation)
            if algorithms.isPrime(int(rotation)) == True:
                if y == len(rotation):
                    #last time
                    primesCounter += 1
                    break
            else:
                break
    if testPrime == 2:
        testPrime += 1
    else:
        testPrime += 2
        while str(testPrime).count("2" or "4" or "6" or  "8") <> 0:
            testPrime += 2
    if (testPrime % 1111111 == 0):
        print testPrime
print primesCounter            
        
       
