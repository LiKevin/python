#__author__=="k22li"

# first implementations:

def getAllValidMembers(n=0):
	validMembers = []
	for i in range(1, n):
		for j in range(2, i):
			if i%j == 0:
				break
		else:
			validMembers.append(i)

	print validMembers



if __name__=="__main__":

	getAllValidMembers(100)
		
