# -*- coding: utf-8 -*-
__author__ = 'k22li'


#
#for item in dir(dict):
#    print item
"""
试验如何进行按值及引用传递，在字典类型的变量中
"""

aDict = {'a':1, 'b':2}

#对于字典类型来说，如果需要按值传递的话，用ｃｏｐｙ字段
bDict = aDict.copy()
print id(bDict), id(aDict) #35894024 31139048

#以下说明对于可变类型来说，进行的是按引用传递
bDict = aDict
print id(bDict), id(aDict) #31139048 31139048


"""
fromkeys, 可以将字典中全部ｋｅｙ快速负成统一值；　ｆｒｏｍｋｅｙｓ将从原字典中即成所有的ｋｅｙ，然后以第二个参数初始化所有ｋｅｙｓ
"""
cDict = dict.fromkeys(aDict, 'newValue')
print cDict #{'a': 'newValue', 'b': 'newValue'}


"""
对于dict object的update函数做下代码场景和学习笔记
"""
dic = {"A":"a", "B":"b"}
# print the original dict object, output {"A":"a", "B":"b"}
print dic
# update the given key to invoke the another value if the given key exists
dic.update(A="Aa")
# output {'A': 'Aa', 'B': 'b'}
print dic


# if the the given key is not existed, add this key/value pair in the target dict object
dic.update(C="C")
# output {'A': 'Aa', 'C': 'C', 'B': 'b'}
print dic

#if the param for update is another Dict
#这种场景下对于ａＤｉｃ中每一对ｋｅｙ，ｖａｌｕｅ分别在现有ｄｉｃｔ中实现替换
aDic = {'A':1, 'D':2, 'C':3}
dic.update(aDic)
print dic