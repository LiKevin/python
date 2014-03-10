__author__ = 'k22li'

import itertools
import string

listA = string.digits[:5]
listB = string.letters[:5]


# Difference than 'listA + listB' is that the later format will require the two lists are of the same types; while
# then chain() method won't care about this.

print list(itertools.chain(listA, listB))