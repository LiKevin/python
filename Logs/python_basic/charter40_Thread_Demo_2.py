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

import sys
import thread, time

list_a = [0]*50000

def set_new_values_to_list(lst, ind, val):
    lst[ind] =  val

def set_new_values_to_list_with_lock(lst, ind, val, lck):
    with lck:
        lst[ind] =  val

def set_list(lst):
    for i in range(len(lst)):
        set_new_values_to_list(lst, i, '7')

def get_cur_values_from_list(lst, ind):
    sys.stdout.write(str(lst[ind])+'\t')

def get_list(lst):
    for i in range(len(lst)):
        get_cur_values_from_list(lst, i)
#        time.sleep(30)

def _test_thread_demo_without_lock(lst):

    for i in range(len(lst)):
        for j in range(3):
            thread.start_new(set_new_values_to_list, (lst, i, 1))
            thread.start_new(get_cur_values_from_list, (lst, i))
            time.sleep(0.01)


def _test_thread_demo_with_lock(lst):
    a_lock = thread.allocate_lock()

    with a_lock:    #fixme: 资源独享,要求等锁释放后以下的线程才能开始使用资源...
        for i in range(len(lst)):
            for j in range(3):
                thread.start_new(set_new_values_to_list, (lst, i, 1))

    #fixme: 等前面的写操作的所有线程结束后,以下的子线程才可以被执行
    for i in range(len(lst)):
        for j in range(3):
            thread.start_new(get_cur_values_from_list, (lst, i))
            time.sleep(0.001)

########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':

    # demo 1:  without locking, error came outs
#    _test_thread_demo_without_lock(list_a)

    _test_thread_demo_with_lock(list_a)
