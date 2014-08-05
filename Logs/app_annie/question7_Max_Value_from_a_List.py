__author__ = 'k22li'
__doc__ = '''3、找出一个数列中的最大值'''

def max(lst=[]):
    '''
    return the max value from a list
    '''
    if lst:
        lst.sort()
        return lst[-1]
    else:
         return None


if __name__ == '__main__':

    print max([1, 2, 3, 7, 4, 5, 9, 43])