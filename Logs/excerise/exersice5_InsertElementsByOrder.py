__author__ = 'k22li'

import bisect
import random

list1 = [random.randint(1, 20) for i in xrange(10)]
list1.sort()

def insertElementByOrder(lista, newElement):
    """
    insert the new element to the list provided and sort the list by order
    """

    print lista

    bisect.insort(lista, newElement)

    print lista

insertElementByOrder(list1, 12)

