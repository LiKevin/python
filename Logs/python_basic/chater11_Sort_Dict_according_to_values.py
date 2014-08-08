# -*- coding: utf-8 -*-
__author__ = 'k22li'

#######################################################################################################################
# function implementations
# purpose is to:
#   查找一个age最高的name
#######################################################################################################################

def get_the_yongest_name_return_tuple(person_dict):

    '''
    sort the names by his/her age, return the yongest one's info in tuple
    '''
    name_sorted = sorted(person_dict.items(), key=lambda x: x[1])
    name = name_sorted.pop(0)
    del name_sorted #clean up the memory once the list isnt useful
    return name

def get_the_yongest_name_return_string(person_dict):
    '''
    sort the names by his/her age, return the yongest ones' name
    '''
    name_sorted =  sorted(person_dict, key=lambda x : person_dict[x])
    name = name_sorted.pop(0)
    del name_sorted
    return name

if __name__ == '__main__':

    person = {'shao':23, 'wang':20, 'zhang':21, 'he':22}

    print get_the_yongest_name_return_tuple(person)
    print person.items()

    print get_the_yongest_name_return_string(person)