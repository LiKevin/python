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
        return self.data_iter.next() + str(self.start)

if __name__ == '__main__':

    f = open('patten.py', 'r')
    t = test_iter(f, 12)

    for i in t:
        print i