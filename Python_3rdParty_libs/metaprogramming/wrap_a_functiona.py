__author__ = 'k22li'

import time
from functools import wraps

def timethis(func):

    @wraps(func)
    def wrapper(* args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print (func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n>0:
        print n
        n -= 1


@timethis
def add_calc(a, b):
    return a+b


if __name__=='__main__':

#    countdown(10*1000)
#    print add_calc.__repr__
    t = add_calc(7, 9)

    org_countdown = t.__wrapped__

    org_countdown(10, 20)