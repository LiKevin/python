# -*- coding:  utf-8 -*-
__author__ = 'k22li'

'''
Purpose:

这里的问题在于except语句不会像这样去接受一系列的异常。
并且，在Python 2.x里面，语法except Exception, e是用来将异常和这个可选的参数绑定起来（即这里的e），以用来在后面查看的。
因此，在上面的代码中，IndexError异常不会被except语句捕捉到；而最终ValueError这个异常被绑定在了一个叫做IndexError的参数上。

在except语句中捕捉多个异常的正确做法是将所有想要捕捉的异常放在一个元组（tuple）里并作为第一个参数给except语句。
并且，为移植性考虑，使用as关键字，因为Python 2和Python 3都支持这样的语法
'''

class ExceptionCupture():

    def __init__(self):
        self.list = ['a', 'b']
        print '**** start init ****'

    def __enter__(self):
        try:
            print "**** start enter ****"
            print self.list[2]

        except (ValueError, IndexError) as e:  #想同时捕获两个异常
            print 'IndexError Debugging: %s' %e
            pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "**** start exit ****"
        print 'Type:  %s, Value: %s, TraceBack:  %s' %(exc_type, exc_val, exc_tb)


if __name__ == '__main__':

    with ExceptionCupture() as t:
        print 'Value of "t" is:  %s' %t
