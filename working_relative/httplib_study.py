# -*- coding: utf-8 -*-
__author__ = 'k22li'

import httplib

#h = httplib.Http('.cache')

conn1 = httplib.HTTPConnection('www.baidu.com:80')
#resp, content = h.request('www.baidu.com')

print conn1

conn1.request('GET', '/', '', {'user-agent' : 'test'})
res = conn1.getresponse()

print res.status
print '*'*40
print res.msg
print '*'*40
for item in dir(res):
    print item

print [1, 2, 3]+['a', 'b', 'c']

aDic = {'a': 1, 'b':2}
print id(aDic)
bDic = {'c':3, 'd':4}
print id(bDic)
aDic.update(bDic)

print aDic, id(aDic), id(bDic)

a = 'bc'
print '1-->', id(a)
b = 'ab'
print '2-->', id(b)

a = b
print '3-->', id(a)

c = b[:]
print id(c)
print id(b)


alist = ['a', 'b']
print '%s'%alist, id(alist)
blist = [1, 2]
print '%s'%blist, id(blist)
clist = alist
print '%s'%clist, id(clist)
dlist = blist[:]
print '%s'%dlist, id(dlist)