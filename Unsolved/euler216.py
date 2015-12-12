squares = [False] * 50000000
primes = [False] * 50000000



def sieve(n):
    arr = [True] * n
    arr[0] = arr[1] = False
    for (i, isPrime) in enumerate(arr):
        if isPrime:
            yield i
            for x in range(i*i, n, i):
                arr[x] = False


for x in sieve(50000000):
    primes[x] = True

count = 0
n = 0
for k,v in enumerate(primes):
    while 2*n**2 - 1 <= k:
        n += 1
    if v and squares[k]:
        count += 1 

print count