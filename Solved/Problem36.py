number = 1
numberBin = 0
total = 0
while number < 1000000:
    numberBin = bin(number)
    numberBin = numberBin[::-1]
    numberBin = numberBin[:-2]
    if (str(number)[::-1]== str(number)) and str(numberBin)[::-1] == str(numberBin):
        total += number
    number += 1
print total     
