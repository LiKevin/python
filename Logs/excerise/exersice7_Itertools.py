__author__ = 'k22li'


import itertools

def generateAllSortingPossibilities(listA):
    """
    is to return all those combination possibilities of listA
    """
    return itertools.permutations(listA)


if __name__ == '__main__':

    list1 = [x for x in xrange(8) if x%2 == 0 ]

    for i in generateAllSortingPossibilities(list1):

        print i
