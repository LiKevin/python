# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# Questions:
# 删除list中重复的list
# Fixme: key point:   list is not hashable, so can not "Set()" or "dict()"; the way is to convert those list elem to str\
# Fixme: then roll them back
########################################################################################################################

#demo 1
########################################################################################################################
def remove_dups_from_list_of_lists(lst=None):
    if lst is None:
        lst = []
        return '>>> Nothing to deal with, empty list provided as input...'

    convert_to_str_list = [ repr(x) for x in lst ]  #Fixme: sets.Set() doesn't support list type elements, so converting
    import sets
    convert_str_list_to_set = sets.Set(convert_to_str_list) #dups is to removed via this converting to set
    convert_set_back_to_list = [ eval(x) for x in convert_str_list_to_set ] # now all members were converted back to lst

    return convert_set_back_to_list

#demo 2
########################################################################################################################
def remove_dups_from_list_of_lists_via_dict(lst=None):
    if lst is None:
        lst = []
        return '>>> Nothing to deal with, empty list provided as input...'

    dct = dict(enumerate(lst))  #convert the list & its index to dict
    str_formatted_keys = [repr(x) for x in dct.values()]
    try:
        reversed_dct = dict(zip(dct.values(), dct.keys()))   # try to reverse the key - value pairs, but not succeed, \
        # as list type of elem is not able to be used as keys
    except TypeError as e:
        print '>>> Error to reverse the key-value pairs : %s' %e
        reversed_dct = dict(zip(str_formatted_keys, dct.keys()))

    return [ eval(x) for x in reversed_dct.keys() ]

########################################################################################################################
# test codes
########################################################################################################################

if  __name__ == '__main__':

    z=[ [1,2] , [3,4] , [1,2] , [5,6] , [7,8] , [9,0] , [3,4] , [1,2] , [7,8] ]

    print remove_dups_from_list_of_lists(z)
    print remove_dups_from_list_of_lists_via_dict(z)