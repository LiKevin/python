__author__ = 'k22li'


_generator = (x*2 for x in range(5))
print _generator.gi_running

for _item in _generator:
    print _generator.gi_running
    print '>>> %s' %_item

def testFunction():
    print '>>> inside the function ... '

print '>>> from the function code: %s'%testFunction.func_code

print '>>> test "__func__ method: %s"'%testFunction.func_globals