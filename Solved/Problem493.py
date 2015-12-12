from random import *
from math import *



def nchoosek(n,k):
    res = 1
    res2 = 1
    for x in range(n-k+1, n+1): 
        res *= x
    for y in range(1,k+1):
        res2 *= y
    return res/res2


tot = 0
vals = [0]*10
vals[2] = 1
for x in range(2,8):
    choose1 = nchoosek(7,x)
    choose2 = nchoosek(10*x,20)
    for y in range(2,x):
        choose2 -= nchoosek(x,y) * vals[y]
    vals[x] = choose2
    tot += x  * choose1 * choose2

print tot*1.0/nchoosek(70,20)



