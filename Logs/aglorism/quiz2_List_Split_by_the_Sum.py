# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
# 问题：有一个没有排序，元素个数为2*n的正整数数组，要求:如何能把这个数组分割成元素个数为n的两个数组，并使两个子数组的和最接近？
######################################################################################################################


# demo 1
######################################################################################################################
#from operator import itemgetter
from random import randint

def get_list_splitted_by_sums(lst=None):

    if lst is None:
        lst = []
        return [], []

    aver = sum(lst)/len(lst)
    new_lst = [(key, aver-key) for key in lst]

    new_lst_sorted = sorted(new_lst, key = lambda x : abs(x[1])) # 根据每个元素据average值得摆动幅度排序,取摆动最小的n个为第一
                                                                # 序列;剩余的为第二序列

    lst_a = new_lst_sorted[:len(lst)/2]
    lst_b =  new_lst_sorted[len(lst)/2:]

    sum_a = sum([item[0] for item in lst_a])
    sum_b = sum([item[0] for item in lst_b])

    return sum_a, sum_b

# demo 2
######################################################################################################################

def get_list_of_int_splitted_into_sublists(lst):

    sorted_lst = sorted(lst)

    lst_a =  [i for i in sorted_lst if sorted_lst.index(i)%2 == 1]
    lst_b =  [i for i in sorted_lst if sorted_lst.index(i)%2 == 0]

    return sum(lst_a), sum(lst_b)


# demo 3
######################################################################################################################



if __name__ == '__main__':

    test_list = [randint(1, 1000) for i in range(10)]

#    print test_list
    print get_list_splitted_by_sums(test_list)

    print get_list_of_int_splitted_into_sublists(test_list)
