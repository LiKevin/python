# -*- coding: utf-8 -*-

__author__ = 'k22li'
import random

def testFunction10Times(func ='', *arg):
    for i in range(10):
        print 'The %d \'s result of %s calling is:'%(i, func)
        print func(*arg)

"""
random.random
random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
"""

tFunc = random.random
testFunction10Times(tFunc)



"""
random.uniform
random.uniform的函数原型为：random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。"""

tFunc = random.uniform
testFunction10Times(tFunc, 2, 3)


"""
random.randint
random.randint()的函数原型为：random.randint(a, b)，用于生成一个指定范围内的整数。
其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b"""

tFunc = random.randint
testFunction10Times(tFunc, 2, 10)

"""
random.randrange
random.randrange的函数原型为：random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。"""

tFunc = random.randrange
testFunction10Times(tFunc, 10, 100, 2)

"""
random.shuffle
random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱。"""

tFunc = random.shuffle

tList = ['this', 'is', 'an', 'random', 'shuffle', 'function', 'test']

#testFunction10Times(tFunc, tList)
#print tList

"""
random.sample
random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。"""

tFunc = random.sample
testFunction10Times(tFunc, tList, 3)
