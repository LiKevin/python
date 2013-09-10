# -*- coding: utf-8 -*-
__author__ = 'k22li'
from sets import Set

"""
题目: 如何去除list中的dup 元素
方案1: 列表解析方案
"""
# order preserving
aList = ['a', 'b', 'c', 'd', 'a', 'c']
[aList.remove(item) for item in aList if aList.count(item)>1] #返回值为None

print aList

"""
方案2： 利用字典的keys（）method可以自动去重
"""
#字典的keys（）method会自动去重
#NOT order preserving

def viaDict(seq):
    temDic = {}
    for value in seq:
        temDic[value] = 1
    return temDic.keys()

"""
方案3： 对原列表进行遍历
"""
#order preserving
def walkThrough(seq):
    newList = []
    for item in seq:
        if not item in newList:
            newList.append(item)

    return newList

"""
python的set和其他语言类似, 是一个 基本功能包括关系测试和消除重复元素.
集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.
from sets import Set
"""
#order perservings
def setList(seq):
    set = Set(seq)
    return list(set)


"""
"""
def listAndDict(seq, idFun = None):
    if not len(seq):
        return []
    else:
        if idFun == None:
            def idFun(x): return x

        tempDic = {}
        refreshResult = []

        for item in seq:
            marker = idFun(item)
            if not tempDic.has_key(marker):
                tempDic[item] = 1
                refreshResult.append(item)
            else:
                continue

    return refreshResult

if __name__ == '__main__':
    newList1 = viaDict(aList)
    print newList1
#    try with 'walkThrough'
    newList2 = walkThrough(aList)
    print newList2
#    try with 'setList'
    newList3 = setList(aList)
    print newList3
#   try with 'listAndDict
    newList4 = listAndDict(aList,)
    print newList4
#   what's more supported by the 'listAndDic' methods,
"""
Clearly "listAndDict" is the "best" solution.
Not only is it really really fast;
it's also order preserving and supports an optional transform function which makes it possible to do this:
"""
    bList = list('ABCdeDEFG')
    newList5 = listAndDict(bList, lambda x : x.lower())
    print newList5