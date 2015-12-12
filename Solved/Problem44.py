from algorithms import *
top = 10000
res = []
distance = 100000000000

def isPentagonal(num):
	res = (sqrt(24 * num + 1) + 1)/6
	if res - int(res) < .0001:
		return True
	return False
for x in range(1,top):
	val1 = x * (3 *x -1)/2
	for n in range(1,x):
		val2 = n * ( 3 * n -1)/2
		if isPentagonal(val1 + val2) and isPentagonal(val1 - val2) and abs(val1-val2) < distance:
			
			distance = abs(val1-val2) 
			print n,x, val1, val2, distance

	
'''
def evalEq(x,n,a):
	if (n * (3*n -1)/2) + ((x * (3*x -1))/2) - ((a * (3*a -1))/2) == 0:
		return True
	else: 
		return False
print evalEq(42,51,66)'''