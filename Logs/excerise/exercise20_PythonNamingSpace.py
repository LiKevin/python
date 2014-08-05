# -*- coding: utf-8 -*-
__author__ = 'k22li'

'''
Purpose;

Python的作用域解析是基于叫做LEGB（Local（本地），Enclosing（封闭），Global（全局），Built-in（内置））的规则进行操作的.

这是因为，在一个作用域里面给一个变量赋值的时候，Python自动认为这个变量是这个作用域的本地变量，并屏蔽作用域外的同名的变量。
'''

################################################################################################################
# Demo 1:

x = 10
def foo():
    try:
        x += 1
        print x
    except (ValueError, NameError) as e:
        print '*** Error Warning:  %s ***' %e

'''
output:  "*** Error Warning:  local variable 'x' referenced before assignment ***"
reason:  global "x" declaration Vs. local "x" declaration
'''



################################################################################################################
# Demo 2:

def outer_foo():

    x = 10

    def inner_foo():
        try:
            x += 10
            print 'The Value of "x" from the inner embeded method is: %s' %x
        except  (NameError, ValueError) as e:
            print '*** Error Warning from the inner method calling:  %s ***' %e
            pass

    inner_foo()

'''
output:  *** Error Warning from the inner method calling:  local variable 'x' referenced before assignment ***
reason:  outer local variable "x" isn't recognized by the inner method calling
'''


################################################################################################################
# Demo 3:

def outer_foo_with_local_declaration():

    x = 10

    def inner_foo():
        try:
            global x    # with this declaration, the outter "x" definition could be used for the innner methods
            x += 10
            print 'The Value of "x" from the inner embeded method is: %s' %x
        except  (NameError, ValueError) as e:
            print '*** Error Warning from the inner method calling:  %s ***' %e
            pass

    inner_foo()

'''
output: The Value of "x" from the inner embeded method is: 20
reason: with this declaration, the outter "x" definition could be used for the innner methods
'''


if __name__ == '__main__':

    foo()

    outer_foo()

    outer_foo_with_local_declaration()