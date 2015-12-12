from random import *

def randomPermutation(lst):
        shuffle(lst)
        return lst

def isSorted(lst):
        if lst == []:
             return True
        prev = lst[0]
        for x in lst[1:]:
            if x < prev:
                return False
            prev = x
        return True
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def guessSort(x):

        #number of comparisons performed
        comps = 0

        #continue until array is sorted
        while (isSorted(x) == False):
            comps += 1

            #pick two random elements
            ele1 = randrange(len(x))
            ele2 = randrange(len(x))

            #if out of order, swap them
            if x[ele1] > x[ele2] and ele1 < ele2:
                temp = x[ele1]
                x[ele1] = x[ele2]
                x[ele2] = temp
        return {"lst":x, "comps":comps}
def threeSort(x):
    while (isSorted(x) == False):
        pass
        #select

    comps = 0

def bozoSort():
    tot = 0
    for x in range(100000):
        lst = randomPermutation(range(4))
        ret = guessSort(lst)
        tot+= ret["comps"]
    print tot/100000.0

bozoSort()
