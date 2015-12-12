from algorithms import *

cons = 0
test = 2

mult = 1


divs = erasSieve(1000)
def getPrimeFactors(num):
    facs = []
    currentNumIndex = 0
    while divs.count(num) != 1 and currentNumIndex < 168:
        if num % divs[currentNumIndex] == 0:
            facs.append(divs[currentNumIndex])
            num = num / divs[currentNumIndex]
            currentNumIndex = 0
        else:
            currentNumIndex += 1
    if currentNumIndex == 999:
        return []
    facs.append(num)
    return facs

while cons < 4:
	if (test % 1000) == 0:
		mult += 1
	if len(set(getPrimeFactors(test))) == 4:
		cons += 1
	else:
		cons = 0
	test += 1
	
print test - 4

