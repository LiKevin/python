__author__ = 'k22li'

from functools import wraps
import logging

def logged(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.CRITICAL)
def add(x, y):
    return x+y


if __name__=='__main__':
    print add(3, 4)