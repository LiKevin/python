# -*- coding: utf-8 -*-

__author__ = 'k22li'


'''
Conclusion:

答案是一个函数参数的默认值，仅仅在该函数定义的时候，被赋值一次。
如此，只有当函数foo()第一次被定义的时候，才讲参数bar的默认值初始化到它的默认值（即一个空的列表）。
当调用foo()的时候（不给参数bar），会继续使用bar最早初始化时的那个列表。
'''
def method_with_mutable_param_problematic(bar=[]):
    bar.append('baz')
    return bar

def method_with_mutable_param_fixed(bar=None):
    if bar is None:
        bar = []
    bar.append('baz')
    return  bar


if __name__ == '__main__':

    ################ problematic methods calling #####################
#    print method_with_mutable_param()
#    # output:  ['baz']
#
#    print method_with_mutable_param()
#    # output:  ['baz', 'baz']
#
#    print method_with_mutable_param()
#    # output:  ['baz', 'baz', 'baz']


    ################ fixed methods calling #################

    print method_with_mutable_param_fixed()
    # output: ['baz']
    print method_with_mutable_param_fixed()
    # output: ['baz']
    print method_with_mutable_param_fixed()
    # output: ['baz']


