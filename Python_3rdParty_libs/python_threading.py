__author__ = 'k22li'


import threading
import string, random

class TestClass():

    def __init__(self, name, loop):
        self.name = name
        self.loop = loop

    def printOut(self):

        print 'Name of the current method is: %s and the loop number is: %d' %(self.name, self.loop)

    def run(self):
        self.printOut()


if __name__ == '__main__':

#    for i in range(5):
    name = random.sample(string.letters, 4)
    loop = 2
    test1 = TestClass(name, loop)

    thread1 = threading.Thread(test1)
    thread1.start()