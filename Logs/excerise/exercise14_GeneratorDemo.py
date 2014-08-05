__author__ = 'k22li'


def list_comprehension_method():
    '''
    here the list comprehension is used; the disadvantage is that it has to store all value needed into memory
    once for all, but this could be damage when the list is too long
    '''
    myList = [x*x for x in range(10)]
    for x in myList:
        print x

def generator_method():
    '''
    the difference between list & () is that the later one use the iterator mechanism instead of list; the advantage is
    the way use only limited memory spaces, while the disadvantage is that
    '''
    myGenerator = (x*x for x in range(10))
    for x in myGenerator:
        print x

    '''
    Notices:  the second time to processing a list, then it would do nothing.... as all those elements has been walked
    through from the 1st time
    '''
    for x in myGenerator:
        print x

def yield_generator_method():
    '''
    yield generator demo
    '''
    my_generator_feed = range(10)
    for x in my_generator_feed:
        yield 'The elements to be yield is: %s' %(x*x)


############################ MAIN FUNCTION ############################
if __name__ == '__main__':
    t = yield_generator_method()
    for x in range(10):
        print t.next()

    '''
    the last time to exit from the iterating must be a "StopIteration" error
    '''
    try:
        print t.next()
    except StopIteration as e:
        print "Error Warning, Reason: StopIteration! "