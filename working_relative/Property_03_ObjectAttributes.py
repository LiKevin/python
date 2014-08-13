# -*- coding: utf-8 -*-

"""
同一个对象的不同属性之间可能存在依赖关系。
当某个属性被修改时，我们希望依赖于该属性的其他属性也同时变化。
这时，我们不能通过__dict__的方式来静态的储存属性。Python提供了多种即时生成属性的方法。
其中一种称为特性(property)。特性是特殊的属性
"""

# example 1
"""
上面的num为一个数字，而neg为一个特性，用来表示数字的负数。当一个数字确定的时候，它的负数总是确定的；而当我们修改一个数的负数时，它本身的值也应该变化。
这两点由getNeg和setNeg来实现。而delNeg表示的是，如果删除特性neg，那么应该执行的操作是删除属性value。
property()的最后一个参数("I'm negative")为特性negative的说明文档。
"""
class num(object):

    def __init__(self, value):
        self.value = value

    def getNeg(self):
        return -self.value

    def setNeg(self, value):
        self.value = -value

    def delNeg(self):
        print('Value also being deleted!')
        del self.value

    neg = property(getNeg, setNeg, delNeg, 'I am negative')


x = num(1)
print x.neg #call this num.getNeg() method

x.neg = -22
print x.value #check the change on the item will also impact the value in the other functions

del x.neg #this will truely remove this per attributes of class as well

try:
    print x.value
except AttributeError, err:
    print(err)

print num.neg.__doc__


"""
特性使用内置函数property()来创建。
property()最多可以加载四个参数。前三个参数为函数，分别用于处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，可以为一个字符串，起说明作用。
"""

#example 2
"""
同一个对象的不同属性之间可能存在依赖关系。当某个属性被修改时，我们希望依赖于该属性的其他属性也同时变化。
这时，我们不能通过__dict__的方式来静态的储存属性。
Python提供了多种即时生成属性的方法。其中一种称为特性(property)。
特性是特殊的属性。比如我们为chicken类增加一个特性adult。当对象的age超过1时，adult为True；否则为False
"""
class bird(object):
    feather = True

class chicken(bird):

    fly = False
    def __init__(self, age):
        self.age = age

    def getAdult(self):
        if self.age > 2: return True
        else: return False

    def setAdult(self, age):
        self.age = age

    adult = property(getAdult, setAdult, 'This is the method to check if the chicken is adult or not')


summer = chicken(2)
print '\n*********this is alread the example 2*********\n'
print summer.adult

summer.adult = 3
print summer.adult
