colin = [0]*37 #Define two arrays to contain the number of ways each person can roll a certain number
peter = [0]*37

peterWins = 0 #Total number of ways in which peter wins

#Function that recursively computers the number of ways a 'diceNum' number 
#of dice with 'sides' sides can be rolled for a total of 'total'

#Number of ways a sum can be rolled is defined recursively:
#ways(diceNum, total, sides) = ways(diceNum-1, total - 1,sides) + ways(diceNum-1, total - 2,sides) + ... ways(diceNum-1, total - sides,sides)

def ways(diceNum,total,sides): 
	if diceNum == 1: 
		if total > 0 and total <= sides:
			return 1   #If one dice is being rolled and the total is a number on the face of the dice, it can be achieved in one way
		else:
			return 0 #If number is not on dice
	else:
		totl = 0
		for y in range(1,sides+1):  
			totl += ways(diceNum-1, total - y,sides) #First die can be in range [1,sides]
		return totl 

#Obtain the number of ways Colin can roll different sums
for x in range(6,37):
	colin[x] = ways(6,x,6)
#Obtain the number of ways Peter can roll different sums
for z in range(9,37):
	peter[z] = ways(9,z,4)
#Loop through all of the entries in Colin for each entry in Peter
for x in range(0, len(peter)):
	for y in range(0, len(colin)):
		if x > y:
			peterWins += peter[x] * colin[y] #If Peter's score is higher, add the total ways this could occur to the ways in which Peter could win



sampSpace = pow(4,9) * pow(6,6) #Total number of dice rolling outcomes between the two players

#Divide ways Peter wins by total number of possible outcomes
print peterWins,"/",sampSpace, " = ", str(peterWins * 1.0 / sampSpace) #  7009890480 / 12230590464  =  0.573144076783
			

 

