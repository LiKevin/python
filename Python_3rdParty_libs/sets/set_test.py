__author__ = 'k22li'

import sets

aList = ['a', 'b', 'c', 'd']

bList = ['a', 'c', 'e', 'f']

aS= sets.Set(aList)
bS = sets.Set(bList)

print list(aS.intersection(bS))

