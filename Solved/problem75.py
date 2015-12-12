from algorithms import * 
from fractions import Fraction

nums = []
count = 0 
for n in range(1,1500):
	for m in range(n+1,1500):
		if gcd(n,m) == 1 and (m - n) % 2 != 0:
			add = 2*m*(m + n)
			if add <= 1500000:
				nums.append(add)
			for y in range(2,(1500000/add)+1):
				nums.append(add*y)
print len(nums)
nums = sorted(nums)
for x in range(0,len(nums)-1):
	x1 = x - 20
	if x1 < 0 :
		x1 = 0
	x2 = x + 20
	if x2 > len(nums) - 1:
		x2 = len(nums) - 1
	work = nums[x1:x2]
	if work.count(nums[x]) == 1:
		count += 1
print count