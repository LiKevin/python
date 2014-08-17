# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose: # fixme：函数式编程！！！
# fixme: 生成器表达式 (expr for iter_var in iterable)  vs (expr for iter_var in iterable if cond_expr)
# fixme: 生成器表达式是在python2.4中引入的，当序列过长， 而每次只需要获取一个元素时，应当考虑使用生成器表达式而不是列表解析。
# fixme: 生成器表达式的语法和列表解析一样，只不过生成器表达式是被()括起来的，而不是[]
########################################################################################################################

def _test_generator_expr():

    generator_new = (x*2 for x in range(10))
    list_new = [ x*2 for x in range(10) ]

    print 'Return of generator expr: %s'.ljust(100, '*') %generator_new
    print 'Return of list expr: %s'.ljust(100, '*') %list_new

#    print len(generator_new)    # check the length of the generators #fixme:  generator doesn't support len()

    for i in generator_new:
        print i # fixme:  normally for generators, "yeild" will stops when this StopIteration exceptions being caught
                # fixme:  internally

########################################################################################################################
#    what's more::
#    生成器表达式并不真正创建数字列表， 而是返回一个生成器，这个生成器在每次计算出一个条目后，把这个条目“产生”(yield)出来。
#    生成器表达式使用了“惰性计算”(lazy evaluation，也有翻译为“延迟求值”，我以为这种按需调用call by need的方式翻译为惰性更好一些)，
#    只有在检索时才被赋值( evaluated)，所以在列表比较长的情况下使用内存上更有效。
########################################################################################################################

if __name__ == '__main__':

    _test_generator_expr()