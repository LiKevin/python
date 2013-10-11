# -*- coding: utf-8 -*-

#print 'हिन्दी'.decode('utf-8')
import sys

print sys.getdefaultencoding()

#sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding()

print u'\u7b80\u4f53 \u62fc\u97f3\u5168\u952e\u76d8'.encode('utf-8')
print u'\u62fc\u97f3'.encode('utf-8')
#print 'हिन्दी'.encode('utf-8')


#print u'\u0627\u0644\u0639\u0631\u0628\u064a\u0629'.encode('utf-8')

#print 'العربية'.decode('utf-8')

t = 'العربية'

if isinstance(t, unicode):
    print 'العربية'.decode('cp1256').decode('raw_unicode_escape')
else:
    k =  t.decode('utf-8').encode('raw_unicode_escape')


c = k.decode('utf-8')

print c

#print u'\u0627\u0644\u0639\u0631\u0628\u064a\u0629'.decode('utf-8')
print u'\u0939\u093f\u0928\u094d\u0926\u0940'.encode('utf-8')
#prin t= u'\u0939\u093f\u0928\u094d\u0926\u0940'.encode('raw_unicode_escape')


print u'\u0939\u093f\u0928\u094d\u0926\u0940'.encode('utf-8')


print 'हिन्दी'.__class__
#print u'\ua7d8\u84d9\ub9d8\ub1d8\ua8d8\u8ad9\ua9d8'.decode('raw_unicode_escape')
#print u'\u56fe\u50cf'.encode('utf-8')
#
##print '主题元素'.decode('gb2312')
#t = '主题元素'
#
#if isinstance(t, unicode):
#
#    print t.encode('gb2312')
#
#else:
#    print t.decode('utf-8').encode('raw_unicode_escape')
#
#
t  = ['nryDd6qL5OQuXbSskzcS2gb', 'English full keyboard', 'English phone keypad', u'\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0', u'\u0939\u093f\u0928\u094d\u0926\u0940', u'\u0c95\u0ca8\u0ccd\u0ca8\u0ca1', u'\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02', u'\u0ba4\u0bae\u0bbf\u0bb4\u0bcd', u'\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41', u'\u0627\u0631\u062f\u0648 full keyboard', u'\u0627\u0631\u062f\u0648 phone keypad', 'n6Vpdj39k8kO7BzxnrXOErg', '1:50 pm']

print '*'*23, t[4]



k = u'\u0939\u093f\u0928\u094d\u0926\u0940'

print 'k value is: %s'%k

if k in t:
#if isinstance(t[4], unicode):
    print 'True'
else:
    print 'False'

k = '稍后登录'
#c = k.decode('utf-8').encode('raw_unicode_escape')
c = u'\u7a0d\u540e\u767b\u5f55'
#print c
#print c.decode('utf8')
#print u'\u7a0d\u540e\u767b\u5f55'.decode('utf-8')

print '-'*80
print 'हिन्दी'.decode('utf-8').encode('raw_unicode_escape')