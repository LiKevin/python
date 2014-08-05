# -*_ coding:  utf-8 -*-
__author__ = 'k22li'
__doc__ = '''

找出一个数列中值重复出现的次数，并按出现的次数多少进行排序显示
'''

import sets

def sorted_elements(lst = []):

    unique_lst = list(sets.Set(lst))
    for elem in unique_lst:
        print 'Count "%s" is:  %s' %(elem, aList.count(elem))


if __name__ == '__main__':

    aList = [1, 2, 2, 3, 3, 3, 4,4,4,4, 5,5,5,5,5]

    sorted_elements(aList)
