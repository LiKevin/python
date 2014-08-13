# -*- coding: utf-8 -*-
__author__ = 'k22li'

import timeit

#case 1:

exe = \
    """
    aList = [1, 2, 3, 4, 2, 3]

    def removeUniques(listItem):

        newList = [elem for elem in listItem if listItem.count(elem)>1]
        return newList

    c = removeUniques(aList)
#    print c
    """

timer1 = timeit.Timer(exe)

print timer1.timeit(number = 1000)

#case 2: set

bList = [1, 2, 3, 4, 2, 3]

def removeUniquesSec(listItem):
    for item in listItem:
        if listItem.count(item)>
        tempList.append()