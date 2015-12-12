from random import *
for it in range(2,13):
	f = 1.0/it
	count = 0
	for x in range(1,10001):
		amt = 1.0
		for x in range(0,1000):
			toss = randint(0,1)
			if toss == 0:
				amt *= (1 - f)
			else:
				amt += f * amt * 2
		if amt > 1000000000:
			count += 1 
	print count/10000.0  