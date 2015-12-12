pair = []
upper = 3.0/7
lower = 0

for d in range(1000000):
    for n in range(int(d*.4284) + 1,int(d*.4286)):
        div = (n*1.0/d)
        if d % n != 0 and div > lower and div < upper:
            pair = [n,d]
            lower = div
print pair