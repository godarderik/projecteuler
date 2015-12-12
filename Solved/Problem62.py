cubes = {}

for z in range(10000):
    sort = list(str(z**3))
    for x,y in enumerate(sort):
        sort[x] = int(y)
    sort = sorted(sort)
    for x,y in enumerate(sort):
        sort[x] = str(y)
    sort = "".join(sort)
    if sort in cubes:
        cubes[sort][0] += 1
        cubes[sort][1].append(z**3)
        if cubes[sort][0] == 5:
            print sorted(cubes[sort][1]) 
    else:
        cubes[sort] = []
        cubes[sort].append(1)
        cubes[sort].append([z**3])

