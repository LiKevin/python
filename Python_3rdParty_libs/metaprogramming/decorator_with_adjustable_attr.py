__author__ = 'k22li'

from functools import wraps, partial
import logging

def logged(level, name=None, message=None):

    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@logged(logging.DEBUG)
def add(x, y):
    return x+y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__=='__main__':
    add(3, 4)
    spam()

