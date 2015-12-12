end = 0
number = 1
contains = 0 
def containsSameDigits(oldNum, newNum):
    cont = 0
    oldNum = list(oldNum)
    newNum = list(newNum)
    for x in oldNum:
        if newNum.count(x) == 1:
            continue
        else:
            cont = 1
    for x in newNum:
        if oldNum.count(x) == 1:
            continue
        else:
            cont = 1
    return cont
        
while end < 1:
  for x in range(2,7):
      if containsSameDigits(str(number),str(number * x)) == 0:
          continue
      else:
          contains = 1
          break
  if contains == 0:
       print number
       break
  else:
       contains = 0
       number += 1
  
        
    
