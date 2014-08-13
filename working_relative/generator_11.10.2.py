# -*- coding: utf-8 -*-
__author__ = 'k22li'

#
#def counter(start_at = 0):
#    count = start_at
#    while True:
#        val = (yield count) if val is not None:
#        count = val
#    else:
#        count += 1
#
#
#
#k = counter()
#
#print k.next()



"""
函数式编程
"""
list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']

t = map(None, list_1, list_2)

print t


import sys

for item in sys.modules.items():
    print item