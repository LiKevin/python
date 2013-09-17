# -*- coding:utf-8 -*-
__author__ = 'k22li'

import random

#直接引用timeit中的timeit方法
from timeit import timeit as timeIt


"""
方案1: from timeit import timeit as TI
"""

def testCase():

    aList = range(10)

    random.shuffle(aList)

    print aList

    random.sample(aList, 2)

    print aList


print timeIt('x = range(10)', number = 1000)

print timeIt('x=1', number = 10000)

print timeIt('k = map(lambda x : x*20, range(10))', number = 10000)



"""
方案2: timeit.Timer() to start timing & timeit().timeit() to end timing
"""
#引用timeit然后调用其中的timer()函数
import timeit

t1 = timeit.Timer('X=1')
print t1.timeit()

t2 = timeit.Timer('k = map(lambda x: x*10, range(10))')
t2.timeit(number=10000)
t2.print_exc()


#repeat func连续3次调用timeit方法
print t2.repeat(number = 1000)


#SETUP functions in timeit
t3 = timeit.Timer('1 in alist', setup='alist=range(10)')
print t3.timeit(number=10000)


#
stmt = \
    """
    import random

    aList = range(10)

    random.shuffle(aList)

    print aList

    random.sample(aList, 2)

    print aList
    """

t4 = timeit.Timer(stmt)
print t4.timeit(number = 1000)