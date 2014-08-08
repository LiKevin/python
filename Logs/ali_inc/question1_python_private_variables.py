# -*- coding: utf-8 -*-
__author__ = 'k22li'

#######################################################################################################################
#探究 \
# 懂Python的朋友都知道Python把以两个或以上下划线字符开头且没有以两个或以上下划线结尾的变量当作私有变量。\
# 私有变量会在代码生成之前被转换为长格式（变为公有）。\
# 转换机制是这样的：在变量前端插入类名，再在前端加入一个下划线字符。\
# 这就是所谓的私有变量轧压（Private name mangling）。\
# 如类A里的__private标识符将被转换为_A__private，这就是上一节出现_A__private和__private消失的原因了。\
# 再讲两点题外话：\
# 一是因为轧压会使标识符变长，当超过255的时候，Python会切断，要注意因此引起的命名冲突。\
# 二是当类名全部以下划线命名的时候，Python就不再执行轧压。如：
#
#
#
# super(C, self).__init__()  <====> C.__init__(self)
#

#######################################################################################################################

class A(object):

    def __init__(self):
        self.__callPrivate()
        self.callPublic()

    def __callPrivate(self):
        print "A.__callPrivate() is called!"

    def callPublic(self):
        print "A.callPublic() method is called!"


class B(A):

    def __init__(self):
        super(A, self).__init__()
        print "B.__init__() method is called"

    def __callPrivate(self):
        print "B.__callPrivate() method is called!"

    def callPublic(self):
        print "B.callPublic() method is called!"

class C(A):

    def __init__(self):
#        super(C, self).__init__() # 注意，super（）第一个参数为当前类，以其寻找其父类，然后将self实例传给父函数，然后调用其父类的方法
        # 非绑定的类方法（用类名来引用的方法），并在参数列表中，引入待绑定的对象（self），从而达到调用父类的目的
#        A.__init__(self) # A._A__init__() ??? 怎末理解？？？
        self.__callPrivate()
        print "C.__init__() method is called"

    def __callPrivate(self):
        print "C.__callPrivate() method is called!"

    def callPublic(self):
        print "C.callPublic() method is called!"


if __name__ == '__main__':

    c = C()

    try:
        c.__callPrivate()  #Execution failed, because it's the private methods which only visible to the class,
                           # neither the instance of the class
    except AttributeError as error:
        print ('>>> Pls. check the attribute error: %s from %s' %(error, c.__class__))

    c.callPublic()