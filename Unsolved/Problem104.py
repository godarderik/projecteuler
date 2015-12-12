from algorithms import *
stop = False
f1 = 1
f2 = 1
count = 2
while stop == False:
    #if len(str(f1)) % 1000 == 0:
       # print len(str(f1))
    if f1 > f2:
        f2+=f1
        #print f2
        count+=1
        if isPandigital(str(f2)[:9],9) and isPandigital(str(f2)[-9:],9):
            print count
            stop = True
    else:
        f1+=f2
       # print f1
        count+=1
        if isPandigital(str(f1)[:9],9) and isPandigital(str(f1)[-9:],9):
            print count
            stop = True
    
