# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
要求设计一个函数，输入一个给定的整数数组A[0],A[1],...,A[N-1],返回该数组中离平均值偏差最大的数字,
即求数字A[P](0<=P<N),使得|A[P]-avg|最大，其中avg为数组平均值，avg=(A[0]+A[1]+...+A[N-1])/N,
例如:  给定数组[0,1,1,3,10] 该数组平均值为  0+1+1+3+10/5=3；数字|10-3|为7，为最大，因此函数返回10
'''

def get_most_far_item_from_average(aList):

    if len(aList) <= 1:
        return aList
    average = sum(aList)/len(aList)
#    average = average(aList)
    aList.sort()

    return ((aList[0] + aList[-1])/2 < average and aList[0] or aList[-1], average)


if __name__ == '__main__':

    list_a = [1, 3, 5, 7, 9, 2, 4 ,5, 10, 23, -3]

    print get_most_far_item_from_average(list_a)
