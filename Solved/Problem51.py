import math

def sieve(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for (i, isPrime) in enumerate(arr):
        if isPrime:
            yield i
            for x in range(i*i, n, i):
                arr[x] = False

def isPrime(n):
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    div = 5
    while (div <= math.sqrt(n)):
        if n % div == 0:
            return False
        div += 2
    return True



primes = [False]* 10000000
test = []
for x in sieve(10000000):
    primes[x] = True
    if str(x).count("1") >= 2:
        ind1 = str(x).find("1")
        ind2 = str(x).find("1" , ind1 + 1)
        ind3 = str(x).find("1", ind2 + 1)
        ind4 = str(x).find("1", ind3 + 1)
        ind5 = str(x).find("1", ind4 + 1)
        test.append([x,ind1, ind2, ind3, ind4, ind5])


def countPrimes(arr):
    num = arr[0]
    ind1 = arr[1]
    ind2 = arr[2]
    ind3 = arr[3]
    #ind4 = arr[4]

    count = 0
    for x in range(0,10):
        newNum = list(str(num))
        newNum[ind1] = str(x)
        newNum[ind2] = str(x)
        newNum[ind3] = str(x)
        #newNum[ind4] = str(x)
        #newNum[ind5] = str(x)
        newNum = "".join(newNum)
        if primes[int(newNum)] and len(str(int(newNum))) == len(str(num)):
            count += 1
    return count
print len(test)

maxNum = [999999999999999]
for x in test:
    if countPrimes(x) == 8 and x[0] < maxNum[0]:
        maxNum = x
print maxNum

def countPrimesTest(arr):
    num = arr[0]
    ind1 = arr[1]
    ind2 = arr[2]
    ind3 = arr[3]
    #ind4 = arr[4]
    for x in range(0,10):
        newNum = list(str(num))
        newNum[ind1] = str(x)
        newNum[ind2] = str(x)
        newNum[ind3] = str(x)
        newNum = "".join(newNum)
        if primes[int(newNum)] and len(str(int(newNum))) == len(str(num)):
            print isPrime(int(newNum)), newNum
countPrimesTest(maxNum)



