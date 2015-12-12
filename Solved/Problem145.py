from algorithms import *
counter = 0
def containsOnlyOddDigits(string):
    string = list(str(string))
    if string.count("0") > 0 or string.count("2") > 0 or string.count("4") > 0 or string.count("6") > 0 or string.count("8") > 0:
        return False
    else:
        return True
for n in range(1, 10000000):
    if containsOnlyOddDigits(n + int(reverseString(n))) and n % 10 != 0:
        counter += 1
print counter

