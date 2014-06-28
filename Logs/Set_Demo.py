__author__ = 'k22li'


import sets
import random


aList = ['a', 'b', 'c']

bList = ['c', 'd', 'e']


aSet = sets.Set(aList)
bSet = sets.Set(bList)


print list(aSet.difference(bSet))

#print list(bSet.difference_update(aSet))

print list(aSet.intersection(bSet))

print '*' * 80
print list(aSet.union(bSet))

print list(aSet)

print aList * int(2)

sList = aList*3
random.shuffle(sList)

print sList


