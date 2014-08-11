# -*- coding: utf-8 -*-
__author__ = 'k22li'

######################################################################################################################
# function implementations
# purpose is to:
#   isinstance vs issubclass
# fixme: isinstance() methods only working with child & its direct parent class
# fixme: while issubclass() methods working with parent & super parent class as well
#######################################################################################################################

# demo 1
#######################################################################################################################

def demo_of_isinstance():
    '''
    check the working scope of the isinstance methods, try to check with the child and its super parents
    '''
    for item in [1, None, 'a', ['a', 'b'], ('a',), {'a':65}]:

        try:
            print isinstance(item, type)
        except Exception as e:
            print 'isinstance {}, type: {}'.format(item, e)

# demo 2
#######################################################################################################################
def demo_of_issubclass():

    class A(object):
        pass
    class B(A):
        pass
    class C(B):
        pass

    print issubclass(C, B)

    print issubclass(C, A)

    print issubclass(C, (A, B))

#######################################################################################################################
# test codes
#######################################################################################################################
if __name__ == '__main__':

    # demo 1 testing
    demo_of_isinstance()

    # demo 2 testing
    demo_of_issubclass()