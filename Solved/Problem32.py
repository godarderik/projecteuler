from algorithms import *
#31633
pans = []
amt = 0
nums = ["1","2","3","4","5","6","7","8","9"]
for x in range(1,2000):
	for y in range(1,2000):
		totString = str(x) + str(y) + str(x*y)
		if isPandigital(totString, 9):
			pans.append(x * y)
pans = list(set(pans))
for x in pans:
	amt += x
print amt