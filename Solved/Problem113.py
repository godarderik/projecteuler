def initArray(digits, desc):
    num = 9
    arr = []
    if desc:
        num = 10
    for i in range(digits):
        arr.append([])
        for j in range(num):
            arr[i].append(0)
    return arr

def getTotInc(arr):
    for l in range(1,len(arr)):
        for m in range(len(arr[l])):
            arr[l][m] = sum(arr[l-1][m :])
    return arr
def getTotDec(arr):
    for l in range(1,len(arr)):
        for m in range(len(arr[l])):
            arr[l][m] = sum(arr[l-1][0: m + 1])
    return arr

digits = 100
inc = initArray(digits - 1, False)
dec= initArray(digits - 1, True)
#print inc, dec
for k in range(9):
    inc[0][k] = len(inc[0]) - k
for k in range(10):
    dec[0][k] = k+1

inc = getTotInc(inc)
dec = getTotDec(dec)

tot = 0
for x in range(len(inc)):
    tot += sum(inc[x])
for y in range(len(dec)):
    tot += sum(dec[y])
tot += 9 #1 through 9
tot -= digits  - 1
tot -= (9 * (digits - 1)) 
print tot


