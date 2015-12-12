from algorithms import *

highest = 0
highestX = 0
current = 0
for x in range(2,1000):
    current = calculateDecimalPeriod(x)
    if current > highest:
    	highestX = x
    	highest = current
print highestX
	
	
