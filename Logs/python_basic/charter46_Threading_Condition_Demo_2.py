# -*- coding: utf-8 -*-
__author__ = 'k22li'

########################################################################################################################
# purpose:
# more explanations about "threading"
# answer:
#    3.4. Condition
#    Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，
#    否则它将自己生成一个RLock实例。
#
#    可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，
#    直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
#
#    构造方法：
#    Condition([lock/rlock])
#
#    实例方法：
#    acquire([timeout])/release(): 调用关联的锁的相应方法。
#    wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
#    notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；
#    其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
#    notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。
#    使用前线程必须已获得锁定，否则将抛出异常。
########################################################################################################################

import threading

class Seeker(threading.Thread):

    def __init__(self, con_1, con_2, name):

        super(Seeker, self).__init__()
        self.__con1 = con_1
        self.__con2 = con_2
        self.name = name

    def run(self):
        # 等待裁判宣布比赛开始
        self.__con1.acquire()
        self.__con1.wait()

        # 比赛开始后，作为比赛发起方开始比赛
        self.__con2.acquire()
        print ' '.join([self.name, ': 我已经把眼睛蒙上'])
        self.__con2.notify()
        self.__con2.wait()

        # 等待比赛对方的准备就绪，然后开始找
        print ' '.join([self.name, ': 我已经把你找到了'])
        self.__con2.notify()
        self.__con2.wait()

        # 找到了对方
        print ' '.join([self.name, '：我赢了'])
        self.__con2.release()

        # 通知裁判方比赛将要结束
        self.__con1.notify()
        self.__con1.release()

class Hider(threading.Thread):

    def __init__(self, con, name):

        super(Hider, self).__init__()
        self.__con = con
        self.name = name

    def run(self):
        self.__con.acquire()

        # 等待比赛对方准备就绪
        self.__con.wait()
        print ' '.join([self.name, ': 我已经藏好了，开始找吧'])

        # 通知对方我方已就绪
        self.__con.notify()
        self.__con.wait()

        # 比赛结束
        print ' '.join([self.name, ': 我被你找到了唉'])
        self.__con.notify()
        self.__con.release()

class Justice(threading.Thread):

    def __init__(self, con, name):
        super(Justice, self).__init__()
        self.__con =  con
        self.name = name

    def run(self):
        # 裁判宣布比赛开始
        self.__con.acquire()
        print ' '.join([self.name, ': 比赛开始...'])
        # 通知开始方，比赛开始进行
        self.__con.notify()
        # 等待被通知比赛结束
        self.__con.wait()
        print ' '.join([self.name, ': 比赛结束...'])
        self.__con.release()


########################################################################################################################
# test codes
########################################################################################################################
if __name__ == '__main__':

    # create two locks separately
    cond_1 = threading.Condition()
    cond_2 = threading.Condition()

    # create threads for each role
    hider = Hider(cond_2, 'kevin')
    seeker = Seeker(cond_1, cond_2, 'cathy')
    justice = Justice(cond_1, 'Micheal')

    # start the game
    hider.start()
    seeker.start()
    justice.start()
