import algorithms
import math
n = 0
maxPrimes = 0
tempPrimes = 0
maxA = 0
maxB = 0
for a in range(-999, 1000):
    if a % 100 == 0:
        print a
    for b in range(-999,1000):
            while algorithms.isPrime(math.pow(n,2) + (a*n) + b) == True:
                tempPrimes += 1
                if a == -3 and b == 7:
                    print (math.pow(n,2) + (a*n) + b)
                    print tempPrimes
                    print n
                n+= 1
            if tempPrimes > maxPrimes:
                maxPrimes = tempPrimes
                maxA = a
                maxB = b
            tempPrimes = 0
            n = 0
print maxA * maxB
print maxA
print maxB
print maxPrimes
            
