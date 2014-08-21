# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
#   test the 'Timer' class from the Thread...
#
#    3.7. Timer
#    fixme: Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。
#
#    构造方法：
#    fixme: Timer(interval, function, args=[], kwargs={})
#    @interval: 指定的时间
#    @function: 要执行的方法
#    @args/kwargs: 方法的参数
#
#    实例方法：
#    Timer从Thread派生，没有增加实例方法。
########################################################################################################################

import threading

def timerFunc():

    print '>>> Hello, this is from Timer! -- by: %s' %threading.currentThread().getName()

t1 = threading.Timer(interval=2, function=timerFunc)
t2 = threading.Timer(interval=2, function=timerFunc)
t3 = threading.Timer(interval=1, function=timerFunc)

t1.start()
t2.start()
t3.start()
