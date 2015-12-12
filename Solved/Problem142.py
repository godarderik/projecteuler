from math import *
from itertools import *

'''x > y > z > 0

(x + y) (x - y) (x + z) (x - z) (y + z) (y - z)

(x^2 - y^2) (x^2 - z^2) (y^2 - z^2)

(a - b) (b - c) (a - c)

(a^2 - ab - ac + bc)(b - c)

(a^2*b - b^2*a) + (c^2 * a - a^2*c) + (b^2 * c - c^2 * b)'''

#first n squares
def squares1(low_n,n):
    for z in range(low_n,n):
        yield z**2
def squares2(low_n,n):
    for z in range(low_n,n):
        yield z**2
def squares3(low_n,n):
    for x in range(low_n,n):
        yield x**2


def isSquare(n):
    return ((int(round(pow(n,1/2.0))))**2 == n)

def test(i,j,k):
    return isSquare(abs(i -j)) and isSquare(abs(i - k)) and isSquare(abs(j - k)) and isSquare(i + j) and isSquare(i + k) and isSquare(j + k)


squares = [False] * 4000000
for x in range(2000):
    squares[x**2] = True

arr = {}


for x in range(1,1000000):
    print x
    for y in range(x+1, 1000000):
       if squares[y+x] and squares[y - x]:
            if str(y) in arr:
                arr[str(y)].append(x)
            else:
                arr[str(y)] = [x]

count = 0
minAmt = 0
print len(arr) 
print "half"
for (key,value) in arr.iteritems():
    k = int(key)
    for y in combinations(value,2):
        if test(k,y[0], y[1]):
            print k, y[0], y[1]

'''for (key,value) in arr.iteritems():
    if len(value) >= 2:
        for k in range(len(value)):
            for j in range(k+1,len(value)):
                itK = value[k]
                itJ = value[j]
                if isSquare(itJ - itK) and itK != itJ and test(sqrt(int(key)), sqrt(itJ), sqrt(itK)):
                    print sqrt(int(key)), itJ, itK'''





