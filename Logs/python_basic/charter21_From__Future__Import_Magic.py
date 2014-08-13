#from __future__ import with_statement #fixme: SyntaxError: from __future__ imports must occur at the beginning of the file
__author__ = 'k22li' # this declaration should be removed if the "from __future__ import " existing

######################################################################################################################
# function implementations
# purpose is to:
#  try to understand "from __future__ import with_statement"
########################################################################################################################

# demo 1
########################################################################################################################

with open('patten.py', 'r') as f:
    l = f.readline()
    while l:
        print l
        l = f.readline()



# demo 2: error demo
########################################################################################################################


f = open('patten.py', 'r')
with f:
    k = f.readline()
    while k:
        print k
        k = f.readline()

try:
    with f:
        k = f.readline()
        while k:
            print k
            k = f.readline()

except ValueError as e:
    print('Error when again opening the file: %s'%e)


# demo 3: threading.locked acquire and releasing
########################################################################################################################
from contextlib import contextmanager

@contextmanager
def locking(myLock):
    lk = myLock.acquire()
    try:
        yield
    finally:
        myLock.release()

# implementations

with locking(lock):
    xxx