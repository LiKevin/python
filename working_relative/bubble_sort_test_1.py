#-*-coding: utf-8 -*-
__author__ = 'k22li'


#冒泡排序法通过重复交换相邻两个反序元素最终调整好整个序列的过程
from random import randint

testList = [randint(0, 99) for i in range(50)]
lenList = len(testList)


def bubbleSort(aList):
    for i in range(lenList):
        for j in range(lenList-1, i, -1):
            if aList[j]<aList[j-1]:
                temp = aList[j-1]
                aList[j-1] = aList[j]
                aList[j] = temp
            j -= 1
        i += 1
    return aList

if __name__ == '__main__':
    print testList
    sortedList = bubbleSort(testList)
    print sortedList
