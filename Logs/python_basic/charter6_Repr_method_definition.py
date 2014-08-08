# -*- coding: utf-8 -*-
__author__ = 'k22li'

#######################################################################################################################
# function implementations
# purpose is to:
#   implement a method with which to define the calculations of encrypting a strings
#######################################################################################################################
class A(object):

    def __init__(self):

        print('>>> initialization of the class ...')

    def __str__(self):
        self.debugging =  '>>> This is the debugging info from the __str__() methods..'
        return self.debugging

    def __repr__(self):
        self.debugging =  '>>> This is the debugging info from the __repr__() methods...'
        return self.debugging


#######################################################################################################################
# test codes
#######################################################################################################################
if __name__ == '__main__':

    # demo 1
    ###################################################################################################################
    print repr(A)
    # output:
    # <class '__main__.A'>, still the "object" class's __repr__() built-in method being called


    # demo 2
    ###################################################################################################################
    a = A()
    print repr(a)
    # output:
    # >>> This is the debugging info from the __repr__() methods...  now the the self defined the info being displayed; \
    # purpose is to providing enough debugging info of this class.

    # demo 3
    ###################################################################################################################
    print A.__repr__(a)
    # output:
    # >>> This is the debugging info from the __repr__() methods...  now the the self defined the info being displayed; \
    # purpose is to providing enough debugging info of this class.


    # demo 4
    ###################################################################################################################
    print a
    # output:
    # >>> This is the debugging info from the __str__() methods...
    # but simply calling this object/class, by default would be the __str__() returns being provided;
    #Fixme: but "__repr__()" would be called instead if without "__str__()" being defined

    # demo 5
    ###################################################################################################################
    print '%s' %a
    # output:
    # >>> This is the debugging info from the __str__() methods...
    # but simply calling this object/class, by default would be the __str__() returns being provided; "print()" method \
    # will call for the "__str__()" methods defined in the object/ class by default;
    #Fixme: but "__repr__()" would be called instead if without "__str__()" being defined

    # demo 6
    ###################################################################################################################
    print '%r' %a
    # output:
    # >>> This is the debugging info from the __repr__() methods...
    # by calling this "a" instance int he vorbose window, then by default this __repr__() returns displayed;
    # also, by formatting the output to "%r" would be also by default would be the __repr__() returns being provided;
    # Fixme:  also the desired state is that "eval(repr(object))" could regenerate the same class/ object/ instance;
    # which was the key difference between __str__ & __repr__

# More info:
# 内建函数str()和repr() (representation，表达，表示)或反引号操作符（``）可以方便地以字符串的方式获取对象的内容、类型、数值属性等信息。
# str()函数得到的字符串可读性好（故被print调用），
# 而repr()函数得到的字符串通常可以用来重新获得该对象，通常情况下 obj==eval(repr(obj)) 这个等式是成立的。
# 这两个函数接受一个对象作为其参数，返回适当的字符串。
# 事实上repr()和``做一样的事情，返回一个对象的“官方”字符串表示。
# Fixme: 其结果绝大多数情况下（不是所有）可以通过求值运算（内建函数eval()）重新得到该对象。
# Fixme: str()则不同，它生成一个对象的可读性好的字符串表示，结果通常无法用eval()求值，但适合print输出。
# Fixme: 为什么有了repr（）还需要``？
# Fixme: Python中，有的操作符和函数是做同样的事情，原因是某些场合下函数会比操作符更适合使用，比如函数对象可作为参数传递。
# 双星号（＊＊）乘方运算和pow()内建函数都返回x的y次方.



