__author__ = 'k22li'

import threading
import time

def worker():
    global ID
    print 'Thread one: %d' % ID
    ID += 1
    time.sleep(1)
#    print 'Thread two: %d' % ID
    return

threads = []
for i in xrange(10):
    ID = 1
    t = threading.Thread(target= worker)
    threads.append(t)
#    t.setDaemon(True)
    t.start()

print 'the end'
for item in threading.enumerate():
    print item