from algorithms import *
count = 0 
for d in range(2,12001):
    for n in range(int(.33 * d),int((.5 * d)) + 1):
        if gcd(n,d) == 1 and float(n)/d < .5 and float(n)/d > 1.0/3:
            count += 1
print count
            
