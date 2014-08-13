# -*- coding: utf-8 -*-
__author__ = 'k22li'


"""
（Python编程金典P92）
 和其他语言不一样，传递参数的时候，python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。实际上，这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值－－相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。

python一般内部赋值变量的话，都是传个引用变量，和C语言的传地址的概念差不多。可以用id()来查询内存地址

如果a=b的话， a和b的地址是相同的；如果只是想拷贝，那么就得用 a=b[:]。

！！！注意这一点，这可是可以引起重大错误的。。。
"""
#example 1

aStr = 'abc'
bStr = 'efg'
cStr = aStr
dStr = bStr[:]


for item in [aStr, bStr, cStr, dStr]:
    print '%s'%item, 'the id is:%d'%id(item)

"""
from this above, as the value passing among is a String type, so they are Passing via Value in actual; should be the same as数字，元组类型
"""

#example 2

aList = [1, 2]
bList = ['a', 'b']

cList = aList
dList = bList[:]

for item in [aList, bList, cList, dList]:
    print '%s'%item, 'the ID is:', id(item)

"""
由此可见，对于可变对象，以上‘＝’进行的是按引用传递，所以地址一致；而［：］进行的是按值传递，所以后者新建立了一个对象，新ｉｄ
"""

"""
可变对象：　dict, list
不可变对象：　int, str, tuple
"""
#example 3
a = 'abc'
b = 'abc'

print id(a), id(b)

