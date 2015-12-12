from math import *
total = 0
f = open("triangles.txt")


def triangleContainsPoint(verts, point):
	for x in range(0,3): #normalize vectors
		dist = sqrt((pow(verts[x*2],2) + pow(verts[x*2+1],2)))
		verts[x*2] /= dist
		verts[x*2+1] /= dist
	totalAng = acos(verts[0] * verts[2] + verts[1] * verts[3])
	totalAng += acos(verts[2] * verts[4] + verts[3] * verts[5])
	totalAng += acos(verts[4] * verts[0] + verts[5] * verts[1])
	if abs(totalAng - 2*pi) <.0000001:
		return True
	else:
		return False
for line in f:
	arr = line.split(",")
	for x in range(0,len(arr)):
		arr[x] = int(arr[x])
	total += triangleContainsPoint(arr,0)
	
	
print total


	
