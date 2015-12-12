from itertools import *
from math import *

turns = 15 

probs = range(2,turns+2)
ways = 0
totalPerms = factorial(turns+1)

for x in range(0,7+1): #Number of reds
	if x == 0:
		continue
	perms = combinations(probs,x)
	for y in perms:
		prod = 1
		for z in y:
			prod *= (z - 1)
		ways += prod
ways += 1
print ways, "/", totalPerms
print trunc(1 /( ways * 1.0 / totalPerms))
		 

