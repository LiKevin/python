# -*- coding: utf-8 -*-
__author__ = 'k22li'

from random import randint

"""
挂起返回出中间值并多次继续的协同程序被称为生成器，那就是 python 的生成器真正在
做的事。
"""

def simpleGen():
    yield 1
    yield 2

k = simpleGen()
#
#print generator.next()
#print generator.next()
#
## when this next() is out of iteration scope, then stopIteration exception would be triggerred
#print generator.next()
print k

"""
由于 python 的 for 循环有 next()调用和对 StopIteration 的处理，使用一个 for 循环而不是手
动迭代穿过一个生成器（或者那种事物的迭代器）总是要简洁漂亮得多。
"""
for eachItem in k:
    print eachItem


"""
我们将要创建一个带序列并从那个序列中返回一个随机元素的随机迭代器
"""
b = 0
def randListGen(aList):
    while len(aList) > 0:
#        seed = randint(0, len(aList))
        global b
        len(aList)
        print 'this is the b:', len(aList)
        yield aList.pop(randint(0, len(aList)-1))


genList = randListGen(['Kevin', 'Cathy', 'Xiang'])

for item in genList:
    print item
"""
randin(m, n) will generate the digits in range(m, n+1); so 'n' also would be one of the randseeds
"""