# -*- coding: utf-8 -*-
__author__ = 'k22li'
#######################################################################################################################
# function implementations
# purpose is to:
#   字符串去重
#######################################################################################################################

# demo 1:  using the existing lib "set"
#######################################################################################################################
def remove_dup_chars_from_string(str_a):

    return ''.join(set(str_a))

# demo 2:  walking through the string
#######################################################################################################################
def remove_dup_chars_from_string_normal(str_a):
    str_new =[]
    for chr in str_a:
        if not chr in str_new:
            str_new.append(chr)
    return ''.join(str_new)


#######################################################################################################################
# test code
#######################################################################################################################
if __name__ == '__main__':

    print remove_dup_chars_from_string('asbdsadfafe')

    print remove_dup_chars_from_string_normal('asbdsadfafe')