# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpoes:
# work out the usage of the "__all__" and "__slot__" arguments from a module
# fixme: 1) __all__可用于模块导入时限制; 被导入模块若定义了__all__属性, 则只有all内指定的属性、方法、类可被导入;
# fixme:    若没定义，则模块内的所有将被导入 (及定义ｍｏｄｕｌｅ暴露给外面的接口）
# fixme: 2) __slots__用于限定类属性; 在类外部（非本模块内）实例的调用时，只允许调用在 "__slots__"中声明的方法及属性；
########################################################################################################################

# demo 1
########################################################################################################################
from repr import *  #fixme: for "import *" only acceptable in the module level, unacceptable in any class/ methods level

# test codes 1
def _test__all__():
    try:
        print _possibly_sorted
    except NameError, err:
        print('Failed to import method: %s;  reason: %s' %('_possibly_sorted', err))

    print repr

# output:
# Failed to import method: _possibly_sorted;  reason: name '_possibly_sorted' is not defined
# <bound method Repr.repr of <repr.Repr instance at 0x000000000241A9C8>>


# demo ２
########################################################################################################################
# 即从object继承下来的类有一个变量是__slots__，slots的作用是阻止在实例化类时为实例分配dict，
# fixme: 默认情况下每个类都会有一个dict,通过__dict__访问，这个dict维护了这个实例的所有属性；
# fixme：实例的dict只保持实例的变量，对于类的属性是不保存的，类的属性包括变量和函数。
# 由于每次实例化一个类都要分配一个新的dict，因此存在空间的浪费，因此有了slots，当定义了slots后，slots中定义的变量变成了类的描述符，
# fixme: 相当于java，c++中的成员变量声明，类的实例只能拥有这些个变量，而不在有dict，因此也就不能在增加新的变量
########################################################################################################################
class A(object):
    __slots__ = ['x', 'name', 'age', 'sex', '_class']  #用于限定类的实例不可有其他之外的属性

    x = '3' # fixme:  类的成员变量
    y = '4' # fixme:  类的成员变量

    def __init__(self, name='kevin', sex='male', age=31):
        self.name = name    #fixme: 类变量
        self.sex = sex    #fixme: 类变量
        self.age = age    #fixme: 类变量

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

# test codes 2
def _test__slots__():

    a = A()

    #case 1, try to print out the "__dict__" for the new instance
    try:    #fixme:  被__slots__限定的类的实例不能有__dict__ 属性， 不能附加新的attribute
        print a.__dict__
    except AttributeError, err:
        print '>>> Warning: {}'.format(err)

    # try to assign new value to A() instance a.name which has been pre-defined in __slots__
    a.name = 'Cathy'    # successful

    #case 2, try to declare new variable to A() instance a.grade which was not included in __slots__
    try:
        a.grade = 'A'   # was unsuccessful; because of the "grade" attr was not accepted
    except AttributeError, err:
        print '>>> Warning: {}'.format(err)

    # acceptable variables...
    a._class = 'junior'
    print a._class

    #case 3, 尝试修改类的成员变量； 在__slots__中有声明
    try:
        a.x = 6     # fixme:  一旦类成员变量被__slots__声明，那末这个(所有的: x, y)成员变量只能是read-only 了
    except  AttributeError, err:
        print '{}'.format(err)

    print a.x

    #case 4, 尝试修改类的成员变量； 在__slots__中没有声明
    try:
        a.y  = 8    # fixme:  一旦类成员变量被__slots__声明，那末这个(所有的: x, y)成员变量只能是read-only 了, 即时没有
                    # 在slots中声明
    except AttributeError, err:
        print '{}'.format(err)

    print a.y
#    print a.__dict__

########################################################################################################################
# test codes
########################################################################################################################

if __name__ == '__main__':
    # test via test tools
    _test__all__()

    _test__slots__()
