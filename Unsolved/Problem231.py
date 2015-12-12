import algorithms
import copy


cache = [0] * 100


def updateCache(n, val):
    if n < len(cache):
        cache[n] = val

def calculateSum(mask):
    tot = 0
    num = 0 
    for k,v in mask.iteritems():
        if v != 0:
            num += int(k)**v
            tot += int(k) * v
    print mask, num, tot

    return {"num": num, "tot" : tot}
    



def sumFactors(mask, limit):
    for k,v in mask.iteritems():
        calc = calculateSum(mask)
        if (calc["num"] < limit):
            cache[calc["num"]] = calc["tot"]
            newMask = copy.deepcopy(mask)
            newMask[k] += 1
            sumFactors(newMask, limit)
        else: 
            break




def factorSum():
    bitmask = {}
    for x in algorithms.sieve(10):
        bitmask[x] = 0
    sumFactors(bitmask, 100)
    print cache
    return sum(cache)

print factorSum()
