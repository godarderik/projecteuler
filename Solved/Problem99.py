from math import *


maxm = 0
count = 1
maxLine = 0
f = open("base_exp.txt")
for line in f:
	arr = line.split(",")
	for y in range(0,len(arr)):
		arr[y] = int(arr[y])
	#arr[0] = pow(arr[0],1/log10(arr[0]))
	arr[1] *= log10(arr[0])
	arr[0] = log10(arr[0])
	print arr[0]
	if arr[1]>maxm:
		maxm = arr[1] 
		maxLine = count
	count += 1
print maxLine