__author__ = 'k22li'

"""
Example of decorator design
"""

def formatting(func):
    '''
    multiply the digit given by a factor
    '''
    def wrapped():
        print "#"*63
        func()
        print "#"*63
    return wrapped

def func_decorator(func):
    '''
    decorator to decorate the functions
    '''
    def wrapped():
        '''
        decorator used to wrap the func to decorate
        '''
        print "*"*20+"Beginning of decorating"+"*"*20
        func()
        print "*"*20+"  Ending of decorating "+"*"*20
    return wrapped

@func_decorator
@formatting
def func_to_decorate():
    print "Hi, i am the function to decorate"


if __name__=='__main__':
    func_to_decorate()


