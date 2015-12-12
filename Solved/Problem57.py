denom = 2
olddenom = 2
num = 3
count = 0
for x in range(1000):
    if len(str(denom)) < len(str(num)):
        count += 1

    olddenom = denom
    denom += num
    num = denom + olddenom
print count