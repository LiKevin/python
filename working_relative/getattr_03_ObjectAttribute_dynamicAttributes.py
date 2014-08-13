# -*- coding: utf-8 -*-

"""
我们可以用__getattr__(self, name)来查询即时生成的属性。
当我们查询一个属性时，如果通过__dict__方法无法找到该属性，那么Python会调用对象的__getattr__方法，来即时生成该属性。
"""

#example 1

class bird(object):
    feather = True

class chicken(bird):

    fly = False

    def __init__(self, age):
        self.age = age

    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 2: return True
            else:  return False
        else:
            raise AttributeError(name)

summer = chicken(2)

print summer.adult

print summer.age

print summer.feature

print summer.test

"""
每个特性需要有自己的处理函数，而__getattr__可以将所有的即时生成属性放在同一个函数中处理。
__getattr__可以根据函数名区别处理不同的属性。比如上面我们查询属性名male的时候，raise AttributeError。
(Python中还有一个__getattribute__特殊方法，用于查询任意属性。__getattr__只能用来查询不在__dict__系统中的属性)
__setattr__(self, name, value)和__delattr__(self, name)可用于修改和删除属性。它们的应用面更广，可用于任意属性。
"""