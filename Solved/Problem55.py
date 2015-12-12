import algorithims

x  = 1
number = 0
totalNumbers = 0
iterations = 0
while x < 10000:
    while iterations < 50:
        if iterations == 0:
            number = x
            number += int(algorithims.reverseString(x))
        else:
            number += int(algorithims.reverseString(number))
        if str(number) == algorithims.reverseString(number):
            #number is non lychrel
            iterations = 0
            break
        elif iterations == 49:
            iterations = 0
            totalNumbers+=1
            break
        else:
            iterations += 1
    x+= 1
    if (x % 100) == 0:
        print x
        
            
print totalNumbers 
    
    
