# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
Purpose:
常见错误6：搞不清楚在闭包（closures）中Python是怎样绑定变量的
'''
from copy import deepcopy

#########################################################################################################
# Demo 1:
def create_multipler_problematic():
    return [ lambda n : i * n for i in xrange(5)]  # 闭包实现，动态（后期）绑定
#    return [i*n for i in range(5)]  # 列表解析实现，不存在动态（后期）绑定的问题。

#########################################################################################################
# Demo 2:  problem fixed versions, i=i 形参和实参的转换
def create_multipler_fixed():
    return [ lambda n, i=i: i* n for i in xrange(5)]    # 闭包实现，动态（后期）绑定

def test_create_multiplier(func):
    for multiplied in func():
        print multiplied(2)


if __name__ == '__main__':
    ######################################### Demo 1 ###################################################
    test_create_multiplier(create_multipler_problematic)
    # output:  [8, 8, 8, 8, 8]

    ######################################### Demo 2 ###################################################
    test_create_multiplier(create_multipler_fixed)
    # output: [0, 2, 4, 6, 8]

    '''
    这是由于Python的后期绑定（late binding）机制导致的，这是指在闭包中使用的变量的值，是在内层函数被调用的时候查找的。
    因此在上面的代码中，当任一返回函数被调用的时候，i的值是在它被调用时的周围作用域中查找
    （到那时，循环已经结束了，所以i已经被赋予了它最终的值4）
    '''
