# -*- coding: utf-8 -*-
__author__ = 'k22li'

# 将数组 a= [31, 41, 59, 26, 41, 58] 使用insert-sort方式重新排序
a = [31, 41, 59, 26, 41, 58, 60, 91, 12, 11, 6, 8]
alen = len(a)

# 2.1-1, 将以上序列按非降序排列

def sortAsc(aList):
    for i in range(1,len(aList)):
        key = aList[i]
        j = i-1
        while j>=0 and key < aList[j]:
            aList[j+1] = aList[j]
#            aList[j] = key
            j = j-1
        else:
            aList[j+1] = key
    print 'Now the a is sorted according to the ASC order as following: \n', aList

#2. 1-2, 将以上序列按非升序顺序排列

def sortDsc(aList):
    for i in range(1, len(aList)):
        key = aList[i]
        j = i-1
        while j>=0 and key > aList[j]:
            aList[j+1] = aList[j]
            aList[j] = key
            j = j-1
        else:
            aList[j+1] = key

    print 'Now the a is sorted according to the DSC order as following: \n', aList

#2. 1-3, input: aList and any value 'V',
#       output: for a given value 'i' to let a[i] == 'v', and return i = nil if v isn't in aList
# 二分法对于查找可能更有效，暂时保留！！！

def lookForValue(aList, tarVal):
    ind = 0
    while ind < alen: #先判断然后执行，所以需要考虑末尾时，用alen 而不是alen-1
        if tarVal == aList[ind]: #FIXME:  对于python解法需要考虑如何实现多个重复值出现时如何提供准确的index
            return ind
        ind += 1
    else:
        return None

#   python code: FIXME: 对于python解法需要考虑如何实现多个重复值出现时如何提供准确的index
#    if tarVal in aList:
#        return aList.index(tarVal)
#    else:
#        return None

def print_format(*arg):
    if not len(arg)>0:
        print '\n', '*'*60
    else:
        for item in arg:
            print 'The value is: %s'%item

if __name__ == '__main__':
#    print_format()
#    sortAsc(a)
#    print_format()
#    sortDsc(a)
#    print_format()

    for item in a:
        indexFind = lookForValue(a, item)
        print_format(item)
        print_format(indexFind)

