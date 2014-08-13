# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# 斐波那契数列，又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、……\
# 在数学上，斐波纳契数列以如下被以递归的方法定义：F0=1，F1=1，Fn=F(n-1)+F(n-2)（n>=2，n∈N*）
########################################################################################################################

def fibonacci_calculate(n):

    if 0 == n or 1 == n:
        return 1
    else:
        return fibonacci_calculate(n-2)+fibonacci_calculate(n-1)


########################################################################################################################
# test codes                                                                                                           #
########################################################################################################################
if __name__ == '__main__':

    for i in range(10):
        print(fibonacci_calculate(i))