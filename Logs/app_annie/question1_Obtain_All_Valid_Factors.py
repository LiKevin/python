# -*- coding:  utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
Question:
求一个整数的因子个数，比如24的因子个数有1，2，3，4，6，8，12，24，函数返回8，
要按最差时间复杂度根号N来算，还有一个最差空间复杂度没记住
'''
def finding_factors(x):
    return [ i for i in range(x+1)[1:] if (x % i) == 0 ]


if __name__ == '__main__':

    for k in range(4, 24):
        print 'Factors for %s: %s' %(k, finding_factors(k))

