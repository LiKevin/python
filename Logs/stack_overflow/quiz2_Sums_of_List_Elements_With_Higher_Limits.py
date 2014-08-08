# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
There is a given list l,may contain more than 5000 integer elements.
There is a limit on sum of the numbers, 20000 or may be high.
The output should be all the possible sums of 2 numbers picked from list
'''

import itertools

def kevin_way(lst):

    if not lst:
        return 0
    combinations = itertools.product(lst, repeat=2)
    sums = [x+y for x, y in item for item in combinations]
    sorted(sums)

    return sums

