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

thread_start()
print count