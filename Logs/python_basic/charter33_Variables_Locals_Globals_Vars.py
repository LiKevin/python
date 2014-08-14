# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose;
#   is to figure out what's the working scope for each of those following 3 sub-functions:
#   1) vars()       # fixme：== locals
#   2) globals()    #fixme： 当前有效作用域的全局attrs
#   3) locals()     #fixme:  当前有效作用域内声明的所有attrs; those variables defined outside of the class/ function are
#                   fixme:   invisible to the locals

#    局部名字空间 - 特指当前函数或类的方法。如果函数定义了一个局部变量 x, 或一个参数 x，Python 将使用它，然后停止搜索。
#    全局名字空间 - 特指当前的模块。如果模块定义了一个名为 x 的变量，函数或类，Python 将使用它然后停止搜索。
#    内置名字空间 - 对每个模块都是全局的。作为最后的尝试，Python 将假设 x 是内置函数或变量。
#    如果 Python 在这些名字空间找不到 x，它将放弃查找并引发一个 NameError 异常，同时传 递 There is no variable named 'x' 这样一条信息

#
#    Python 2.2 引入了一种略有不同但重要的改变，它会影响名字空间的搜索顺序: 嵌套的作用域。
#    在 Python 2.2 版本之前，当您在一个嵌套函数 或 lambda 函数 中引用一个变量时，
#    Python 会在当前 (嵌套的或 lambda) 函数的名字空间中搜索，然后在模块的名字空间。
#    Python 2.2 将只在当前 (嵌套的或 lambda) 函数的名字空间中搜索，然后是在父函数的名字空间中搜索，接着是模块的名字空间中搜索。
#    Python 2.1 可 以两种方式工作，缺省地，按 Python 2.0 的方式工作。
#    但是您可以把下面一行代码增加到您的模块头部，使您的模块工作起来象 Python 2.2 的方式:
########################################################################################################################


# demo 1
########################################################################################################################

G_VARIABLE = 'global variables'

class test_variable_scope():

    c_variable = 'testing'

    def test_method():
        tester_a = 'Kevin'
        tester_b = 'Micheal'

        def test_method_inner():
            test_co = 'Nokia'
            test_fa = 'Moto'

        test_method_inner()
    test_method()

    print '*'*100
    print 'Values from "vars()" : %s' %vars()

    print '*'*100
    print 'Values from "globals()" : %s' %globals()
#    for ky, val in sorted(globals()['__builtins__'].items(), key= lambda x: x[1]):
#        if ky != 'copyright':
#            print ky.ljust(25, ' '), ' ---> ', val

    print '*'*100
    print 'Values from "locals()" : %s' %locals()


def _test_test_variable_scope():

    c = test_variable_scope()

    print '*'*100
    print 'Values from "vars()" : %s' %vars()

    print '*'*100
    print 'Values from "globals()" : %s' %globals()
    #    for ky, val in sorted(globals()['__builtins__'].items(), key= lambda x: x[1]):
    #        if ky != 'copyright':
    #            print ky.ljust(25, ' '), ' ---> ', val

    print '*'*100
    print 'Values from "locals()" : %s' %locals()

# outputs:  from inside of the class definitions
########################################################################################################################
#    ****************************************************************************************************
#    Values from "vars()" : {'c_variable': 'testing', '__module__': '__main__', 'test_method': \
#                               <function test_method at 0x00000000024BC2E8>}
#    ****************************************************************************************************
#    Values from "globals()" : {'__builtins__': <module '__builtin__' (built-in)>,
#                               '__file__': 'C:/Users/k22li/workspace/gitHub/Python_Projects/python/Logs/python_basic/charter33_Variables_Locals_Globals_Vars.py',
#                               '__author__': 'k22li',
#                               'G_VARIABLE': 'global variables',
#                               '__name__': '__main__',
#                               '__package__': None,
#                               '__doc__': None}
#    ****************************************************************************************************
#    Values from "locals()" : {'c_variable': 'testing', '__module__': '__main__', 'test_method':
#                               <function test_method at 0x00000000024BC2E8>}

# outputs:  from outside of the class definitions; from the modules
########################################################################################################################

#    ****************************************************************************************************
#    Values from "vars()" : {'test_variable_scope': <class __main__.test_variable_scope at 0x00000000020EC888>,
#                           'c': <__main__.test_variable_scope instance at 0x000000000257BD48>,
#                           '__builtins__': <module '__builtin__' (built-in)>,
#                           '__file__': 'C:/Users/k22li/workspace/gitHub/Python_Projects/python/Logs/python_basic/charter33_Variables_Locals_Globals_Vars.py',
#                           '__author__': 'k22li',
#                           'G_VARIABLE': 'global variables',
#                           '__name__': '__main__',
#                           '__package__': None,
#                           '__doc__': None}
#    ****************************************************************************************************
#    Values from "globals()" : {'test_variable_scope': <class __main__.test_variable_scope at 0x00000000020EC888>,
#                               'c': <__main__.test_variable_scope instance at 0x000000000257BD48>,
#                               '__builtins__': <module '__builtin__' (built-in)>,
#                               '__file__': 'C:/Users/k22li/workspace/gitHub/Python_Projects/python/Logs/python_basic/charter33_Variables_Locals_Globals_Vars.py',
#                               '__author__': 'k22li',
#                               'G_VARIABLE': 'global variables',
#                               '__name__': '__main__',
#                               '__package__': None,
#                               '__doc__': None}
#    ****************************************************************************************************
#    Values from "locals()" : {'test_variable_scope': <class __main__.test_variable_scope at 0x00000000020EC888>,
#                               'c': <__main__.test_variable_scope instance at 0x000000000257BD48>,
#                               '__builtins__': <module '__builtin__' (built-in)>,
#                               '__file__': 'C:/Users/k22li/workspace/gitHub/Python_Projects/python/Logs/python_basic/charter33_Variables_Locals_Globals_Vars.py',
#                               '__author__': 'k22li',
#                               'G_VARIABLE': 'global variables',
#                               '__name__': '__main__',
#                               '__package__': None,
#                               '__doc__': None}



# demo 2:  try to change the locals() & globals() dynamically
########################################################################################################################
# Conclusion:
# fixme:  locals() is not changable through locals() dictionary updating; while globals() are modifiable through this
########################################################################################################################

G_Z = 7

def foo_2(arg):

    x = 1
    print locals()
#    setattr(locals(), 'x', 4)
    locals()['x'] =  4
    print 'x = %s' %x
    # global variables
    print 'G_Z= %s' %G_Z

#    setattr(globals(), 'G_Z', 8)
    globals()['G_Z'] = 8
    print 'G_Z= %s' %G_Z

# outputs:
#    Values from "locals()" : {'c_variable': 'testing', '__module__': '__main__', 'test_method': <function test_method at 0x000000000241C358>}
#    {'x': 1, 'arg': 3}
#    x = 1
#    G_Z= 7
#    G_Z= 8
#    G_Z= 8


def _test_foo_2():
    foo_2(3)




########################################################################################################################
# test codes, main functions
########################################################################################################################

if __name__ == '__main__':
#    _test_test_variable_scope()

    _test_foo_2()
    # again to double confirm this changed global values
    print 'G_Z= %s' %G_Z

# fixme: what's more:
# 回想一下 from module import 和 import module 之间的不同。使用 import module，模块自身被导入，但是它保持着自已的名字空间，
# 这就是为什么您需要使用模块名来访问它的函数或属性: module.function 的原因。但是使用 from module import，
# 实际上是从另一个模块中将指定的函数和属性导入到您自己的名字空间，这就是为什么您可以直接访问它们却不需要引用它们所来源的模块的原因。
# 使用 globals 函数，您会真切地看到这一切的发生。