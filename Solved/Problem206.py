from math import *

#for x in range(10000,100000):
#	num = x**2
#	if num%10000000 == 7988900:
#		print x,num
ending = [49470,58030,44470,39470,16970,22070,12930,49570,47930,20430,82930,90430,54570,40830,25830,10830,73330,19170,43330,34170,13330,49170,64170,16670,79170,94170]
nums = ["0","1","2","3","4","5","6","7","8","9"]
for a in nums:
	for b in nums:
		for c in nums:
			for d in nums:
				for e in ending:
					string = "1" + a + b + c + d + str(e)
					string = str(int(string)**2)
					if string[2] == "2" and string[4] == "3" and string[6] == "4" and string[8] == "5" and string[10] == "6" and string[12] == "7" and string[14] == "8" and string[16] == "9":
						print string  
