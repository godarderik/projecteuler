from random import *

num = 0
for x in range(0,50):
    num += (1 - ((2**x - 1.0)/(2**x))**32 )


print num