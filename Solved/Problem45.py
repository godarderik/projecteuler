pentagons = []
hexagons = []
for n in range(0,100000):
    pentagons.append((n*(3*n-1))/2)
    hexagons.append(n*(2*n-1))
final = set(pentagons).intersection(hexagons)
print final 
    
