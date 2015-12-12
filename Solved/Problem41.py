from algorithms import *
from itertools import*

nums = [1,2,3,4,5,6,7,8,9]
highestPrime = 0
for x in range(2,10):
	start = nums[:x]
	new = list(permutations(start))
	for y in new:
		amt = 0
		for z in range(0,len(y)):
			amt += pow(10,(len(y) - z - 1)) * y[z]
		if isPrime(amt) and amt > highestPrime:
			highestPrime = amt
print int(highestPrime)

