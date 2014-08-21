# -*- coding: utf-8 -*-
__author__ = 'k22li'

def add(x, y):
    return x+y

#print add('三角形的树', '北极')

lst  = range(11)
amount = 0

for i in lst:
    amount = add(i, amount)
    print amount

print sum(lst)

print reduce(lambda x, y: x+y, lst)