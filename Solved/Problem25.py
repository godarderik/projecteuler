num1 = 1
num2 = 1
termNumber = 2
length = 0

while length < 1000:
    if num1 > num2:
        num2 += num1
        length = len(str(num2))
    else:
        num1 += num2
        length = len(str(num1))
    termNumber +=1
print termNumber
    
