from algorithms import *
highest = 0
highN = 0
tests = erasSieve(10000)
for n in range(0,len(tests)):
    res = float(tests[n])/phi(tests[n])
    if res > highest:
        highN = tests[n]
        highest = res
print highN
