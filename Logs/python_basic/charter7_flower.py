# -*- coding: utf-8 -*-
__author__ = 'k22li'

#######################################################################################################################
# function implementations
# purpose is to:
#  在100~1000 之间找出所有满足条件: 各位上的数字的三次方之和等于这个数的 数字 (水仙花)
#######################################################################################################################

def figure_out_matched_case(lower_limit, upper_limit):
    for i in range(lower_limit,upper_limit):
        a = i%10
        b = i%100//10
        c = i//100
        if a**3+b**3+c**3 == i:
            print(i)

def figure_out_special_case(lower_limit, upper_limit):

    for i in range(lower_limit, upper_limit):
        i_str =  str(i)
        a, b, c = i_str
        if int(a)**3+int(b)**3+int(c)**3 == i:
            print i

#######################################################################################################################
# test code
#######################################################################################################################

if __name__ == '__main__':

    figure_out_special_case(100, 1000)
    figure_out_matched_case(100, 1000)