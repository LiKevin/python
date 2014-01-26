#-*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = """
题目：现在有两个排好序的整数数组，a[N]和b[N]，要求写一个函数，功能为返回两个数组中第N大数和第N+1大数的中间值，即求解两者的和除以2。

函数原型：double getMedian( int a[], int b[] );

下面，我们先来分析一个类似的问题，假设a和b都是升序的，分别有n1和n2个元素，求两个数组合并后第k大元素值。

分别取两个数组中间索引的数，a[x]和b[y]，比较两个数的大小：

if( a[x] <= a[y] )

——————————————————————————————————————————————————————————————

如果k <= x+y+1，则可以判断出b[y]以及b[y]后面的元素都可以排除在外，减小搜索规模。

如果k  > x+y+1，则可以判断出a数组的前半部分元素都不符合条件，减少a一半的搜索规模。

该算法利用了递归的思想，结束条件是：

a中元素排除出去，则选择b中得第k大元素；

b中元素全部排除，选择a中第k大元素。

——————————————————————————————————————————————————————————————
"""
import random

def generateTestList(length = 0):
    tmpList = []
    if length:
        for i in range(length):
            tmpList.append(random.randint(1, 10))
    return tmpList

def getMedianFigure(listA, listB, n):
    listA.extend(listB)
    listA.sort()
    return listA[n-1], listA


if __name__ == '__main__':
    listA = generateTestList(10)
    listB = generateTestList(10)
    print getMedianFigure(listA, listB, 10)

