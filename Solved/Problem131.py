from math import *


def sieve(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for (i, isPrime) in enumerate(arr):
        if isPrime:
            yield i
            for x in range(i*i, n, i):
                arr[x] = False

def isCube(n):
    return ((int(round(pow(n,1/3.0))))**3 == n)
 
count = []

def cubes(n):
    for x in range(n):
        yield x**3

for y in sieve(1000000):
    for x in cubes(1000):
        num = (y + x)
        if isCube(num):
            count.append([x,y])
            break
print len(count)
print count


