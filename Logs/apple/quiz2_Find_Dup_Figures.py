__author__ = 'k22li'
__date__ = "22th-Dec-2014"
__doc__ = "purpose is to find out the element which is dup of one of the other elements from the existing list"
##############################
# function implementations    
##############################
import os 

listWithDups = range(100000)
listWithDups.insert(40, 9999)

for item in listWithDups:
	if (listWithDups.count(item)) >1:
		print item
		break
