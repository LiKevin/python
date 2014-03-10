__author__ = 'k22li'

# itertools.dropwhile(func, iterator):  accept two params, while func return true, then start the generator/iterator
# slicing, till end of the generator/ iterator


import itertools

def countDown(n):

    while n>0:
        yield n
        n -= 1

t = itertools.dropwhile(lambda x : x>=10, countDown(30))

print list(t)

print '****all possible permutations from countdown method:****'
for p in itertools.permutations(countDown(3)):
    print p


print '****all possible combinations from countdown method:****'
for q in itertools.combinations(countDown(3), 2):
    print q