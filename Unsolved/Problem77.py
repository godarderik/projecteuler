from algorithms import *
arr = []
for x in erasSieve(5):
	tempArr = [1]
	for y in range(1,2):
		tempArr += [0]*(x-1)
		tempArr.append(1)
	arr.append(tempArr)
finalArr = arr[0] + [0]*9
arr.remove(arr[0])
print finalArr
print arr
for z in range(len(arr)):
	for x in range(len(arr[z])):
		yCoeff = len(arr[z]) - 1
		xCoeff = len(finalArr) - (finalArr[::-1]).index(1) - 1
		for y in range(len(finalArr)):
			print xCoeff, yCoeff
			print finalArr[y]
			if finalArr[y] != 0 and arr[z][x] != 0 and (x + y) <= yCoeff + xCoeff :
				print "here"
				finalArr[x+y] = arr[z][x]*finalArr[y]
				print finalArr
			
print finalArr
