# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
# more explanations about "threading"
# answer:
#    Semaphore（信号量）是计算机科学史上最古老的同步指令之一。fixme: Semaphore管理一个内置的计数器，每当调用acquire()时-1，
#    fixme: 调用release() 时+1。计数器不能小于0；当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。
#
#    fixme: 基于这个特点，Semaphore经常用来同步一些有“访客上限”的对象，比如连接池。
#
#    fixme: BoundedSemaphore 与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值是否超过了计数器的初始值，
#    fixme: 如果超过了将抛出一个异常。
#
#    构造方法：
#    Semaphore(value=1): value是计数器的初始值。
#
#    实例方法：
#    acquire([timeout]): 请求Semaphore。如果计数器为0，将阻塞线程至同步阻塞状态；否则将计数器-1并立即返回。
#    release(): 释放Semaphore，将计数器+1，如果使用BoundedSemaphore，还将进行释放次数检查。release()方法不检查线程是否已获得Semaphore。
########################################################################################################################

import threading
import time

class SemaphoreClass(threading.Thread):

    def __init__(self, sema_con, name):
        super(SemaphoreClass, self).__init__(group=None, name=name)
        self.sema = sema_con

    def run(self):
        self.sema.acquire()
        print '>>> %s get semaphore ...'%threading.currentThread().getName()
        time.sleep(4)
        print '>>> %s release semaphore ...' %threading.currentThread().getName()
        self.sema.release()

########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':

    sema = threading.Semaphore(2)   # limited maximum agents who owning the thread lock...

    se_1 = SemaphoreClass(sema, 'kevin')
    se_2 = SemaphoreClass(sema, 'cathy')
    se_3 = SemaphoreClass(sema, 'micheal')
    se_4 = SemaphoreClass(sema, 'coco')

    se_1.start()
    se_2.start()
    se_3.start()
    se_4.start()

    time.sleep(10)
    print '>>> main thread releasing the semaphore without acquire... '
    sema.release()

