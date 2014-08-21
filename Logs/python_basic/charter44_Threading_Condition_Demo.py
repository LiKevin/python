# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# puropse:
#   try the "condition()" to pass by the locks within threads
#
#    fixme: condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，
#    fixme: 否则它将自己生成一个RLock实例。
#
#    fixme: 可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，
#    fixme: 直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
#
#    构造方法：
#    Condition([lock/rlock])
#
#    实例方法：
#    acquire([timeout])/release(): 调用关联的锁的相应方法。
#    wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
#    notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；
#    其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
#    notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。
#    使用前线程必须已获得锁定，否则将抛出异常。
########################################################################################################################

# demo 1: product & consuming pairs -- typical case
########################################################################################################################

import time
import threading

PRODUCT = None
con = threading.Condition()

def produce():
    global PRODUCT
    i = 5
    print '>>> product producing started ... '
    if con.acquire():
        while i:
            if PRODUCT is None:
                print '>>> producing ongoing ... %s' %str(i)
                PRODUCT = 'apple'
                con.notify()
#                con.wait()
                if i>1:
                    con.wait()
                else:
                    con.release()
            time.sleep(1)
            i -= 1

    print '>>> product producing completed ... '


def consume():
    global PRODUCT
    i = 5
    print '>>> product consuming started ... '
    if con.acquire():
        while i:
            if PRODUCT is not None:
                print '>>> consuming ongoing ... %s' %str(i)
                PRODUCT = None

                con.notify()
                if i>1:
                    con.wait()
                else:
                    con.release()
            time.sleep(1)
            i -= 1
    print '>>> product consuming completed ... '

def run():

    pro_thread = threading.Thread(target=produce)
    con_thread = threading.Thread(target=consume)

    pro_thread.start()
    con_thread.start()

    time.sleep(15)
    print pro_thread.getName(), pro_thread.isAlive()
    print con_thread.getName(), con_thread.isAlive()

########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':

    run()