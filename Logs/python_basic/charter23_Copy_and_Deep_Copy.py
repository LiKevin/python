# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
# fixme: copy模块包括创建复合对象(包括列表、元组、字典和用户定义对象的实例)的深浅复制的函数
# fixme: 对于那些不可修改的对象(string, 数字, 元组)，因为你不用担心修改他们。复制不复制也就没有什么大的意义了。
# fixme: 对于内置类型，函数copy()并不经常使用。而是使用诸如list(x), dict(x), set(x)等调用方式来创建x的浅复制，
# 要知道像这样直接使用类型名显然比使用copy()快很多。但是它们达到的效果是一样的。
# fixme: 判断对象之间是否是拷贝，可以使用is运算符来确定; (that's also why "None" only comparable with "is"????)
# 需要注意的是：
# (1)  copy模块用于像整数和字符串这样的简单类型，不过很少需要这么做。
# (2)   这些复制函数无法与模块、类对象、函数、方法、回溯、栈帧、文件、套接字和其他类似类型同时工作。
# 如果不能复制对象，则会引发copy.error异常。

# 如果类实现了pickle模块所用的方法__getstate__()和__setstate__()，那么copy模块将使用这些方法来创建副本。，
# 但是通过实现方法__copy__(self)和__deepcopy__(self, visit),类就可以实现自定义的复制方法，这两个方法分别实现了浅复制和深复制操作。
# fixme: __deepcopy__()方法必须使用字典visit，用来在复制过程中跟踪前面遇到的对象。 ????
########################################################################################################################

# demo 1
########################################################################################################################
def cmp_numbers():
    a = 1
    b = 1
    print 'int comparation: %s' %(a is b)
    print id(a)

    a = 1.1
    b = 1.1
    print 'float comparation: %s' %(a is b)

# demo 2
########################################################################################################################
def cmp_strings():
    a = 'abc'
    b = 'abc'
    print 'str comparation: %s' %(a is b)

# demo 3
########################################################################################################################
def cmp_tuple():
    a = (1, 2, 3)
    b = (1, 2, 3)
    c = a   # same id(a) than id(c); also the same ids for each members inside

    print 'tuple comparation: %s' %(a is b)
    print 'tuple comparation: %s' %(a is c)
    for item in a:
        print id(item)  # same id than a[0], as well as "a" from "cmp_numbers()"

    print id(a) # diff id(a) than id(b); but the ids of the item inside are equals
    print id(b) # diff id(a) than id(b); but the ids of the item inside are equals
    print id(b[0])  # same id than a[0], as well as "a" from "cmp_numbers()"

# demo 4
########################################################################################################################
def cmp_list_demo1():
    '''
    demo of the "slight copy" methods for the list data types
    '''
    import copy     # fixme: working scope is the method inside, while outside of the method, was not able to refer
    a  = ['a', 'b', 'c']
    b = a       # the same list object returned; both reference to the same values
    c = copy.copy(a)        # false, new list obj created and returned
    d = list(a)     # false, new list obj created and returned

    print 'list comparison: (=): %s' %(a is b)
    print 'list comparison: (copy) : %s' %(a is c)
    print 'list comparison: (new list): %s' %(a is d)

# demo 4
########################################################################################################################
def cmp_list_demo2():
    '''
    demo the list datatype while the copying, the weakness existing with the "slight copy"
    '''
    import copy

    a = [['a'],[1],[2.0]]
    b = copy.copy(a)
    c = a
    a[0].append('b')

    print 'list comparison: (list embedded): %s' %(a is b)  # list comparison: (list embedded): False
    print 'list comparison: (list embedded): %s' %(a is c)  # list comparison: (list embedded): True
    print 'sublist comparison: a[0] vs b[0]: %s' %(a[0] is b[0])    # sublist comparison: a[0] vs b[0]: True

# demo 5
########################################################################################################################
def cmp_list_demo3():
    '''
    demo the list datatype while the copying, the weakness existing with the "slight copy"
    '''
    import copy

    a = [['a'],[1],[2.0]]
    b = copy.deepcopy(a) #fixme: deepcopy is are recursive slight copy()????
    c = a
    a[0].append('b')

    print 'list comparison: (list embedded): %s' %(a is b)  # list comparison: (list embedded): False
    print 'list comparison: (list embedded): %s' %(a is c)  # list comparison: (list embedded): True
    print 'sublist comparison: a[0] vs b[0]: %s' %(a[0] is b[0])    # sublist comparison: a[0] vs b[0]: True

# demo 6
########################################################################################################################
def cmp_dict_demo():

    _deep_copy_table = d ={}

    print _deep_copy_table
    print d
    print 'dict comparison: _deep_copy_table vs d: %s' %(_deep_copy_table is d)

########################################################################################################################
# test code
########################################################################################################################
if __name__ == '__main__':

    cmp_numbers()

    cmp_strings()

    cmp_tuple()

    cmp_list_demo1()
    # outputs:
    #list comparison:  (=): True
    #list comparison: (copy): False
    #list comparison: (new list): False

    cmp_list_demo2()
    # outputs:
    #list comparison: (list embedded): False
    #list comparison: (list embedded): True
    #sublist comparison: a[0] vs b[0]: True

    cmp_list_demo3()
    # outputs:
    #list comparison: (list embedded): False
    #list comparison: (list embedded): True
    #sublist comparison: a[0] vs b[0]: False

    cmp_dict_demo()
    # outputs:
    # dict comparison: _deep_copy_table vs d: True

    print {}.get('a')   #fixme: return is "None" by default, there is no exceptions raised with Dict operating
