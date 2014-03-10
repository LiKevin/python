__author__ = 'k22li'

import itertools

def countDown(n):

    while n >0:
        yield n
        n -= 1
# check all those possible elements from the list
print list(countDown(30))

# pick a slices from the generator/ iterators
# itertools.islice produce the other generator accordingly
c = countDown(30)

print list(itertools.islice(c, 20, 25))