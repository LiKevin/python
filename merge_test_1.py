# -*- coding: utf-8 -*-
__author__ = 'k22li'

# merging: 合并：将两个子序列合并排序。

#Kevin's solution, 合并两个序列，然后对新 序列进行排序
from random import randint

aList = [randint(0, 999) for i in range(10)]
bList = [randint(0, 999) for i in range(10)]


def combineTwoList(listA, listB):
    aLen = len(listA)
    bLen = len(listB)
    newList = ['' for i in range(aLen+bLen)]
    i = 0
    while i>=0 and i<aLen:
        newList[i] = listA[i]
        i += 1
    while i>= aLen and i<aLen+bLen:
        newList[i] = listB[i-aLen]
        i += 1
    return newList

def sortAsc(listC):
    cLen = len(listC)
    for i in range(1,cLen):
        key = listC[i]
        j = i-1
        while j>=0 and key< listC[j]:
            listC[j+1] = listC[j]
            j -= 1
        listC[j+1] = key
    return listC

#


def print_format(*arg):
    if not len(arg)>0:
        print '\n', '*'*60
    else:
        print 'The value is: %s'%arg

if __name__ == '__main__':
    print_format()
    print_format(aList)
    print_format(bList)
    combineList = combineTwoList(aList, bList)
    print_format(combineList)
    sortedList = sortAsc(combineList)
    print_format(sortedList)
