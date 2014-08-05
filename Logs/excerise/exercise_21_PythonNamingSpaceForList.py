# -*- coding: utf-8 -*-
__author__ = 'k22li'

'''

'''

#######################################################################################
# Demo 1:

list_a = [1, 2, 3]

def append_to_list_mehtod():
    list_a.append(5)
    return list_a

'''
output: value of t is: [1, 2, 3, 5]
reason:
'''

def add_to_list_method():

    try:
        list_a += [5]   # Dont work, as trying to assign a value to list_a (local variable)
#        list_a.extend([5])     # working, as operating with the items outside (global)
        return list_a
    except UnboundLocalError as e:
        print "*** Error Warning: %s ***" %e
        return None

'''
Output: *** Error Warning: local variable 'list_a' referenced before assignment ***
Reason:
append_to_list_mehtod 并没有给lst赋值，但是 add_to_list_method 尝试给lst赋值。
注意lst+=[5]只是lst=lst+[5]的简写，由此可以看到我们尝试给lst赋值
（因此Python假设作用域为本地）。但是，这个要赋给lst的值是基于lst本身的（这里的作用域仍然是本地），而lst却没有被定义，这就出错了。
'''

if __name__ == '__main__':

    t = append_to_list_mehtod()
    print 'value of t is: %s' %t

    k = add_to_list_method()
    print 'value of t is: %s' %k
