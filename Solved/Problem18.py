import algorithms
import copy
lines = []
linesArray = []
tempValues = []
tempValuesPrev = []
for c in range(0,101):
    tempValues.append(0)
f = open('/Users/joelnpam/Desktop/triangle.txt', 'r')
for line in f:
    lines.append(line)
for x in range(0,len(lines)):
    linesArray.append(lines[x].split())
    for y in range(0,len(linesArray[x])):
        linesArray[x][y] = int(linesArray[x][y])
tempValues[0] = linesArray[0][0]

###Actual solving
y = range(0,len(linesArray))
y.reverse()
for a in y:
    tempValuesPrev = copy.deepcopy(tempValues)
    for b in range(0,len(linesArray[a])):
        if a+1 ==  len(linesArray):
            tempValues[b] = linesArray[a][b]
        else:
            tempValues[b] = linesArray[a][b] + algorithms.maximum(tempValuesPrev[b], tempValuesPrev[b + 1])
print tempValues            
        #if b == 0:
        #    tempValues[b] = tempValues[b] + (linesArray[a+1][b])
        #elif b == a:
        #        tempValues[b] = tempValuesPrev[b - 1]  + (linesArray[a][b])
        #else:
        #        tempValues[b] = linesArray[a][b] + algorithms.maximum(tempValues[b], tempValues[b - 1])
            #print tempValues[b]
    
                
