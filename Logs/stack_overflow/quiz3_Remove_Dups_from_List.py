__author__ = 'k22li'

########################################################################################################################
# Questions:
# to remove all those dup elems from a list
########################################################################################################################

# Demo 1
########################################################################################################################

import sets

def remove_dups_via_set(lst):
    '''
    remove the dups via calling this set functions
    '''
    return list(sets.Set(lst))


# Demo 2
########################################################################################################################
def remove_dups_via_list(lst):
    '''
    remove the dups implementations via list comprehension
    '''
    new_lst = []
    [ new_lst.append(item) for item in lst if not item in new_lst ]
    return new_lst

# Demo 3
########################################################################################################################
def remove_dups_via_dict(lst):
    '''
     remove dups via dict analyzing
    '''
    dct_origin = dict(enumerate(lst))
    dct_new = dict(zip(dct_origin.values(), dct_origin.keys()))
    return dct_new.keys()

########################################################################################################################
# test codes                                                                                                           #
########################################################################################################################
if __name__ == '__main__':
    list_a = ['b','b','d','b','c','a','a']
    # test demo 1
    print(remove_dups_via_set(list_a))
    # test demo 2
    print(remove_dups_via_list(list_a))
    # test demo 3
    print(remove_dups_via_dict(list_a))