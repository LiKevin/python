#-*- encoding: gb2312 -*-
import string, threading, time

def thread_main(a):
    global count, mutex
    # ����߳���
    threadname = threading.currentThread().getName()

    for x in xrange(0, int(a)):
        # ȡ����
        mutex.acquire()
        count = count + 1
        # �ͷ���
        mutex.release()
        print threadname, x, count
        time.sleep(1)

def main(num):
    global count, mutex
    threads = []

    count = 1
    # ����һ����
    mutex = threading.Lock()
    # �ȴ����̶߳���
    for x in xrange(0, num):
        threads.append(threading.Thread(target=thread_main, args=(10,)))
        # ���������߳�
    for t in threads:
        t.start()
        # ���߳��еȴ��������߳��˳�
    for t in threads:
        t.join()


if __name__ == '__main__':
    num = 4
    # ����4���߳�
    main(num)
