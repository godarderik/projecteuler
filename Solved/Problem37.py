from algorithms import *
primesTest = erasSieve(1000000)
add = True
primesArray = []
numString = ""
for x in range(1,len(primesTest)):
    numString = str(primesTest[x])
    for y in range(1, len(numString)):
        numString = numString[1:]
        if isPrime(int(numString)):
            continue
        else:
            add = False
            break
    numString = str(primesTest[x])   
    for z in range(1, len(numString)):
        numString = numString[:-1]
        if isPrime(int(numString)):
            continue
        else:
            add = False
            break
    if add == True and len(str(primesTest[x])) > 1:
        primesArray.append(primesTest[x])
    add = True
total = 0
for b in primesArray:
    total+=int(b)
print total
        
