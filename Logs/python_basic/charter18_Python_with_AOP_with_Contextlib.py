# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
#   Python核心库中的contextlib中的contextmanager来实现AOP就非常简单了，contextmanager是一个装饰器
# fixme: 如果想在with子句中加入as variable，那么这个变量接收的是yield <value>中的value
# fixme: 其实tag方法相当于是一个模板，里面的yield是用来引导执行with子句中的主体部分的，这样一个AOP功能就实现了
#######################################################################################################################

from contextlib import contextmanager

@contextmanager
def tag(name):
    print('<%s>' %name)
    yield
    print('</%s>' %name)

def function():
    print('\t here is the main test body!')

with tag('h1'):
    function()
