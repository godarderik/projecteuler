from algorithms import *
primes = erasSieve(1000000)

highestPrime = 0
highestX = 0

for x in range(0,5):
	amt = 0
	y = 0
	while amt < 1000000:
		amt += primes[x+y]
		y += 1
		if (isPrime(amt) and amt < 1000000 and y > highestX):
			highestPrime = amt
			highestX = y
print highestPrime
print highestX