# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpoes:
# profile是python的标准库。可以统计程序里每一个函数的运行时间，并且提供了多样化的报表
########################################################################################################################

#  demo 1
########################################################################################################################
import sys

def test_method():
    for x in xrange(10000):
        sys.stdout.write('\r%s'%x)

import profile
profile.run('test_method()')

##outputs:
#999999         1000004 function calls in 9.086 seconds
#
#Ordered by: standard name
#
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#1    0.002    0.002    0.002    0.002 :0(setprofile)
#1000000    6.445    0.000    6.445    0.000 :0(write)
#1    0.000    0.000    9.084    9.084 <string>:1(<module>)
#1    2.639    2.639    9.084    9.084 charter27_Profile_for_Analyzing_Python_Codes_Performance.py:11(test_method)
#0    0.000             0.000          profile:0(profiler)
#1    0.000    0.000    9.086    9.086 profile:0(test_method())


#  demo 2
########################################################################################################################
# 小巧实用的瑞士军刀——timeit
#    如果我们某天心血来潮，想要向list里append一个元素需要多少时间或者想知道抛出一个异常要多少时间，那使用profile就好像用牛刀杀鸡了
########################################################################################################################
import timeit

k = timeit.Timer('[].append("a")')
#k = timeit.Timer
print k.timeit(number=1000)
