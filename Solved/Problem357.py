import math
import random

def isPrime(n):
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    div = 5
    while (div <= math.sqrt(n)):
        if n % div == 0:
            return False
        div += 2
    return True

def sieve(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for (i, isPrime) in enumerate(arr):
        if isPrime:
            yield i
            for x in range(i*i, n, i):
                arr[x] = False

def divisors(num):
    div = 2
    while (div <= math.sqrt(num)):
        if num % div == 0:
            yield div
        div += 1
primes = [False] * 1000000
for x in sieve(1000000):
    primes[x] = True
num = 100000000
arr = [False] * num
for x in sieve(num):
    mark = True
    for y in divisors(x-1):
        check = y + (x-1)/y
        if check < 1000000:
            mark = primes[check]
        else:
            mark = isPrime(check)
        if (mark == False):
            break
    arr[x-1] = mark


count = 0
for ind,z in enumerate(arr):
    if z:
        count += ind

print count


