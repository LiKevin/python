__author__ = 'k22li'

from cStringIO import StringIO

t = StringIO()

for item in dir(t):
    print '%s %s> %s' %(item, '-'*(100-len(item)-len(str(getattr(t,item)))),getattr(t, item))

# outputs:
#
#    __class__ -----------------------------------------------------------------> <type 'cStringIO.StringO'>
#    __delattr__ ---------> <method-wrapper '__delattr__' of cStringIO.StringO object at 0x00000000020C8458>
#    __doc__ -----------------------------------------------------------> Simple type for output to strings.
#    __format__ ------------> <built-in method __format__ of cStringIO.StringO object at 0x00000000020C8458>
#    __getattribute__ > <method-wrapper '__getattribute__' of cStringIO.StringO object at 0x00000000020C8458>
#    __hash__ ---------------> <method-wrapper '__hash__' of cStringIO.StringO object at 0x00000000020C8458>
#    __init__ ---------------> <method-wrapper '__init__' of cStringIO.StringO object at 0x00000000020C8458>
#    __iter__ ---------------> <method-wrapper '__iter__' of cStringIO.StringO object at 0x00000000020C8458>
#    __new__ -------------------------------> <built-in method __new__ of type object at 0x000000001E2987C0>
#    __reduce__ ------------> <built-in method __reduce__ of cStringIO.StringO object at 0x00000000020C8458>
#    __reduce_ex__ ------> <built-in method __reduce_ex__ of cStringIO.StringO object at 0x00000000020C8458>
#    __repr__ ---------------> <method-wrapper '__repr__' of cStringIO.StringO object at 0x00000000020C8458>
#    __setattr__ ---------> <method-wrapper '__setattr__' of cStringIO.StringO object at 0x00000000020C8458>
#    __sizeof__ ------------> <built-in method __sizeof__ of cStringIO.StringO object at 0x00000000020C8458>
#    __str__ -----------------> <method-wrapper '__str__' of cStringIO.StringO object at 0x00000000020C8458>
#    __subclasshook__ -------------> <built-in method __subclasshook__ of type object at 0x000000001E2603C0>
#    close ----------------------> <built-in method close of cStringIO.StringO object at 0x00000000020C8458>
#    closed -----------------------------------------------------------------------------------------> False
#    flush ----------------------> <built-in method flush of cStringIO.StringO object at 0x00000000020C8458>
#    getvalue ----------------> <built-in method getvalue of cStringIO.StringO object at 0x00000000020C8458>
#    isatty --------------------> <built-in method isatty of cStringIO.StringO object at 0x00000000020C8458>
#    next -----------------------> <method-wrapper 'next' of cStringIO.StringO object at 0x00000000020C8458>
#    read ------------------------> <built-in method read of cStringIO.StringO object at 0x00000000020C8458>
#    readline ----------------> <built-in method readline of cStringIO.StringO object at 0x00000000020C8458>
#    readlines --------------> <built-in method readlines of cStringIO.StringO object at 0x00000000020C8458>
#    reset ----------------------> <built-in method reset of cStringIO.StringO object at 0x00000000020C8458>
#    seek ------------------------> <built-in method seek of cStringIO.StringO object at 0x00000000020C8458>
#    softspace ------------------------------------------------------------------------------------------> 0
#    tell ------------------------> <built-in method tell of cStringIO.StringO object at 0x00000000020C8458>
#    truncate ----------------> <built-in method truncate of cStringIO.StringO object at 0x00000000020C8458>
#    write ----------------------> <built-in method write of cStringIO.StringO object at 0x00000000020C8458>
#    writelines ------------> <built-in method writelines of cStringIO.StringO object at 0x00000000020C8458>

