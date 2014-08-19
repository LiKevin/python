__author__ = 'k22li'

########################################################################################################################
# purpose:
# ways of factories implementations
########################################################################################################################


# demo 1
########################################################################################################################

import thread, time

count = 0

def threadTest():

    global count

    for i in xrange(1000):
        count += 1

def thread_start(thread_num=10):
    for i in range(thread_num):
        thread.start_new_thread(threadTest, ())
    time.sleep(3)


def threadFunction(a = None, b = None, c = None, d = None):

    print time.strftime('%H:%M:%S', time.localtime()), a
    time.sleep(1)
    print time.strftime('%H:%M:%S', time.localtime()), b
    time.sleep(1)
    print time.strftime('%H:%M:%S', time.localtime()), c
    time.sleep(1)
    print time.strftime('%H:%M:%S', time.localtime()), d
    time.sleep(1)
    print time.strftime('%H:%M:%S', time.localtime()), 'over!'

def _test_threadFunction():

    for i in range(4):
#        thread.start_new_thread(threadFunction, (3, 4, 5, 6))
        a_lock = thread.allocate_lock()

        with a_lock:
            print '>>> Inside thread lock...'
            thread.start_new(threadFunction, (1, 2, 3, 4))
            time.sleep(5)   # fixme:  mandatoru to have this interruptions, as ...
    #        thread.exit()  # fixme:  it's going to exit from the main thread, so non-of-following threads going to continue
        print '>>> Outside thread lock...'


if __name__ == '__main__':

    # demo 1
    ####################################################################################################################
#    thread_start()
#    print count

    _test_threadFunction()

