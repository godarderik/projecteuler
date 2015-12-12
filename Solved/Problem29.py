import math
combos = []
for a in range(2,101):
    for b in range(2,101):
        combos.append(math.pow(a,b))
combos = list(set(combos))
print len(combos)
        
