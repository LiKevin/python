# -*- coding: utf-8 -*-
__author__ = 'k22li'
########################################################################################################################
# purpose:
# try to figure out the diff between "__builtin__" & "__builtins__"
# 在Python2.X版本中，内建模块被命名为__builtin__，而到了Python3.X版本中，却更名为builtins
# fixme: 当使用内建模块中函数或其它功能时，可以直接使用，不用添加内建模块的名字;但是，如果想要向内建模块中添加一些功能，
# fixme: 以便在任何函数中都能直接使用而不 用再进行import，这时，就要导入内建模块，在内建模块的命名空间(即__dict__字典属性)中
# fixme: 添加该功能。在导入时，如果是Python2.X 版本，就要导入__builtin__模块;如果是Python3.X版本，就要导入builtins模块
########################################################################################################################


# demo 1:  fixme: Python2.X中，向内建模块添加 一个函数(该函数打印“hello, world”)
########################################################################################################################

def greeting(name='kevin'):

    print '>>> Hey, good morning %s !' %name

# test newly adding one function to __builtin__
def _test_add_new_func_to_builtin():
    # update the __builtin__ with the new defines -- {'greet' :  greeting}
    import __builtin__
    __builtin__.__dict__.update({'greet' : greeting})
    # calling the local func defines
    greeting('Boush')
    # calling the newly added built-ins
    greet('cathy')

#    del __builtin__

# outputs:
#    >>> Hey, good morning Boush !
#    >>> Hey, good morning cathy !

# demo 2:  fixme: 无论任何地方要想使用内建模块，都必须在该位置所处的作用域中导入__builtin__内建模块;
#          fixme: 而对于__builtins__却不用导入，它在任何模块都直接可见
########################################################################################################################


def _test_importing_rules():

    print '>>> check the availability of "__builtins__": %s' %(__builtins__)

    def __test_builtin(module='__builtin__'):
        try:
            print '>>> check the availability of "%s": %s' %(module, eval(module))
        except (UnboundLocalError, NameError), err:
            print ' ERROR: %s '.center(100, '-') %err

    __test_builtin("__builtin__")
    import __builtin__
    __test_builtin("__builtin__")
    print(__builtin__)

########################################################################################################################
#    1】 在主模块__main__中：
#       __builtins__是对内建模块__builtin__本身的引用，即__builtins__完全等价于__builtin__，二者完全是一个东西，不分彼此。
#       它在任何地方都可见，即在任何地方都可使用它。此时，__builtins__的类型是模块类型。
#       __builtin__仅仅在导入它时才可见。哪个作用域中使用__builtin__，哪个作用域就要导入它(导入仅仅是让__builitin__标识符在该作用域
#       内可见)。一般都是在模块的顶层(即模块的全局作用域)导入__builtin__，这样，其后的任何作用域可通过标识符向上查找来引用 __builtin__。
#    2】在非__main__模块中：
#       __builtins__仅是对__builtin__.__dict__的引用，而非__builtin__本身。它在任何地方都可见。此时__builtins__的类型是字典。
########################################################################################################################


########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':

    _test_add_new_func_to_builtin()
#    print __builtins__
    _test_importing_rules()