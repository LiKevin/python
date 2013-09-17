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

#打印出a中出现b中没有的元素，或者a中不存在b中存在的项目
print a^b #set(['b', 'd', 'm', 'l', 'r', 'z'])

"""
请 注意：union(), intersection(), difference() 和 symmetric_difference() 的非运算符（non-operator，就是形如 s.union()这样的）版本将会接受任何 iterable 作为参数。
相反，它们的运算符版本（operator based counterparts）要求参数必须是 sets。
这样可以避免潜在的错误，如：为了更可读而使用 set('abc') & 'cbs' 来替代 set('abc').intersection('cbs')。
从 2.3.1 版本中做的更改：以前所有参数都必须是 sets。
另 外，Set 和 ImmutableSet 两者都支持 set 与 set 之间的比较。
两个 sets 在也只有在这种情况下是相等的：每一个 set 中的元素都是另一个中的元素（二者互为subset）。
一个 set 比另一个 set 小，只有在第一个 set 是第二个 set 的 subset 时（是一个 subset，但是并不相等）。
一个 set 比另一个 set 大，只有在第一个 set 是第二个 set 的 superset 时（是一个 superset，但是并不相等）。
子 set 和相等比较并不产生完整的排序功能。例如：任意两个 sets 都不相等也不互为子 set，因此以下的运算都会返回 False：a<b, a==b, 或者a>b。因此，sets 不提供 __cmp__ 方法。"""

print len(a-b)


#从 set “s”中删除元素 x, 如果不存在则引发 KeyError
a.remove('a')
print a

#如果在 set “s”中存在元素 x, 则删除
a.discard('a')
print a

#删除并且返回 set “s”中的一个不确定的元素, 如果为空则引发 KeyError
a.pop()
print a

#删除 set “s”中的所有元素
a.clear()
print a

#向 set “s”中增加元素 x
a.add('abc')
print a