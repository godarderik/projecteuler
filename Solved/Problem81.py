f = open('matrix.txt','r')
matrix = []
for line in f:
	line = line.split(",")
	for x in range(0,len(line)):
		line[x] = int(line[x])		
	matrix.append(line)
modMat = []
for x in range(0,len(matrix)):
	modMat.append([10000000]*len(matrix))
modMat[0][0] = matrix[0][0]

def genCoords(total):
	ret = []
	if total <= len(matrix)-1:
		x = total 
		y = 0 
		while x >= 0:
			ret.append([x,y])
			x -= 1
			y += 1
		return ret
	else:
		x = len(matrix)-1
		y = total - (len(matrix)-1)
		while x >= total - (len(matrix)-1):
			ret.append([x,y])
			x -= 1
			y += 1
		return ret
			

for total in range(0,((len(matrix)-1)*2)+1):
	for coord in genCoords(total):
		x = coord[0]
		y = coord[1]
		if x < len(matrix)-1:
			modMat[x+1][y] = min(modMat[x][y] + matrix[x+1][y],modMat[x+1][y])
		if y < len(matrix)-1:
			modMat[x][y+1] = min(modMat[x][y] + matrix[x][y+1],modMat[x][y+1])
print modMat[79][79]