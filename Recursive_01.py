# -*- coding: utf-8 -*-
__author__ = 'k22li'

"""
如果函数包含了对其自身的调用，该函数就是递归的。根据 Aho, Sethi, 和 Ullman, ”[a] 如
果一个新的调用能在相同过程中较早的调用结束之前开始，那么该过程就是递归的“
"""
def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n*factorial(n-1)


c = factorial(10)

print c

"""
我们现在可以看到阶乘是递归的，因为 factorial(N) = N* factorial(N-1).换句话说，为了获
得 factorial(N)的值，需要计算 factorial(N-1).而且，为了找到 factorial(N-1)，需要计算
factorial(N-2)等等。
"""

sum = 1

for i in range(1,11):
    sum = sum * i
    print sum