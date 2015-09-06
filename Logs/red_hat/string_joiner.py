__author__ = 'k22li'

from cStringIO import StringIO
a = 'aaaaaa'
st = StringIO()

for i in xrange(100):
	st.write(a)

#print dir(st)
print a
print st.readlines()
