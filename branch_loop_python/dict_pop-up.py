__author__ = 'k22li'


# 1, test pop function of dict

aDict = {'a': 12, 'b':20, 'c':32}

print id(aDict)
k = aDict.pop('a', None)
#t = aDict.pop('k')
print k
print id(k), id(aDict)


#2, test the update function of dict
bDict = {'k': 24}

print id(bDict)
aDict.update(bDict)
print id(aDict), id(bDict)


#3, test List EXTEND function for comparison purpose

aList = ['a', 'b', 'c']

print id(aList)

aList.extend('k')

print id(aList), aList

