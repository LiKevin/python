# coding: utf-8
import os


a = list(range(10))
b = list(range(2, 14))

def mergeAndSort(a, b):

    c = list();
    i=j=0

    while i<len(a) and j <len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    print '>>> value of i: %s, value of j: %s' %(i, j)
    while i<len(a):
        print '>>> handling the rest of elements from a： %s' %a[i]
        c.append(a[i])
        i += 1

    while j<len(b):
        print '>>> handling the rest of elements from b: %s' %b[j]
        c.append(b[j])
        j += 1

    return c


# the python way to handling the list comparison and create the union ones 
def mergeAndSortB(a, b):
    a.extend(b)
    return  sorted(a)


if __name__=="__main__":

   # print mergeAndSort(a, b)
    print mergeAndSortB(a, b)
