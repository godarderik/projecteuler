bouncy = 12951

def isIncreasing(n):
    high = list(str(n))[0]
    for x in list(str(n)):
        if x < high:
            return False
        else: 
            high = x
    return True


def isDecreasing(n):
    low = list(str(n))[0]
    for x in list(str(n)):
        if x > low:
            return False
        else: 
            low = x
    return True


start = 999999
while ((1.0 * bouncy)/start > .01):
    start += 1
    if isIncreasing(start) or isDecreasing(start):
        bouncy += 1
print start