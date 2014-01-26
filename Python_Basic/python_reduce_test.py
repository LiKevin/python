__author__ = 'k22li'

# function of reduce
"""
reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable
to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left \
argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional \
initializer is present, it is placed before the items of the iterable in the calculation, \
and serves as a default when the iterable is empty. \
If initializer is not given and iterable contains only one item, the first item is returned.
"""

print reduce(lambda x, y: x*y, range(1, 5))

# equal to 1*2*3*4 = 24 as the output

print reduce(lambda x, y: x*y, range(1,2))

# suppose the only one param is provided, then the function will return the first only params finally


"""
filter(function, iterable)
Construct a list from those elements of iterable for which function returns true. \
iterable may be either a sequence, a container which supports iteration, or an iterator. \
"""

print filter(lambda x: 2*x, range(1, 4))

"""
If iterable is a string or a tuple, the result also has that type; otherwise it is always a list. \
"""

print filter(lambda x: x*2, (1, 2, 3, 4))

"""
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed. \
"""

print filter(None, range(6)) # Zero would be skipped after as the return

"""
Note that filter(function, iterable) is equivalent to [item for item in iterable if function(item)] if function is not \
None and [item for item in iterable if item] if function is None.

See itertools.filterfalse() for the complementary function that returns elements of iterable for which function returns
\false.
"""

print filter(lambda x : x*2, 'tests') #
