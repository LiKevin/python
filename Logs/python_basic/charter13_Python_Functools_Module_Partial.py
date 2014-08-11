# -*- coding: utf-8 -*-
__author__ = 'k22li'
######################################################################################################################
# function implementations
# purpose is to:
#   Python的functools模块
# fixme: 首先是partial函数，它可以重新绑定函数的可选参数，生成一个callable的partial对象
#######################################################################################################################
import functools

# demo 1
#######################################################################################################################
def int_base_update_closure():
    # closure method to implement this binding of the arguments
    def int16(input):
        return int(input, base=16)

    return int16

# demo 2
#######################################################################################################################
def int_base_partial(*arg):
    # modify the base of the "int()" function via "functools.partial()" methods;
    # @arguments:  function name to modify, argument_dict
    # @returns:     new function after modifications
    int2 = functools.partial(int, base=2)   #fixme: 动态绑定 base参数 给“int” function； 以后调用int时默认参数改为base
    return int2(*arg)


# demo 3

def int_base_wraps(*arg):
    int2  = functools.wraps(int)
    return int2(*arg)

#######################################################################################################################
# test codes
#######################################################################################################################
if __name__ == '__main__':

#    test_method()

    # demo 1 testing:
    ###################################################################################################################
    new_int = int_base_update_closure()
    print new_int('ff')
    #output:
    # 255


    # demo 2 testing:
    ###################################################################################################################
    print int_base_partial('11')
    #output:
    # 3

    print int('12')
