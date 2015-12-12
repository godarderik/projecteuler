yProduct = 1
xProduct = 1
for x in range(10,100):
	for y in range(x+1,100):
		for sub in str(x):
			if (y%10 != 0  and str(y).count(sub) == 1):
				if float(x)/y == float(str(x).replace(sub,"",1))/int(str(y).replace(sub, "",1)):
					yProduct *= y
					xProduct *= x
print xProduct, "/", yProduct

