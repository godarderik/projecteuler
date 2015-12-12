from algorithms import *

amt = 0
for x in range(2,3):
	if int(x**0.5) != x**.5:
		 temp =  newtonMethod(x,100)
		 print temp
print amt
