# -*- coding:  utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
Purpose:
常见错误5：在遍历列表的同时又在修改这个列表
'''
#########################################################################################################
# Demo 1:

def modify_and_iterating_a_list():
    '''
    遍历一个列表或者数组的同时又删除里面的元素，对任何有经验的软件开发人员来说这是个很明显的错误。
    但是像上面的例子那样明显的错误，即使有经验的程序员也可能不经意间在更加复杂的程序中不小心犯错。
    '''
    odd =  lambda x : bool(x % 2)
    numbers = range(10)

    for i in range(len(numbers)):
        try:
            if odd(numbers[i]):
#                del numbers[i]
                numbers.remove(numbers[i])
        except IndexError as e:
            print 'Error Warning:  %s' %e
            break

    print 'Printed from "modify_and_iterating_a_list": %s' %numbers

#########################################################################################################
# Demo 2:

def modify_and_iterating_a_list_2nd():
    odd = lambda x : bool(x % 2)
    numbers = range(10)

    for item in numbers:
        if odd(item):
            numbers.remove(item)
    print 'Printed from "modify_and_iterating_a_list_2nd": %s' %numbers


#########################################################################################################
# Demo 3:

def modify_and_iterating_a_list_via_list_comprehension():
    '''
    所幸，Python集成了一些优雅的编程范式，如果使用得当，可以写出相当简化和精简的代码。
    一个附加的好处是更简单的代码更不容易遇到这种“不小心在遍历列表时删掉列表元素”的bug。
    例如列表推导式（list comprehensions）就提供了这样的范式。
    再者，列表推导式在避免这样的问题上特别有用，接下来这个对上面的代码的重新实现就相当完美
    '''
    odd = lambda x : bool(x % 2)
    numbers = range(10)

    odds = [ x for x in numbers if not odd(x)]

    print 'Printed from "modify_and_iterating_a_list_via_list_comprehension": %s' %odds

######################################### Main Function #################################################
if __name__ == '__main__':

    ########################################## Demo 1 ####################################################
    modify_and_iterating_a_list()
    # output:  Error Warning:  list index out of range \n Printed from "modify_and_iterating_a_list": [0, 2, 4, 6, 8]

    ########################################## Demo 2 ####################################################
    modify_and_iterating_a_list_2nd()
    # output:  Printed from "modify_and_iterating_a_list_2nd": [0, 2, 4, 6, 8]

    ########################################## Demo 3 ####################################################
    modify_and_iterating_a_list_via_list_comprehension()
    # output:  Printed from "modify_and_iterating_a_list_via_list_comprehension": [0, 2, 4, 6, 8]