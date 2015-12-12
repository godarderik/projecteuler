baseNumber = 1
total = 0
while baseNumber <= 1000:
    total += baseNumber ** baseNumber
    baseNumber += 1
total = str(total)
print total[-10:]
