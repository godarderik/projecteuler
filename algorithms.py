from math import *
from itertools import *
from decimal import *
#Function that returns the total number of divisors of a number (inclduing the number)

def getTotalDivisors(num):
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
def getFactors(num):
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
    return factors

def sieve(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for (i, isPrime) in enumerate(arr):
        if isPrime:
            yield i
            for x in range(i*i, n, i):
                arr[x] = False  

                                                  

 #Function that returns a reverse of the passed string
def reverseString(string):
    return str(string)[::-1]

#Function that returns whether a number is prime or not
def isPrime(num):
    x = 2
    if num < 2:
        return False
    while x <= sqrt(num):
        if num % x == 0:
            #not prime
            return False
        if x == 2:
            x +=1
        else:
            x+=2
    return True
def perm(l):
    sz = len(l)
    if sz <= 1:
        return [l]
    return [p[:i]+[l[0]]+p[i:] for i in xrange(sz) for p in perm(l[1:])]

#Sieve of erasthmus
def erasSieve(n):
      siv=range(n+1)
      siv[1]=0
      sqn=int(round(n**0.5))
      for i in range(2,sqn+1):
          if siv[i]!=0:
              siv[2*i:n/i*i+1:i]=[0]*(n/i-1)
      return filter(None,siv)

#Returns the prime factorization of num, given an array of primes divs
def getPrimeFactors(num,divs):
    facs = []
    currentNumIndex = 0
    while divs.count(num) != 1 and currentNumIndex < len(divs):
        if num % divs[currentNumIndex] == 0:
            facs.append(divs[currentNumIndex])
            num = num / divs[currentNumIndex]
            currentNumIndex = 0
        else:
            currentNumIndex += 1
    if currentNumIndex == 999:
        return []
    facs.append(num)
    return facs

#Determines is a number 'num' is a 'digits' digit pandigital number
def isPandigital(num, digits):
    num = list(num)
    if num.count("0") > 0:
        return False
    for x in range(1,(digits + 1)):
        if num.count(str(x)) == 1:
            continue
        else:
            return False
    return True


#Euler's phi function, return number of integers smaller than 'num' that are
#relatively prime with it

def phi(num):
    factors = list(set(getFactors(num)))
    result = num
    for x in factors:
        result *= (1 - (1.0 / x))
    return int(result)

#Return the greatest common divisor of two numbers
def gcd(a,b):
      while b:
         a, b = b, a % b
      return a 

#Returns all of the permutations of the input list
def allPermutations(input):
    return list(permutations(input))


#Calculates the decimal representation of the decimal of form 1/num to 'places' places
def calculateDecimalRepresentation(num,places):
    repeating = False
    rem = 1
    div = num
    decimal = ""
    while repeating == False:
        if div > rem:
            rem *= 10 
        decimal += str(rem/div)
        rem = rem % div
        if rem == 0 or len(decimal)>places:
            return decimal 

def calculateDecimal(num,dem,places):

    temp = str(num/dem)
    pos = temp.find(".")

    num = int(str(num).replace(".", ""))
    dem = int(str(dem).replace(".", ""))

    repeating = False
    rem = num
    div = dem
    decimal = ""
    while repeating == False:
        if div > rem:
            rem *= 10 
        decimal += str(rem/div)
        rem = rem % div
        if rem == 0 or len(decimal)>places:
            decimal = decimal[:pos] + "." + decimal[pos:] 
            if (num * dem) > 0:
                return decimal
            else:
                return -1 * float(decimal)

#Returns the period of the decimal representation of the fraction 1/num
#If 1/num does not repeat, it returns 0
def calculateDecimalPeriod(num):
    if num % 2 != 0 and num % 5 != 0:
        current = 1
        while (10**current - 1)%int(num) != 0:
            current += 1
        return current
    else:
        return 0

def newtonMethod(num,digits):
    #execute newton's method here
    vals = [0]*(digits+1)
    vals[0] = int(num**0.5)
    for x in range(0,digits):
        int1 = vals[x]
        int2 = (vals[x]**2.0 - num)
        int3 = (2*vals[x])
        dec = float(calculateDecimal(int2,int3,100))
        vals[x + 1] = (int1 - dec)
    return vals[99]

#turns a tuple into its integer representation
def tupleToNum(tup):
    ret = 0
    for y in range(0, len(tup)):
        ret += pow(10,y) * tup[len(tup)-1-y]
    return ret
