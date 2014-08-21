# -*- coding:  utf-8 -*-
__author__ = 'k22li'
########################################################################################################################
# purpose:
# try to verify what's the time.sleep() blocks, either the "thread" or the "process"?
# answer:
# fixme: It blocks the thread. If you look in Modules/timemodule.c in the Python source, you'll see that in the call
# fixme: to floatsleep(), the substantive part of the sleep operation is wrapped in a Py_BEGIN_ALLOW_THREADS and
# fixme: Py_END_ALLOW_THREADS block, allowing other threads to continue to execute while the current one sleeps.
# fixme: You can also test this with a simple python program
########################################################################################################################

import time
import threading
#from threading import Thread

class Worker(threading.Thread):

    def run(self):
        for i in range(1, 5):
            print i
            print '>>> go to sleep from worker <<<'
            time.sleep(1)
            print '>>> go to wake from worker <<<'

class Farmer(threading.Thread):

    def run(self):
        for i in range(100, 105):
            print i
            print '>>> go to sleep from farmer <<<'
            time.sleep(0.5)
            print '>>> go to wake from farmer <<<'

def run():
    Worker().start()
    Farmer().start()
    print "\n## %s ##" %str(threading.enumerate())
    print "\n## %s ##" %str(threading.activeCount())
    print "\n## %s ##" %str(threading.currentThread())


if __name__ == '__main__':

    run()

# outputs:
#    1
#    >>> go to sleep from worker <<<
#    100
#
#    >>> go to sleep from farmer <<<
#    >>> go to wake from farmer <<<
#    101
#    >>> go to sleep from farmer <<<
#    >>> go to wake from farmer <<<
#    102
#    >>> go to sleep from farmer <<<
#    >>> go to wake from worker <<<
#    2
#    >>> go to sleep from worker <<<
#    >>> go to wake from farmer <<<
#    103
#    >>> go to sleep from farmer <<<
#    >>> go to wake from farmer <<<
#    104
#    >>> go to sleep from farmer <<<
#    >>> go to wake from worker <<<
#    3
#    >>> go to sleep from worker <<<
#    >>> go to wake from farmer <<<
#    >>> go to wake from worker <<<
#    4
#    >>> go to sleep from worker <<<
#    >>> go to wake from worker <<<