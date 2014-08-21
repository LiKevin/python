# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
# more explanations about "threading"
# answer:
# fixme: threading基于Java的线程模型设计。锁（Lock）和条件变量（Condition）在Java中是对象的基本行为（每一个对象都自带了锁和条件变量），
#    而在Python中则是独立的对象。Python Thread提供了Java Thread的行为的子集；没有优先级、线程组，线程也不能被停止、暂停、恢复、中断。
#    Java Thread中的部分被Python实现了的静态方法在threading中以模块方法的形式提供。
#
#    threading 模块提供的常用方法：
#    threading.currentThread(): 返回当前的线程变量。
#    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
#    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
#
#    threading模块提供的类：
#    Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local.
########################################################################################################################

# demo 1: 方法1：将要执行的方法作为参数传给Thread的构造方法：
########################################################################################################################

import threading

def threadFunc(name = 'kevin'):
    print '>>> func() is passed to thread for executing! --  author: %s' %(name)

t = threading.Thread(group=None, target=threadFunc, name='threading from function', args=('kevin',))
t.start()
#print ''    # this is important as the former print() function was called from the sub-threads, so it's "\n" may not be
            # well-formatted
print ">>> current thread name: %s" %(t.getName())


# demo 2: 方法2：从Thread继承，并重写run():
########################################################################################################################
class ThreadVirtuaClass(threading.Thread):
    '''
    构造方法：
        Thread(group=None, target=None, name=None, args=(), kwargs={})
        group: 线程组，目前还没有实现，库引用中提示必须是None；
        target: 要执行的方法；
        name: 线程名；
        args/kwargs: 要传入方法的参数。
    '''
    def __init__(self, name_2='threading from virtual class'):
        super(ThreadVirtuaClass, self).__init__(name=name_2)    # thread name is assigned when declaring
#        self.setName(name)

    def run(self):
        threadFunc(name='Cathy')
        print ">>> current thread name: %s" %(self.getName())   # self.getName to obtain the threading name

# make sure it's the Virtual class's instance is called to command the threading starts
ThreadVirtuaClass().start()


# demo 3:一个使用join()的例子
########################################################################################################################
#    实例方法：
#    isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。
#    get/setName(name): 获取/设置线程名。
#    is/setDaemon(bool): 获取/设置是否守护线程。初始值从创建该线程的线程继承。当没有非守护线程仍在运行时，程序将终止。
#    start(): 启动线程。
#    fixme: join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
########################################################################################################################

import time
#import threading  # already imported from above

def joinFunc():
    '''
    the embedded thread inside another thread
    '''
    print '>>> in sub-thread: joinFunc()'
    time.sleep(1)
    print '>>> out of sub-thread: joinFunc()'

def contextFunc(joinThread):
    '''
    the outer/ main thread whose inside another sub-thread going to execute
    '''
    print '### in main-thread: contextFunc()'
    # calling the embeded sub-thread
    joinThread.start()
    # fixme: authorize the embedded thread the authority to stub the main thread till the sub-thread completely done
    joinThread.join()

    # after the sub-thread done, then go back to this main thread
    print '### out of main-thread: contextFunc()'

#  test functions
join_thread = threading.Thread(group=None, target=joinFunc, args=())
context_thread =  threading.Thread(group=None, target=contextFunc, args=(join_thread,))
# start thread from the outer threads
context_thread.start()