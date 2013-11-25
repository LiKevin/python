# -*- coding: utf-8 -*-
__author__ = 'k22li'


#tList = [i for i in range(10)]
tList = range(10)
kList = range(3)
print tList
print kList

for loop in range(len(kList)):
    tList.remove(kList.pop())
print tList



#列表过滤
newList = [i for i in tList if i not in kList]
print newList



#dict合并
tDict = {'a': 1, 'b':2, 'c':3}
kDict = {'e': 4, 'f':5}

tDict.update(kDict)

print tDict
print tDict.popitem()
print tDict.pop('c')
print tDict

print max('abcedfg')
print min('abced')