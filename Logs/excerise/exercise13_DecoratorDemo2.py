__author__ = 'k22li'
__doc__ = "Passing arguments to the decorated function"

def a_decorator_passing_arguments(func):
    '''
    demo a decorator which can accept arguments passing
    '''
    def a_wrapper_accepting_arguments(arg1, arg2):
        print "Here i got the two arguments are:  %s, %s" %(arg1, arg2)
        func(arg1, arg2)
        print "Now end of the function"
    return a_wrapper_accepting_arguments


@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print "My name is:  %s, %s" %(first_name, last_name)


if __name__ == '__main__':

    name_tuple = (('Li', 'Kevin'), ('Li', 'Micheal'), ('Jiang', 'Ke'), ('Li', 'Hao'))

    for item in name_tuple:
        arg1, arg2 = item
        print_full_name(arg1, arg2)
