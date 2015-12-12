m = 2
n = 1
d = 1
total = []
temp = 0
prev = {}
greatestCount = 0
greatestX = 0
while m < 25:
    while n < m:
        while d < 6:
            temp = (d * (m**2 - n**2)) + (d * (2 * m * n)) + (d * (m**2 + n**2))
            if temp <= 1000:
                total.append(temp)
                if temp == 720:
                    print (d * (m**2 - n**2)) , (d * (2 * m * n)) , (d * (m**2 + n**2))
            d+= 1
        n += 1
        d = 1
    n = 1
    m += 1
        
#for x in total:
if total.count(120) > greatestCount:
     greatestCount = total.count(120)
     greatestX = 120
print greatestCount
print greatestX
