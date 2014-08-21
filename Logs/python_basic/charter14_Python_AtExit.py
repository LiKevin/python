# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
#   "atexit" 模块，
# Fixme：主要用途在于callback 函数当函数执行退出的时候，典型用例：测试框架的teardown函数
#######################################################################################################################

import sys
import atexit

def greeting_method_1(name='Kevin'):

    print 'Hello , %s' %name


def check_exitfunc_availability():
    if hasattr(sys, 'exitfunc'):
        print 'it\'s true that there is already exitfunc registered'
        print 'outputs of %s is: %s' %(repr(sys.exitfunc), sys.exitfunc())

    else:
        print 'nothing to append'

def debugging(debug_info):

    print '%s'.center(100-len(debug_info), '#') %debug_info

if __name__ == '__main__':

    check_exitfunc_availability()

#    print ' the 1st time of "exitfunc()" check is done '.center(100, '*')
    debugging(' the 1st time of "exitfunc()" check is done ')
    for family_member in ['Li Zhihui-kevin', 'Jiang Ke-Cathy', 'Li Xiang-Micheal']:
        atexit.register(greeting_method_1, family_member) # notice this action only register those callback functions \
                                                            # sys.exitfunc (_run_exitfuncs); but do not excute any codes\
                                                            # at all. all executions last till right before exit the \
                                                            # python runtime
#    print ' the 2nd time of "exitfunc()" check hasn\'t started '.center(100, '*')
    debugging(' the 2nd time of "exitfunc()" check hasn\'t started ')
    check_exitfunc_availability()

# outputs:
#    it's true that there is already exitfunc registered
#    outputs of <function _run_exitfuncs at 0x000000000240A358> is: None
#    ########################### the 1st time of "exitfunc()" check is done ###########################
#    ######################## the 2nd time of "exitfunc()" check hasn't started #######################
#    it's true that there is already exitfunc registered
#    Hello , Li Xiang-Micheal
#    Hello , Jiang Ke-Cathy
#    Hello , Li Zhihui-kevin
#    outputs of <function _run_exitfuncs at 0x000000000240A358> is: None
