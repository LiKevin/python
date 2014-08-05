# -*- coding:  utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
在一个数列中找到差值最大的两个点，注意一定是后面的值减去前面的一个值
'''

def get_the_two_points_contribute_the_biggest_gap_from_a_lst(lst=[]):

    if len(lst)<=1:
        return None
    lst.sort()
    return (lst[0], lst[-1])


if __name__ == '__main__':

    aList = [1, 2, -3, 4, 99, 32, 45, 12]

    print get_the_two_points_contribute_the_biggest_gap_from_a_lst(aList)
