# -*- coding: utf-8 -*-
__author__ = 'k22li'


######################################################################################################################
# function implementations
# purpose is to:
#   Python的functools模块
# fixme: 首先是partial函数，它可以重新绑定函数的可选参数，生成一个callable的partial对象
# fixme: 接着是update_wrapper函数，它可以把被封装函数的__name__、__module__、__doc__和 __dict__都复制到封装函数去
#######################################################################################################################

# demo 1
#######################################################################################################################

def thisIsLiving(func):

    def living(*args, **kwargs):
        return func(*args, **kwargs) + '\n - Answer: eating is the basis of living ...'
    return living

@thisIsLiving
def whatIsLiving():
    '''doc of whatIsLiving: live is to eat'''
    return 'Question: what\'s living?'

# demo 2    # function "update_wrapper()"
#######################################################################################################################

from functools import update_wrapper

def thisIsLivingNew(func):

    def living(*args, **kwargs):
        return func(*args, **kwargs) + '\n - Answer: eating is the basis of living ...'
    return update_wrapper(living, func) #fixme: 返回wrapped function; with all those __doc__/ __name__/ __module__ updated

@thisIsLivingNew    # equal to functools.update_wrapper(thisIsLivingNew, whatIsLivingNew)
def whatIsLivingNew():
    '''
    doc of whatIsLivingNew:  live is to eat
    '''
    return 'Question:  what\'s living?'

# demo 3    # function "wraps()"
#######################################################################################################################
from functools import wraps

def thisIsLivingNewest(func):
    @wraps
    def living(*args, **kwargs):
        return func(*args, **kwargs)
    return  living

@thisIsLivingNewest
def whatIsLivingNewest():
    '''
    doc of whatIsLivingNew:  live is to eat
    '''
    return 'Question:  what\'s living?'


#######################################################################################################################
# test code
#######################################################################################################################
if __name__ == '__main__':

    # demo 1 test
    ####################################################################################################################
    print 'from non-wrapper function:', whatIsLiving()
    print 'from non-wrapper doc:', whatIsLiving.__doc__
    print 'from non-wrapper module:', whatIsLiving.__module__
    print 'from non-wrapper name:', whatIsLiving.__name__
    # outputs:
    # from non-wrapper function: Question: what's living?\n- Answer: eating is the basis of living ...
    # from non-wrapper doc: None
    # from non-wrapper module: __main__
    # from non-wrapper name: living


    # demo 2 test
    ####################################################################################################################
    print('from wrapper function:', whatIsLivingNew())
    print('from wrapper doc:', whatIsLivingNew.__doc__)
    print('from wrapper module:', whatIsLivingNew.__module__)
    print('from wrapper name:', whatIsLivingNew.__name__)
    #output:
    # ('from wrapper function:', "Question:  what's living?\n - Answer: eating is the basis of living ...")
    # ('from wrapper doc:', '\n    doc of whatIsLivingNew:  live is to eat\n    ')
    # ('from wrapper module:', '__main__')
    # ('from wrapper name:', 'whatIsLivingNew')



    # demo 3 test
    ####################################################################################################################
    print('from wrapper_newest function:', whatIsLivingNew())
    print('from wrapper_newest doc:', whatIsLivingNew.__doc__)
    print('from wrapper_newest module:', whatIsLivingNew.__module__)
    print('from wrapper_newest name:', whatIsLivingNew.__name__)
    #output:
    # ('from wrapper_newest function:', "Question:  what's living?\n - Answer: eating is the basis of living ...")
    # ('from wrapper_newest doc:', '\n    doc of whatIsLivingNew:  live is to eat\n    ')
    # ('from wrapper_newest module:', '__main__')
    # ('from wrapper_newest name:', 'whatIsLivingNew')