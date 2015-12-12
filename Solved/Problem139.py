from algorithms import * 
from math import *
count = 0 
for n in range(1,10000):
	for m in range(n+1,10000):
		if gcd(n,m) == 1 and (m - n) % 2 != 0:
			if (m**2 + n**2)**2 % (2*m*n - (m**2 - n**2))**2 == 0: 
				count += 100000000/(2*m*(m + n))
print count