# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
## to demo the "Thread" calling...; and the locking mechanism
# 多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。考虑这样一种情况：
# 一个列表里所有元 素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。那么，可能线程"set"开始改的时候，
# 线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
#
# 锁有两种状态—— 锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；
# 如果已经有别的线程比如"print"获得锁定了，那么就让线程"set" 暂停，也就是同步阻塞；等到线程"print"访问完毕，
# 释放锁以后，再让线程"set"继续。经过这样的处理, 打印列表时要么全部输出0，要么全部输出 1，不会再出现一半0一半1的尴尬场面。
########################################################################################################################


import threading, time

count = 0

class Counter(threading.Thread):    # 对象继承自threading.Thread 基类，

    def __init__(self, lck, threadFunctionName):
        '''
        @summary: 初始化对象。
        @param lock: 琐对象。
        @param threadName: 线程名称。
        '''
        super(Counter, self).__init__(name=threadFunctionName)
        self.lock = lck

    def run(self):      # 重写Thread 类的run方法； 锁的应用情况应注入在这里
        '''
        @summary: 重写父类run方法，在线程启动后执行该方法内的代码。
        '''
        global count
        self.lock.acquire()
        for i in xrange(1000000000):
            count += 1
        self.lock.release()

########################################################################################################################
if __name__ == '__main__':

    lock = threading.Lock() # 实例一个线程锁，
    for i in range(5):  #  开启5个线程，开始计算
        Counter(lock, 'thread - '+str(i)).start()   # 通过start（）执行run（）方法
    time.sleep(0.5)
    print count