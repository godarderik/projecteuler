'''pows = []

bArr = [3]
rArr = [1]
found = 0
b = 15
rIt = [6]

while found == 0:
	for r in rIt:
		num = (pow(b,2) - b)/ ((pow(b,2) - b) + (pow(r,2) - r) + 2.0 * b * r)
		if num == .5:
			print b,r
			bArr.append(b)
			rArr.append(r)

			b *= (bArr[len(bArr)-1]*1.0)/bArr[len(bArr)-2]
			print (bArr[len(bArr)-1]*1.0)/bArr[len(bArr)-2]
			b = int(b)
			rIt = range(int(b* 1.0 *rArr[len(rArr)-1] / bArr[len(bArr)-1]),int(b* 1.0 *rArr[len(rArr)-1] / bArr[len(bArr)-1]) + 100)
			print "len", len(rIt)
			print "r", rIt[0], "b", b

			if b + r > pow(10,12):
				found = 1
	b += 1
	rIt = range(int(b* 1.0 *rArr[len(rArr)-1] / bArr[len(bArr)-1]),int(b* 1.0 *rArr[len(rArr)-1] / bArr[len(bArr)-1])+ 100 '''

xSols = [1]
ySols = [1]

for x in range(0,20):
	xSols.append(3*xSols[x] + 2 * ySols[x] - 2)
	ySols.append(4*xSols[x] + 3 * ySols[x] - 3)
	if ySols[-1] > pow(10,12):
		print xSols[x + 1]
		break

			

		