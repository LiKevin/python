__author__ = 'k22li'

from datetime import datetime

# purpose: just want explain that by using of datetime module it's by default be aware of the leap years

a = datetime(2012, 2, 28)
b = datetime(2012, 3, 1)

c = b - a

print c
print c.days


d = datetime(2013, 2, 28)
e = datetime(2013, 3, 1)

f = e-d

print f
print f.days
print f.seconds
print f.min
