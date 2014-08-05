# -*- coding:  utf-8 -*-
__author__ = 'k22li'

'''
PURPOSE:
在Python里，类变量通常在内部被当做字典来处理并遵循通常所说的方法解析顺序（Method Resolution Order (MRO)）。
因此在上面的代码中，因为属性x在类C中找不到，因此它会往上去它的基类中查找
（在上面的例子中只有A这个类，当然Python是支持多重继承（multiple inheritance）的）。
换句话说，C没有它自己独立于A的属性x。因此对C.x的引用实际上是对A.x的引用。
（B.x不是对A.x的引用是因为在第二步里B.x=2将B.x引用到了2这个对象上，倘若没有如此，B.x仍然是引用到A.x上的。——译者注）
'''

class A(object):
    x = 1

class B(A):
    pass

class C(A):
    pass




if __name__=='__main__':

    print A.x, B.x, C.x
    # output:  1, 1, 1

    # update the middle value of the class B
    B.x = 2
    print A.x, B.x, C.x
    # output:  1, 2, 1

    # update the value of the parent class
    A.x = 3
    print A.x, B.x, C.x
    # output:  3, 2, 3



