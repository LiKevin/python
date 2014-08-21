# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
# more explanations about "threading"
# answer:
#    3.6. Event
#    fixme: Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，
#    fixme: 当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。
#
#    Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。
#
#    构造方法：
#    Event()
#
#    实例方法：
#    isSet(): 当内置标志为True时返回True。
#    set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
#    clear(): 将标志设为False。
#    wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。
########################################################################################################################

# demo 1:
########################################################################################################################

import threading
import time

class EventClass(threading.Thread):

    def __init__(self, event=None, name = ''):
        super(EventClass, self).__init__(name=name)
        self.__event = event

    def run(self):
        print '>>> %s wait for event happening ...' %threading.currentThread().getName()
        time.sleep(0.2)
        self.__event.wait()
        time.sleep(0.2)
        print '>>> %s recev event ... ' %threading.currentThread().getName()



########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':

    even = threading.Event()

    event_instance_1 = EventClass(even, 'kevin')
    event_instance_2 = EventClass(even, 'cathy')
    event_instance_3 = EventClass(even, 'micheal')

    print '>>> start all event threads from now ...'
    event_instance_1.start()
    event_instance_2.start()
    event_instance_3.start()

    time.sleep(3)
    print '>>> main thread set() the events, which really trigger all paused threads ...'
    even.set()  # set the state of the event, change it to "True"

    print '>>> check the state of the main thread: %s' %even.isSet()    # "True" state

    time.sleep(3)
    print '>>> main thread clear() all the event ... '
    even.clear()    # clear the state of the event, change it to "False"
    print '>>> check the state of the main thread again: %s' %even.isSet()      # "False" state