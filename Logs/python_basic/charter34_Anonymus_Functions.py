# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose: # fixme：函数式编程！！！
#  lambda functions:  anynomus functions
#  why lambda??：
#    1. 使用Python写一些执行脚本时，使用lambda可以省去定义函数的过程，让代码更加精简。
#    2. 对于一些抽象的，不会别的地方再复用的函数，有时候给函数起个名字也是个难题，使用lambda不需要考虑命名的问题。
#    3. 使用lambda在某些时候让代码更容易理解。
#    4. Python中，也有几个定义好的全局函数方便lambda functions 使用的，他们就是filter, map, reduce。
########################################################################################################################

# demo 1:
########################################################################################################################
FOOL_LIST = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# test map functions
def _test_map_function(lst):
    expr = lambda x:  x*2+10
    return map(expr, lst)

# test filter functions
def _test_filter_function(lst):
    expr = lambda x: x % 3 == 0
    return filter(expr, lst)

# test reduce functions
def _test_reduce_function(lst):     # fixme：遍历累积运算/ two initial arguments at first beginning， then one input each
                                    # next time
    expr = lambda x, y: x + y
    return reduce(expr, lst)


# demo 2:
########################################################################################################################
# one replacement technical than "lambda functions"
# fixme：在对象遍历处理方面，其实Python的“ 列表解析 + for..in..if ” 语法已经很强大，并且在易读上胜过了lambda。
########################################################################################################################

# test via list comprehension to replace the map() functions
def _test_list_compre_to_replace_map(lst):
    return [x*2+10 for x in lst]


def _test_list_compre_to_replace_filter(lst):
    return [x for x in lst if x %3 == 0]

def _test_list_compre_to_replace_reduce(lst):
#    return [ x+y for y in lst for x in ]
    pass
    # fixme:  can't done via list comprehension?????


# demo 3:
########################################################################################################################
# broken Lambda？？？
# fixme：当匿名函数需要引用函数外部全局变量时， 需要以形参的形式在lambda函数中声明
########################################################################################################################

def _test_lambda_function_with_global_variable():
    return [(lambda n, i=i : i + n) for i in range(10)]


### following are the actually methods
fs = [(lambda n, i=i : i + n) for i in range(10)]

print fs[4](3)



########################################################################################################################
# main test codes
########################################################################################################################
if __name__ == '__main__':

    print 'filter function: '.center(80) + \
        str(_test_filter_function(FOOL_LIST))

    print 'map function: '.center(80) + \
        str(_test_map_function(FOOL_LIST))

    print 'reduce function: '.center(80) + \
        str(_test_reduce_function(FOOL_LIST))

# outputs:
#    filter function:                                   [18, 9, 24, 12, 27]
#    map function:                                      [14, 46, 28, 54, 44, 58, 26, 34, 64]
#    reduce function:                                   139


    print _test_lambda_function_with_global_variable()[3](4)

