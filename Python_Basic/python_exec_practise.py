__author__ = 'k22li'

def checkAvailability(param):
    return globals().has_key(param)

str = "for i in range(10): print i"
c = compile(str,'', 'exec')
exec c
print checkAvailability('d')

str = "for i in range(20, 30): print i"
d = compile(str, '', 'exec')
exec d
print checkAvailability('d')
