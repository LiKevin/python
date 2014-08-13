# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
# check the working scope of global + local variables
#######################################################################################################################


x = 40

def test_global_vs_local_variables():
    global x
    print('value of "x" from global variables is: %s'%x)

    x = 30  # now switch the variable "x" from global to local
    print('value of "x" from local variables is: %s' %x)

if __name__ == '__main__':

    test_global_vs_local_variables()