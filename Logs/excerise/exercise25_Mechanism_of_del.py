# -*- coding: utf-8 -*-
__author__ = 'k22li'
__doc__ = '''
当一个对象显式定义了__del__方法，而且里面有循环引用，Python不会自动回收这个对象。
如果这种情况没有正确处理，会造成内存泄漏。
解决的办法是在__del__中手动解除循环引用，或者干脆避免这种有循环引用的写法。'''

class Foo():

    def __init__(self):
        self._bar   = {'test': self.test}   #循环引用
        print 'construct'

    def test(self):
        print 'main body, test'

    def __del__(self):
        print 'del object'


if __name__ == '__main__':

    f = Foo()
    f.__del__() # manual del the objects, working
    del f # doesn't working, can't del the f