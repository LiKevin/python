# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
3.求一个一维数组的递增子序列个数，比如[2,3,1,4]，有 [2,3],[3,4],[1,4],[2,3,4]四个，函数返回值为4；
时间复杂度，N*logN
空间复杂度，没记住；
'''

import sets
from itertools import product
from copy import deepcopy
from question4_Switch_Key_and_Values_from_a_Dict import switch_key_values_from_a_dict

def get_ordered_subsets_of_a_given_list(lst = []):

    dict_a =  dict(enumerate(lst))
    dict_b = switch_key_values_from_a_dict(dict_a)

    all_sub_lists = []
#    all_sub_lists_excl_dup_elements = []
#    all_sub_lists_with_elements_ordered = []
    all_ordered_sub_lists = []

    if not lst:
        return []
    # get all those possible sublists
    for i in range(2, len(lst)):
        all_sub_lists.extend(product(lst, repeat=i))
    # remove all those dup-elements sub lists
    all_sub_lists_excl_dup_elements =  \
        [ list(sub_list) for sub_list in all_sub_lists if len(set(sub_list)) == len(sub_list)]
    # select the only sub lists whose elements were ordered from smallest till biggest
    all_sub_lists_with_elements_ordered =  \
        [ lst for lst in all_sub_lists_excl_dup_elements if sorted(deepcopy(lst)) == lst ]
    # ensure the matched sub lists's index orders also align with it's principle orders from the first start
    for tmp_lst in all_sub_lists_with_elements_ordered:
        tmp_lst_copy = deepcopy(tmp_lst)
        coordinates_list = [dict_b[item] for item in tmp_lst_copy]
        new_coordinates_list = deepcopy(coordinates_list)
        new_coordinates_list.sort()

        if new_coordinates_list ==  coordinates_list:
            all_ordered_sub_lists.append(tmp_lst)

    return all_ordered_sub_lists

############################################ Main Function ###################################################

if __name__ == '__main__':

    list_a = [2, 3, 1, 4]

    ############################################## Demo 1 ###################################################
    print get_ordered_subsets_of_a_given_list(list_a)
