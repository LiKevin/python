__author__ = 'k22li'

from decorator_that_takes_arguments import *
from itertools import combinations, permutations

@logged(logging.DEBUG)
def countDown(n):
    while n > 0:
        yield n
        n -= 1

@logged(logging.CRITICAL, 'test_instance')
def spam():
    print 'Spam!'


if __name__=='__main__':

    print list(countDown(20))

    print list(combinations(countDown(5), 4))

    print list(permutations(countDown(5), 4))
    spam()