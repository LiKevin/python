# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
#    Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。
#    可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。
#
#    构造方法：
#    Lock()
#
#    实例方法：
#    acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。
#    release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。
########################################################################################################################

# demo 1:  create a list with multi-threads via Lock
########################################################################################################################

import time
import threading

list_to_create = []
a_lock = threading.Lock()

def threadFunc(lst=None, arg='a'):

    if lst is None:
        lst = []

    print '>>> inside sub-threading: %s'%threading.currentThread().getName()
    with a_lock:
        for i in range(10):
            lst.append(arg)
            time.sleep(0.2)
    print '>>> leaving sub-threading: %s'%threading.currentThread().getName()

ta = threading.Thread(group=None, target=threadFunc, args=(list_to_create, 'a'))
tb = threading.Thread(group=None, target=threadFunc, args=(list_to_create, 'b'))
tc = threading.Thread(group=None, target=threadFunc, args=(list_to_create, 'c'))
td = threading.Thread(group=None, target=threadFunc, args=(list_to_create, 'd'))

ta.start()
tb.start()
tc.start()
td.start()

time.sleep(10) # wait till all those sub-threads done  -- main threads
print list_to_create

# outputs:
#
#    >>> inside sub-threading: Thread-1
#    >>> inside sub-threading: Thread-2
#    >>> inside sub-threading: Thread-3
#    >>> inside sub-threading: Thread-4
#    >>> leaving sub-threading: Thread-1
#    >>> leaving sub-threading: Thread-2
#    >>> leaving sub-threading: Thread-3
#    >>> leaving sub-threading: Thread-4
#    ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c',
#       'c', 'c', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']

# demo 2:  create a list with multi-threads without Locking
########################################################################################################################
list_to_create = []
def threadFuncWithoutLocking(lst=None, arg='a'):

    if lst is None:
        lst = []

    print '>>> inside sub-threading: %s'%threading.currentThread().getName()
#    with a_lock:   # check the outputs with the locking authorized.
    for i in range(10):
        lst.append(arg)
        time.sleep(0.2)
    print '>>> leaving sub-threading: %s'%threading.currentThread().getName()

# test codes
ta = threading.Thread(group=None, target=threadFuncWithoutLocking, args=(list_to_create, 'a'))
tb = threading.Thread(group=None, target=threadFuncWithoutLocking, args=(list_to_create, 'b'))
tc = threading.Thread(group=None, target=threadFuncWithoutLocking, args=(list_to_create, 'c'))
td = threading.Thread(group=None, target=threadFuncWithoutLocking, args=(list_to_create, 'd'))
# start threading
ta.start()
tb.start()
tc.start()
td.start()

time.sleep(10) # wait till all those sub-threads done  -- main threads
print list_to_create

# outputs:
#    >>> inside sub-threading: Thread-5
#    >>> inside sub-threading: Thread-6
#    >>> inside sub-threading: Thread-7
#    >>> inside sub-threading: Thread-8
#    >>> leaving sub-threading: Thread-5
#    >>> leaving sub-threading: Thread-7
#    >>> leaving sub-threading: Thread-6
#    >>> leaving sub-threading: Thread-8
#    ['a', 'b', 'c', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c',
#       'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'c', 'b', 'd', 'a', 'b', 'c', 'd']

########################################################################################################################
# diff join() & lock():
# fixme：  join()  主要应用场景为线程嵌入，子线程 获得优先权，等join（）的线程结束执行后父线程再恢复执行
# fixme:   lock（）主要应用于多个线程共享同一个数据资源的情况， 进行资源锁定
########################################################################################################################
