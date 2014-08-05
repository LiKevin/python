# -*- coding:  utf-8 -*-
__author__ = 'k22li'
___doc__ = '''

Purpose:
Append => Single Element; Extend => Multiple Element.
'''

###################################################################################################
# Demo 1:  difference between "Append" & "Extend" operations for a list

def append_vs_extend(opend = 'append'):

    lst = [1, 2, 3, 4, 5]

    if opend.startswith('app'):
        print "Append method is to be called: "
        lst.append([6, 7])
        print lst
    else:
        print "Extend method is to be called: "
        lst.extend([6, 7])
        print lst

###################################################################################################
# Demo 2:  any iterable will do for the extend, here is an example for dictionary argument

def extend_with_a_dict():
    lst = [1, 2, 3, 4]
    dct = {5: 'a', 6:'c'}
    lst.extend(dct)
    print lst

###################################################################################################
# Demo 3:  any iterable will do for the extend, here is an example for dictionary argument

def extend_with_a_tuple():
    lst = [1, 2, 3, 4]
    tpl = (5, 6)
    lst.extend(tpl)
    print lst

###################################################################################################
# Demo 4:  any iterable will do for the extend, here is an example for dictionary argument
def extend_to_a_tuple():
    tpl = (1, 2, 3)
    lst = [4, 5]
    try:
        tpl.extend(lst)
        print tpl
    except AttributeError as e:
        print 'Error Warning:  %s' %e



###################################################################################################
# Demo 5:  any iterable will do for the extend, here is an example for dictionary argument
def extend_with_a_string_in_a_tuple():
    lst = [1, 2, 3, 4]
#    tpl = ("abc", "def")  # would be the tuple being iterated
    tpl = ("abc")   # would be the only string item being iterated; output: [1, 2, 3, 4, 'a', 'b', 'c']
#    tpl = {'keys': 'values'}  # output: [1, 2, 3, 4, 'keys']
#    tpl = ['keys']     # output: [1, 2, 3, 4, 'keys']
#    tpl = [('keys'),]   # output: [1, 2, 3, 4, 'keys']
    lst.extend(tpl)
    print lst


if __name__ =='__main__':
    ######################################## Demo 1 ################################################
    append_vs_extend()
    # output: Append method is to be called: \n [1, 2, 3, 4, 5, [6, 7]]

    append_vs_extend('extend')
    # output: Extend method is to be called: \n [1, 2, 3, 4, 5, 6, 7]

    ######################################## Demo 2 ################################################
    extend_with_a_dict()
    # output:   any iterable will do for the extend, by default the keys would be used for extend iterations from the \
    # dict [1, 2, 3, 4, 5, 6]

    ######################################## Demo 3 ################################################
    extend_with_a_tuple()
    # output:   any iterable will do for the extend, by default the keys would be used for extend iterations from the \
    # dict [1, 2, 3, 4, 5, 6]

    ######################################## Demo 4 ################################################
    extend_to_a_tuple()
    # output:   Error Warning:  'tuple' object has no attribute 'extend'

    ######################################## Demo 5 ################################################
    extend_with_a_string_in_a_tuple()
    # output:  [1, 2, 3, 4, 'a', 'b', 'c']
    # reason:  when the only str items used as the iterable objects (in a tuple), then would be the string \
    # being iterated directly