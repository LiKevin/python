# -*- coding: utf-8 -*-
__author__ = 'k22li'

"""
python的set和其他语言类似, 是一个 基本功能包括关系测试和消除重复元素.
集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.
"""

# 案例1 set 对list对象的操作
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket) # create a set without duplicates

#set 用作list元素去重,order preserving。 但set的直接返回值是set实例，需要通过list（）重新转换成list变量
print fruit, isinstance(fruit, set), list(fruit)

#set 实例可以用作关系测试
print 'orange' in fruit #True

#案例2 set 对string对象的操作
a = set('abracadabra')
b = set('alacazam')

# set 可以直接对str对象操作，转换成list-set 对象并且去除其中重复内容
print a, '\n', b # 找出string中出现的唯一的字符集 #set(['a', 'c', 'z', 'm', 'l'])
print ''.join(a) #重新转换为字符串 #arbcds

#取出在a中出现但没有在B中存在的字符集
print a-b #set(['r', 'b', 'd'])

#打印出a或者b中出现过的字符集
print a | b #set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])

#打印出a和b共有的字符集
print a&b #set(['a', 'c'])