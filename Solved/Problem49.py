from algorithms import *
import itertools
eras = erasSieve(10000)
candidates = []
final = []
x = 0
while eras[x] < 1000:
	eras.remove(eras[x])
for x in eras:
	tempX = x
	tempX = str(x)
	tempTup = [int(tempX[0]), int(tempX[1]), int(tempX[2]), int(tempX[3])]
	combs = itertools.permutations(tempTup,4)

	candAdd = []

	for y in combs:
		if eras.count(tupleToNum(y)) > 0:
			candAdd.append(int(tupleToNum(y))) 
	if len(list(set(candAdd))) > 2:
		candidates.append(list(set(candAdd)))
for x in range(0, len(candidates)):
	for a in candidates[x]:
		for b in candidates[x]:
			for c in candidates[x]:
				if 2*(b-a) == c-a and a!=b:
					final.append([a,b,c])
for x in final:
	x = x.sort()
print final