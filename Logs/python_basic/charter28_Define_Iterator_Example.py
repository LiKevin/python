# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpoes:
# self- define iterators
# key factors:
#   1)  __iter__
#   2) next()
#   3) stop
########################################################################################################################

# demo 1
########################################################################################################################
# fixme： 只要 __iter__() 在class中被定义了，那末类的对象就可以直接应用于for。。。in。。。 语句作迭代器的作用
########################################################################################################################

class test_iter(object):

    def __init__(self, data_iter, stop):
        self.start = 0
        self.data_iter = data_iter
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        self.start += 1
        if self.start >= self.stop:
            raise StopIteration
        return str(self.start)+'\t' +  self.data_iter.next()

if __name__ == '__main__':

    f = open('patten.py', 'r')
    t = test_iter(f, 12)

    # demo 1 of the iterating of the class instance ...
    for i in t: # 当__iter__() 被声明后，类的实例可以直接作迭代器使用
        print i

#output:
#   stop iterating by meeting the stop criterias, wont raise the "stopIteration" error in this case.

    # demo 2 of the stop criteria of the iterators
    for i in range(13):
        print t.next()

#output:
#    raise StopIteration
# StopIteration
