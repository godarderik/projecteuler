from random import *
from math import *

def sieve(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for (i, isPrime) in enumerate(arr):
        if isPrime:
            yield i
            for x in range(i*i, n, i):
                arr[x] = False