import algorithms
import inspect
from math import *
startNumber = 9
canBeWritten = False
end = False
def lineno():
    return inspect.currentframe().f_back.f_lineno


while end == False:
    if (algorithms.isPrime(startNumber) == False):
        for testSquare in range(1, int(sqrt(startNumber))):
            for testPrime in range(1, startNumber):
                if algorithms.isPrime(testPrime) == False:
                    continue
                if testPrime + (2 * (testSquare ** 2)) == startNumber:
                    canBeWritten = True
                    break
            if canBeWritten == True:
                break
    if canBeWritten == False:
        print startNumber
        end = True
    else:
        canBeWritten = False
        startNumber +=2
        while (algorithms.isPrime(startNumber)) == True:
            startNumber +=2
        if startNumber % 555 == 0:
            print startNumber



