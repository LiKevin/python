# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# Purpose
#    3.8. local
#    local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个local，线程无法访问其他线程设置的属性；
#    线程设置的属性不会被其他线程设置的同名属性替换。
#
#    可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key检索对应的属性字典、再使用属性名作为key检索属性值的细节。
########################################################################################################################

import threading
import time

localConfig = threading.local()
localConfig.tname = 'main thread'

def localFunction():

    print '>>> inside the local function ... '
    print '>>> the current thread name is:  %s' %threading.currentThread().getName()
    localConfig.tname = 'sub-thread'
    print '>>> again the cur thread name after setting local variables: %s' %threading.currentThread().getName()
    print '>>> value of the localConfig.tname from the sub-thread: %s'%localConfig.tname


########################################################################################################################
# test code
########################################################################################################################

if __name__ == '__main__':

    threadInstance = threading.Thread(target=localFunction)
    threadInstance.start()
    time.sleep(15)
    print '>>> value of the localConfig.tname from the main thread: %s'%localConfig.tname

