__author__ = 'k22li'
)
import re
import os

#print callable(getattr(str, 'split'))

# test functions of filter & map

pat = re.compile('st$')
availableChoice = ['a', 'b', 'c', 'test']

print filter(pat.search, availableChoice)

testFunc = lambda x : os.path.splitext(x)[0]

print map(testFunc, ['a', 'a.b', 'a.b.c', 'test']