"""
100 rmb 
target to buy 100 chickens; 
price:
	3 small ones cost 1rmb; 
	1 middle size one costs 3 rmb; 
	1 large size one costs 5 rmb; 

question: design the pattern to figure out all those possibilities of the buys
methods; 
"""

def spendMoney():
	for x in range(20):
		for y in range(33):
			if (5*x + 3*y + (100-x-y)/3.0) == 100:
				print x, y , 100-x-y


if __name__ == '__main__':
	
	spendMoney()
