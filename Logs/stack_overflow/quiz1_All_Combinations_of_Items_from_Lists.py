# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
Question:

Given a list of lists, I need a new list that gives all the possible combinations of items between the lists.
e.g:
[[1,2,3],[4,5,6],[7,8,9,10]] -> [[1,4,7],[1,4,8],...,[3,6,10]]
The number of lists is unknown, so I need something that works for all cases.
'''

import itertools

def get_all_combinations(input_list):
    '''
    with the sub-lists inside the input_list, return all the possible combinations of elems from each of them
    '''
    return list(itertools.product(*input_list))
    # *a means these are arguments being passed to the function or method. def fn(a,b,c): would respond to fn(*[1,2,3])

if __name__ == '__main__':
    list_a = [[1,2,3],[4,5,6],[7,8,9,10]]
    list_b = [[1,2,3], [1]]
    print get_all_combinations(list_b)