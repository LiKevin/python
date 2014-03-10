__author__ = 'k22li'

from functools import wraps, partial
import logging

def attach_wrapper(obj,func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):

    def decorate(func):
        logname=name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

#        attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
#            nonlocal level
            global level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
#            nonlocal logmsg
            global logmsg
            logmsg = newmsg

        return wrapper
    return decorate

@logged(logging.CRITICAL)
def add(x, y):
    return x+y

@logged(logging.CRITICAL, 'example')
def spam():
    print 'Spam!'


if __name__=='__main__':
    print add(3, 4)

    add.set_message('Add called')
    add.set_level(logging.CRITICAL)
    print add(5, 65)