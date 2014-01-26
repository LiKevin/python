__author__ = 'k22li'

import itertools

#itertools.repeat(1.2)

for item in dir(itertools):
    print item


print map(lambda x: x, itertools.count(2, 1))