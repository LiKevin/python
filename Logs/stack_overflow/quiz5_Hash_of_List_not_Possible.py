# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# Questions:
# 删除list中重复的list
# Fixme: key point:   list is not hashable, so can not "Set()" or "dict()"; the way is to convert those list elem to str\
# Fixme: then roll them back
# 4、字典的键
# (1)不允许一个键对应多个值
# 对应的值可以是其他的容器类型的对象。
# (2)键必须是可以哈希的
# Fixme: 像列表和字典这样的可变类型，由于它们不是可哈希的，所以不能作为键。所有不可变类型的都是可哈希的，因此他们都可以作为字典的键。
# Fixme: 一个要说明的问题是数字：值相等的数字表示相同的键。同时，也有一些可变对象（很少）是可哈希的，他们可以作为字典的键，但是很少见。
# Fixme: 举一个例子，实现了__hash__特殊方法的类。因为__hash__返回一个整型，所以仍然是用不可变的值（做字典的键）。
# 我们知道数字和字符串可以被用作字典的键，但元组如何呢？
# fixme: 用元组做有效的键，必须加以限制：元组中只包括想数字和字符串这样的不可变参数，才可以作为字典中有效的键。
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