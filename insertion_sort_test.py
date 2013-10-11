__author__ = 'k22li'

from random import randint
import copy
import timeit

# for public using
def randListGenerator(length = 0):

    randList = [ randint(0, 999) for i in range(length)]
    return randList


"""
case 1, kevin design
"""
def findTheMinEle(tempList):
    minEle = tempList[0]
    for item in tempList:
        if item <= minEle:
            minEle = item
    return minEle

def insertion_sort(aList):
    sortedList = []
    bList = aList[:]
    for i in range(len(bList)):
        minEle = findTheMinEle(bList)
        sortedList.append(minEle)
        try:
            bList.remove(minEle)
        except:
            print minEle, bList
    return sortedList


"""
case 2, from book
"""
def insertion_sort2(aList):
    for j in range(0, len(aList)):
        key = aList[j]
        i = j-1
        while i>=0 and aList[i]>key:
            aList[i+1] = aList[i]
            i = i - 1
        aList[i+1] = key
    return aList


if __name__ == "__main__":

    testList = randListGenerator(20)

    print testList
    print insertion_sort2(testList)


    string = \
        """
        def findTheMinEle(tempList):
            minEle = tempList[0]
            for item in tempList:
                if item <= minEle:
                    minEle = item
            return minEle
        def insertion_sort(aList):
            sortedList = []
            bList = aList[:]
            for i in range(len(bList)):
                minEle = findTheMinEle(bList)
                sortedList.append(minEle)
                try:
                    bList.remove(minEle)
                except:
                    print minEle, bList
            return sortedList
        insertion_sort([17, 465, 288, 695, 990, 919, 196, 309, 729, 363, 22, 476, 416, 809, 526, 232, 122, 184, 617, 464])
        """
    t1 = timeit.Timer(string)
    print t1.timeit(number = 10000)
#    testResult = insertion_sort(testList)
    string2 = \
        """
        [17, 465, 288, 695, 990, 919, 196, 309, 729, 363, 22, 476, 416, 809, 526, 232, 122, 184, 617, 464].sort()
        """
    t2 = timeit.Timer(string2)
    print t2.timeit(number = 10000)


    string3 = \
        """
        def insertion_sort2(aList):
            for j in range(0, len(aList)):
                key = aList[j]
                i = j-1
                while i>=0 and aList[i]>key:
                    aList[i+1] = aList[i]
                    i = i - 1
                aList[i+1] = key
            return aList
        insertion_sort2([17, 465, 288, 695, 990, 919, 196, 309, 729, 363, 22, 476, 416, 809, 526, 232, 122, 184, 617, 464])
        """
    t3 = timeit.Timer(string3)
    print t3.timeit(number = 10000)




##    assert testResult == testList, 'failed matching'